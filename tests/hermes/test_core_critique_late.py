from pathlib import Path

import pytest
from logopia_studio.engine import Studio
from logopia_studio.models import ReviewInput, Workflow
from tests.hermes.test_core_fixtures import REPO, brief
from tests.hermes.test_core_resume_fixtures import ResumeHost, original_hashes


@pytest.mark.parametrize("cancel_after_choice", [False, True])
@pytest.mark.parametrize("late_error", [False, True])
def test_superseded_critic_cannot_overwrite_fresh_review_or_choice(
    tmp_path: Path, late_error: bool, cancel_after_choice: bool
) -> None:
    # Given a critique whose return crosses a completed explicit recovery and user choice.
    accepted: list[Workflow] = []
    snapshots: list[Workflow] = []
    recovery_host = ResumeHost(tmp_path, prefix="replacement")
    recovery = Studio(tmp_path, REPO, recovery_host)

    def settle_and_recover(request: ReviewInput) -> None:
        if request.image_path.stem != "c3":
            return
        active = recovery.status("resume")
        interrupted = recovery.interrupt(
            "resume", active.revision, "Fixture original runner settled"
        )
        snapshots.append(interrupted)
        resumed = recovery.produce("resume", interrupted.revision)
        assert resumed.phase == "awaiting_choice"
        chosen = recovery.choose("resume", resumed.revision, "c1")
        accepted.append(
            recovery.interrupt("resume", chosen.revision, "Fixture cancelled after choosing")
            if cancel_after_choice
            else chosen
        )

    host = ResumeHost(tmp_path, unknown_at=3 if late_error else None, on_review=settle_and_recover)
    original = Studio(tmp_path, REPO, host)
    created = original.create("resume", brief(3))
    # When that superseded call returns or raises late, then the new state is unchanged.
    result = original.produce("resume", created.revision)
    assert len(accepted) == 1
    assert result == accepted[0]
    assert recovery.status("resume") == accepted[0]
    assert result.selected_id == "c1"
    assert result.phase == ("cancelled" if cancel_after_choice else "ready")
    assert result.jobs[-2] == snapshots[0].jobs[-1]
    assert original_hashes(tmp_path, result) == original_hashes(tmp_path, snapshots[0])
    assert len(recovery_host.reviews) == 1
    assert not recovery_host.plans
    assert not recovery_host.calls
    reconciled = recovery.reconcile("resume", result.revision, snapshots[0].jobs[-1].id)
    assert reconciled == result


def test_late_edited_child_critic_cannot_resume_old_edit_sequence(tmp_path: Path) -> None:
    # Given an edited child whose old critic outlives an explicit recovery and parent choice.
    host = ResumeHost(tmp_path)
    original = Studio(tmp_path, REPO, host)
    created = original.create("resume", brief())
    produced = original.produce("resume", created.revision)
    accepted: list[Workflow] = []
    recovery_host = ResumeHost(tmp_path, prefix="child-replacement")
    recovery = Studio(tmp_path, REPO, recovery_host)

    def settle_and_recover(_request: ReviewInput) -> None:
        active = recovery.status("resume")
        interrupted = recovery.interrupt("resume", active.revision, "Fixture edit critic settled")
        resumed = recovery.produce("resume", interrupted.revision)
        assert resumed.phase == "awaiting_choice"
        accepted.append(recovery.choose("resume", resumed.revision, "c1"))

    editor = Studio(
        tmp_path, REPO, ResumeHost(tmp_path, prefix="old-child", on_review=settle_and_recover)
    )
    # When the superseded child report returns, then ready parent selection stays unchanged.
    result = editor.revise("resume", produced.revision, "c1", ("Ring",), "Spacing")
    assert result == accepted[0]
    assert result.phase == "ready"
    assert result.selected_id == "c1"
    assert len(recovery_host.reviews) == 1
    assert not recovery_host.calls
    assert not recovery_host.plans
