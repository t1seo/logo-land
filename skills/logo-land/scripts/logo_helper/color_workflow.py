"""Locked append-only palette, reference and measurement session transactions."""

from __future__ import annotations

import hashlib
from datetime import UTC, datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from pydantic import ValidationError

from logo_helper.color_analysis import analyze_png
from logo_helper.models import (
    ArtifactId,
    PaletteContent,
    PaletteId,
    PaletteVersion,
    ProjectError,
    Reference,
    ReferenceId,
    RegionOfInterest,
    ReportId,
    Session,
    SessionId,
    palette_digest,
)
from logo_helper.reference_evidence import verify_reference_evidence
from logo_helper.references import inspect_reference
from logo_helper.storage import Store, read_source, safe_path, validate_id, write_new
from logo_helper.workflow import advance

if TYPE_CHECKING:
    from pathlib import Path


def add_reference(
    store: Store,
    identifier: SessionId,
    revision: int,
    *,
    reference_id: ReferenceId,
    image: Path,
    roi: RegionOfInterest | None = None,
) -> Session:
    _ = validate_id(reference_id)
    data = read_source(image)
    facts = inspect_reference(data, roi=roi)
    with store.locked(identifier):
        state = store.expect(identifier, revision)
        if any(item.id == reference_id for item in state.references):
            raise ProjectError("conflict", f"Reference {reference_id} already exists")
        extension = "png" if facts.format == "PNG" else "jpg"
        reference = Reference(
            id=reference_id,
            path=f"references/{reference_id}.{extension}",
            sha256=hashlib.sha256(data).hexdigest(),
            format=facts.format,
            width=facts.width,
            height=facts.height,
            exif_orientation=facts.exif_orientation,
            roi=roi,
            created_at=datetime.now(UTC),
        )
        updated = advance(state.model_copy(update={"references": (*state.references, reference)}))
        updated = Session.model_validate_json(updated.model_dump_json())
        directory = store.session_dir(identifier)
        safe_path(directory, "references").mkdir(exist_ok=True)
        destination = safe_path(directory, reference.path)
        write_new(destination, data)
        try:
            store.save(updated)
        except (OSError, ProjectError, ValidationError):
            destination.unlink()
            raise
    return updated


def add_palette(
    store: Store,
    identifier: SessionId,
    revision: int,
    *,
    palette_id: PaletteId,
    content: PaletteContent,
    parent_palette_id: PaletteId | None = None,
) -> Session:
    _ = validate_id(palette_id)
    with store.locked(identifier):
        state = store.expect(identifier, revision)
        if any(item.id == palette_id for item in state.palettes):
            raise ProjectError("conflict", f"Palette {palette_id} already exists")
        if parent_palette_id is not None:
            _ = state.palette(parent_palette_id)
        verify_reference_evidence(store, state, content)
        palette = PaletteVersion(
            id=palette_id,
            parent_palette_id=parent_palette_id,
            digest=palette_digest(content),
            swatches=content.swatches,
            constraints=content.constraints,
            source=content.source,
            source_evidence=content.source_evidence,
            selected_by=content.selected_by,
            rationale=content.rationale,
            calculation_version=content.calculation_version,
        )
        updated = advance(
            state.model_copy(
                update={
                    "palettes": (*state.palettes, palette),
                    "active_palette_id": palette.id,
                }
            )
        )
        store.save(updated)
    return updated


def analyze_artifact(
    store: Store,
    identifier: SessionId,
    revision: int,
    *,
    artifact_id: ArtifactId,
    roi: RegionOfInterest | None = None,
) -> Session:
    with store.locked(identifier):
        state = store.expect(identifier, revision)
        artifact = state.artifact(artifact_id)
        palette = state.palette(artifact.palette_id) if artifact.palette_id is not None else None
        data = read_source(safe_path(store.session_dir(identifier), artifact.path))
        report = analyze_png(
            data, artifact, palette, report_id=ReportId(f"report-{uuid4().hex}"), roi=roi
        )
        updated = advance(
            state.model_copy(update={"color_reports": (*state.color_reports, report)})
        )
        store.save(updated)
    return updated
