"""Deterministic palette proposals without session mutation."""

from __future__ import annotations

from functools import cache
from typing import TYPE_CHECKING, Final, Literal, Self, assert_never

from pydantic import model_validator

from logo_helper.color_math import RECIPES, HarmonyRecipe, delta_e, harmony_colors
from logo_helper.color_models import (
    ColorConstraints,
    HexColor,
    PaletteContent,
    SourceEvidence,
    Swatch,
)
from logo_helper.model_base import FrozenModel, ProjectError, Text

if TYPE_CHECKING:
    from collections.abc import Callable

MAX_DESIGN_COLORS: Final = 8


class PaletteRequest(FrozenModel):
    """A structured seed or supplied colors with independently composable constraints."""

    seed_hex: HexColor = "#247A52"
    constraints: ColorConstraints = ColorConstraints()
    source: Literal["local_harmony", "reference", "assistant", "leonardo"] = "local_harmony"
    source_evidence: SourceEvidence = SourceEvidence()
    selected_by: Literal["assistant", "user"] = "assistant"
    rationale: Text | None = None
    swatches: tuple[Swatch, ...] = ()
    extracted_colors: tuple[HexColor, ...] = ()

    @model_validator(mode="after")
    def consistent_source(self) -> Self:
        match self.source:
            case "local_harmony":
                valid = not self.swatches and not self.extracted_colors
            case "reference":
                valid = (
                    bool(self.extracted_colors)
                    and not self.swatches
                    and (self.source_evidence.reference_id is not None)
                )
            case "assistant" | "leonardo":
                valid = bool(self.swatches) and not self.extracted_colors
            case _:
                assert_never(self.source)
        if not valid:
            raise ProjectError(
                "invalid_palette_request", "Colors and evidence must match their source"
            )
        if len({*self.constraints.locked_hex, *self.constraints.required_hex}) > MAX_DESIGN_COLORS:
            raise ProjectError(
                "constraint_conflict", "At most eight mandatory design colors are supported"
            )
        return self


class PaletteProposal(FrozenModel):
    """Read-only candidates; the caller supplies its own session and revision wrapper."""

    candidates: tuple[PaletteContent, ...]
    warnings: tuple[Text, ...] = ()


def _build_candidate(
    request: PaletteRequest, recipe: HarmonyRecipe, distance: Callable[[str, str], float]
) -> PaletteContent:
    constraints = request.constraints
    mandatory = tuple(dict.fromkeys((*constraints.locked_hex, *constraints.required_hex)))
    seed = mandatory[0] if mandatory else request.seed_hex
    match request.source:
        case "assistant" | "leonardo":
            return PaletteContent(
                swatches=request.swatches,
                constraints=constraints,
                source=request.source,
                source_evidence=request.source_evidence,
                selected_by=request.selected_by,
                rationale=request.rationale
                or f"Validated {request.source} suggestion; constraints retained.",
            )
        case "local_harmony":
            colors = harmony_colors(seed, recipe)
            allowed = constraints.allowed_hex
            choices = (
                tuple(
                    sorted(
                        allowed,
                        key=lambda item: (
                            min(distance(item, target) for target in colors),
                            item,
                        ),
                    )
                )
                if allowed is not None
                else colors
            )
            rationale = f"{recipe.capitalize()} OKLCH companions; exact locks retained."
        case "reference":
            choices = tuple(
                color
                for color in request.extracted_colors
                if constraints.allowed_hex is None or color in constraints.allowed_hex
            )
            rationale = "Reference extraction order retained after exact locks and color limits."
        case _:
            assert_never(request.source)
    ordered = tuple(dict.fromkeys((*mandatory, *choices)))
    if not ordered:
        raise ProjectError("constraint_conflict", "No reference color satisfies the allowed set")
    limit = constraints.max_colors or max(3, len(mandatory))
    return PaletteContent(
        swatches=tuple(
            Swatch(hex=color, role="primary" if index == 0 else f"companion {index}")
            for index, color in enumerate(ordered[:limit])
        ),
        constraints=constraints,
        source=request.source,
        source_evidence=request.source_evidence,
        selected_by=request.selected_by,
        rationale=request.rationale or rationale,
    )


def propose_palette(
    request: PaletteRequest, *, recipe: HarmonyRecipe = "analogous"
) -> PaletteContent:
    """Produce one source-aware candidate; the recipe affects only local harmony."""
    return _build_candidate(request, recipe, cache(delta_e))


def propose_palettes(request: PaletteRequest) -> PaletteProposal:
    """Return up to three distinct local recipes or one validated supplied-color candidate."""
    recipes: tuple[HarmonyRecipe, ...]
    match request.source:
        case "local_harmony":
            recipes = RECIPES
        case "assistant" | "leonardo" | "reference":
            recipes = ("analogous",)
        case _:
            assert_never(request.source)
    distance = cache(delta_e)
    unique: dict[tuple[str, ...], PaletteContent] = {}
    for recipe in recipes:
        candidate = _build_candidate(request, recipe, distance)
        _ = unique.setdefault(tuple(sorted(s.hex for s in candidate.swatches)), candidate)
    warnings: tuple[str, ...] = ()
    if len(unique) < len(recipes):
        warnings = ("Constraints reduced the number of distinct palette candidates.",)
    return PaletteProposal(candidates=tuple(unique.values()), warnings=warnings)


def validate_candidate(
    candidate: PaletteContent, *, constraints: ColorConstraints
) -> PaletteContent:
    """Enforce both existing and new constraints without replacing any supplied colors."""
    prior = candidate.constraints
    allowed = constraints.allowed_hex
    if prior.allowed_hex is not None:
        allowed = tuple(color for color in prior.allowed_hex if allowed is None or color in allowed)
    limits = tuple(
        limit for limit in (prior.max_colors, constraints.max_colors) if limit is not None
    )
    merged = ColorConstraints(
        locked_hex=(*prior.locked_hex, *constraints.locked_hex),
        required_hex=(*prior.required_hex, *constraints.required_hex),
        allowed_hex=allowed,
        max_colors=min(limits) if limits else None,
        allow_gradients=prior.allow_gradients or constraints.allow_gradients,
    )
    return PaletteContent(
        swatches=candidate.swatches,
        constraints=merged,
        source=candidate.source,
        source_evidence=candidate.source_evidence,
        selected_by=candidate.selected_by,
        rationale=candidate.rationale,
        calculation_version=candidate.calculation_version,
    )
