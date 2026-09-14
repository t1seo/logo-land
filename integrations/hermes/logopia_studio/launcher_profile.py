"""Bind explicit named profiles and serialize owned macOS/Linux CLI launches."""

from __future__ import annotations

import fcntl
import os
import stat
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING

from .host_settings import HostSettings, load_settings
from .launcher_process import LaunchError, validate_profile

if TYPE_CHECKING:
    from collections.abc import Generator


def profile_path(profile: str, explicit: Path | None) -> Path:
    name = validate_profile(profile)
    standard = Path.home() / ".hermes" / "profiles" / name
    path = standard if explicit is None else explicit.expanduser()
    if not path.is_absolute() or path.name != name or path.parent.name != "profiles":
        raise LaunchError("invalid_profile_home", "Use an absolute profiles/NAME directory")
    environment = os.environ.get("HERMES_HOME", "").strip()
    root = Path(environment).expanduser() if environment else standard.parent.parent
    if root.parent.name == "profiles":
        root = root.parent.parent
    if not root.is_absolute() or root / "profiles" / name != path:
        raise LaunchError(
            "profile_home_mismatch",
            "HERMES_HOME routing differs; supply its exact profiles/NAME with --profile-home",
        )
    if not path.is_dir():
        raise LaunchError("missing_profile", f"Create it first: hermes profile create {name}")
    if any(part.is_symlink() for part in (path, path.parent, path.parent.parent)):
        raise LaunchError("unsafe_profile", "Profile and Hermes root must not be symlinks")
    return path


@contextmanager
def profile_lock(profile: Path) -> Generator[None, None, None]:
    path = profile / ".logopia-launch.lock"
    descriptor = os.open(path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW | os.O_CLOEXEC, 0o600)
    with os.fdopen(descriptor, "a+b") as stream:
        metadata = os.fstat(stream.fileno())
        if not stat.S_ISREG(metadata.st_mode) or metadata.st_nlink != 1:
            raise LaunchError("unsafe_profile", "Profile lock must be an unlinked regular file")
        try:
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise LaunchError(
                "profile_busy", "Another Logopia launcher holds this profile"
            ) from error
        try:
            yield
        finally:
            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
    # Keep the inode: unlinking allows a waiter and a new opener to hold different locks.


def installed_settings(profile: Path, workspace: Path | None) -> HostSettings:
    plugin = profile / "plugins" / "logopia-studio"
    if any(path.is_symlink() for path in (plugin.parent, plugin, plugin / "settings.json")):
        raise LaunchError("unsafe_profile", "Installed settings must not traverse symlinks")
    settings = load_settings(plugin)
    if workspace is not None and workspace.resolve() != settings.workspace.resolve():
        raise LaunchError("workspace_mismatch", "--workspace differs from installed settings.json")
    return settings
