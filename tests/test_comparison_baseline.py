from __future__ import annotations

from typing import TYPE_CHECKING

from logo_helper.app_icon_gallery import GalleryManifest
from tests.test_comparison_support import source_bytes

if TYPE_CHECKING:
    from tests.conftest import Harness


def test_old_icon_gallery_preserves_two_originals_and_session_when_published(
    harness: Harness,
) -> None:
    # Given: two imported candidates with exact CRLF prompts and known PNG bytes.
    harness.init()
    intent = harness.workspace / "icon.json"
    _ = intent.write_text('{"preset":"pictogram","subject":"Book","placement":"center"}')
    _ = harness.prompt.write_bytes(b"Book fixture\r\nExact prompt\n")
    for revision, identifier in enumerate(("v1", "v2")):
        _ = harness.import_image(revision, identifier, "--app-icon-file", str(intent))
    before = source_bytes(harness.workspace)
    # When: the existing public CLI publishes both IDs in explicit order.
    _ = harness.ok("icon-gallery", "--session", "demo", "--artifacts", "v2,v1", "--output", "old")
    # Then: original bytes, prompts, order and every source file remain unchanged.
    folder = harness.workspace / "old"
    manifest = GalleryManifest.model_validate_json((folder / "manifest.json").read_bytes())
    assert [item.artifact_id for item in manifest.artifacts] == ["v2", "v1"]
    for item in manifest.artifacts:
        assert (folder / item.image_file).read_bytes() == harness.png.read_bytes()
        assert (folder / item.prompt_file).read_bytes() == harness.prompt.read_bytes()
    assert source_bytes(harness.workspace) == before
