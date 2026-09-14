from __future__ import annotations

import json
from typing import TYPE_CHECKING, Literal, TypeAlias, assert_never

import pytest
from logopia_studio import registration
from logopia_studio.engine import Studio
from logopia_studio.host_api import JsonObject
from logopia_studio.models import FeedbackEnvelope, StudioError, Workflow
from pydantic import TypeAdapter
from tests.hermes.test_host_fakes import FakeContext, brief
from tests.hermes.test_host_registration import configured_root, stored_state

if TYPE_CHECKING:
    from pathlib import Path

    from logopia_studio.models import StudioBrief

TestAction: TypeAlias = Literal["start", "continue", "choose", "revise", "deliver", "reconcile"]


def action_arguments(state: Workflow, action: TestAction) -> JsonObject:
    match action:
        case "start":
            return {
                "workflow_id": state.id,
                "brief": TypeAdapter(JsonObject).validate_json(brief().model_dump_json()),
            }
        case "choose" | "revise":
            feedback = FeedbackEnvelope(
                workflow_id=state.id,
                expected_revision=state.revision,
                candidate_id="one",
                candidate_sha256=state.candidates[0].sha256,
                action=action,
                keep=("Exact text",),
                change="Open the counter" if action == "revise" else "",
            )
            return TypeAdapter(JsonObject).validate_json(feedback.model_dump_json())
        case "reconcile":
            return {
                "workflow_id": state.id,
                "action": action,
                "expected_revision": state.revision,
                "job_id": "job-1",
            }
        case "continue" | "deliver":
            return {"workflow_id": state.id, "action": action, "expected_revision": state.revision}
        case _:
            assert_never(action)


@pytest.mark.parametrize(
    "action", ["start", "continue", "choose", "revise", "deliver", "reconcile"]
)
def test_mutating_actions_route_exact_arguments_and_publish_a_fresh_gallery(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    action: TestAction,
) -> None:
    plugin_root = configured_root(tmp_path)
    state = stored_state(tmp_path)
    called: list[str] = []
    outputs: list[Path] = []

    def create(studio: Studio, workflow_id: str, saved_brief: StudioBrief) -> Workflow:
        del studio
        assert workflow_id == state.id
        assert saved_brief == brief()
        called.append("create")
        return state

    def status(studio: Studio, workflow_id: str) -> Workflow:
        del studio
        assert workflow_id == state.id
        return state

    def stage(studio: Studio, workflow_id: str, expected_revision: int) -> Workflow:
        del studio
        assert (workflow_id, expected_revision) == (state.id, state.revision)
        called.append("stage")
        return state

    def choose(
        studio: Studio, workflow_id: str, expected_revision: int, candidate_id: str
    ) -> Workflow:
        assert candidate_id == "one"
        return stage(studio, workflow_id, expected_revision)

    def revise(
        studio: Studio,
        workflow_id: str,
        expected_revision: int,
        candidate_id: str,
        keep: tuple[str, ...],
        change: str,
    ) -> Workflow:
        assert keep == ("Exact text",)
        assert change == "Open the counter"
        return choose(studio, workflow_id, expected_revision, candidate_id)

    def reconcile(
        studio: Studio, workflow_id: str, expected_revision: int, job_id: str
    ) -> Workflow:
        assert job_id == "job-1"
        return stage(studio, workflow_id, expected_revision)

    def publish(workspace: Path, snapshot: Workflow, output: Path) -> Path:
        assert workspace == tmp_path
        assert snapshot == state
        assert not output.exists()
        outputs.append(output)
        return output / "index.html"

    monkeypatch.setattr(Studio, "create", create)
    monkeypatch.setattr(Studio, "status", status)
    monkeypatch.setattr(Studio, "produce", stage)
    monkeypatch.setattr(Studio, "choose", choose)
    monkeypatch.setattr(Studio, "revise", revise)
    monkeypatch.setattr(Studio, "deliver", stage)
    monkeypatch.setattr(Studio, "reconcile", reconcile)
    monkeypatch.setattr(registration, "publish_gallery", publish)
    ctx = FakeContext()
    registration.register(ctx, plugin_root)
    args = action_arguments(state, action)
    handler = ctx.handlers["logopia_start" if action == "start" else "logopia_action"]
    for _ in range(2):
        result = TypeAdapter(JsonObject).validate_json(handler(args))
        assert result["success"] is True
        assert result["gallery"] == str(outputs[-1] / "index.html")
    assert len(outputs) == 2
    assert outputs[0] != outputs[1]
    assert called == (["create", "stage"] * 2 if action == "start" else ["stage", "stage"])
    assert not ctx.llm.calls
    assert not ctx.dispatches


def test_repeated_core_error_remains_visible_without_gallery_or_fallback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    plugin_root = configured_root(tmp_path)
    ctx = FakeContext()

    def interrupted(studio: Studio, workflow_id: str, expected_revision: int) -> Workflow:
        del studio, workflow_id, expected_revision
        raise StudioError("outcome_unknown", "First native request has no confirmed outcome")

    monkeypatch.setattr(Studio, "produce", interrupted)
    registration.register(ctx, plugin_root)
    responses = [
        ctx.handlers["logopia_action"](
            {
                "workflow_id": "sample",
                "action": "continue",
                "expected_revision": 4,
            }
        )
        for _ in range(2)
    ]
    assert responses[0] == responses[1]
    assert json.loads(responses[0]) == {
        "success": False,
        "error": "outcome_unknown",
        "detail": "First native request has no confirmed outcome",
    }
    assert not (tmp_path / "output").exists()
    assert not ctx.llm.calls
    assert not ctx.dispatches
