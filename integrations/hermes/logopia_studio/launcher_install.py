"""Install with finite native tool deadlines in an explicit named Hermes profile."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import uuid4

from .installer import install_payload
from .launcher_output import CommandResult
from .launcher_process import LaunchError, run_process
from .launcher_profile import profile_lock, profile_path
from .store_files import safe_path

if TYPE_CHECKING:
    from pathlib import Path


def install_profile(
    profile: str,
    profile_home: Path | None,
    workspace: Path,
    source: Path,
    helper_repo: Path,
) -> CommandResult:
    home = profile_path(profile, profile_home)
    root = workspace.resolve(strict=True)
    if not root.is_dir():
        raise LaunchError("invalid_workspace", "--workspace must be an existing directory")
    with profile_lock(home):
        installed = install_payload(source, home, root, helper_repo)
        logs = safe_path(root, f"output/logopia-runs/install-{uuid4().hex}")
        commands = (
            (
                "doctor",
                ("hermes", "-p", profile, "plugins", "doctor", str(installed.destination), "--ci"),
                "doctor",
            ),
            (
                "sequential_call",
                (
                    "hermes",
                    "-p",
                    profile,
                    "config",
                    "set",
                    "timeouts.tools.sequential_call",
                    "1800",
                ),
                "set timeouts.tools.sequential_call=1800",
            ),
            (
                "concurrent_batch",
                (
                    "hermes",
                    "-p",
                    profile,
                    "config",
                    "set",
                    "timeouts.tools.concurrent_batch",
                    "1800",
                ),
                "set timeouts.tools.concurrent_batch=1800",
            ),
            (
                "enable",
                (
                    "hermes",
                    "-p",
                    profile,
                    "plugins",
                    "enable",
                    "logopia-studio",
                    "--no-allow-tool-override",
                ),
                "enable",
            ),
        )
        for name, command, operation in commands:
            receipt = run_process(command, root, logs / name, 120)
            if receipt.exit_code != 0 or receipt.timed_out or receipt.interrupted:
                return CommandResult(
                    success=False,
                    error=f"{name}_failed",
                    logs=str(logs),
                    installation=str(installed.destination),
                    message=f"Plugin copied; Hermes {operation} failed. Inspect process logs.",
                )
        return CommandResult(
            success=True,
            message="\n".join(
                (
                    f"Logopia installed, doctor checked and enabled in named profile {profile}.",
                    "timeouts.tools.sequential_call=1800 seconds",
                    "timeouts.tools.concurrent_batch=1800 seconds",
                )
            ),
            installation=str(installed.destination),
            logs=str(logs),
        )
