from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from logopia_studio.host_api import JsonObject
from logopia_studio.host_requests import parse_action, parse_start
from logopia_studio.host_settings import load_settings
from logopia_studio.models import FeedbackEnvelope, StudioError
from pydantic import TypeAdapter
from tests.hermes.test_host_fakes import brief

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize(
    "args",
    [
        {"workflow_id": "sample"},
        {"workflow_id": "sample", "action": "unknown"},
        {"workflow_id": "sample", "action": "continue"},
        {"workflow_id": "sample", "action": "continue", "expected_revision": True},
        {"workflow_id": "sample", "action": "continue", "expected_revision": "2"},
        {"workflow_id": "sample", "action": "status", "expected_revision": 2},
        {"workflow_id": "sample", "action": "status", "workspace": "/untrusted/elsewhere"},
        {"workflow_id": "../escape", "action": "status"},
        {
            "workflow_id": "sample",
            "action": "deliver",
            "expected_revision": 2,
            "candidate_id": "one",
        },
        {
            "workflow_id": "sample",
            "action": "choose",
            "expected_revision": 2,
            "candidate_id": "one",
        },
        {"workflow_id": "sample", "action": "reconcile", "expected_revision": 2},
    ],
)
def test_inappropriate_or_missing_fields_are_rejected(args: JsonObject) -> None:
    with pytest.raises(StudioError, match="invalid_request"):
        _ = parse_action(args)


def test_gallery_feedback_uses_the_core_envelope_and_rejects_stale_shape() -> None:
    request = FeedbackEnvelope(
        workflow_id="sample",
        expected_revision=2,
        candidate_id="candidate",
        candidate_sha256="a" * 64,
        action="revise",
        keep=("Exact text",),
        change="Open the counter",
    )
    args = TypeAdapter(JsonObject).validate_json(request.model_dump_json())
    assert parse_action(args) == request
    for invalid in (
        {**args, "schema_version": True},
        {**args, "change": " "},
        {**args, "change": "a" * 2001},
        {**args, "model": "replacement"},
        {**args, "action": "choose", "change": "Unexpected edit"},
    ):
        with pytest.raises(StudioError):
            _ = parse_action(invalid)


def test_start_rejects_strict_color_policy_and_excess_payload() -> None:
    data = TypeAdapter(JsonObject).validate_json(brief().model_dump_json())
    assert parse_start({"workflow_id": "sample", "brief": data}).brief == brief()
    with pytest.raises(StudioError):
        _ = parse_start({"workflow_id": "sample", "brief": {**data, "color_policy": "strict"}})
    with pytest.raises(StudioError, match="32 KiB"):
        _ = parse_action({"workflow_id": "sample", "action": "status", "extra": "한" * 12000})


@pytest.mark.parametrize("kind", ["missing", "relative", "unknown", "bool_version", "missing_root"])
def test_settings_fail_clearly_without_defaults_or_model_overrides(
    tmp_path: Path, kind: str
) -> None:
    data: JsonObject = {
        "schema_version": 1,
        "workspace": str(tmp_path),
        "helper_repo": str(tmp_path),
    }
    if kind == "relative":
        data["workspace"] = "relative"
    if kind == "unknown":
        data["model"] = "replacement"
    if kind == "bool_version":
        data["schema_version"] = True
    if kind == "missing_root":
        data["workspace"] = str(tmp_path / "absent")
    if kind != "missing":
        _ = (tmp_path / "settings.json").write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(StudioError):
        _ = load_settings(tmp_path)
