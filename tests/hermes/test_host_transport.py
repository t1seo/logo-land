from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest
from logopia_studio.host import HermesHost
from logopia_studio.host_api import JsonObject
from logopia_studio.models import StudioError
from PIL import Image
from pydantic import TypeAdapter
from tests.hermes.test_host_fakes import (
    FakeCompletion,
    FakeContext,
    FakeLlm,
    brief,
    native_receipt,
    planning_responses,
    write_png,
)

if TYPE_CHECKING:
    from pathlib import Path


def test_plan_uses_two_bounded_public_calls_with_brief_as_data() -> None:
    ctx = FakeContext(llm=FakeLlm(planning_responses()))
    result = HermesHost(ctx).plan(brief())
    assert len(result.directions) == 2
    assert result.provider == "test-provider"
    assert result.model == "test-model"
    assert [call["purpose"] for call in ctx.llm.calls] == ["logopia.strategy", "logopia.directions"]
    for call in ctx.llm.calls:
        assert call["timeout"] == 120
        assert call["max_tokens"] == 6000
        assert brief().notes not in call["instructions"]
        first = call["input"][0]
        assert first["type"] == "text"
        assert brief().notes in first["text"]
        assert set(call) == {
            "instructions",
            "input",
            "json_schema",
            "schema_name",
            "timeout",
            "max_tokens",
            "purpose",
        }
    assert not ctx.dispatches


@pytest.mark.parametrize("raw", ["not json", "{}", '{"directions": []}', '{"directions": "yes"}'])
def test_plan_rejects_invalid_director_without_extra_calls(raw: str) -> None:
    responses = planning_responses()
    responses[-1] = FakeCompletion(raw)
    ctx = FakeContext(llm=FakeLlm(responses))
    with pytest.raises(StudioError, match="invalid_report") as caught:
        _ = HermesHost(ctx).plan(brief())
    assert caught.value.raw_reports[-1] == raw
    assert len(ctx.llm.calls) == 2
    assert not ctx.dispatches


def test_generate_once_uses_exact_parent_and_preserves_originals(tmp_path: Path) -> None:
    parent = tmp_path / "parent.png"
    child = tmp_path / "child.png"
    parent_bytes = write_png(parent)
    child_bytes = write_png(child, "#773311")
    raw = native_receipt(child)
    ctx = FakeContext(dispatch_results=[raw])
    result = HermesHost(ctx).generate("Open the joint; keep exact lettering", parent, "opaque")
    assert ctx.dispatches == [
        (
            "image_generate",
            {
                "prompt": "Open the joint; keep exact lettering",
                "aspect_ratio": "square",
                "image_url": str(parent),
            },
        )
    ]
    assert result.path == child
    assert result.receipt == raw
    assert result.provider == "openai-codex"
    assert result.model == "gpt-image-2-medium"
    assert parent.read_bytes() == parent_bytes
    assert child.read_bytes() == child_bytes
    assert not ctx.llm.calls


@pytest.mark.parametrize(
    "raw",
    [
        "not json",
        "[]",
        '{"success":true}',
        '{"success":"true","image":null}',
        (
            '{"success":false,"image":null,"error":"provider failed",'
            '"error_type":"provider_exception"}'
        ),
        '{"success":true,"image":"/missing.png","provider":"p","model":"m"}',
        '{"success":true,"image":"https://example.test/image.png","provider":"p","model":"m"}',
    ],
)
def test_native_failure_keeps_receipt_and_never_retries(raw: str) -> None:
    ctx = FakeContext(dispatch_results=[raw])
    with pytest.raises(StudioError) as caught:
        _ = HermesHost(ctx).generate("One image", None, "opaque")
    assert caught.value.raw_reports == (raw,)
    assert len(ctx.dispatches) == 1
    assert "image_url" not in ctx.dispatches[0][1]
    assert not ctx.llm.calls


@pytest.mark.parametrize("kind", ["missing", "corrupt", "jpeg", "symlink", "directory"])
def test_receipt_success_requires_an_actual_regular_png(tmp_path: Path, kind: str) -> None:
    path = tmp_path / "result.png"
    if kind == "corrupt":
        _ = path.write_bytes(b"\x89PNG\r\n\x1a\ninvalid")
    if kind == "jpeg":
        with Image.new("RGB", (10, 10)) as image:
            image.save(path, format="JPEG")
    if kind == "symlink":
        target = tmp_path / "target.png"
        _ = write_png(target)
        path.symlink_to(target)
    if kind == "directory":
        path.mkdir()
    ctx = FakeContext(dispatch_results=[native_receipt(path)])
    with pytest.raises(StudioError, match="invalid_png"):
        _ = HermesHost(ctx).generate("One image", None, "opaque")
    assert len(ctx.dispatches) == 1


def test_native_receipt_rejects_unknown_fields_and_missing_attribution(tmp_path: Path) -> None:
    path = tmp_path / "output.png"
    _ = write_png(path)
    original = TypeAdapter(JsonObject).validate_json(native_receipt(path))
    for payload in ({**original, "unexpected": True}, {**original, "model": ""}):
        raw = json.dumps(payload)
        ctx = FakeContext(dispatch_results=[raw])
        with pytest.raises(StudioError, match="invalid_receipt"):
            _ = HermesHost(ctx).generate("One image", None, "opaque")
        assert len(ctx.dispatches) == 1


def test_timeout_is_the_same_error_with_no_hidden_dispatch_or_fallback() -> None:
    timeout = TimeoutError("owned deadline")
    ctx = FakeContext(dispatch_results=[timeout])
    with pytest.raises(TimeoutError) as caught:
        _ = HermesHost(ctx).generate("One image", None, "opaque")
    assert caught.value is timeout
    assert len(ctx.dispatches) == 1
    assert not ctx.llm.calls
    planning = FakeContext(llm=FakeLlm([timeout]))
    with pytest.raises(TimeoutError) as caught_plan:
        _ = HermesHost(planning).plan(brief())
    assert caught_plan.value is timeout
    assert len(planning.llm.calls) == 1


def test_missing_parent_and_invalid_background_fail_before_dispatch(tmp_path: Path) -> None:
    ctx = FakeContext()
    with pytest.raises(StudioError, match="invalid_png"):
        _ = HermesHost(ctx).generate("One image", tmp_path / "missing.png", "opaque")
    with pytest.raises(StudioError, match="invalid_background"):
        _ = HermesHost(ctx).generate("One image", None, "unknown")
    assert not ctx.dispatches


def test_parent_returned_as_child_is_rejected_after_exactly_one_dispatch(tmp_path: Path) -> None:
    parent = tmp_path / "parent.png"
    original = write_png(parent)
    raw = native_receipt(parent)
    ctx = FakeContext(dispatch_results=[raw])
    with pytest.raises(StudioError, match="parent_changed") as caught:
        _ = HermesHost(ctx).generate("Open counter", parent, "opaque")
    assert caught.value.raw_reports == (raw,)
    assert len(ctx.dispatches) == 1
    assert parent.read_bytes() == original
