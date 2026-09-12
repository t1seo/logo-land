"""Frozen schema-1 parser; legacy reads never infer color or lockup intent."""

from datetime import datetime
from typing import Annotated, Final, Literal, Self, assert_never

from pydantic import BeforeValidator, Field, TypeAdapter, model_validator

from logo_helper.model_base import (
    ArtifactId,
    Background,
    Digest,
    FrozenModel,
    LogoType,
    ProjectError,
    SessionId,
    Text,
    schema_integer,
)
from logo_helper.session_models import Session


class LegacyBrief(FrozenModel):
    """Brand intent; exact_text and slogan are preserved verbatim."""

    brand_name: Text
    exact_text: Annotated[str, Field(max_length=2000)]
    industry: Text
    audience: Text
    slogan: str = ""
    logo_type: LogoType = "combination"
    styles: tuple[Text, ...] = ()
    palette: tuple[Text, ...] = ()
    forbidden: tuple[Text, ...] = ()
    use_cases: tuple[Text, ...] = ()
    assumptions: tuple[Text, ...] = ()
    background: Background = "opaque"
    concept_count: Annotated[int, Field(ge=1)] = 3


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


class LegacyArtifact(FrozenModel):
    """Immutable image provenance with a replaceable explicit visual review."""

    id: Annotated[ArtifactId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    path: str
    sha256: Digest
    image: ImageFacts
    prompt: Text
    parent_id: ArtifactId | None = None
    created_at: datetime
    requested_background: Background | None = None
    review: VisualReview | None = None
    reviewed_at: datetime | None = None

    def effective_background(self, brief: LegacyBrief) -> Background:
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


class LegacySession(FrozenModel):
    """Persisted session with ordered, acyclic parent lineage and revision control."""

    schema_version: Annotated[Literal[1], BeforeValidator(schema_integer)] = 1
    id: Annotated[SessionId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    revision: Annotated[int, Field(ge=0)] = 0
    created_at: datetime
    updated_at: datetime
    brief: LegacyBrief
    artifacts: tuple[LegacyArtifact, ...] = ()
    selected_id: ArtifactId | None = None
    failures: tuple[FailedAttempt, ...] = ()
    exports: tuple[ExportRecord, ...] = ()

    @model_validator(mode="after")
    def consistent_lineage(self) -> Self:
        """Reject tampered paths, duplicate IDs, missing parents, and cycles on resume."""
        seen: set[ArtifactId] = set()
        for artifact in self.artifacts:
            if artifact.id in seen or (
                artifact.parent_id is not None and artifact.parent_id not in seen
            ):
                raise ProjectError(
                    "invalid_state", "Duplicate artifact ID or invalid parent lineage"
                )
            if artifact.path != f"artifacts/{artifact.id}.png":
                raise ProjectError(
                    "unsafe_path", "LegacyArtifact path does not match its immutable ID"
                )
            seen.add(artifact.id)
        if self.selected_id is not None and self.selected_id not in seen:
            raise ProjectError("invalid_state", "Selected artifact does not exist")
        if any(item.parent_id is not None and item.parent_id not in seen for item in self.failures):
            raise ProjectError("invalid_state", "Failed attempt parent does not exist")
        if any(item.artifact_id not in seen for item in self.exports):
            raise ProjectError("invalid_state", "Export artifact does not exist")
        return self

    def artifact(self, identifier: ArtifactId) -> LegacyArtifact:
        """Resolve an explicit identifier without silently selecting a latest image."""
        for artifact in self.artifacts:
            if artifact.id == identifier:
                return artifact
        raise ProjectError("not_found", f"LegacyArtifact {identifier!r} does not exist")


type StoredSession = LegacySession | Session
_SESSION_ADAPTER: Final[TypeAdapter[StoredSession]] = TypeAdapter(StoredSession)


def parse_stored_session(data: str | bytes) -> LegacySession | Session:
    """Parse the original schema without rewriting or widening its allowed fields."""
    return _SESSION_ADAPTER.validate_json(data)


def parse_session(data: str | bytes) -> Session:
    """Dispatch strictly by schema; migrate only the validated in-memory model."""
    parsed = parse_stored_session(data)
    match parsed:
        case LegacySession() as legacy:
            return Session.model_validate_json(legacy.model_dump_json(exclude={"schema_version"}))
        case Session() as current:
            return current
        case _:
            assert_never(parsed)
