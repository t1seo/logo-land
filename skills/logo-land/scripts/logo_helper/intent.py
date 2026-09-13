"""Shared prompt/import precedence for immutable palette and requested lockup intent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from logo_helper.model_base import ProjectError

if TYPE_CHECKING:
    from logo_helper.app_icon_models import AppIconIntent
    from logo_helper.models import ArtifactId, LockupIntent, PaletteId, PaletteVersion, Session


@dataclass(frozen=True, slots=True)
class EffectiveIntent:
    """Resolved immutable intent shared by prompt and import boundaries."""

    palette: PaletteVersion | None
    lockup: LockupIntent | None
    app_icon: AppIconIntent | None = None


def resolve_intent(
    state: Session,
    parent_id: ArtifactId | None,
    palette_id: PaletteId | None,
    lockup: LockupIntent | None,
    app_icon: AppIconIntent | None = None,
) -> EffectiveIntent:
    parent = state.artifact(parent_id) if parent_id is not None else None
    inherited_palette = parent.palette_id if parent is not None else state.active_palette_id
    identifier = palette_id if palette_id is not None else inherited_palette
    inherited_lockup = parent.lockup if parent is not None else state.brief.lockup
    inherited_icon = parent.app_icon if parent is not None else state.brief.app_icon
    icon = app_icon if app_icon is not None else inherited_icon
    if icon is not None and lockup is not None:
        raise ProjectError("intent_conflict", "App icon intent conflicts with explicit lockup")
    effective_lockup = lockup if lockup is not None else inherited_lockup
    return EffectiveIntent(
        palette=state.palette(identifier) if identifier is not None else None,
        lockup=None if icon is not None else effective_lockup,
        app_icon=icon,
    )
