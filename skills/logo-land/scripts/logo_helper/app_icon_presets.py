"""Typed conversational choices; explicit placement is always respected."""

from typing import Final

from logo_helper.app_icon_models import AppIconPlacement, AppIconPreset
from logo_helper.model_base import FrozenModel


class AppIconPresetChoice(FrozenModel):
    """A discoverable style and its conversational starting placement."""

    id: AppIconPreset
    label: str
    description: str
    default_placement: AppIconPlacement


APP_ICON_PRESETS: Final[tuple[AppIconPresetChoice, ...]] = (
    AppIconPresetChoice(
        id="ip_mascot",
        label="IP mascot",
        description=(
            "Simple personified character with rounded heavy forms "
            "and two subject color families on a solid background."
        ),
        default_placement="lower_left",
    ),
    AppIconPresetChoice(
        id="pictogram",
        label="Pictogram",
        description="One immediately recognizable silhouette with clean flat shapes.",
        default_placement="center",
    ),
    AppIconPresetChoice(
        id="abstract",
        label="Abstract",
        description="A compact geometric composition with clear negative space.",
        default_placement="center",
    ),
    AppIconPresetChoice(
        id="monogram",
        label="Monogram",
        description="One to eight exact Unicode characters shaped as readable lettering.",
        default_placement="center",
    ),
    AppIconPresetChoice(
        id="soft_3d",
        label="Soft 3D",
        description="A tactile, softly rounded object with restrained depth and lighting.",
        default_placement="center",
    ),
    AppIconPresetChoice(
        id="pixel_art",
        label="Pixel art",
        description="Deliberate block geometry on a consistent pixel grid.",
        default_placement="center",
    ),
)
