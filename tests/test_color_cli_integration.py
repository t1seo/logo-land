from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from logo_helper.models import PaletteContent, ReferenceId, Session, SourceEvidence, Swatch
from logo_helper.palette_proposals import ProposalResult
from tests.test_palette_workflow import add_palette

if TYPE_CHECKING:
    from tests.conftest import Harness


def reference(harness: Harness) -> Session:
    return Session.model_validate_json(
        harness.ok(
            "reference-add",
            "--session",
            "demo",
            "--reference",
            "photo",
            "--image",
            str(harness.png),
            "--revision",
            "0",
        )
    )


def test_reference_when_external_source_moves(harness: Harness) -> None:
    # Given a recorded reference whose external source is subsequently moved.
    harness.init()
    state = reference(harness)
    _ = harness.png.rename(harness.png.with_name("moved.png"))
    request = harness.workspace / "request.json"
    _ = request.write_text('{"constraints":{"locked_hex":["#247A52"],"max_colors":2}}')
    before = harness.state_path.read_bytes()
    # When proposing from the immutable session-local copy.
    result = ProposalResult.model_validate_json(
        harness.ok(
            "palette-propose",
            "--session",
            "demo",
            "--reference",
            "photo",
            "--request-file",
            str(request),
        )
    )
    # Then actual extraction and hash provenance accompany the composed constraints.
    assert result.extraction is not None
    assert result.extraction.sampling.core_samples == 255
    assert result.candidates[0].source_evidence.reference_sha256 == state.references[0].sha256
    assert result.candidates[0].swatches[0].hex == "#247A52"
    assert result.candidates[0].source_evidence.response == result.extraction.model_dump_json()
    assert harness.state_path.read_bytes() == before


@pytest.mark.parametrize("identifier", ["../outside", "photo"])
def test_reference_when_id_is_unsafe_or_duplicate(harness: Harness, identifier: str) -> None:
    # Given an existing immutable reference.
    harness.init()
    _ = reference(harness)
    before = harness.state_path.read_bytes()
    # When a duplicate or escaping identifier is used.
    result = harness.run(
        "reference-add",
        "--session",
        "demo",
        "--reference",
        identifier,
        "--image",
        str(harness.png),
        "--revision",
        "1",
    )
    # Then state and original reference remain intact.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
    assert (
        harness.state_path.parent / "references/photo.png"
    ).read_bytes() == harness.png.read_bytes()


def test_reference_when_managed_directory_is_symlink(harness: Harness) -> None:
    # Given a reference path redirected outside managed storage.
    harness.init()
    (harness.state_path.parent / "references").symlink_to(
        harness.workspace, target_is_directory=True
    )
    before = harness.state_path.read_bytes()
    # When importing a valid reference.
    result = harness.run(
        "reference-add",
        "--session",
        "demo",
        "--reference",
        "photo",
        "--image",
        str(harness.png),
        "--revision",
        "0",
    )
    # Then no file escapes or state is committed.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "photo.png").exists()


def test_color_analyze_when_report_is_appended(harness: Harness) -> None:
    # Given an imported image with initial palette evidence.
    harness.init()
    _ = add_palette(harness, "green", 0, "#247A52")
    before = Session.model_validate_json(harness.import_image(1))
    # When a fresh real analysis is requested.
    state = Session.model_validate_json(
        harness.ok(
            "color-analyze",
            "--session",
            "demo",
            "--artifact",
            "v1",
            "--revision",
            "2",
        )
    )
    # Then prior evidence remains and a fresh bound report is appended.
    assert state.color_reports[:-1] == before.color_reports
    assert state.color_reports[-1].id != before.color_reports[0].id
    assert state.color_reports[-1].artifact_sha256 == before.artifacts[0].sha256
    assert state.revision == 3


@pytest.mark.parametrize("roi_json", ['{"passed":true}', '{"x":0,"y":0,"width":99,"height":1}'])
def test_color_analyze_when_roi_is_invalid(harness: Harness, roi_json: str) -> None:
    # Given an imported image and malformed/out-of-bounds sampling instructions.
    harness.init()
    _ = harness.import_image()
    roi = harness.workspace / "roi.json"
    _ = roi.write_text(roi_json)
    before = harness.state_path.read_bytes()
    # When invalid analysis is requested.
    result = harness.run(
        "color-analyze",
        "--session",
        "demo",
        "--artifact",
        "v1",
        "--revision",
        "1",
        "--roi-file",
        str(roi),
    )
    # Then no caller-supplied pass or invalid scope enters stored evidence.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before


def test_gallery_when_read_only(harness: Harness) -> None:
    # Given a selected explicit image list.
    harness.init()
    _ = harness.import_image()
    before = harness.state_path.read_bytes()
    # When rendering through the real CLI.
    _ = harness.ok(
        "color-gallery",
        "--session",
        "demo",
        "--artifacts",
        "v1",
        "--output",
        "output/color-galleries/demo",
    )
    # Then a portable page contains the same original PNG without session writes.
    output = harness.workspace / "output/color-galleries/demo"
    assert (output / "index.html").is_file()
    assert (output / "images/v1.png").read_bytes() == harness.png.read_bytes()
    assert harness.state_path.read_bytes() == before


def test_palette_when_fabricated_reference_evidence(harness: Harness) -> None:
    # Given a candidate claiming fabricated extraction from a real reference hash.
    harness.init()
    state = reference(harness)
    ref = state.reference(ReferenceId("photo"))
    candidate = harness.workspace / "candidate.json"
    _ = candidate.write_text(
        PaletteContent(
            swatches=(Swatch(hex="#000000", role="primary"),),
            source="reference",
            selected_by="assistant",
            rationale="Fixture",
            source_evidence=SourceEvidence(
                reference_id=ref.id,
                reference_sha256=ref.sha256,
                response="invented extraction",
            ),
        ).model_dump_json()
    )
    before = harness.state_path.read_bytes()
    # When the fabricated evidence crosses the palette persistence boundary.
    result = harness.run(
        "palette-add",
        "--session",
        "demo",
        "--palette",
        "fake",
        "--palette-file",
        str(candidate),
        "--revision",
        "1",
    )
    # Then actual-byte provenance cannot be replaced by a caller claim.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
