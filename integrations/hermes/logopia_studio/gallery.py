"""Offline publication entry point; canonical workflow selection is read-only."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from .gallery_delivery import delivery_files
from .gallery_files import GalleryFile, candidate_files, write_publication
from .gallery_render import render_gallery
from .gallery_review import review_labels
from .models import StudioError

if TYPE_CHECKING:
    from .models import Workflow


def publish_gallery(workspace: Path, state: Workflow, output: Path) -> Path:
    """Publish an independent snapshot into an unused directory and return its index."""
    if output.exists() or output.is_symlink():
        raise StudioError(
            "gallery_output", "Publication directory already exists; use a fresh path"
        )
    files = (*candidate_files(workspace, state), *delivery_files(workspace, state))
    snapshot = GalleryFile(Path("workflow.json"), state.model_dump_json(indent=2).encode("utf-8"))
    index = GalleryFile(
        Path("index.html"),
        render_gallery(state, review_labels(workspace, state), files).encode("utf-8"),
    )
    return write_publication(output, (*files, snapshot, index))
