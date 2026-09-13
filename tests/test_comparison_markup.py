from __future__ import annotations

import json
from html.parser import HTMLParser
from typing import TYPE_CHECKING, override

from logo_helper.comparison_gallery import render_comparison_gallery
from logo_helper.comparison_models import ComparisonManifest, ComparisonSelection
from logo_helper.models import SessionId
from logo_helper.storage import Store
from tests.test_comparison_support import prepare_sources, source_bytes

if TYPE_CHECKING:
    from tests.conftest import Harness


class PageParser(HTMLParser):
    tags: list[tuple[str, dict[str, str | None]]]

    def __init__(self) -> None:
        super().__init__()
        self.tags = []

    @override
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append((tag, dict(attrs)))


def test_markup_and_urls_stay_inert_data_when_notes_and_brand_are_hostile(harness: Harness) -> None:
    # Given: markup, URL schemes, quotes, template strings and control content.
    payload = '</textarea><img src="https://bad.test/" onerror="alert(1)"><script>bad()</script>'
    payload += " javascript:alert(2) $cards `$(touch nope)` ' & \x00\x1b\r\n한글"
    _ = prepare_sources(harness)
    store = Store.at(harness.workspace)
    state = store.load(SessionId("brand"))
    store.save(
        state.model_copy(update={"brief": state.brief.model_copy(update={"brand_name": payload})})
    )
    selection = ComparisonSelection.model_validate_json(
        json.dumps(
            {
                "title": "<script>title()</script>",
                "items": [
                    {
                        "session": "brand",
                        "artifact": "v1",
                        "revision": 1,
                        "rationale": payload,
                        "preserve": payload,
                        "change": payload,
                        "observation": payload,
                    }
                ],
            }
        )
    )
    # When: HTML is generated and parsed as a browser would parse tags/attributes.
    result = render_comparison_gallery(store, selection, "gallery")
    folder = harness.workspace / result.path
    markup = (folder / "index.html").read_text()
    parser = PageParser()
    parser.feed(markup)
    # Then: no supplied tag/attribute or URL becomes active, while JSON retains exact notes.
    assert sum(tag == "script" for tag, _ in parser.tags) == 1
    assert not any(key.startswith("on") for _, attrs in parser.tags for key in attrs)
    for _, attrs in parser.tags:
        for key in ("href", "src"):
            if key in attrs:
                assert attrs[key] in {"images/001.png", "prompts/001.txt", "manifest.json"}
    assert "&lt;script&gt;bad()&lt;/script&gt;" in markup
    assert "\\u0000\\u001b" in markup
    manifest = ComparisonManifest.model_validate_json((folder / "manifest.json").read_bytes())
    assert manifest.artifacts[0].source.rationale == payload
    assert manifest.artifacts[0].brand_name == payload
    assert not (harness.workspace / "nope").exists()


def test_preview_controls_and_exact_facts_are_available_without_remote_assets(
    harness: Harness,
) -> None:
    # Given: a brand and app artwork with different actual dimensions.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    # When: both sources are published.
    result = render_comparison_gallery(Store.at(harness.workspace), selection, "gallery")
    folder = harness.workspace / result.path
    markup = (folder / "index.html").read_text()
    manifest = ComparisonManifest.model_validate_json((folder / "manifest.json").read_bytes())
    # Then: contextual views and size/surround/filter/reset/copy controls are locally available.
    assert [(item.source.session, item.source.artifact) for item in manifest.artifacts] == [
        ("brand", "v1"),
        ("icon", "v1"),
    ]
    assert [(item.image.width, item.image.height) for item in manifest.artifacts] == [
        (120, 48),
        (96, 96),
    ]
    assert [item.kind for item in manifest.artifacts] == ["brand", "app_icon"]
    for context in ("artwork", "app-home", "web-header", "favicon"):
        assert f'value="{context}"' in markup
    for size in (16, 32, 64, 128):
        assert f'width="{size}" height="{size}"' in markup
    for control in ("surround", "kind", "style"):
        assert f'id="{control}"' in markup
    assert 'type="reset"' in markup
    assert 'data-copy="decision-2"' in markup
    assert "illustrative" in markup
    assert not any(
        value in markup for value in ("http://", "https://", "fetch(", "eval(", "innerHTML")
    )


def test_comparison_does_not_approve_selected_candidate_or_relax_export_gate(
    harness: Harness,
) -> None:
    # Given: a selected brand candidate which has never received visual approval.
    _ = prepare_sources(harness)
    _ = harness.ok("select", "--session", "brand", "--artifact", "v1", "--revision", "1")
    selection = ComparisonSelection.model_validate_json(
        '{"title":"Selected","items":[{"session":"brand","artifact":"v1","revision":2}]}'
    )
    before = source_bytes(harness.workspace)
    _ = render_comparison_gallery(Store.at(harness.workspace), selection, "gallery")
    # When: exporting the compared candidate is attempted.
    result = harness.run("export", "--session", "brand", "--revision", "2", "--output", "delivery")
    # Then: review is still required and comparison did not mutate saved selection/approval.
    assert result.returncode == 1
    assert "review" in result.stderr.lower()
    assert not (harness.workspace / "delivery").exists()
    assert source_bytes(harness.workspace) == before
