"""Escaped, self-contained palette markup with no provider evidence disclosure."""

from __future__ import annotations

from html import escape
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from logo_helper.color_models import PaletteContent


def swatch(hex_color: str, label: str) -> str:
    return (
        f'<li><span class="swatch" style="background-color:{escape(hex_color, quote=True)}"'
        f' aria-hidden="true"></span><span><code>{escape(hex_color)}</code> '
        f"{escape(label)}</span></li>"
    )


def palette_body(palette: PaletteContent) -> str:
    colors = "".join(swatch(item.hex, item.role) for item in palette.swatches)
    mode = "Strict constraints" if palette.constraints.strict else "Advisory intent"
    return (
        f'<p class="eyebrow">{mode} · {escape(palette.source)}</p>'
        f'<ul class="swatches">{colors}</ul><p>{escape(palette.rationale)}</p>'
        f'<p class="muted">Selected by {escape(palette.selected_by)}</p>'
    )


def render_palette_cards(candidates: tuple[PaletteContent, ...]) -> str:
    """Render inert candidate radio cards; selection changes no persisted state."""
    cards = "".join(
        (
            f'<article class="palette-card"><input type="radio" name="palette-candidate" '
            f'id="candidate-{index}" value="{index}"><label for="candidate-{index}">'
            f"Candidate {index}</label>{palette_body(candidate)}</article>"
        )
        for index, candidate in enumerate(candidates, 1)
    )
    return f'<section class="palette-grid" aria-label="Palette candidates">{cards}</section>'
