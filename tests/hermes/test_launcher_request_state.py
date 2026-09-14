from __future__ import annotations

from typing import TYPE_CHECKING, Final

import pytest
from logopia_studio.engine import Studio
from logopia_studio.host_requests import ContinueRequest, DeliverRequest, StartRequest
from logopia_studio.launcher_process import LaunchError
from logopia_studio.launcher_state import verify_result
from logopia_studio.models import FeedbackEnvelope, Workflow
from tests.hermes.test_core_fixtures import FixtureHost, brief
from tests.hermes.test_launcher_cli_fixtures import REPO

if TYPE_CHECKING:
    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


@pytest.fixture
def produced(cli_fixture: CliFixture) -> Workflow:
    studio = Studio(cli_fixture.workspace, REPO, FixtureHost(cli_fixture.workspace))
    state = studio.create("saved", brief())
    return studio.produce(state.id, state.revision)


def test_start_rejects_unrequested_selection(produced: Workflow) -> None:
    request = StartRequest(workflow_id=produced.id, brief=produced.brief)
    selected = produced.model_copy(update={"selected_id": produced.candidates[0].id})
    with pytest.raises(LaunchError, match="postcondition_failed"):
        verify_result(request, None, selected)


def test_continue_preserves_prior_selection(produced: Workflow) -> None:
    request = ContinueRequest(
        workflow_id=produced.id, action="continue", expected_revision=produced.revision
    )
    selected = produced.model_copy(
        update={"revision": produced.revision + 1, "selected_id": produced.candidates[0].id}
    )
    with pytest.raises(LaunchError, match="postcondition_failed"):
        verify_result(request, produced, selected)


@pytest.mark.parametrize("action", ["choose", "revise"])
def test_feedback_cannot_succeed_on_unmodified_state(produced: Workflow, action: str) -> None:
    candidate = produced.candidates[0]
    request = FeedbackEnvelope.model_validate_json(
        '{"schema_version":1,"workflow_id":"saved","expected_revision":'
        + str(produced.revision)
        + ',"candidate_id":"'
        + candidate.id
        + '","candidate_sha256":"'
        + candidate.sha256
        + '","action":"'
        + action
        + '","keep":[],"change":"'
        + ("spacing" if action == "revise" else "")
        + '"}',
    )
    with pytest.raises(LaunchError, match="postcondition_failed"):
        verify_result(request, produced, produced)


def test_delivery_requires_actual_receipt(produced: Workflow) -> None:
    request = DeliverRequest(
        workflow_id=produced.id, action="deliver", expected_revision=produced.revision
    )
    pretend = produced.model_copy(update={"phase": "delivered", "revision": produced.revision + 1})
    with pytest.raises(LaunchError, match="postcondition_failed"):
        verify_result(request, produced, pretend)
