from __future__ import annotations

from typing import TYPE_CHECKING

from PIL import Image

from logo_helper.models import ColorConstraints, PaletteContent, PaletteId, Session, Swatch
from logo_helper.prompts import PromptResult
from tests.test_app_icon_workflow import icon_brief
from tests.test_palette_workflow import add_palette

if TYPE_CHECKING:
    from tests.conftest import Harness


def test_icon_palette_explicit_parent_active_precedence(harness: Harness) -> None:
    _ = icon_brief(harness)
    harness.init()
    _ = add_palette(harness, "green", 0, "#247A52")
    _ = harness.import_image(1, "v1")
    _ = add_palette(harness, "navy", 2, "#173454")
    _ = harness.import_image(3, "v2", "--parent", "v1", "--palette", "navy")
    _ = add_palette(harness, "future", 4, "#FAFAFA")
    result = PromptResult.model_validate_json(
        harness.ok(
            "prompt",
            "--session",
            "demo",
            "--parent",
            "v2",
            "--changes",
            "Smile",
        )
    )
    state = Session.model_validate_json(harness.import_image(5, "v3", "--parent", "v2"))
    assert result.palette_id == "navy"
    assert result.palette_digest == state.palette(PaletteId("navy")).digest
    assert state.artifacts[-1].palette_id == result.palette_id
    assert state.artifacts[-1].app_icon == result.app_icon
    assert state.color_reports[-1].palette_id == "navy"


def test_icon_style_keeps_strict_color_export_gate(harness: Harness) -> None:
    _ = icon_brief(harness)
    harness.init()
    candidate = PaletteContent(
        swatches=(Swatch(hex="#FFFFFF", role="background"),),
        constraints=ColorConstraints(
            allowed_hex=("#FFFFFF",), locked_hex=("#FFFFFF",), max_colors=1
        ),
        source="assistant",
        selected_by="user",
        rationale="Strict white fixture",
    )
    path = harness.brief.with_name("strict.json")
    _ = path.write_text(candidate.model_dump_json(), encoding="utf-8")
    _ = harness.ok(
        "palette-add",
        "--session",
        "demo",
        "--palette",
        "white",
        "--revision",
        "0",
        "--palette-file",
        str(path),
    )
    prompt = PromptResult.model_validate_json(harness.ok("prompt", "--session", "demo"))
    assert '"max_colors":1' in prompt.prompt
    assert '"locked_hex":["#FFFFFF"]' in prompt.prompt
    assert "warm yellow" not in prompt.prompt
    with Image.new("RGB", (40, 40), (240, 0, 0)) as image:
        image.save(harness.png)
    state = Session.model_validate_json(harness.import_image(1))
    assert state.color_reports[-1].status != "pass"
    _ = harness.ok("select", "--session", "demo", "--artifact", "v1", "--revision", "2")
    _ = harness.ok(
        "review",
        "--session",
        "demo",
        "--artifact",
        "v1",
        "--revision",
        "3",
        "--review-file",
        str(harness.review),
    )
    before = harness.state_path.read_bytes()
    result = harness.run("export", "--session", "demo", "--revision", "4")
    assert result.returncode != 0
    assert "color_mismatch" in result.stderr
    assert "Required color #FFFFFF" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output/logo-generator/demo").exists()
