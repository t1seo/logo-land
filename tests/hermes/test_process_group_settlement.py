from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
from contextlib import contextmanager, suppress
from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.launcher_process import LaunchError, run_process
from logopia_studio.process_scope import ProcessInspectionError, SessionGroup

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path

TREE_SOURCE: Final = """# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# How to run: launched with literal argv by the finite process fixture.
import os, signal, sys, time
from pathlib import Path
root = Path(sys.argv[1])
mode, ignores = sys.argv[2:4]
caller = os.getppid()
signal.alarm(10)
root.joinpath("leader.pid").write_text(f"{os.getpid()} {os.getpgrp()}")
read_fd, write_fd = os.pipe()
child = os.fork()
if child == 0:
    os.close(read_fd)
    if ignores == "yes":
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.alarm(10)
    root.joinpath("descendant.pid").write_text(f"{os.getpid()} {os.getpgrp()}")
    if mode in ("exit", "nonzero"):
        os.close(1)
        os.close(2)
    os.write(write_fd, b"ready")
    os.close(write_fd)
    if mode == "repeat":
        while True:
            os.kill(caller, signal.SIGINT)
            time.sleep(0.4)
    signal.pause()
else:
    os.close(write_fd)
    assert os.read(read_fd, 5) == b"ready"
    os.close(read_fd)
    root.joinpath("ready").write_text("ready")
    if mode in ("exit", "nonzero"):
        print("exact stdout", flush=True)
        sys.exit(7 if mode == "nonzero" else 0)
    signal.pause()
"""


def process_state(pid: int) -> str:
    result = subprocess.run(  # noqa: S603 - fixed ps executable and exact owned PID.
        ("/bin/ps", "-p", str(pid), "-o", "pid=,ppid=,pgid=,stat="),
        capture_output=True,
        text=True,
        check=False,
        timeout=2,
    )
    return result.stdout.strip()


def group_exists(pgid: int) -> bool:
    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def recorded_processes(root: Path) -> tuple[tuple[int, int], ...]:
    return tuple(
        (int(parts[0]), int(parts[1]))
        for receipt in sorted(root.glob("*.pid"))
        if (parts := receipt.read_text(encoding="utf-8").split())
    )


def observe(root: Path, elapsed: float) -> tuple[tuple[str, ...], bool]:
    records = recorded_processes(root)
    assert records, "The finite fixture did not publish its ownership receipt"
    states = tuple(process_state(pid) for pid, _ in records)
    alive = any(group_exists(pgid) for _, pgid in records)
    _ = sys.stdout.write(
        json.dumps(
            {
                "fixture": root.name,
                "owned": records,
                "states": states,
                "group_exists": alive,
                "elapsed": round(elapsed, 3),
            }
        )
        + "\n"
    )
    return states, alive


@contextmanager
def finite_fixture(root: Path, source: str, *args: str) -> Generator[tuple[str, ...], None, None]:
    """Own finite fixture scripts and settle every recorded PID even on RED."""
    script = root / "finite_fixture.py"
    _ = script.write_text(source, encoding="utf-8")
    try:
        yield (sys.executable, str(script), str(root), *args)
    finally:
        previous = signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            records = recorded_processes(root)
            for pid, _ in records:
                with suppress(ProcessLookupError):
                    os.kill(pid, signal.SIGKILL)
            deadline = time.monotonic() + 3
            while True:
                for pid, _ in records:
                    with suppress(ChildProcessError):
                        _ = os.waitpid(pid, os.WNOHANG)
                states = tuple(process_state(pid) for pid, _ in records)
                alive = any(group_exists(pgid) for _, pgid in records)
                if (not any(states) and not alive) or time.monotonic() >= deadline:
                    break
                time.sleep(0.01)
            _ = sys.stdout.write(
                json.dumps(
                    {
                        "cleanup": root.name,
                        "owned": records,
                        "states": states,
                        "group_exists": alive,
                    }
                )
                + "\n"
            )
            assert not any(states), "Finite fixture PIDs failed to settle"
            assert not alive, "Finite fixture groups failed to settle"
        finally:
            _ = signal.signal(signal.SIGINT, previous)


@pytest.mark.parametrize("ignores", ["yes", "no"])
def test_launcher_deadline_settles_same_group_descendant(tmp_path: Path, ignores: str) -> None:
    # Given a ready finite tree, with descendant signal handling as the controlled toggle.
    with finite_fixture(tmp_path, TREE_SOURCE, "deadline", ignores) as command:
        started = time.monotonic()
        # When the real launcher deadline expires and the leader exits on SIGINT.
        result = run_process(command, tmp_path, tmp_path / "logs", 1, grace_seconds=0.2)
        states, alive = observe(tmp_path, time.monotonic() - started)
        # Then the receipt covers complete group settlement before return.
        assert (tmp_path / "ready").read_text(encoding="utf-8") == "ready"
        assert result.timed_out
        assert not result.interrupted
        assert result.exit_code != 0
        assert not any(states)
        assert not alive
        assert time.monotonic() - started < 4


def test_launcher_normal_exit_settles_orphan_descendant(tmp_path: Path) -> None:
    # Given a ready descendant whose leader exits successfully before cleanup starts.
    with finite_fixture(tmp_path, TREE_SOURCE, "exit", "yes") as command:
        started = time.monotonic()
        # When the launcher reports the leader's normal result.
        result = run_process(command, tmp_path, tmp_path / "logs", 2, grace_seconds=0.2)
        states, alive = observe(tmp_path, time.monotonic() - started)
        # Then success preserves the logs while settling the exact owned group.
        assert result.exit_code == 0
        assert not result.timed_out
        assert not result.interrupted
        assert result.stdout_path.read_text(encoding="utf-8") == "exact stdout\n"
        assert not any(states)
        assert not alive
        assert time.monotonic() - started < 3


def test_launcher_repeated_interrupts_settle_descendant(tmp_path: Path) -> None:
    # Given a ready finite descendant sending real repeated interrupts to the caller.
    with finite_fixture(tmp_path, TREE_SOURCE, "repeat", "yes") as command:
        started = time.monotonic()
        # When cancellation starts, further interrupts must not abandon the owned group.
        result = run_process(command, tmp_path, tmp_path / "logs", 3, grace_seconds=1)
        states, alive = observe(tmp_path, time.monotonic() - started)
        # Then the interruption receipt follows full group settlement.
        assert result.interrupted
        assert not result.timed_out
        assert result.exit_code != 0
        assert not any(states)
        assert not alive
        assert time.monotonic() - started < 3


def test_cleanup_preserves_other_session_process(tmp_path: Path) -> None:
    # Given an independent finite process outside the launcher's owned session.
    with subprocess.Popen(
        (sys.executable, "-c", "import signal; signal.alarm(10); signal.pause()"),
        start_new_session=True,
    ) as control:
        try:
            with finite_fixture(tmp_path, TREE_SOURCE, "deadline", "yes") as command:
                # When only the launcher's group is settled.
                result = run_process(command, tmp_path, tmp_path / "logs", 1, grace_seconds=0.2)
                # Then the independent control remains alive until its own finally cleanup.
                assert result.timed_out
                assert control.poll() is None
                assert all(pgid != control.pid for _, pgid in recorded_processes(tmp_path))
                launcher_group = recorded_processes(tmp_path)[0][1]
                assert not SessionGroup(launcher_group, control.pid, control.pid).signal(
                    signal.SIGKILL
                )
                assert control.poll() is None
                _ = sys.stdout.write(
                    json.dumps({"unowned_control": process_state(control.pid)}) + "\n"
                )
        finally:
            control.kill()
            _ = control.wait(timeout=2)
        assert not process_state(control.pid)


@pytest.mark.parametrize("deadline", [0, -1, 3601])
def test_invalid_deadline_starts_no_process(tmp_path: Path, deadline: int) -> None:
    # Given an invalid launch deadline.
    output = tmp_path / "logs"
    # When validation runs, then no log directory or subprocess is created.
    with pytest.raises(LaunchError, match="invalid_deadline"):
        _ = run_process((sys.executable,), tmp_path, output, deadline)
    assert not output.exists()


def test_empty_argv_starts_no_process(tmp_path: Path) -> None:
    # Given empty argv, when validation runs, then no process or logs are created.
    with pytest.raises(LaunchError, match="invalid_command"):
        _ = run_process((), tmp_path, tmp_path / "logs", 1)
    assert not (tmp_path / "logs").exists()


def test_failed_session_inspection_returns_bounded_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Given a finite owned tree and unavailable numeric session inspection.
    def unavailable(_session_id: int, _deadline: float) -> tuple[SessionGroup, ...]:
        raise ProcessInspectionError("fixture_query_failure")

    monkeypatch.setattr("logopia_studio.process_group.session_groups", unavailable)
    monkeypatch.setattr("logopia_studio.process_group._FORCE_SECONDS", 0.1)
    with finite_fixture(tmp_path, TREE_SOURCE, "deadline", "yes") as command:
        started = time.monotonic()
        # When ownership cannot be inspected, then no successful receipt can be returned.
        with pytest.raises(LaunchError, match="process_inspection_failed"):
            _ = run_process(command, tmp_path, tmp_path / "logs", 1, grace_seconds=0.1)
        states, alive = observe(tmp_path, time.monotonic() - started)
        assert not any(states)
        assert not alive
        assert time.monotonic() - started < 3
