"""Export evidence policy: stored reports select scope but never authorize fidelity."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, Literal, assert_never
from uuid import uuid4

from PIL import __version__ as pillow_version

from logo_helper.color_analysis import analyze_png
from logo_helper.color_reports import ColorReport, SamplingSettings
from logo_helper.images import inspect_png
from logo_helper.models import ProjectError, ReportId

if TYPE_CHECKING:
    from datetime import datetime

    from logo_helper.color_models import PaletteVersion
    from logo_helper.models import Artifact, Session

type ColorPolicy = Literal["strict", "advisory", "unverified"]
COLOR_METHOD: Final = "sRGB to Lab D50; CIEDE2000, ColorAide method=2000"
COLOR_LIMITS: Final = (
    "Sampled raster evidence, not an exact-pixel, Pantone, or print-proof guarantee.",
    "At most 16384 original-coordinate samples; small accents may be missed.",
    "Alpha-zero pixels are excluded; conformance uses alpha >=250 and preserves white.",
    "Strict evidence needs 128 core samples and at most 10% partial-alpha visible samples.",
    "Restricted fit requires 99% core coverage within delta-E00 <=5; design colors need 1% share.",
    "Locks/required colors need 32 matching core samples and 0.5% core share.",
    "Quantized measured swatches are estimates; conformance uses original sampled colors.",
    "Color roles, lettering, and placement require visual review; histograms cannot prove them.",
    "ROI evidence covers only the stated region; opaque full-image evidence includes background.",
    "Contrast ratios on explicit composited surfaces are guidance, not logo AA certification.",
)


@dataclass(frozen=True, slots=True)
class ColorDelivery:
    """Selected intent and fresh evidence published in one export transaction."""

    palette: PaletteVersion | None
    report: ColorReport
    policy: ColorPolicy
    warnings: tuple[str, ...]


def _require_determinate(report: ColorReport) -> None:
    match report.status:
        case "pass" | "mismatch":
            return
        case "indeterminate" | "unverified":
            raise ProjectError(
                "color_review_required",
                "Run color-analyze to resolve missing color evidence: " + "; ".join(report.reasons),
            )
        case _:
            assert_never(report.status)


def _fresh_report(
    data: bytes,
    artifact: Artifact,
    palette: PaletteVersion | None,
    previous: ColorReport | None,
    now: datetime,
) -> ColorReport:
    report_id = ReportId(f"export-{uuid4().hex}")
    try:
        return analyze_png(
            data,
            artifact,
            palette,
            report_id=report_id,
            created_at=now,
            roi=previous.sampling.roi if previous else None,
            surfaces=tuple(dict.fromkeys(item.surface for item in previous.contrasts))
            if previous and previous.contrasts
            else ("#FFFFFF", "#171717"),
        )
    except ProjectError as error:
        if error.code != "invalid_reference" or error.__cause__ is not None:
            raise
        if inspect_png(data) != artifact.image:
            raise ProjectError(
                "integrity", "Export PNG facts differ from artifact facts"
            ) from error
        return ColorReport(
            id=report_id,
            artifact_id=artifact.id,
            artifact_sha256=artifact.sha256,
            palette_id=palette.id if palette else None,
            palette_digest=palette.digest if palette else None,
            color_engine_version="not_used",
            pillow_version=pillow_version,
            profile_treatment="unsupported",
            sampling=SamplingSettings(
                width=artifact.image.width,
                height=artifact.image.height,
                sampled_positions=0,
                sampled_fraction=0,
                visible_samples=0,
                core_samples=0,
                partial_alpha_samples=0,
            ),
            status="indeterminate" if palette else "unverified",
            reasons=(f"Color evidence unavailable: {error}",),
            created_at=now,
        )


def export_colors(
    state: Session,
    artifact: Artifact,
    data: bytes,
    now: datetime,
) -> ColorDelivery:
    """Recompute the latest explicitly analyzed scope with fixed current policy thresholds."""
    palette = state.palette(artifact.palette_id) if artifact.palette_id is not None else None
    previous = next(
        (
            report
            for report in reversed(state.color_reports)
            if report.artifact_id == artifact.id
            and report.artifact_sha256 == artifact.sha256
            and report.palette_id == artifact.palette_id
            and report.palette_digest == (palette.digest if palette else None)
        ),
        None,
    )
    strict = palette is not None and palette.constraints.strict
    if strict:
        if previous is None:
            raise ProjectError("color_review_required", "Run color-analyze before strict export")
        _require_determinate(previous)
    report = _fresh_report(data, artifact, palette, previous, now)
    if strict:
        _require_determinate(report)
        if report.status == "mismatch":
            raise ProjectError("color_mismatch", "; ".join(report.reasons))
    policy: ColorPolicy = "unverified" if palette is None else "strict" if strict else "advisory"
    warnings: list[str] = []
    if palette is None:
        warnings.append("Color-unverified: no structured palette intent is bound to this artifact.")
    elif not strict:
        warnings.append(f"Advisory color evidence: {report.status}; no strict constraints apply.")
    warnings.extend(report.reasons)
    if report.profile_treatment == "assumed_srgb":
        warnings.append("Untagged PNG colors are assumed sRGB; no embedded profile confirms this.")
    if report.sampling.roi is not None:
        warnings.append("Color evidence is limited to the explicit ROI, not the whole image.")
    return ColorDelivery(palette, report, policy, tuple(warnings))
