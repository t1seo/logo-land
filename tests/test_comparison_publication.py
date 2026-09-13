from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest

from logo_helper import comparison_gallery
from logo_helper.comparison_gallery import render_comparison_gallery
from logo_helper.comparison_models import ComparisonManifest, ComparisonSelection
from logo_helper.models import ProjectError, SessionId
from logo_helper.storage import Store, read_source, write_new
from tests.test_comparison_support import prepare_sources, source_bytes

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


@pytest.mark.parametrize("target", ["001.png", "001.txt", "manifest.json", "index.html"])
def test_cancel_repeat_then_retry_removes_partial_publication(
    harness: Harness, monkeypatch: pytest.MonkeyPatch, target: str
) -> None:
    # Given: cancellation at each publication phase, twice in succession.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    before = source_bytes(harness.workspace)
    store = Store.at(harness.workspace)
    link = os.link

    def interrupt(source: Path, destination: Path) -> None:
        if destination.name == target:
            assert not (harness.workspace / "gallery/index.html").exists()
            raise KeyboardInterrupt
        link(source, destination)

    # When: both cancelled attempts unwind, then a real retry completes.
    with monkeypatch.context() as patch:
        patch.setattr(os, "link", interrupt)
        for _ in range(2):
            with pytest.raises(KeyboardInterrupt):
                _ = render_comparison_gallery(store, selection, "gallery")
            assert not (harness.workspace / "gallery").exists()
            assert not list(harness.workspace.glob(".comparison-gallery-*"))
    result = render_comparison_gallery(store, selection, "gallery")
    # Then: only the complete retry is visible and the sources never changed.
    folder = harness.workspace / result.path
    manifest = ComparisonManifest.model_validate_json((folder / "manifest.json").read_bytes())
    assert len(manifest.artifacts) == 2
    assert (folder / "index.html").is_file()
    assert source_bytes(harness.workspace) == before


def test_foreign_replacement_survives_when_publication_is_cancelled(
    harness: Harness, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given: another owner replaces an already-published image inode.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    link = os.link
    foreign = harness.workspace / "replacement"
    _ = foreign.write_bytes(b"foreign owner")

    def replace_then_interrupt(source: Path, destination: Path) -> None:
        if destination.name == "002.png":
            _ = foreign.replace(destination.with_name("001.png"))
            raise KeyboardInterrupt
        link(source, destination)

    monkeypatch.setattr(os, "link", replace_then_interrupt)
    # When: cancellation triggers inode-aware rollback.
    with pytest.raises(KeyboardInterrupt):
        _ = render_comparison_gallery(Store.at(harness.workspace), selection, "gallery")
    # Then: foreign bytes survive, while no completion index/manifest can mislead users.
    folder = harness.workspace / "gallery"
    assert (folder / "images/001.png").read_bytes() == b"foreign owner"
    assert not (folder / "index.html").exists()
    assert not (folder / "manifest.json").exists()
    assert not list(harness.workspace.glob(".comparison-gallery-*"))


def test_revision_advance_during_staging_fails_before_publish(
    harness: Harness, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given: a concurrent writer advances a selected session after the initial read.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    store = Store.at(harness.workspace)
    state = store.load(SessionId("brand"))
    write = write_new

    def advance(path: Path, data: bytes) -> None:
        write(path, data)
        if path.name == "index.html":
            store.save(state.model_copy(update={"revision": 2}))

    monkeypatch.setattr(comparison_gallery, "write_new", advance)
    # When: staging completes and the revision is rechecked.
    with pytest.raises(ProjectError, match="stale_revision"):
        _ = render_comparison_gallery(store, selection, "gallery")
    # Then: the obsolete snapshot is not published or used to overwrite the writer.
    assert store.load(state.id).revision == 2
    assert not (harness.workspace / "gallery").exists()
    assert not list(harness.workspace.glob(".comparison-gallery-*"))


def test_source_tampering_during_copy_fails_without_publication(
    harness: Harness, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given: verified source bytes are replaced between loading and copying.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    read = read_source

    def tamper(path: Path) -> bytes:
        _ = path.write_bytes(b"changed after load")
        return read(path)

    monkeypatch.setattr(comparison_gallery, "read_source", tamper)
    # When/Then: copying detects the mismatch and removes staging.
    with pytest.raises(ProjectError, match="hash_mismatch"):
        _ = render_comparison_gallery(Store.at(harness.workspace), selection, "gallery")
    assert not (harness.workspace / "gallery").exists()
    assert not list(harness.workspace.glob(".comparison-gallery-*"))


def test_rerun_is_deterministic_and_existing_destination_is_never_overwritten(
    harness: Harness,
) -> None:
    # Given: a stable selection and two separate output destinations.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    store = Store.at(harness.workspace)
    # When: repeated renders publish the same saved snapshot.
    for destination in ("first", "second"):
        _ = render_comparison_gallery(store, selection, destination)
    # Then: every output byte is deterministic, and a dirty destination fails.
    first = harness.workspace / "first"
    for file in first.rglob("*"):
        if file.is_file():
            assert (
                file.read_bytes()
                == (harness.workspace / "second" / file.relative_to(first)).read_bytes()
            )
    with pytest.raises(ProjectError, match="conflict"):
        _ = render_comparison_gallery(store, selection, "first")
