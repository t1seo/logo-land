from __future__ import annotations

import json
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from logo_helper.color_models import (
    ColorConstraints,
    PaletteContent,
    PaletteVersion,
    Swatch,
    normalize_hex,
    palette_digest,
)
from logo_helper.lockup_models import LockupIntent
from logo_helper.models import (
    Artifact,
    ArtifactId,
    Brief,
    ColorReport,
    ImageFacts,
    PaletteId,
    ProjectError,
    Reference,
    ReferenceId,
    RegionOfInterest,
    ReportId,
    SamplingSettings,
    Session,
    SessionId,
)


def palette(identifier: str = "p1", parent: str | None = None) -> PaletteVersion:
    content = PaletteContent(
        swatches=(Swatch(hex="#247a52", role="primary"),),
        source="assistant",
        selected_by="assistant",
        rationale="Keep the requested green",
    )
    return PaletteVersion(
        swatches=content.swatches,
        constraints=content.constraints,
        source=content.source,
        source_evidence=content.source_evidence,
        selected_by=content.selected_by,
        rationale=content.rationale,
        calculation_version=content.calculation_version,
        id=PaletteId(identifier),
        parent_palette_id=PaletteId(parent) if parent is not None else None,
        digest=palette_digest(content),
    )


def session(*palettes: PaletteVersion) -> Session:
    now = datetime.now(UTC)
    return Session(
        id=SessionId("demo"),
        created_at=now,
        updated_at=now,
        brief=Brief(
            brand_name="모로", exact_text="모로  Studio", industry="design", audience="all"
        ),
        palettes=palettes,
    )


@pytest.mark.parametrize(("value", "expected"), [("#abc", "#AABBCC"), ("#247a52", "#247A52")])
def test_hex_is_normalized(value: str, expected: str) -> None:
    assert normalize_hex(value) == expected


@pytest.mark.parametrize("value", ["red", "#abcd", "#12345678", "#GG0000", " #abc", "rgb(0,0,0)"])
def test_invalid_hex_is_rejected(value: str) -> None:
    with pytest.raises(ProjectError, match="invalid_color"):
        _ = normalize_hex(value)


def test_constraints_deduplicate_after_normalization() -> None:
    constraints = ColorConstraints.model_validate_json(
        '{"locked_hex":["#abc","#AABBCC"],"allowed_hex":["#abc","#aabbcc"],"max_colors":1}'
    )
    assert constraints.locked_hex == ("#AABBCC",)
    assert constraints.allowed_hex == ("#AABBCC",)
    assert constraints.strict
    assert not ColorConstraints().strict


@pytest.mark.parametrize(
    "raw",
    [
        '{"locked_hex":["#000","#fff"],"max_colors":1}',
        '{"locked_hex":["#000"],"allowed_hex":["#fff"]}',
        '{"required_hex":["#000"],"allowed_hex":["#fff"]}',
        '{"allow_gradients":true,"max_colors":2}',
        '{"allow_gradients":true,"allowed_hex":["#fff"]}',
        '{"allowed_hex":[]}',
    ],
)
def test_constraint_conflicts_have_stable_code(raw: str) -> None:
    with pytest.raises(ProjectError, match="constraint_conflict"):
        _ = ColorConstraints.model_validate_json(raw)


@pytest.mark.parametrize("raw", ['{"max_colors":true}', '{"max_colors":9}', '{"mode":"auto"}'])
def test_constraints_reject_coercion_and_unknown_fields(raw: str) -> None:
    with pytest.raises(ValidationError):
        _ = ColorConstraints.model_validate_json(raw)


def test_palette_digest_detects_changed_intent() -> None:
    original = palette()
    with pytest.raises(ProjectError, match="digest_mismatch"):
        _ = PaletteVersion.model_validate_json(
            original.model_dump_json().replace("#247A52", "#112233")
        )
    assert original.digest == palette("p2").digest
    assert palette_digest(original) == original.digest


def test_session_rejects_missing_palette_parent_and_duplicate_ids() -> None:
    with pytest.raises(ProjectError, match="invalid_state"):
        _ = session(palette(parent="missing"))
    with pytest.raises(ProjectError, match="invalid_state"):
        _ = session(palette(), palette())
    assert session(palette(), palette("p2", "p1")).palette(PaletteId("p2")).id == "p2"


def test_lockup_roundtrip_preserves_exact_text_and_requested_font() -> None:
    lockup = LockupIntent(
        layout="stacked", typography_style="Round Hangul", font_reference="Requested family"
    )
    brief = session().brief.model_copy(update={"lockup": lockup})
    restored = Brief.model_validate_json(brief.model_dump_json())
    assert restored.exact_text == "모로  Studio"
    assert restored.lockup == lockup
    assert session().brief.lockup is None
    with pytest.raises(ValidationError):
        _ = LockupIntent.model_validate_json('{"layout":"diagonal","typography_style":"round"}')


def test_duplicate_swatches_keep_first_role_and_digest_normalizes() -> None:
    content = PaletteContent(
        swatches=(Swatch(hex="#abc", role="primary"), Swatch(hex="#AABBCC", role="accent")),
        source="assistant",
        selected_by="user",
        rationale="Requested color",
    )
    assert content.swatches == (Swatch(hex="#AABBCC", role="primary"),)
    with pytest.raises(ValidationError, match="frozen_instance"):
        content.rationale = "Changed"


def test_invalid_active_palette_is_rejected() -> None:
    invalid = session().model_copy(update={"active_palette_id": "missing"})
    with pytest.raises(ProjectError, match="Active palette"):
        _ = Session.model_validate_json(invalid.model_dump_json())


def test_reference_roi_is_oriented_and_paths_are_bound_to_format() -> None:
    reference = Reference(
        id=ReferenceId("photo"),
        path="references/photo.jpg",
        sha256="a" * 64,
        format="JPEG",
        width=40,
        height=20,
        exif_orientation=6,
        roi=RegionOfInterest(x=0, y=20, width=20, height=20),
        created_at=datetime.now(UTC),
    )
    assert reference.roi is not None
    with pytest.raises(ProjectError, match="invalid_roi"):
        _ = Reference.model_validate_json(reference.model_dump_json().replace('"x":0', '"x":1'))
    with pytest.raises(ProjectError, match="unsafe_path"):
        _ = Reference.model_validate_json(
            reference.model_dump_json().replace("photo.jpg", "photo.png")
        )


def bound_report_session() -> Session:
    current = session(palette())
    artifact = Artifact(
        id=ArtifactId("v1"),
        path="artifacts/v1.png",
        sha256="a" * 64,
        image=ImageFacts(
            width=16,
            height=16,
            alpha_min=255,
            alpha_max=255,
            transparent_pixels=0,
            visible_pixels=256,
        ),
        prompt="Fixture only",
        created_at=current.created_at,
        palette_id=PaletteId("p1"),
    )
    report = ColorReport(
        id=ReportId("r1"),
        artifact_id=artifact.id,
        artifact_sha256=artifact.sha256,
        palette_id=PaletteId("p1"),
        palette_digest=palette().digest,
        color_engine_version="8.12.1",
        pillow_version="12.3.0",
        profile_treatment="assumed_srgb",
        sampling=SamplingSettings(
            width=16,
            height=16,
            sampled_positions=256,
            sampled_fraction=1.0,
            visible_samples=256,
            core_samples=256,
            partial_alpha_samples=0,
        ),
        status="unverified",
        reasons=("Fixture only",),
        created_at=current.created_at,
    )
    result = current.model_copy(update={"artifacts": (artifact,), "color_reports": (report,)})
    return Session.model_validate_json(result.model_dump_json())


@pytest.mark.parametrize(
    ("original", "changed"),
    [
        ('"artifact_sha256":"' + "a" * 64, '"artifact_sha256":"' + "b" * 64),
        ('"artifact_id":"v1"', '"artifact_id":"missing"'),
        ('"palette_digest":"', '"palette_digest":"f'),
        ('"core_samples":256', '"core_samples":257'),
        ('"profile_treatment":"assumed_srgb"', '"profile_treatment":"made_up"'),
    ],
)
def test_report_binding_and_measurement_tampering_is_rejected(original: str, changed: str) -> None:
    raw = bound_report_session().model_dump_json()
    assert original in raw
    with pytest.raises((ProjectError, ValidationError)):
        _ = Session.model_validate_json(raw.replace(original, changed))


def test_reports_require_paired_palette_binding_and_failure_reason() -> None:
    report = bound_report_session().color_reports[0]
    for update in ({"palette_digest": None}, {"reasons": ()}):
        invalid = report.model_copy(update=update)
        with pytest.raises(ProjectError, match="invalid_state"):
            _ = ColorReport.model_validate_json(invalid.model_dump_json())


@pytest.mark.parametrize("field", ["locked_hex", "allowed_hex", "required_hex"])
def test_constraint_lists_reject_nine_unique_colors(field: str) -> None:
    # Given
    raw = json.dumps({field: [f"#{index:06X}" for index in range(9)]})
    # When
    with pytest.raises(ProjectError, match="constraint_conflict"):
        _ = ColorConstraints.model_validate_json(raw)


@pytest.mark.parametrize("field", ["locked_hex", "allowed_hex", "required_hex"])
def test_constraint_lists_allow_eight_colors_after_normalization(field: str) -> None:
    # Given
    colors = ["#abc", "#AABBCC", *(f"#{index:06X}" for index in range(7))] * 2
    # When
    parsed = ColorConstraints.model_validate_json(json.dumps({field: colors}))
    # Then
    assert parsed.model_dump()[field] == ("#AABBCC", *(f"#{index:06X}" for index in range(7)))
