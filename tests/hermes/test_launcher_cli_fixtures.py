from __future__ import annotations

import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.host_settings import HostSettings
from logopia_studio.store import Store

if TYPE_CHECKING:
    from collections.abc import Generator

    from logopia_studio.models import Workflow

REPO: Final = Path(__file__).resolve().parents[2]
ENTRY: Final = REPO / "integrations/hermes/studio.py"


@dataclass(frozen=True, slots=True)
class CliFixture:
    root: Path
    profile: Path
    workspace: Path
    executable: Path

    def invoke(self, *arguments: str, timeout: int = 20) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment["HERMES_HOME"] = str(self.profile.parent.parent)
        environment["PATH"] = str(self.executable.parent) + os.pathsep + environment["PATH"]
        environment["NO_COLOR"] = "1"
        environment["TERM"] = "dumb"
        return subprocess.run(  # noqa: S603 - literal argv, isolated fake executable.
            (sys.executable, str(ENTRY), *arguments),
            cwd=REPO,
            env=environment,
            text=True,
            capture_output=True,
            check=False,
            timeout=timeout,
        )

    def run(self, request: Path, *options: str) -> subprocess.CompletedProcess[str]:
        return self.invoke(
            "run",
            "--profile",
            "logopia",
            "--profile-home",
            str(self.profile),
            "--request",
            str(request),
            *options,
        )

    def request(self, raw: str) -> Path:
        path = self.root / "request 한글 with spaces.json"
        _ = path.write_text(raw, encoding="utf-8")
        return path

    def configure(self) -> None:
        plugin = self.profile / "plugins/logopia-studio"
        plugin.mkdir(parents=True, exist_ok=True)
        settings = HostSettings(schema_version=1, workspace=self.workspace, helper_repo=REPO)
        _ = (plugin / "settings.json").write_text(settings.model_dump_json(), encoding="utf-8")

    def save(self, state: Workflow) -> None:
        _ = Store(self.workspace).save(state)

    def mode(self, value: str) -> None:
        _ = (self.profile.parent.parent / "mode.txt").write_text(value, encoding="utf-8")

    def invocation_count(self) -> int:
        path = self.profile.parent.parent / "invocations.jsonl"
        return len(path.read_text(encoding="utf-8").splitlines()) if path.exists() else 0


def make_cli_fixture(tmp_path: Path) -> CliFixture:
    profile = tmp_path / "hermes/profiles/logopia"
    profile.mkdir(parents=True)
    workspace = tmp_path / "workspace 한글 space"
    workspace.mkdir()
    executable = tmp_path / "bin/hermes"
    executable.parent.mkdir()
    _ = executable.write_text(
        "\n".join(
            (
                f"#!{sys.executable}",
                "import sys",
                f"sys.path.insert(0, {str(REPO)!r})",
                f"sys.path.insert(0, {str(REPO / 'integrations/hermes')!r})",
                "from tests.hermes.test_launcher_cli_fake import main",
                "main()",
                "",
            )
        ),
        encoding="utf-8",
    )
    executable.chmod(0o700)
    return CliFixture(tmp_path, profile, workspace, executable)


@pytest.fixture
def cli_fixture(tmp_path: Path) -> Generator[CliFixture, None, None]:
    with TemporaryDirectory(prefix="launcher-", dir=tmp_path) as temporary:
        yield make_cli_fixture(Path(temporary).resolve())
