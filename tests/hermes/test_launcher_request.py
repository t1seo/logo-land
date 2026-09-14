from __future__ import annotations

from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.host_requests import ContinueRequest, StartRequest
from logopia_studio.launcher_output import CommandResult
from logopia_studio.models import Job, Workflow
from tests.hermes.test_core_fixtures import brief

if TYPE_CHECKING:
    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


def test_json_error_is_machine_readable(cli_fixture: CliFixture) -> None:
    result = cli_fixture.run(cli_fixture.request("{"), "--json")
    receipt = CommandResult.model_validate_json(result.stderr)
    assert result.returncode != 0
    assert not receipt.success
    assert receipt.error == "invalid_request"


@pytest.mark.parametrize(
    "raw",
    ["{", "[]", '"do whatever is necessary"', "{}", "x" * 32769],
    ids=["broken", "array", "instruction", "empty", "oversize"],
)
def test_malformed_request_is_rejected_before_dispatch(
    cli_fixture: CliFixture,
    raw: str,
) -> None:
    # Given an invalid or oversized request file.
    path = cli_fixture.request(raw)
    # When the CLI receives the file.
    result = cli_fixture.run(path)
    # Then the request is rejected without starting Hermes.
    assert result.returncode != 0
    assert "invalid_request" in result.stderr
    assert not (cli_fixture.profile.parent.parent / "invocations.jsonl").exists()


def test_missing_settings_fail_before_inference(cli_fixture: CliFixture) -> None:
    request = StartRequest(workflow_id="new", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "not_configured" in result.stderr
    assert not (cli_fixture.profile.parent.parent / "invocations.jsonl").exists()


def test_stale_revision_fails_before_inference(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    cli_fixture.save(Workflow(id="saved", brief=brief(), revision=5))
    request = ContinueRequest(workflow_id="saved", action="continue", expected_revision=4)
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "stale_revision" in result.stderr
    assert not (cli_fixture.profile.parent.parent / "invocations.jsonl").exists()


@pytest.mark.parametrize("phase", ["outcome_unknown", "cancelled"])
def test_paused_workflow_is_not_resubmitted(cli_fixture: CliFixture, phase: str) -> None:
    cli_fixture.configure()
    state = Workflow.model_validate_json(
        Workflow(id="saved", brief=brief()).model_dump_json().replace('"draft"', f'"{phase}"'),
    )
    cli_fixture.save(state)
    request = ContinueRequest(workflow_id="saved", action="continue", expected_revision=0)
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert phase in result.stderr
    assert not (cli_fixture.profile.parent.parent / "invocations.jsonl").exists()


def test_unknown_job_blocks_resubmit_even_with_draft_phase(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    job = Job(id="j1", kind="plan", status="unknown", request_sha256="a" * 64)
    cli_fixture.save(Workflow(id="saved", brief=brief(), jobs=(job,)))
    request = ContinueRequest(workflow_id="saved", action="continue", expected_revision=0)
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "outcome_unknown" in result.stderr
    assert not (cli_fixture.profile.parent.parent / "invocations.jsonl").exists()
