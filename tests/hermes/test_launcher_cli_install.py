from __future__ import annotations

from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.host_settings import load_settings
from logopia_studio.launcher_install import install_profile
from logopia_studio.launcher_process import ProcessReceipt
from pydantic import TypeAdapter
from tests.hermes.test_launcher_cli_fixtures import REPO

if TYPE_CHECKING:
    from pathlib import Path

    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


def _calls(cli_fixture: CliFixture) -> tuple[tuple[str, ...], ...]:
    path = cli_fixture.profile.parent.parent / "invocations.jsonl"
    return tuple(
        TypeAdapter(tuple[str, ...]).validate_json(line)
        for line in path.read_text(encoding="utf-8").splitlines()
    )


def _install(cli_fixture: CliFixture) -> tuple[str, ...]:
    return (
        "install",
        "--profile",
        "logopia",
        "--profile-home",
        str(cli_fixture.profile),
        "--workspace",
        str(cli_fixture.workspace),
    )


def test_install_sets_only_named_profile_native_deadlines(cli_fixture: CliFixture) -> None:
    config = cli_fixture.profile / "config.yaml"
    _ = config.write_text("model: unchanged\n", encoding="utf-8")
    default = cli_fixture.profile.parent.parent / "config.yaml"
    _ = default.write_bytes(b"default profile sentinel\n")
    result = cli_fixture.invoke(*_install(cli_fixture))
    assert result.returncode == 0, result.stderr
    assert _calls(cli_fixture) == (
        (
            "-p",
            "logopia",
            "plugins",
            "doctor",
            str(cli_fixture.profile / "plugins/logopia-studio"),
            "--ci",
        ),
        ("-p", "logopia", "config", "set", "timeouts.tools.sequential_call", "1800"),
        ("-p", "logopia", "config", "set", "timeouts.tools.concurrent_batch", "1800"),
        ("-p", "logopia", "plugins", "enable", "logopia-studio", "--no-allow-tool-override"),
    )
    assert "timeouts.tools.sequential_call=1800" in result.stdout
    assert "timeouts.tools.concurrent_batch=1800" in result.stdout
    assert default.read_bytes() == b"default profile sentinel\n"
    assert config.read_text(encoding="utf-8") == "model: unchanged\n"
    settings = load_settings(cli_fixture.profile / "plugins/logopia-studio")
    assert settings.workspace == cli_fixture.workspace


def test_failed_doctor_stops_before_enable(cli_fixture: CliFixture) -> None:
    cli_fixture.mode("doctor-fail")
    result = cli_fixture.invoke(
        "install",
        "--profile",
        "logopia",
        "--profile-home",
        str(cli_fixture.profile),
        "--workspace",
        str(cli_fixture.workspace),
    )
    assert result.returncode != 0
    assert "doctor_failed" in result.stderr
    assert cli_fixture.invocation_count() == 1


def test_dirty_foreign_plugin_is_preserved(cli_fixture: CliFixture) -> None:
    plugin = cli_fixture.profile / "plugins/logopia-studio"
    plugin.mkdir(parents=True)
    foreign = plugin / "user-content.txt"
    _ = foreign.write_text("retain", encoding="utf-8")
    result = cli_fixture.invoke(
        "install",
        "--profile",
        "logopia",
        "--profile-home",
        str(cli_fixture.profile),
        "--workspace",
        str(cli_fixture.workspace),
    )
    assert result.returncode != 0
    assert "unmanaged_install" in result.stderr
    assert foreign.read_text(encoding="utf-8") == "retain"
    assert cli_fixture.invocation_count() == 0


@pytest.mark.parametrize(("key", "count"), [("sequential_call", 2), ("concurrent_batch", 3)])
def test_failed_timeout_configuration_stops_install(
    cli_fixture: CliFixture, key: str, count: int
) -> None:
    cli_fixture.mode(f"{key}-fail")
    result = cli_fixture.invoke(*_install(cli_fixture))
    assert result.returncode != 0
    assert f"{key}_failed" in result.stderr
    assert f"timeouts.tools.{key}" in result.stderr
    assert cli_fixture.invocation_count() == count
    assert all("enable" not in call and "chat" not in call for call in _calls(cli_fixture))


def test_reinstall_managed_payload_reapplies_finite_deadlines(cli_fixture: CliFixture) -> None:
    for _ in range(2):
        result = cli_fixture.invoke(*_install(cli_fixture))
        assert result.returncode == 0, result.stderr
    calls = _calls(cli_fixture)
    assert len(calls) == 8
    assert calls[:4] == calls[4:]
    assert not (cli_fixture.profile.parent.parent / "fixture-image-calls.txt").exists()


def test_install_preserves_literal_unusual_workspace(cli_fixture: CliFixture) -> None:
    unusual = cli_fixture.root / "workspace 한글 ' ; $(touch SHOULD_NOT_RUN)"
    unusual.mkdir()
    arguments = (*_install(cli_fixture)[:-1], str(unusual))
    result = cli_fixture.invoke(*arguments)
    assert result.returncode == 0, result.stderr
    settings = load_settings(cli_fixture.profile / "plugins/logopia-studio")
    assert settings.workspace == unusual
    assert not (REPO / "SHOULD_NOT_RUN").exists()
    assert not (unusual / "SHOULD_NOT_RUN").exists()
    assert cli_fixture.invocation_count() == 4


def test_all_install_commands_remain_bounded(
    cli_fixture: CliFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[tuple[str, ...]] = []

    def run(
        command: tuple[str, ...], workspace: Path, output: Path, timeout_seconds: int
    ) -> ProcessReceipt:
        assert timeout_seconds == 120
        assert workspace == cli_fixture.workspace
        calls.append(command)
        return ProcessReceipt(
            exit_code=0,
            timed_out=False,
            interrupted=False,
            stdout_path=output / "stdout.txt",
            stderr_path=output / "stderr.txt",
        )

    monkeypatch.setenv("HERMES_HOME", str(cli_fixture.profile.parent.parent))
    monkeypatch.setattr("logopia_studio.launcher_install.run_process", run)
    result = install_profile(
        "logopia", cli_fixture.profile, cli_fixture.workspace, REPO / "integrations/hermes", REPO
    )
    assert result.success
    assert len(calls) == 4
