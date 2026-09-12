"""Versioned JSON contracts at the brief, review, and session trust boundaries."""

from __future__ import annotations

from typing import Annotated, ClassVar, Final, Literal, NewType, override

from pydantic import BaseModel, ConfigDict, Field, JsonValue, TypeAdapter

SessionId = NewType("SessionId", str)
ArtifactId = NewType("ArtifactId", str)
type Identifier = Annotated[str, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
type Text = Annotated[str, Field(min_length=1, max_length=20000, pattern=r"\S")]
type Digest = Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]
type Background = Literal["opaque", "transparent"]
type LogoType = Literal[
    "wordmark", "lettermark", "monogram", "symbol", "abstract", "combination", "emblem", "mascot"
]


class ProjectError(Exception):
    """Carry a stable CLI error code; traceback state remains mutable for Python."""

    code: str
    detail: str

    def __init__(self, code: str, detail: str) -> None:
        self.code = code
        self.detail = detail
        super().__init__(detail)

    @override
    def __str__(self) -> str:
        return f"{self.code}: {self.detail}"


class FrozenModel(BaseModel):
    """Reject unknown keys and type coercion at external JSON boundaries."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid", strict=True)


PaletteId = NewType("PaletteId", str)
ReferenceId = NewType("ReferenceId", str)
ReportId = NewType("ReportId", str)

_STRICT_INTEGER: Final[TypeAdapter[int]] = TypeAdapter(int, config=ConfigDict(strict=True))


def schema_integer(value: JsonValue) -> int:
    """Prevent Literal equality from accepting true or 1.0 as a schema version."""
    return _STRICT_INTEGER.validate_python(value)
