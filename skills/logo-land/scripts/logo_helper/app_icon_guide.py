"""Selected icon intent and the boundary between raster artwork and platform assets."""

from __future__ import annotations

from html import escape
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from logo_helper.app_icon_models import AppIconIntent

ARTWORK_LIMITATIONS: Final = (
    "This PNG is app-icon artwork, not an Icon Composer document, Android adaptive layers, "
    "an app build, or evidence of store acceptance. Platform preparation and validation "
    "are separate steps. Preview masks are illustrative and do not alter the original."
)


def app_icon_guide(intent: AppIconIntent | None) -> str:
    """Describe only the selected artifact's intent, preserving Unicode lettering."""
    if intent is None:
        return ""
    return (
        "\n## Selected app-icon artwork\n\n"
        f"Preset: {escape(intent.preset)}\n\n"
        f"Subject: {escape(intent.subject)}\n\n"
        f"Placement: {escape(intent.placement)}\n\n"
        f"Exact lettering: {escape(intent.text or 'None')}\n\n"
        f"{ARTWORK_LIMITATIONS}\n"
    )
