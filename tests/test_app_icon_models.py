from __future__ import annotations

import json
from typing import Final

import pytest
from pydantic import JsonValue, TypeAdapter, ValidationError

from logo_helper.app_icon_models import AppIconIntent
from logo_helper.app_icon_presets import APP_ICON_PRESETS
from logo_helper.models import Brief, ProjectError

PRESETS: Final = ("ip_mascot", "pictogram", "abstract", "monogram", "soft_3d", "pixel_art")


@pytest.mark.parametrize("preset", PRESETS)
@pytest.mark.parametrize("placement", ["center", "lower_left", "lower_right"])
def test_every_preset_accepts_all_explicit_placements(preset: str, placement: str) -> None:
    raw = json.dumps(
        {
            "preset": preset,
            "subject": "owl",
            "placement": placement,
            "text": "한e\u0301" if preset == "monogram" else None,
        }
    )
    icon = AppIconIntent.model_validate_json(raw)
    assert icon.preset == preset
    assert icon.placement == placement
    assert AppIconIntent.model_validate_json(icon.model_dump_json()) == icon
    with pytest.raises(ValidationError, match="frozen"):
        icon.subject = "changed"


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("preset", "unknown"),
        ("subject", ""),
        ("subject", " \t\n"),
        ("subject", "x" * 501),
        ("subject", None),
        ("subject", 42),
        ("placement", None),
        ("placement", "top"),
        ("extra", True),
        ("text", "A"),
    ],
)
def test_invalid_icon_shape(field: str, value: JsonValue) -> None:
    raw: dict[str, JsonValue] = {"preset": "ip_mascot", "subject": "owl", "placement": "center"}
    raw[field] = value
    with pytest.raises((ValidationError, ProjectError)):
        _ = AppIconIntent.model_validate_json(json.dumps(raw))


def test_placement_is_required_and_defaults_live_in_discovery() -> None:
    with pytest.raises(ValidationError, match="placement"):
        _ = AppIconIntent.model_validate_json('{"preset":"ip_mascot","subject":"owl"}')
    assert tuple(item.id for item in APP_ICON_PRESETS) == PRESETS
    assert APP_ICON_PRESETS[0].default_placement == "lower_left"
    assert all(item.default_placement == "center" for item in APP_ICON_PRESETS[1:])


@pytest.mark.parametrize("text", [None, "", "123456789", "A B", "A\n", "\x00", "\u200b"])
def test_monogram_rejects_missing_long_whitespace_or_control_text(text: str | None) -> None:
    with pytest.raises((ValidationError, ProjectError)):
        _ = AppIconIntent.model_validate_json(
            json.dumps(
                {"preset": "monogram", "subject": "notes", "placement": "center", "text": text}
            )
        )


@pytest.mark.parametrize("text", ["한글", "e\u0301", "文字", "12345678", "$(x);`a`"])
def test_unicode_monogram_is_preserved_exactly(text: str) -> None:
    icon = AppIconIntent(preset="monogram", subject="notes", placement="lower_right", text=text)
    assert icon.text == text


@pytest.mark.parametrize(
    "changes",
    [
        '{"background":"transparent"}',
        '{"slogan":"tagline"}',
        '{"exact_text":"brand"}',
        '{"lockup":{"layout":"horizontal","typography_style":"round"}}',
    ],
)
def test_icon_brief_conflicts_at_json_boundary(changes: str) -> None:
    icon = AppIconIntent(preset="pictogram", subject="cloud", placement="center")
    brief = Brief(
        brand_name="weather", exact_text="", industry="weather", audience="everyone", app_icon=icon
    )
    raw = brief.model_dump(mode="json") | TypeAdapter(dict[str, JsonValue]).validate_json(changes)
    with pytest.raises(ProjectError, match="intent_conflict"):
        _ = Brief.model_validate_json(json.dumps(raw))


def test_monogram_brief_exact_text_must_match() -> None:
    icon = AppIconIntent(preset="monogram", subject="notes", placement="center", text="한글")
    with pytest.raises(ProjectError, match="intent_conflict"):
        _ = Brief(
            brand_name="브랜드", exact_text="", industry="notes", audience="everyone", app_icon=icon
        )
