# T2 palette engine evidence

Date: 2026-09-13 KST. Scope: deterministic palette library and shared color math only.
No CLI registration, session/state writes, native image calls, commits or dependency installation
were performed by this worker. T1 supplied shared frozen models and ColorAide 8.12.1.

## Public API for T4 and T3

All imports below are from `skills/logo-land/scripts/logo_helper`. The request and result inherit
T1's strict, frozen, extra-forbid Pydantic base; shared types are imported, not replaced.

```python
from logo_helper.palettes import (
    PaletteRequest, PaletteProposal, propose_palette, propose_palettes, validate_candidate,
)

PaletteRequest(
    seed_hex: HexColor = "#247A52",
    constraints: ColorConstraints = ColorConstraints(),
    source: Literal["local_harmony", "reference", "assistant", "leonardo"] = "local_harmony",
    source_evidence: SourceEvidence = SourceEvidence(),
    selected_by: Literal["assistant", "user"] = "assistant",
    rationale: Text | None = None,
    swatches: tuple[Swatch, ...] = (),
    extracted_colors: tuple[HexColor, ...] = (),
)
PaletteProposal(candidates: tuple[PaletteContent, ...], warnings: tuple[Text, ...] = ())

propose_palette(request: PaletteRequest, *, recipe: HarmonyRecipe = "analogous") -> PaletteContent
propose_palettes(request: PaletteRequest) -> PaletteProposal
validate_candidate(candidate: PaletteContent, *, constraints: ColorConstraints) -> PaletteContent

# logo_helper.color_math
HarmonyRecipe = Literal["monochromatic", "analogous", "complementary"]
harmony_colors(seed: str, recipe: HarmonyRecipe) -> tuple[str, ...]
engine_version() -> str
delta_e(first: str, second: str) -> float
contrast_ratio(foreground: str, surface: str, *, alpha: float = 1.0) -> float
```

`propose_palettes` returns three distinct local recipe candidates in the order above when possible.
Constraints can reduce that number; duplicate color sets collapse with a warning. A supplied
assistant/Leonardo palette returns one validated candidate. Reference input returns one candidate.
T4 supplies the `{session_id, revision, candidates, warnings}` read-only CLI envelope.

External assistant/Leonardo input uses `swatches`; the first role for each normalized HEX wins.
Missing locks, missing required colors, disallowed colors and excessive counts raise
`constraint_conflict`; no replacement colors or silent local fallback are inserted. The standalone
validator composes the candidate's existing policy with the incoming one, intersecting allowed sets,
taking the tighter count, and retaining both sets of mandatory colors.

Reference input requires `extracted_colors` plus `SourceEvidence.reference_id` and
`reference_sha256`. Integration with T3 is:

```python
extraction = extract_palette(reference_bytes)
request = PaletteRequest(
    source="reference",
    extracted_colors=tuple(swatch.hex for swatch in extraction.swatches),
    source_evidence=SourceEvidence(
        reference_id=reference.id,
        reference_sha256=reference.sha256,
        notes=("Full-image extraction; visible opaque background consumes a color slot.",),
    ),
    constraints=ColorConstraints(locked_hex=("#247A52",), max_colors=2),
)
proposal = propose_palettes(request)
```

The caller retains extraction status/scope/profile limitations and binds the evidence to its
managed reference. Extraction estimates do not become conformance evidence. `SourceEvidence`
provider/tool/response/notes values remain inert metadata. Missing/ambiguous source payloads return
`invalid_palette_request`; malformed HEX returns `invalid_color`.

## Algorithms and scope

- Seeds, locks, required colors and external/reference colors normalize through T1's HEX boundary.
  Exact locked sRGB is inserted before any candidate trimming; every mandatory color survives.
- Ordinary candidates prefer three colors. An explicit maximum is a ceiling rather than a requested
  exact size. Four to eight mandatory colors override the ordinary preference. More than eight
  mandatory colors cannot form a supported palette and fail at the request boundary.
- Chromatic seeds use ColorAide `harmony("mono"|"analogous"|"complement", space="oklch",
  out_space="oklch")`. Monochromatic/analogous take endpoint companions; complementary uses the
  opposite hue and its OKLCH lightness-0.82 companion.
- For achromatic anchors, recipe order selects preset companion hues **45°, 145°, 250°**. Each uses
  OKLCH `(L, C) = (0.55, 0.10)` and `(0.82, 0.06)`. The neutral anchor itself remains unchanged.
  These are documented neutral-anchor exceptions to the chromatic harmony recipes.
- Only generated companions map to sRGB with explicit `method="oklch-chroma"`; short HEX output,
  alpha and implicit compression are disabled. Local allowed-set ordering uses nearest generated
  color distance followed by HEX as a stable tie breaker. Repeated distances share a call-scoped
  cache, with no persistent/global result cache.
- Delta E explicitly uses CIEDE2000 `method="2000", space="lab"` after Lab D50 conversion.
  Merely converting the inputs to Lab D50 would not override ColorAide's default distance whitepoint.
- Contrast explicitly uses source-over compositing in sRGB and `method="wcag21"`. It is readability
  guidance, without a logo pass/fail threshold.
- ColorAide imports only at calculation time. A missing import raises `color_engine_unavailable`;
  no installer, network client or state writer exists in these modules. External literal-color
  validation works without ColorAide.

Primary references: [ColorAide harmonies](https://facelessuser.github.io/coloraide/harmonies/),
[CIEDE2000 and Lab D50](https://facelessuser.github.io/coloraide/distance/), and
[explicit OKLCH gamut mapping](https://facelessuser.github.io/coloraide/gamut/).
The installed pinned package source was also inspected for supported recipe names and method flags.

## TDD and verification log

1. Existing-test baseline was started before T2 production work:
   `uv run --locked pytest -q --ignore=tests/test_color_models.py --ignore=tests/test_palette_compatibility.py`.
   It returned **84 passed, 12 failed in 102.41s**. T1 changed shared state from schema 1 to schema 2
   during that run, so the old in-process models rejected new CLI records; failures also included
   copied-script portability during dependency/bootstrap edits. This is a recorded shared-checkout
   transition, not a claimed clean baseline or a T2 regression. The coordinator was notified.
2. First red: `uv run --locked pytest -q tests/test_palette_engine.py` returned **1 failed**,
   `AttributeError: module 'logo_helper.palettes' has no attribute 'PaletteRequest'`.
   Collection succeeded; the empty owned module existed and the requested public API did not.
3. First green: the same command returned **1 passed in 0.09s**, using real ColorAide calculations.
4. Expanded red: `uv run --locked pytest -q tests/test_palette_engine.py --tb=short` returned
   **16 failed, 13 passed in 0.20s**. Failures named missing external validation/metrics and missing
   source-specific behavior, rather than unrelated import errors.
5. Expanded green: T2 plus T1 color-model tests returned **59 passed in 0.41s**.
6. After T1 explicitly announced models/dependencies ready, a fresh process ran
   `uv run --locked pytest -q tests/test_palette_engine.py tests/test_color_models.py tests/test_palette_compatibility.py --tb=short`:
   **69 passed in 17.75s**. This includes schema compatibility tests against the actual new models.
7. Added adversarial coverage and a real T3 extraction integration test; T2 plus T1 color models:
   **68 passed in 0.92s**.
8. `uv run --locked basedpyright skills/logo-land/scripts/logo_helper/color_math.py skills/logo-land/scripts/logo_helper/palettes.py tests/test_palette_engine.py`:
   **0 errors, 0 warnings, 0 notes**.
9. `uv run --locked ruff check` on the same files: **All checks passed!**
10. The programming skill's actual `check-no-excuse-rules.py` on the same files:
    **no violations in 3 file(s)**. Its initial `--help` probe returned exit 2 because this checker
    accepts only file/directory arguments; the corrected explicit-file invocation passed.
11. Final fresh-process run of T2 + T1 models + compatibility:
    **79 passed in 15.66s**. Final Ruff check passed; Ruff format check reported
    **3 files already formatted**; basedpyright again reported **0 errors, 0 warnings, 0 notes**.
    Nonblank/noncomment line counts: `color_math.py` **79**, `palettes.py` **164**,
    `test_palette_engine.py` **203**; each is below the 250 LOC ceiling.

Covered boundaries include short/full duplicate HEX, neutral black/white/gray, exact saturated locks,
one/four/eight-color ceilings, contradictory constraints, disallowed external colors, missing locks
and requirements, additive existing policies, unknown input keys, missing source evidence, malformed
CSS/alpha HEX, alpha NaN/infinity/range rejection, engine absence, and reference + lock + count.

## Manual library execution

Executed a real interpreter via `PYTHONPATH=skills/logo-land/scripts uv run --locked python -`.
The driver imported the public API, printed normalized results, called T3 `extract_palette` on
synthetic PNG bytes, exercised rejection paths, and temporarily blocked the engine import in that
process. Exit status was **0**. This is local module/fixture QA, not native logo-generation evidence.

Input:

```json
{"constraints":{"locked_hex":["#247a52"]}}
```

Observed candidate arrays, each with `source="local_harmony"`, `selected_by="assistant"`, roles
`primary` / `companion 1` / `companion 2`, and `calculation_version="logo-color-v1"`:

```json
[
  ["#247A52", "#02140A", "#B8D2C2"],
  ["#247A52", "#56742E", "#007B74"],
  ["#247A52", "#8E4F7C", "#F1AADA"]
]
```

Repeated full `model_dump_json()` comparison returned `true`.

Manual reference fixture: 32×32 RGB PNG; half white and half RGB(255,128,32); SHA256
`ccf63404daf75d93ba6d55d1b26df13546962583d7d40fb157950448db1cac95`.
Actual extraction produced `#FF8020` and `#FFFFFF`, 512 samples/0.5 share each, `full_image`,
`all_pixels`, 1024 visible/core samples, `assumed_srgb`, status `extracted`, no reasons.
Adding locked `#247A52` and `max_colors=2` produced:

```json
{"colors":["#247A52","#FF8020"],"source":"reference","max_colors":2,
 "reference_id":"manual-ref",
 "reference_sha256":"ccf63404daf75d93ba6d55d1b26df13546962583d7d40fb157950448db1cac95"}
```

Other actual observations:

```text
External #AABBCC replacing #247A52 -> constraint_conflict: Palette is missing a locked or required color
Malformed #GG0000 -> invalid_color
Missing ColorAide -> color_engine_unavailable: ColorAide is unavailable; prepare the declared dependencies
Engine version -> 8.12.1
Red/blue Delta E00 D50 -> 55.79977339019779
Opaque black/white WCAG2 -> 20.999999999999996
Half-alpha black/white WCAG2 -> 3.976653024912437
```

Separate manual neutral requests returned these companion pairs for black, white and gray anchors:

```json
[["#A15D3E","#E6B9A4"],["#49814C","#ADCFAD"],["#4075AA","#A7C8EA"]]
```

The leading anchor remained `#000000`, `#FFFFFF` or `#888888` respectively.

## Cleanup and remaining integration

Only the four assigned files were written. Manual PNGs stayed in `BytesIO`; no image files or
projects were left behind. Pytest fixtures use its temporary directories; import monkeypatches
restore automatically, and the manual import blocker was restored in `finally`. No changes were
made to the plan, Boulder state, shared ledger, T1 models, dependency manifest or lockfile.

No subagents were spawned, as explicitly required by this dispatch. The review-work skill's
goal/quality/security/QA/context checks were applied locally; the plan's independent five-reviewer
release gate remains coordinator-owned, as do CLI registration, native image QA and publication.
