"""Lazy ColorAide calculations with explicit, versioned color algorithms."""

from __future__ import annotations

import math
from importlib.metadata import version
from typing import TYPE_CHECKING, Final, Literal, assert_never

from logo_helper.color_models import normalize_hex
from logo_helper.model_base import ProjectError

if TYPE_CHECKING:
    from coloraide import Color

type HarmonyRecipe = Literal["monochromatic", "analogous", "complementary"]
RECIPES: Final[tuple[HarmonyRecipe, ...]] = ("monochromatic", "analogous", "complementary")
ACHROMATIC_HUES: Final = (45.0, 145.0, 250.0)


def color_type() -> type[Color]:
    """Load the optional engine only for calculations; never install dependencies."""
    try:
        from coloraide import Color  # noqa: PLC0415
    except ImportError as error:
        raise ProjectError(
            "color_engine_unavailable",
            "ColorAide is unavailable; prepare the declared dependencies",
        ) from error
    return Color


def harmony_colors(seed: str, recipe: HarmonyRecipe) -> tuple[str, ...]:
    """Keep the seed verbatim and gamut-map only generated OKLCH companions."""
    anchor = normalize_hex(seed)
    color = color_type()(anchor).convert("oklch")
    if color.is_achromatic():
        hue = ACHROMATIC_HUES[RECIPES.index(recipe)]
        companions = [
            color_type()("oklch", [light, chroma, hue])
            for light, chroma in ((0.55, 0.10), (0.82, 0.06))
        ]
    else:
        match recipe:
            case "monochromatic":
                colors = color.harmony("mono", space="oklch", out_space="oklch")
                companions = [colors[0], colors[-1]]
            case "analogous":
                colors = color.harmony("analogous", space="oklch", out_space="oklch")
                companions = [colors[0], colors[-1]]
            case "complementary":
                opposite = color.harmony("complement", space="oklch", out_space="oklch")[-1]
                companions = [opposite, opposite.clone().set("l", 0.82)]
            case _:
                assert_never(recipe)
    generated = tuple(
        companion.convert("srgb")
        .fit("srgb", method="oklch-chroma")
        .to_string(hex=True, alpha=False, upper=True, compress=False)
        for companion in companions
    )
    return tuple(dict.fromkeys((anchor, *generated)))


def engine_version() -> str:
    """Report the installed engine after verifying that it can actually import."""
    _ = color_type()
    return version("coloraide")


def delta_e(first: str, second: str) -> float:
    """Calculate CIEDE2000 in Lab D50, explicitly overriding ColorAide's D65 default."""
    engine = color_type()
    left = engine(normalize_hex(first)).convert("lab")
    right = engine(normalize_hex(second)).convert("lab")
    return left.delta_e(right, method="2000", space="lab")


def contrast_ratio(foreground: str, surface: str, *, alpha: float = 1.0) -> float:
    """Composite foreground over opaque sRGB surface, then calculate WCAG2 guidance."""
    if not math.isfinite(alpha) or not 0.0 <= alpha <= 1.0:
        raise ProjectError(
            "invalid_alpha", "Contrast alpha must be finite and between zero and one"
        )
    engine = color_type()
    foreground_color = engine(normalize_hex(foreground)).set("alpha", alpha)
    background = engine(normalize_hex(surface))
    composite = engine.layer(
        [foreground_color, background],
        blend="normal",
        operator="source-over",
        space="srgb",
        out_space="srgb",
    )
    return composite.contrast(background, method="wcag21")
