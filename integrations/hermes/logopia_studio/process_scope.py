"""Discover numeric process groups only within a launcher's captured owned session."""

from __future__ import annotations

import errno
import os
import signal
import subprocess
import time
from contextlib import contextmanager
from dataclasses import dataclass
from tempfile import TemporaryFile
from threading import current_thread, main_thread
from typing import TYPE_CHECKING, Final, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable, Generator
    from types import FrameType

_QUERY_SECONDS: Final = 0.25
_INTERRUPT_SECONDS: Final = 0.1
_Result = TypeVar("_Result")


@contextmanager
def defer_interrupts() -> Generator[None, None, None]:
    """Delay the original SIGINT exception until a bounded Popen operation releases its lock."""
    previous = signal.getsignal(signal.SIGINT)
    if current_thread() is not main_thread() or not callable(previous):
        yield
        return
    interrupted: list[KeyboardInterrupt] = []

    def retain(sig: int, frame: FrameType | None) -> None:
        try:
            previous(sig, frame)
        except KeyboardInterrupt as error:
            interrupted.append(error)

    _ = signal.signal(signal.SIGINT, retain)
    try:
        yield
    finally:
        try:
            _ = signal.signal(signal.SIGINT, previous)
        finally:
            if interrupted:
                raise interrupted[0]


def bounded_call(action: Callable[[float], _Result], timeout: float) -> _Result:
    """Keep the invocation deadline while bounding each interrupt-deferred wait."""
    deadline = time.monotonic() + timeout
    while True:
        try:
            with defer_interrupts():
                return action(min(_INTERRUPT_SECONDS, max(0, deadline - time.monotonic())))
        except subprocess.TimeoutExpired as error:
            if time.monotonic() >= deadline:
                error.timeout = timeout
                raise


class ProcessInspectionError(OSError):
    """Refuse a settled receipt when numeric ownership cannot be verified."""

    stage: str

    def __init__(self, stage: str) -> None:
        self.stage = stage
        super().__init__(errno.EIO, f"Cannot verify owned process settlement: {stage}")


@dataclass(frozen=True, slots=True)
class SessionGroup:
    """An observed representative whose session and group must be rechecked before signalling."""

    session_id: int
    group_id: int
    member_pid: int

    def signal(self, sig: signal.Signals) -> bool:
        if self.group_id <= 1 or self.group_id == os.getpgrp():
            return False
        try:
            if (
                os.getsid(self.member_pid) != self.session_id
                or os.getpgid(self.member_pid) != self.group_id
            ):
                return False
        except ProcessLookupError:
            return False
        except OSError as error:
            raise ProcessInspectionError("group_membership") from error
        try:
            os.killpg(self.group_id, sig)
        except (ProcessLookupError, PermissionError):
            # Reaping can transiently produce EPERM; group absence is checked by the caller.
            return False
        return True


def _stop_probe(process: subprocess.Popen[bytes]) -> KeyboardInterrupt | None:
    deadline = time.monotonic() + _QUERY_SECONDS
    interrupted: KeyboardInterrupt | None = None
    while True:
        try:
            with defer_interrupts():
                if process.poll() is not None:
                    return interrupted
                process.kill()
                _ = process.wait(timeout=max(0, deadline - time.monotonic()))
        except KeyboardInterrupt as error:
            if interrupted is None:
                interrupted = error


def _numeric_pids(deadline: float) -> tuple[int, ...]:
    with TemporaryFile() as output:
        process = subprocess.Popen(
            ("/bin/ps", "-A", "-o", "pid="), stdout=output, stderr=subprocess.DEVNULL
        )
        try:
            code = bounded_call(
                lambda remaining: process.wait(timeout=remaining),
                max(0, deadline - time.monotonic()),
            )
            if code != 0:
                raise ProcessInspectionError("pid_listing_exit")
        finally:
            interrupted = _stop_probe(process)
        if interrupted is not None:
            raise interrupted
        _ = output.seek(0)
        tokens = output.read().split()
    if any(not token.isdigit() for token in tokens):
        raise ProcessInspectionError("pid_listing_format")
    return tuple(int(token) for token in tokens)


def session_groups(session_id: int, deadline: float) -> tuple[SessionGroup, ...]:
    """Read PID numbers, never names/argv/environment, and select only our fresh session."""
    if session_id <= 1 or session_id == os.getsid(0):
        raise ProcessInspectionError("invalid_session")
    query_deadline = min(deadline, time.monotonic() + _QUERY_SECONDS)
    try:
        pids = _numeric_pids(query_deadline)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise ProcessInspectionError("pid_listing") from error
    groups: dict[int, SessionGroup] = {}
    for pid in pids:
        if time.monotonic() >= query_deadline:
            raise ProcessInspectionError("query_deadline")
        try:
            if os.getsid(pid) == session_id:
                group_id = os.getpgid(pid)
                groups[group_id] = SessionGroup(session_id, group_id, pid)
        except ProcessLookupError:
            continue
        except OSError as error:
            raise ProcessInspectionError("pid_membership") from error
    return tuple(groups.values())
