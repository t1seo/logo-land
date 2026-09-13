from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from pydantic import JsonValue, ValidationError

from logo_helper.comparison_models import ComparisonSelection
from logo_helper.models import ProjectError
from tests.test_comparison_support import prepare_sources, source_bytes

if TYPE_CHECKING:
    from tests.conftest import Harness


@pytest.mark.parametrize(
    "raw",
    [
        "{",
        "[]",
        "null",
        "{}",
        '{"title":"x","items":[]}',
        '{"title":"x","items":[{"session":"a","artifact":"v1","revision":0}],"extra":1}',
        '{"title":"x","items":[{"session":"a","artifact":"v1","revision":0,"approved":true}]}',
        '{"title":"x","items":[{"session":"../a","artifact":"v1","revision":0}]}',
        '{"title":"x","items":[{"session":"a","artifact":"../v1","revision":0}]}',
        '{"title":"x","items":[{"session":"a","artifact":"v1","revision":true}]}',
        '{"title":"x","items":[{"session":"a","artifact":"v1","revision":"0"}]}',
        '{"title":"x","items":[{"session":"a","artifact":"v1","revision":-1}]}',
        '{"title":" ","items":[{"session":"a","artifact":"v1","revision":0}]}',
    ],
)
def test_invalid_json_fails_before_publication_when_contract_is_violated(
    harness: Harness, raw: str
) -> None:
    # Given: a valid workspace but an invalid selection document.
    selection = prepare_sources(harness)
    before = source_bytes(harness.workspace)
    _ = selection.write_text(raw)
    # When: the public CLI receives malformed, unsupported or coercible input.
    result = harness.run(
        "compare-gallery", "--selection-file", str(selection), "--output", "gallery"
    )
    # Then: failure cannot be mistaken for a partial success; source state is intact.
    assert result.returncode == 1
    assert '"error"' in result.stderr
    assert not (harness.workspace / "gallery").exists()
    assert source_bytes(harness.workspace) == before


@pytest.mark.parametrize("field", ["rationale", "preserve", "change", "observation", "title"])
def test_text_is_bounded_when_inputs_are_overlong(field: str) -> None:
    # Given: one excessively long decision field or title.
    item: dict[str, JsonValue] = {"session": "brand", "artifact": "v1", "revision": 1}
    payload: dict[str, JsonValue] = {"title": "Study", "items": [item]}
    if field == "title":
        payload[field] = "x" * 201
    else:
        item[field] = "x" * 2001
    # When/Then: boundary parsing rejects it before any filesystem work.
    with pytest.raises(ValidationError, match="string_too_long"):
        _ = ComparisonSelection.model_validate_json(json.dumps(payload))


@pytest.mark.parametrize("count", [0, 61])
def test_cardinality_is_bounded_when_candidate_count_is_outside_range(count: int) -> None:
    # Given: unique candidates outside the supported 1-60 range.
    items = [{"session": "a", "artifact": f"v{number}", "revision": 0} for number in range(count)]
    # When/Then: the parsed selection cannot represent empty or excessive input.
    with pytest.raises(ValidationError, match=r"too_short|too_long"):
        _ = ComparisonSelection.model_validate_json(json.dumps({"title": "x", "items": items}))


def test_duplicate_tuple_is_rejected_when_revision_differs() -> None:
    # Given: the same source appears twice with conflicting revisions.
    items = [{"session": "a", "artifact": "v1", "revision": revision} for revision in (1, 2)]
    # When/Then: revision is not a namespace escape for a repeated candidate.
    with pytest.raises(ProjectError, match="invalid_selection"):
        _ = ComparisonSelection.model_validate_json(json.dumps({"title": "x", "items": items}))


def test_large_input_fails_with_bounded_cli_timeout(harness: Harness) -> None:
    # Given: a file larger than the comparison-specific input budget.
    selection = harness.workspace / "huge.json"
    _ = selection.write_bytes(b" " * (4 * 1024 * 1024 + 1))
    # When: the CLI is invoked through Harness's 20-second timeout.
    result = harness.run(
        "compare-gallery", "--selection-file", str(selection), "--output", "gallery"
    )
    # Then: it fails explicitly before publishing, without claiming success.
    assert result.returncode == 1
    assert "4 MiB" in result.stderr
    assert not (harness.workspace / "gallery").exists()


def test_selection_symlink_is_rejected_before_publication(harness: Harness) -> None:
    # Given: a valid selection behind a symlink leaf.
    selection = prepare_sources(harness)
    linked = harness.workspace / "linked.json"
    linked.symlink_to(selection)
    # When: the CLI reads the untrusted selection path.
    result = harness.run("compare-gallery", "--selection-file", str(linked), "--output", "gallery")
    # Then: the path is rejected before reading session data or publishing output.
    assert result.returncode == 1
    assert "invalid_file" in result.stderr
    assert not (harness.workspace / "gallery").exists()
