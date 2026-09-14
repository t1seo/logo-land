from pathlib import Path

from logopia_studio.engine import Studio
from logopia_studio.models import Critique, PlanResult, ReviewInput, StudioBrief, StudioError
from tests.hermes.test_core_fixtures import REPO, FixtureHost, brief
from typing_extensions import override


class FailedPlanner(FixtureHost):
    @override
    def plan(self, brief: StudioBrief) -> PlanResult:
        self.plans.append(brief)
        raise StudioError("invalid_report", "Fixture malformed plan", ('{"malformed":true}',))


class WrongCountPlanner(FixtureHost):
    @override
    def plan(self, brief: StudioBrief) -> PlanResult:
        return super().plan(brief.model_copy(update={"count": 2}))


class WrongEvidenceHost(FixtureHost):
    @override
    def critique(self, request: ReviewInput) -> tuple[Critique, ...]:
        reports = super().critique(request)
        return tuple(report.model_copy(update={"image_sha256": "f" * 64}) for report in reports)


class ReusedCallsHost(FixtureHost):
    @override
    def critique(self, request: ReviewInput) -> tuple[Critique, ...]:
        reports = super().critique(request)
        return tuple(
            report.model_copy(update={"call_id": f"{report.role}-1"}) for report in reports
        )


def test_failed_plan_is_never_retried(tmp_path: Path) -> None:
    # Given a malformed planning result.
    host = FailedPlanner(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    first = studio.produce("core", created.revision)
    # When continued explicitly, then the one planning budget remains spent.
    second = studio.produce("core", first.revision)
    assert second == first
    assert len(host.plans) == 1
    assert first.jobs[0].raw_reports == ('{"malformed":true}',)
    assert host.calls == []


def test_wrong_direction_count_stops_before_image(tmp_path: Path) -> None:
    # Given two planned directions for an agreed one-count brief.
    host = WrongCountPlanner(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    # When plan output is accepted, then exact count mismatch stops image calls.
    result = studio.produce("core", created.revision)
    assert result.phase == "failed"
    assert result.directions == ()
    assert host.calls == []
    assert result.jobs[0].plan is not None


def test_mismatched_report_evidence_is_bounded_and_never_approved(tmp_path: Path) -> None:
    # Given reports attributed to another original.
    host = WrongEvidenceHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    result = studio.produce("core", created.revision)
    # When repeated explicit continues exhaust the two critique attempts.
    for _ in range(3):
        result = studio.produce("core", result.revision)
    # Then reports remain in history but never become candidate approval.
    assert result.candidates[0].critiques == ()
    assert len(host.reviews) == 2
    assert len(host.calls) == 1
    assert len(tuple(job for job in result.jobs if job.raw_reports)) == 2


def test_edit_cannot_reuse_prior_call_identity(tmp_path: Path) -> None:
    # Given a host binding child pixels correctly but reusing the parent's call identities.
    host = ReusedCallsHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    initial = studio.produce("core", created.revision)
    # When the child is critiqued, then reused call identities are rejected as non-fresh evidence.
    result = studio.revise("core", initial.revision, initial.candidates[0].id, (), "Open spacing")
    assert result.phase == "failed"
    assert result.candidates[1].critiques == ()
    assert len(host.reviews) == 2
