"""Bounded original-byte decoding shared by reference and artifact analysis."""

from __future__ import annotations

import warnings
from contextlib import contextmanager
from dataclasses import dataclass
from io import BytesIO
from typing import TYPE_CHECKING, Annotated, Final, Literal

from PIL import Image, ImageOps
from pydantic import Field

from logo_helper.images import MAX_PIXELS, PNG_END
from logo_helper.model_base import FrozenModel, ProjectError

if TYPE_CHECKING:
    from collections.abc import Generator, Mapping

    from logo_helper.reference_models import RegionOfInterest

MAX_REFERENCE_BYTES: Final = 64 * 1024 * 1024
SWAPPED_ORIENTATION: Final = 5
MAX_ORIENTATION: Final = 8


class ReferenceInspection(FrozenModel):
    """Original dimensions and orientation; ROI coordinates use oriented dimensions."""

    format: Literal["PNG", "JPEG"]
    width: Annotated[int, Field(gt=0)]
    height: Annotated[int, Field(gt=0)]
    exif_orientation: Annotated[int, Field(ge=1, le=8)] = 1


@dataclass(frozen=True, slots=True)
class DecodedReference:
    """Temporary image lifetime is owned by decode_reference's context manager."""

    image: Image.Image
    inspection: ReferenceInspection


@contextmanager
def decode_reference(
    data: bytes, roi: RegionOfInterest | None = None
) -> Generator[DecodedReference]:
    """Verify format/size before loading, then orient a temporary in-memory image."""
    if len(data) > MAX_REFERENCE_BYTES:
        raise ProjectError("invalid_reference", "Reference exceeds the 64 MiB limit")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(BytesIO(data)) as probe:
                if probe.format not in {"PNG", "JPEG"}:
                    raise ProjectError("invalid_reference", "Reference must be PNG or JPEG")
                if probe.width * probe.height > MAX_PIXELS:
                    raise ProjectError("invalid_reference", "Reference exceeds the 40M pixel limit")
                if probe.format == "PNG" and not data.endswith(PNG_END):
                    raise ProjectError("invalid_reference", "PNG must end with a complete IEND")
                if probe.format == "JPEG" and not data.endswith(b"\xff\xd9"):
                    raise ProjectError("invalid_reference", "JPEG must end with a complete EOI")
                if getattr(probe, "n_frames", 1) != 1:
                    raise ProjectError("invalid_reference", "Reference must be static")
                probe.verify()
            with Image.open(BytesIO(data)) as decoded:
                exif: Mapping[int, int | str | bytes] = decoded.getexif()
                orientation = _orientation(exif)
                facts = ReferenceInspection(
                    format="PNG" if decoded.format == "PNG" else "JPEG",
                    width=decoded.width,
                    height=decoded.height,
                    exif_orientation=orientation,
                )
                width, height = facts.width, facts.height
                if facts.exif_orientation >= SWAPPED_ORIENTATION:
                    width, height = height, width
                if roi is not None and not roi.contained_by(width, height):
                    raise ProjectError("invalid_roi", "ROI leaves the oriented image")
                _ = decoded.load()
                with ImageOps.exif_transpose(decoded) as oriented:
                    yield DecodedReference(oriented, facts)
    except (
        OSError,
        SyntaxError,
        ValueError,
        Image.DecompressionBombError,
        Image.DecompressionBombWarning,
    ) as error:
        raise ProjectError(
            "invalid_reference", f"Reference could not be decoded: {error}"
        ) from error


def _orientation(exif: Mapping[int, int | str | bytes]) -> int:
    value = exif.get(274, 1)
    if not isinstance(value, int) or not 1 <= value <= MAX_ORIENTATION:
        raise ProjectError("invalid_reference", "EXIF orientation must be an integer from 1 to 8")
    return value
