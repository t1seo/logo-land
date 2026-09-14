from __future__ import annotations

import shutil
import signal
from pathlib import Path
from typing import TYPE_CHECKING, Final, Literal, assert_never

import pytest
from logopia_studio.installer import install_payload
from tests.hermes.test_installer_foreign_marker import SENTINEL

if TYPE_CHECKING:
    from tests.hermes.test_installer_foreign_marker import InstalledFixture

pytest_plugins: Final = ("tests.hermes.test_installer_foreign_marker",)


def snapshot(root: Path) -> tuple[tuple[str, bytes], ...]:
    return tuple(
        (path.relative_to(root).as_posix(), path.read_bytes())
        for path in sorted(root.rglob("*"))
        if path.is_file()
    )


def test_managed_update_pins_complete_installed_bytes(
    tmp_path: Path, installed: InstalledFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given literal source data and a complete managed installation.
    _ = (installed.source / "__init__.py").write_bytes(SENTINEL)
    original_rename = Path.rename
    staged: list[tuple[tuple[str, bytes], ...]] = []

    def observe_stage(path: Path, destination: str | Path) -> Path:
        if path.name == "new":
            staged.append(snapshot(path))
        return original_rename(path, destination)

    monkeypatch.setattr(Path, "rename", observe_stage)
    # When an explicit normal update publishes the replacement.
    receipt = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then every installed byte matches the full staged tree and source sentinel.
    assert staged == [snapshot(receipt.destination)]
    assert (receipt.destination / "__init__.py").read_bytes() == SENTINEL
    assert receipt.file_count == len(staged[0]) - 1
    assert list(installed.target.parent.iterdir()) == [installed.target]


@pytest.mark.parametrize("moved", [False, True], ids=["before-restore", "after-restore"])
@pytest.mark.parametrize("interrupt", [False, True], ids=["io", "sigint"])
def test_failed_restoration_keeps_original_error_and_old_payload(
    tmp_path: Path,
    installed: InstalledFixture,
    monkeypatch: pytest.MonkeyPatch,
    moved: bool,
    interrupt: bool,
) -> None:
    # Given a publication failure followed by an I/O error or SIGINT during restoration.
    before = snapshot(installed.target)
    original_rename = Path.rename
    failure = PermissionError("fixture publication failure")
    restore_failure = PermissionError("fixture restoration failure")
    backup_seen: list[Path] = []

    def fail_restoration(path: Path, destination: str | Path) -> Path:
        if path.name == "new":
            raise failure
        if path.name == "previous":
            backup_seen.append(path)
            assert snapshot(path) == before
            if moved:
                _ = original_rename(path, destination)
            if interrupt:
                signal.raise_signal(signal.SIGINT)
            raise restore_failure
        return original_rename(path, destination)

    monkeypatch.setattr(Path, "rename", fail_restoration)
    # When the bounded restoration attempt also fails.
    with pytest.raises(PermissionError) as raised:
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then the publication exception survives and the only old tree is never auto-deleted.
    assert raised.value is failure
    assert len(backup_seen) == 1
    backup = backup_seen[0]
    assert not (installed.target.parent / ".logopia-install.lock").exists()
    if moved:
        assert snapshot(installed.target) == before
        assert list(installed.target.parent.iterdir()) == [installed.target]
    else:
        assert not installed.target.exists()
        assert snapshot(backup) == before
        assert list(backup.parent.iterdir()) == [backup]
        assert list(installed.target.parent.iterdir()) == [backup.parent]
        assert any(str(backup) in note for note in raised.value.__notes__)


@pytest.mark.parametrize("kind", ["directory", "file", "symlink", "dangling"])
def test_foreign_target_and_old_backup_both_survive_first_rename_sigint(
    tmp_path: Path,
    installed: InstalledFixture,
    monkeypatch: pytest.MonkeyPatch,
    kind: Literal["directory", "file", "symlink", "dangling"],
) -> None:
    # Given an external fixture that occupies the destination after the real backup move.
    before = snapshot(installed.target)
    original_rename = Path.rename
    foreign = tmp_path / "foreign"
    _ = foreign.write_bytes(SENTINEL)
    absent = tmp_path / "absent"
    backups: list[Path] = []
    observed: list[KeyboardInterrupt] = []

    def occupy_and_interrupt(path: Path, destination: str | Path) -> Path:
        renamed = original_rename(path, destination)
        if path == installed.target and Path(destination).name == "previous":
            backups.append(renamed)
            assert snapshot(renamed) == before
            occupy_target(installed.target, foreign, absent, kind)
            try:
                signal.raise_signal(signal.SIGINT)
            except KeyboardInterrupt as error:
                observed.append(error)
                raise
        return renamed

    monkeypatch.setattr(Path, "rename", occupy_and_interrupt)
    # When SIGINT prevents completion and the target cannot safely be restored.
    with pytest.raises(KeyboardInterrupt) as raised:
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then exact old bytes remain at an identified recovery path beside untouched foreign data.
    assert raised.value is observed[0]
    assert len(backups) == 1
    backup = backups[0]
    assert snapshot(backup) == before
    assert list(backup.parent.iterdir()) == [backup]
    assert set(installed.target.parent.iterdir()) == {installed.target, backup.parent}
    assert any(str(backup) in note for note in raised.value.__notes__)
    assert foreign.read_bytes() == SENTINEL
    match kind:
        case "directory":
            assert snapshot(installed.target) == (("user.txt", SENTINEL),)
        case "file":
            assert installed.target.read_bytes() == SENTINEL
        case "symlink":
            assert installed.target.is_symlink()
            assert installed.target.readlink() == foreign
        case "dangling":
            assert installed.target.is_symlink()
            assert installed.target.readlink() == absent
            assert not absent.exists()
        case _:
            assert_never(kind)


def occupy_target(
    target: Path,
    foreign: Path,
    absent: Path,
    kind: Literal["directory", "file", "symlink", "dangling"],
) -> None:
    match kind:
        case "directory":
            target.mkdir()
            _ = (target / "user.txt").write_bytes(SENTINEL)
        case "file":
            _ = target.write_bytes(SENTINEL)
        case "symlink":
            target.symlink_to(foreign)
        case "dangling":
            target.symlink_to(absent)
        case _:
            assert_never(kind)


@pytest.mark.parametrize("first_rename", [True, False], ids=["backup", "publication"])
def test_sigint_restores_prior_bytes_then_allows_explicit_retry(
    tmp_path: Path,
    installed: InstalledFixture,
    monkeypatch: pytest.MonkeyPatch,
    first_rename: bool,
) -> None:
    # Given a managed install and a replacement whose first or second rename is interrupted.
    before = snapshot(installed.target)
    _ = (installed.source / "__init__.py").write_bytes(SENTINEL)
    source_before = snapshot(installed.source)
    original_rename = Path.rename
    observed: list[KeyboardInterrupt] = []
    backed_up: list[bool] = []

    def interrupt_boundary(path: Path, destination: str | Path) -> Path:
        at_backup = path == installed.target and Path(destination).name == "previous"
        at_publication = path.name == "new" and Path(destination) == installed.target
        if (first_rename and at_backup) or (not first_rename and at_publication):
            if first_rename:
                _ = original_rename(path, destination)
            backup = Path(destination) if first_rename else path.parent / "previous"
            backed_up.append(snapshot(backup) == before)
            try:
                signal.raise_signal(signal.SIGINT)
            except KeyboardInterrupt as error:
                observed.append(error)
                raise
        return original_rename(path, destination)

    # When two attempts receive real SIGINT after the old payload has moved.
    with monkeypatch.context() as patch:
        patch.setattr(Path, "rename", interrupt_boundary)
        for _ in range(2):
            with pytest.raises(KeyboardInterrupt) as raised:
                _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
            assert raised.value is observed[-1]
            assert snapshot(installed.target) == before
            assert list(installed.target.parent.iterdir()) == [installed.target]
    # Then prior bytes and literal source survive; an explicit normal update can publish.
    assert backed_up == [True, True]
    assert snapshot(installed.source) == source_before
    expected: list[tuple[tuple[str, bytes], ...]] = []

    def capture_update(path: Path, destination: str | Path) -> Path:
        if path.name == "new":
            expected.append(snapshot(path))
        return original_rename(path, destination)

    monkeypatch.setattr(Path, "rename", capture_update)
    receipt = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    assert expected == [snapshot(receipt.destination)]
    assert (receipt.destination / "__init__.py").read_bytes() == SENTINEL
    assert list(installed.target.parent.iterdir()) == [installed.target]


@pytest.mark.parametrize("interrupt", [False, True], ids=["io", "sigint"])
def test_cleanup_failure_cannot_delete_unrestored_backup(
    tmp_path: Path,
    installed: InstalledFixture,
    monkeypatch: pytest.MonkeyPatch,
    interrupt: bool,
) -> None:
    # Given publication and restoration failures plus a failing stage cleanup.
    before = snapshot(installed.target)
    rename = Path.rename
    failure = PermissionError("fixture publication failure")
    restore_failure = PermissionError("fixture restoration failure")
    cleanup_failure = PermissionError("fixture cleanup failure")
    backups: list[Path] = []

    def fail_publication_and_restore(path: Path, destination: str | Path) -> Path:
        if path.name == "new":
            raise failure
        if path.name == "previous":
            backups.append(path)
            raise restore_failure
        return rename(path, destination)

    def fail_cleanup(path: Path) -> None:
        assert path.name == "new"
        if interrupt:
            signal.raise_signal(signal.SIGINT)
        raise cleanup_failure

    monkeypatch.setattr(Path, "rename", fail_publication_and_restore)
    monkeypatch.setattr(shutil, "rmtree", fail_cleanup)
    # When even discarding the unpublished stage is interrupted or denied.
    with pytest.raises(PermissionError) as raised:
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then the original exception identifies exact retained old bytes and unfinished cleanup.
    assert raised.value is failure
    assert len(backups) == 1
    assert snapshot(backups[0]) == before
    assert not (installed.target.parent / ".logopia-install.lock").exists()
    assert any(str(backups[0]) in note for note in raised.value.__notes__)
    assert any("cleanup failed" in note for note in raised.value.__notes__)
