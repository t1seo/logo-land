from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from logopia_studio.installer import install_payload
from logopia_studio.launcher_process import LaunchError

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def plugin_source(tmp_path: Path) -> Path:
    source = tmp_path / "source"
    source.mkdir()
    _ = (source / "plugin.yaml").write_text("name: logopia-studio\n", encoding="utf-8")
    _ = (source / "__init__.py").write_text("fixture = True\n", encoding="utf-8")
    package = source / "logopia_studio"
    package.mkdir()
    _ = (package / "__init__.py").write_text("", encoding="utf-8")
    _ = (source / "settings.json").write_text("private source settings", encoding="utf-8")
    return source


def test_install_copies_payload_and_owns_only_its_plugin(
    tmp_path: Path,
    plugin_source: Path,
) -> None:
    profile = tmp_path / "profiles/logopia"
    profile.mkdir(parents=True)
    config = profile / "config.yaml"
    _ = config.write_text("model: unchanged\n", encoding="utf-8")
    result = install_payload(plugin_source, profile, tmp_path, tmp_path)
    assert result.destination == profile / "plugins/logopia-studio"
    original = (plugin_source / "plugin.yaml").read_bytes()
    assert (result.destination / "plugin.yaml").read_bytes() == original
    assert "private source settings" not in (result.destination / "settings.json").read_text()
    assert config.read_text(encoding="utf-8") == "model: unchanged\n"
    assert result.file_count == 4


def test_managed_update_is_idempotent_and_preserves_user_config(
    tmp_path: Path,
    plugin_source: Path,
) -> None:
    profile = tmp_path / "logopia"
    profile.mkdir()
    first = install_payload(plugin_source, profile, tmp_path, tmp_path)
    _ = (plugin_source / "__init__.py").write_text("fixture = False\n", encoding="utf-8")
    second = install_payload(plugin_source, profile, tmp_path, tmp_path)
    assert second.destination == first.destination
    assert (second.destination / "__init__.py").read_text() == "fixture = False\n"
    assert list((profile / "plugins").iterdir()) == [second.destination]


def test_unmanaged_plugin_is_preserved(tmp_path: Path, plugin_source: Path) -> None:
    profile = tmp_path / "logopia"
    target = profile / "plugins/logopia-studio"
    target.mkdir(parents=True)
    _ = (target / "user.txt").write_text("keep", encoding="utf-8")
    with pytest.raises(LaunchError, match="unmanaged_install"):
        _ = install_payload(plugin_source, profile, tmp_path, tmp_path)
    assert (target / "user.txt").read_text() == "keep"


def test_edited_managed_payload_is_preserved(tmp_path: Path, plugin_source: Path) -> None:
    profile = tmp_path / "logopia"
    profile.mkdir()
    target = install_payload(plugin_source, profile, tmp_path, tmp_path).destination
    _ = (target / "__init__.py").write_text("user modification\n", encoding="utf-8")
    with pytest.raises(LaunchError, match="modified_install"):
        _ = install_payload(plugin_source, profile, tmp_path, tmp_path)
    assert (target / "__init__.py").read_text() == "user modification\n"


def test_source_symlink_is_rejected(tmp_path: Path, plugin_source: Path) -> None:
    profile = tmp_path / "logopia"
    profile.mkdir()
    foreign = tmp_path / "foreign.py"
    _ = foreign.write_text("private = True", encoding="utf-8")
    (plugin_source / "logopia_studio/foreign.py").symlink_to(foreign)
    with pytest.raises(LaunchError, match="unsafe_payload"):
        _ = install_payload(plugin_source, profile, tmp_path, tmp_path)
    assert not (profile / "plugins/logopia-studio").exists()
