from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import ValidationError

from logo_helper import storage, workflow
from logo_helper.legacy_state import parse_session
from logo_helper.models import ArtifactId, ProjectError, Session, SessionId
from logo_helper.storage import Store
from tests.test_color_models import palette

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


def legacy_fixture(harness: Harness) -> bytes:
    harness.init()
    _ = harness.import_image()
    return write_legacy(harness)


def write_legacy(harness: Harness) -> bytes:
    state = Session.model_validate_json(harness.state_path.read_bytes())
    raw = state.model_dump_json(
        indent=2,
        exclude={
            "palettes": True,
            "active_palette_id": True,
            "references": True,
            "color_reports": True,
            "brief": {"lockup"},
            "artifacts": {"__all__": {"palette_id", "lockup", "requested_background"}},
        },
    ).replace('"schema_version": 2', '"schema_version": 1')
    data = raw.encode()
    _ = harness.state_path.write_bytes(data)
    return data


def test_legacy_reads_do_not_write_and_first_select_migrates(harness: Harness) -> None:
    before = legacy_fixture(harness)
    for args in [("show", "--session", "demo"), ("list",), ("prompt", "--session", "demo")]:
        _ = harness.ok(*args)
        assert harness.state_path.read_bytes() == before
    backup = harness.state_path.with_name("session.v1.backup.json")
    assert not backup.exists()
    result = Session.model_validate_json(
        harness.ok("select", "--session", "demo", "--artifact", "v1", "--revision", "1")
    )
    assert result.schema_version == 2
    assert result.revision == 2
    assert result.selected_id == "v1"
    assert result.brief.palette == ("green",)
    assert result.palettes == result.color_reports == ()
    assert result.artifacts[0].palette_id is None
    assert result.artifacts[0].lockup is None
    assert result.artifacts[0].requested_background is None
    assert backup.read_bytes() == before
    _ = harness.ok(
        "review",
        "--session",
        "demo",
        "--artifact",
        "v1",
        "--revision",
        "2",
        "--review-file",
        str(harness.review),
    )
    assert backup.read_bytes() == before
    assert Store.at(harness.workspace).load(SessionId("demo")).revision == 3


def fail_atomic(_path: Path, _state: Session) -> None:
    raise OSError(28, "simulated full disk")


def test_failed_migration_reuses_verified_backup(
    harness: Harness, monkeypatch: pytest.MonkeyPatch
) -> None:
    before = legacy_fixture(harness)
    store = Store.at(harness.workspace)
    with monkeypatch.context() as patch:
        patch.setattr(storage, "atomic_state", fail_atomic)
        with pytest.raises(OSError, match="full disk"):
            _ = workflow.select(store, SessionId("demo"), 1, ArtifactId("v1"))
    assert harness.state_path.read_bytes() == before
    backup = harness.state_path.with_name("session.v1.backup.json")
    assert backup.read_bytes() == before
    _ = workflow.select(store, SessionId("demo"), 1, ArtifactId("v1"))
    assert backup.read_bytes() == before
    assert store.load(SessionId("demo")).schema_version == 2


def test_mismatched_backup_is_never_overwritten(harness: Harness) -> None:
    before = legacy_fixture(harness)
    backup = harness.state_path.with_name("session.v1.backup.json")
    _ = backup.write_bytes(b"unrelated data")
    result = harness.run("select", "--session", "demo", "--artifact", "v1", "--revision", "1")
    assert result.returncode != 0
    assert "backup_conflict" in result.stderr
    assert backup.read_bytes() == b"unrelated data"
    assert harness.state_path.read_bytes() == before


def test_strict_legacy_and_future_version_rejection(harness: Harness) -> None:
    before = legacy_fixture(harness)
    for old, new in [
        (b'"schema_version": 1', b'"schema_version": 77'),
        (b'"brief": {', b'"brief": {"lockup": null,'),
    ]:
        with pytest.raises(ValidationError):
            _ = parse_session(before.replace(old, new))
    assert harness.state_path.read_bytes() == before


def test_immutable_palette_history_is_enforced_on_save(harness: Harness) -> None:
    harness.init()
    store = Store.at(harness.workspace)
    with store.locked(SessionId("demo")):
        initial = store.load(SessionId("demo"))
        saved = workflow.advance(initial.model_copy(update={"palettes": (palette(),)}))
        store.save(saved)
        before = harness.state_path.read_bytes()
        removed = workflow.advance(saved.model_copy(update={"palettes": ()}))
        with pytest.raises(ProjectError, match="immutable_history"):
            store.save(removed)
    assert harness.state_path.read_bytes() == before


@pytest.mark.parametrize("version", [b"true", b"1.0", b'"1"'])
def test_legacy_version_requires_a_json_integer(harness: Harness, version: bytes) -> None:
    before = legacy_fixture(harness)
    with pytest.raises(ValidationError):
        _ = parse_session(before.replace(b'"schema_version": 1', b'"schema_version": ' + version))


def test_new_init_writes_v2_and_review_can_be_first_migration(harness: Harness) -> None:
    before = legacy_fixture(harness)
    raw = harness.ok(
        "review",
        "--session",
        "demo",
        "--artifact",
        "v1",
        "--revision",
        "1",
        "--review-file",
        str(harness.review),
    )
    result = Session.model_validate_json(raw)
    assert result.schema_version == 2
    assert result.artifacts[0].review is not None
    assert result.artifacts[0].review.passed
    assert harness.state_path.with_name("session.v1.backup.json").read_bytes() == before


def test_legacy_migration_preserves_edited_lineage_selection_and_exports(harness: Harness) -> None:
    harness.prepare_export()
    _ = harness.ok("export", "--session", "demo", "--revision", "3")
    _ = harness.prompt.write_text("Edit this green logo to navy; fixture only.", encoding="utf-8")
    _ = harness.import_image(4, "v2", "--parent", "v1")
    before = write_legacy(harness)
    old = parse_session(before)
    resumed = Session.model_validate_json(harness.ok("show", "--session", "demo"))
    assert resumed.selected_id == "v1"
    assert resumed.artifacts[1].parent_id == "v1"
    assert resumed.artifacts[1].palette_id is None
    assert "navy" in resumed.artifacts[1].prompt
    assert resumed.brief.palette == ("green",)
    assert harness.state_path.read_bytes() == before
    updated = Session.model_validate_json(
        harness.ok("select", "--session", "demo", "--artifact", "v2", "--revision", "5")
    )
    assert updated.exports == old.exports
    assert updated.artifacts == old.artifacts
    assert updated.selected_id == "v2"
    assert harness.state_path.with_name("session.v1.backup.json").read_bytes() == before


def test_existing_artifact_cannot_gain_retroactive_palette_intent(harness: Harness) -> None:
    harness.init()
    _ = harness.import_image()
    store = Store.at(harness.workspace)
    with store.locked(SessionId("demo")):
        original = store.load(SessionId("demo"))
        rebound = original.artifacts[0].model_copy(update={"palette_id": "p1"})
        changed = workflow.advance(
            original.model_copy(update={"palettes": (palette(),), "artifacts": (rebound,)})
        )
        before = harness.state_path.read_bytes()
        with pytest.raises(ProjectError, match="immutable_history"):
            store.save(changed)
    assert harness.state_path.read_bytes() == before
