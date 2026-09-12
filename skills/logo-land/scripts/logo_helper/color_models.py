"""Normalized sRGB palette intent and composable constraints."""

from __future__ import annotations

import hashlib
import json
import re
from typing import Annotated, Final, Literal, Self

from pydantic import AfterValidator, Field, field_validator, model_validator

from logo_helper.model_base import Digest, FrozenModel, PaletteId, ProjectError, ReferenceId, Text

SHORT_HEX_LENGTH: Final = 3
MAX_PALETTE_COLORS: Final = 8


def normalize_hex(value: str) -> str:
    """Accept only opaque short or full sRGB HEX, without trimming or guessing."""
    if re.fullmatch(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?", value) is None:
        raise ProjectError("invalid_color", "Use #RGB or #RRGGBB without alpha")
    digits = value[1:]
    if len(digits) == SHORT_HEX_LENGTH:
        digits = "".join(char * 2 for char in digits)
    return f"#{digits.upper()}"


type HexColor = Annotated[str, AfterValidator(normalize_hex)]


class ColorConstraints(FrozenModel):
    """Independent color requirements; an allowed list does not require presence."""

    locked_hex: tuple[HexColor, ...] = ()
    allowed_hex: tuple[HexColor, ...] | None = None
    max_colors: Annotated[int, Field(ge=1, le=8)] | None = None
    required_hex: tuple[HexColor, ...] = ()
    allow_gradients: bool = False

    @field_validator("locked_hex", "allowed_hex", "required_hex")
    @classmethod
    def distinct_colors(cls, values: tuple[str, ...] | None) -> tuple[str, ...] | None:
        if values is None:
            return None
        unique = tuple(dict.fromkeys(values))
        if len(unique) > MAX_PALETTE_COLORS:
            raise ProjectError(
                "constraint_conflict", "Each constraint list supports at most eight unique colors"
            )
        return unique

    @model_validator(mode="after")
    def consistent_constraints(self) -> Self:
        required = {*self.locked_hex, *self.required_hex}
        if self.allowed_hex is not None and (
            not self.allowed_hex or not required.issubset(self.allowed_hex)
        ):
            raise ProjectError(
                "constraint_conflict", "Allowed colors must contain locks and requirements"
            )
        if self.max_colors is not None and len(required) > self.max_colors:
            raise ProjectError(
                "constraint_conflict", "Required and locked colors exceed max_colors"
            )
        if self.allow_gradients and (self.allowed_hex is not None or self.max_colors is not None):
            raise ProjectError(
                "constraint_conflict", "Gradients conflict with an allowed set or color count"
            )
        return self

    @property
    def strict(self) -> bool:
        return (
            bool(self.locked_hex or self.required_hex)
            or self.allowed_hex is not None
            or self.max_colors is not None
        )


class Swatch(FrozenModel):
    """One intended design color with a human-readable role."""

    hex: HexColor
    role: Text


class SourceEvidence(FrozenModel):
    """Portable reference or provider provenance; responses remain inert text."""

    reference_id: Annotated[ReferenceId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")] | None = None
    reference_sha256: Digest | None = None
    provider: Text | None = None
    tool: Text | None = None
    response: Text | None = None
    notes: tuple[Text, ...] = ()

    @model_validator(mode="after")
    def paired_reference(self) -> Self:
        if (self.reference_id is None) != (self.reference_sha256 is None):
            raise ProjectError("invalid_state", "Reference evidence needs both ID and hash")
        return self


class PaletteContent(FrozenModel):
    """Canonical immutable intent independent of its version ID or lineage."""

    swatches: Annotated[tuple[Swatch, ...], Field(min_length=1)]
    constraints: ColorConstraints = ColorConstraints()
    source: Literal["assistant", "local_harmony", "reference", "leonardo"]
    source_evidence: SourceEvidence = SourceEvidence()
    selected_by: Literal["assistant", "user"]
    rationale: Text
    calculation_version: Text = "logo-color-v1"

    @field_validator("swatches")
    @classmethod
    def distinct_swatches(cls, values: tuple[Swatch, ...]) -> tuple[Swatch, ...]:
        unique: dict[str, Swatch] = {}
        for value in values:
            _ = unique.setdefault(value.hex, value)
        if len(unique) > MAX_PALETTE_COLORS:
            raise ProjectError(
                "constraint_conflict", "A palette supports at most eight design colors"
            )
        return tuple(unique.values())

    @model_validator(mode="after")
    def satisfies_constraints(self) -> Self:
        colors = {swatch.hex for swatch in self.swatches}
        constraints = self.constraints
        required = {*constraints.locked_hex, *constraints.required_hex}
        if not required.issubset(colors):
            raise ProjectError(
                "constraint_conflict", "Palette is missing a locked or required color"
            )
        if constraints.allowed_hex is not None and not colors.issubset(constraints.allowed_hex):
            raise ProjectError(
                "constraint_conflict", "Palette contains a color outside the allowed set"
            )
        if constraints.max_colors is not None and len(colors) > constraints.max_colors:
            raise ProjectError("constraint_conflict", "Palette exceeds max_colors")
        return self


def palette_digest(content: PaletteContent) -> str:
    """Hash normalized content, excluding identity/lineage and the digest itself."""
    data = content.model_dump(mode="json", include=set(PaletteContent.model_fields))
    encoded = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


class PaletteVersion(PaletteContent):
    """One version whose content digest is verified at each JSON boundary."""

    id: Annotated[PaletteId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    parent_palette_id: Annotated[PaletteId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")] | None = (
        None
    )
    digest: Digest

    @model_validator(mode="after")
    def verified_digest(self) -> Self:
        if self.digest != palette_digest(self):
            raise ProjectError(
                "digest_mismatch", "Palette content differs from its canonical digest"
            )
        return self
