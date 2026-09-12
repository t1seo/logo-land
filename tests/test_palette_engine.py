from __future__ import annotations

import importlib
import json
import math
import sys
from hashlib import sha256
from io import BytesIO

import pytest
from PIL import Image
from pydantic import ValidationError

from logo_helper import color_math, palettes
from logo_helper.color_models import ColorConstraints, PaletteContent, SourceEvidence, Swatch
from logo_helper.model_base import ProjectError, ReferenceId
from logo_helper.references import extract_palette


def test_three_deterministic_recipes_when_anchor_is_locked() -> None:
    # Given an exact anchor that every candidate must retain.
    request = palettes.PaletteRequest(constraints=ColorConstraints(locked_hex=("#247A52",)))
    # When the same structured request is proposed twice.
    first, second = palettes.propose_palettes(request), palettes.propose_palettes(request)
    # Then colors and ordering are byte equivalent and every candidate keeps the anchor.
    assert first.model_dump_json() == second.model_dump_json()
    assert len(first.candidates) == 3
    assert len({tuple(swatch.hex for swatch in item.swatches) for item in first.candidates}) == 3
    assert all("#247A52" in {s.hex for s in item.swatches} for item in first.candidates)


@pytest.mark.parametrize("anchor", ["#000", "#fff", "#888"])
def test_valid_companions_when_anchor_is_achromatic(anchor: str) -> None:
    # Given a neutral locked anchor.
    request = palettes.PaletteRequest(constraints=ColorConstraints(locked_hex=(anchor,)))
    # When three recipes are calculated.
    result = palettes.propose_palettes(request)
    # Then all preset companion hues are finite and the anchor survives exactly.
    assert len(result.candidates) == 3
    for candidate, hue in zip(result.candidates, color_math.ACHROMATIC_HUES, strict=True):
        assert candidate.swatches[0].hex == request.constraints.locked_hex[0]
        measured = color_math.color_type()(candidate.swatches[1].hex).convert("oklch").coords()
        assert all(math.isfinite(value) for value in measured)
        assert abs(measured[2] - hue) < 3


def test_reference_evidence_when_lock_and_count_compose() -> None:
    # Given a real extraction payload and a separately requested anchor.
    evidence = SourceEvidence(reference_id=ReferenceId("ref1"), reference_sha256="a" * 64)
    request = palettes.PaletteRequest(
        source="reference",
        extracted_colors=("#fff", "#fedcba", "#000"),
        source_evidence=evidence,
        constraints=ColorConstraints(locked_hex=("#247A52",), max_colors=2),
    )
    # When converting the extraction to a constrained proposal.
    result = palettes.propose_palettes(request)
    # Then it retains the anchor, first extracted color, count and provenance.
    assert len(result.candidates) == 1
    assert tuple(s.hex for s in result.candidates[0].swatches) == ("#247A52", "#FFFFFF")
    assert result.candidates[0].source_evidence == evidence
    assert result.candidates[0].source == "reference"


@pytest.mark.parametrize("source", ["assistant", "leonardo"])
def test_normalized_external_candidate_when_duplicate_short_hex_is_given(source: str) -> None:
    # Given externally supplied colors with normalized duplicates.
    request = palettes.PaletteRequest.model_validate_json(
        json.dumps(
            {
                "source": source,
                "swatches": [
                    {"hex": "#abc", "role": "primary"},
                    {"hex": "#AABBCC", "role": "duplicate"},
                    {"hex": "#fff", "role": "accent"},
                ],
                "constraints": {"locked_hex": ["#abc"], "max_colors": 2},
            }
        )
    )
    # When the external input is validated.
    result = palettes.propose_palettes(request)
    # Then the first role wins, locks remain exact and no local colors replace the source.
    assert len(result.candidates) == 1
    assert tuple((s.hex, s.role) for s in result.candidates[0].swatches) == (
        ("#AABBCC", "primary"),
        ("#FFFFFF", "accent"),
    )
    assert result.candidates[0].source == source


@pytest.mark.parametrize(
    "constraints",
    [
        ColorConstraints(locked_hex=("#247A52",)),
        ColorConstraints(required_hex=("#247A52",)),
        ColorConstraints(allowed_hex=("#000",)),
        ColorConstraints(max_colors=1),
    ],
)
def test_rejected_external_candidate_when_it_breaks_constraints(
    constraints: ColorConstraints,
) -> None:
    # Given an external suggestion that violates the independently supplied policy.
    candidate = PaletteContent(
        swatches=(Swatch(hex="#fff", role="primary"), Swatch(hex="#abc", role="accent")),
        source="leonardo",
        selected_by="assistant",
        rationale="Suggestion",
    )
    # When that policy is applied at the shared validation boundary.
    with pytest.raises(ProjectError, match="constraint_conflict"):
        _ = palettes.validate_candidate(candidate, constraints=constraints)
    # Then the rejected original remains unchanged.
    assert candidate.constraints == ColorConstraints()


def test_constraints_are_combined_when_external_candidate_already_has_policy() -> None:
    # Given an externally recorded lock and an additional user count limit.
    candidate = PaletteContent(
        swatches=(Swatch(hex="#fff", role="primary"),),
        constraints=ColorConstraints(locked_hex=("#fff",)),
        source="assistant",
        selected_by="user",
        rationale="Retain white",
    )
    # When an additional policy is validated.
    result = palettes.validate_candidate(candidate, constraints=ColorConstraints(max_colors=1))
    # Then neither old nor new constraints are lost.
    assert result.constraints.locked_hex == ("#FFFFFF",)
    assert result.constraints.max_colors == 1


def test_allowed_subset_when_all_colors_are_not_required() -> None:
    # Given an allowed set larger than the requested count.
    request = palettes.PaletteRequest(
        constraints=ColorConstraints(
            allowed_hex=("#000", "#fff", "#abc"), required_hex=("#abc",), max_colors=2
        )
    )
    # When local proposals must stay inside that set.
    result = palettes.propose_palettes(request)
    # Then all candidates keep requirements without requiring the entire allowed set.
    assert all(len(item.swatches) <= 2 for item in result.candidates)
    assert all("#AABBCC" in {s.hex for s in item.swatches} for item in result.candidates)
    assert all(
        {s.hex for s in item.swatches} <= {"#000000", "#FFFFFF", "#AABBCC"}
        for item in result.candidates
    )


@pytest.mark.parametrize(
    "raw",
    [
        '{"constraints":{"locked_hex":["#000","#fff","#abc"],"max_colors":2}}',
        '{"constraints":{"allow_gradients":true,"max_colors":2}}',
        '{"constraints":{"locked_hex":["#000"],"allowed_hex":["#fff"]}}',
    ],
)
def test_conflict_before_calculation_when_constraints_are_impossible(raw: str) -> None:
    # Given inconsistent structured constraints.
    # When parsing the request, before any engine call.
    with pytest.raises(ProjectError, match="constraint_conflict"):
        _ = palettes.PaletteRequest.model_validate_json(raw)
    # Then there is no request to persist or generate from.


@pytest.mark.parametrize(
    "raw",
    [
        '{"seed_hex":"#GG0000"}',
        '{"source":"leonardo","swatches":[{"hex":"red","role":"primary"}]}',
        '{"extracted_colors":["#12345678"]}',
    ],
)
def test_invalid_hex_when_request_crosses_boundary(raw: str) -> None:
    # Given invalid CSS or alpha-bearing HEX at any input source.
    # When parsing the request.
    with pytest.raises(ProjectError, match="invalid_color"):
        _ = palettes.PaletteRequest.model_validate_json(raw)
    # Then invalid colors cannot reach ColorAide.


@pytest.mark.parametrize(
    "raw",
    [
        '{"source":"reference"}',
        '{"source":"assistant"}',
        '{"source":"leonardo"}',
        '{"swatches":[{"hex":"#abc","role":"primary"}]}',
        '{"source":"reference","extracted_colors":["#abc"]}',
    ],
)
def test_source_input_rejected_when_missing_or_ambiguous(raw: str) -> None:
    # Given missing source evidence or a payload incompatible with its source.
    # When parsing source-specific input.
    with pytest.raises(ProjectError, match="invalid_palette_request"):
        _ = palettes.PaletteRequest.model_validate_json(raw)
    # Then no fabricated local candidate can masquerade as a reference or provider response.


def test_missing_engine_when_calculation_is_requested(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given the optional package is unavailable in this interpreter.
    monkeypatch.setitem(sys.modules, "coloraide", None)
    # When importing the math module and then requesting a calculation.
    _ = importlib.reload(color_math)
    with pytest.raises(ProjectError, match="color_engine_unavailable"):
        _ = palettes.propose_palettes(palettes.PaletteRequest())
    # Then importing was safe and calculation named the missing engine without installing it.


def test_explicit_color_metrics_when_known_reference_pairs_are_used() -> None:
    # Given red/blue distinguish D50 from the library default D65.
    # When requesting explicit CIEDE2000 and WCAG2 calculations.
    difference = color_math.delta_e("#f00", "#00f")
    ratio = color_math.contrast_ratio("#000", "#fff")
    # Then the result matches D50 and opaque contrast reference values.
    assert difference == pytest.approx(55.79977339019779)
    assert ratio == pytest.approx(21)
    assert color_math.engine_version() == "8.12.1"


@pytest.mark.parametrize(("alpha", "expected"), [(0.0, 1.0), (0.5, 3.976653024912438)])
def test_contrast_compositing_when_foreground_is_translucent(alpha: float, expected: float) -> None:
    # Given black ink composited over opaque white in sRGB.
    # When requesting contrast at an explicit alpha.
    ratio = color_math.contrast_ratio("#000", "#fff", alpha=alpha)
    # Then the preview surface participates in the result.
    assert ratio == pytest.approx(expected)


def test_frozen_strict_boundary_when_request_has_unknown_keys() -> None:
    # Given a misspelled policy key.
    # When parsing the boundary JSON.
    with pytest.raises(ValidationError, match="extra_forbidden"):
        _ = palettes.PaletteRequest.model_validate_json('{"maxcolors":2}')
    # Then typos cannot silently relax requested constraints.


@pytest.mark.parametrize("count", [1, 4, 8])
def test_every_lock_survives_when_count_is_tight(count: int) -> None:
    # Given exact saturated locks at the count limit, exceeding the ordinary three-color preference.
    colors = ("#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#FFF", "#000")[
        :count
    ]
    constraints = ColorConstraints(locked_hex=colors, max_colors=count)
    # When recipes are deduplicated under the restrictive policy.
    result = palettes.propose_palettes(palettes.PaletteRequest(constraints=constraints))
    # Then no lock is gamut-mapped, dropped or multiplied into redundant candidates.
    assert len(result.candidates) == 1
    assert tuple(s.hex for s in result.candidates[0].swatches) == constraints.locked_hex
    assert result.warnings


@pytest.mark.parametrize("alpha", [-0.1, 1.1, float("nan"), float("inf")])
def test_invalid_alpha_when_contrast_crosses_boundary(alpha: float) -> None:
    # Given out-of-range or non-finite alpha.
    # When calculating surface contrast.
    with pytest.raises(ProjectError, match="invalid_alpha"):
        _ = color_math.contrast_ratio("#000", "#fff", alpha=alpha)
    # Then alpha cannot silently produce a false ratio.


def test_external_validation_when_engine_is_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given an unavailable engine and a valid explicitly supplied palette.
    monkeypatch.setitem(sys.modules, "coloraide", None)
    request = palettes.PaletteRequest(
        source="assistant", swatches=(Swatch(hex="#fff", role="ink"),)
    )
    # When validation needs no numerical color calculation.
    result = palettes.propose_palette(request)
    # Then a literal white palette remains usable without the engine.
    assert result.swatches == request.swatches


def test_real_reference_extraction_when_composed_with_lock_and_count() -> None:
    # Given synthetic PNG bytes with visible white and orange artwork, plus real extraction output.
    with Image.new("RGB", (32, 32), "white") as image, BytesIO() as buffer:
        image.paste((255, 128, 32), (16, 0, 32, 32))
        image.save(buffer, format="PNG")
        data = buffer.getvalue()
    extraction = extract_palette(data)
    request = palettes.PaletteRequest(
        source="reference",
        extracted_colors=tuple(s.hex for s in extraction.swatches),
        source_evidence=SourceEvidence(
            reference_id=ReferenceId("fixture"), reference_sha256=sha256(data).hexdigest()
        ),
        constraints=ColorConstraints(locked_hex=("#247A52",), max_colors=2),
    )
    # When the T3 extraction is converted through the public T2 request.
    result = palettes.propose_palette(request)
    # Then the extraction scope remains real and the combined palette satisfies every constraint.
    assert extraction.sampling.core_samples == 1024
    assert tuple(s.hex for s in result.swatches) == ("#247A52", extraction.swatches[0].hex)
    assert result.source_evidence.reference_sha256 == sha256(data).hexdigest()
