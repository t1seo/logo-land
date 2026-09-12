from __future__ import annotations

import hashlib
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Literal, assert_never
from zipfile import ZipFile

import pytest
from PIL import Image

from logo_helper import color_analysis, color_delivery, delivery
from logo_helper.images import inspect_png
from logo_helper.models import ProjectError, SessionId
from logo_helper.storage import Store
from tests.test_color_reports import prepare_color
from tests.test_palette_compatibility import write_legacy

if TYPE_CHECKING:
    from logo_helper.color_models import PaletteVersion
    from logo_helper.models import Artifact, ReportId
    from logo_helper.reference_models import RegionOfInterest
    from tests.conftest import Harness

type Metadata = Literal["invalid_exif", "invalid_icc"]
type Policy = Literal["schema1", "unverified", "advisory"]


def metadata_png(harness: Harness, metadata: Metadata) -> bytes:
    with Image.open(harness.png) as source:
        source_pixels = source.tobytes()
        with source.copy() as image:
            match metadata:
                case "invalid_exif":
                    exif = Image.Exif()
                    exif[274] = 0
                    image.save(harness.png, exif=exif)
                case "invalid_icc":
                    image.save(harness.png, icc_profile=b"invalid deterministic ICC fixture")
                case _:
                    assert_never(metadata)
    with Image.open(harness.png) as result:
        assert result.tobytes() == source_pixels
    data = harness.png.read_bytes()
    assert inspect_png(data).visible_pixels == 255
    return data


@pytest.mark.parametrize("metadata", ["invalid_exif", "invalid_icc"])
@pytest.mark.parametrize("policy", ["schema1", "unverified", "advisory"])
def test_non_strict_export_preserves_png_with_unassessable_metadata(
    harness: Harness, metadata: Metadata, policy: Policy
) -> None:
    # Given accepted original PNG bytes and no strict color requirements.
    original = metadata_png(harness, metadata)
    match policy:
        case "advisory":
            state = prepare_color(harness, strict=False)
        case "schema1" | "unverified":
            harness.prepare_export()
            if policy == "schema1":
                _ = write_legacy(harness)
            state = Store.at(harness.workspace).load(SessionId("demo"))
        case _:
            assert_never(policy)
    before = harness.state_path.read_bytes()
    # When exporting through the actual CLI, including first-mutation v1 migration.
    _ = harness.ok("export", "--session", "demo", "--revision", str(state.revision))
    # Then byte-identical delivery and truthful unavailable evidence commit together.
    bundle = harness.workspace / "output/logo-generator/demo"
    manifest = delivery.Manifest.model_validate_json((bundle / "manifest.json").read_bytes())
    updated = Store.at(harness.workspace).load(state.id)
    report = manifest.color_report
    assert report.status == ("indeterminate" if policy == "advisory" else "unverified")
    assert manifest.color_policy == ("advisory" if policy == "advisory" else "unverified")
    assert report.profile_treatment == "unsupported"
    assert report.targets == report.contrasts == report.measured_swatches == ()
    assert report.matched_fraction is report.unmatched_fraction is report.observed_colors is None
    assert any("EXIF" in reason or "ICC" in reason for reason in report.reasons)
    assert report.reasons[0] in manifest.warnings
    assert report.reasons[0] in (bundle / "brand-guide.md").read_text(encoding="utf-8")
    assert updated.color_reports == (*state.color_reports, report)
    assert len(updated.exports) == len(state.exports) + 1
    assert report.artifact_sha256 == hashlib.sha256(original).hexdigest()
    assert (bundle / "logo.png").read_bytes() == original
    with ZipFile(bundle / "logo-package.zip") as archive:
        assert set(archive.namelist()) == {"logo.png", "manifest.json", "brand-guide.md"}
        assert all(
            archive.read(name) == (bundle / name).read_bytes() for name in archive.namelist()
        )
    if metadata == "invalid_exif":
        assert report.sampling.sampled_positions == report.sampling.core_samples == 0
        assert report.sampling.sampled_fraction == 0
    if policy == "schema1":
        assert harness.state_path.with_name("session.v1.backup.json").read_bytes() == before
        assert updated.schema_version == 2
        assert updated.artifacts == state.artifacts


@pytest.mark.parametrize("metadata", ["invalid_exif", "invalid_icc"])
@pytest.mark.parametrize("forged_pass", [False, True])
def test_strict_export_cannot_promote_unassessable_metadata_to_pass(
    harness: Harness, metadata: Metadata, forged_pass: bool
) -> None:
    # Given strict intent, valid visual review, and missing or forged color evidence.
    _ = metadata_png(harness, metadata)
    state = prepare_color(harness)
    if forged_pass:
        report = state.color_reports[0].model_copy(update={"status": "pass", "reasons": ()})
        _ = harness.state_path.write_text(
            state.model_copy(update={"color_reports": (report,)}).model_dump_json(),
            encoding="utf-8",
        )
    before = harness.state_path.read_bytes()
    # When export independently verifies strict color evidence.
    result = harness.run("export", "--session", "demo", "--revision", str(state.revision))
    # Then no report, export, or output is committed from invalid evidence.
    assert result.returncode != 0
    assert "color_review_required" in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output").exists()


@pytest.mark.parametrize("tampering", ["hash", "truncated", "facts"])
def test_metadata_fallback_does_not_bypass_original_integrity(
    harness: Harness, tampering: Literal["hash", "truncated", "facts"]
) -> None:
    # Given an accepted PNG whose stored original changes after review.
    _ = metadata_png(harness, "invalid_exif")
    harness.prepare_export()
    store = Store.at(harness.workspace)
    state = store.load(SessionId("demo"))
    source = store.session_dir(state.id) / state.artifacts[0].path
    artifact = state.artifacts[0]
    match tampering:
        case "hash":
            _ = source.write_bytes(source.read_bytes() + b"changed")
            expected = "hash_mismatch"
        case "truncated":
            truncated = source.read_bytes()[:-12]
            _ = source.write_bytes(truncated)
            artifact = artifact.model_copy(update={"sha256": hashlib.sha256(truncated).hexdigest()})
            expected = "invalid_png"
        case "facts":
            artifact = artifact.model_copy(
                update={
                    "image": artifact.image.model_copy(update={"width": artifact.image.width + 1})
                }
            )
            expected = "invalid_state"
        case _:
            assert_never(tampering)
    _ = harness.state_path.write_text(
        state.model_copy(update={"artifacts": (artifact,)}).model_dump_json(), encoding="utf-8"
    )
    before = harness.state_path.read_bytes()
    # When export reaches the original-byte integrity gate.
    result = harness.run("export", "--session", "demo", "--revision", str(state.revision))
    # Then the original gate still blocks all output and state mutation.
    assert result.returncode != 0
    assert expected in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output").exists()


@pytest.mark.parametrize(
    "error", [ProjectError("integrity", "fixture mismatch"), ValueError("bug")]
)
def test_color_export_does_not_swallow_integrity_or_programming_errors(
    harness: Harness, monkeypatch: pytest.MonkeyPatch, error: ProjectError | ValueError
) -> None:
    # Given a narrow analysis dependency failing outside known color-decode errors.
    harness.prepare_export()
    state = Store.at(harness.workspace).load(SessionId("demo"))

    def fail_analysis(
        _data: bytes,
        _artifact: Artifact,
        _palette: PaletteVersion | None,
        *,
        report_id: ReportId,
        roi: RegionOfInterest | None,
        surfaces: tuple[str, ...],
        created_at: datetime,
    ) -> None:
        _ = report_id, roi, surfaces, created_at
        raise error

    monkeypatch.setattr(color_delivery, "analyze_png", fail_analysis)
    # When obtaining the export color evidence.
    with pytest.raises(type(error), match=str(error)):
        _ = color_delivery.export_colors(
            state, state.artifacts[0], harness.png.read_bytes(), datetime.now(UTC)
        )
    # Then the exact unexpected error remains visible to the caller.


def test_wrapped_sampling_bug_is_not_reclassified_as_unavailable(
    harness: Harness, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given a programming error inside the decoder context manager's yielded analysis.
    harness.prepare_export()
    before = harness.state_path.read_bytes()
    sampling_error = ValueError("synthetic sampling bug")

    def fail_sampling(_image: Image.Image, _roi: RegionOfInterest | None) -> None:
        raise sampling_error

    monkeypatch.setattr(color_analysis, "sample_image", fail_sampling)
    # When the decoder wraps the sampling failure as invalid_reference.
    with pytest.raises(ProjectError, match="invalid_reference") as caught:
        _ = delivery.export(Store.at(harness.workspace), SessionId("demo"), 3, "failed")
    # Then its cause propagates and no unverified delivery hides the programming error.
    assert caught.value.__cause__ is sampling_error
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "failed").exists()
