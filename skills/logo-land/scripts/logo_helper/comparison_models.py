"""Strict selection inputs and portable comparison provenance contracts."""

from typing import Annotated, Literal, Self

from pydantic import Field, model_validator

from logo_helper.app_icon_models import AppIconIntent
from logo_helper.artifact_models import ImageFacts
from logo_helper.lockup_models import LockupIntent
from logo_helper.model_base import ArtifactId, Digest, FrozenModel, ProjectError, SessionId

type DecisionText = Annotated[str, Field(max_length=2000)]


class ComparisonItem(FrozenModel):
    """One explicit candidate and conversational notes, without approval semantics."""

    session: Annotated[SessionId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    revision: Annotated[int, Field(ge=0)]
    artifact: Annotated[ArtifactId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    rationale: DecisionText = ""
    preserve: DecisionText = ""
    change: DecisionText = ""
    observation: DecisionText = ""


class ComparisonSelection(FrozenModel):
    """A bounded, ordered selection spanning one or more sessions."""

    title: Annotated[str, Field(min_length=1, max_length=200, pattern=r"\S")]
    items: Annotated[tuple[ComparisonItem, ...], Field(min_length=1, max_length=60)]

    @model_validator(mode="after")
    def unique_sources(self) -> Self:
        identities = {(item.session, item.artifact) for item in self.items}
        if len(identities) != len(self.items):
            raise ProjectError("invalid_selection", "Choose distinct (session, artifact) pairs")
        return self


class ComparisonArtifact(FrozenModel):
    """Exact source identity, decoded facts and byte hashes for one candidate."""

    source: ComparisonItem
    parent_id: ArtifactId | None
    brand_name: str
    kind: Literal["brand", "app_icon"]
    style: str
    image_file: str
    prompt_file: str
    sha256: Digest
    prompt_sha256: Digest
    image: ImageFacts
    app_icon: AppIconIntent | None
    lockup: LockupIntent | None


class ComparisonManifest(FrozenModel):
    """An immutable comparison snapshot, separate from session selection/export."""

    schema_version: Literal[1] = 1
    kind: Literal["comparison_gallery"] = "comparison_gallery"
    title: str
    artifacts: tuple[ComparisonArtifact, ...]
    preview_note: str = (
        "Illustrative CSS contexts and sizes; original PNG bytes are unchanged. "
        "Candidate notes do not approve exports. Recheck source revisions before resuming."
    )


class ComparisonResult(FrozenModel):
    """Locations returned only after the complete gallery has been published."""

    path: str
    index_path: str
    count: int
