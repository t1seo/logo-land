from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from logo_helper.models import Session
from logo_helper.prompts import PromptResult

if TYPE_CHECKING:
    from tests.conftest import Harness

FIXTURES = Path(__file__).resolve().parents[1] / "docs/qa/app-icons/core-fixtures"


def install_baseline(harness: Harness, version: int) -> bytes:
    directory = harness.state_path.parent
    (directory / "artifacts").mkdir(parents=True)
    _ = (directory / "artifacts/v1.png").write_bytes(
        (FIXTURES / "synthetic-baseline.png").read_bytes()
    )
    original = (FIXTURES / f"session-v{version}.json").read_bytes()
    _ = harness.state_path.write_bytes(original)
    return original


@pytest.mark.parametrize("version", [1, 2])
def test_real_pre_icon_reads_and_first_mutation(harness: Harness, version: int) -> None:
    before = install_baseline(harness, version)
    for args in [("show", "--session", "demo"), ("list",), ("prompt", "--session", "demo")]:
        _ = harness.ok(*args)
        assert harness.state_path.read_bytes() == before
    result = Session.model_validate_json(
        harness.ok("select", "--session", "demo", "--artifact", "v1", "--revision", "1")
    )
    assert result.schema_version == 2
    assert result.revision == 2
    assert result.brief.exact_text == "Legacy Ω"
    assert result.artifacts[0].prompt == "Baseline original prompt; synthetic evidence."
    backup = harness.state_path.with_name("session.v1.backup.json")
    if version == 1:
        assert backup.read_bytes() == before
    else:
        assert not backup.exists()


@pytest.mark.parametrize("mode", ["generation", "edit"])
def test_pre_icon_prompt_preserves_intent_and_saved_history(harness: Harness, mode: str) -> None:
    before = install_baseline(harness, 2)
    state = Session.model_validate_json(harness.ok("show", "--session", "demo"))
    original_image = (harness.state_path.parent / state.artifacts[0].path).read_bytes()
    extra = ("--parent", "v1", "--changes", "Use navy blue") if mode == "edit" else ()
    prompt = PromptResult.model_validate_json(harness.ok("prompt", "--session", "demo", *extra))
    # New construction guidance may evolve; historical bytes and effective intent cannot.
    assert prompt.mode == mode
    assert prompt.revision == state.revision
    assert repr(state.brief.exact_text) in prompt.prompt
    assert repr(state.brief.slogan) in prompt.prompt
    assert prompt.palette_id is None
    assert prompt.app_icon is None
    if mode == "edit":
        assert prompt.parent_id == "v1"
        assert prompt.lockup is None
        assert "Use navy blue" in prompt.prompt
        assert "Create one" not in prompt.prompt
    else:
        assert prompt.parent_id is None
        assert prompt.lockup == state.brief.lockup
    assert harness.state_path.read_bytes() == before
    assert (harness.state_path.parent / state.artifacts[0].path).read_bytes() == original_image


def test_legacy_import_keeps_unknown_lockup_and_original_prompt(harness: Harness) -> None:
    _ = install_baseline(harness, 2)
    state = Session.model_validate_json(harness.import_image(1, "v2", "--parent", "v1"))
    assert state.artifacts[0].requested_background == "opaque"
    assert state.artifacts[1].requested_background == "transparent"
    assert state.artifacts[1].prompt == harness.prompt.read_text(encoding="utf-8")
    assert state.brief.lockup is not None
    assert state.artifacts[0].lockup is None
    assert state.artifacts[1].lockup is None


def test_legacy_stale_command_leaves_exact_state(harness: Harness) -> None:
    before = install_baseline(harness, 1)
    result = harness.run("select", "--session", "demo", "--artifact", "v1", "--revision", "0")
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
    assert not harness.state_path.with_name("session.v1.backup.json").exists()
