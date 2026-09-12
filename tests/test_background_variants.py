from __future__ import annotations

from typing import TYPE_CHECKING
from zipfile import ZipFile

import pytest
from PIL import Image

from logo_helper.delivery import Manifest
from logo_helper.models import Background, Brief, Session
from logo_helper.prompts import PromptResult

if TYPE_CHECKING:
    from tests.conftest import Harness


def prepare_parent(harness: Harness, background: Background) -> None:
    brief = Brief.model_validate_json(harness.brief.read_bytes())
    _ = harness.brief.write_text(
        brief.model_copy(update={"background": background}).model_dump_json(), encoding="utf-8"
    )
    set_fixture_background(harness, background)
    harness.init()
    _ = harness.import_image()


def set_fixture_background(harness: Harness, background: Background) -> None:
    with Image.open(harness.png) as image, image.convert("RGBA") as rgba:
        rgba.putpixel((0, 0), (0, 120, 50, 0 if background == "transparent" else 255))
        rgba.save(harness.png)


def select_and_review(harness: Harness, artifact: str, revision: int) -> None:
    _ = harness.ok(
        "select", "--session", "demo", "--artifact", artifact, "--revision", str(revision)
    )
    _ = harness.ok(
        "review",
        "--session",
        "demo",
        "--artifact",
        artifact,
        "--revision",
        str(revision + 1),
        "--review-file",
        str(harness.review),
    )


@pytest.mark.parametrize(
    ("initial", "requested"), [("opaque", "transparent"), ("transparent", "opaque")]
)
def test_export_when_child_requests_opposite_background(
    harness: Harness, initial: Background, requested: Background
) -> None:
    # Given a reviewed child whose explicit background differs from its original brief.
    prepare_parent(harness, initial)
    set_fixture_background(harness, requested)
    _ = harness.prompt.write_text(f"Change the background to {requested}.", encoding="utf-8")
    _ = harness.import_image(1, "v2", "--parent", "v1", "--background", requested)
    select_and_review(harness, "v2", 2)
    # When the selected child is exported through a fresh CLI process.
    _ = harness.ok("export", "--session", "demo", "--revision", "4")
    # Then the bundle records both historical and selected intent and preserves the child bytes.
    output = harness.workspace / "output/logo-generator/demo"
    manifest = Manifest.model_validate_json((output / "manifest.json").read_bytes())
    assert manifest.brief.background == initial
    assert manifest.source.id == "v2"
    assert manifest.source.parent_id == "v1"
    assert manifest.source.requested_background == requested
    assert manifest.requested_background == requested
    assert manifest.transparency_verified == (requested == "transparent")
    assert (output / "logo.png").read_bytes() == harness.png.read_bytes()
    guide = (output / "brand-guide.md").read_text(encoding="utf-8")
    assert f"Initial brief background (historical intent): {initial}" in guide
    assert f"Selected artifact requested background: {requested}" in guide
    with ZipFile(output / "logo-package.zip") as archive:
        assert archive.read("logo.png") == harness.png.read_bytes()
        assert archive.read("manifest.json") == (output / "manifest.json").read_bytes()
        assert archive.read("brand-guide.md") == (output / "brand-guide.md").read_bytes()
    resumed = Session.model_validate_json(harness.ok("show", "--session", "demo"))
    assert resumed.selected_id == "v2"
    assert resumed.artifacts[0].requested_background == initial
    assert resumed.artifacts[1].requested_background == requested
    assert resumed.revision == 5


@pytest.mark.parametrize(
    ("initial", "requested"), [("opaque", "transparent"), ("transparent", "opaque")]
)
def test_export_rejects_when_child_pixels_mismatch_explicit_background(
    harness: Harness, initial: Background, requested: Background
) -> None:
    # Given a child that requests the opposite background but retains the original pixels.
    prepare_parent(harness, initial)
    _ = harness.import_image(1, "v2", "--parent", "v1", "--background", requested)
    select_and_review(harness, "v2", 2)
    before = harness.state_path.read_bytes()
    # When export checks the explicit request despite an all-passing visual review.
    result = harness.run("export", "--session", "demo", "--revision", "4")
    # Then the mismatch is rejected without state or delivery side effects.
    assert result.returncode == 1
    assert f"background_mismatch: Requested {requested}" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output/logo-generator/demo").exists()


@pytest.mark.parametrize(
    ("initial", "requested"), [("opaque", "transparent"), ("transparent", "opaque")]
)
def test_export_when_original_is_selected_after_opposite_child_import(
    harness: Harness, initial: Background, requested: Background
) -> None:
    # Given an original selected after importing a newer child with a different background.
    prepare_parent(harness, initial)
    parent_bytes = harness.png.read_bytes()
    set_fixture_background(harness, requested)
    _ = harness.import_image(1, "v2", "--parent", "v1", "--background", requested)
    select_and_review(harness, "v1", 2)
    # When exporting the explicitly selected original.
    _ = harness.ok("export", "--session", "demo", "--revision", "4")
    # Then the newer child's background intent does not affect the selected delivery.
    output = harness.workspace / "output/logo-generator/demo"
    manifest = Manifest.model_validate_json((output / "manifest.json").read_bytes())
    assert manifest.source.id == "v1"
    assert manifest.requested_background == initial
    assert (output / "logo.png").read_bytes() == parent_bytes


@pytest.mark.parametrize("changes", ["Use navy blue", "Make the background opaque"])
def test_prompt_when_parent_background_differs_from_original(
    harness: Harness, changes: str
) -> None:
    # Given an opaque brief and a transparent parent whose latest edit may change background.
    prepare_parent(harness, "opaque")
    set_fixture_background(harness, "transparent")
    _ = harness.import_image(1, "v2", "--parent", "v1", "--background", "transparent")
    before = harness.state_path.read_bytes()
    # When the next edit prompt is built from that parent.
    result = PromptResult.model_validate_json(
        harness.ok("prompt", "--session", "demo", "--parent", "v2", "--changes", changes)
    )
    # Then historical brief intent, parent intent, and authoritative latest changes are distinct.
    assert result.parent_id == "v2"
    assert result.parent_requested_background == "transparent"
    assert "Initial brief background (historical intent): opaque" in result.prompt
    assert changes in result.prompt
    assert "Latest requested changes" in result.prompt
    assert "Requested changes override" in result.prompt
    assert str(harness.state_path.parent / "artifacts/v2.png") == result.parent_image_path
    assert harness.state_path.read_bytes() == before
