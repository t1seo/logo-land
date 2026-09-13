from __future__ import annotations

from hashlib import sha256
from typing import TYPE_CHECKING

from logo_helper.comparison_models import ComparisonItem, ComparisonManifest, ComparisonSelection
from logo_helper.models import ArtifactId, SessionId
from logo_helper.storage import Store
from tests.test_comparison_support import prepare_sources, source_bytes

if TYPE_CHECKING:
    from tests.conftest import Harness


def test_sixty_candidates_and_maximum_notes_finish_under_cli_timeout(harness: Harness) -> None:
    # Given: 60 real PNG artifacts with maximal allowed title and decision lengths.
    _ = prepare_sources(harness)
    store = Store.at(harness.workspace)
    state = store.load(SessionId("brand"))
    first = state.artifacts[0]
    folder = store.session_dir(state.id)
    data = (folder / first.path).read_bytes()
    artifacts = tuple(
        first.model_copy(
            update={"id": ArtifactId(f"v{number}"), "path": f"artifacts/v{number}.png"}
        )
        for number in range(1, 61)
    )
    for artifact in artifacts[1:]:
        _ = (folder / artifact.path).write_bytes(data)
    store.save(state.model_copy(update={"artifacts": artifacts, "revision": 60}))
    notes = '한<&"\n' * 400
    selection = ComparisonSelection(
        title="한" * 200,
        items=tuple(
            ComparisonItem(
                session=state.id,
                artifact=artifact.id,
                revision=60,
                rationale=notes,
                preserve=notes,
                change=notes,
                observation=notes,
            )
            for artifact in artifacts
        ),
    )
    selection_file = harness.workspace / "selection.json"
    _ = selection_file.write_text(selection.model_dump_json())
    before = source_bytes(harness.workspace)
    # When: the actual CLI runs with its existing 20-second subprocess timeout.
    result = harness.run(
        "compare-gallery", "--selection-file", str(selection_file), "--output", "gallery"
    )
    # Then: every explicit source is present with exact PNG/prompt bytes and notes.
    assert result.returncode == 0, result.stderr
    output = harness.workspace / "gallery"
    manifest = ComparisonManifest.model_validate_json((output / "manifest.json").read_bytes())
    assert len(manifest.artifacts) == 60
    for item in manifest.artifacts:
        assert (output / item.image_file).read_bytes() == data
        assert sha256((output / item.prompt_file).read_bytes()).hexdigest() == item.prompt_sha256
        assert item.source.observation == notes
    assert source_bytes(harness.workspace) == before
