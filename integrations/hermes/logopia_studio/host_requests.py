"""Action-specific tool schemas reject missing, stale and inappropriate fields."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal, TypeAlias

from pydantic import ConfigDict, Field, RootModel, ValidationError

from .models import FeedbackEnvelope, StudioBrief, StudioError
from .models_base import FrozenModel, Identifier, Revision

if TYPE_CHECKING:
    from .host_api import JsonObject


class StartRequest(FrozenModel):
    """Model arguments identify a workflow, never a filesystem location."""

    workflow_id: Identifier
    brief: StudioBrief


class StatusRequest(FrozenModel):
    """Status accepts no mutation fields."""

    workflow_id: Identifier
    action: Literal["status"]


class ContinueRequest(FrozenModel):
    """Continue resumes the saved workflow at an explicit revision."""

    workflow_id: Identifier
    action: Literal["continue"]
    expected_revision: Revision


class DeliverRequest(FrozenModel):
    """Delivery uses the canonical selection, never a candidate override."""

    workflow_id: Identifier
    action: Literal["deliver"]
    expected_revision: Revision


class ReconcileRequest(FrozenModel):
    """Reconciliation names an exact saved job and dispatches no inference."""

    workflow_id: Identifier
    action: Literal["reconcile"]
    expected_revision: Revision
    job_id: Identifier


Action: TypeAlias = Annotated[
    StatusRequest | ContinueRequest | DeliverRequest | FeedbackEnvelope | ReconcileRequest,
    Field(discriminator="action"),
]


class ActionRequest(RootModel[Action]):
    """Strict discriminated union matching the native action tool."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, strict=True)


def tool_json(args: JsonObject) -> str:
    try:
        raw = json.dumps(args, ensure_ascii=False, allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise StudioError("invalid_request", "Tool arguments must be JSON") from exc
    if len(raw.encode("utf-8")) > 32 * 1024:
        raise StudioError("invalid_request", "Tool arguments exceed 32 KiB")
    return raw


def parse_action(args: JsonObject) -> Action:
    try:
        return ActionRequest.model_validate_json(tool_json(args)).root
    except ValidationError as exc:
        raise StudioError("invalid_request", str(exc)) from exc


def parse_start(args: JsonObject) -> StartRequest:
    try:
        return StartRequest.model_validate_json(tool_json(args))
    except ValidationError as exc:
        raise StudioError("invalid_request", str(exc)) from exc
