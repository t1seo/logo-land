from __future__ import annotations

import subprocess
import sys
from typing import TYPE_CHECKING

import pytest
from logopia_studio.launcher_process import LaunchError, hermes_command, run_process

if TYPE_CHECKING:
    from pathlib import Path


def test_command_preserves_query_file_and_workspace(tmp_path: Path) -> None:
    query = tmp_path / "한글 brief with spaces.txt"
    assert hermes_command("logopia", query, tmp_path) == (
        "hermes",
        "-p",
        "logopia",
        "chat",
        "--cli",
        "--quiet",
        "--oneshot",
        "--query-file",
        str(query),
        "--in",
        str(tmp_path),
        "--no-restore-cwd",
        "--toolsets",
        "logopia-studio,image_gen",
        "--skills",
        "logopia-studio:director",
        "--max-turns",
        "6",
        "--run-budget",
        "1800",
    )


@pytest.mark.parametrize("profile", ["default", "../default", "name with spaces", ""])
def test_command_rejects_invalid_or_default_profile(profile: str, tmp_path: Path) -> None:
    with pytest.raises(LaunchError, match="invalid_profile"):
        _ = hermes_command(profile, tmp_path / "request.txt", tmp_path)


def test_actual_child_logs_are_retained(tmp_path: Path) -> None:
    result = run_process(
        (sys.executable, "-c", 'print("MODEL_FINAL_ONLY")'),
        tmp_path,
        tmp_path / "run",
        timeout_seconds=5,
    )
    assert result.exit_code == 0
    assert result.timed_out is False
    assert result.stdout_path.read_text(encoding="utf-8") == "MODEL_FINAL_ONLY\n"
    assert result.stderr_path.read_bytes() == b""


def test_deadline_settles_only_the_owned_process(tmp_path: Path) -> None:
    result = run_process(
        (sys.executable, "-c", "import time; time.sleep(30)"),
        tmp_path,
        tmp_path / "run",
        timeout_seconds=1,
        grace_seconds=0.2,
    )
    assert result.timed_out is True
    assert result.exit_code != 0
    assert result.interrupted is False


def test_existing_logs_are_never_overwritten(tmp_path: Path) -> None:
    output = tmp_path / "run"
    output.mkdir()
    sentinel = output / "keep.txt"
    _ = sentinel.write_text("another task", encoding="utf-8")
    with pytest.raises(LaunchError, match="output_exists"):
        _ = run_process((sys.executable, "-c", "print('unused')"), tmp_path, output, 5)
    assert sentinel.read_text(encoding="utf-8") == "another task"
    assert sorted(p.name for p in output.iterdir()) == ["keep.txt"]


def test_second_interrupt_during_cleanup_still_reaps_child(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original_wait = subprocess.Popen[str].wait
    children: list[subprocess.Popen[str]] = []

    def second_interrupt(process: subprocess.Popen[str], timeout: float | None = None) -> int:
        if process not in children:
            children.append(process)
        if timeout == 0.2:
            raise KeyboardInterrupt
        return original_wait(process, timeout)

    monkeypatch.setattr(subprocess.Popen, "wait", second_interrupt)
    try:
        try:
            result = run_process(
                (sys.executable, "-c", "import time; time.sleep(30)"),
                tmp_path,
                tmp_path / "run",
                timeout_seconds=1,
                grace_seconds=0.2,
            )
        except KeyboardInterrupt:
            pytest.fail("A second interrupt escaped cleanup instead of settling the owned child")
        assert result.timed_out is True
        assert result.exit_code != 0
        assert all(child.poll() is not None for child in children)
    finally:
        for child in children:
            if child.poll() is None:
                child.kill()
            _ = original_wait(child, timeout=5)
