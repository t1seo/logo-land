# Independent correction re-review: C1 and G3

Date: 2026-09-13 KST. Orca run: `run_c07646c87b07`; task: `task_6ef98b414999`; dispatch: `ctx_412d2178f464`. Baseline: `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`.

**Development-code correction verdict: PASS. Confidence: HIGH for this bounded review.** C1 is resolved and G3 is aligned for future generated galleries. No new actionable correction finding was identified from code, security, goal or CLI QA perspectives. This clears the previous C1 objection to preserving the source as an explicitly unreleased development preview.

**Whole-goal/public-release verdict: FAIL; still blocked.** Required successful restricted-color and white-transparent native deliveries remain absent. This correction approval does not approve a public v0.4.0 release or replace the coordinator's final integration checks.

## Findings and disposition

| Finding | Disposition | Independent evidence |
| --- | --- | --- |
| C1: optional analysis blocks accepted legacy PNG delivery | **Resolved / PASS** | Newly created real fd1 schema-1 session fails under the exact prior review source and exports unchanged original bytes under the correction. Advisory EXIF failure is also reproduced and corrected. |
| G3: generated Dark surface differs from default measured surface | **Resolved / PASS for new output** | Actual current `color-gallery` output contains `#171717`; all seven existing public comparison HTML files still match their historical copies byte for byte. |
| G1/G2: missing essential native successes | **Open / release blockers** | Existing restricted and white native evidence remains indeterminate or unsuccessful; no new generation or acceptance evidence was created in this review. |

The earlier security review's S1 diagnostic-value exposure remains a pre-existing, low-severity observation outside this correction. No change to its code or severity is claimed here.

## Scope and source identity

Read [C1](review-code.md), [G3 and the native gates](review-goal.md), [the implementation correction report](metadata-export-fix.md), the current integration summary, relevant plan requirements and the complete corrected modules/test. Inspected the surrounding decoder, image validation, sampling/profile handling, reports, import handling, delivery/guide and storage boundaries, plus the focused regression cases.

Compared every one of the **37 production Python files** with the prior review's `source-sha256.txt`. Only `color_delivery.py` and `color_analysis.py` differ. The retained scripts-only portability workspace matches all 37 prior hashes and supplies the exact prior CLI for the red reproduction. The previous template reconstructed by restoring its single Dark literal matches the recorded prior SHA-256 exactly. Existing tests match the prior review hashes; `test_color_export_compatibility.py` is the sole additional test module, with 16 cases. The complete source/template correction diff is retained at `output/review-corrections/correction.diff`.

Final checks confirmed all **60 current source/test/template files** match this review's starting hashes and all **100 files under `docs/colors/`** remain unchanged during this review. Production, tests, other reviewers' reports and public evidence were read-only. This worker owns only this report and `output/review-corrections/`.

## Real baseline and current CLI reproduction

The reviewer independently extracted fd1 scripts with `git archive`, then used that actual CLI to init, import, review, select and export a new session under `output/review-corrections/workspaces/fd1-exif0`. The stored file is genuinely schema 1, produced by fd1 rather than manually downgraded current JSON. Fresh disposable copies were used for prior-source and corrected-source resume at revision 4.

The existing NORTHLINE PNG receives only an ancillary EXIF orientation-0 chunk. Decoded pixels are asserted identical to the original; the fixture also matches the original C1 reproduction hash:

```text
fe3433fe90168197446e4df3cd1f472a555759db5aa7cff8fe2703f6d729f87e
```

| Scenario | CLI result | Observed result |
| --- | --- | --- |
| Actual fd1 schema-1 lifecycle with EXIF 0 | Export exit 0 | Original PNG delivered. |
| Prior review CLI resumes copied fd1 session | Exit 1, `invalid_reference` | Original C1 reproduced; no new output or state change. |
| Corrected CLI resumes independent copy | Exit 0 | `color_policy=unverified`, `status=unverified`, `profile_treatment=unsupported`, zero samples; exact source and ZIP bytes retained. |
| Prior review CLI with EXIF 1 control | Exit 0 | Same decoded pixels; ordinary unverified report with assumed sRGB. |
| Prior review CLI with equivalent advisory EXIF 0 | Exit 1, `invalid_reference` | Analogous optional-analysis failure independently reproduced. |
| Corrected CLI with palette-free/advisory EXIF 0 | Exit 0 | Respectively unverified/unverified and advisory/indeterminate; no invented measurements. |

The corrected legacy export preserves the schema-1 bytes exactly in `session.v1.backup.json`, appends one fresh report, and preserves the existing report prefix. Every successful package's PNG matches the input; every ZIP contains exactly `logo.png`, `manifest.json` and `brand-guide.md`, each identical to its standalone counterpart. Report reasons appear in both manifest warnings and the guide. The legacy manifest explicitly states:

```text
Color evidence unavailable: invalid_reference: EXIF orientation must be an integer from 1 to 8
```

Executable probes: `output/review-corrections/probe.py` and `boundary-probe.py`. Logs: `cli-probe.txt`, `boundary-probe.txt`; full command/stdout/stderr/exit receipts: `receipts/`. The completed main matrix uses **72 real CLI invocations**, and the final additional boundary matrix uses **8**. There are 85 retained receipts because an initial five-call boundary attempt is also preserved: its truncated fixture was rejected earlier by report/hash binding than the harness expected. The corrected disposable probe updates that binding to reach and confirm `invalid_png`; no product or test expectation was weakened. This harness correction is documented in `debug-journal.md`.

## Exception scope, integrity and report semantics

The fallback at `skills/logo-land/scripts/logo_helper/color_delivery.py:81` catches only `ProjectError` with code `invalid_reference` and **no explicit cause**. Other domain errors and wrapped errors propagate. This distinction matters because `decode_reference`'s context manager also encloses the yielded sampling code: a sampling `ValueError` can become an `invalid_reference` with a cause. The focused test confirms that exact cause survives and no delivery/state change hides the programming error.

Before creating fallback evidence, `inspect_png` rechecks a complete, static, nonempty PNG and compares every image fact against the artifact. The existing store and export SHA checks precede this branch; the normal analyzer also verifies SHA before decoding. The original size, pixel, PNG completion, visual-review, destination and transaction gates are unchanged. Independent real CLI probes confirmed:

- Altered original bytes: `hash_mismatch`.
- Forged image dimensions: `invalid_state`.
- Truncated PNG, with disposable artifact/report hashes made consistent: `invalid_png`.
- Missing visual review: `review_required`.
- Opaque original requested as transparent, despite EXIF fallback eligibility: `background_mismatch`.
- Explicit `reference-add` and `color-analyze` on EXIF 0: still `invalid_reference`.

Each refused operation preserved session bytes and created no requested output. Focused tests also cover direct integrity/ValueError propagation, fresh strict recomputation against forged metrics, and failed publication/state-save rollback.

The fallback's empty measurements are truthful: zero sampled/visible/core/partial positions and sampled fraction; no measured/minor swatches, target distances, match fractions, observed color count or contrast values; `color_engine_version=not_used`. Artifact hash and any palette ID/digest remain bound. `unsupported` describes unavailable interpretation here; the explicit EXIF reason prevents implying a successful ICC interpretation.

Malformed ICC and non-sRGB gamma were exercised independently with metadata-only NORTHLINE fixtures under palette-free, advisory and strict policies. Palette-free/advisory exports remain available with unverified/indeterminate status and an explicit unsupported-profile reason. Their 16,384 sampled positions and alpha counts remain useful opacity evidence; RGB color measurements are absent. The one-line `color_analysis.py:173` correction preserves the previously dropped reason for palette-free reports.

Strict EXIF, ICC and gamma cases all refuse with `color_review_required`, both with their original unavailable reports and after a stored pass is forged. The prior implementation also refuses the forged EXIF strict case, though it exposed `invalid_reference`; changing that error to `color_review_required` improves the explanation without changing the refusal. Existing strict mismatch tests still return `color_mismatch`. No threshold or policy was relaxed.

## Gallery alignment and historical preservation

Ran the current CLI's `color-gallery --session demo --artifacts v1 --output new-gallery` in the corrected copied legacy workspace. It exited 0, preserved session bytes and copied the original PNG exactly. Its generated HTML contains:

```css
#surface-dark:checked ~ .artifact-grid .surface { background: #171717; }
```

This equals `analyze_png`'s unchanged default dark measurement surface. All seven `docs/colors/projects/*/index.html` files match `output/final-galleries/t8-portable-copy/projects/*/index.html` exactly and retain their historical `#252a32` preview. Individual paths and hashes are recorded in `output/review-corrections/gallery-verification.json`.

The broader old portable copy differs in five editorial/summary files from before this review; those are not silently treated as correction edits. All 100 current public files match the hashes captured at this dispatch's start. Browser rendering was intentionally not exercised, as instructed; G3 evidence concerns the emitted CSS and preserved bytes, not a new browser visual approval.

## Focused checks and limits

Existing environment: Python 3.12.12, Pillow 12.3.0, Pydantic 2.13.5, ColorAide 8.12.1, pytest 9.1.1. No dependency installation or synchronization was performed.

```sh
PYTHONDONTWRITEBYTECODE=1 uv run --locked --no-sync pytest -p no:cacheprovider \
  --basetemp output/review-corrections/pytest \
  tests/test_color_export_compatibility.py tests/test_color_reports.py \
  tests/test_color_gallery.py tests/test_background_compatibility.py -q
```

**67 passed in 51.76s.** Independently ran Ruff and basedpyright on both corrected modules and the new compatibility test: `All checks passed!`; `0 errors, 0 warnings, 0 notes`. `git diff --check` passed. Logs and final hash/count verification are in `output/review-corrections/verification-summary.json` and adjacent files. The coordinator owns the final full suite; this review makes no independent full-suite claim.

No browser/native generation, installation, pixel repair, commit, push, policy change, recursive team, debugger instrumentation or persistent process was introduced. Disposable workspaces are retained under the assigned output directory as replayable review evidence, not public/native success artifacts.

The open native gates are unchanged: restricted 밤결 has 615/2,697 partial-alpha visible samples, FIELD NOTE 371/3,019, and white `white-v3` 923/3,483; their recorded evidence remains indeterminate and no required approved package exists. These values come from the existing native evidence and prior independent reviews, not new native QA in this correction review. The existing two-repair limit remains binding. Development correction PASS therefore leaves whole-goal completion and public release blocked.
