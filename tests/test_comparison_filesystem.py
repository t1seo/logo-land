from __future__ import annotations

import json
from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from logo_helper.comparison_gallery import render_comparison_gallery
from logo_helper.comparison_models import ComparisonSelection
from logo_helper.models import ProjectError
from logo_helper.storage import Store
from tests.test_comparison_support import prepare_sources, source_bytes

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


@pytest.mark.parametrize(
    "output",
    ["", ".", "../escape", "/escape", "a/../escape", "a\\b", "C:x", ".git/x", ".LoGo-GeNeRaToR/x"],
)
def test_unsafe_output_fails_when_path_escapes_or_uses_reserved_storage(
    harness: Harness, output: str
) -> None:
    # Given: valid sources and an unsafe output path.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    before = source_bytes(harness.workspace)
    # When/Then: publication fails without writing source state.
    with pytest.raises(ProjectError, match=r"unsafe_path|reserved_output"):
        _ = render_comparison_gallery(Store.at(harness.workspace), selection, output)
    assert source_bytes(harness.workspace) == before


@pytest.mark.parametrize(
    "case",
    [
        "dirty",
        "symlink",
        "parent_symlink",
        "missing",
        "tampered",
        "source_symlink",
        "state_symlink",
        "facts",
        "unsupported",
    ],
)
def test_invalid_files_leave_no_partial_gallery(
    harness: Harness,
    tmp_path: Path,
    case: Literal[
        "dirty",
        "symlink",
        "parent_symlink",
        "missing",
        "tampered",
        "source_symlink",
        "state_symlink",
        "facts",
        "unsupported",
    ],
) -> None:
    # Given: an existing destination or a damaged/missing/unsupported source.
    selection = ComparisonSelection.model_validate_json(prepare_sources(harness).read_bytes())
    output = harness.workspace / "gallery"
    source = harness.workspace / ".logo-generator/sessions/brand/artifacts/v1.png"
    state = source.parent.parent / "session.json"
    match case:
        case "dirty":
            output.mkdir()
            _ = (output / "foreign").write_bytes(b"keep")
        case "symlink" | "parent_symlink":
            output.symlink_to(tmp_path, target_is_directory=True)
        case "missing":
            source.unlink()
        case "tampered":
            _ = source.write_bytes(b"tampered")
        case "unsupported":
            _ = source.write_bytes(b"<svg xmlns='http://www.w3.org/2000/svg'/>")
        case "source_symlink":
            source.unlink()
            source.symlink_to(harness.png)
        case "state_symlink":
            snapshot = tmp_path / "state.json"
            _ = snapshot.write_bytes(state.read_bytes())
            state.unlink()
            state.symlink_to(snapshot)
        case "facts":
            _ = state.write_text(state.read_text().replace('"width": 120', '"width": 119'))
        case _:
            assert_never(case)
    before = source_bytes(harness.workspace)
    # When: comparison attempts to read and publish the selected sources.
    with pytest.raises(
        ProjectError, match=r"conflict|unsafe_path|invalid_file|hash_mismatch|invalid_state"
    ):
        _ = render_comparison_gallery(
            Store.at(harness.workspace),
            selection,
            "gallery/nested" if case == "parent_symlink" else "gallery",
        )
    # Then: no index or staging directory survives and unrelated data is preserved.
    assert not (output / "index.html").exists()
    assert not list(harness.workspace.glob(".comparison-gallery-*"))
    assert source_bytes(harness.workspace) == before
    if case == "dirty":
        assert (output / "foreign").read_bytes() == b"keep"
    assert output.exists() == (case in {"dirty", "symlink", "parent_symlink"})


@pytest.mark.parametrize(
    ("session", "artifact", "revision", "code"),
    [
        ("brand", "v1", 0, "stale_revision"),
        ("brand", "missing", 1, "not_found"),
        ("missing", "v1", 1, "invalid_file"),
    ],
)
def test_unresolvable_identity_fails_before_publication(
    harness: Harness, session: str, artifact: str, revision: int, code: str
) -> None:
    # Given: a stale or missing explicit source identity.
    _ = prepare_sources(harness)
    selection = ComparisonSelection.model_validate_json(
        json.dumps(
            {
                "title": "x",
                "items": [{"session": session, "artifact": artifact, "revision": revision}],
            }
        )
    )
    # When/Then: the source cannot be silently replaced by a same-ID candidate.
    with pytest.raises(ProjectError, match=code):
        _ = render_comparison_gallery(Store.at(harness.workspace), selection, "gallery")
    assert not (harness.workspace / "gallery").exists()
