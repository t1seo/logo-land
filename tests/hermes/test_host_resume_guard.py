from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from logopia_studio import registration
from logopia_studio.engine import Studio
from logopia_studio.host_api import JsonObject
from pydantic import TypeAdapter
from tests.hermes.test_host_actions import action_arguments
from tests.hermes.test_host_fakes import FakeContext
from tests.hermes.test_host_registration import configured_root, stored_state

if TYPE_CHECKING:
    from pathlib import Path

    from logopia_studio.models import Phase, StudioBrief, Workflow


def invoke_start(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, phase: Phase
) -> tuple[JsonObject, list[str], Workflow]:
    plugin = configured_root(tmp_path)
    state = stored_state(tmp_path).model_copy(update={"phase": phase})
    calls: list[str] = []

    def create(studio: Studio, workflow_id: str, brief: StudioBrief) -> Workflow:
        del studio
        assert workflow_id == state.id
        assert brief == state.brief
        calls.append("create")
        return state

    def produce(studio: Studio, workflow_id: str, expected_revision: int) -> Workflow:
        del studio
        assert (workflow_id, expected_revision) == (state.id, state.revision)
        calls.append("produce")
        return state

    def publish(workspace: Path, current: Workflow, output: Path) -> Path:
        assert workspace == tmp_path
        assert current == state
        return output / "index.html"

    monkeypatch.setattr(Studio, "create", create)
    monkeypatch.setattr(Studio, "produce", produce)
    monkeypatch.setattr(registration, "publish_gallery", publish)
    context = FakeContext()
    registration.register(context, plugin)
    result = TypeAdapter(JsonObject).validate_json(
        context.handlers["logopia_start"](action_arguments(state, "start"))
    )
    assert context.llm.calls == []
    assert context.dispatches == []
    return result, calls, state


def test_start_of_a_draft_still_routes_to_production(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    result, calls, state = invoke_start(tmp_path, monkeypatch, "draft")
    assert calls == ["create", "produce"]
    assert result["workflow_id"] == state.id
    assert result["revision"] == state.revision


@pytest.mark.parametrize("phase", ["failed", "outcome_unknown", "cancelled"])
def test_repeated_start_cannot_implicitly_retry_interrupted_work(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, phase: Phase
) -> None:
    result, calls, state = invoke_start(tmp_path, monkeypatch, phase)
    assert calls == ["create"]
    assert result["success"] is False
    assert result["phase"] == phase
    assert result["revision"] == state.revision
    assert result["selected_id"] == state.selected_id
