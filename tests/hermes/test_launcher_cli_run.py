from __future__ import annotations

from typing import TYPE_CHECKING, Final

from logopia_studio.host_requests import ContinueRequest, StartRequest, StatusRequest
from logopia_studio.launcher_output import CommandResult
from logopia_studio.launcher_profile import profile_lock
from logopia_studio.models import Workflow
from logopia_studio.store import Store
from tests.hermes.test_core_fixtures import brief

if TYPE_CHECKING:
    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


def test_run_reports_only_verified_fixture_state(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    cli_fixture.mode("tool")
    request = StartRequest(workflow_id="produced", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()), "--json")
    assert result.returncode == 0, result.stderr
    receipt = CommandResult.model_validate_json(result.stdout)
    assert receipt.success
    assert receipt.workflow_id == "produced"
    assert receipt.phase == "awaiting_choice"
    assert receipt.candidate_count == 1
    assert receipt.gallery is not None
    assert cli_fixture.invocation_count() == 1


def test_profile_lock_rejects_another_actual_cli(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    request = StartRequest(workflow_id="locked", brief=brief())
    with profile_lock(cli_fixture.profile):
        result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "profile_busy" in result.stderr
    assert cli_fixture.invocation_count() == 0


def test_deadline_marks_reserved_call_unknown_after_child_settles(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    cli_fixture.mode("timeout")
    cli_fixture.save(Workflow(id="paused", brief=brief()))
    request = StartRequest(workflow_id="paused", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()), "--timeout", "1")
    assert result.returncode != 0
    assert "run_timed_out" in result.stderr
    state = Store(cli_fixture.workspace).load("paused")
    assert state.phase == "outcome_unknown"
    assert state.jobs[0].status == "unknown"
    assert (cli_fixture.profile.parent.parent / "settled.txt").exists()
    assert cli_fixture.invocation_count() == 1


def test_run_status_has_no_hidden_hermes_call(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    cli_fixture.save(Workflow(id="saved", brief=brief(), phase="cancelled"))
    request = StatusRequest(workflow_id="saved", action="status")
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode == 0, result.stderr
    assert "cancelled" in result.stdout
    assert cli_fixture.invocation_count() == 0


def test_run_rejects_workspace_override(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    request = StartRequest(workflow_id="saved", brief=brief())
    result = cli_fixture.run(
        cli_fixture.request(request.model_dump_json()), "--workspace", str(cli_fixture.root)
    )
    assert result.returncode != 0
    assert "workspace_mismatch" in result.stderr
    assert cli_fixture.invocation_count() == 0


def test_gallery_preserves_foreign_output(cli_fixture: CliFixture) -> None:
    cli_fixture.save(Workflow(id="saved", brief=brief()))
    foreign = cli_fixture.root / "foreign"
    foreign.mkdir()
    sentinel = foreign / "index.html"
    _ = sentinel.write_text("keep", encoding="utf-8")
    result = cli_fixture.invoke(
        "gallery",
        "--workflow",
        "saved",
        "--workspace",
        str(cli_fixture.workspace),
        "--output",
        str(foreign),
    )
    assert result.returncode != 0
    assert sentinel.read_text(encoding="utf-8") == "keep"
    assert cli_fixture.invocation_count() == 0


def test_missing_action_workflow_never_dispatches(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    request = ContinueRequest(workflow_id="missing", action="continue", expected_revision=0)
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "workflow_missing" in result.stderr
    assert cli_fixture.invocation_count() == 0
