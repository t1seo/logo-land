"""Bounded target-view rasterization with a typed Pillow resize boundary."""

from __future__ import annotations

from io import BytesIO
from typing import TYPE_CHECKING, Final, Protocol

from PIL import Image, UnidentifiedImageError

from .models import StudioError
from .store_files import read_file

if TYPE_CHECKING:
    from pathlib import Path

MAX_PIXELS: Final = 40_000_000
MAX_VIEW_PIXELS: Final = 4_000_000


class _Resizable(Protocol):
    def resize(self, size: tuple[int, int], resample: int | None = None) -> Image.Image: ...


def review_view(path: Path, width: int) -> bytes:
    """Canonical RGBA PNG at exact CSS width; this is only a review aid."""
    data = read_file(path)
    try:
        with Image.open(BytesIO(data)) as source:
            _check_size(source, width)
            height = max(1, round(source.height * width / source.width))
            with (
                source.convert("RGBA") as rgba,
                _resize(rgba, width, height) as resized,
                BytesIO() as output,
            ):
                resized.save(output, format="PNG")
                return output.getvalue()
    except (OSError, UnidentifiedImageError, Image.DecompressionBombError) as error:
        raise StudioError("invalid_png", str(error)) from error


def _check_size(source: Image.Image, width: int) -> None:
    if source.format != "PNG" or source.width * source.height > MAX_PIXELS:
        raise StudioError("invalid_png", "Expected a bounded original PNG")
    height = max(1, round(source.height * width / source.width))
    if width * height > MAX_VIEW_PIXELS:
        raise StudioError("invalid_png", "Target preview would exceed its pixel budget")


def _resize(source: _Resizable, width: int, height: int) -> Image.Image:
    return source.resize((width, height), Image.Resampling.LANCZOS)
