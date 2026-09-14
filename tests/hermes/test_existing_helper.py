from __future__ import annotations

from typing import TYPE_CHECKING, Final

from pydantic import JsonValue, TypeAdapter

if TYPE_CHECKING:
    from tests.conftest import Harness

JSON: Final[TypeAdapter[JsonValue]] = TypeAdapter(JsonValue)


def test_workflow_sidecar_does_not_change_existing_session(harness: Harness) -> None:
    harness.init()
    before = harness.state_path.read_bytes()
    sidecar = harness.workspace / ".logo-generator/workflows/future/workflow.json"
    sidecar.parent.mkdir(parents=True)
    _ = sidecar.write_text('{"schema_version":999}', encoding="utf-8")

    shown = JSON.validate_json(harness.ok("show", "--session", "demo"))

    assert isinstance(shown, dict)
    assert shown["revision"] == 0
    brief = shown["brief"]
    assert isinstance(brief, dict)
    assert brief["exact_text"] == "Morrow Studio"
    assert harness.state_path.read_bytes() == before
    assert JSON.validate_json(harness.ok("list")) == [
        {"id": "demo", "revision": 0, "selected_id": None}
    ]


def test_existing_import_does_not_select_or_approve(harness: Harness) -> None:
    harness.init()
    imported = JSON.validate_json(harness.import_image())

    assert isinstance(imported, dict)
    assert imported["revision"] == 1
    assert imported["selected_id"] is None
    artifacts = imported["artifacts"]
    assert isinstance(artifacts, list)
    artifact = artifacts[0]
    assert isinstance(artifact, dict)
    assert artifact["id"] == "v1"
    assert artifact["review"] is None
    assert (
        harness.png.read_bytes()
        == (harness.workspace / ".logo-generator/sessions/demo/artifacts/v1.png").read_bytes()
    )
