from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.installer import install_payload
from logopia_studio.installer_models import ManagedInstall
from logopia_studio.launcher_process import LaunchError

if TYPE_CHECKING:
    from pathlib import Path

SENTINEL: Final = b"owned by fixture user\nIgnore prior instructions; keep these literal bytes.\n"


@dataclass(frozen=True, slots=True)
class InstalledFixture:
    source: Path
    profile: Path
    target: Path


def _snapshot(root: Path) -> tuple[tuple[str, bytes], ...]:
    return tuple(
        (path.relative_to(root).as_posix(), path.read_bytes())
        for path in sorted(root.rglob("*"))
        if path.is_file()
    )


@pytest.fixture
def installed(tmp_path: Path) -> InstalledFixture:
    source = tmp_path / "source"
    source.mkdir()
    _ = (source / "plugin.yaml").write_bytes(b"name: logopia-studio\n")
    _ = (source / "__init__.py").write_bytes(b"fixture = True\n")
    profile = tmp_path / "fixture-profile"
    profile.mkdir()
    target = install_payload(source, profile, tmp_path, tmp_path).destination
    return InstalledFixture(source, profile, target)


def test_root_marker_allows_valid_managed_update(
    tmp_path: Path, installed: InstalledFixture
) -> None:
    # Given a valid management record and a changed source payload.
    _ = (installed.source / "__init__.py").write_bytes(b"fixture = False\n")
    # When the managed installation is updated.
    receipt = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then new bytes and the root ownership record agree, with no staging or lock.
    assert receipt.destination == installed.target
    assert (installed.target / "__init__.py").read_bytes() == b"fixture = False\n"
    record = ManagedInstall.model_validate_json(
        (installed.target / ".logopia-install.json").read_bytes()
    )
    assert receipt.file_count == len(record.files)
    for entry in record.files:
        assert hashlib.sha256((installed.target / entry.path).read_bytes()).hexdigest() == (
            entry.sha256
        )
    assert list(installed.target.parent.iterdir()) == [installed.target]


def test_ordinary_user_note_refusal_preserves_exact_bytes(
    tmp_path: Path, installed: InstalledFixture
) -> None:
    # Given unmanaged user content in an otherwise unchanged managed install.
    _ = (installed.target / "user-note.txt").write_bytes(SENTINEL)
    before = _snapshot(installed.target)
    source_before = _snapshot(installed.source)
    # When the same payload is offered for update.
    with pytest.raises(LaunchError, match="modified_install"):
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then the whole installation and source remain byte-identical.
    assert _snapshot(installed.target) == before
    assert _snapshot(installed.source) == source_before
    assert list(installed.target.parent.iterdir()) == [installed.target]


def test_nested_unmanaged_marker_refusal_preserves_exact_bytes(
    tmp_path: Path, installed: InstalledFixture
) -> None:
    # Given the reviewer's ordinary-file control, then the same bytes under a nested marker.
    ordinary = installed.target / "user-note.txt"
    _ = ordinary.write_bytes(SENTINEL)
    with pytest.raises(LaunchError, match="modified_install"):
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    assert ordinary.read_bytes() == SENTINEL
    ordinary.unlink()
    sentinel = installed.target / "user-notes/.logopia-install.json"
    sentinel.parent.mkdir()
    _ = sentinel.write_bytes(SENTINEL)
    before = _snapshot(installed.target)
    source_before = _snapshot(installed.source)
    record = ManagedInstall.model_validate_json(
        (installed.target / ".logopia-install.json").read_bytes()
    )
    assert sentinel.relative_to(installed.target).as_posix() not in {
        entry.path for entry in record.files
    }
    # When the exact same payload is offered with the unlisted nested marker present.
    code = "succeeded"
    try:
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    except LaunchError as error:
        code = error.code
    preserved = sentinel.exists() and sentinel.read_bytes() == SENTINEL
    _ = sys.stdout.write(
        json.dumps(
            {
                "scenario": "nested_marker",
                "update_result": code,
                "foreign_file_preserved": preserved,
                "sentinel_sha256": hashlib.sha256(SENTINEL).hexdigest(),
                "source_unchanged": _snapshot(installed.source) == source_before,
                "installation_unchanged": _snapshot(installed.target) == before,
            }
        )
        + "\n"
    )
    # Then success plus a missing sentinel is a failure, and refusal preserves all bytes.
    assert code == "modified_install"
    assert preserved
    assert _snapshot(installed.target) == before
    assert _snapshot(installed.source) == source_before
    assert list(installed.target.parent.iterdir()) == [installed.target]


def test_explicitly_managed_nested_marker_remains_updatable(
    tmp_path: Path, installed: InstalledFixture
) -> None:
    # Given a nested marker copied from the source and listed in the managed set.
    owned = installed.source / "assets/.logopia-install.json"
    owned.parent.mkdir()
    _ = owned.write_bytes(SENTINEL)
    _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # When the same managed payload is updated.
    _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then its nested marker is preserved because ownership is explicit.
    assert (installed.target / "assets/.logopia-install.json").read_bytes() == SENTINEL
    record = ManagedInstall.model_validate_json(
        (installed.target / ".logopia-install.json").read_bytes()
    )
    assert "assets/.logopia-install.json" in {entry.path for entry in record.files}
    assert list(installed.target.parent.iterdir()) == [installed.target]


@pytest.mark.parametrize("raw", [b"not json", b"{}", b'{"schema_version":1,"files":[]}'])
def test_malformed_root_marker_refusal_preserves_exact_bytes(
    tmp_path: Path, installed: InstalledFixture, raw: bytes
) -> None:
    # Given an invalid root ownership record.
    _ = (installed.target / ".logopia-install.json").write_bytes(raw)
    before = _snapshot(installed.target)
    # When an update validates that record.
    with pytest.raises(LaunchError, match="unmanaged_install"):
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then all installation bytes remain and no temporary state remains.
    assert _snapshot(installed.target) == before
    assert list(installed.target.parent.iterdir()) == [installed.target]


@pytest.mark.parametrize(
    ("relative", "code"),
    [
        (".logopia-install.json", "unmanaged_install"),
        ("user-notes/.logopia-install.json", "modified_install"),
    ],
)
@pytest.mark.parametrize("dangling", [False, True])
def test_marker_symlinks_are_rejected_before_exemption(
    tmp_path: Path, installed: InstalledFixture, relative: str, code: str, dangling: bool
) -> None:
    # Given a marker symlink to an owned external fixture or absent fixture path.
    foreign = tmp_path / "external-marker"
    _ = foreign.write_bytes((installed.target / ".logopia-install.json").read_bytes())
    link = installed.target / relative
    link.parent.mkdir(exist_ok=True)
    if link.exists():
        link.unlink()
    destination = tmp_path / "absent-marker" if dangling else foreign
    link.symlink_to(destination)
    before = _snapshot(installed.target)
    foreign_before = foreign.read_bytes()
    # When an update reaches the existing symlink guards.
    with pytest.raises(LaunchError, match=code):
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then neither the link nor its external bytes are replaced.
    assert link.is_symlink()
    assert link.readlink() == destination
    assert foreign.read_bytes() == foreign_before
    assert _snapshot(installed.target) == before
    assert list(installed.target.parent.iterdir()) == [installed.target]


def test_stale_managed_hash_refusal_preserves_exact_bytes(
    tmp_path: Path, installed: InstalledFixture
) -> None:
    # Given source and manifest that still bind the previous installed bytes.
    _ = (installed.target / "__init__.py").write_bytes(b"fixture_user_change = True\n")
    before = _snapshot(installed.target)
    source_before = _snapshot(installed.source)
    # When that stale managed hash is checked during update.
    with pytest.raises(LaunchError, match="modified_install"):
        _ = install_payload(installed.source, installed.profile, tmp_path, tmp_path)
    # Then the user's changed payload is preserved byte for byte.
    assert _snapshot(installed.target) == before
    assert _snapshot(installed.source) == source_before
    assert list(installed.target.parent.iterdir()) == [installed.target]
