"""Portable immutable reference-image provenance and oriented analysis bounds."""

from datetime import datetime
from typing import Annotated, Literal, Self, assert_never

from pydantic import Field, model_validator

from logo_helper.model_base import Digest, FrozenModel, ProjectError, ReferenceId


class RegionOfInterest(FrozenModel):
    """Integer bounds in the EXIF-oriented decoded image."""

    x: Annotated[int, Field(ge=0)]
    y: Annotated[int, Field(ge=0)]
    width: Annotated[int, Field(gt=0)]
    height: Annotated[int, Field(gt=0)]

    def contained_by(self, width: int, height: int) -> bool:
        return self.x + self.width <= width and self.y + self.height <= height


class Reference(FrozenModel):
    """Original bytes with their actual decoder facts, not an edit-parent image."""

    id: Annotated[ReferenceId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    path: str
    sha256: Digest
    format: Literal["PNG", "JPEG"]
    width: Annotated[int, Field(gt=0)]
    height: Annotated[int, Field(gt=0)]
    exif_orientation: Annotated[int, Field(ge=1, le=8)] = 1
    roi: RegionOfInterest | None = None
    created_at: datetime

    @model_validator(mode="after")
    def valid_scope(self) -> Self:
        width, height = self.width, self.height
        if self.exif_orientation in {5, 6, 7, 8}:
            width, height = height, width
        if self.roi is not None and not self.roi.contained_by(width, height):
            raise ProjectError("invalid_roi", "Reference ROI leaves the oriented image")
        match self.format:
            case "PNG":
                extension = "png"
            case "JPEG":
                extension = "jpg"
            case _:
                assert_never(self.format)
        if self.path != f"references/{self.id}.{extension}":
            raise ProjectError("unsafe_path", "Reference path does not match its ID and format")
        return self
