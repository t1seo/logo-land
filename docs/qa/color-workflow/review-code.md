# Independent code-quality review

Date: 2026-09-13 KST. Task: `task_c9c54f6ab7e6`; dispatch: `ctx_49a670eb6bcb`.
Base: `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`. Scope: the uncommitted implementation, including new production modules.

**Code-quality verdict: FAIL. Confidence: HIGH.** One reproducible compatibility regression needs correction before approval. The focused existing tests pass, and recomputation of all 17 stored native artifacts agrees with their latest reports, but those checks do not cover the legacy export failure below.

**Development-preview commit approval: NO for the reviewed implementation until C1 is corrected and rechecked.** The documentation may truthfully describe unfinished development; this is not a request to discard the implementation or evidence. After the compatibility fix, development-preview readiness can be reconsidered independently of native-image success.

**Whole-goal/public-release verdict: FAIL.** Required restricted-color and white-transparent native successes remain missing. Correcting C1 would not clear those separate release gates.

## Findings

### C1 — MAJOR: optional color analysis newly blocks a previously exportable legacy PNG

Primary location: [color_delivery.py:82](../../../skills/logo-land/scripts/logo_helper/color_delivery.py#L82). Related locations: [reference_decode.py:95](../../../skills/logo-land/scripts/logo_helper/reference_decode.py#L95), [color_analysis.py:161](../../../skills/logo-land/scripts/logo_helper/color_analysis.py#L161), [delivery.py:136](../../../skills/logo-land/scripts/logo_helper/delivery.py#L136).

`export_colors` calls `analyze_png` unconditionally, including when the selected artifact has no structured palette. The new reference decoder rejects EXIF orientation outside 1–8. The existing PNG import/resume validator accepts a static, fully decodable PNG carrying orientation 0, and the base version successfully exports that same PNG. Current import, review and selection still succeed, but export now returns `invalid_reference` instead of delivering the color-unverified original. This also occurs when resuming an actual schema-1 session written by the base CLI.

The EXIF value is invalid metadata; the regression is imposing this new analysis prerequisite on the otherwise accepted legacy delivery path. No assertion is made that such metadata should count as valid color evidence. The plan explicitly preserves palette-less export behavior ([contract 10](../../../plans/logo-land-color-workflow.md#locked-implementation-contract)).

Reproduction uses the existing NORTHLINE PNG with only an ancillary `eXIf` chunk added. Decoded pixel bytes are asserted identical to the original; no logo pixels are changed and no image tool is invoked. The base and current failure cases use exactly the same fixture SHA-256, `fe3433fe90168197446e4df3cd1f472a555759db5aa7cff8fe2703f6d729f87e`.

| CLI/input | Init/import/review/select | Export |
| --- | --- | --- |
| Base fd1, EXIF orientation 0 | All exit 0 | Exit 0; original PNG delivered |
| Current source, identical orientation-0 PNG | All exit 0 | Exit 1; no delivery |
| Current source, only orientation changed to 1 | All exit 0 | Exit 0; original PNG delivered |
| Current source resuming base-created schema-1 orientation-0 session | Base session remains readable | Exit 1; same error |

Actual failure:

```json
{"error": "invalid_reference: EXIF orientation must be an integer from 1 to 8"}
```

Exact fixture/CLI reproduction is retained locally at `output/review-code/metadata-probe.sh`; output is `output/review-code/metadata-probe.txt`. It expects the source snapshot produced by:

```sh
mkdir -p output/review-code/baseline
git archive fd1d89c66e2fb2193954a5ee732cd1a688bdba6d skills/logo-land/scripts |
  tar -x -C output/review-code/baseline
sh output/review-code/metadata-probe.sh
```

The script deliberately creates new case directories and refuses to overwrite a prior run. The independent legacy-resume failure is retained in `output/review-code/legacy-resume.stderr` and can be repeated against the existing fixture:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python skills/logo-land/scripts/logo_project.py \
  --workspace output/review-code/metadata-probe/base-orientation-0 \
  export --session demo --revision 4 --output resumed-current
```

Suggested correction: preserve accepted palette-less exports with a truthful unverified analysis result/reason when optional analysis cannot interpret metadata. Keep original-byte integrity, visual/background checks, strict reference validation and strict color refusal intact. Add regression coverage using a real schema-1 session, and check the analogous advisory-analysis failure boundary. No general bypass or PNG rewrite is needed.

## Code and contract assessment

Read full contents of every changed/new production Python module and the unchanged PNG decoder; inspected the tracked base diff, all ten new color/palette/reference test modules, changed tests and relevant transaction, background and portability tests. The production tree has 37 Python files; the largest is the 214-line CLI, below the module ceiling even before removing comments and blanks.

| Area | Assessment |
| --- | --- |
| Parsing and types | Frozen, strict, extra-forbidden Pydantic boundaries; tuples for persisted collections; explicit schema-integer validation; normalized HEX and digest validation. No new type escape hatch found. |
| Transactions and migration | Cooperative locks and revision checks precede writes; import/reference files roll back on commit failure; export publication rolls back its files/directories; v1 reads remain in memory, with verified exact-byte backup reuse on migration retry. |
| Immutable provenance | Save compares immutable history prefixes; artifact reviews are intentionally replaceable. Palette/reference/report IDs and hashes/digests are bound through the session graph. Original PNG hashes/facts are checked on load and bytes rechecked for export. |
| Palette math | One lazy ColorAide engine, explicit Lab D50/CIEDE2000 and WCAG2 compositing, OKLCH companion generation, unchanged locks, deterministic deduplication. Direct runtime inspection produced three distinct three-color recipes for the default green seed. |
| Analysis bounds | 64 MiB/40M-pixel decode limits and at most 16,384 original-coordinate samples. Full decode/profile buffers still scale to the pixel cap; sampling is not a claim of constant-memory image decoding. White is retained and alpha-zero RGB excluded. |
| Sampled reports | Required/locked presence, restricted coverage, minor matched groups, alpha/core thresholds, profile uncertainty and ROI scope agree with the declared policy. All 17 actual native reports reproduced exactly. |
| Export enforcement | Strict reports are freshly recomputed with fixed thresholds; forged saved metrics cannot authorize output. Latest explicit ROI remains disclosed. Original PNG, three ZIP members and selected artifact palette/lockup remain authoritative. C1 is the non-strict compatibility exception. |
| CLI and layout intent | Additive flat commands, shared prompt/import intent precedence, stale-revision rejection and legacy background omission semantics remain explicit. Requested fonts are appearance references only. |
| Complexity | The focused model/math/analysis/transaction/presentation split is justified. Frozen schema-1 definitions isolate compatibility intentionally. No speculative abstraction or separate implementation of color math warranted another finding. |

## Verification performed

The reviewer independently ran the following existing tests without dependency installation or source modification:

```sh
PYTHONDONTWRITEBYTECODE=1 uv run --locked --no-sync pytest -p no:cacheprovider \
  --basetemp output/review-code/pytest \
  tests/test_color_models.py tests/test_palette_engine.py \
  tests/test_palette_compatibility.py tests/test_color_analysis.py \
  tests/test_color_reports.py tests/test_color_workflow_transactions.py \
  tests/test_background_compatibility.py
```

Result: **144 passed in 33.92s**. Local log: `output/review-code/focused-tests.txt`. These include real CLI subprocesses and deliberate failed-commit, forged-report, missing-engine, policy-boundary and legacy-migration cases. C1 was then reproduced separately using the real base/current CLIs, including the metadata-only control and schema-1 resume.

Read-only native recomputation loaded actual live sessions, read the corresponding public PNG copies, checked their recorded hashes through `analyze_png`, and compared every field of the recomputed latest report using its saved report ID/time/scope/surfaces. **All 17 artifacts matched completely**, including white-v3: 2,560 core, 923 partial-alpha, 3,483 visible samples, `indeterminate`. Local log: `output/review-code/native-recompute.txt`. An initial verification-harness attempt treated editorial public session summaries as persisted `Session` objects and correctly failed strict parsing; the completed check used the actual session store instead.

The implementation's separate **299-test** and Ruff/basedpyright/format results were read from the supplied evidence, not claimed as additional full-suite runs by this reviewer. Source hashes and the tracked diff reviewed here are retained under `output/review-code/`. No source change, commit, push, installation, Chrome control, native generation or pixel edit was performed.

## Release and remaining work

Reviewed `review-context.md`, both READMEs, the full color plan, validation overview, structured native case evidence, `native-cases.md`, `chrome-live.md` and `installation-040.md`. During the review, the coordinator corrected README release wording; the latest inspected text clearly distinguishes development 0.4.0 from published 0.3.1. No stale README wording is reported as an outstanding finding.

The evidence accurately separates 8 requests, 16 native calls and 17 stored artifacts, with only NORTHLINE, GROVE and TIDE exported. A passing anchor-only histogram does not excuse GROVE warm edits' opaque checkerboards. The clean-looking white preview remains quantitatively indeterminate; restricted/white success requirements remain unmet. The 15 installed-helper calls and 46 Chrome screenshots are prior worker evidence, not new actions by this reviewer.

Blocking code issue: **C1**. Blocking release issues: required restricted-color and white-transparent native success evidence, plus completion of the independent review/fix gates. This reviewer has completed its assigned perspective and does not wait for or approve the other reviewers' work. A targeted compatibility fix and re-review are still needed; the essential native gates remain required afterward.
