from __future__ import annotations

from typing import TYPE_CHECKING

from logo_helper.color_analysis import analyze_png
from logo_helper.color_models import PaletteContent, PaletteVersion, Swatch, palette_digest
from logo_helper.delivery import Manifest, guide
from logo_helper.lockup_models import LockupIntent
from logo_helper.models import ArtifactId, PaletteId, ReportId, SessionId
from logo_helper.reference_models import RegionOfInterest
from logo_helper.storage import Store
from tests.test_color_reports import prepare_color

if TYPE_CHECKING:
    from tests.conftest import Harness


def test_guide_records_selected_edit_request_when_palette_has_changed(harness: Harness) -> None:
    # Given the original green brief and a selected navy revision.
    harness.init()
    _ = harness.import_image()
    _ = harness.prompt.write_text("Change green to navy and preserve exact text.", encoding="utf-8")
    _ = harness.import_image(1, "v2", "--parent", "v1")
    state = Store.at(harness.workspace).load(SessionId("demo"))
    # When the guide is generated for the selected edit.
    text = guide(state, state.artifact(ArtifactId("v2")))
    # Then initial palette intent and authoritative selected request are both explicit.
    assert "Initial brief palette" in text
    assert "green" in text
    assert "Selected version request" in text
    assert "authoritative" in text.lower()
    assert "Change green to navy and preserve exact text." in text


def test_old_selected_parent_exports_its_palette_and_lockup(harness: Harness) -> None:
    # Given a selected green parent and a newer navy child whose palette is active.
    lockup = LockupIntent(
        layout="horizontal",
        typography_style="단정한 한글 고딕",
        font_reference="Noto Sans KR",
    )
    state = prepare_color(harness, lockup=lockup)
    parent = state.artifact(ArtifactId("v1"))
    navy_content = PaletteContent(
        swatches=(Swatch(hex="#000080", role="symbol"),),
        constraints=state.palettes[0].constraints,
        source="assistant",
        selected_by="user",
        rationale="New child direction",
    )
    navy = PaletteVersion.model_validate(
        {
            **navy_content.model_dump(),
            "id": PaletteId("navy"),
            "parent_palette_id": PaletteId("green"),
            "digest": palette_digest(navy_content),
        }
    )
    child = parent.model_copy(
        update={
            "id": ArtifactId("v2"),
            "path": "artifacts/v2.png",
            "parent_id": parent.id,
            "palette_id": navy.id,
            "lockup": lockup.model_copy(update={"layout": "stacked"}),
        }
    )
    _ = (harness.state_path.parent / child.path).write_bytes(harness.png.read_bytes())
    store = Store.at(harness.workspace)
    store.save(
        state.model_copy(
            update={
                "artifacts": (parent, child),
                "palettes": (*state.palettes, navy),
                "active_palette_id": navy.id,
            }
        )
    )
    # When the existing parent is exported through the actual CLI.
    _ = harness.ok("export", "--session", "demo", "--revision", str(state.revision))
    # Then intent, fresh report, and typography all describe the selected green parent.
    bundle = harness.workspace / "output/logo-generator/demo"
    manifest = Manifest.model_validate_json((bundle / "manifest.json").read_bytes())
    text = (bundle / "brand-guide.md").read_text(encoding="utf-8")
    assert manifest.intended_palette == state.palettes[0]
    assert manifest.color_report.palette_id == PaletteId("green")
    assert manifest.color_report.status == "pass"
    assert manifest.lockup_intent == lockup
    assert manifest.font_reference_usage == "appearance-reference-only"
    assert "Selected palette version: green" in text
    assert "#000080" not in text
    assert "horizontal" in text
    assert "단정한 한글 고딕" in text
    assert "Noto Sans KR" in text
    assert "appearance-reference-only" in text
    assert "font license" in text


def test_legacy_export_stays_color_unverified(harness: Harness) -> None:
    # Given a reviewed artifact whose palette exists only as historical free text.
    harness.prepare_export()
    # When legacy behavior exports the original image.
    _ = harness.ok("export", "--session", "demo", "--revision", "3")
    # Then no structured HEX or compliant status is invented from the old brief.
    bundle = harness.workspace / "output/logo-generator/demo"
    manifest = Manifest.model_validate_json((bundle / "manifest.json").read_bytes())
    assert manifest.intended_palette is None
    assert manifest.color_policy == "unverified"
    assert manifest.color_report.status == "unverified"
    assert manifest.color_report.targets == ()
    assert "Color-unverified" in " ".join(manifest.warnings)
    assert "historical intent" in (bundle / "brand-guide.md").read_text(encoding="utf-8")


def test_export_preserves_explicit_roi_and_discloses_scope(harness: Harness) -> None:
    # Given the latest explicit analysis covers a region with exactly 128 core samples.
    state = prepare_color(harness)
    roi = RegionOfInterest(x=0, y=8, width=16, height=8)
    report = analyze_png(
        harness.png.read_bytes(),
        state.artifacts[0],
        state.palettes[0],
        report_id=ReportId("region"),
        roi=roi,
        surfaces=("#FFFFFF", "#000000"),
    )
    Store.at(harness.workspace).save(
        state.model_copy(
            update={
                "color_reports": (*state.color_reports, report),
            }
        )
    )
    # When export recomputes the selected scope from the original PNG.
    _ = harness.ok("export", "--session", "demo", "--revision", str(state.revision))
    # Then both structured evidence and the guide explicitly limit the claim to the ROI.
    bundle = harness.workspace / "output/logo-generator/demo"
    manifest = Manifest.model_validate_json((bundle / "manifest.json").read_bytes())
    assert manifest.color_report.sampling.roi == roi
    assert manifest.color_report.sampling.core_samples == 128
    assert {c.surface for c in manifest.color_report.contrasts} == {"#FFFFFF", "#000000"}
    assert "ROI" in " ".join(manifest.warnings)
    assert "Scope: roi" in (bundle / "brand-guide.md").read_text(encoding="utf-8")
