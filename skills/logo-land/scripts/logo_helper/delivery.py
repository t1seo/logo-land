"""Export a reviewed original PNG with truthful provenance and a matching ZIP."""

from __future__ import annotations

import hashlib
import os
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Literal
from zipfile import ZIP_DEFLATED, ZipFile

from logo_helper.models import (
    Artifact,
    Background,
    Brief,
    ExportRecord,
    FrozenModel,
    ProjectError,
    Session,
    SessionId,
)
from logo_helper.storage import Store, read_source, safe_path, write_new
from logo_helper.workflow import advance


class Manifest(FrozenModel):
    """Describe the actual exported artifact without promising vector or legal rights."""

    schema_version: Literal[1] = 1
    session_id: SessionId
    revision: int
    exported_at: datetime
    image_file: Literal["logo.png"] = "logo.png"
    source: Artifact
    brief: Brief
    media_kind: Literal["raster"] = "raster"
    requested_background: Background
    transparency_verified: bool


def guide(state: Session, artifact: Artifact) -> str:
    """Separate requested brand choices from measured PNG facts and host review."""
    brief = state.brief
    selected_request = "\n".join(f"> {line}" for line in artifact.prompt.splitlines())
    return (
        f"# {brief.brand_name}\n\n"
        f"Selected artifact: {artifact.id}\n\n"
        f"Initial brief text: {brief.exact_text}\n\nInitial brief slogan: {brief.slogan}\n\n"
        f"Initial brief styles: {', '.join(brief.styles)}\n\n"
        "Initial brief palette (historical intent, not measured or final color specifications): "
        f"{', '.join(brief.palette)}\n\n"
        f"Initial brief background (historical intent): {brief.background}\n\n"
        f"Selected artifact requested background: {artifact.effective_background(brief)}\n\n"
        f"Intended uses: {', '.join(brief.use_cases)}\n\n"
        f"Actual deliverable: PNG raster, "
        f"{artifact.image.width} x {artifact.image.height} pixels.\n\n"
        f"Pixels below full opacity: {artifact.image.transparent_pixels}. "
        f"Visible pixels: {artifact.image.visible_pixels}.\n\n"
        "The original bytes are preserved. Do not enlarge beyond a useful raster resolution. "
        "Keep clear space around the mark and verify legibility at its final display size.\n\n"
        "This package does not include editable SVG/EPS/AI vectors, licensed font files, "
        "CMYK print proofs, or trademark/exclusivity guarantees. "
        "Initial colors and styles describe historical intent; the supplied PNG is the actual "
        "artwork. The selected version request is authoritative for changes to the initial brief. "
        "The manifest records the explicit visual review and generation/edit prompt.\n\n"
        "## Selected version request\n\n"
        f"{selected_request}\n"
    )


def _export_destination(root: Path, relative: str) -> Path:
    destination = safe_path(root, relative)
    if destination.relative_to(root).parts[0].casefold() == ".logo-generator":
        raise ProjectError(
            "reserved_output",
            "Export destination cannot be inside reserved .logo-generator storage",
        )
    return destination


def export(store: Store, identifier: SessionId, revision: int, output: str | None) -> Session:
    """Stage a complete bundle before publishing it to a new workspace directory."""
    relative = output if output is not None else f"output/logo-generator/{identifier}"
    destination = _export_destination(store.root, relative)
    with store.locked(identifier):
        state = store.expect(identifier, revision)
        if state.selected_id is None:
            raise ProjectError("not_selected", "Select an artifact before export")
        artifact = state.artifact(state.selected_id)
        if artifact.review is None or not artifact.review.passed:
            raise ProjectError("review_required", "All explicit visual review checks must pass")
        requested_background = artifact.effective_background(state.brief)
        requested_transparency = requested_background == "transparent"
        if requested_transparency != artifact.image.has_transparency:
            detail = (
                f"Requested {requested_background} background differs from decoded transparency "
                f"({artifact.image.has_transparency})"
            )
            raise ProjectError(
                "background_mismatch",
                detail,
            )
        if destination.exists():
            raise ProjectError("conflict", f"Export destination already exists: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        data = read_source(safe_path(store.session_dir(identifier), artifact.path))
        if hashlib.sha256(data).hexdigest() != artifact.sha256:
            raise ProjectError("hash_mismatch", "Selected image changed during export")
        now = datetime.now(UTC)
        record = ExportRecord(path=relative, artifact_id=artifact.id, created_at=now)
        updated = advance(state.model_copy(update={"exports": (*state.exports, record)}))
        manifest = Manifest(
            session_id=identifier,
            revision=updated.revision,
            exported_at=now,
            source=artifact,
            brief=state.brief,
            requested_background=requested_background,
            transparency_verified=artifact.image.has_transparency,
        )
        with TemporaryDirectory(prefix=".logo-export-", dir=destination.parent) as temporary:
            staging = Path(temporary) / "bundle"
            staging.mkdir()
            write_new(staging / "logo.png", data)
            write_new(staging / "manifest.json", manifest.model_dump_json(indent=2).encode("utf-8"))
            write_new(staging / "brand-guide.md", guide(state, artifact).encode("utf-8"))
            with ZipFile(staging / "logo-package.zip", "x", compression=ZIP_DEFLATED) as archive:
                for name in ("logo.png", "manifest.json", "brand-guide.md"):
                    archive.write(staging / name, name)
            destination.mkdir()
            published: list[Path] = []
            try:
                for file in staging.iterdir():
                    target = destination / file.name
                    os.link(file, target)
                    published.append(target)
                store.save(updated)
            except (OSError, ProjectError):
                for file in published:
                    file.unlink()
                destination.rmdir()
                raise
    return updated
