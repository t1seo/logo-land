from __future__ import annotations

import subprocess
import sys
from typing import TYPE_CHECKING, Final

from logopia_studio.host_requests import StartRequest
from tests.hermes.test_core_fixtures import brief
from tests.hermes.test_launcher_cli_fixtures import REPO

if TYPE_CHECKING:
    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


def test_kernel_releases_lock_after_owner_exits_without_cleanup(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    source = "\n".join(
        (
            "import os, sys",
            "from pathlib import Path",
            f"sys.path.insert(0, {str(REPO / 'integrations/hermes')!r})",
            "from logopia_studio.launcher_profile import profile_lock",
            "with profile_lock(Path(sys.argv[1])):",
            "    os._exit(0)",
        )
    )
    owner = subprocess.run(  # noqa: S603 - isolated owned child and literal path.
        (sys.executable, "-c", source, str(cli_fixture.profile)),
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert owner.returncode == 0, owner.stderr
    request = StartRequest(workflow_id="missing", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert "workflow_missing" in result.stderr
    assert cli_fixture.invocation_count() == 1


def test_lock_symlink_preserves_foreign_target(cli_fixture: CliFixture) -> None:
    cli_fixture.configure()
    foreign = cli_fixture.root / "foreign.txt"
    _ = foreign.write_text("keep", encoding="utf-8")
    (cli_fixture.profile / ".logopia-launch.lock").symlink_to(foreign)
    request = StartRequest(workflow_id="missing", brief=brief())
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode != 0
    assert foreign.read_text(encoding="utf-8") == "keep"
    assert cli_fixture.invocation_count() == 0
