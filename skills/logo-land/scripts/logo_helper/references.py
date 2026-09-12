"""Read-only reference inspection and deterministic candidate palette estimates."""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING, Final, Literal

from PIL import Image

from logo_helper.color_profiles import ProfileTreatment  # noqa: TC001 - runtime Pydantic field
from logo_helper.color_reports import MeasuredSwatch, SamplingSettings
from logo_helper.color_sampling import ColorSamples, evidence_limits, sample_image
from logo_helper.model_base import FrozenModel, ProjectError
from logo_helper.reference_decode import ReferenceInspection, decode_reference

if TYPE_CHECKING:
    from logo_helper.reference_models import RegionOfInterest

__all__ = ["PaletteExtraction", "ReferenceInspection", "extract_palette", "inspect_reference"]
MAX_PALETTE_COLORS: Final = 8


class PaletteExtraction(FrozenModel):
    """Sample estimates with explicit scope/profile limits, never conformance proof."""

    swatches: tuple[MeasuredSwatch, ...]
    sampling: SamplingSettings
    profile_treatment: ProfileTreatment
    status: Literal["extracted", "indeterminate"]
    reasons: tuple[str, ...]


def inspect_reference(data: bytes, *, roi: RegionOfInterest | None = None) -> ReferenceInspection:
    """Inspect static PNG/JPEG bytes without changing or saving the source."""
    with decode_reference(data, roi) as decoded:
        return decoded.inspection


def quantized_swatches(samples: ColorSamples, max_colors: int = 8) -> tuple[MeasuredSwatch, ...]:
    """Estimate eligible core colors via Pillow median-cut, retaining white."""
    if not samples.core or samples.profile_treatment == "unsupported":
        return ()
    pixels = bytes(
        channel for color, count in samples.core for _ in range(count) for channel in color
    )
    with (
        Image.frombytes("RGB", (samples.sampling.core_samples, 1), pixels) as image,
        image.quantize(colors=max_colors, method=Image.Quantize.MEDIANCUT) as quantized,
        quantized.convert("RGB") as colors,
    ):
        raw = colors.tobytes()
    counts = Counter(
        f"#{raw[i]:02X}{raw[i + 1]:02X}{raw[i + 2]:02X}" for i in range(0, len(raw), 3)
    )
    return tuple(
        MeasuredSwatch(hex=color, samples=count, share=count / samples.sampling.core_samples)
        for color, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    )


def extract_palette(
    data: bytes, *, roi: RegionOfInterest | None = None, max_colors: int = 8
) -> PaletteExtraction:
    """Return bounded palette estimates and evidence limits from original reference bytes."""
    if not 1 <= max_colors <= MAX_PALETTE_COLORS:
        raise ProjectError("invalid_color_count", "Extraction supports one to eight colors")
    with decode_reference(data, roi) as decoded:
        samples = sample_image(decoded.image, roi)
    reasons = evidence_limits(samples)
    return PaletteExtraction(
        swatches=quantized_swatches(samples, max_colors),
        sampling=samples.sampling,
        profile_treatment=samples.profile_treatment,
        status="indeterminate" if reasons else "extracted",
        reasons=reasons,
    )
