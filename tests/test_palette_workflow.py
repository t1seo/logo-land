from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from logo_helper.models import LockupIntent, PaletteContent, PaletteId, Session, Swatch
from logo_helper.prompts import PromptResult

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


def palette_file(harness: Harness, color: str = "#247A52") -> Path:
    candidate = PaletteContent(
        swatches=(Swatch(hex=color, role="primary"),),
        source="assistant",
        selected_by="assistant",
        rationale="Fixture intent",
    )
    path = harness.workspace / "palette.json"
    _ = path.write_text(candidate.model_dump_json(), encoding="utf-8")
    return path


def add_palette(harness: Harness, identifier: str, revision: int, color: str) -> Session:
    return Session.model_validate_json(
        harness.ok(
            "palette-add",
            "--session",
            "demo",
            "--palette",
            identifier,
            "--palette-file",
            str(palette_file(harness, color)),
            "--revision",
            str(revision),
        )
    )


def test_palette_propose_when_read_only(harness: Harness) -> None:
    # Given normalized seed/lock input and untouched state.
    harness.init()
    request = harness.workspace / "request.json"
    _ = request.write_text('{"seed_hex":"#247a52","constraints":{"locked_hex":["#247a52"]}}')
    before = harness.state_path.read_bytes()
    # When requesting candidates through the real CLI.
    result = harness.run("palette-propose", "--session", "demo", "--request-file", str(request))
    # Then actual normalized candidates are returned without mutation.
    assert result.returncode == 0, result.stderr
    assert '"#247A52"' in result.stdout
    assert '"revision": 0' in result.stdout
    assert harness.state_path.read_bytes() == before


def test_palette_when_parent_differs_from_active(harness: Harness) -> None:
    # Given green parent, navy child and a newer active green palette.
    harness.init()
    _ = add_palette(harness, "green", 0, "#247A52")
    _ = harness.import_image(1, "v1")
    _ = add_palette(harness, "navy", 2, "#173454")
    _ = harness.import_image(3, "v2", "--parent", "v1", "--palette", "navy")
    _ = add_palette(harness, "future-green", 4, "#247A52")
    # When making a geometry-only edit without overriding palette.
    prompt = PromptResult.model_validate_json(
        harness.ok(
            "prompt",
            "--session",
            "demo",
            "--parent",
            "v2",
            "--changes",
            "Round the corners",
        )
    )
    state = Session.model_validate_json(
        harness.import_image(prompt.revision, "v3", "--parent", "v2")
    )
    # Then both prompt and image preserve navy rather than active future intent.
    assert prompt.palette_id == PaletteId("navy")
    assert prompt.palette_digest == state.palette(PaletteId("navy")).digest
    assert [item.palette_id for item in state.artifacts] == ["green", "navy", "navy"]
    assert len(state.color_reports) == 3


@pytest.mark.parametrize("extra", [("--palette", "missing"), ("--revision", "99")])
def test_import_when_palette_or_revision_is_invalid(
    harness: Harness, extra: tuple[str, str]
) -> None:
    # Given valid intent and a pristine artifacts directory.
    harness.init()
    _ = add_palette(harness, "green", 0, "#247A52")
    before = harness.state_path.read_bytes()
    # When import references an unavailable palette or stale revision.
    result = harness.run(
        "import",
        "--session",
        "demo",
        "--artifact",
        "invalid",
        "--image",
        str(harness.png),
        "--prompt-file",
        str(harness.prompt),
        "--revision",
        "1",
        *extra,
    )
    # Then no orphan image or changed state remains.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
    assert not (harness.state_path.parent / "artifacts/invalid.png").exists()


def test_lockup_when_parent_has_explicit_override(harness: Harness) -> None:
    # Given an explicit symbol/text lockup on a parent.
    harness.init()
    lockup = harness.workspace / "lockup.json"
    _ = lockup.write_text(
        LockupIntent(
            layout="horizontal",
            symbol_position="end",
            text_alignment="center",
            typography_style="rounded Hangul sans",
            font_reference="Pretendard",
        ).model_dump_json()
    )
    _ = harness.import_image(0, "v1", "--lockup-file", str(lockup))
    # When making a geometry-only edit.
    result = harness.ok(
        "prompt", "--session", "demo", "--parent", "v1", "--changes", "Round corners"
    )
    state = Session.model_validate_json(harness.import_image(1, "v2", "--parent", "v1"))
    # Then the requested layout and visual font direction survive the edit.
    assert state.artifacts[1].lockup == state.artifacts[0].lockup
    assert state.artifacts[1].lockup is not None
    assert "Pretendard" in result
    assert "horizontal" in result
    assert "Morrow Studio" in result


def test_palette_add_when_duplicate(harness: Harness) -> None:
    # Given an immutable recorded palette.
    harness.init()
    _ = add_palette(harness, "green", 0, "#247A52")
    before = harness.state_path.read_bytes()
    # When that ID is reused with different content.
    result = harness.run(
        "palette-add",
        "--session",
        "demo",
        "--palette",
        "green",
        "--palette-file",
        str(palette_file(harness, "#173454")),
        "--revision",
        "1",
    )
    # Then the previous version is untouched.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
