"""Build host image-tool prompts while keeping generation outside this helper."""

from __future__ import annotations

from typing import Literal

from logo_helper.intent import resolve_intent
from logo_helper.models import (
    ArtifactId,
    Background,
    Digest,
    FrozenModel,
    LockupIntent,
    PaletteId,
    ProjectError,
    Session,
)
from logo_helper.storage import Store, safe_path


class PromptResult(FrozenModel):
    """A host-call instruction plus the exact verified local edit target, when present."""

    mode: Literal["generation", "edit"]
    session_id: str
    revision: int
    prompt: str
    parent_id: ArtifactId | None
    parent_image_path: str | None
    parent_requested_background: Background | None = None
    palette_id: PaletteId | None = None
    palette_digest: Digest | None = None
    lockup: LockupIntent | None = None


def build_prompt(
    store: Store,
    state: Session,
    *,
    concept: str,
    parent_id: ArtifactId | None,
    changes: str,
    palette_id: PaletteId | None = None,
    lockup: LockupIntent | None = None,
) -> PromptResult:
    """Preserve exact text and bind edits to an existing parent without changing state."""
    if bool(changes.strip()) != (parent_id is not None):
        raise ProjectError(
            "invalid_request", "An edit requires both --parent and nonempty --changes"
        )
    brief = state.brief
    intent = resolve_intent(state, parent_id, palette_id, lockup)
    background_label = (
        "Initial brief background (historical intent)" if parent_id is not None else "Background"
    )
    direction = (
        f"Create one {brief.logo_type} logo for {brief.brand_name}. "
        f"Industry: {brief.industry}. Audience: {brief.audience}.\n"
        f"Exact text (copy verbatim, no other words): {brief.exact_text!r}. "
        f"Exact slogan: {brief.slogan!r}.\n"
        f"Styles: {', '.join(brief.styles)}. Original brief palette context: "
        f"{', '.join(brief.palette)}.\n"
        f"Avoid: {', '.join(brief.forbidden)}. Use cases: {', '.join(brief.use_cases)}.\n"
        f"{background_label}: {brief.background}. Produce a real PNG raster image. "
        "Use clean, readable shapes at small sizes; leave safe margins. "
        "Do not draw a transparency checkerboard, mockup, watermarks, or a concept grid.\n"
        f"Concept direction: {concept}. Assumptions: {', '.join(brief.assumptions)}."
    )
    parent_path: str | None = None
    parent_background: Background | None = None
    mode: Literal["generation", "edit"] = "generation"
    if parent_id is not None:
        parent = state.artifact(parent_id)
        parent_background = parent.effective_background(brief)
        parent_path = str(safe_path(store.session_dir(state.id), parent.path))
        mode = "edit"
        direction = (
            f"Edit the supplied parent logo {parent_id}; do not recreate an unrelated logo.\n"
            f"Parent requested background: {parent_background}; preserve it unless the latest "
            "requested changes specify another background.\n"
            f"Latest requested changes (authoritative): {changes}. Preserve all unrequested "
            "text, geometry, layout, silhouette, and brand identity from that parent. "
            "Requested changes override conflicting parent intent and fields in the following "
            f"original brief context; its background is historical, not a new request.\n{direction}"
        )
    if intent.palette is not None:
        palette = intent.palette
        direction += (
            "\nEffective structured palette intent (authoritative over historical palette): "
            f"{palette.model_dump_json()}. Keep locked and required HEX values exactly in intent; "
            "use the declared roles and allowed colors/count. Opaque backgrounds count as "
            "visible design colors; transparent pixels do not. No gradients unless allowed. "
            "Raster fidelity is measured after generation, never promised as exact pixels."
        )
    if intent.lockup is not None:
        direction += (
            f"\nEffective symbol-plus-text lockup: {intent.lockup.model_dump_json()}. "
            "Horizontal start/end means symbol left/right of text; stacked start/end means "
            "symbol above/below text. Preserve the exact text and slogan. Font reference is "
            "a requested visual direction, not proof of an installed or licensed font file."
        )
    return PromptResult(
        mode=mode,
        session_id=state.id,
        revision=state.revision,
        prompt=direction,
        parent_id=parent_id,
        parent_image_path=parent_path,
        parent_requested_background=parent_background,
        palette_id=intent.palette.id if intent.palette is not None else None,
        palette_digest=intent.palette.digest if intent.palette is not None else None,
        lockup=intent.lockup,
    )
