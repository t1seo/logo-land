from __future__ import annotations

import json
from io import BytesIO
from typing import TYPE_CHECKING

import pytest
from PIL import Image
from pydantic import ValidationError

from logo_helper.images import inspect_png
from logo_helper.models import Brief, ProjectError, VisualReview
from logo_helper.storage import safe_path, validate_id

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


@pytest.mark.parametrize("identifier", ["../x", "x/y", "/absolute", "", "A", "a" * 65, "x\\y"])
def test_identifier_rejects_when_value_cannot_be_portable(identifier: str) -> None:
    # Given an identifier that cannot safely name a portable session/artifact.
    # When the boundary parses it.
    with pytest.raises(ProjectError, match="invalid_id"):
        _ = validate_id(identifier)
    # Then it cannot reach a filesystem operation.


@pytest.mark.parametrize(
    "relative", ["../escape", "/absolute/escape", "a/../../escape", "a\\b", "C:/escape"]
)
def test_path_rejects_when_input_escapes_portable_root(tmp_path: Path, relative: str) -> None:
    # Given a traversal or platform-specific absolute path.
    # When the path is resolved below a workspace.
    with pytest.raises(ProjectError, match="unsafe_path"):
        _ = safe_path(tmp_path.resolve(), relative)
    # Then no escaped path is returned.


@pytest.mark.parametrize("field", ["brand_name", "industry", "audience"])
def test_brief_rejects_when_required_description_is_whitespace(field: str) -> None:
    # Given an otherwise complete brief with an empty semantic field.
    payload = {
        "brand_name": "brand",
        "exact_text": "brand",
        "industry": "design",
        "audience": "all",
    }
    payload[field] = " \n\t"
    # When JSON crosses the brief boundary.
    with pytest.raises(ValidationError):
        _ = Brief.model_validate_json(json.dumps(payload))
    # Then blank content cannot masquerade as supplied intent.


def test_review_rejects_when_boolean_is_text(harness: Harness) -> None:
    # Given text instead of an explicit boolean assessment.
    payload = harness.review.read_text(encoding="utf-8").replace(
        '"text_correct": true', '"text_correct": "true"'
    )
    # When parsing the review boundary.
    with pytest.raises(ValidationError):
        _ = VisualReview.model_validate_json(payload)
    # Then coercion cannot accidentally approve an artifact.


def test_brief_accepts_explicit_concept_count_above_default(harness: Harness) -> None:
    # Given a user who explicitly requested twenty-four concepts.
    payload = harness.brief.read_text(encoding="utf-8").removesuffix("}")
    # When the request is parsed.
    brief = Brief.model_validate_json(payload + ', "concept_count": 24}')
    # Then the helper preserves the requested count without enforcing a batch size.
    assert brief.concept_count == 24


def test_inspect_when_palette_png_has_real_transparency() -> None:
    # Given a palette PNG with a transparent palette entry and visible logo pixels.
    with BytesIO() as stream, Image.new("P", (2, 2), 1) as image:
        image.putpalette([0, 0, 0, 0, 150, 50] + [0] * 762)
        image.putpixel((0, 0), 0)
        image.save(stream, format="PNG", transparency=0)
        payload = stream.getvalue()
    # When fully decoded.
    facts = inspect_png(payload)
    # Then palette transparency is measured, not inferred from the mode string.
    assert facts.transparent_pixels == 1
    assert facts.visible_pixels == 3
    assert facts.alpha_min == 0
    assert facts.alpha_max == 255


def test_inspect_when_rgba_is_opaque() -> None:
    # Given an RGBA image whose alpha channel is uniformly opaque.
    with BytesIO() as stream, Image.new("RGBA", (2, 2), "green") as image:
        image.save(stream, format="PNG")
        payload = stream.getvalue()
    # When inspected.
    facts = inspect_png(payload)
    # Then presence of an alpha channel does not assert transparency.
    assert not facts.has_transparency
    assert facts.transparent_pixels == 0


def test_inspect_rejects_when_png_is_animated() -> None:
    # Given a real animated PNG with two frames.
    with (
        BytesIO() as stream,
        Image.new("RGB", (2, 2), "green") as first,
        Image.new("RGB", (2, 2), "blue") as second,
    ):
        first.save(
            stream, format="PNG", save_all=True, append_images=[second], duration=100, loop=0
        )
        payload = stream.getvalue()
    # When imported as a static logo.
    with pytest.raises(ProjectError, match="Animated"):
        _ = inspect_png(payload)
    # Then multi-frame content is rejected.


@pytest.mark.parametrize("missing_bytes", [1, 4, 8, 12])
def test_inspect_rejects_when_png_end_is_truncated(missing_bytes: int) -> None:
    # Given a decodable raster with an incomplete PNG termination chunk.
    with BytesIO() as stream, Image.new("RGB", (2, 2), "green") as image:
        image.save(stream, format="PNG")
        payload = stream.getvalue()[:-missing_bytes]
    # When checking the actual delivered file.
    with pytest.raises(ProjectError, match="PNG"):
        _ = inspect_png(payload)
    # Then permissive decoder behavior cannot admit a truncated file.
