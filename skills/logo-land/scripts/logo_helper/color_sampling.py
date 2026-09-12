"""Deterministic original-coordinate sampling without resize interpolation."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

from logo_helper.color_profiles import ProfileTreatment, profiled_pixels
from logo_helper.color_reports import SamplingSettings

if TYPE_CHECKING:
    from PIL import Image

    from logo_helper.reference_models import RegionOfInterest

MAX_SAMPLES: Final = 16384
GRID_SIZE: Final = 128
CORE_ALPHA: Final = 250
MIN_CORE_SAMPLES: Final = 128
type RGB = tuple[int, int, int]


@dataclass(frozen=True, slots=True)
class ColorSamples:
    """Original-coordinate RGB counts with separate visible opacity evidence."""

    core: tuple[tuple[RGB, int], ...]
    visible: tuple[tuple[RGB, int, int], ...]
    sampling: SamplingSettings
    profile_treatment: ProfileTreatment
    reasons: tuple[str, ...]


def sample_image(image: Image.Image, roi: RegionOfInterest | None = None) -> ColorSamples:
    """Read at most 16,384 pixel centers, keeping core and partial-alpha evidence."""
    x, y = (roi.x, roi.y) if roi else (0, 0)
    width, height = (roi.width, roi.height) if roi else image.size
    area = width * height
    all_pixels = area <= MAX_SAMPLES
    columns, rows = (
        (width, height) if all_pixels else (min(GRID_SIZE, width), min(GRID_SIZE, height))
    )
    coordinates = tuple(
        (x + (2 * col + 1) * width // (2 * columns), y + (2 * row + 1) * height // (2 * rows))
        for row in range(rows)
        for col in range(columns)
    )
    core: Counter[RGB] = Counter()
    visible: Counter[tuple[RGB, int]] = Counter()
    with (
        image.convert("RGBA") as rgba,
        rgba.getchannel("A") as alpha,
        profiled_pixels(image) as rgb,
    ):
        channels = rgb.image.split()
        with channels[0] as red, channels[1] as green, channels[2] as blue:
            red_bytes, green_bytes, blue_bytes = red.tobytes(), green.tobytes(), blue.tobytes()
            alpha_bytes = alpha.tobytes()
            for px, py in coordinates:
                offset = py * image.width + px
                opacity = alpha_bytes[offset]
                if opacity == 0:
                    continue
                color = (red_bytes[offset], green_bytes[offset], blue_bytes[offset])
                visible[(color, opacity)] += 1
                if opacity >= CORE_ALPHA:
                    core[color] += 1
        visible_count, core_count = sum(visible.values()), sum(core.values())
        return ColorSamples(
            core=tuple(sorted(core.items())),
            visible=tuple(
                (color, opacity, count) for (color, opacity), count in sorted(visible.items())
            ),
            sampling=SamplingSettings(
                width=image.width,
                height=image.height,
                roi=roi,
                scope="roi" if roi else "full_image",
                coordinate_policy="all_pixels" if all_pixels else "grid_128_pixel_centers",
                sampled_positions=len(coordinates),
                sampled_fraction=len(coordinates) / area,
                visible_samples=visible_count,
                core_samples=core_count,
                partial_alpha_samples=visible_count - core_count,
            ),
            profile_treatment=rgb.treatment,
            reasons=rgb.reasons,
        )


def evidence_limits(samples: ColorSamples) -> tuple[str, ...]:
    reasons = list(samples.reasons)
    settings = samples.sampling
    if settings.core_samples < MIN_CORE_SAMPLES:
        reasons.append("Fewer than 128 core samples; insufficient color evidence")
    if settings.partial_alpha_samples * 10 > settings.visible_samples:
        reasons.append("Partial alpha exceeds 10% of visible samples")
    return tuple(reasons)
