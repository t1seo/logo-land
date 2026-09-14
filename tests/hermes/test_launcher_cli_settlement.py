from __future__ import annotations

from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.host_requests import StartRequest
from logopia_studio.launcher_output import CommandResult
from logopia_studio.launcher_process import ProcessReceipt
from logopia_studio.launcher_runner import RunOptions, run_request
from logopia_studio.models import Job, Workflow
from logopia_studio.store import Store
from tests.hermes.test_core_fixtures import brief

if TYPE_CHECKING:
    from pathlib import Path

    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


@pytest.mark.parametrize(
    ("exit_code", "timed_out", "interrupted", "cause", "absent"),
    [
        (0, False, False, "exited with unfinished operation", "deadline"),
        (1, False, False, "exited with unfinished operation", "interruption"),
        (-2, True, False, "settled after its deadline", "interruption"),
        (-2, False, True, "settled after an interruption", "deadline"),
    ],
)
def test_settlement_reports_only_observed_cause(
    cli_fixture: CliFixture,
    exit_code: int,
    timed_out: bool,
    interrupted: bool,
    cause: str,
    absent: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    cli_fixture.configure()
    cli_fixture.save(Workflow(id="partial", brief=brief()))

    def run(
        command: tuple[str, ...], workspace: Path, output: Path, timeout_seconds: int
    ) -> ProcessReceipt:
        assert command[:3] == ("hermes", "-p", "logopia")
        assert workspace == cli_fixture.workspace
        assert timeout_seconds == 1800
        job = Job(id="pending", kind="plan", request_sha256="a" * 64)
        cli_fixture.save(
            Workflow(id="partial", brief=brief(), jobs=(job,), phase="planning", revision=1)
        )
        return ProcessReceipt(
            exit_code, timed_out, interrupted, output / "stdout.txt", output / "stderr.txt"
        )

    monkeypatch.setenv("HERMES_HOME", str(cli_fixture.profile.parent.parent))
    monkeypatch.setattr("logopia_studio.launcher_runner.run_process", run)
    request = StartRequest(workflow_id="partial", brief=brief())
    result = run_request(
        RunOptions(
            profile="logopia",
            profile_home=cli_fixture.profile,
            request=cli_fixture.request(request.model_dump_json()),
        )
    )
    assert not result.success
    state = Store(cli_fixture.workspace).load("partial")
    assert state.phase == "outcome_unknown"
    assert state.jobs[0].status == "unknown"
    assert state.last_error is not None
    assert cause in state.last_error
    assert absent not in state.last_error
    assert "provider cancellation is not confirmed" in state.last_error
    assert state.jobs[0].error == state.last_error


def test_successful_prose_with_partial_state_never_invents_deadline(
    cli_fixture: CliFixture,
) -> None:
    cli_fixture.configure()
    cli_fixture.mode("partial-exit")
    cli_fixture.save(Workflow(id="partial", brief=brief()))
    request = StartRequest(workflow_id="partial", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()), "--json")
    assert result.returncode != 0
    receipt = CommandResult.model_validate_json(result.stderr)
    assert receipt.error == "outcome_unknown"
    assert "exited with unfinished operation" in receipt.message
    assert "deadline" not in receipt.message
    assert "interruption" not in receipt.message
    state = Store(cli_fixture.workspace).load("partial")
    assert state.last_error == receipt.message
    assert cli_fixture.invocation_count() == 1
    assert not (cli_fixture.profile.parent.parent / "fixture-image-calls.txt").exists()
