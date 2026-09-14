"""Run one requested operation and verify it after the owned process has settled."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING
from uuid import uuid4

from .engine import Studio
from .host_requests import StatusRequest
from .launcher_output import CommandResult, fresh_gallery, state_result
from .launcher_process import MAX_DEADLINE, LaunchError, hermes_command, run_process
from .launcher_profile import installed_settings, profile_lock, profile_path
from .launcher_requests import load_request
from .launcher_state import NoInferenceHost, existing_state, preflight, verify_result
from .models import StudioError
from .store_files import safe_path

if TYPE_CHECKING:
    from pathlib import Path

    from .launcher_process import ProcessReceipt
    from .launcher_requests import Request
    from .models import Workflow


@dataclass(frozen=True, slots=True)
class RunOptions:
    """Trusted CLI options kept separate from model-supplied request arguments."""

    profile: str
    request: Path
    profile_home: Path | None = None
    workspace: Path | None = None
    timeout: int = 1800


def _settled_state(studio: Studio, request: Request, receipt: ProcessReceipt) -> Workflow | None:
    state = existing_state(studio, request.workflow_id)
    if state is None:
        return None
    interrupted = receipt.timed_out or receipt.interrupted
    active = any(job.status in {"reserved", "returned"} for job in state.jobs)
    if interrupted or active:
        if receipt.timed_out:
            cause = "settled after its deadline"
        elif receipt.interrupted:
            cause = "settled after an interruption"
        else:
            cause = f"exited with unfinished operation (exit code {receipt.exit_code})"
        reason = " ".join(
            (
                f"Owned Hermes process {cause}; provider cancellation is not confirmed.",
                "Inspect saved jobs before any explicit reconciliation.",
            )
        )
        state = studio.interrupt(state.id, state.revision, reason)
    return state


def _check_receipt(receipt: ProcessReceipt) -> None:
    if receipt.timed_out:
        raise LaunchError(
            "run_timed_out", "Owned Hermes deadline reached; provider outcome may be unknown"
        )
    if receipt.interrupted:
        raise LaunchError(
            "run_interrupted", "Owned Hermes process stopped; provider cancellation is unconfirmed"
        )
    if receipt.exit_code != 0:
        raise LaunchError("hermes_failed", f"Hermes exited with code {receipt.exit_code}")


def _finish(
    studio: Studio,
    request: Request,
    before: Workflow | None,
    receipt: ProcessReceipt,
    logs: Path,
    workspace: Path,
) -> CommandResult:
    state = _settled_state(studio, request, receipt)
    try:
        state = _verified_state(receipt, request, before, state)
    except LaunchError as error:
        if state is None:
            return CommandResult(
                success=False, message=error.detail, error=error.code, logs=str(logs)
            )
        gallery = fresh_gallery(workspace, state)
        return state_result(
            state,
            success=False,
            message=error.detail,
            gallery=gallery,
            logs=logs,
            error=error.code,
        )
    gallery = fresh_gallery(workspace, state)
    return state_result(
        state, message="Requested result verified in saved state", gallery=gallery, logs=logs
    )


def _verified_state(
    receipt: ProcessReceipt,
    request: Request,
    before: Workflow | None,
    state: Workflow | None,
) -> Workflow:
    _check_receipt(receipt)
    if state is None:
        raise LaunchError(
            "workflow_missing", "Hermes returned without saving the requested workflow"
        )
    verify_result(request, before, state)
    return state


def run_request(options: RunOptions) -> CommandResult:
    document = load_request(options.request)
    if not 1 <= options.timeout <= MAX_DEADLINE:
        raise LaunchError("invalid_deadline", "--timeout must be between 1 and 3600 seconds")
    profile = profile_path(options.profile, options.profile_home)
    with profile_lock(profile):
        settings = installed_settings(profile, options.workspace)
        studio = Studio(settings.workspace, settings.helper_repo, NoInferenceHost())
        before = preflight(studio, document.request)
        if isinstance(document.request, StatusRequest) and before is not None:
            return state_result(before)
        run_root = safe_path(
            settings.workspace,
            f"output/logopia-runs/{document.request.workflow_id}-{uuid4().hex}",
        )
        run_root.mkdir(parents=True, mode=0o700, exist_ok=False)
        query = run_root / "query.txt"
        with query.open("x", encoding="utf-8") as stream:
            _ = stream.write(document.query())
        receipt = run_process(
            hermes_command(options.profile, query, settings.workspace),
            settings.workspace,
            run_root / "process",
            options.timeout,
        )
        try:
            return _finish(
                studio,
                document.request,
                before,
                receipt,
                run_root / "process",
                settings.workspace,
            )
        except (LaunchError, StudioError, OSError) as error:
            return CommandResult(
                success=False,
                message=str(error)[:1200],
                error="result_unverified",
                logs=str(run_root / "process"),
            )
