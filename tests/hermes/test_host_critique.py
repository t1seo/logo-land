from __future__ import annotations

import hashlib
import io
import json
from typing import TYPE_CHECKING

import pytest
from logopia_studio.checks import verify_critiques
from logopia_studio.host import HermesHost
from logopia_studio.host_api import JsonObject
from logopia_studio.models import ReviewInput, StudioError
from PIL import Image
from pydantic import TypeAdapter
from tests.hermes.test_host_fakes import (
    FakeCompletion,
    FakeContext,
    FakeLlm,
    brief,
    critic_response,
    write_png,
)

if TYPE_CHECKING:
    from pathlib import Path


def review_input(tmp_path: Path, *, parent: bool = True) -> ReviewInput:
    image = tmp_path / "candidate.png"
    data = write_png(image)
    parent_path = tmp_path / "parent.png" if parent else None
    if parent_path:
        _ = write_png(parent_path, "#994433")
    return ReviewInput(
        brief=brief(),
        image_path=image,
        image_sha256=hashlib.sha256(data).hexdigest(),
        parent_path=parent_path,
        keep=("Exact text",),
        change="Open the counter",
    )


def test_independent_critics_receive_four_actual_pngs_with_bound_hashes(tmp_path: Path) -> None:
    request = review_input(tmp_path)
    ctx = FakeContext(llm=FakeLlm([critic_response(), critic_response()]))
    reports = HermesHost(ctx).critique(request)
    verify_critiques(request, reports)
    assert [report.role for report in reports] == ["design", "production"]
    assert len({report.call_id for report in reports}) == 2
    assert len(ctx.llm.calls) == 2
    assert not ctx.dispatches
    for call, report in zip(ctx.llm.calls, reports, strict=True):
        assert call["timeout"] == 120
        assert call["max_tokens"] == 2400
        assert call["purpose"] == f"logopia.critique.{report.role}"
        images = [block for block in call["input"] if block["type"] == "image"]
        assert [block["file_name"] for block in images] == [
            "candidate-original.png",
            "candidate-target.png",
            "parent-original.png",
            "parent-target.png",
        ]
        assert images[0]["data"] == request.image_path.read_bytes()
        assert request.parent_path is not None
        assert images[2]["data"] == request.parent_path.read_bytes()
        for block in images:
            assert block["mime_type"] == "image/png"
            with Image.open(io.BytesIO(block["data"])) as decoded:
                assert decoded.format == "PNG"
                if "target" in block["file_name"]:
                    assert decoded.size == (96, 48)
        assert report.image_sha256 == hashlib.sha256(images[0]["data"]).hexdigest()
        assert report.view_sha256 == hashlib.sha256(images[1]["data"]).hexdigest()
        assert report.parent_sha256 == hashlib.sha256(images[2]["data"]).hexdigest()
        assert report.parent_view_sha256 == hashlib.sha256(images[3]["data"]).hexdigest()
        assert report.view_width == 96
        for block in call["input"]:
            if block["type"] == "text":
                assert critic_response().text not in block["text"]


def test_new_image_has_two_png_inputs_and_no_parent_evidence(tmp_path: Path) -> None:
    request = review_input(tmp_path, parent=False)
    ctx = FakeContext(llm=FakeLlm([critic_response(), critic_response()]))
    reports = HermesHost(ctx).critique(request)
    assert all(report.parent_sha256 is None for report in reports)
    assert all(report.parent_view_sha256 is None for report in reports)
    assert all(
        sum(block["type"] == "image" for block in call["input"]) == 2 for call in ctx.llm.calls
    )


@pytest.mark.parametrize(
    "raw",
    [
        "invalid report",
        "{}",
        '{"summary":"Fine","criteria":[]}',
        '{"summary":"Fine","criteria":[],"score":99}',
    ],
)
def test_invalid_report_retains_prior_report_and_cannot_approve(tmp_path: Path, raw: str) -> None:
    request = review_input(tmp_path)
    first = critic_response()
    ctx = FakeContext(llm=FakeLlm([first, FakeCompletion(raw)]))
    with pytest.raises(StudioError, match="invalid_report") as caught:
        _ = HermesHost(ctx).critique(request)
    assert caught.value.raw_reports == (first.text, raw)
    assert len(ctx.llm.calls) == 2


@pytest.mark.parametrize("invalid_kind", ["duplicate", "invalid_na", "spoofed_evidence"])
def test_semantically_invalid_critic_report_fails_closed(tmp_path: Path, invalid_kind: str) -> None:
    request = review_input(tmp_path)
    payload = TypeAdapter(JsonObject).validate_json(critic_response().text)
    criteria = payload["criteria"]
    assert isinstance(criteria, list)
    assert isinstance(criteria[1], dict)
    if invalid_kind == "duplicate":
        criteria[1]["key"] = "text"
    if invalid_kind == "invalid_na":
        criteria[1]["status"] = "not_applicable"
    if invalid_kind == "spoofed_evidence":
        payload["image_sha256"] = request.image_sha256
    ctx = FakeContext(llm=FakeLlm([FakeCompletion(json.dumps(payload))]))
    with pytest.raises(StudioError, match="invalid_report"):
        _ = HermesHost(ctx).critique(request)
    assert len(ctx.llm.calls) == 1


def test_changed_original_and_missing_parent_prevent_calls(tmp_path: Path) -> None:
    request = review_input(tmp_path)
    ctx = FakeContext()
    _ = write_png(request.image_path, "#000001")
    with pytest.raises(StudioError, match="image_changed"):
        _ = HermesHost(ctx).critique(request)
    request = review_input(tmp_path)
    assert request.parent_path is not None
    request.parent_path.unlink()
    with pytest.raises(StudioError, match="invalid_png"):
        _ = HermesHost(ctx).critique(request)
    assert not ctx.llm.calls


def test_original_changed_during_critique_is_not_an_approved_result(tmp_path: Path) -> None:
    request = review_input(tmp_path)

    def mutate_after_input_read(call: int) -> None:
        if call == 2:
            _ = write_png(request.image_path, "#334455")

    ctx = FakeContext(
        llm=FakeLlm([critic_response(), critic_response()], on_call=mutate_after_input_read)
    )
    with pytest.raises(StudioError, match="image_changed") as caught:
        _ = HermesHost(ctx).critique(request)
    assert len(caught.value.raw_reports) == 2


def test_second_critic_timeout_preserves_first_raw_report(tmp_path: Path) -> None:
    request = review_input(tmp_path)
    first = critic_response()
    timeout = TimeoutError("Second critic exceeded its deadline")
    ctx = FakeContext(llm=FakeLlm([first, timeout]))
    with pytest.raises(StudioError, match="host_timeout") as caught:
        _ = HermesHost(ctx).critique(request)
    assert caught.value.raw_reports == (first.text,)
    assert caught.value.__cause__ is timeout
    assert len(ctx.llm.calls) == 2


def test_original_removed_during_critique_retains_both_raw_reports(tmp_path: Path) -> None:
    request = review_input(tmp_path)

    def remove_original(call: int) -> None:
        if call == 2:
            request.image_path.unlink()

    first = critic_response()
    ctx = FakeContext(llm=FakeLlm([first, first], on_call=remove_original))
    with pytest.raises(StudioError, match="invalid_png") as caught:
        _ = HermesHost(ctx).critique(request)
    assert caught.value.raw_reports == (first.text, first.text)
