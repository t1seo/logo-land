from pathlib import Path

import pytest
from logopia_studio.engine import Studio
from logopia_studio.helper import HelperBridge
from logopia_studio.helper_models import HelperSession
from logopia_studio.models import StudioError
from tests.hermes.test_core_fixtures import REPO, FixtureHost, brief


def test_import_commit_reconciles_without_new_image(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given a helper import that commits successfully before the bridge loses its reply.
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    original = HelperBridge.invoke
    calls: list[str] = []

    def lost_reply(bridge: HelperBridge, *args: str) -> HelperSession:
        session = original(bridge, *args)
        if args[0] == "import" and not calls:
            calls.append(args[0])
            raise StudioError("helper_timeout", "Fixture interrupted after committed import")
        return session

    monkeypatch.setattr(HelperBridge, "invoke", lost_reply)
    interrupted = studio.produce("core", created.revision)
    assert interrupted.phase == "outcome_unknown"
    assert interrupted.candidates == ()
    # When the exact saved image job is reconciled and production explicitly continued.
    recovered = studio.reconcile("core", interrupted.revision, interrupted.jobs[-1].id)
    finished = studio.produce("core", recovered.revision)
    # Then the committed original is adopted once and only a critique pair runs.
    assert len(host.calls) == 1
    assert len(finished.candidates) == 1
    assert finished.phase == "awaiting_choice"
    assert calls == ["import"]


def test_export_commit_reconciles_without_duplicate_package(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given a fully reviewed selected original and a lost export reply after helper commit.
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    produced = studio.produce("core", created.revision)
    chosen = studio.choose("core", produced.revision, produced.candidates[0].id)
    original = HelperBridge.invoke
    exports: list[str] = []

    def lost_reply(bridge: HelperBridge, *args: str) -> HelperSession:
        session = original(bridge, *args)
        if args[0] == "export":
            exports.append(args[0])
            raise StudioError("helper_timeout", "Fixture interrupted after committed export")
        return session

    monkeypatch.setattr(HelperBridge, "invoke", lost_reply)
    interrupted = studio.deliver("core", chosen.revision)
    assert interrupted.delivery is None
    # When the exact export job is reconciled and delivery is repeated.
    recovered = studio.reconcile("core", interrupted.revision, interrupted.jobs[-1].id)
    delivered = studio.deliver("core", recovered.revision)
    # Then the helper record and package are verified without repeating export.
    assert delivered.delivery is not None
    assert delivered.phase == "delivered"
    assert exports == ["export"]
    assert len(host.calls) == 1


def test_foreign_output_is_preserved(tmp_path: Path) -> None:
    # Given foreign files at the deterministic export destination.
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief())
    produced = studio.produce("core", created.revision)
    chosen = studio.choose("core", produced.revision, produced.candidates[0].id)
    target = tmp_path / "output/logopia/core"
    target.mkdir(parents=True)
    sentinel = target / "foreign.txt"
    _ = sentinel.write_bytes(b"foreign work")
    # When delivery encounters the collision, then it fails and preserves the sentinel.
    result = studio.deliver("core", chosen.revision)
    assert result.delivery is None
    assert result.phase == "failed"
    assert sentinel.read_bytes() == b"foreign work"


def test_missing_import_file_cannot_be_success(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given a real helper import reply whose original disappears before core acceptance.
    studio = Studio(tmp_path, REPO, FixtureHost(tmp_path))
    created = studio.create("core", brief())
    original = HelperBridge.invoke

    def misleading(bridge: HelperBridge, *args: str) -> HelperSession:
        session = original(bridge, *args)
        if args[0] == "import":
            (
                bridge.root
                / f".logo-generator/sessions/{session.id}/artifacts/{session.artifacts[0].id}.png"
            ).unlink()
        return session

    monkeypatch.setattr(HelperBridge, "invoke", misleading)
    # When core consumes that success, then it rejects the absent canonical original.
    result = studio.produce("core", created.revision)
    assert result.candidates == ()
    assert result.phase == "failed"


def test_helper_background_gate_remains_authoritative(tmp_path: Path) -> None:
    # Given a fixture critic passing a PNG that lacks the requested transparency.
    host = FixtureHost(tmp_path)
    studio = Studio(tmp_path, REPO, host)
    created = studio.create("core", brief().model_copy(update={"background": "transparent"}))
    produced = studio.produce("core", created.revision)
    selected = studio.choose("core", produced.revision, produced.candidates[0].id)
    assert selected.phase == "ready"
    # When delivery reaches the existing helper, then decoded background facts block export.
    delivered = studio.deliver("core", selected.revision)
    assert delivered.phase == "failed"
    assert delivered.delivery is None
    assert delivered.last_error is not None
    assert "background_mismatch" in delivered.last_error
    assert not (tmp_path / "output/logopia/core").exists()
