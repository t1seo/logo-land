from __future__ import annotations

from typing import TYPE_CHECKING

from logo_helper.comparison_models import ComparisonManifest, ComparisonResult
from tests.test_comparison_support import prepare_sources, source_bytes

if TYPE_CHECKING:
    from tests.conftest import Harness


def test_compare_namespaces_duplicate_ids_when_brand_and_icon_share_v1(harness: Harness) -> None:
    # Given: two real sessions have different unreviewed PNGs both named v1.
    selection = prepare_sources(harness)
    before = source_bytes(harness.workspace)
    # When: the actual CLI publishes a combined comparison snapshot.
    result = harness.run(
        "compare-gallery", "--selection-file", str(selection), "--output", "gallery"
    )
    # Then: both source identities, original/prompt bytes and source state survive.
    assert result.returncode == 0, result.stderr
    folder = harness.workspace / "gallery"
    manifest = ComparisonManifest.model_validate_json((folder / "manifest.json").read_bytes())
    assert manifest.kind == "comparison_gallery"
    for number, session in enumerate(("brand", "icon"), 1):
        original = before[f"sessions/{session}/artifacts/v1.png"]
        assert (folder / f"images/{number:03d}.png").read_bytes() == original
        assert (folder / f"prompts/{number:03d}.txt").read_bytes() == (
            f"Exact {session} prompt\r\nKeep book shape. 한글\n".encode()
        )
    markup = (folder / "index.html").read_text()
    assert 'data-session="brand"' in markup
    assert 'data-session="icon"' in markup
    assert source_bytes(harness.workspace) == before
    assert ComparisonResult.model_validate_json(result.stdout).index_path == "gallery/index.html"
