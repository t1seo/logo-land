"""Bounded settlement for one owned process group or a launcher's fresh session."""

from __future__ import annotations

import os
import signal
import subprocess
import time
from typing import Final

from .process_scope import ProcessInspectionError, SessionGroup, defer_interrupts, session_groups

_FORCE_SECONDS: Final = 10.0
_POLL_SECONDS: Final = 0.01


def _group_exists(pgid: int) -> bool:
    try:
        os.killpg(pgid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _signal_group(pgid: int, sig: signal.Signals) -> None:
    try:
        os.killpg(pgid, sig)
    except (ProcessLookupError, PermissionError):
        # macOS can report EPERM while an owned group is being reaped; absence is checked below.
        return


class _OwnedGroups:
    """Accumulate observed groups and completed signals while settlement progresses."""

    def __init__(self, pid: int, include_session: bool) -> None:
        self._session_id: int = pid
        self._include_session: bool = include_session
        self._active: set[int] = {pid}
        self._finished: set[int] = set()
        self._members: dict[int, SessionGroup] = {pid: SessionGroup(pid, pid, pid)}
        self._signalled: dict[int, signal.Signals] = {}
        self.inspection_error: ProcessInspectionError | None = None

    def _refresh(self, deadline: float) -> bool:
        if not self._include_session:
            return True
        try:
            for member in session_groups(self._session_id, deadline):
                if member.group_id not in self._finished:
                    self._members[member.group_id] = member
                    self._active.add(member.group_id)
        except ProcessInspectionError as error:
            if time.monotonic() < deadline and self.inspection_error is None:
                self.inspection_error = error
            return False
        return True

    def _signal(self, sig: signal.Signals) -> None:
        for group_id in self._active:
            if self._signalled.get(group_id) == sig:
                continue
            if self._include_session:
                try:
                    if not self._members[group_id].signal(sig):
                        continue
                except ProcessInspectionError as error:
                    self.inspection_error = error
                    continue
            else:
                _signal_group(group_id, sig)
            self._signalled[group_id] = sig

    def step(self, sig: signal.Signals, deadline: float) -> bool:
        verified = self._refresh(deadline)
        self._signal(signal.SIGKILL if self.inspection_error is not None else sig)
        self._finished.update(group for group in self._active if not _group_exists(group))
        self._active.difference_update(self._finished)
        return verified and not self._active

    def raise_inspection_error(self) -> None:
        if self.inspection_error is not None:
            raise self.inspection_error


def settle_group(
    process: subprocess.Popen[str],
    initial_signal: signal.Signals,
    grace_seconds: float,
    *,
    include_session: bool = False,
) -> KeyboardInterrupt | None:
    """Reap the leader and owned groups within fixed graceful and forced deadlines."""
    deadline = time.monotonic() + grace_seconds
    force_deadline = deadline + _FORCE_SECONDS
    owned = _OwnedGroups(process.pid, include_session)
    forced = False
    interrupted: KeyboardInterrupt | None = None
    while True:
        try:
            with defer_interrupts():
                exit_code = process.poll()
            settled = owned.step(signal.SIGKILL if forced else initial_signal, force_deadline)
            if owned.inspection_error is not None:
                forced = True
                deadline = force_deadline
            if settled and exit_code is not None:
                owned.raise_inspection_error()
                return interrupted
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                if forced:
                    owned.raise_inspection_error()
                    raise subprocess.TimeoutExpired(process.args, grace_seconds + _FORCE_SECONDS)
                forced = True
                deadline = force_deadline
                continue
            time.sleep(min(_POLL_SECONDS, remaining))
        except KeyboardInterrupt as error:
            if interrupted is None:
                interrupted = error
            forced = True
            deadline = force_deadline
