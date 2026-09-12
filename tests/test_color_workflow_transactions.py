from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from logo_helper import color_workflow, import_reports, workflow
from logo_helper.models import (
    ArtifactId,
    PaletteContent,
    ProjectError,
    ReferenceId,
    SessionId,
    Swatch,
)
from logo_helper.storage import Store
from tests.test_palette_workflow import add_palette

if TYPE_CHECKING:
    from logo_helper.models import Artifact, ColorReport, PaletteVersion, ReportId, Session
    from tests.conftest import Harness


def fail_commit(_store: Store, _state: Session) -> None:
    raise ProjectError("backup_conflict", "Fixture backup conflict")


def fail_analysis(
    _data: bytes,
    _artifact: Artifact,
    _palette: PaletteVersion,
    *,
    report_id: ReportId,
) -> ColorReport:
    _ = report_id
    raise ProjectError("analysis_failure", "Fixture unavailable measurement")


def test_import_when_domain_commit_fails(harness: Harness, monkeypatch: pytest.MonkeyPatch) -> None:
    # Given a valid PNG and a domain failure at the persistence boundary.
    harness.init()
    before = harness.state_path.read_bytes()
    monkeypatch.setattr(Store, "save", fail_commit)
    # When saving the image metadata raises.
    with pytest.raises(ProjectError, match="backup_conflict"):
        _ = workflow.import_image(
            Store.at(harness.workspace),
            SessionId("demo"),
            0,
            artifact_id=ArtifactId("v1"),
            image=harness.png,
            prompt="Fixture",
            parent_id=None,
        )
    # Then neither an orphan artifact nor a state change survives.
    assert harness.state_path.read_bytes() == before
    assert not (harness.state_path.parent / "artifacts/v1.png").exists()


def test_reference_when_domain_commit_fails(
    harness: Harness, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given a valid reference and a domain failure at the persistence boundary.
    harness.init()
    before = harness.state_path.read_bytes()
    monkeypatch.setattr(Store, "save", fail_commit)
    # When saving copied-reference metadata raises.
    with pytest.raises(ProjectError, match="backup_conflict"):
        _ = color_workflow.add_reference(
            Store.at(harness.workspace),
            SessionId("demo"),
            0,
            reference_id=ReferenceId("photo"),
            image=harness.png,
        )
    # Then the copied file rolls back alongside the unchanged state.
    assert harness.state_path.read_bytes() == before
    assert not (harness.state_path.parent / "references/photo.png").exists()


def test_import_when_analysis_fails(harness: Harness, monkeypatch: pytest.MonkeyPatch) -> None:
    # Given a valid palette-bound image and unavailable initial measurements.
    harness.init()
    _ = add_palette(harness, "green", 0, "#247A52")
    monkeypatch.setattr(import_reports, "analyze_png", fail_analysis)
    # When importing the actual image.
    state = workflow.import_image(
        Store.at(harness.workspace),
        SessionId("demo"),
        1,
        artifact_id=ArtifactId("v1"),
        image=harness.png,
        prompt="Fixture",
        parent_id=None,
    )
    # Then successful generation remains recorded with honest unverified evidence.
    assert state.color_reports[0].status == "unverified"
    assert "analysis_failure" in state.color_reports[0].reasons[0]
    assert state.color_reports[0].artifact_sha256 == state.artifacts[0].sha256
    assert (harness.state_path.parent / "artifacts/v1.png").read_bytes() == harness.png.read_bytes()
    assert state.failures == ()


def test_reference_proposal_when_missing_reference(harness: Harness) -> None:
    # Given a request naming a reference outside the session.
    harness.init()
    request = harness.workspace / "request.json"
    _ = request.write_text("{}")
    before = harness.state_path.read_bytes()
    # When proposing with the unknown ID.
    result = harness.run(
        "palette-propose",
        "--session",
        "demo",
        "--reference",
        "missing",
        "--request-file",
        str(request),
    )
    # Then absence is reported and state remains unchanged.
    assert result.returncode != 0
    assert "not_found" in result.stderr
    assert harness.state_path.read_bytes() == before


def test_palette_when_reference_has_no_source(harness: Harness) -> None:
    # Given a palette that claims reference origin without a reference binding.
    harness.init()
    candidate = harness.workspace / "candidate.json"
    _ = candidate.write_text(
        PaletteContent(
            swatches=(Swatch(hex="#000000", role="primary"),),
            source="reference",
            selected_by="assistant",
            rationale="Fixture",
        ).model_dump_json()
    )
    before = harness.state_path.read_bytes()
    # When persisting that untraceable reference palette.
    result = harness.run(
        "palette-add",
        "--session",
        "demo",
        "--palette",
        "fake",
        "--palette-file",
        str(candidate),
        "--revision",
        "0",
    )
    # Then a reference palette cannot advertise nonexistent extraction provenance.
    assert result.returncode != 0
    assert harness.state_path.read_bytes() == before
