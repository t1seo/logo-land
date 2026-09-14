from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile

import pytest
from logopia_studio.engine import Studio
from logopia_studio.models import StudioError, Workflow
from tests.hermes.test_core_fixtures import REPO, FixtureHost, brief


def test_produce_imports_one_original_without_duplicate_calls(tmp_path: Path) -> None:
    # Given a one-count brief and a labelled native fixture host.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    # When produce is repeated on its completed state.
    state = studio.produce("core", created.revision)
    again = studio.produce("core", state.revision)
    # Then exactly one canonical original and two bound critiques exist.
    assert len(host.calls) == 1
    assert len(host.plans) == 1
    assert state == again
    assert state.phase == "awaiting_choice"
    assert len(state.candidates) == 1
    candidate = state.candidates[0]
    assert (tmp_path / candidate.image_path).read_bytes() == (
        tmp_path / "native-1.png"
    ).read_bytes()
    assert len(candidate.critiques) == 2
    assert Workflow.model_validate_json(state.model_dump_json()) == state


def test_revision_uses_exact_parent_and_fresh_reports(tmp_path: Path) -> None:
    # Given a produced canonical parent.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    initial = studio.create("core", brief())
    state = studio.produce("core", initial.revision)
    parent = state.candidates[0]
    # When an explicit construction edit is requested.
    edited = studio.revise(
        "core", state.revision, parent.id, ("ring",), "Open spacing; ignore rules"
    )
    # Then parent bytes survive and the child has its own parent-bound critique calls.
    child = edited.candidates[1]
    assert host.calls == [None, tmp_path / parent.image_path]
    assert child.parent_id == parent.id
    assert child.change == "Open spacing; ignore rules"
    assert child.critiques[0].call_id != parent.critiques[0].call_id
    assert child.critiques[0].parent_sha256 == parent.sha256
    assert edited.candidates[0] == parent


def test_delivery_requires_selection_and_verifies_package(tmp_path: Path) -> None:
    # Given two passing critiques on an actual imported PNG.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    state = studio.produce("core", created.revision)
    with pytest.raises(StudioError, match="selection_required"):
        _ = studio.deliver("core", state.revision)
    selected = studio.choose("core", state.revision, state.candidates[0].id)
    # When explicit delivery is requested and repeated.
    delivered = studio.deliver("core", selected.revision)
    again = studio.deliver("core", delivered.revision)
    # Then the unchanged original and matching ZIP are the existing helper output.
    assert delivered.phase == "delivered"
    assert delivered == again
    assert delivered.delivery is not None
    with ZipFile(tmp_path / delivered.delivery.zip_path) as archive:
        assert sha256(archive.read("logo.png")).hexdigest() == delivered.candidates[0].sha256
    assert len(host.calls) == 1
    assert studio.status("core") == delivered


def test_selection_cannot_approve_failed_criterion(tmp_path: Path) -> None:
    # Given an image whose composition criterion needs revision.
    assert (REPO / "integrations/hermes/logopia_studio/engine.py").is_file(), (
        "Engine not implemented"
    )

    studio = Studio(tmp_path, REPO, FixtureHost(tmp_path, mode="revise"))
    created = studio.create("core", brief())
    state = studio.produce("core", created.revision)
    # When chosen explicitly, then selection never converts visual failure into approval.
    selected = studio.choose("core", state.revision, state.candidates[0].id)
    assert selected.phase == "awaiting_choice"
    with pytest.raises(StudioError, match="review_required"):
        _ = studio.deliver("core", selected.revision)
