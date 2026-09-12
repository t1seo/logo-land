from __future__ import annotations

import shutil
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Literal, assert_never

import pytest

from logo_helper.color_gallery import render_color_gallery, render_palette_cards
from logo_helper.color_gallery_data import report_markup
from logo_helper.color_models import (
    ColorConstraints,
    PaletteContent,
    PaletteVersion,
    SourceEvidence,
    Swatch,
    palette_digest,
)
from logo_helper.color_reports import (
    ColorReport,
    MeasuredSwatch,
    SamplingSettings,
    TargetMeasurement,
)
from logo_helper.lockup_models import LockupIntent
from logo_helper.models import ArtifactId, PaletteId, ProjectError, ReportId, Session, SessionId
from logo_helper.storage import Store

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


@pytest.fixture
def gallery_state(harness: Harness) -> Session:
    harness.init()
    _ = harness.import_image()
    _ = harness.import_image(1, "v2", "--parent", "v1")
    return Store.at(harness.workspace).load(SessionId("demo"))


def color_state(
    state: Session,
    status: Literal["pass", "mismatch", "indeterminate", "unverified"] | None,
    *,
    strict: bool = True,
) -> Session:
    content = PaletteContent(
        swatches=(Swatch(hex="#fff", role="primary"),),
        constraints=ColorConstraints(max_colors=1) if strict else ColorConstraints(),
        source="assistant",
        selected_by="user",
        rationale="Public palette direction",
    )
    palette = PaletteVersion.model_validate(
        {**content.model_dump(), "id": PaletteId("p1"), "digest": palette_digest(content)}
    )
    artifact = state.artifacts[1].model_copy(
        update={
            "palette_id": palette.id,
            "lockup": LockupIntent(
                layout="stacked", typography_style="Round Hangul", font_reference="Requested Family"
            ),
        }
    )
    sampling_json = (
        '{"width":16,"height":16,"sampled_positions":256,"sampled_fraction":1.0,'
        '"visible_samples":255,"core_samples":255,"partial_alpha_samples":0}'
    )
    reports = (
        ()
        if status is None
        else (
            ColorReport(
                id=ReportId("r1"),
                artifact_id=artifact.id,
                artifact_sha256=artifact.sha256,
                palette_id=palette.id,
                palette_digest=palette.digest,
                color_engine_version="fixture",
                pillow_version="fixture",
                profile_treatment="assumed_srgb",
                status=status,
                reasons=("<script>unsafe reason</script>",),
                created_at=datetime.now(UTC),
                sampling=SamplingSettings.model_validate_json(sampling_json),
                measured_swatches=(MeasuredSwatch(hex="#007832", samples=255, share=1.0),),
                targets=(
                    TargetMeasurement(
                        hex="#fff",
                        matching_samples=0,
                        share=0.0,
                        mean_delta_e=42.0,
                        max_delta_e=43.0,
                    ),
                ),
            ),
        )
    )
    return Session.model_validate_json(
        state.model_copy(
            update={
                "palettes": (palette,),
                "artifacts": (state.artifacts[0], artifact),
                "color_reports": reports,
            }
        ).model_dump_json()
    )


def test_candidate_cards_escape_text_and_hide_private_evidence() -> None:
    # Given: a candidate contains display text and private provider evidence.
    candidate = PaletteContent(
        swatches=(Swatch(hex="#fff", role='<img src=x onerror="alert(1)">'),),
        source="assistant",
        selected_by="user",
        rationale="<script>alert(1)</script>",
        source_evidence=SourceEvidence(response="PRIVATE PROVIDER PROMPT /Users/private"),
    )
    before = candidate.model_dump_json()
    # When: the candidate is presented for selection without persisting it.
    markup = render_palette_cards((candidate,))
    # Then: visible content is inert and evidence remains private.
    assert "&lt;script&gt;" in markup
    assert "&lt;img" in markup
    assert "#FFFFFF" in markup
    assert 'type="radio"' in markup
    assert "PRIVATE PROVIDER" not in markup
    assert "/Users/private" not in markup
    assert "<script>" not in markup
    assert candidate.model_dump_json() == before


def test_explicit_artifacts_are_portable_byteidentical_and_readonly(
    harness: Harness, gallery_state: Session, tmp_path: Path
) -> None:
    # Given: two versions exist and only the child is requested.
    state_bytes = harness.state_path.read_bytes()
    store = Store.at(harness.workspace)
    # When: the gallery is rendered then relocated with its assets.
    result = render_color_gallery(store, gallery_state, (ArtifactId("v2"),), "output/colors")
    relocated = tmp_path / "relocated"
    _ = shutil.copytree(harness.workspace / result.path, relocated)
    markup = (relocated / "index.html").read_text()
    # Then: only explicit original bytes and relative links ship, with no session mutation.
    assert result.index_path == "output/colors/index.html"
    assert result.artifact_ids == (ArtifactId("v2"),)
    assert (relocated / "images/v2.png").read_bytes() == harness.png.read_bytes()
    assert not (relocated / "images/v1.png").exists()
    assert 'src="images/v2.png"' in markup
    assert all(
        text in markup
        for text in ("Parent artifact", "v1", "Legacy / unknown intent", "unverified")
    )
    assert str(store.root) not in markup
    assert harness.prompt.read_text() not in markup
    assert all(text not in markup for text in ("https://", "http://", "<script"))
    assert harness.state_path.read_bytes() == state_bytes


@pytest.mark.parametrize("status", ["pass", "mismatch", "indeterminate", "unverified", None])
@pytest.mark.parametrize("strict", [True, False])
def test_reports_keep_status_intent_measurement_and_font_truth(
    harness: Harness,
    gallery_state: Session,
    status: Literal["pass", "mismatch", "indeterminate", "unverified"] | None,
    *,
    strict: bool,
) -> None:
    # Given: bound palette intent and an optional stored report.
    state = color_state(gallery_state, status, strict=strict)
    # When: the explicit child is rendered.
    result = render_color_gallery(Store.at(harness.workspace), state, (ArtifactId("v2"),), "colors")
    markup = (harness.workspace / result.index_path).read_text()
    # Then: unknown stays unverified and report scope/measurements remain visibly distinct.
    assert f'<section data-status="{status or "unverified"}"' in markup
    assert all(
        text in markup
        for text in (
            "Intended colors",
            "Measured colors",
            "Requested Family",
            "stacked",
            "system font",
            "font file",
            'id="surface-dark"',
            'id="size-small"',
        )
    )
    assert ("Strict constraints" if strict else "Advisory intent") in markup
    if status is not None:
        assert all(text in markup for text in ("full_image", "42.00", "43.00"))
        assert "&lt;script&gt;unsafe reason&lt;/script&gt;" in markup
        assert "#007832" in markup
    else:
        assert '<section data-status="pass"' not in markup


@pytest.mark.parametrize(
    "output",
    [
        "../escape",
        "/escape",
        "a/../escape",
        "a\\escape",
        ".logo-generator/gallery",
        ".git/gallery",
    ],
)
def test_unsafe_destinations_are_rejected(
    harness: Harness, gallery_state: Session, output: str
) -> None:
    # Given: an escaping or reserved destination.
    store = Store.at(harness.workspace)
    # When / Then: rendering rejects it without touching session bytes.
    before = harness.state_path.read_bytes()
    with pytest.raises(ProjectError, match=r"unsafe_path|reserved_output"):
        _ = render_color_gallery(store, gallery_state, (ArtifactId("v1"),), output)
    assert harness.state_path.read_bytes() == before


@pytest.mark.parametrize(
    "kind", ["existing", "symlink", "missing", "tampered", "duplicate", "empty"]
)
def test_failed_render_preserves_files_and_cleans_staging(
    harness: Harness,
    gallery_state: Session,
    tmp_path: Path,
    kind: Literal["existing", "symlink", "missing", "tampered", "duplicate", "empty"],
) -> None:
    # Given: one named filesystem or selection failure.
    store = Store.at(harness.workspace)
    output = harness.workspace / "colors"
    image = store.session_dir(gallery_state.id) / gallery_state.artifacts[0].path
    ids = (ArtifactId("v1"),)
    expected = "conflict"
    match kind:
        case "existing":
            output.mkdir()
            _ = (output / "keep.txt").write_text("keep")
        case "symlink":
            output.symlink_to(tmp_path, target_is_directory=True)
            expected = "unsafe_path"
        case "missing":
            image.unlink()
            expected = "invalid_file"
        case "tampered":
            _ = image.write_bytes(b"tampered")
            expected = "hash_mismatch"
        case "duplicate":
            ids = (ArtifactId("v1"), ArtifactId("v1"))
            expected = "invalid_selection"
        case "empty":
            ids = ()
            expected = "invalid_selection"
        case _:
            assert_never(kind)
    # When / Then: the named failure leaves no partial gallery or staging directory.
    with pytest.raises(ProjectError, match=expected):
        _ = render_color_gallery(store, gallery_state, ids, "colors")
    assert not list(harness.workspace.glob(".logo-gallery-*"))
    if output.is_dir() and not output.is_symlink():
        assert (output / "keep.txt").read_text() == "keep"
    elif not output.is_symlink():
        assert not output.exists()


def test_brand_xss_is_inert(harness: Harness, gallery_state: Session) -> None:
    # Given: a brand deliberately contains HTML and attribute injection.
    brand = '<script>alert("x")</script><img src=x onerror=alert(1)>'
    state = gallery_state.model_copy(
        update={"brief": gallery_state.brief.model_copy(update={"brand_name": brand})}
    )
    # When: the page is generated.
    result = render_color_gallery(Store.at(harness.workspace), state, (ArtifactId("v1"),), "colors")
    markup = (harness.workspace / result.index_path).read_text()
    # Then: the brand is text in every HTML context.
    assert all(text in markup for text in ("&lt;script&gt;", "&quot;x&quot;"))
    assert all(text not in markup for text in ("<script>", "<img src=x"))


def test_unbound_report_pass_is_never_color_verification(gallery_state: Session) -> None:
    # Given: a stored pass has no palette intent to verify against.
    report = color_state(gallery_state, "pass").color_reports[0]
    unbound = report.model_copy(update={"palette_id": None, "palette_digest": None})
    # When: it is presented as a snapshot.
    markup = report_markup(unbound)
    # Then: unknown intent cannot acquire a passing color status.
    assert '<section data-status="unverified"' in markup
