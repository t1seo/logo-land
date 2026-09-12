"""Read-only proposals bound to actual stored reference extraction evidence."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

from pydantic import JsonValue, TypeAdapter

from logo_helper.models import (
    FrozenModel,
    PaletteContent,
    ProjectError,
    ReferenceId,
    Session,
    SessionId,
)
from logo_helper.palettes import PaletteRequest, propose_palettes
from logo_helper.reference_evidence import extract_reference
from logo_helper.references import PaletteExtraction  # noqa: TC001 - runtime Pydantic field

if TYPE_CHECKING:
    from logo_helper.storage import Store


class ProposalResult(FrozenModel):
    """Candidates and measured reference provenance at one unchanged session revision."""

    session_id: SessionId
    revision: int
    candidates: tuple[PaletteContent, ...]
    warnings: tuple[str, ...]
    extraction: PaletteExtraction | None = None


def propose(
    store: Store,
    state: Session,
    request_data: bytes,
    reference_id: ReferenceId | None = None,
) -> ProposalResult:
    extraction: PaletteExtraction | None = None
    if reference_id is not None:
        extraction, evidence = extract_reference(store, state, reference_id)
        raw = TypeAdapter(dict[str, JsonValue]).validate_json(request_data)
        raw.update(
            {
                "source": "reference",
                "swatches": [],
                "extracted_colors": [item.hex for item in extraction.swatches],
                "source_evidence": evidence.model_dump(mode="json"),
            }
        )
        request = PaletteRequest.model_validate_json(json.dumps(raw))
    else:
        request = PaletteRequest.model_validate_json(request_data)
        evidence = request.source_evidence
        if evidence.reference_id is not None:
            extraction, actual = extract_reference(store, state, evidence.reference_id)
            if evidence != actual:
                raise ProjectError(
                    "invalid_evidence", "Reference evidence differs from actual extraction"
                )
            if request.source == "reference":
                request = request.model_copy(
                    update={
                        "extracted_colors": tuple(item.hex for item in extraction.swatches),
                    }
                )
    proposal = propose_palettes(request)
    return ProposalResult(
        session_id=state.id,
        revision=state.revision,
        candidates=proposal.candidates,
        warnings=(*proposal.warnings, *(extraction.reasons if extraction is not None else ())),
        extraction=extraction,
    )
