"""Contained files and crash-safe sidecar writes; never overwrite originals."""

from __future__ import annotations

import os
import re
from pathlib import Path, PurePosixPath
from typing import Final
from uuid import uuid4

from .models import StudioError

MAX_FILE_BYTES: Final = 64 * 1024 * 1024


def validate_id(value: str) -> str:
    if re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", value) is None:
        raise StudioError("invalid_id", "Expected a portable lowercase identifier")
    return value


def safe_path(root: Path, relative: str) -> Path:
    parts = PurePosixPath(relative)
    if (
        parts.is_absolute()
        or not parts.parts
        or any(part in {"", ".", ".."} for part in relative.split("/"))
        or "\\" in relative
        or ":" in relative
    ):
        raise StudioError("unsafe_path", "Expected a contained workspace-relative path")
    target = root
    for part in parts.parts:
        target = target / part
        if target.is_symlink():
            raise StudioError("unsafe_path", "Managed paths cannot contain symlinks")
    if not target.resolve().is_relative_to(root):
        raise StudioError("unsafe_path", "Path escapes the workspace")
    return target


def read_file(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise StudioError("invalid_file", f"Expected a regular non-symlink file: {path}")
    with path.open("rb") as stream:
        data = stream.read(MAX_FILE_BYTES + 1)
    if len(data) > MAX_FILE_BYTES:
        raise StudioError("invalid_file", "File exceeds the 64 MiB bound")
    return data


def write_new(path: Path, data: bytes) -> None:
    with path.open("xb") as stream:
        _ = stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def immutable_file(path: Path, data: bytes) -> None:
    if path.exists():
        if read_file(path) != data:
            raise StudioError("conflict", f"Existing file differs: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    write_new(path, data)


def atomic_write(path: Path, data: bytes) -> None:
    temporary = path.with_name(f".core-{uuid4().hex}.tmp")
    try:
        write_new(temporary, data)
        if path.is_symlink():
            raise StudioError("unsafe_path", "Sidecar cannot be a symlink")
        _ = temporary.replace(path)
        descriptor = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    finally:
        temporary.unlink(missing_ok=True)
