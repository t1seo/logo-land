from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest

from logo_helper import delivery, workflow
from logo_helper.models import ArtifactId, ProjectError, Session, SessionId
from logo_helper.storage import Store, write_new

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


def fail_save(_store: Store, _state: Session) -> None:
    raise OSError(28, "simulated full disk")


def fail_fsync(_fd: int) -> None:
    raise OSError(28, "simulated full disk")


def test_export_rolls_back_when_state_commit_fails(
    harness: Harness,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given an exportable session and a failure at the JSON commit boundary.
    harness.prepare_export()
    before = harness.state_path.read_bytes()
    monkeypatch.setattr(Store, "save", fail_save)
    # When committing the bundle fails.
    with pytest.raises(OSError, match="full disk"):
        _ = delivery.export(Store.at(harness.workspace), SessionId("demo"), 3, None)
    # Then previous state and absence of an advertised package are preserved.
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output/logo-generator/demo").exists()


def test_import_rolls_back_when_state_commit_fails(
    harness: Harness,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given a session with a write failure at the JSON commit boundary.
    harness.init()
    before = harness.state_path.read_bytes()
    monkeypatch.setattr(Store, "save", fail_save)
    # When importing a valid image cannot commit metadata.
    with pytest.raises(OSError, match="full disk"):
        _ = workflow.import_image(
            Store.at(harness.workspace),
            SessionId("demo"),
            0,
            artifact_id=ArtifactId("v1"),
            image=harness.png,
            prompt="Fixture",
            parent_id=None,
        )
    # Then the uncommitted artifact is removed and revision remains unchanged.
    assert harness.state_path.read_bytes() == before
    assert not (harness.state_path.parent / "artifacts/v1.png").exists()


def test_write_new_cleans_partial_file_when_fsync_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given a newly allocated file and a disk failure during flush.
    destination = tmp_path / "new.png"
    monkeypatch.setattr(os, "fsync", fail_fsync)
    # When a write cannot be made durable.
    with pytest.raises(OSError, match="full disk"):
        write_new(destination, b"bytes")
    # Then no incomplete immutable artifact blocks a later retry.
    assert not destination.exists()


def test_write_new_preserves_existing_file_when_name_collides(tmp_path: Path) -> None:
    # Given an existing user file.
    destination = tmp_path / "existing.png"
    _ = destination.write_bytes(b"original")
    # When exclusive creation collides.
    with pytest.raises(FileExistsError):
        write_new(destination, b"replacement")
    # Then the original bytes survive.
    assert destination.read_bytes() == b"original"


def test_cli_update_refuses_when_another_writer_holds_lock(harness: Harness) -> None:
    # Given a live cooperating writer holding the same session lock.
    harness.init()
    _ = harness.import_image()
    before = harness.state_path.read_bytes()
    with Store.at(harness.workspace).locked(SessionId("demo")):
        # When another real process tries to mutate the session.
        result = harness.run("select", "--session", "demo", "--artifact", "v1", "--revision", "1")
    # Then contention is explicit and state is unchanged.
    assert result.returncode != 0
    assert "locked" in result.stderr
    assert harness.state_path.read_bytes() == before


def test_lock_releases_when_operation_raises(harness: Harness) -> None:
    # Given a session lock that protects a failing operation.
    store = Store.at(harness.workspace)
    # When the operation raises its typed domain error.
    with pytest.raises(ProjectError, match="fixture"), store.locked(SessionId("demo")):
        raise ProjectError("fixture", "deliberate test error")
    # Then a later operation can acquire the lock again.
    with store.locked(SessionId("demo")):
        assert (harness.workspace / ".logo-generator/locks/demo.lock").is_dir()
