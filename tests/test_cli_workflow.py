from __future__ import annotations

import hashlib
import json
from zipfile import ZipFile

from tests.conftest import Harness, SessionView


def test_init_when_brief_contains_unicode(harness: Harness) -> None:
    # Given a JSON brief in a workspace with spaces and Korean characters.
    # When the user creates a session in a fresh process.
    result = harness.ok("init", "--session", "demo", "--brief", str(harness.brief))
    # Then the persisted brief survives without losing text.
    assert SessionView.model_validate_json(result).revision == 0
    assert "모로 스튜디오" in harness.state_path.read_text(encoding="utf-8")


def test_resume_when_edit_has_parent_lineage(harness: Harness) -> None:
    # Given two immutable imported image revisions.
    harness.init()
    _ = harness.import_image()
    _ = harness.import_image(1, "v2", "--parent", "v1")
    # When a fresh process resumes the session.
    state = SessionView.model_validate_json(harness.ok("show", "--session", "demo"))
    # Then both files and the explicit parent remain available.
    assert [(item.id, item.parent_id) for item in state.artifacts] == [("v1", None), ("v2", "v1")]
    for item in state.artifacts:
        assert (harness.state_path.parent / item.path).read_bytes() == harness.png.read_bytes()


def test_export_when_selected_image_is_explicitly_reviewed(harness: Harness) -> None:
    # Given a selected, explicitly reviewed fixture image.
    harness.prepare_export()
    # When the delivery bundle is exported through the CLI.
    _ = harness.ok("export", "--session", "demo", "--revision", "3")
    # Then the ZIP and on-disk deliverable preserve the actual PNG byte for byte.
    output = harness.workspace / "output/logo-generator/demo"
    source_hash = hashlib.sha256(harness.png.read_bytes()).hexdigest()
    with ZipFile(output / "logo-package.zip") as archive:
        assert set(archive.namelist()) == {"logo.png", "manifest.json", "brand-guide.md"}
        assert hashlib.sha256(archive.read("logo.png")).hexdigest() == source_hash
        assert archive.read("manifest.json") == (output / "manifest.json").read_bytes()
    assert "raster" in (output / "brand-guide.md").read_text(encoding="utf-8").lower()
    resumed = SessionView.model_validate_json(harness.ok("show", "--session", "demo"))
    assert resumed.revision == 4


def test_prompt_when_edit_changes_color(harness: Harness) -> None:
    # Given an imported parent.
    harness.init()
    _ = harness.import_image()
    # When an edit prompt is built without mutating the session.
    result = harness.ok(
        "prompt",
        "--session",
        "demo",
        "--parent",
        "v1",
        "--changes",
        "Use navy blue",
    )
    # Then the requested edit and a verifiable exact parent file are exposed.
    assert "Use navy blue" in result
    assert "Requested changes override" in result
    assert "original brief context" in result
    assert str(harness.state_path.parent / "artifacts/v1.png") in result
    assert SessionView.model_validate_json(harness.ok("show", "--session", "demo")).revision == 1


def test_list_when_multiple_sessions_exist(harness: Harness) -> None:
    # Given independently named sessions.
    harness.init()
    _ = harness.ok("init", "--session", "second", "--brief", str(harness.brief))
    # When listing the workspace.
    result = harness.ok("list")
    # Then explicit session identifiers are returned.
    assert '"demo"' in result
    assert '"second"' in result


def test_failure_when_host_did_not_return_image(harness: Harness) -> None:
    # Given a session and a host tool failure.
    harness.init()
    # When the failure is recorded.
    result = harness.ok(
        "failure",
        "--session",
        "demo",
        "--prompt-file",
        str(harness.prompt),
        "--reason",
        "Host image tool unavailable",
        "--revision",
        "0",
    )
    # Then no artifact is invented and the reason survives resume.
    state = SessionView.model_validate_json(result)
    assert state.artifacts == ()
    assert "Host image tool unavailable" in harness.ok("show", "--session", "demo")


def test_export_when_visual_review_failed(harness: Harness) -> None:
    # Given an explicitly failed visual review.
    _ = harness.review.write_text(
        json.dumps(
            {
                "reviewer": "tester",
                "notes": "Text unreadable",
                "text_correct": False,
                "composition_ok": True,
                "small_size_ok": True,
                "preservation_ok": True,
                "background_checked": True,
            }
        ),
        encoding="utf-8",
    )
    harness.prepare_export()
    # When export is attempted.
    result = harness.run("export", "--session", "demo", "--revision", "3")
    # Then no bundle is produced.
    assert result.returncode != 0
    assert "review" in result.stderr.lower()
    assert not (harness.workspace / "output/logo-generator/demo").exists()
