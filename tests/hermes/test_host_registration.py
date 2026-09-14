from __future__ import annotations

import hashlib
import json
from typing import TYPE_CHECKING

import pytest
from logopia_studio import registration
from logopia_studio.engine import Studio
from logopia_studio.host_api import JsonObject
from logopia_studio.models import Candidate, FeedbackEnvelope, Workflow
from pydantic import TypeAdapter
from tests.hermes.test_host_fakes import FakeContext, brief, direction, strategy, write_png

if TYPE_CHECKING:
    from pathlib import Path


def test_registers_two_tools_and_director_without_reading_settings(tmp_path: Path) -> None:
    ctx = FakeContext()
    registration.register(ctx, tmp_path)
    assert list(ctx.handlers) == ["logopia_start", "logopia_action"]
    assert ctx.toolsets == ["logopia-studio", "logopia-studio"]
    assert ctx.skills == [("director", tmp_path / "skills" / "director" / "SKILL.md")]
    assert not ctx.dispatches
    assert not ctx.llm.calls
    assert not tuple(tmp_path.iterdir())
    result = TypeAdapter(JsonObject).validate_json(
        ctx.handlers["logopia_action"](
            {
                "action": "status",
                "workflow_id": "sample",
            },
            task_id="public-hermes-task",
        )
    )
    assert result["success"] is False
    assert result["error"] == "not_configured"


def configured_root(tmp_path: Path) -> Path:
    plugin_root = tmp_path / "plugin"
    plugin_root.mkdir()
    _ = (plugin_root / "settings.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "workspace": str(tmp_path),
                "helper_repo": str(tmp_path),
            }
        ),
        encoding="utf-8",
    )
    return plugin_root


def stored_state(tmp_path: Path) -> Workflow:
    path = tmp_path / ".logo-generator" / "sessions" / "sample" / "artifacts" / "one.png"
    path.parent.mkdir(parents=True)
    raw = write_png(path)
    return Workflow(
        id="sample",
        revision=4,
        brief=brief(),
        phase="awaiting_choice",
        strategy=strategy(),
        directions=(direction(0), direction(1)),
        candidates=(
            Candidate(
                id="one",
                direction_id="direction-0",
                parent_id=None,
                image_path=str(path.relative_to(tmp_path)),
                sha256=hashlib.sha256(raw).hexdigest(),
                width=320,
                height=160,
                prompt="One original",
                provider="test-provider",
                model="test-model",
            ),
        ),
    )


def test_status_has_no_publish_or_filesystem_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    plugin_root = configured_root(tmp_path)
    ctx = FakeContext()
    state = Workflow(id="sample", brief=brief())
    calls: list[str] = []

    def status(studio: Studio, workflow_id: str) -> Workflow:
        del studio
        assert workflow_id == state.id
        calls.append("status")
        return state

    def no_publish(workspace: Path, state: Workflow, output: Path) -> Path:
        del workspace, state, output
        pytest.fail("Status must not publish")

    monkeypatch.setattr(Studio, "status", status)
    monkeypatch.setattr(registration, "publish_gallery", no_publish)
    registration.register(ctx, plugin_root)
    before = {str(path): path.read_bytes() for path in tmp_path.rglob("*") if path.is_file()}
    result = TypeAdapter(JsonObject).validate_json(
        ctx.handlers["logopia_action"](
            {
                "workflow_id": "sample",
                "action": "status",
            }
        )
    )
    after = {str(path): path.read_bytes() for path in tmp_path.rglob("*") if path.is_file()}
    assert result["success"] is True
    assert result["gallery"] is None
    assert result["revision"] == 0
    assert before == after
    assert calls == ["status"]
    assert not ctx.llm.calls


@pytest.mark.parametrize("stale", ["revision", "hash"])
def test_stale_feedback_calls_no_mutation_or_image(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    stale: str,
) -> None:
    plugin_root = configured_root(tmp_path)
    state = stored_state(tmp_path)
    ctx = FakeContext()

    def status(studio: Studio, workflow_id: str) -> Workflow:
        del studio, workflow_id
        return state

    def no_choose(
        studio: Studio, workflow_id: str, expected_revision: int, candidate_id: str
    ) -> Workflow:
        del studio, workflow_id, expected_revision, candidate_id
        pytest.fail("Stale feedback cannot choose")

    monkeypatch.setattr(Studio, "status", status)
    monkeypatch.setattr(Studio, "choose", no_choose)
    registration.register(ctx, plugin_root)
    request = FeedbackEnvelope(
        workflow_id=state.id,
        expected_revision=3 if stale == "revision" else state.revision,
        candidate_id="one",
        candidate_sha256="a" * 64 if stale == "hash" else state.candidates[0].sha256,
        action="choose",
    )
    raw = ctx.handlers["logopia_action"](
        TypeAdapter(JsonObject).validate_json(request.model_dump_json())
    )
    result = TypeAdapter(JsonObject).validate_json(raw)
    assert result["success"] is False
    assert result["error"] == ("stale_revision" if stale == "revision" else "stale_candidate")
    assert not ctx.dispatches
    assert not ctx.llm.calls
