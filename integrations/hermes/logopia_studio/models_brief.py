"""Saved design intent and structured planning results."""

from typing import Annotated, Literal, Self, assert_never

from pydantic import Field, model_validator

from .models_base import Background, Count, FrozenModel, Identifier, Note, Prompt, StudioError, Text


class StudioBrief(FrozenModel):
    """Native workflow scope; text and colors are preserved as supplied."""

    name: Text
    exact_text: Note
    product: Text
    audience: Text
    personality: Text
    use_case: Text
    display_width: Annotated[int, Field(ge=16, le=1024)] = 192
    logo_type: Literal[
        "wordmark",
        "lettermark",
        "monogram",
        "symbol",
        "abstract",
        "combination",
        "emblem",
        "mascot",
    ] = "combination"
    mode: Literal["brand", "app_icon", "ip"] = "brand"
    background: Background = "opaque"
    count: Count | None = None
    colors: Annotated[tuple[Text, ...], Field(max_length=12)] = ()
    notes: Note = ""
    color_policy: Literal["advisory"] = "advisory"

    @model_validator(mode="after")
    def supported_intent(self) -> Self:
        if self.mode in {"app_icon", "ip"} and (
            self.background != "opaque" or self.exact_text != ""
        ):
            raise StudioError("unsupported_intent", "App/IP requires opaque and empty exact_text")
        return self

    @property
    def effective_count(self) -> int:
        if self.count is not None:
            return self.count
        match self.mode:
            case "brand" | "app_icon":
                return 3
            case "ip":
                return 6
            case _:
                assert_never(self.mode)


class Strategy(FrozenModel):
    """Design proposals, not claims of researched market facts."""

    positioning: Text
    audience_need: Text
    brand_promise: Text
    distinctive_principle: Text
    typography: Text
    color_roles: Text
    assumptions: Annotated[tuple[Text, ...], Field(max_length=12)]


class Direction(FrozenModel):
    """One independently generated candidate direction."""

    id: Identifier
    title: Text
    motif: Text
    construction: Text
    rationale: Text
    risk: Text
    preserve: Annotated[tuple[Text, ...], Field(max_length=20)]
    prompt: Prompt


class PlanResult(FrozenModel):
    """Attribution and exact ordered output of a single planning attempt."""

    strategy: Strategy
    directions: Annotated[tuple[Direction, ...], Field(min_length=1, max_length=6)]
    provider: Text
    model: Text

    @model_validator(mode="after")
    def unique_directions(self) -> Self:
        if len({item.id for item in self.directions}) != len(self.directions):
            raise StudioError("invalid_plan", "Direction IDs must be unique")
        return self
