from __future__ import annotations

import errno
import os
import re
from base64 import b64decode
from typing import TYPE_CHECKING

import pytest
from logopia_studio.gallery import publish_gallery
from logopia_studio.models import FeedbackEnvelope, StudioError
from pydantic import TypeAdapter
from tests.hermes.test_gallery_fixture import make_workflow

if TYPE_CHECKING:
    from pathlib import Path


def test_failed_write_rolls_back_only_its_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given: an empty publication and a filesystem failure after partial progress.
    state = make_workflow(tmp_path)
    output = tmp_path / "publication"
    calls: list[int] = []

    def fail_second_sync(descriptor: int) -> None:
        calls.append(descriptor)
        if len(calls) == 2:
            _ = (output / "foreign-note.txt").write_text("concurrent foreign draft")
            raise OSError(errno.ENOSPC, "simulated disk full")

    monkeypatch.setattr(os, "fsync", fail_second_sync)
    # When: the publisher encounters the bounded injected write failure.
    with pytest.raises(StudioError, match="gallery_output"):
        _ = publish_gallery(tmp_path, state, output)
    # Then: only foreign data remains, and the canonical sources survive.
    assert list(output.iterdir()) == [output / "foreign-note.txt"]
    assert (output / "foreign-note.txt").read_text() == "concurrent foreign draft"
    assert all((tmp_path / item.image_path).is_file() for item in state.candidates)


def test_stale_review_view_is_not_displayed_as_matching_review(tmp_path: Path) -> None:
    # Given: a valid original whose report points to a different target view.
    state = make_workflow(tmp_path)
    candidate = state.candidates[1]
    stale = candidate.critiques[0].model_copy(update={"view_sha256": "0" * 64})
    candidate = candidate.model_copy(update={"critiques": (stale, candidate.critiques[1])})
    state = state.model_copy(
        update={"candidates": (state.candidates[0], candidate, *state.candidates[2:])}
    )
    # When: the snapshot is published.
    index = publish_gallery(tmp_path, state, tmp_path / "publication")
    # Then: the mismatching evidence remains visible without a matching-review label.
    assert "검토 조건 불일치" in index.read_text()


def test_published_metadata_uses_core_feedback_envelope(tmp_path: Path) -> None:
    # Given: a published snapshot.
    state = make_workflow(tmp_path)
    index = publish_gallery(tmp_path, state, tmp_path / "publication")
    # When: each saved target is read through the core boundary.
    html = index.read_text()
    raw = html.split('<script type="application/json" id="gallery-data">')[1].split("</script>")[0]
    envelopes = TypeAdapter(tuple[FeedbackEnvelope, ...]).validate_json(
        raw.split('"candidates":')[1][:-1]
    )
    for envelope in envelopes:
        # Then: identity, revision and exact candidate digest are core-valid.
        assert envelope.workflow_id == state.id
        assert envelope.expected_revision == state.revision
        assert envelope.candidate_sha256 == next(
            candidate.sha256
            for candidate in state.candidates
            if candidate.id == envelope.candidate_id
        )


def test_offline_download_carries_exact_original_bytes(tmp_path: Path) -> None:
    # Given: Chrome opens file links instead of honoring their download attribute.
    state = make_workflow(tmp_path)
    # When: a publication is prepared for offline downloading.
    index = publish_gallery(tmp_path, state, tmp_path / "publication")
    pattern = r'<a href="data:image/png;base64,([^"]+)" download="candidate-2.png"'
    match = re.search(pattern, index.read_text())
    # Then: the download carries exact bytes alongside a direct original link.
    assert match is not None
    assert b64decode(match[1]) == (tmp_path / state.candidates[1].image_path).read_bytes()
    assert 'href="originals/candidate-2.png"' in index.read_text()


def test_workspace_alias_preserves_matching_review_status(tmp_path: Path) -> None:
    # Given: an explicit workspace alias like macOS /tmp pointing at real originals.
    workspace = tmp_path / "workspace"
    state = make_workflow(workspace)
    alias = tmp_path / "alias"
    alias.symlink_to(workspace, target_is_directory=True)
    # When: the caller publishes through that alias.
    index = publish_gallery(alias, state, tmp_path / "publication")
    # Then: valid evidence is not mislabeled as a stale report.
    assert "검토됨 · 192px 조건 통과" in index.read_text()
