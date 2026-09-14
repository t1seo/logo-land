from pathlib import Path

import pytest
from logopia_studio.engine import Studio
from logopia_studio.models import StudioError
from tests.hermes.test_core_fixtures import REPO, FixtureHost, brief


def test_unknown_result_never_retries(tmp_path: Path) -> None:
    # Given a native image timeout after durable reservation.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    host = FixtureHost(tmp_path, mode="unknown")
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    state = studio.produce("core", created.revision)
    # When repeatedly interrupted, reconciled and continued without return evidence.
    for _ in range(3):
        state = studio.interrupt("core", state.revision, "Owned runner settled")
        state = studio.reconcile("core", state.revision, state.jobs[-1].id)
        state = studio.produce("core", state.revision)
    # Then the unknown call remains one consumed attempt and never regenerates.
    assert state.phase == "outcome_unknown"
    assert len(host.calls) == 1
    assert sum(job.kind == "generate" for job in state.jobs) == 1


def test_report_failure_can_resume_critique_only(tmp_path: Path) -> None:
    # Given a malformed report after the original was imported.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    host = FixtureHost(tmp_path, mode="bad_report")
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    state = studio.produce("core", created.revision)
    assert state.phase == "failed"
    assert state.candidates[0].critiques == ()
    # When explicitly continued, then only a fresh critique pair is called.
    resumed = studio.produce("core", state.revision)
    assert resumed.phase == "awaiting_choice"
    assert len(host.calls) == 1
    assert len(host.reviews) == 2
    assert any(job.raw_reports == ('{"oops":1}',) for job in resumed.jobs)


def test_stale_revision_and_changed_original_fail(tmp_path: Path) -> None:
    # Given a produced original and the initial stale revision.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    state = studio.produce("core", created.revision)
    # When a stale choice or changed original is encountered, then no new native call occurs.
    with pytest.raises(StudioError, match="stale_revision"):
        _ = studio.choose("core", created.revision, state.candidates[0].id)
    _ = (tmp_path / state.candidates[0].image_path).write_bytes(b"changed")
    with pytest.raises(StudioError):
        _ = studio.status("core")
    assert len(host.calls) == 1


def test_missing_image_is_failure_not_success(tmp_path: Path) -> None:
    # Given a misleading native success receipt that names an absent PNG.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    host = FixtureHost(tmp_path, mode="missing")
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    # When production runs, then it records failure without an invented artifact.
    state = studio.produce("core", created.revision)
    assert state.phase in {"failed", "outcome_unknown"}
    assert state.candidates == ()
    assert len(host.calls) == 1
