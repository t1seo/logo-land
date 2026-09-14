"""Verify canonical bytes and exclusively write owned publication files."""

from __future__ import annotations

import errno
import os
from dataclasses import dataclass
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, Final

from PIL import Image, UnidentifiedImageError

from .models import StudioError

if TYPE_CHECKING:
    from .models import Candidate, Workflow

MAX_PIXELS: Final = 32_000_000


@dataclass(frozen=True, slots=True)
class GalleryFile:
    """One verified payload relative to its exclusively owned publication."""

    path: Path
    data: bytes


def original_bytes(workspace: Path, candidate: Candidate) -> bytes:
    root = workspace.resolve()
    path = root / candidate.image_path
    resolved = path.resolve()
    if not resolved.is_relative_to(root) or path.is_symlink():
        raise StudioError("gallery_source", f"Original path is not canonical: {candidate.id}")
    try:
        if not path.is_file() or path.stat().st_size > 64 * 1024 * 1024:
            raise StudioError("gallery_source", f"Original missing or too large: {candidate.id}")
        data = path.read_bytes()
        if sha256(data).hexdigest() != candidate.sha256:
            raise StudioError("gallery_source", f"Original changed: {candidate.id}")
        with Image.open(BytesIO(data)) as image:
            if image.format != "PNG" or image.size != (candidate.width, candidate.height):
                raise StudioError(
                    "gallery_source", f"Original PNG dimensions differ: {candidate.id}"
                )
            if image.width * image.height > MAX_PIXELS:
                raise StudioError("gallery_source", f"Original exceeds pixel limit: {candidate.id}")
            image.verify()
        with Image.open(BytesIO(data)) as image:
            _ = image.load()
    except (OSError, UnidentifiedImageError, SyntaxError, Image.DecompressionBombError) as error:
        raise StudioError("gallery_source", f"Cannot decode original: {candidate.id}") from error
    return data


def candidate_files(workspace: Path, state: Workflow) -> tuple[GalleryFile, ...]:
    files: list[GalleryFile] = []
    for candidate in state.candidates:
        data = original_bytes(workspace, candidate)
        prompt = candidate.prompt.encode("utf-8")
        files.extend(
            (
                GalleryFile(Path("originals") / f"{candidate.id}.png", data),
                GalleryFile(Path("prompts") / f"{candidate.id}.txt", prompt),
                GalleryFile(
                    Path("prompts") / f"{candidate.id}.txt.sha256",
                    (sha256(prompt).hexdigest() + "\n").encode(),
                ),
            )
        )
    return tuple(files)


def _remove_empty(path: Path) -> None:
    try:
        path.rmdir()
    except OSError as error:
        if error.errno not in {errno.ENOTEMPTY, errno.ENOENT, errno.EEXIST}:
            raise


def _rollback(owned: list[tuple[Path, int, int, bytes]], directories: list[Path]) -> None:
    for path, device, inode, expected in reversed(owned):
        if path.is_symlink() or not path.is_file():
            continue
        stat = path.stat()
        if (stat.st_dev, stat.st_ino) == (device, inode):
            actual = path.read_bytes()
            if expected.startswith(actual):
                path.unlink()
    for directory in reversed(directories):
        _remove_empty(directory)


def write_publication(output: Path, files: tuple[GalleryFile, ...]) -> Path:
    """Reserve a fresh directory; rollback never recursively deletes foreign data."""
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.mkdir()
    except OSError as error:
        raise StudioError(
            "gallery_output", "Choose a fresh, writable publication directory"
        ) from error
    owned: list[tuple[Path, int, int, bytes]] = []
    directories = [output]
    complete = False
    try:
        for item in files:
            path = output / item.path
            if path.parent != output and path.parent not in directories:
                path.parent.mkdir()
                directories.append(path.parent)
            with path.open("xb") as stream:
                stat = os.fstat(stream.fileno())
                owned.append((path, stat.st_dev, stat.st_ino, item.data))
                _ = stream.write(item.data)
                stream.flush()
                os.fsync(stream.fileno())
            if path.read_bytes() != item.data:
                raise StudioError("gallery_output", "Publication bytes changed during writing")
        complete = True
    except OSError as error:
        raise StudioError(
            "gallery_output", "Publication failed; existing foreign data was preserved"
        ) from error
    finally:
        if not complete:
            _rollback(owned, directories)
    return output / "index.html"
