"""Structural contracts for the installed public Hermes context, without Hermes imports."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Literal, NotRequired, Protocol, TypeAlias, TypedDict, Unpack

from pydantic import BaseModel, JsonValue, TypeAdapter

if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path

JsonObject: TypeAlias = dict[str, JsonValue]


class TextInput(TypedDict):
    """A public structured-completion text input."""

    type: Literal["text"]
    text: str


class ImageInput(TypedDict):
    """Raw PNG bytes use Hermes's public image-input route."""

    type: Literal["image"]
    data: bytes
    mime_type: Literal["image/png"]
    file_name: str


LlmInput: TypeAlias = TextInput | ImageInput


class ImageArguments(TypedDict):
    """Only native image_generate parameters; routing belongs to Hermes."""

    prompt: str
    aspect_ratio: Literal["square"]
    image_url: NotRequired[str]


class Completion(Protocol):
    """Read attribution and raw text; never trust the optional parsed field."""

    @property
    def text(self) -> str: ...

    @property
    def provider(self) -> str: ...

    @property
    def model(self) -> str: ...


class CompletionRequest(TypedDict):
    """Exact public keyword arguments, with no provider/model/profile overrides."""

    instructions: str
    input: Sequence[LlmInput]
    json_schema: JsonObject
    schema_name: str
    timeout: float
    max_tokens: int
    purpose: str


class StructuredLlm(Protocol):
    """The bounded subset of ctx.llm used by the host."""

    def complete_structured(self, **request: Unpack[CompletionRequest]) -> Completion: ...


class HermesContext(Protocol):
    """Transport capabilities required by HermesHost."""

    @property
    def llm(self) -> StructuredLlm: ...

    def dispatch_tool(self, tool_name: str, args: ImageArguments) -> str: ...


class ToolHandler(Protocol):
    """Native tool handlers return JSON and accept Hermes context keywords."""

    def __call__(self, args: JsonObject, **kwargs: JsonValue) -> str: ...


class RegistrationContext(HermesContext, Protocol):
    """Public registration methods used by the plugin entry point."""

    def register_tool(
        self, *, name: str, toolset: str, schema: JsonObject, handler: ToolHandler
    ) -> None: ...

    def register_skill(self, name: str, path: Path, description: str = "") -> None: ...


def schema_for(model: type[BaseModel]) -> JsonObject:
    return TypeAdapter(JsonObject).validate_json(json.dumps(model.model_json_schema()))
