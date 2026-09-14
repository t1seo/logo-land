"""Durable critique supersession without rewriting the interrupted attempt."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Job, Workflow


def is_superseded(state: Workflow, job_id: str) -> bool:
    return any(job.retry_of == job_id for job in state.jobs)


def unresolved_jobs(state: Workflow) -> tuple[Job, ...]:
    replaced = {job.retry_of for job in state.jobs if job.retry_of is not None}
    return tuple(
        job
        for job in state.jobs
        if job.status in {"reserved", "returned"}
        or (job.status == "unknown" and job.id not in replaced)
    )
