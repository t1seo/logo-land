"""Short advisory locks, optimistic revisions and validated workflow snapshots."""

from __future__ import annotations

import fcntl
from contextlib import contextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING

from pydantic import ValidationError

from .models import Job, StudioError, Workflow
from .store_files import atomic_write, read_file, safe_path, validate_id

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path


@dataclass(frozen=True, slots=True)
class Store:
    """Atomic sidecars with process-released advisory locks."""

    root: Path

    def path(self, workflow_id: str) -> Path:
        return safe_path(
            self.root, f".logo-generator/workflows/{validate_id(workflow_id)}/workflow.json"
        )

    @contextmanager
    def locked(self, workflow_id: str) -> Generator[None]:
        directory = safe_path(self.root, ".logo-generator/workflow-locks")
        directory.mkdir(parents=True, exist_ok=True)
        path = safe_path(directory, f"{validate_id(workflow_id)}.lock")
        with path.open("a+b") as stream:
            try:
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                raise StudioError("locked", "Another workflow writer is committing") from error
            try:
                yield
            finally:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)

    def load(self, workflow_id: str) -> Workflow:
        path = self.path(workflow_id)
        if not path.exists():
            raise StudioError("not_found", f"Workflow {workflow_id} does not exist")
        try:
            state = Workflow.model_validate_json(read_file(path))
        except ValidationError as error:
            raise StudioError("invalid_state", str(error)) from error
        if state.id != workflow_id:
            raise StudioError("invalid_state", "Stored ID differs from directory")
        return state

    def expect(self, workflow_id: str, revision: int) -> Workflow:
        if type(revision) is not int or revision < 0:
            raise StudioError("invalid_revision", "Revision must be a nonnegative integer")
        state = self.load(workflow_id)
        if state.revision != revision:
            raise StudioError("stale_revision", f"Expected {revision}; current {state.revision}")
        return state

    def save(self, state: Workflow) -> Workflow:
        verified = Workflow.model_validate_json(state.model_dump_json())
        path = self.path(verified.id)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            previous = self.load(state.id)
            if previous.brief != verified.brief or verified.revision != previous.revision + 1:
                raise StudioError(
                    "invalid_state", "Intent is immutable; revision must advance once"
                )
            if verified.jobs[: len(previous.jobs)] and tuple(
                job.id for job in verified.jobs[: len(previous.jobs)]
            ) != tuple(job.id for job in previous.jobs):
                raise StudioError(
                    "immutable_history", "Attempt history cannot be removed or reordered"
                )
            for old_job, new_job in zip(previous.jobs, verified.jobs, strict=False):
                _verify_job_history(old_job, new_job)
            if len(verified.jobs) < len(previous.jobs):
                raise StudioError("immutable_history", "Attempt counters cannot reset")
            for old, new in zip(previous.candidates, verified.candidates, strict=False):
                if old.model_copy(update={"critiques": ()}) != new.model_copy(
                    update={"critiques": ()}
                ):
                    raise StudioError("immutable_history", "Canonical candidates cannot change")
            if len(verified.candidates) < len(previous.candidates):
                raise StudioError("immutable_history", "Canonical candidates cannot be removed")
        atomic_write(path, (verified.model_dump_json(indent=2) + "\n").encode())
        return verified


def _job_request(job: Job) -> Job:
    return job.model_copy(
        update={
            "status": "reserved",
            "generated": None,
            "image_sha256": None,
            "plan": None,
            "critiques": (),
            "raw_reports": (),
            "error": None,
        }
    )


def _verify_job_history(old: Job, new: Job) -> None:
    if _job_request(old) != _job_request(new):
        raise StudioError("immutable_history", "Reserved request identity cannot change")
    if old.status == "succeeded" and old != new:
        raise StudioError("immutable_history", "Completed attempt cannot be rewritten")
    if old.generated is not None and old.generated != new.generated:
        raise StudioError("immutable_history", "Recorded native receipt cannot change")
    if old.image_sha256 is not None and old.image_sha256 != new.image_sha256:
        raise StudioError("immutable_history", "Recorded native image hash cannot change")
    if new.raw_reports[: len(old.raw_reports)] != old.raw_reports:
        raise StudioError("immutable_history", "Raw report history cannot be removed or rewritten")
