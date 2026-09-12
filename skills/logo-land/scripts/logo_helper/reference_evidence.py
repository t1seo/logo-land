"""Canonical extraction evidence derived only from a verified session-local reference."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

from logo_helper.models import ProjectError, SourceEvidence
from logo_helper.references import PaletteExtraction, extract_palette
from logo_helper.storage import Store, read_source, safe_path

if TYPE_CHECKING:
    from logo_helper.models import PaletteContent, ReferenceId, Session


def extract_reference(
    store: Store,
    state: Session,
    reference_id: ReferenceId,
) -> tuple[PaletteExtraction, SourceEvidence]:
    reference = state.reference(reference_id)
    data = read_source(safe_path(store.session_dir(state.id), reference.path))
    if hashlib.sha256(data).hexdigest() != reference.sha256:
        raise ProjectError("hash_mismatch", f"Reference {reference.id} changed during extraction")
    extraction = extract_palette(data, roi=reference.roi)
    evidence = SourceEvidence(
        reference_id=reference.id,
        reference_sha256=reference.sha256,
        tool="Pillow median-cut; logo-color-v1",
        response=extraction.model_dump_json(),
        notes=extraction.reasons,
    )
    return extraction, evidence


def verify_reference_evidence(store: Store, state: Session, content: PaletteContent) -> None:
    evidence = content.source_evidence
    if content.source == "reference" and evidence.reference_id is None:
        raise ProjectError(
            "invalid_evidence", "Reference palettes require actual extraction provenance"
        )
    if evidence.reference_id is not None:
        _, actual = extract_reference(store, state, evidence.reference_id)
        if evidence != actual:
            raise ProjectError(
                "invalid_evidence", "Reference evidence differs from actual extraction"
            )
