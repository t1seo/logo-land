"""Profile interpretation for analysis buffers; original pixels are never saved."""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, Literal

from PIL import Image, ImageCms

if TYPE_CHECKING:
    from collections.abc import Generator, Mapping

type ProfileTreatment = Literal["declared_srgb", "converted_icc", "assumed_srgb", "unsupported"]
SRGB_GAMMA: Final = 0.45455


@dataclass(frozen=True, slots=True)
class ProfiledPixels:
    """In-memory RGB buffer and the provenance required to interpret its values."""

    image: Image.Image
    treatment: ProfileTreatment
    reasons: tuple[str, ...] = ()


@contextmanager
def profiled_pixels(image: Image.Image) -> Generator[ProfiledPixels]:
    """Convert supported RGB ICC in memory and explicitly label uncertain profiles."""
    metadata: Mapping[str | tuple[int, int], bytes | str | int | float | None] = image.info
    icc = metadata.get("icc_profile")
    treatment: ProfileTreatment = "assumed_srgb"
    reason: tuple[str, ...] = ()
    with image.convert("RGB") as rgb:
        if icc is not None:
            if not isinstance(icc, bytes):
                yield ProfiledPixels(rgb, "unsupported", ("Malformed ICC metadata",))
                return
            try:
                from PIL._imagingcms import (  # noqa: PLC0415 - optional ICC support loads on demand
                    createProfile,
                    profile_frombytes,
                )

                profile = profile_frombytes(icc)
                if profile.xcolor_space.strip() != "RGB":
                    yield ProfiledPixels(rgb, "unsupported", ("Embedded ICC is not RGB",))
                    return
                transform = ImageCms.buildTransformFromOpenProfiles(
                    profile,
                    createProfile("sRGB"),
                    "RGB",
                    "RGB",
                    renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC,
                )
                converted = transform.apply(rgb)
            except (ImportError, ImageCms.PyCMSError, OSError, ValueError) as error:
                yield ProfiledPixels(rgb, "unsupported", (f"Unsupported ICC profile: {error}",))
                return
            with converted:
                yield ProfiledPixels(converted, "converted_icc")
            return
        if "srgb" in metadata:
            treatment = "declared_srgb"
        elif "gamma" in metadata and metadata["gamma"] != SRGB_GAMMA:
            treatment = "unsupported"
            reason = ("Non-sRGB gamma-only metadata cannot establish sRGB colors",)
        elif image.mode == "CMYK":
            treatment = "unsupported"
            reason = ("Untagged CMYK cannot establish sRGB colors",)
        yield ProfiledPixels(rgb, treatment, reason)
