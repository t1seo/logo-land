from pathlib import Path

import pytest
from logopia_studio.engine import Studio
from logopia_studio.models import PlanResult, StudioBrief, StudioError, Workflow
from tests.hermes.test_core_fixtures import REPO, FixtureHost, brief
from tests.hermes.test_core_resume_fixtures import (
    ResumeHost,
    interrupted_reviews,
    original_hashes,
)
from typing_extensions import override


class UnknownPlanner(FixtureHost):
    @override
    def plan(self, brief: StudioBrief) -> PlanResult:
        self.plans.append(brief)
        raise StudioError("outcome_unknown", "Fixture unknown planning call")


def test_unknown_plan_never_resubmits(tmp_path: Path) -> None:
    # Given an interrupted planning reservation without return evidence.
    host = UnknownPlanner(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("resume", brief())
    state = studio.produce("resume", created.revision)
    # When explicit continuation and interruption repeat, then planning stays one attempt.
    for _ in range(3):
        state = studio.interrupt("resume", state.revision, "Fixture runner settled")
        state = studio.produce("resume", state.revision)
    assert state.phase == "outcome_unknown"
    assert len(host.plans) == 1
    assert not host.calls
    assert not host.reviews


def test_explicit_continue_recovers_only_missing_critique(tmp_path: Path) -> None:
    # Given three imported originals, two review pairs and a settled unknown third critique.
    studio, state, setup = interrupted_reviews(tmp_path)
    before = original_hashes(tmp_path, state)
    old_job = state.jobs[-1]
    host = ResumeHost(tmp_path, prefix="fresh")
    resumed = Studio(tmp_path, REPO, host)
    # When continuation explicitly uses the saved revision, then only one critique is dispatched.
    result = resumed.produce("resume", state.revision)
    assert result.phase == "awaiting_choice"
    assert len(host.reviews) == 1
    assert not host.plans
    assert not host.calls
    assert result.jobs[:-1] == state.jobs
    assert result.jobs[-1].kind == "critique"
    assert result.jobs[-1].status == "succeeded"
    assert result.jobs[-2] == old_job
    assert result.candidates[:2] == state.candidates[:2]
    assert {report.role for report in result.candidates[2].critiques} == {"design", "production"}
    assert original_hashes(tmp_path, result) == before
    assert Workflow.model_validate_json(result.model_dump_json()) == result
    assert studio.status("resume") == result
    assert len(setup.calls) == 3
    assert resumed.produce("resume", result.revision) == result
    chosen = resumed.choose("resume", result.revision, "c3")
    assert chosen.phase == "ready"
    assert len(host.reviews) == 1


def test_repeated_interruption_exhausts_remaining_review_attempt(tmp_path: Path) -> None:
    # Given one consumed unknown critique and one permitted remaining attempt.
    _, state, _ = interrupted_reviews(tmp_path, count=1)
    host = ResumeHost(tmp_path, prefix="second", unknown_at=1)
    resumed = Studio(tmp_path, REPO, host)
    # When the remaining attempt also has no result, then restart never resets that budget.
    second = resumed.produce("resume", state.revision)
    assert len(host.reviews) == 1
    assert second.jobs[: len(state.jobs)] == state.jobs
    assert sum(job.kind == "critique" for job in second.jobs) == 2
    for _ in range(3):
        reloaded = Studio(tmp_path, REPO, host)
        second = reloaded.interrupt("resume", second.revision, "Fixture second runner settled")
        second = reloaded.reconcile("resume", second.revision, state.jobs[-1].id)
        second = reloaded.produce("resume", second.revision)
    assert second.phase == "outcome_unknown"
    assert second.candidates[0].critiques == ()
    assert len(host.reviews) == 1
    assert not host.plans
    assert not host.calls
    with pytest.raises(StudioError, match="busy"):
        _ = resumed.choose("resume", second.revision, "c1")
