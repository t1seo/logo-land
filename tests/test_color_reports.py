from __future__ import annotations

import hashlib
import os
from typing import TYPE_CHECKING, Literal, assert_never
from zipfile import ZipFile

import pytest
from PIL import Image
from PIL.PngImagePlugin import PngInfo

from logo_helper import delivery
from logo_helper.color_models import (
    ColorConstraints,
    PaletteContent,
    Swatch,
)
from logo_helper.models import Session, SessionId
from logo_helper.storage import Store

if TYPE_CHECKING:
    from pathlib import Path

    from logo_helper.lockup_models import LockupIntent
    from tests.conftest import Harness


def prepare_color(
    harness: Harness,
    *,
    strict: bool = True,
    evidence: bool = True,
    lockup: LockupIntent | None = None,
) -> Session:
    harness.init()
    content = PaletteContent(
        swatches=(Swatch(hex="#007832", role="symbol"), Swatch(hex="#FFFFFF", role="lettering")),
        constraints=ColorConstraints(max_colors=2) if strict else ColorConstraints(),
        source="assistant",
        selected_by="user",
        rationale="Synthetic fixture palette",
    )
    palette_file = harness.brief.with_name("palette.json")
    _ = palette_file.write_text(content.model_dump_json(), encoding="utf-8")
    _ = harness.ok(
        "palette-add",
        "--session",
        "demo",
        "--revision",
        "0",
        "--palette",
        "green",
        "--palette-file",
        str(palette_file),
    )
    extra: tuple[str, ...] = ()
    if lockup is not None:
        lockup_file = harness.brief.with_name("lockup.json")
        _ = lockup_file.write_text(lockup.model_dump_json(), encoding="utf-8")
        extra = ("--lockup-file", str(lockup_file))
    _ = harness.import_image(1, "v1", *extra)
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
    state = Store.at(harness.workspace).load(SessionId("demo"))
    if not evidence:
        state = state.model_copy(update={"color_reports": ()})
        _ = harness.state_path.write_text(state.model_dump_json(), encoding="utf-8")
    return state


@pytest.mark.parametrize("status", ["missing", "unverified", "indeterminate"])
def test_strict_export_requires_existing_analysis(harness: Harness, status: str) -> None:
    # Given a fully reviewed strict artifact with no stored analysis.
    state = prepare_color(harness, evidence=status != "missing")
    if state.color_reports:
        report = state.color_reports[0].model_copy(
            update={
                "status": status,
                "reasons": ("Previous analysis unavailable",),
            }
        )
        _ = harness.state_path.write_text(
            state.model_copy(update={"color_reports": (report,)}).model_dump_json(),
            encoding="utf-8",
        )
    before = harness.state_path.read_bytes()
    # When exporting through the actual CLI.
    result = harness.run("export", "--session", "demo", "--revision", str(state.revision))
    # Then no visual-review boolean silently substitutes for explicit analysis.
    assert result.returncode != 0
    assert "color_review_required" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output").exists()


@pytest.mark.parametrize("stored_status", ["pass", "mismatch"])
@pytest.mark.parametrize("third_color", [False, True])
def test_export_recomputes_forged_report_metrics(
    harness: Harness,
    stored_status: str,
    third_color: bool,
) -> None:
    # Given an obviously red source and forged stored green matching metrics.
    with Image.new("RGBA", (20, 20), "red") as image:
        if third_color:
            image.paste((0, 120, 50, 255), (0, 0, 10, 20))
            image.paste((255, 255, 255, 255), (10, 0, 19, 20))
        image.putpixel((0, 0), (0, 0, 0, 0))
        image.save(harness.png)
    state = prepare_color(harness)
    report = state.color_reports[0].model_copy(
        update={
            "status": stored_status,
            "matched_fraction": 1.0,
            "unmatched_fraction": 0.0,
            "observed_colors": 1,
            "delta_e_threshold": 1000.0,
            "targets": tuple(
                target.model_copy(
                    update={
                        "matching_samples": 399,
                        "share": 1.0,
                        "mean_delta_e": 0.0,
                        "max_delta_e": 0.0,
                    }
                )
                for target in state.color_reports[0].targets
            ),
        }
    )
    forged = state.model_copy(update={"color_reports": (report,)})
    _ = harness.state_path.write_text(forged.model_dump_json(), encoding="utf-8")
    before = harness.state_path.read_bytes()
    # When export recomputes from the hash-verified bytes.
    result = harness.run("export", "--session", "demo", "--revision", str(state.revision))
    # Then the truthful mismatch blocks output and leaves all existing evidence unchanged.
    assert result.returncode != 0
    assert "color_mismatch" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output").exists()


@pytest.mark.parametrize("uncertainty", ["unsupported_profile", "insufficient_core"])
@pytest.mark.parametrize("forged_pass", [False, True])
def test_strict_export_requires_determinate_evidence(
    harness: Harness,
    uncertainty: Literal["unsupported_profile", "insufficient_core"],
    forged_pass: bool,
) -> None:
    # Given an otherwise matching image whose profile or core evidence is insufficient.
    metadata = PngInfo()
    opacity = 255
    match uncertainty:
        case "unsupported_profile":
            metadata.add(b"gAMA", (100000).to_bytes(4))
        case "insufficient_core":
            opacity = 100
        case _:
            assert_never(uncertainty)
    with Image.new("RGBA", (16, 16), (0, 120, 50, opacity)) as image:
        image.putpixel((0, 0), (0, 0, 0, 0))
        image.save(harness.png, pnginfo=metadata)
    state = prepare_color(harness)
    if forged_pass:
        report = state.color_reports[0].model_copy(update={"status": "pass", "reasons": ()})
        _ = harness.state_path.write_text(
            state.model_copy(update={"color_reports": (report,)}).model_dump_json(),
            encoding="utf-8",
        )
    before = harness.state_path.read_bytes()
    # When exporting despite every visual review check passing.
    result = harness.run("export", "--session", "demo", "--revision", str(state.revision))
    # Then uncertainty is explicit and neither output nor state is published.
    assert result.returncode != 0
    assert "color_review_required" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output").exists()


@pytest.mark.parametrize("stored_mismatch", [False, True])
def test_export_appends_fresh_report_with_original_zip_bytes(
    harness: Harness,
    stored_mismatch: bool,
) -> None:
    # Given a measured strict green artifact.
    state = prepare_color(harness)
    if stored_mismatch:
        report = state.color_reports[0].model_copy(
            update={
                "status": "mismatch",
                "reasons": ("Stale stored conclusion",),
            }
        )
        state = state.model_copy(update={"color_reports": (report,)})
        _ = harness.state_path.write_text(state.model_dump_json(), encoding="utf-8")
    original = harness.png.read_bytes()
    # When exporting through the actual CLI.
    _ = harness.ok("export", "--session", "demo", "--revision", str(state.revision))
    # Then one immutable fresh report and export record commit together with truthful payloads.
    updated = Store.at(harness.workspace).load(state.id)
    bundle = harness.workspace / "output/logo-generator/demo"
    manifest = delivery.Manifest.model_validate_json((bundle / "manifest.json").read_bytes())
    assert manifest.schema_version == 2
    assert len(updated.color_reports) == len(state.color_reports) + 1
    assert updated.color_reports[:-1] == state.color_reports
    assert manifest.color_report == updated.color_reports[-1]
    assert manifest.intended_palette == state.palettes[0]
    assert manifest.color_report.status == "pass"
    assert len(updated.exports) == 1
    assert (bundle / "logo.png").read_bytes() == original
    with ZipFile(bundle / "logo-package.zip") as archive:
        assert set(archive.namelist()) == {"logo.png", "manifest.json", "brand-guide.md"}
        assert all(
            archive.read(name) == (bundle / name).read_bytes() for name in archive.namelist()
        )
    assert hashlib.sha256(original).hexdigest() == manifest.source.sha256


def test_advisory_mismatch_exports_with_explicit_warning(harness: Harness) -> None:
    # Given unconstrained green intent and an actual red source.
    with Image.new("RGBA", (16, 16), "red") as image:
        image.putpixel((0, 0), (0, 0, 0, 0))
        image.save(harness.png)
    state = prepare_color(harness, strict=False)
    # When exporting an advisory palette mismatch.
    _ = harness.ok("export", "--session", "demo", "--revision", str(state.revision))
    # Then the package preserves the mismatch and warns rather than claiming fidelity.
    bundle = harness.workspace / "output/logo-generator/demo"
    manifest = delivery.Manifest.model_validate_json((bundle / "manifest.json").read_bytes())
    assert manifest.color_report.status == "mismatch"
    assert manifest.color_policy == "advisory"
    assert manifest.warnings
    assert "mismatch" in (bundle / "brand-guide.md").read_text(encoding="utf-8")


def fail_save(_store: Store, _state: Session) -> None:
    raise OSError(28, "simulated full disk")


def test_color_report_rolls_back_when_state_commit_fails(
    harness: Harness,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given an existing successful export and a subsequent state-write failure.
    state = prepare_color(harness)
    updated = delivery.export(Store.at(harness.workspace), state.id, state.revision, "prior")
    before = harness.state_path.read_bytes()
    prior = (harness.workspace / "prior/logo-package.zip").read_bytes()
    monkeypatch.setattr(Store, "save", fail_save)
    # When a second export cannot commit its new report and export record.
    with pytest.raises(OSError, match="full disk"):
        _ = delivery.export(
            Store.at(harness.workspace), state.id, updated.revision, "failed/nested"
        )
    # Then prior state and package survive and the failed directory is removed.
    assert harness.state_path.read_bytes() == before
    assert (harness.workspace / "prior/logo-package.zip").read_bytes() == prior
    assert not (harness.workspace / "failed").exists()


def test_color_report_rolls_back_when_publish_fails(
    harness: Harness,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given a measured strict source and an unavailable publication filesystem.
    state = prepare_color(harness)
    before = harness.state_path.read_bytes()
    original_link = os.link

    def fail_link(source: Path, destination: Path) -> None:
        if destination.name == "manifest.json":
            raise OSError(28, "simulated publish failure")
        original_link(source, destination)

    monkeypatch.setattr(os, "link", fail_link)
    # When linking the staged package fails.
    with pytest.raises(OSError, match="publish failure"):
        _ = delivery.export(Store.at(harness.workspace), state.id, state.revision, "failed/nested")
    # Then the report, export record, and partial bundle are all absent.
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "failed").exists()
