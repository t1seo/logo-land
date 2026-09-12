from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from pydantic import TypeAdapter

from logo_helper.app_icon_presets import APP_ICON_PRESETS, AppIconPresetChoice
from logo_helper.color_gallery import GalleryResult
from logo_helper.models import Session
from logo_helper.prompts import PromptResult

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


def icon_file(harness: Harness, *, monogram: bool = False) -> Path:
    path = harness.brief.with_name("icon.json")
    _ = path.write_text(
        json.dumps(
            {
                "preset": "monogram" if monogram else "ip_mascot",
                "subject": "독서 안내 부엉이",
                "placement": "lower_left",
                "text": "한글" if monogram else None,
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return path


def icon_brief(harness: Harness, *, monogram: bool = False) -> Path:
    icon = icon_file(harness, monogram=monogram).read_text(encoding="utf-8")
    _ = harness.brief.write_text(
        (
            '{"brand_name":"historical brand","industry":"reading","audience":"readers",'
            f'"exact_text":{json.dumps("한글" if monogram else "")},'
            f'"background":"opaque","app_icon":{icon}}}'
        ),
        encoding="utf-8",
    )
    return harness.brief


def import_args(harness: Harness, *extra: str) -> tuple[str, ...]:
    return (
        "import",
        "--session",
        "demo",
        "--artifact",
        "v1",
        "--revision",
        "0",
        "--image",
        str(harness.png),
        "--prompt-file",
        str(harness.prompt),
        *extra,
    )


@pytest.mark.parametrize("monogram", [False, True])
def test_json_init_prompt_import_show_snapshots(harness: Harness, monogram: bool) -> None:
    _ = icon_brief(harness, monogram=monogram)
    harness.init()
    before = harness.state_path.read_bytes()
    result = PromptResult.model_validate_json(harness.ok("prompt", "--session", "demo"))
    assert result.app_icon is not None
    assert result.requested_background == "opaque"
    assert result.parent_requested_background is None
    assert harness.state_path.read_bytes() == before
    _ = harness.prompt.write_text(result.prompt, encoding="utf-8")
    original = harness.png.read_bytes()
    state = Session.model_validate_json(harness.import_image())
    artifact = state.artifacts[0]
    assert artifact.app_icon == result.app_icon == state.brief.app_icon
    assert artifact.prompt == result.prompt
    assert artifact.requested_background == "opaque"
    assert artifact.image.width == artifact.image.height == 16
    assert artifact.image.has_transparency
    assert harness.png.read_bytes() == original
    assert (harness.state_path.parent / artifact.path).read_bytes() == original
    assert Session.model_validate_json(harness.ok("show", "--session", "demo")) == state


def test_explicit_legacy_transform_and_child_inherit(harness: Harness) -> None:
    harness.init()
    path = icon_file(harness)
    prompt = PromptResult.model_validate_json(
        harness.ok("prompt", "--session", "demo", "--app-icon-file", str(path))
    )
    state = Session.model_validate_json(
        harness.ok(*import_args(harness, "--app-icon-file", str(path)))
    )
    assert state.brief.background == "transparent"
    assert state.brief.app_icon is None
    assert state.artifacts[0].app_icon == prompt.app_icon
    assert state.artifacts[0].requested_background == "opaque"
    child_prompt = PromptResult.model_validate_json(
        harness.ok("prompt", "--session", "demo", "--parent", "v1", "--changes", "Smile")
    )
    child = Session.model_validate_json(harness.import_image(1, "v2", "--parent", "v1"))
    assert child.artifacts[1].app_icon == child_prompt.app_icon == prompt.app_icon
    assert child.artifacts[1].requested_background == "opaque"
    assert child_prompt.parent_requested_background == "opaque"


@pytest.mark.parametrize(
    "raw",
    [
        "{",
        "null",
        "[]",
        '{"preset":"unknown"}',
        '{"preset":"ip_mascot","subject":"owl","placement":"center","extra":true}',
    ],
)
def test_invalid_icon_file_rejects_both_boundaries_without_mutation(
    harness: Harness, raw: str
) -> None:
    harness.init()
    path = icon_file(harness)
    _ = path.write_text(raw, encoding="utf-8")
    before = harness.state_path.read_bytes()
    for args in [("prompt", "--session", "demo"), import_args(harness)]:
        result = harness.run(*args, "--app-icon-file", str(path))
        assert result.returncode != 0
        assert harness.state_path.read_bytes() == before
        assert not (harness.state_path.parent / "artifacts/v1.png").exists()


def test_explicit_transparent_icon_import_conflicts(harness: Harness) -> None:
    harness.init()
    path = icon_file(harness)
    before = harness.state_path.read_bytes()
    result = harness.run(
        *import_args(harness, "--app-icon-file", str(path), "--background", "transparent")
    )
    assert result.returncode != 0
    assert "intent_conflict" in result.stderr
    assert harness.state_path.read_bytes() == before


def test_icon_and_explicit_lockup_conflict(harness: Harness) -> None:
    harness.init()
    path = icon_file(harness)
    lockup = path.with_name("lockup.json")
    _ = lockup.write_text('{"layout":"horizontal","typography_style":"rounded"}', encoding="utf-8")
    before = harness.state_path.read_bytes()
    for args in [("prompt", "--session", "demo"), import_args(harness)]:
        result = harness.run(*args, "--app-icon-file", str(path), "--lockup-file", str(lockup))
        assert result.returncode != 0
        assert "intent_conflict" in result.stderr
        assert harness.state_path.read_bytes() == before


def test_discovery_returns_six_typed_choices_without_session_writes(harness: Harness) -> None:
    choices = TypeAdapter(tuple[AppIconPresetChoice, ...]).validate_json(harness.ok("icon-presets"))
    assert choices == APP_ICON_PRESETS
    assert tuple(choice.id for choice in choices) == (
        "ip_mascot",
        "pictogram",
        "abstract",
        "monogram",
        "soft_3d",
        "pixel_art",
    )
    assert not (harness.workspace / ".logo-generator").exists()


def test_icon_gallery_cli_publishes_unreviewed_original_without_state_mutation(
    harness: Harness,
) -> None:
    _ = icon_brief(harness)
    harness.init()
    _ = harness.import_image()
    before = harness.state_path.read_bytes()
    result = TypeAdapter(GalleryResult).validate_json(
        harness.ok(
            "icon-gallery",
            "--session",
            "demo",
            "--artifacts",
            "v1",
            "--output",
            "icon-comparison",
        )
    )
    assert result.artifact_ids == ("v1",)
    assert (harness.workspace / result.index_path).is_file()
    assert harness.state_path.read_bytes() == before


def test_oversized_icon_import_has_no_mutation(harness: Harness) -> None:
    _ = icon_brief(harness)
    harness.init()
    before = harness.state_path.read_bytes()
    _ = harness.prompt.write_text("x" * 20001, encoding="utf-8")
    result = harness.run(*import_args(harness))
    assert result.returncode != 0
    assert "20000" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.state_path.parent / "artifacts/v1.png").exists()
