"""Requested symbol/text layout; font references are visual intent only."""

from typing import Literal

from logo_helper.model_base import FrozenModel, Text


class LockupIntent(FrozenModel):
    """Preserve requested layout without claiming actual font-file provenance."""

    layout: Literal["horizontal", "stacked"]
    symbol_position: Literal["start", "end"] = "start"
    text_alignment: Literal["start", "center", "end"] = "start"
    typography_style: Text
    font_reference: Text | None = None
