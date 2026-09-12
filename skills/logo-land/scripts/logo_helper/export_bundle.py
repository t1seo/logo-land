"""Publish immutable delivery files and roll them back if the state commit fails."""

from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING
from zipfile import ZIP_DEFLATED, ZipFile

from logo_helper.storage import write_new

if TYPE_CHECKING:
    from collections.abc import Generator


@contextmanager
def publish_bundle(
    destination: Path,
    image: bytes,
    manifest: bytes,
    guide: bytes,
) -> Generator[None]:
    """Yield for the state commit, retaining files only after that commit succeeds."""
    missing: list[Path] = []
    parent = destination.parent
    while not parent.exists():
        missing.append(parent)
        parent = parent.parent
    created: list[Path] = []
    published: list[Path] = []
    committed = False
    try:
        for directory in reversed(missing):
            directory.mkdir()
            created.append(directory)
        with TemporaryDirectory(prefix=".logo-export-", dir=destination.parent) as temporary:
            staging = Path(temporary)
            write_new(staging / "logo.png", image)
            write_new(staging / "manifest.json", manifest)
            write_new(staging / "brand-guide.md", guide)
            with ZipFile(staging / "logo-package.zip", "x", compression=ZIP_DEFLATED) as archive:
                for name in ("logo.png", "manifest.json", "brand-guide.md"):
                    archive.write(staging / name, name)
            destination.mkdir()
            created.append(destination)
            for file in staging.iterdir():
                target = destination / file.name
                os.link(file, target)
                published.append(target)
            yield
            committed = True
    finally:
        if not committed:
            for file in published:
                file.unlink()
            for directory in reversed(created):
                directory.rmdir()
