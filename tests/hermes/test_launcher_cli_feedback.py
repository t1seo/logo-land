from __future__ import annotations

from typing import TYPE_CHECKING, Final

from logopia_studio.engine import Studio
from logopia_studio.models import FeedbackEnvelope
from logopia_studio.store import Store
from tests.hermes.test_core_fixtures import FixtureHost, brief
from tests.hermes.test_launcher_cli_fixtures import REPO

if TYPE_CHECKING:
    from tests.hermes.test_launcher_cli_fixtures import CliFixture

pytest_plugins: Final = ("tests.hermes.test_launcher_cli_fixtures",)


def test_revision_across_cli_processes_preserves_parent_and_saves_reviewed_child(
    cli_fixture: CliFixture,
) -> None:
    cli_fixture.configure()
    cli_fixture.mode("tool")
    studio = Studio(cli_fixture.workspace, REPO, FixtureHost(cli_fixture.workspace))
    created = studio.create("saved", brief())
    before = studio.produce(created.id, created.revision)
    parent = before.candidates[0]
    request = FeedbackEnvelope(
        schema_version=1,
        workflow_id=before.id,
        expected_revision=before.revision,
        candidate_id=parent.id,
        candidate_sha256=parent.sha256,
        action="revise",
        keep=("white background",),
        change="Widen spacing",
    )
    result = cli_fixture.run(cli_fixture.request(request.model_dump_json()))
    assert result.returncode == 0, result.stderr
    after = Store(cli_fixture.workspace).load(before.id)
    assert after.candidates[0] == parent
    assert len(after.candidates) == 2
    assert after.candidates[1].parent_id == parent.id
    assert len(after.candidates[1].critiques) == 2
    assert after.selected_id == before.selected_id
