"""Workspace containment, immutable files, atomic JSON, and cooperative update locks."""

from __future__ import annotations

import hashlib
import os
import re
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Final, assert_never
from uuid import uuid4

from logo_helper.images import inspect_png
from logo_helper.legacy_state import LegacySession, parse_session, parse_stored_session
from logo_helper.models import ProjectError, Session, SessionId

if TYPE_CHECKING:
    from collections.abc import Generator

MAX_FILE_BYTES: Final = 64 * 1024 * 1024


def validate_id(value: str) -> str:
    """Only portable lowercase IDs can become directory or artifact names."""
    if re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", value) is None:
        raise ProjectError(
            "invalid_id", "Use 1-64 lowercase letters, digits, underscores or hyphens"
        )
    return value


def safe_path(root: Path, relative: str) -> Path:
    """Reject lexical escapes and every symlink below the trusted workspace root."""
    part = PurePosixPath(relative)
    if (
        part.is_absolute()
        or not part.parts
        or any(p in {"..", "."} for p in relative.split("/"))
        or "\\" in relative
        or ":" in relative
    ):
        raise ProjectError("unsafe_path", "Paths must remain relative to the workspace")
    target = root
    for component in part.parts:
        target = target / component
        if target.is_symlink():
            raise ProjectError(
                "unsafe_path", f"Symlink is not allowed in managed storage: {target}"
            )
    if not target.resolve().is_relative_to(root):
        raise ProjectError("unsafe_path", "Resolved path leaves the workspace")
    return target


def read_source(path: Path) -> bytes:
    """Read a bounded regular file; reject symlink leaf inputs and special files."""
    if path.is_symlink() or not path.is_file():
        raise ProjectError("invalid_file", f"Expected a regular non-symlink file: {path}")
    with path.open("rb") as stream:
        data = stream.read(MAX_FILE_BYTES + 1)
    if len(data) > MAX_FILE_BYTES:
        raise ProjectError("invalid_file", "Input exceeds the 64 MiB size limit")
    return data


def write_new(path: Path, data: bytes) -> None:
    """Create a file exclusively so a collision cannot overwrite user data."""
    created = False
    try:
        with path.open("xb") as stream:
            created = True
            _ = stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except OSError:
        if created:
            path.unlink()
        raise


def atomic_state(path: Path, state: Session) -> None:
    """Replace a fully flushed JSON file within the same locked session directory."""
    temporary = path.with_name(f".state-{uuid4().hex}.tmp")
    try:
        write_new(temporary, (state.model_dump_json(indent=2) + "\n").encode("utf-8"))
        if path.is_symlink():
            raise ProjectError("unsafe_path", "Session JSON cannot be a symlink")
        _ = temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


@dataclass(frozen=True, slots=True)
class Store:
    """Access one canonical workspace; mkdir locks are cross-platform and fail fast."""

    root: Path

    @classmethod
    def at(cls, workspace: Path) -> Store:
        """Treat the caller-selected workspace as the trust root, resolving OS aliases."""
        root = workspace.resolve(strict=True)
        if not root.is_dir():
            raise ProjectError("invalid_workspace", "Workspace must be an existing directory")
        return cls(root)

    def session_dir(self, identifier: SessionId) -> Path:
        return safe_path(self.root, f".logo-generator/sessions/{validate_id(identifier)}")

    @contextmanager
    def locked(self, identifier: SessionId) -> Generator[None]:
        """Fail on another writer; never steal or silently remove an abandoned lock."""
        _ = validate_id(identifier)
        locks = safe_path(self.root, ".logo-generator/locks")
        locks.mkdir(parents=True, exist_ok=True)
        lock = safe_path(self.root, f".logo-generator/locks/{identifier}.lock")
        try:
            lock.mkdir()
        except FileExistsError as error:
            raise ProjectError(
                "locked", f"Session locked; inspect running writers before removing {lock}"
            ) from error
        try:
            yield
        finally:
            lock.rmdir()

    def load(self, identifier: SessionId) -> Session:
        """Reparse persisted state and verify all artifact bytes on every resume."""
        directory = self.session_dir(identifier)
        path = safe_path(directory, "session.json")
        state = parse_session(read_source(path))
        if state.id != identifier:
            raise ProjectError("invalid_state", "Stored session ID differs from its directory")
        for artifact in state.artifacts:
            data = read_source(safe_path(directory, artifact.path))
            if hashlib.sha256(data).hexdigest() != artifact.sha256:
                raise ProjectError(
                    "hash_mismatch", f"Artifact {artifact.id} changed; restore its original file"
                )
            if inspect_png(data) != artifact.image:
                raise ProjectError(
                    "invalid_state", f"Artifact {artifact.id} metadata differs from decoded PNG"
                )
        for reference in state.references:
            data = read_source(safe_path(directory, reference.path))
            if hashlib.sha256(data).hexdigest() != reference.sha256:
                raise ProjectError("hash_mismatch", f"Reference {reference.id} changed")
        return state

    def expect(self, identifier: SessionId, revision: int) -> Session:
        state = self.load(identifier)
        if state.revision != revision:
            raise ProjectError(
                "stale_revision",
                f"Expected revision {revision}; current revision is {state.revision}",
            )
        return state

    def save(self, state: Session) -> None:
        """Commit validated v2 state; preserve immutable history and first v1 bytes."""
        verified = Session.model_validate_json(state.model_dump_json())
        directory = self.session_dir(verified.id)
        path = safe_path(directory, "session.json")
        if path.exists():
            original = read_source(path)
            previous = parse_session(original)
            previous_artifacts = tuple(
                artifact.model_copy(update={"review": None, "reviewed_at": None})
                for artifact in previous.artifacts
            )
            current_artifacts = tuple(
                artifact.model_copy(update={"review": None, "reviewed_at": None})
                for artifact in verified.artifacts[: len(previous.artifacts)]
            )
            for old, new in (
                (previous.palettes, verified.palettes),
                (previous.references, verified.references),
                (previous.color_reports, verified.color_reports),
                (previous_artifacts, current_artifacts),
            ):
                if new[: len(old)] != old:
                    raise ProjectError(
                        "immutable_history", "Saved provenance and color history are immutable"
                    )
            stored = parse_stored_session(original)
            match stored:
                case LegacySession():
                    backup = safe_path(directory, "session.v1.backup.json")
                    if not backup.exists():
                        write_new(backup, original)
                    if read_source(backup) != original:
                        raise ProjectError(
                            "backup_conflict", "Legacy backup differs from session bytes"
                        )
                case Session():
                    pass
                case _:
                    assert_never(stored)
        atomic_state(path, verified)

    def list_sessions(self) -> tuple[Session, ...]:
        directory = safe_path(self.root, ".logo-generator/sessions")
        if not directory.exists():
            return ()
        return tuple(self.load(SessionId(path.name)) for path in sorted(directory.iterdir()))
