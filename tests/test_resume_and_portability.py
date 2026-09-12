from __future__ import annotations

import shutil
import subprocess
from typing import TYPE_CHECKING, Literal, assert_never

import pytest
from PIL import Image

from logo_helper.models import Session, SessionId
from tests.conftest import SCRIPT, Harness

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize("tamper", ["path", "parent", "duplicate", "session", "metadata"])
def test_resume_rejects_when_stored_state_is_tampered(
    harness: Harness,
    tamper: Literal["path", "parent", "duplicate", "session", "metadata"],
) -> None:
    # Given a persisted artifact with deliberately inconsistent stored metadata.
    harness.init()
    _ = harness.import_image()
    state = Session.model_validate_json(harness.state_path.read_bytes())
    artifact = state.artifacts[0]
    match tamper:
        case "path":
            corrupted = state.model_copy(
                update={"artifacts": (artifact.model_copy(update={"path": "../../escape.png"}),)}
            )
        case "parent":
            corrupted = state.model_copy(
                update={"artifacts": (artifact.model_copy(update={"parent_id": artifact.id}),)}
            )
        case "duplicate":
            corrupted = state.model_copy(update={"artifacts": (artifact, artifact)})
        case "session":
            corrupted = state.model_copy(update={"id": SessionId("another")})
        case "metadata":
            facts = artifact.image.model_copy(update={"width": 123})
            corrupted = state.model_copy(
                update={"artifacts": (artifact.model_copy(update={"image": facts}),)}
            )
        case _:
            assert_never(tamper)
    _ = harness.state_path.write_text(corrupted.model_dump_json(), encoding="utf-8")
    before = harness.state_path.read_bytes()
    # When another process resumes.
    result = harness.run("show", "--session", "demo")
    # Then unsafe state is rejected without rewriting the evidence.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before


def test_resume_rejects_when_image_was_deleted(harness: Harness) -> None:
    # Given an imported file removed outside the helper.
    harness.init()
    _ = harness.import_image()
    (harness.state_path.parent / "artifacts/v1.png").unlink()
    # When resuming from saved state only.
    result = harness.run("show", "--session", "demo")
    # Then absence is explicit rather than a fabricated preview.
    assert result.returncode != 0
    assert "invalid_file" in result.stderr


def test_export_succeeds_when_opaque_background_was_requested(harness: Harness) -> None:
    # Given an intentionally opaque brief and actual RGB image.
    _ = harness.brief.write_text(
        harness.brief.read_text(encoding="utf-8").replace('"transparent"', '"opaque"'),
        encoding="utf-8",
    )
    with Image.new("RGB", (8, 8), "green") as image:
        image.save(harness.png)
    harness.prepare_export()
    # When exporting after explicit review.
    result = harness.run("export", "--session", "demo", "--revision", "3")
    # Then an opaque PNG is valid and preserved as opaque.
    assert result.returncode == 0, result.stderr
    manifest = harness.workspace / "output/logo-generator/demo/manifest.json"
    assert '"transparency_verified": false' in manifest.read_text(encoding="utf-8")


def test_export_rejects_when_opaque_brief_has_transparent_pixels(harness: Harness) -> None:
    # Given an opaque brief, an alpha image, and all-true visual review assertions.
    _ = harness.brief.write_text(
        harness.brief.read_text(encoding="utf-8").replace('"transparent"', '"opaque"'),
        encoding="utf-8",
    )
    harness.prepare_export()
    before = harness.state_path.read_bytes()
    # When an incorrectly reviewed transparent image is exported.
    result = harness.run("export", "--session", "demo", "--revision", "3")
    # Then actual alpha facts override the incorrect review and no bundle is created.
    assert result.returncode != 0
    assert "opaque" in result.stderr.lower()
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output/logo-generator/demo").exists()


def test_import_preserves_orphan_file_when_untracked_path_exists(harness: Harness) -> None:
    # Given an untracked file at the requested immutable artifact path.
    harness.init()
    directory = harness.state_path.parent / "artifacts"
    directory.mkdir()
    target = directory / "v1.png"
    _ = target.write_bytes(b"user-owned existing bytes")
    before = harness.state_path.read_bytes()
    # When an import would reuse that path.
    result = harness.run(
        "import",
        "--session",
        "demo",
        "--artifact",
        "v1",
        "--image",
        str(harness.png),
        "--prompt-file",
        str(harness.prompt),
        "--revision",
        "0",
    )
    # Then neither the orphan nor session state is overwritten.
    assert result.returncode != 0
    assert target.read_bytes() == b"user-owned existing bytes"
    assert harness.state_path.read_bytes() == before


def test_export_rejects_when_output_parent_is_symlink(harness: Harness, tmp_path: Path) -> None:
    # Given a reviewed artifact and a destination alias pointing outside the workspace.
    harness.prepare_export()
    (harness.workspace / "linked").symlink_to(tmp_path, target_is_directory=True)
    # When custom output would follow the symlink.
    result = harness.run(
        "export",
        "--session",
        "demo",
        "--revision",
        "3",
        "--output",
        "linked/escaped",
    )
    # Then the target outside the workspace is untouched.
    assert result.returncode != 0
    assert not (tmp_path / "escaped").exists()


def test_init_rejects_when_state_root_is_symlink(harness: Harness, tmp_path: Path) -> None:
    # Given managed storage replaced with an outside alias before initialization.
    (harness.workspace / ".logo-generator").symlink_to(tmp_path, target_is_directory=True)
    # When creating a session.
    result = harness.run("init", "--session", "demo", "--brief", str(harness.brief))
    # Then state cannot escape into that target.
    assert result.returncode != 0
    assert not (tmp_path / "sessions").exists()


def test_cli_runs_when_only_skill_scripts_are_copied(harness: Harness, tmp_path: Path) -> None:
    # Given a skill copied to a path with spaces without the repository root files.
    copied = tmp_path / "portable plugin" / "scripts"
    _ = shutil.copytree(SCRIPT.parent, copied, ignore=shutil.ignore_patterns("__pycache__"))
    uv = shutil.which("uv")
    assert uv is not None
    # When a fresh interpreter invokes that copied CLI from another current directory.
    result = subprocess.run(
        [
            uv,
            "run",
            "--offline",
            "--project",
            str(SCRIPT.parents[3]),
            str(copied / "logo_project.py"),
            "--workspace",
            str(harness.workspace),
            "init",
            "--session",
            "demo",
            "--brief",
            str(harness.brief),
        ],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
        timeout=20,
    )
    # Then local sibling imports work without developer-specific paths.
    assert result.returncode == 0, result.stderr
    assert Session.model_validate_json(result.stdout).revision == 0
