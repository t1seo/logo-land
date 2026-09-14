from pathlib import Path

import pytest
from logopia_studio.engine_recovery import can_resume_critique
from logopia_studio.models import Candidate, Job, Workflow
from tests.hermes.test_core_fixtures import FixtureHost, brief


def eligible_state() -> Workflow:
    intent = brief()
    plan = FixtureHost(Path.cwd()).plan(intent)
    candidate = Candidate(
        id="c1",
        direction_id="d1",
        parent_id=None,
        image_path=".logo-generator/sessions/resume/artifacts/c1.png",
        sha256="a" * 64,
        width=64,
        height=64,
        prompt="Fixture",
        provider="fixture",
        model="stub",
    )
    return Workflow(
        id="resume",
        brief=intent,
        phase="outcome_unknown",
        strategy=plan.strategy,
        directions=plan.directions,
        candidates=(candidate,),
        jobs=(
            Job(id="j1", kind="plan", status="succeeded", request_sha256="b" * 64, plan=plan),
            Job(
                id="j2",
                kind="generate",
                status="succeeded",
                request_sha256="c" * 64,
                candidate_id="c1",
                direction_id="d1",
            ),
            Job(
                id="j3",
                kind="critique",
                status="unknown",
                request_sha256="d" * 64,
                candidate_id="c1",
                error="Fixture settled interruption",
            ),
        ),
    )


def test_eligibility_supports_saved_schema_one_without_retry_field() -> None:
    # Given a schema-one snapshot written before review recovery was available.
    state = eligible_state()
    raw = state.model_dump_json(exclude_defaults=True)
    assert "retry_of" not in raw
    loaded = Workflow.model_validate_json(raw)
    # When eligibility is inspected, then it is pure and the remaining review is resumable.
    assert can_resume_critique(loaded)
    assert loaded.model_dump_json(exclude_defaults=True) == raw


@pytest.mark.parametrize("kind", ["plan", "generate", "edit", "deliver"])
def test_unrelated_unknown_calls_block_review_recovery(kind: str) -> None:
    # Given an otherwise recoverable critique plus a different unknown native operation.
    state = eligible_state()
    job = state.jobs[0 if kind == "plan" else 1].model_copy(
        update={"status": "unknown", "kind": kind}
    )
    jobs = (job, *state.jobs[1:]) if kind == "plan" else (state.jobs[0], job, state.jobs[-1])
    changed = Workflow.model_validate_json(
        state.model_copy(update={"jobs": jobs}).model_dump_json()
    )
    # When inspected, then read-only recovery cannot conceal the unresolved operation.
    assert not can_resume_critique(changed)


@pytest.mark.parametrize("status", ["reserved", "returned", "failed", "succeeded"])
def test_active_or_settled_nonunknown_review_is_ineligible(status: str) -> None:
    # Given a review whose status is not an interrupted unknown attempt.
    state = eligible_state()
    changed = state.model_copy(
        update={"jobs": (*state.jobs[:-1], state.jobs[-1].model_copy(update={"status": status}))}
    )
    # When inspected, then no active-call or failed-call reset is inferred.
    assert not can_resume_critique(Workflow.model_validate_json(changed.model_dump_json()))


def test_missing_original_plan_or_exhausted_budget_is_ineligible() -> None:
    # Given incomplete provenance or an already consumed second critique attempt.
    state = eligible_state()
    exhausted = state.model_copy(
        update={
            "jobs": (
                *state.jobs,
                Job(
                    id="j4",
                    kind="critique",
                    status="failed",
                    request_sha256="e" * 64,
                    candidate_id="c1",
                    error="Fixture second attempt failed",
                ),
            )
        }
    )
    # When eligibility is queried, then none of these cases grants a native call.
    assert not can_resume_critique(state.model_copy(update={"strategy": None}))
    assert not can_resume_critique(state.model_copy(update={"candidates": ()}))
    assert not can_resume_critique(state.model_copy(update={"phase": "cancelled"}))
    assert not can_resume_critique(exhausted)


def test_retry_link_only_supersedes_exact_unknown_critique() -> None:
    # Given a durable replacement referencing the same read-only candidate and request.
    state = eligible_state()
    retry = Job(id="j4", kind="critique", candidate_id="c1", request_sha256="d" * 64, retry_of="j3")
    updated = Workflow.model_validate_json(
        state.model_copy(update={"jobs": (*state.jobs, retry)}).model_dump_json()
    )
    # When reserved, then the old unknown is preserved and further recovery is blocked.
    assert updated.jobs[-2] == state.jobs[-1]
    assert updated.jobs[-1].retry_of == "j3"
    assert not can_resume_critique(updated)
    for bad in (
        retry.model_copy(update={"retry_of": "j2"}),
        retry.model_copy(update={"candidate_id": "absent"}),
        retry.model_copy(update={"request_sha256": "f" * 64}),
        retry.model_copy(update={"kind": "edit"}),
        retry.model_copy(update={"retry_of": "j5"}),
    ):
        with pytest.raises(ValueError, match="retry"):
            _ = Workflow.model_validate_json(
                state.model_copy(update={"jobs": (*state.jobs, bad)}).model_dump_json()
            )
