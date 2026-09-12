"""Exclusive gallery publication with cleanup limited to this invocation's files."""

from __future__ import annotations

import errno
import os
from contextlib import ExitStack
from stat import S_ISDIR
from typing import TYPE_CHECKING

from logo_helper.models import ProjectError

if TYPE_CHECKING:
    from pathlib import Path


def _remove_owned(path: Path, device: int, inode: int) -> None:
    try:
        current = path.lstat()
        if (current.st_dev, current.st_ino) != (device, inode):
            return
        if S_ISDIR(current.st_mode):
            path.rmdir()
        else:
            path.unlink()
    except FileNotFoundError:
        return
    except OSError as error:
        if error.errno not in {errno.ENOTEMPTY, errno.EEXIST}:
            raise


def _own(rollback: ExitStack, path: Path) -> None:
    identity = path.lstat()
    _ = rollback.callback(_remove_owned, path, identity.st_dev, identity.st_ino)


def publish_gallery(staging: Path, destination: Path) -> None:
    """Write the index last; roll back owned entries even on a keyboard interruption."""
    try:
        destination.mkdir()
    except FileExistsError as error:
        raise ProjectError("conflict", "Gallery destination already exists") from error
    with ExitStack() as rollback:
        _own(rollback, destination)
        for name in ("images", "prompts"):
            folder = destination / name
            folder.mkdir()
            _own(rollback, folder)
        sources = (
            *sorted((staging / "images").iterdir()),
            *sorted((staging / "prompts").iterdir()),
            staging / "manifest.json",
            staging / "index.html",
        )
        for source in sources:
            target = destination / source.relative_to(staging)
            os.link(source, target)
            _own(rollback, target)
        _ = rollback.pop_all()
