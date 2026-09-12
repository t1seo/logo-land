"""Decode and inspect original image bytes without generating or editing pixels."""

from __future__ import annotations

import warnings
from io import BytesIO
from typing import Final

from PIL import Image, UnidentifiedImageError

from logo_helper.models import ImageFacts, ProjectError

MAX_PIXELS: Final = 40_000_000
PNG_END: Final = bytes.fromhex("0000000049454e44ae426082")


def inspect_png(data: bytes) -> ImageFacts:
    """Require a complete, nonempty, static PNG and measure decoded alpha values."""
    if not data.endswith(PNG_END):
        raise ProjectError("invalid_png", "PNG must end with a complete IEND chunk")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(BytesIO(data)) as probe:
                if probe.format != "PNG":
                    raise ProjectError("invalid_png", "The actual file format must be PNG")
                if probe.width * probe.height > MAX_PIXELS:
                    raise ProjectError("invalid_png", "PNG exceeds the 40 million pixel limit")
                probe.verify()
            with Image.open(BytesIO(data)) as decoded:
                _ = decoded.load()
                try:
                    decoded.seek(1)
                except EOFError:
                    decoded.seek(0)
                else:
                    raise ProjectError("invalid_png", "Animated PNG is not a static logo")
                with decoded.convert("RGBA") as rgba, rgba.getchannel("A") as alpha:
                    histogram = alpha.histogram()
                occupied = [index for index, count in enumerate(histogram) if count]
                if not occupied or occupied[-1] == 0:
                    raise ProjectError("invalid_png", "Fully transparent images are empty logos")
                return ImageFacts(
                    width=decoded.width,
                    height=decoded.height,
                    alpha_min=occupied[0],
                    alpha_max=occupied[-1],
                    transparent_pixels=sum(histogram[:255]),
                    visible_pixels=sum(histogram[1:]),
                )
    except (
        OSError,
        SyntaxError,
        ValueError,
        UnidentifiedImageError,
        Image.DecompressionBombError,
        Image.DecompressionBombWarning,
    ) as error:
        raise ProjectError("invalid_png", f"PNG could not be fully decoded: {error}") from error
