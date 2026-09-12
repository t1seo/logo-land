from __future__ import annotations

import hashlib
import sys
from datetime import UTC, datetime
from io import BytesIO
from time import perf_counter
from typing import Final

import pytest
from PIL import Image

from logo_helper.color_analysis import analyze_png
from logo_helper.color_models import (
    ColorConstraints,
    PaletteContent,
    PaletteVersion,
    Swatch,
    palette_digest,
)
from logo_helper.images import inspect_png
from logo_helper.models import Artifact, ArtifactId, PaletteId, ProjectError, ReportId
from logo_helper.reference_models import RegionOfInterest

STAMP: Final = datetime(2026, 9, 12, tzinfo=UTC)
NO_CONSTRAINTS: Final = ColorConstraints()


def palette_for(constraints: ColorConstraints = NO_CONSTRAINTS) -> PaletteVersion:
    content = PaletteContent(
        swatches=(Swatch(hex="#000000", role="ink"), Swatch(hex="#F6F3EC", role="paper")),
        constraints=constraints,
        source="assistant",
        selected_by="user",
        rationale="Known swatches",
    )
    return PaletteVersion.model_validate(
        {
            **content.model_dump(),
            "id": PaletteId("known"),
            "digest": palette_digest(content),
        }
    )


def source(image: Image.Image, palette: PaletteVersion | None) -> tuple[bytes, Artifact]:
    with BytesIO() as stream:
        image.save(stream, format="PNG")
        data = stream.getvalue()
    return data, Artifact(
        id=ArtifactId("fixture"),
        path="artifacts/fixture.png",
        sha256=hashlib.sha256(data).hexdigest(),
        image=inspect_png(data),
        prompt="Synthetic test only",
        created_at=STAMP,
        palette_id=palette.id if palette else None,
    )


def test_known_black_ivory_passes_and_bytes_stay_identical() -> None:
    # Given
    palette = palette_for(ColorConstraints(max_colors=2))
    with Image.new("RGB", (256, 256), "#F6F3EC") as image:
        image.paste("#000000", (0, 0, 128, 256))
        data, artifact = source(image, palette)
    # When
    reports = tuple(
        analyze_png(data, artifact, palette, report_id=ReportId("r1"), created_at=STAMP)
        for _ in range(2)
    )
    # Then
    assert reports[0] == reports[1]
    assert reports[0].status == "pass"
    assert reports[0].matched_fraction == 1
    assert reports[0].observed_colors == 2
    assert reports[0].sampling.sampled_positions == 16384
    assert reports[0].targets[0].mean_delta_e == 0
    assert hashlib.sha256(data).hexdigest() == artifact.sha256


@pytest.mark.parametrize(
    ("red_count", "expected"), [(0, "pass"), (100, "pass"), (101, "mismatch"), (500, "mismatch")]
)
def test_restricted_99_percent_boundary(red_count: int, expected: str) -> None:
    # Given
    palette = palette_for(ColorConstraints(max_colors=2))
    with Image.new("RGB", (100, 100), "black") as image:
        for offset in range(red_count):
            image.putpixel((offset % 100, offset // 100), (255, 0, 0))
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == expected
    assert report.unmatched_fraction == pytest.approx(red_count / 10000)


@pytest.mark.parametrize(("color", "expected"), [("#101010", "pass"), ("#303030", "mismatch")])
def test_distance_threshold_uses_original_swatches(color: str, expected: str) -> None:
    # Given
    palette = palette_for(ColorConstraints(max_colors=2))
    with Image.new("RGB", (16, 16), color) as image:
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == expected
    assert report.delta_e_threshold == 5


@pytest.mark.parametrize(
    ("total", "black", "expected"),
    [
        (6400, 0, "mismatch"),
        (6400, 31, "indeterminate"),
        (6400, 32, "pass"),
        (10000, 49, "indeterminate"),
        (10000, 50, "pass"),
    ],
)
@pytest.mark.parametrize("required", [False, True])
def test_required_presence_boundaries(
    total: int, black: int, expected: str, required: bool
) -> None:
    # Given
    constraints = (
        ColorConstraints(required_hex=("#000000",))
        if required
        else ColorConstraints(locked_hex=("#000000",))
    )
    palette = palette_for(constraints)
    with Image.new("RGB", (100, total // 100), "red") as image:
        for offset in range(black):
            image.putpixel((offset % 100, offset // 100), (0, 0, 0))
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == expected


@pytest.mark.parametrize(("partial", "expected"), [(100, "pass"), (101, "indeterminate")])
def test_partial_alpha_boundary(partial: int, expected: str) -> None:
    # Given
    palette = palette_for(ColorConstraints(max_colors=2))
    with Image.new("RGBA", (100, 10), (0, 0, 0, 250)) as image:
        for offset in range(partial):
            image.putpixel((offset % 100, offset // 100), (0, 0, 0, 249))
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == expected
    assert report.sampling.partial_alpha_samples == partial


@pytest.mark.parametrize(("count", "expected"), [(127, "indeterminate"), (128, "pass")])
def test_minimum_core_boundary(count: int, expected: str) -> None:
    # Given
    palette = palette_for(ColorConstraints(max_colors=2))
    with Image.new("RGB", (count, 1), "black") as image:
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == expected


@pytest.mark.parametrize(("red_count", "expected"), [(99, "pass"), (100, "mismatch")])
def test_observed_one_percent_boundary_preserves_minor_groups(
    red_count: int, expected: str
) -> None:
    # Given
    palette = palette_for(
        ColorConstraints(allowed_hex=("#000000", "#F6F3EC", "#FF0000"), max_colors=2)
    )
    with Image.new("RGB", (100, 100), "#F6F3EC") as image:
        image.paste("black", (0, 0, 50, 100))
        for offset in range(red_count):
            image.putpixel((offset % 100, offset // 100), (255, 0, 0))
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == expected
    assert report.observed_colors == (2 if red_count == 99 else 3)
    if red_count == 99:
        assert report.minor_swatches[0].hex == "#FF0000"


def test_roi_limits_scope_and_legacy_intent_stays_unverified() -> None:
    # Given
    with Image.new("RGB", (64, 32), "white") as image:
        data, artifact = source(image, None)
    # When
    report = analyze_png(
        data,
        artifact,
        None,
        report_id=ReportId("r1"),
        roi=RegionOfInterest(x=0, y=0, width=16, height=16),
    )
    # Then
    assert report.status == "unverified"
    assert report.sampling.scope == "roi"
    assert report.palette_id is None


def test_hash_mismatch_is_rejected() -> None:
    # Given
    palette = palette_for()
    with Image.new("RGB", (16, 16), "black") as image:
        data, artifact = source(image, palette)
    # When
    with pytest.raises(ProjectError, match="integrity"):
        _ = analyze_png(data + b"tampered", artifact, palette, report_id=ReportId("r1"))
    # Then
    assert hashlib.sha256(data).hexdigest() == artifact.sha256


def test_4096_image_stays_bounded_and_within_budget() -> None:
    # Given
    palette = palette_for(ColorConstraints(max_colors=2))
    with Image.new("RGBA", (4096, 4096), "black") as image:
        image.paste((0, 0, 0, 128), (0, 0, 1, 4096))
        data, artifact = source(image, palette)
    started = perf_counter()
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert perf_counter() - started < 30
    assert report.sampling.sampled_positions == 16384
    assert report.status == "pass"


def test_missing_engine_keeps_a_truthful_report(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given
    palette = palette_for(ColorConstraints(max_colors=2))
    with Image.new("RGB", (16, 16), "black") as image:
        data, artifact = source(image, palette)
    monkeypatch.setitem(sys.modules, "coloraide", None)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == "indeterminate"
    assert report.color_engine_version == "unavailable"
    assert report.matched_fraction is None
    assert "color_engine_unavailable" in report.reasons[0]


def test_partial_alpha_contrast_is_composited_on_explicit_surface() -> None:
    # Given
    palette = palette_for()
    with Image.new("RGBA", (16, 16), (0, 0, 0, 128)) as image:
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"), surfaces=("#FFFFFF",))
    # Then
    assert report.status == "indeterminate"
    assert len(report.contrasts) == 1
    assert report.contrasts[0].alpha == 128 / 255
    assert 3.9 < report.contrasts[0].ratio < 4.1


def test_transparent_hidden_red_cannot_fail_white_lettering() -> None:
    # Given
    palette = palette_for(ColorConstraints(allowed_hex=("#000000", "#F6F3EC", "#FFFFFF")))
    with Image.new("RGBA", (32, 16), (255, 0, 0, 0)) as image:
        image.paste((255, 255, 255, 255), (0, 0, 16, 16))
        data, artifact = source(image, palette)
    # When
    report = analyze_png(data, artifact, palette, report_id=ReportId("r1"))
    # Then
    assert report.status == "pass"
    assert report.measured_swatches[0].hex == "#FFFFFF"
    assert report.sampling.core_samples == 256
