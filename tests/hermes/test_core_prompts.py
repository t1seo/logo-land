from pathlib import Path

from logopia_studio.prompts import image_prompt
from tests.hermes.test_core_fixtures import FixtureHost, brief


def test_brand_white_presentation_is_preserved(tmp_path: Path) -> None:
    # Given the existing brand prompt policy.
    request = brief()
    direction = FixtureHost(tmp_path).plan(request).directions[0]
    # When a brand prompt is assembled, then original art and white presentation remain explicit.
    prompt = image_prompt(request, direction)
    assert "Pure white solid background." in prompt
    assert "Original logo artwork" in prompt
    assert direction.prompt in prompt


def test_ip_preserves_character_and_chosen_single_background(tmp_path: Path) -> None:
    # Given an IP direction with its own purposeful solid background.
    request = brief().model_copy(update={"mode": "ip", "count": None})
    direction = (
        FixtureHost(tmp_path)
        .plan(request)
        .directions[0]
        .model_copy(update={"prompt": "Blue creature portrait on a yellow solid background."})
    )
    # When an IP prompt is assembled, then brand presentation cannot override the character intent.
    prompt = image_prompt(request, direction)
    assert "Pure white" not in prompt
    assert "Original logo artwork" not in prompt
    assert "opaque" not in prompt
    assert "lower corner" in prompt
    assert direction.prompt in prompt


def test_app_icon_preserves_chosen_filled_background(tmp_path: Path) -> None:
    # Given an app icon direction with a chosen navy filled square background.
    request = brief().model_copy(update={"mode": "app_icon"})
    direction = (
        FixtureHost(tmp_path)
        .plan(request)
        .directions[0]
        .model_copy(
            update={"prompt": "Centered cream pictogram on a navy filled square background."}
        )
    )
    # When assembled, then brand white cannot override the app icon's background intent.
    prompt = image_prompt(request, direction)
    assert "Pure white" not in prompt
    assert "Centered simple pictogram" in prompt
    assert "no lettering" in prompt
    assert direction.prompt in prompt
