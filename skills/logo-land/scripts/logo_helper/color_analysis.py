"""Bounded logo-color-v1 measurements against immutable artifact palette intent."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Final, Literal

from PIL import __version__ as pillow_version

from logo_helper.color_math import contrast_ratio, delta_e, engine_version
from logo_helper.color_models import normalize_hex
from logo_helper.color_reports import (
    ColorReport,
    ContrastMeasurement,
    MeasuredSwatch,
    TargetMeasurement,
)
from logo_helper.color_sampling import ColorSamples, evidence_limits, sample_image
from logo_helper.model_base import ProjectError
from logo_helper.reference_decode import decode_reference
from logo_helper.references import quantized_swatches

if TYPE_CHECKING:
    from logo_helper.color_models import PaletteVersion
    from logo_helper.models import Artifact, ReportId
    from logo_helper.reference_models import RegionOfInterest

DELTA_E_THRESHOLD: Final = 5.0
MIN_PRESENCE_SAMPLES: Final = 32
MIN_PRESENCE_SHARE: Final = 0.005
DESIGN_SHARE: Final = 0.01
RESTRICTED_FIT: Final = 0.99
type ReportStatus = Literal["pass", "mismatch", "indeterminate", "unverified"]


@dataclass(frozen=True, slots=True)
class _Metrics:
    targets: tuple[TargetMeasurement, ...] = ()
    matched_fraction: float | None = None
    unmatched_fraction: float | None = None
    observed_colors: int | None = None
    minor_swatches: tuple[MeasuredSwatch, ...] = ()


def _metrics(samples: ColorSamples, palette: PaletteVersion) -> _Metrics:
    targets = palette.constraints.allowed_hex or tuple(s.hex for s in palette.swatches)
    total = samples.sampling.core_samples
    if not total:
        return _Metrics()
    distances = tuple(
        (count, tuple(delta_e(f"#{r:02X}{g:02X}{b:02X}", target) for target in targets))
        for (r, g, b), count in samples.core
    )
    assigned = [0] * len(targets)
    for count, values in distances:
        nearest = min(range(len(values)), key=values.__getitem__)
        if values[nearest] <= DELTA_E_THRESHOLD:
            assigned[nearest] += count
    measurements: list[TargetMeasurement] = []
    for index, target in enumerate(targets):
        matching = tuple(
            (count, values[index])
            for count, values in distances
            if values[index] <= DELTA_E_THRESHOLD
        )
        count = sum(count for count, _ in matching)
        measurements.append(
            TargetMeasurement(
                hex=target,
                matching_samples=count,
                share=count / total,
                mean_delta_e=sum(count * distance for count, distance in matching) / count
                if count
                else None,
                max_delta_e=max((distance for _, distance in matching), default=None),
            )
        )
    matched = sum(assigned)
    return _Metrics(
        targets=tuple(measurements),
        matched_fraction=matched / total,
        unmatched_fraction=(total - matched) / total,
        observed_colors=sum(count / total >= DESIGN_SHARE for count in assigned),
        minor_swatches=tuple(
            MeasuredSwatch(hex=target, samples=count, share=count / total)
            for target, count in zip(targets, assigned, strict=True)
            if 0 < count / total < DESIGN_SHARE
        ),
    )


def _status(
    samples: ColorSamples, palette: PaletteVersion, metrics: _Metrics
) -> tuple[ReportStatus, tuple[str, ...]]:
    limits = evidence_limits(samples)
    if limits:
        return "indeterminate", limits
    failures: list[str] = []
    uncertain: list[str] = []
    constraints = palette.constraints
    restricted = constraints.allowed_hex is not None or constraints.max_colors is not None
    if (
        (restricted or not constraints.strict)
        and metrics.matched_fraction is not None
        and metrics.matched_fraction < RESTRICTED_FIT
    ):
        failures.append("Fewer than 99% of sampled core pixels match the target palette")
    if (
        constraints.max_colors is not None
        and metrics.observed_colors is not None
        and metrics.observed_colors > constraints.max_colors
    ):
        failures.append("Observed matched colors with at least 1% share exceed max_colors")
    for target in metrics.targets:
        if target.hex not in {*constraints.locked_hex, *constraints.required_hex}:
            continue
        if not target.matching_samples:
            failures.append(f"Required color {target.hex} has no matching core samples")
        elif target.matching_samples < MIN_PRESENCE_SAMPLES or target.share < MIN_PRESENCE_SHARE:
            uncertain.append(f"Required color {target.hex} has fewer than 32 matches or 0.5% share")
    if failures:
        return "mismatch", (*failures, *uncertain)
    if uncertain:
        return "indeterminate", tuple(uncertain)
    return "pass", ()


def _contrasts(samples: ColorSamples, surfaces: tuple[str, ...]) -> tuple[ContrastMeasurement, ...]:
    most_frequent = sorted(samples.visible, key=lambda item: (-item[2], item[0], item[1]))[:8]
    return tuple(
        ContrastMeasurement(
            foreground=f"#{r:02X}{g:02X}{b:02X}",
            surface=surface,
            alpha=alpha / 255,
            ratio=contrast_ratio(f"#{r:02X}{g:02X}{b:02X}", surface, alpha=alpha / 255),
        )
        for (r, g, b), alpha, _ in most_frequent
        for surface in surfaces
    )


def analyze_png(
    data: bytes,
    artifact: Artifact,
    palette: PaletteVersion | None,
    *,
    report_id: ReportId,
    roi: RegionOfInterest | None = None,
    surfaces: tuple[str, ...] = ("#FFFFFF", "#171717"),
    created_at: datetime | None = None,
) -> ColorReport:
    """Measure verified original PNG samples; never recolor, save, or authorize export."""
    if hashlib.sha256(data).hexdigest() != artifact.sha256:
        raise ProjectError("integrity", "Analysis bytes do not match the artifact SHA256")
    if artifact.palette_id != (palette.id if palette else None):
        raise ProjectError("invalid_state", "Analysis palette differs from artifact intent")
    normalized_surfaces = tuple(dict.fromkeys(normalize_hex(surface) for surface in surfaces))
    with decode_reference(data, roi) as decoded:
        if decoded.inspection.format != "PNG":
            raise ProjectError("invalid_png", "Artifact color analysis requires PNG")
        if (decoded.inspection.width, decoded.inspection.height) != (
            artifact.image.width,
            artifact.image.height,
        ):
            raise ProjectError("integrity", "Analysis dimensions differ from artifact facts")
        samples = sample_image(decoded.image, roi)
    metrics = _Metrics()
    version = "not_used"
    contrasts: tuple[ContrastMeasurement, ...] = ()
    status: ReportStatus = "unverified"
    reasons = ("No structured palette intent is recorded for this artifact", *samples.reasons)
    if palette is not None:
        try:
            version = engine_version()
            if samples.profile_treatment != "unsupported":
                metrics = _metrics(samples, palette)
                contrasts = _contrasts(samples, normalized_surfaces)
            status, reasons = _status(samples, palette, metrics)
        except ProjectError as error:
            if error.code != "color_engine_unavailable":
                raise
            version, status, reasons = "unavailable", "indeterminate", (str(error),)
    return ColorReport(
        id=report_id,
        artifact_id=artifact.id,
        artifact_sha256=artifact.sha256,
        palette_id=palette.id if palette else None,
        palette_digest=palette.digest if palette else None,
        color_engine_version=version,
        pillow_version=pillow_version,
        profile_treatment=samples.profile_treatment,
        sampling=samples.sampling,
        status=status,
        reasons=reasons,
        measured_swatches=quantized_swatches(samples),
        targets=metrics.targets,
        matched_fraction=metrics.matched_fraction,
        unmatched_fraction=metrics.unmatched_fraction,
        observed_colors=metrics.observed_colors,
        minor_swatches=metrics.minor_swatches,
        contrasts=contrasts,
        created_at=created_at or datetime.now(UTC),
    )
