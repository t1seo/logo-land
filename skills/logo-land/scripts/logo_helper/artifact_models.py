"""Immutable PNG provenance and explicit visual assessments."""

from datetime import datetime
from typing import Annotated, Literal

from pydantic import Field

from logo_helper.app_icon_models import AppIconIntent, omit_absent
from logo_helper.brief_models import Brief
from logo_helper.lockup_models import LockupIntent
from logo_helper.model_base import ArtifactId, Background, Digest, FrozenModel, PaletteId, Text


class VisualReview(FrozenModel):
    """An explicit host visual assessment, never inferred from image metadata."""

    reviewer: Text
    notes: Text
    text_correct: bool
    composition_ok: bool
    small_size_ok: bool
    preservation_ok: bool
    background_checked: bool

    @property
    def passed(self) -> bool:
        return all(
            (
                self.text_correct,
                self.composition_ok,
                self.small_size_ok,
                self.preservation_ok,
                self.background_checked,
            )
        )


class ImageFacts(FrozenModel):
    """Facts obtained from actual PNG decoding, including visible alpha pixels."""

    format: Literal["PNG"] = "PNG"
    width: Annotated[int, Field(gt=0)]
    height: Annotated[int, Field(gt=0)]
    alpha_min: Annotated[int, Field(ge=0, le=255)]
    alpha_max: Annotated[int, Field(gt=0, le=255)]
    transparent_pixels: Annotated[int, Field(ge=0)]
    visible_pixels: Annotated[int, Field(gt=0)]

    @property
    def has_transparency(self) -> bool:
        return self.transparent_pixels > 0


class Artifact(FrozenModel):
    """Immutable image provenance with a replaceable explicit visual review."""

    id: Annotated[ArtifactId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    path: str
    sha256: Digest
    image: ImageFacts
    prompt: Text
    parent_id: ArtifactId | None = None
    created_at: datetime
    requested_background: Background | None = None
    palette_id: PaletteId | None = None
    lockup: LockupIntent | None = None
    app_icon: AppIconIntent | None = Field(default=None, exclude_if=omit_absent)
    review: VisualReview | None = None
    reviewed_at: datetime | None = None

    def effective_background(self, brief: Brief) -> Background:
        return (
            self.requested_background if self.requested_background is not None else brief.background
        )


class FailedAttempt(FrozenModel):
    """A failed host call recorded without fabricating a successful artifact."""

    prompt: Text
    reason: Text
    parent_id: ArtifactId | None = None
    created_at: datetime


class ExportRecord(FrozenModel):
    """A delivery directory and the exact selected artifact it contains."""

    path: str
    artifact_id: ArtifactId
    created_at: datetime
