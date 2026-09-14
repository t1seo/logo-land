from __future__ import annotations

from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.engine import Studio
from logopia_studio.host_requests import (
    ContinueRequest,
    DeliverRequest,
    StartRequest,
    StatusRequest,
)
from logopia_studio.launcher_output import CommandResult
from logopia_studio.launcher_state import NoInferenceHost, preflight
from logopia_studio.models import FeedbackEnvelope, Job, Workflow
from logopia_studio.store import Store
from tests.hermes.test_core_fixtures import FixtureHost, brief
from tests.hermes.test_launcher_cli_fixtures import REPO

if TYPE_CHECKING:
    from logopia_studio.models_jobs import JobKind
    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


@pytest.fixture
def unknown_review(cli_fixture: CliFixture) -> Workflow:
    host = FixtureHost(cli_fixture.workspace, mode="bad_report")
    studio = Studio(cli_fixture.workspace, REPO, host)
    state = studio.create("review", brief())
    state = studio.produce(state.id, state.revision)
    assert state.jobs[-1].kind == "critique"
    error = "Native tool executor stopped after 420 seconds; critique outcome unknown"
    pending = state.jobs[-1].model_copy(update={"status": "unknown", "error": error})
    state = state.model_copy(
        update={
            "jobs": (*state.jobs[:-1], pending),
            "phase": "outcome_unknown",
            "last_error": error,
            "revision": state.revision + 1,
        }
    )
    cli_fixture.save(state)
    cli_fixture.configure()
    return state


def _continue(state: Workflow) -> ContinueRequest:
    return ContinueRequest(
        workflow_id=state.id, action="continue", expected_revision=state.revision
    )


def test_explicit_continue_allows_eligible_read_only_review(
    cli_fixture: CliFixture, unknown_review: Workflow
) -> None:
    studio = Studio(cli_fixture.workspace, REPO, NoInferenceHost())
    assert preflight(studio, _continue(unknown_review)) == unknown_review
    assert cli_fixture.invocation_count() == 0


def test_cli_review_resume_preserves_image_and_original_error(
    cli_fixture: CliFixture, unknown_review: Workflow
) -> None:
    cli_fixture.mode("tool")
    request = cli_fixture.request(_continue(unknown_review).model_dump_json())
    result = cli_fixture.run(request, "--json")
    assert result.returncode == 0, result.stderr
    receipt = CommandResult.model_validate_json(result.stdout)
    assert receipt.phase == "awaiting_choice"
    state = Store(cli_fixture.workspace).load(unknown_review.id)
    assert state.candidates[0].sha256 == unknown_review.candidates[0].sha256
    assert sum(job.kind == "generate" for job in state.jobs) == 1
    assert sum(job.kind == "plan" for job in state.jobs) == 1
    assert sum(job.kind == "critique" for job in state.jobs) == 2
    original = next(job for job in state.jobs if job.id == unknown_review.jobs[-1].id)
    assert original.error is not None
    assert "420 seconds" in original.error
    assert original.raw_reports == unknown_review.jobs[-1].raw_reports
    assert cli_fixture.invocation_count() == 1
    calls = cli_fixture.profile.parent.parent / "fixture-image-calls.txt"
    assert calls.read_text(encoding="utf-8") == ""
    retry = state.jobs[-1]
    assert retry.retry_of == original.id
    local = Studio(cli_fixture.workspace, REPO, NoInferenceHost())
    candidate = state.candidates[0]
    for action, change in (("choose", ""), ("revise", "Spacing")):
        feedback = FeedbackEnvelope.model_validate(
            {
                "schema_version": 1,
                "workflow_id": state.id,
                "expected_revision": state.revision,
                "candidate_id": candidate.id,
                "candidate_sha256": candidate.sha256,
                "action": action,
                "keep": (),
                "change": change,
            }
        )
        assert preflight(local, feedback) == state
    delivery = DeliverRequest(
        workflow_id=state.id, action="deliver", expected_revision=state.revision
    )
    assert preflight(local, delivery) == state
    assert cli_fixture.invocation_count() == 1


@pytest.mark.parametrize("kind", ["plan", "generate", "edit", "deliver"])
def test_other_unknown_operations_remain_no_call(cli_fixture: CliFixture, kind: JobKind) -> None:
    pending = Job(id="other", kind=kind, status="unknown", request_sha256="a" * 64)
    state = Workflow(id="other", brief=brief(), jobs=(pending,), phase="outcome_unknown")
    cli_fixture.configure()
    cli_fixture.save(state)
    result = cli_fixture.run(cli_fixture.request(_continue(state).model_dump_json()))
    assert result.returncode != 0
    assert "outcome_unknown" in result.stderr
    assert cli_fixture.invocation_count() == 0
    assert Store(cli_fixture.workspace).load(state.id) == state


def test_exhausted_review_budget_remains_no_call(
    cli_fixture: CliFixture, unknown_review: Workflow
) -> None:
    second = unknown_review.jobs[-1].model_copy(update={"id": "second-review"})
    state = unknown_review.model_copy(
        update={"jobs": (*unknown_review.jobs, second), "revision": unknown_review.revision + 1}
    )
    cli_fixture.save(state)
    result = cli_fixture.run(cli_fixture.request(_continue(state).model_dump_json()))
    assert result.returncode != 0
    assert "outcome_unknown" in result.stderr
    assert cli_fixture.invocation_count() == 0


def test_stale_review_continuation_remains_no_call(
    cli_fixture: CliFixture, unknown_review: Workflow
) -> None:
    request = _continue(unknown_review).model_copy(
        update={"expected_revision": unknown_review.revision - 1}
    )
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "stale_revision" in result.stderr
    assert cli_fixture.invocation_count() == 0


def test_review_recovery_requires_explicit_continue(
    cli_fixture: CliFixture, unknown_review: Workflow
) -> None:
    candidate = unknown_review.candidates[0]
    requests = (
        StartRequest(workflow_id=unknown_review.id, brief=unknown_review.brief),
        DeliverRequest(
            workflow_id=unknown_review.id,
            action="deliver",
            expected_revision=unknown_review.revision,
        ),
        FeedbackEnvelope(
            schema_version=1,
            workflow_id=unknown_review.id,
            expected_revision=unknown_review.revision,
            candidate_id=candidate.id,
            candidate_sha256=candidate.sha256,
            action="choose",
            keep=(),
            change="",
        ),
    )
    for request in requests:
        result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
        assert result.returncode != 0
        assert "outcome_unknown" in result.stderr
    status = StatusRequest(workflow_id=unknown_review.id, action="status")
    result = cli_fixture.run(cli_fixture.request(status.model_dump_json()))
    assert result.returncode == 0
    assert "outcome_unknown" in result.stdout
    assert cli_fixture.invocation_count() == 0
    assert Store(cli_fixture.workspace).load(unknown_review.id) == unknown_review
