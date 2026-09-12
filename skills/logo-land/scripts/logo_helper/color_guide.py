"""Human-readable sampled evidence and appearance-only typography intent."""

from __future__ import annotations

from typing import TYPE_CHECKING

from logo_helper.color_delivery import COLOR_LIMITS, COLOR_METHOD

if TYPE_CHECKING:
    from logo_helper.color_delivery import ColorDelivery
    from logo_helper.models import Artifact


def color_guide(evidence: ColorDelivery) -> str:
    report, palette = evidence.report, evidence.palette
    lines = ["## Color intent and sampled evidence", "", f"Policy: {evidence.policy}.", ""]
    if palette is None:
        lines.append("No structured palette intent is recorded. Color compliance is unverified.")
    else:
        lines.extend(
            (
                (
                    f"Selected palette version: {palette.id}; "
                    f"parent: {palette.parent_palette_id or 'none'}."
                ),
                f"Palette digest: {palette.digest}.",
                f"Source: {palette.source}; selected by: {palette.selected_by}.",
                f"Rationale: {palette.rationale}",
                "",
                "Intended swatches:",
                "",
                *(f"- {swatch.hex}: {swatch.role}" for swatch in palette.swatches),
                "",
                "Constraints: " + palette.constraints.model_dump_json(),
            )
        )
    settings = report.sampling
    lines.extend(
        (
            "",
            f"Fresh report: {report.id}; status: {report.status}.",
            f"Artifact SHA256: {report.artifact_sha256}.",
            f"Analysis policy: {report.analysis_policy}; method: {COLOR_METHOD}.",
            f"ColorAide: {report.color_engine_version}; Pillow: {report.pillow_version}.",
            f"Profile treatment: {report.profile_treatment}.",
            (
                f"Scope: {settings.scope}; coordinates: {settings.coordinate_policy}; "
                f"{settings.sampled_positions} samples ({settings.sampled_fraction:.2%} of scope)."
            ),
            (
                f"Core: {settings.core_samples}; partial alpha: {settings.partial_alpha_samples}; "
                f"visible: {settings.visible_samples}."
            ),
        )
    )
    if settings.roi is not None:
        lines.append("Explicit ROI: " + settings.roi.model_dump_json())
    lines.extend(("", "Measured swatches (quantized estimates):", ""))
    lines.extend(
        f"- {swatch.hex}: {swatch.samples} samples, {swatch.share:.2%} share"
        for swatch in report.measured_swatches
    )
    if report.matched_fraction is not None and report.unmatched_fraction is not None:
        lines.extend(
            (
                "",
                (
                    f"Core matched: {report.matched_fraction:.2%}; "
                    f"unmatched: {report.unmatched_fraction:.2%}; "
                    f"observed design colors: {report.observed_colors}."
                ),
            )
        )
    lines.extend(
        ("", f"Target closeness threshold: delta-E00 <= {report.delta_e_threshold:g}.", "")
    )
    for target in report.targets:
        distance = "unavailable"
        if target.mean_delta_e is not None and target.max_delta_e is not None:
            distance = f"mean {target.mean_delta_e:.3f}, max {target.max_delta_e:.3f}"
        description = (
            f"- {target.hex}: {target.matching_samples} matching core samples, "
            f"{target.share:.2%} share; matching-sample delta-E00 {distance}"
        )
        lines.append(description)
    lines.extend(("", "Minor matched swatches below 1% share:", ""))
    lines.extend(f"- {s.hex}: {s.samples} samples, {s.share:.2%}" for s in report.minor_swatches)
    lines.extend(("", "Contrast guidance (explicit surfaces):", ""))
    lines.extend(
        f"- {c.foreground} at alpha {c.alpha:.3f} on {c.surface}: {c.ratio:.2f}:1"
        for c in report.contrasts
    )
    lines.extend(("", "Limitations and warnings:", ""))
    lines.extend(f"- {warning}" for warning in (*evidence.warnings, *COLOR_LIMITS))
    return "\n".join(lines) + "\n"


def typography_guide(artifact: Artifact) -> str:
    lockup = artifact.lockup
    lines = ["## Typography and lockup intent", ""]
    if lockup is None:
        lines.append("No structured lockup intent is recorded for this artifact.")
    else:
        lines.extend(
            (
                (
                    f"Requested layout: {lockup.layout}; "
                    f"symbol position: {lockup.symbol_position}; "
                    f"text alignment: {lockup.text_alignment}."
                ),
                f"Requested typography style: {lockup.typography_style}.",
                f"Font reference: {lockup.font_reference or 'none'} (appearance-reference-only).",
            )
        )
    lines.extend(
        (
            "",
            (
                "Font references describe requested appearance only. They do not identify the "
                "font actually rendered, provide editable typesetting, include font files, "
                "or grant a font license. Verify lettering in the original PNG."
            ),
        )
    )
    return "\n".join(lines) + "\n"
