from __future__ import annotations

from typing import TYPE_CHECKING, Literal, assert_never

import pytest
from PIL import Image

from tests.conftest import Harness, SessionView

if TYPE_CHECKING:
    from pathlib import Path


@pytest.mark.parametrize("kind", ["jpeg", "truncated", "empty", "transparent"])
def test_import_when_png_is_invalid(
    harness: Harness,
    kind: Literal["jpeg", "truncated", "empty", "transparent"],
) -> None:
    # Given an initialized session and an invalid PNG source.
    harness.init()
    match kind:
        case "jpeg":
            with Image.new("RGB", (8, 8), "green") as image:
                image.save(harness.png, format="JPEG")
        case "truncated":
            _ = harness.png.write_bytes(harness.png.read_bytes()[:40])
        case "empty":
            _ = harness.png.write_bytes(b"")
        case "transparent":
            with Image.new("RGBA", (8, 8), (0, 0, 0, 0)) as image:
                image.save(harness.png)
        case _:
            assert_never(kind)
    before = harness.state_path.read_bytes()
    # When the invalid file is imported.
    result = harness.run(
        "import",
        "--session",
        "demo",
        "--artifact",
        "bad",
        "--image",
        str(harness.png),
        "--prompt-file",
        str(harness.prompt),
        "--revision",
        "0",
    )
    # Then neither success state nor an artifact is written.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
    assert not (harness.state_path.parent / "artifacts/bad.png").exists()


@pytest.mark.parametrize(
    "extra", [("--parent", "absent"), ("--artifact", "../escape"), ("--revision", "9")]
)
def test_import_when_request_is_unsafe(harness: Harness, extra: tuple[str, str]) -> None:
    # Given a pristine session.
    harness.init()
    before = harness.state_path.read_bytes()
    # When parent, artifact identifier, or revision violates the contract.
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
        *extra,
    )
    # Then the previous state is byte-identical.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before


def test_import_when_artifact_id_exists(harness: Harness) -> None:
    # Given an existing immutable artifact.
    harness.init()
    _ = harness.import_image()
    before = harness.state_path.read_bytes()
    # When that identifier is reused.
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
        "1",
    )
    # Then the original metadata and file survive.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
    assert (harness.state_path.parent / "artifacts/v1.png").read_bytes() == harness.png.read_bytes()


def test_resume_when_artifact_hash_changed(harness: Harness) -> None:
    # Given a recorded artifact changed outside the helper.
    harness.init()
    _ = harness.import_image()
    _ = (harness.state_path.parent / "artifacts/v1.png").write_bytes(b"tampered")
    # When the user resumes in another process.
    result = harness.run("show", "--session", "demo")
    # Then the corruption is explicit.
    assert result.returncode != 0
    assert "hash" in result.stderr.lower()


@pytest.mark.parametrize("state", ["{", '{"schema_version":99}', '{"schema_version":1}'])
def test_resume_when_state_is_corrupt(harness: Harness, state: str) -> None:
    # Given an unsupported or malformed stored state.
    harness.init()
    _ = harness.state_path.write_text(state, encoding="utf-8")
    # When showing the session.
    result = harness.run("show", "--session", "demo")
    # Then the state is preserved with a diagnostic.
    assert result.returncode != 0
    assert result.stderr
    assert harness.state_path.read_text(encoding="utf-8") == state


@pytest.mark.parametrize("mode", ["RGB", "RGBA"])
def test_export_when_transparency_request_has_opaque_pixels(harness: Harness, mode: str) -> None:
    # Given an opaque image, including RGBA with all alpha values 255.
    with Image.new(mode, (8, 8), "green") as image:
        image.save(harness.png)
    harness.prepare_export()
    # When a transparent delivery is requested by the brief.
    result = harness.run("export", "--session", "demo", "--revision", "3")
    # Then alpha-channel presence alone cannot pass.
    assert result.returncode != 0
    assert "transparen" in result.stderr.lower()


def test_export_when_destination_already_exists(harness: Harness) -> None:
    # Given an exported bundle.
    harness.prepare_export()
    _ = harness.ok("export", "--session", "demo", "--revision", "3")
    original = (harness.workspace / "output/logo-generator/demo/logo.png").read_bytes()
    # When exporting again to the same location.
    result = harness.run("export", "--session", "demo", "--revision", "4")
    # Then no existing bytes are overwritten.
    assert result.returncode != 0
    assert (harness.workspace / "output/logo-generator/demo/logo.png").read_bytes() == original


def test_import_when_storage_is_symlink(harness: Harness, tmp_path: Path) -> None:
    # Given storage replaced by a link outside the session.
    harness.init()
    images = harness.state_path.parent / "artifacts"
    if images.exists():
        images.rmdir()
    images.symlink_to(tmp_path, target_is_directory=True)
    # When import would follow that link.
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
    # Then storage escape is rejected.
    assert result.returncode != 0
    assert not (tmp_path / "v1.png").exists()


def test_export_when_output_traverses_workspace(harness: Harness) -> None:
    # Given an exportable session.
    harness.prepare_export()
    # When the requested destination escapes the workspace.
    result = harness.run(
        "export",
        "--session",
        "demo",
        "--revision",
        "3",
        "--output",
        "../outside",
    )
    # Then no output or revision update occurs.
    assert result.returncode != 0
    assert SessionView.model_validate_json(harness.ok("show", "--session", "demo")).revision == 3
