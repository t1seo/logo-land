from collections.abc import Callable
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from logopia_studio.engine import Studio
from logopia_studio.models import Critique, ReviewInput, StudioError, Workflow
from tests.hermes.test_core_fixtures import REPO, FixtureHost, brief
from typing_extensions import override


@dataclass(frozen=True, slots=True)
class ResumeHost(FixtureHost):
    """Deterministic fixture reviews; never an assessment of model design quality."""

    prefix: str = "setup"
    unknown_at: int | None = None
    on_review: Callable[[ReviewInput], None] | None = None

    @override
    def critique(self, request: ReviewInput) -> tuple[Critique, ...]:
        if self.on_review is not None:
            self.on_review(request)
        if self.unknown_at == len(self.reviews) + 1:
            self.reviews.append(request)
            raise StudioError("outcome_unknown", "Fixture critic interrupted before any report")
        return tuple(
            report.model_copy(update={"call_id": f"{self.prefix}-{report.call_id}"})
            for report in FixtureHost.critique(self, request)
        )


def interrupted_reviews(root: Path, count: int = 3) -> tuple[Studio, Workflow, ResumeHost]:
    host = ResumeHost(root, unknown_at=count)
    studio = Studio(root, REPO, host)
    created = studio.create("resume", brief(count))
    failed = studio.produce("resume", created.revision)
    state = studio.interrupt("resume", failed.revision, "Fixture owned runner has settled")
    assert state.jobs[-1].kind == "critique"
    assert state.jobs[-1].status == "unknown"
    assert state.jobs[-1].critiques == ()
    return studio, state, host


def original_hashes(root: Path, state: Workflow) -> tuple[str, ...]:
    return tuple(
        sha256((root / candidate.image_path).read_bytes()).hexdigest()
        for candidate in state.candidates
    )
