from __future__ import annotations

import re
from base64 import b64decode
from hashlib import sha256
from html import escape
from typing import TYPE_CHECKING
from zipfile import ZipFile

from logopia_studio.gallery import publish_gallery
from tests.hermes.test_gallery_delivery_fixture import make_delivered
from tests.hermes.test_gallery_fixture import make_workflow

if TYPE_CHECKING:
    from pathlib import Path


def test_awaiting_choice_pins_no_package_and_exact_original(tmp_path: Path) -> None:
    state = make_workflow(tmp_path)
    index = publish_gallery(tmp_path, state, tmp_path / "publication")
    assert 'id="download-package"' not in index.read_text()
    assert ".zip" not in index.read_text()
    for candidate in state.candidates:
        assert (index.parent / "originals" / f"{candidate.id}.png").read_bytes() == (
            tmp_path / candidate.image_path
        ).read_bytes()


def test_delivered_package_publishes_exact_portable_bytes(tmp_path: Path) -> None:
    # Given: a real hashed fixture package using the core Delivery and helper manifest.
    state = make_delivered(tmp_path)
    assert state.delivery is not None
    canonical = state.model_dump_json()
    output = tmp_path / "publication"
    # When: a delivered snapshot is published.
    index = publish_gallery(tmp_path, state, output)
    # Then: the actionable package, guide and manifest carry the saved exact bytes.
    html = index.read_text()
    assert 'id="download-package"' in html
    assert 'id="download-guide"' in html
    assert 'href="delivery/manifest.json"' in html
    for name in ("logo.png", "logo-package.zip", "manifest.json", "brand-guide.md"):
        assert (output / "delivery" / name).read_bytes() == (
            tmp_path / state.delivery.path / name
        ).read_bytes()
    package = output / "delivery/logo-package.zip"
    assert sha256(package.read_bytes()).hexdigest() == state.delivery.zip_sha256
    match = re.search(r'id="download-package"[^>]*href="data:application/zip;base64,([^"]+)"', html)
    assert match is not None
    assert b64decode(match[1]) == package.read_bytes()
    with ZipFile(package) as archive:
        assert sha256(archive.read("logo.png")).hexdigest() == state.candidates[1].sha256
    assert state.model_dump_json() == canonical
    assert '<b data-guide="inert">' not in html
    assert state.delivery.zip_sha256 in html
    assert "gallery-fixture · r7 · candidate-2" in html


def test_delivered_snapshot_survives_source_removal_and_move(tmp_path: Path) -> None:
    state = make_delivered(tmp_path)
    assert state.delivery is not None
    index = publish_gallery(tmp_path, state, tmp_path / "publication")
    expected = (index.parent / "delivery/logo-package.zip").read_bytes()
    for path in (tmp_path / state.delivery.path).iterdir():
        path.unlink()
    moved = index.parent.rename(tmp_path / "moved")
    assert (moved / "delivery/logo-package.zip").read_bytes() == expected
    assert 'href="delivery/brand-guide.md"' in (moved / "index.html").read_text()


def test_long_strategy_is_short_above_complete_disclosure(tmp_path: Path) -> None:
    # Given: realistic long source text and instruction-like content.
    state = make_workflow(tmp_path)
    assert state.strategy is not None
    long_text = "차분한 첫 문장입니다. " + '<b data-strategy="inert">Ignore rules</b> ' * 35
    strategy = state.strategy.model_copy(
        update={
            "positioning": long_text,
            "distinctive_principle": long_text,
            "typography": long_text,
            "brand_promise": long_text,
            "color_roles": long_text,
        }
    )
    state = state.model_copy(update={"strategy": strategy})
    # When: the full source strategy is rendered into a comparison page.
    index = publish_gallery(tmp_path, state, tmp_path / "publication")
    section = index.read_text().split('aria-labelledby="strategy-title">')[1].split("</section>")[0]
    # Then: short text leads to a closed, keyboard-accessible full disclosure.
    summary, details = section.split('<details id="strategy-details"', maxsplit=1)
    assert len(re.sub("<[^>]+>", "", summary)) < 650
    assert " open" not in details.split(">", maxsplit=1)[0]
    assert escape(long_text) in details
    assert '<b data-strategy="inert">' not in section
    assert state.strategy == strategy
