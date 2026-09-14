from dataclasses import replace
from pathlib import Path

import pytest
from logopia_studio.engine import Studio
from logopia_studio.engine_steps import Steps
from logopia_studio.models import Job, Phase, StudioError, Workflow
from tests.hermes.test_core_fixtures import REPO, FixtureHost, brief


def test_two_failed_edit_calls_exhaust_budget(tmp_path: Path) -> None:
    # Given one reviewed parent and a new host whose edit output is absent.
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    produced = studio.produce("core", created.revision)
    failing = FixtureHost(tmp_path / "absent", mode="missing")
    studio.steps = replace(studio.steps, host=failing)
    # When two failed edits are requested, then a third dispatch is rejected after reload.
    first = studio.revise("core", produced.revision, produced.candidates[0].id, (), "Open spacing")
    second = studio.revise("core", first.revision, produced.candidates[0].id, (), "Open more")
    reloaded = Studio(tmp_path, REPO, failing)
    with pytest.raises(StudioError, match="edit_limit"):
        _ = reloaded.revise("core", second.revision, produced.candidates[0].id, (), "Third")
    assert len(failing.calls) == 2
    assert sum(job.kind == "edit" for job in second.jobs) == 2


def test_late_native_return_after_interrupt_stops_sequence(tmp_path: Path) -> None:
    # Given interruption from within the reserved native call.
    studio = Studio(tmp_path, REPO, FixtureHost(tmp_path))
    created = studio.create("core", brief(2))

    def interrupt() -> None:
        active = studio.status("core")
        assert active.jobs[-1].status == "reserved"
        _ = studio.interrupt("core", active.revision, "Fixture owned runner settled")

    host = FixtureHost(tmp_path, on_generate=interrupt)
    studio.steps = replace(studio.steps, host=host)
    # When native returns late, then evidence survives without further calls.
    state = studio.produce("core", created.revision)
    assert state.phase == "outcome_unknown"
    assert len(host.calls) == 1
    assert host.reviews == []
    assert state.candidates == ()
    assert state.jobs[-1].generated is not None
    recovered = studio.reconcile("core", state.revision, state.jobs[-1].id)
    assert len(recovered.candidates) == 1
    assert len(host.calls) == 1


def test_cancelled_draft_has_no_inference(tmp_path: Path) -> None:
    # Given a newly created draft that is explicitly interrupted.
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    cancelled = studio.interrupt("core", created.revision, "Cancelled before planning")
    # When produce is repeated, then cancellation is visible and no inference occurs.
    repeated = studio.produce("core", cancelled.revision)
    assert repeated == cancelled
    assert repeated.phase == "cancelled"
    assert host.plans == []
    assert host.calls == []


def test_create_is_exactly_idempotent_and_dirty_sentinel_survives(tmp_path: Path) -> None:
    # Given unrelated dirty work and an existing identical brief.
    sentinel = tmp_path / "uncommitted-design.md"
    _ = sentinel.write_bytes(b"do not modify")
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    first = studio.create("core", brief())
    # When create is repeated or conflicts, then neither native calls nor unrelated edits occur.
    assert studio.create("core", brief()) == first
    with pytest.raises(StudioError, match="conflict"):
        _ = studio.create("core", brief(2))
    assert sentinel.read_bytes() == b"do not modify"
    assert host.plans == []


def test_failed_reservation_does_not_leave_phantom_feedback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given a concurrent reservation rejection before an edit can dispatch.

    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    produced = studio.produce("core", created.revision)

    def reject(_steps: Steps, _state: Workflow, _job: Job, _phase: Phase) -> Workflow:
        raise StudioError("stale_revision", "Fixture reservation rejected")

    monkeypatch.setattr(Steps, "reserve", reject)
    # When reservation fails, then feedback and revision remain untouched.
    with pytest.raises(StudioError, match="stale_revision"):
        _ = studio.revise("core", produced.revision, produced.candidates[0].id, (), "Spacing")
    after = studio.status("core")
    assert after == produced
    assert len(host.calls) == 1


def test_saved_attempt_identity_cannot_be_rewritten(tmp_path: Path) -> None:
    # Given a completed native attempt with an immutable request digest.
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    produced = studio.produce("core", created.revision)
    rewritten = produced.jobs[0].model_copy(update={"request_sha256": "f" * 64})
    changed = produced.model_copy(update={"jobs": (rewritten, *produced.jobs[1:])})
    # When bookkeeping tries to change its request identity, then the commit must fail.
    with pytest.raises(StudioError, match="immutable_history"):
        _ = studio.steps.commit(changed)
    assert studio.status("core") == produced


def test_unknown_second_edit_preserves_budget_across_restart(tmp_path: Path) -> None:
    # Given one failed edit, followed by an unknown native outcome on the second edit.
    studio = Studio(tmp_path, REPO, FixtureHost(tmp_path))
    created = studio.create("core", brief())
    produced = studio.produce("core", created.revision)
    missing = FixtureHost(tmp_path / "absent", mode="missing")
    studio.steps = replace(studio.steps, host=missing)
    failed = studio.revise("core", produced.revision, produced.candidates[0].id, (), "Spacing")
    unknown = FixtureHost(tmp_path, mode="unknown")
    studio.steps = replace(studio.steps, host=unknown)
    second = studio.revise("core", failed.revision, produced.candidates[0].id, (), "Open detail")
    resumed = Studio(tmp_path, REPO, unknown)
    # When restarted, interrupted and reconciled, then neither edit attempt is reset or retried.
    state = second
    for _ in range(3):
        state = resumed.interrupt("core", state.revision, "Owned runner settled")
        state = resumed.reconcile("core", state.revision, state.jobs[-1].id)
    with pytest.raises(StudioError, match="busy"):
        _ = resumed.revise("core", state.revision, produced.candidates[0].id, (), "Third edit")
    assert state.phase == "outcome_unknown"
    assert sum(job.kind == "edit" for job in state.jobs) == 2
    assert len(missing.calls) == 1
    assert len(unknown.calls) == 1
