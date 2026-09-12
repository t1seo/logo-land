"""Public report and lockup snapshots; stored status never authorizes export."""

from __future__ import annotations

from html import escape
from typing import TYPE_CHECKING, assert_never

from logo_helper.color_gallery_cards import palette_body, swatch

if TYPE_CHECKING:
    from logo_helper.color_reports import ColorReport
    from logo_helper.models import Artifact, Session


def report_markup(report: ColorReport | None) -> str:
    if report is None:
        return (
            '<section data-status="unverified"><h3>Measured colors</h3>'
            '<p class="status">unverified · No stored report</p>'
            "<p>Scope and ΔE unavailable. Missing evidence is never a pass.</p></section>"
        )
    status = report.status if report.palette_id is not None else "unverified"
    match status:
        case "pass":
            label = "pass · Stored measurement only"
        case "mismatch":
            label = "mismatch · Inspect color differences"
        case "indeterminate":
            label = "indeterminate · Insufficient evidence"
        case "unverified":
            label = "unverified · No verified color match"
        case _:
            assert_never(status)
    sampling = report.sampling
    measured = (
        "".join(
            swatch(item.hex, f"{item.share:.1%} · {item.samples} samples")
            for item in report.measured_swatches
        )
        or "<li>No measured swatches</li>"
    )
    targets = "".join(
        (
            f"<tr><td>{escape(item.hex)}</td><td>{item.share:.1%}</td>"
            f"<td>{distance(item.mean_delta_e)}</td><td>{distance(item.max_delta_e)}</td></tr>"
        )
        for item in report.targets
    )
    reasons = "".join(f"<li>{escape(reason)}</li>" for reason in report.reasons)
    roi = sampling.roi
    region = f" · x={roi.x}, y={roi.y}, {roi.width} x {roi.height}" if roi else ""
    return (
        f'<section data-status="{status}"><h3>Measured colors</h3>'
        f'<p class="status">{label}</p><p>Report {escape(report.id)} · '
        f"{escape(report.created_at.isoformat())}</p><p>Scope: <strong>{sampling.scope}</strong>"
        f"{region} · {sampling.width} x {sampling.height} px</p>"
        f"<p>{sampling.coordinate_policy} · {sampling.sampled_positions} positions "
        f"({sampling.sampled_fraction:.1%}); {sampling.core_samples} core, "
        f"{sampling.partial_alpha_samples} partial-alpha samples.</p>"
        f'<ul class="swatches">{measured}</ul><div class="table-wrap"><table>'
        "<caption>Target color distance (ΔE)</caption><thead><tr><th>Target</th>"
        "<th>Match share</th><th>Mean ΔE</th><th>Max ΔE</th></tr></thead>"
        f"<tbody>{targets}</tbody></table></div><p>ΔE threshold: {report.delta_e_threshold:g}; "
        f"profile: {report.profile_treatment}; policy: {report.analysis_policy}.</p>"
        f'<ul class="reasons">{reasons}</ul></section>'
    )


def distance(value: float | None) -> str:
    return "Unknown" if value is None else f"{value:.2f}"


def intent_markup(state: Session, artifact: Artifact) -> str:
    if artifact.palette_id is None:
        return (
            "<section><h3>Intended colors</h3><p>Legacy / unknown intent</p>"
            "<p>No palette version was bound to this artifact.</p></section>"
        )
    palette = state.palette(artifact.palette_id)
    return (
        f"<section><h3>Intended colors</h3><p>Palette {escape(palette.id)} · "
        f"Parent palette: {escape(palette.parent_palette_id or 'None')}</p>"
        f"{palette_body(palette)}</section>"
    )


def lockup_markup(artifact: Artifact) -> str:
    lockup = artifact.lockup
    if lockup is None:
        return "<section><h3>Requested lockup</h3><p>Unknown for this artifact.</p></section>"
    return (
        "<section><h3>Requested lockup</h3><dl>"
        f"<dt>Layout</dt><dd>{lockup.layout}</dd>"
        f"<dt>Symbol position</dt><dd>{lockup.symbol_position}</dd>"
        f"<dt>Text alignment</dt><dd>{lockup.text_alignment}</dd>"
        f"<dt>Typography direction</dt><dd>{escape(lockup.typography_style)}</dd>"
        f"<dt>Requested font reference</dt><dd>{escape(lockup.font_reference or 'None')}</dd>"
        '</dl><p class="muted">This is requested visual direction, not proof of a font file '
        "used in the raster. Gallery text uses the CSS system font.</p></section>"
    )
