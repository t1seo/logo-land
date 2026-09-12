"""Shared prompt/import precedence for immutable palette and requested lockup intent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logo_helper.models import ArtifactId, LockupIntent, PaletteId, PaletteVersion, Session


@dataclass(frozen=True, slots=True)
class EffectiveIntent:
    """Resolved immutable intent shared by prompt and import boundaries."""

    palette: PaletteVersion | None
    lockup: LockupIntent | None


def resolve_intent(
    state: Session,
    parent_id: ArtifactId | None,
    palette_id: PaletteId | None,
    lockup: LockupIntent | None,
) -> EffectiveIntent:
    parent = state.artifact(parent_id) if parent_id is not None else None
    inherited_palette = parent.palette_id if parent is not None else state.active_palette_id
    identifier = palette_id if palette_id is not None else inherited_palette
    inherited_lockup = parent.lockup if parent is not None else None
    return EffectiveIntent(
        palette=state.palette(identifier) if identifier is not None else None,
        lockup=lockup if lockup is not None else inherited_lockup or state.brief.lockup,
    )
