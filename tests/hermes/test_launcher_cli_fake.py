from __future__ import annotations

import json
import os
import signal
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, assert_never
from uuid import uuid4

from logopia_studio.engine import Studio
from logopia_studio.host_requests import (
    ContinueRequest,
    DeliverRequest,
    ReconcileRequest,
    StartRequest,
    StatusRequest,
)
from logopia_studio.launcher_requests import BEGIN_REQUEST, END_REQUEST, parse_request
from logopia_studio.models import FeedbackEnvelope, Job, Workflow
from logopia_studio.store import Store
from tests.hermes.test_core_fixtures import FixtureHost
from typing_extensions import override

if TYPE_CHECKING:
    from logopia_studio.models import Critique, ReviewInput


@dataclass(frozen=True, slots=True)
class RunFixtureHost(FixtureHost):
    @override
    def critique(self, request: ReviewInput) -> tuple[Critique, ...]:
        prefix = uuid4().hex
        return tuple(
            report.model_copy(update={"call_id": f"{prefix}-{report.call_id}"})
            for report in FixtureHost.critique(self, request)
        )


def perform(studio: Studio, document: str) -> Workflow:
    request = parse_request(document.encode()).request
    match request:
        case StartRequest():
            state = studio.create(request.workflow_id, request.brief)
            result = studio.produce(state.id, state.revision)
        case ContinueRequest():
            result = studio.produce(request.workflow_id, request.expected_revision)
        case FeedbackEnvelope():
            match request.action:
                case "choose":
                    result = studio.choose(
                        request.workflow_id, request.expected_revision, request.candidate_id
                    )
                case "revise":
                    result = studio.revise(
                        request.workflow_id,
                        request.expected_revision,
                        request.candidate_id,
                        request.keep,
                        request.change,
                    )
                case _:
                    assert_never(request.action)
        case StatusRequest():
            result = studio.status(request.workflow_id)
        case DeliverRequest():
            result = studio.deliver(request.workflow_id, request.expected_revision)
        case ReconcileRequest():
            result = studio.reconcile(
                request.workflow_id, request.expected_revision, request.job_id
            )
        case _:
            assert_never(request)
    return result


def main() -> None:
    root = Path(os.environ["HERMES_HOME"])
    with (root / "invocations.jsonl").open("a", encoding="utf-8") as stream:
        _ = stream.write(json.dumps(sys.argv[1:]) + "\n")
    mode_file = root / "mode.txt"
    mode = mode_file.read_text(encoding="utf-8") if mode_file.exists() else "noop"
    if "doctor" in sys.argv and mode == "doctor-fail":
        _ = sys.stdout.write("FIXTURE: dependency check failed\n")
        raise SystemExit(1)
    if "config" in sys.argv and mode in {"sequential_call-fail", "concurrent_batch-fail"}:
        key = mode.removesuffix("-fail")
        if f"timeouts.tools.{key}" in sys.argv:
            _ = sys.stdout.write("FIXTURE: timeout configuration failed\n")
            raise SystemExit(1)
    if "--query-file" not in sys.argv:
        _ = sys.stdout.write("FIXTURE: configuration command, zero native calls\n")
        return
    query = Path(sys.argv[sys.argv.index("--query-file") + 1]).read_text(encoding="utf-8")
    _ = (root / "received-query.txt").write_text(query, encoding="utf-8")
    document = query.split(BEGIN_REQUEST, 1)[1].rsplit(END_REQUEST, 1)[0]
    workspace = Path(sys.argv[sys.argv.index("--in") + 1])
    if mode in {"timeout", "partial-exit"}:
        request = parse_request(document.encode()).request
        store = Store(workspace)
        state = store.load(request.workflow_id)
        job = Job(id="j1", kind="plan", status="reserved", request_sha256="a" * 64)
        _ = store.save(
            state.model_copy(update={"jobs": (job,), "phase": "planning", "revision": 1})
        )
        if mode == "partial-exit":
            _ = sys.stdout.write("Successfully produced every logo; all checks passed.\n")
            return
        try:
            _ = (root / "ready.txt").write_text("waiting", encoding="utf-8")
            signal.pause()
        finally:
            _ = (root / "settled.txt").write_text("owned fake settled", encoding="utf-8")
        return
    if mode == "tool":
        host = RunFixtureHost(workspace)
        studio = Studio(workspace, Path(__file__).resolve().parents[2], host)
        state = perform(studio, document)
        with (root / "fixture-image-calls.txt").open("a", encoding="utf-8") as stream:
            _ = stream.write("fixture image\n" * len(host.calls))
        _ = sys.stdout.write(f"FIXTURE: saved {state.id} {state.phase}; no actual image provider\n")
        return
    _ = sys.stdout.write("Successfully produced every logo; all checks passed.\n")
