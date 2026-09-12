from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import pytest

from logo_helper.delivery import Manifest
from logo_helper.models import Background, Session
from logo_helper.prompts import PromptResult
from tests.test_background_variants import prepare_parent, select_and_review, set_fixture_background

if TYPE_CHECKING:
    from tests.conftest import Harness


@pytest.mark.parametrize("initial", ["opaque", "transparent"])
@pytest.mark.parametrize("stored_field", ["missing", "null"])
def test_legacy_session_when_background_intent_is_missing_or_null(
    harness: Harness, initial: Background, stored_field: Literal["missing", "null"]
) -> None:
    # Given a reviewed original stored in the old schema or with an unset background intent.
    prepare_parent(harness, initial)
    select_and_review(harness, "v1", 1)
    state = Session.model_validate_json(harness.state_path.read_bytes())
    legacy_json = state.model_dump_json(
        exclude={"artifacts": {"__all__": {"requested_background"}}}
    )
    if stored_field == "null":
        legacy_json = legacy_json.replace(
            '"parent_id":', '"requested_background":null,"parent_id":'
        )
    _ = harness.state_path.write_text(legacy_json, encoding="utf-8")
    before = harness.state_path.read_bytes()
    # When a fresh CLI resumes, builds a child prompt, and exports the legacy selection.
    resumed = Session.model_validate_json(harness.ok("show", "--session", "demo"))
    prompt = PromptResult.model_validate_json(
        harness.ok("prompt", "--session", "demo", "--parent", "v1", "--changes", "Use navy")
    )
    assert harness.state_path.read_bytes() == before
    _ = harness.ok("export", "--session", "demo", "--revision", "3")
    # Then the original brief remains the fallback while no per-artifact request is fabricated.
    output = harness.workspace / "output/logo-generator/demo"
    manifest = Manifest.model_validate_json((output / "manifest.json").read_bytes())
    assert resumed.artifacts[0].requested_background is None
    assert prompt.parent_requested_background == initial
    assert manifest.source.requested_background is None
    assert manifest.requested_background == initial
    assert manifest.brief.background == initial
    assert (output / "logo.png").read_bytes() == harness.png.read_bytes()


@pytest.mark.parametrize(
    ("initial", "requested"), [("opaque", "transparent"), ("transparent", "opaque")]
)
def test_import_defaults_to_original_brief_when_parent_requested_another_background(
    harness: Harness, initial: Background, requested: Background
) -> None:
    # Given a parent with an explicit background different from the original brief.
    prepare_parent(harness, initial)
    set_fixture_background(harness, requested)
    _ = harness.import_image(1, "v2", "--parent", "v1", "--background", requested)
    # When a later child is imported without --background.
    result = Session.model_validate_json(harness.import_image(2, "v3", "--parent", "v2"))
    # Then intent defaults to the original brief rather than inferring from pixels or the parent.
    assert result.artifacts[-1].requested_background == initial
    assert result.artifacts[-1].image.has_transparency == (requested == "transparent")


def test_import_rejects_when_background_option_is_invalid(harness: Harness) -> None:
    # Given an existing session with an unchanged revision and artifact set.
    prepare_parent(harness, "opaque")
    before = harness.state_path.read_bytes()
    # When the CLI receives an unsupported background value.
    result = harness.run(
        "import",
        "--session",
        "demo",
        "--artifact",
        "v2",
        "--image",
        str(harness.png),
        "--prompt-file",
        str(harness.prompt),
        "--revision",
        "1",
        "--background",
        "auto",
    )
    # Then argument parsing rejects it before any state or image is written.
    assert result.returncode == 2
    assert "opaque" in result.stderr
    assert "transparent" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.state_path.parent / "artifacts/v2.png").exists()


@pytest.mark.parametrize("stored_background", ['"auto"', "false"])
def test_resume_rejects_when_requested_background_state_is_invalid(
    harness: Harness, stored_background: str
) -> None:
    # Given a valid state whose per-artifact background field was externally corrupted.
    prepare_parent(harness, "opaque")
    state = harness.state_path.read_text(encoding="utf-8")
    corrupted = state.replace(
        '"requested_background": "opaque"', f'"requested_background": {stored_background}'
    )
    assert corrupted != state
    _ = harness.state_path.write_text(corrupted, encoding="utf-8")
    # When a new process loads the corrupted state.
    result = harness.run("show", "--session", "demo")
    # Then the typed boundary rejects invalid intent without rewriting the evidence.
    assert result.returncode == 1
    assert "requested_background" in result.stderr
    assert harness.state_path.read_text(encoding="utf-8") == corrupted
