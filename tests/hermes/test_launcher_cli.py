from __future__ import annotations

from typing import TYPE_CHECKING, Final

from logopia_studio.host_requests import StartRequest
from logopia_studio.models import Workflow
from tests.hermes.test_core_fixtures import brief

if TYPE_CHECKING:
    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


def test_help_lists_usable_commands_when_cli_is_invoked(cli_fixture: CliFixture) -> None:
    # Given an isolated environment with no installed plugin.
    # When the actual entry point is invoked.
    result = cli_fixture.invoke("--help")
    # Then every supported command is visible and no Hermes process ran.
    assert result.returncode == 0, result.stderr
    for command in ("install", "run", "show", "gallery"):
        assert command in result.stdout
    assert not (cli_fixture.profile.parent.parent / "invocations.jsonl").exists()


def test_invalid_profile_is_explicit_when_installing(cli_fixture: CliFixture) -> None:
    # Given a forbidden default profile.
    # When installation is requested through the entry point.
    result = cli_fixture.invoke("install", "--profile", "default")
    # Then no dispatch or filesystem installation occurs.
    assert result.returncode != 0
    assert "invalid_profile" in result.stderr
    assert not (cli_fixture.profile / "plugins").exists()


def test_missing_profile_is_not_created(cli_fixture: CliFixture) -> None:
    profile = cli_fixture.profile.with_name("missing")
    result = cli_fixture.invoke("install", "--profile", "missing", "--profile-home", str(profile))
    assert result.returncode != 0
    assert "missing_profile" in result.stderr
    assert not profile.exists()


def test_success_prose_does_not_create_workflow_proof(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    request = StartRequest(workflow_id="missing", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "workflow_missing" in result.stderr
    assert "produced" not in result.stdout.lower()


def test_unmodified_draft_is_not_reported_as_produced(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    cli_fixture.save(Workflow(id="saved", brief=brief()))
    request = StartRequest(workflow_id="saved", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "postcondition_failed" in result.stderr


def test_show_and_gallery_do_not_launch_hermes(cli_fixture: CliFixture) -> None:
    cli_fixture.save(Workflow(id="saved", brief=brief()))
    shown = cli_fixture.invoke(
        "show", "--workflow", "saved", "--workspace", str(cli_fixture.workspace)
    )
    published = cli_fixture.invoke(
        "gallery",
        "--workflow",
        "saved",
        "--workspace",
        str(cli_fixture.workspace),
    )
    assert shown.returncode == 0, shown.stderr
    assert "draft" in shown.stdout
    assert published.returncode == 0, published.stderr
    assert "index.html" in published.stdout
    assert not (cli_fixture.profile.parent.parent / "invocations.jsonl").exists()
