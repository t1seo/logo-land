"""Stable public API for durable, explicitly selected logo production."""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import engine_actions, engine_pipeline, engine_recovery
from .checks import review_input, verify_critiques
from .engine_steps import Steps
from .helper import HelperBridge
from .helper_delivery import verified_delivery
from .models import StudioBrief, StudioError, Workflow
from .store import Store

if TYPE_CHECKING:
    from pathlib import Path

    from .protocols import DesignHost


class Studio:
    """The workspace is caller configuration; model arguments cannot choose paths."""

    steps: Steps

    def __init__(self, workspace: Path, helper_repo: Path, host: DesignHost) -> None:
        root = workspace.resolve(strict=True)
        repo = helper_repo.resolve(strict=True)
        if not root.is_dir() or not repo.is_dir():
            raise StudioError("invalid_workspace", "Workspace and helper repo must be directories")
        self.steps = Steps(Store(root), HelperBridge(root, repo), host)

    def create(self, workflow_id: str, brief: StudioBrief) -> Workflow:
        validated = StudioBrief.model_validate_json(brief.model_dump_json())
        with self.steps.store.locked(workflow_id):
            if self.steps.store.path(workflow_id).exists():
                state = self.steps.store.load(workflow_id)
                if state.brief != validated:
                    raise StudioError(
                        "conflict", "Workflow ID already belongs to a different brief"
                    )
            else:
                if self.steps.helper.session_path(workflow_id).exists():
                    raise StudioError(
                        "conflict", "Existing helper session is not owned by this workflow"
                    )
                state = self.steps.store.save(Workflow(id=workflow_id, brief=validated))
        _ = self.steps.helper.ensure(state)
        return self.status(workflow_id)

    def status(self, workflow_id: str) -> Workflow:
        state = self.steps.store.load(workflow_id)
        if self.steps.helper.session_path(workflow_id).exists():
            _ = self.steps.helper.show(state)
        elif state.candidates:
            raise StudioError("invalid_state", "Canonical helper session is missing")
        for candidate in state.candidates:
            if candidate.critiques:
                verify_critiques(
                    review_input(self.steps.store.root, state, candidate), candidate.critiques
                )
        if (
            state.delivery is not None
            and verified_delivery(self.steps.helper, state, state.delivery.path) != state.delivery
        ):
            raise StudioError("invalid_delivery", "Delivery no longer matches its recorded hashes")
        return state

    def _expect(self, workflow_id: str, expected_revision: int) -> Workflow:
        state = self.status(workflow_id)
        if type(expected_revision) is not int or expected_revision < 0:
            raise StudioError("invalid_revision", "Revision must be a nonnegative integer")
        if state.revision != expected_revision:
            raise StudioError(
                "stale_revision", f"Expected {expected_revision}; current {state.revision}"
            )
        return state

    def produce(self, workflow_id: str, expected_revision: int) -> Workflow:
        return engine_pipeline.produce(self.steps, self._expect(workflow_id, expected_revision))

    def revise(
        self,
        workflow_id: str,
        expected_revision: int,
        candidate_id: str,
        keep: tuple[str, ...],
        change: str,
    ) -> Workflow:
        return engine_actions.revise(
            self.steps, self._expect(workflow_id, expected_revision), candidate_id, keep, change
        )

    def choose(self, workflow_id: str, expected_revision: int, candidate_id: str) -> Workflow:
        return engine_actions.choose(
            self.steps, self._expect(workflow_id, expected_revision), candidate_id
        )

    def deliver(self, workflow_id: str, expected_revision: int) -> Workflow:
        return engine_actions.deliver(self.steps, self._expect(workflow_id, expected_revision))

    def interrupt(self, workflow_id: str, expected_revision: int, reason: str) -> Workflow:
        return engine_recovery.interrupt(
            self.steps, self._expect(workflow_id, expected_revision), reason
        )

    def reconcile(self, workflow_id: str, expected_revision: int, job_id: str) -> Workflow:
        return engine_recovery.reconcile(
            self.steps, self._expect(workflow_id, expected_revision), job_id
        )
