from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from logo_helper.models import Session

if TYPE_CHECKING:
    from tests.conftest import Harness


@pytest.mark.parametrize(
    "output",
    [
        ".logo-generator",
        ".logo-generator/locks",
        ".logo-generator/locks/demo.lock/package",
        ".logo-generator/locks/another.lock/package",
        ".logo-generator/sessions/demo",
        ".logo-generator/sessions/another",
        ".logo-generator/sessions/demo/artifacts/package",
        ".logo-generator//locks/demo.lock/package",
        ".LOGO-GENERATOR/locks/demo.lock/package",
    ],
)
def test_export_rejects_when_output_is_reserved(harness: Harness, output: str) -> None:
    # Given a reviewed session and any output within the reserved storage namespace.
    harness.prepare_export()
    before = harness.state_path.read_bytes()
    before_paths = sorted(harness.workspace.rglob("*"))
    # When the actual CLI attempts that export.
    result = harness.run("export", "--session", "demo", "--revision", "3", "--output", output)
    # Then the stable domain error leaves all state and files unchanged, with no held lock.
    assert result.returncode == 1
    assert "reserved_output:" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert sorted(harness.workspace.rglob("*")) == before_paths
    assert not (harness.workspace / ".logo-generator/locks/demo.lock").exists()


def test_export_rejects_reserved_output_before_creating_storage(harness: Harness) -> None:
    # Given an empty workspace with no helper state or lock directories.
    assert not tuple(harness.workspace.iterdir())
    # When a reserved output is supplied even without an existing session.
    result = harness.run(
        "export", "--session", "demo", "--revision", "0", "--output", ".logo-generator/package"
    )
    # Then validation precedes every managed-storage write, including lock acquisition.
    assert result.returncode == 1
    assert "reserved_output:" in result.stderr
    assert not tuple(harness.workspace.iterdir())


@pytest.mark.parametrize("output", ["exports/final-v2", ".logo-generator-backup/final-v2"])
def test_export_succeeds_when_custom_output_is_not_reserved(harness: Harness, output: str) -> None:
    # Given a reviewed session and an ordinary or similarly named user output directory.
    harness.prepare_export()
    # When the actual CLI exports outside the reserved namespace.
    result = harness.ok("export", "--session", "demo", "--revision", "3", "--output", output)
    # Then the PNG is preserved and the successful revision is committed without a held lock.
    state = Session.model_validate_json(result)
    assert state.revision == 4
    assert state.exports[-1].path == output
    assert (harness.workspace / output / "logo.png").read_bytes() == harness.png.read_bytes()
    assert not (harness.workspace / ".logo-generator/locks/demo.lock").exists()
