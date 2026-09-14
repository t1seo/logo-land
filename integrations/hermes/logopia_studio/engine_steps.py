"""Commit attempts before external calls and retain late/error evidence durably."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import TYPE_CHECKING, assert_never

from pydantic import ValidationError

from .engine_jobs import is_superseded, unresolved_jobs
from .models import Feedback, Job, StudioError, Workflow

if TYPE_CHECKING:
    from .helper import HelperBridge
    from .models import Phase
    from .protocols import DesignHost
    from .store import Store


def advance(state: Workflow) -> Workflow:
    return state.model_copy(update={"revision": state.revision + 1})


def put_job(state: Workflow, job: Job) -> Workflow:
    return state.model_copy(
        update={"jobs": tuple(job if item.id == job.id else item for item in state.jobs)}
    )


def job_by_id(state: Workflow, job_id: str) -> Job:
    for job in state.jobs:
        if job.id == job_id:
            return job
    raise StudioError("not_found", f"Job {job_id} does not exist")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def is_paused(state: Workflow) -> bool:
    return state.phase in {"outcome_unknown", "cancelled"}


@dataclass(frozen=True, slots=True)
class Steps:
    """Shared finite-step context; mutable state lives only in persisted snapshots."""

    store: Store
    helper: HelperBridge
    host: DesignHost

    def reserve(self, state: Workflow, job: Job, phase: Phase) -> Workflow:
        with self.store.locked(state.id):
            current = self.store.expect(state.id, state.revision)
            updated = current.model_copy(
                update={"jobs": (*current.jobs, job), "phase": phase, "last_error": None}
            )
            if any(item.id != job.id for item in unresolved_jobs(updated)):
                raise StudioError("busy", "An existing call needs completion or reconciliation")
            if job.kind == "edit":
                if job.parent_id is None:
                    raise StudioError("invalid_job", "Edit reservation requires a parent")
                feedback = Feedback(candidate_id=job.parent_id, keep=job.keep, change=job.change)
                updated = updated.model_copy(update={"feedback": (*current.feedback, feedback)})
            return self.store.save(advance(updated))

    def record(self, state: Workflow, job: Job) -> Workflow:
        with self.store.locked(state.id):
            current = self.store.load(state.id)
            previous = job_by_id(current, job.id)
            if is_superseded(current, job.id):
                return current
            if previous.request_sha256 != job.request_sha256:
                raise StudioError("conflict", "Late return differs from reserved request")
            recorded = job.model_copy(update={"error": job.error or previous.error})
            return self.store.save(advance(put_job(current, recorded)))

    def commit(self, state: Workflow) -> Workflow:
        with self.store.locked(state.id):
            _ = self.store.expect(state.id, state.revision)
            return self.store.save(advance(state))

    def fail(
        self,
        state: Workflow,
        job: Job,
        error: StudioError | TimeoutError | OSError | ValidationError,
    ) -> Workflow:
        match error:
            case StudioError():
                unknown = any(word in error.code for word in ("unknown", "timeout", "interrupted"))
                reports = error.raw_reports or job.raw_reports
            case TimeoutError() | OSError():
                unknown = True
                reports = job.raw_reports
            case ValidationError():
                unknown = False
                reports = job.raw_reports
            case _:
                assert_never(error)
        failed = job.model_copy(
            update={
                "status": "unknown" if unknown else "failed",
                "error": job.error or str(error)[:64000],
                "raw_reports": reports,
            }
        )
        with self.store.locked(state.id):
            current = self.store.load(state.id)
            if is_superseded(current, job.id):
                return current
            updated = put_job(current, failed)
            if not is_paused(current):
                updated = updated.model_copy(
                    update={
                        "phase": "outcome_unknown" if unknown else "failed",
                        "last_error": str(error)[:64000],
                    }
                )
            return self.store.save(advance(updated))
