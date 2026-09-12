"""Preserve successful PNG imports even when their initial color analysis fails."""

from __future__ import annotations

from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING
from uuid import uuid4

from PIL import __version__ as pillow_version
from pydantic import ValidationError

from logo_helper.color_analysis import analyze_png
from logo_helper.models import ColorReport, ProjectError, ReportId, SamplingSettings

if TYPE_CHECKING:
    from logo_helper.models import Artifact, PaletteVersion


def initial_report(data: bytes, artifact: Artifact, palette: PaletteVersion) -> ColorReport:
    report_id = ReportId(f"report-{uuid4().hex}")
    try:
        return analyze_png(data, artifact, palette, report_id=report_id)
    except (ProjectError, OSError, ValidationError) as error:
        reason = f"Initial color analysis failed: {error}"
    try:
        engine_version = version("coloraide")
    except PackageNotFoundError:
        engine_version = "unavailable"
    return ColorReport(
        id=report_id,
        artifact_id=artifact.id,
        artifact_sha256=artifact.sha256,
        palette_id=palette.id,
        palette_digest=palette.digest,
        color_engine_version=engine_version,
        pillow_version=pillow_version,
        profile_treatment="unsupported",
        sampling=SamplingSettings(
            width=artifact.image.width,
            height=artifact.image.height,
            sampled_positions=0,
            sampled_fraction=0.0,
            visible_samples=0,
            core_samples=0,
            partial_alpha_samples=0,
        ),
        status="unverified",
        reasons=(reason,),
        created_at=datetime.now(UTC),
    )
