"""Typed sampled measurements bound to original bytes and palette intent."""

from datetime import datetime
from typing import Annotated, Literal, Self

from pydantic import Field, model_validator

from logo_helper.color_models import HexColor
from logo_helper.model_base import (
    ArtifactId,
    Digest,
    FrozenModel,
    PaletteId,
    ProjectError,
    ReportId,
    Text,
)
from logo_helper.reference_models import RegionOfInterest

type Share = Annotated[float, Field(ge=0, le=1, allow_inf_nan=False)]
type Distance = Annotated[float, Field(ge=0, allow_inf_nan=False)]
type Count = Annotated[int, Field(ge=0)]


class MeasuredSwatch(FrozenModel):
    """Estimated color share in the declared sample scope."""

    hex: HexColor
    samples: Count
    share: Share


class TargetMeasurement(FrozenModel):
    """Matching core sample evidence against one intended sRGB target."""

    hex: HexColor
    matching_samples: Count
    share: Share
    mean_delta_e: Distance | None = None
    max_delta_e: Distance | None = None


class ContrastMeasurement(FrozenModel):
    """Explicit composited foreground/surface readability guidance."""

    foreground: HexColor
    surface: HexColor
    ratio: Annotated[float, Field(ge=1, le=21, allow_inf_nan=False)]
    alpha: Share = 1.0


class SamplingSettings(FrozenModel):
    """Deterministic coordinate scope with auditable alpha sample counts."""

    width: Annotated[int, Field(gt=0)]
    height: Annotated[int, Field(gt=0)]
    roi: RegionOfInterest | None = None
    scope: Literal["full_image", "roi"] = "full_image"
    coordinate_policy: Literal["all_pixels", "grid_128_pixel_centers"] = "all_pixels"
    sampled_positions: Annotated[int, Field(ge=0, le=16384)]
    sampled_fraction: Share
    visible_samples: Count
    core_samples: Count
    partial_alpha_samples: Count

    @model_validator(mode="after")
    def consistent_samples(self) -> Self:
        if (self.scope == "roi") != (self.roi is not None):
            raise ProjectError("invalid_state", "Sampling scope must agree with its ROI")
        if self.roi is not None and not self.roi.contained_by(self.width, self.height):
            raise ProjectError("invalid_roi", "Sampling ROI leaves the image")
        if self.core_samples + self.partial_alpha_samples != self.visible_samples:
            raise ProjectError(
                "invalid_state", "Visible samples must equal core plus partial alpha"
            )
        if self.visible_samples > self.sampled_positions:
            raise ProjectError("invalid_state", "Visible samples exceed sampled positions")
        return self


class ColorReport(FrozenModel):
    """Immutable evidence; a stored pass never substitutes for export recomputation."""

    id: Annotated[ReportId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    artifact_id: Annotated[ArtifactId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    artifact_sha256: Digest
    palette_id: Annotated[PaletteId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")] | None = None
    palette_digest: Digest | None = None
    analysis_policy: Literal["logo-color-v1"] = "logo-color-v1"
    color_engine_version: Text
    pillow_version: Text
    profile_treatment: Literal["declared_srgb", "converted_icc", "assumed_srgb", "unsupported"]
    sampling: SamplingSettings
    status: Literal["pass", "mismatch", "indeterminate", "unverified"]
    reasons: tuple[Text, ...] = ()
    measured_swatches: tuple[MeasuredSwatch, ...] = ()
    targets: tuple[TargetMeasurement, ...] = ()
    matched_fraction: Share | None = None
    unmatched_fraction: Share | None = None
    observed_colors: Count | None = None
    minor_swatches: tuple[MeasuredSwatch, ...] = ()
    contrasts: tuple[ContrastMeasurement, ...] = ()
    delta_e_threshold: Distance = 5.0
    created_at: datetime

    @model_validator(mode="after")
    def consistent_binding(self) -> Self:
        if (self.palette_id is None) != (self.palette_digest is None):
            raise ProjectError("invalid_state", "Report palette ID and digest must be paired")
        if self.status != "pass" and not self.reasons:
            raise ProjectError("invalid_state", "Non-pass reports require an explicit reason")
        return self
