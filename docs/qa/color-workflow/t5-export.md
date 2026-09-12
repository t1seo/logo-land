# T5: selected-artifact color exports

Implemented and verified on 2026-09-13 KST. This evidence covers synthetic fixtures and actual local CLI execution; it does not claim native-image generation, lettering quality, or release verification.

## Delivered behavior

- Export resolves the selected artifact's immutable palette and lockup, independently of the active palette or newer children.
- Manifest version 2 adds `intended_palette`, the freshly computed `color_report`, `color_policy`, `warnings`, `color_method`, `color_limits`, `lockup_intent`, and `font_reference_usage: "appearance-reference-only"`.
- Original PNG bytes remain unchanged. The ZIP still contains exactly `logo.png`, `manifest.json`, and `brand-guide.md`, matching the adjacent files byte for byte.
- Successful export appends its fresh report and export record together under the existing session lock and revision check. Failed publication or state commit removes new files and new empty parent directories, preserving prior state and packages.
- The guide records intended and measured swatches, coverage, matching-sample delta-E, sampling/ROI/profile details, methods and limitations, explicit-surface contrast guidance, and requested typography without claiming an actual font identity or license.

### Strict and advisory decisions

Contract 10 was explicitly confirmed with the coordinator: missing, unverified, or indeterminate stored strict evidence requires `color-analyze` before export and returns `color_review_required`. A matching stored pass or mismatch is recomputed from verified original bytes; fresh mismatch returns `color_mismatch`, and fresh uncertainty returns `color_review_required`. Visual review booleans, stored metrics, and edited thresholds do not bypass this gate.

The latest matching report supplies its explicit ROI and contrast surfaces; measurements and fixed policy thresholds are recomputed. The guide and warnings disclose that ROI evidence covers only that region. Full-image analysis remains the default when no prior scope exists.

Palette-less legacy artifacts remain color-unverified. Unconstrained palettes are advisory and can export mismatch or limited evidence with explicit warnings. Untagged PNGs are honestly labeled `assumed_srgb`, as required by the locked measurement policy; unsupported profiles/gamma or insufficient core evidence are indeterminate.

## Verification

The initial new export tests failed seven expected feature assertions before implementation. Additional nested-directory rollback tests failed twice before the transaction fix. Final integrated regression command:

```sh
uv run --locked pytest tests/test_color_reports.py tests/test_delivery_guide.py tests/test_transactions.py tests/test_reserved_output.py tests/test_background_variants.py tests/test_background_compatibility.py tests/test_cli_workflow.py tests/test_resume_and_portability.py -q
```

Result: **74 passed in 74.65 seconds**. [Raw result](t5-export-tests.txt).

The focused color/delivery suite has 20 passing cases, including missing/unverified/indeterminate stored evidence, fresh uncertainty behind a forged pass, forged coverage/targets/thresholds, a third visible color, old mismatch recomputation, selected old parent versus active/new child, ROI/surface preservation, legacy/advisory warnings, ZIP identity, and publication/save rollback. Broader regressions cover existing background semantics, reserved paths, workflow, concurrency, resume, and copied-script portability.

All six owned Python files pass Ruff, Ruff formatting, strict basedpyright, and the programming skill's no-excuse audit. Their nonblank/noncomment line counts are 155 (`delivery.py`), 95 (`color_delivery.py`), 117 (`color_guide.py`), 53 (`export_bundle.py`), 245 (`test_color_reports.py`), and 120 (`test_delivery_guide.py`). See [quality results](t5-export-quality.txt).

## Actual CLI fixture run

[Full transcript](t5-export-evidence/cli-transcript.txt), [representative manifest](t5-export-evidence/manifest.json), [representative guide](t5-export-evidence/brand-guide.md), and [actual third-color report](t5-export-evidence/third-color-report.json).

1. Created a transparent synthetic green/white PNG and imported it with a strict maximum of two colors and a horizontal font appearance reference.
2. Added a navy child and made navy active, then selected/reviewed/exported the green parent. The output retained green intent, horizontal lockup, and a fresh passing report with 1,600 sampled positions and 1,599 core samples.
3. Verified SHA256 `2b108381a45f159737f997e08a3cbe976edce197e588ffed9f383bfdb7ee060c` and all three ZIP payloads against the original/adjacent bytes.
4. Imported a third-color fixture with 80 red samples among 1,599 core samples (about 5.0031%). Forged its report status, coverage, and threshold; real CLI export still returned `color_mismatch` and preserved state/output absence.
5. A forged report palette binding returned `invalid_state`; modified managed PNG bytes returned `hash_mismatch` before export. The fixture modifications were then restored.
6. Removed the green artifact's stored reports: export returned `color_review_required` without state changes. Explicit `color-analyze` followed by export succeeded.
7. Confirmed source and imported PNG hashes and preserved the prior package. Removed the entire temporary fixture workspace and generated PNG/ZIP files; retained only the text/JSON evidence linked above.

## Scope and integration

Owned implementation: `delivery.py`, `color_delivery.py`, `color_guide.py`, `export_bundle.py`, `tests/test_color_reports.py`, and `tests/test_delivery_guide.py`. Tests use the integrated T1 immutable state, T3 analysis, and T4 palette/import/analyze APIs. No commits, pushes, release changes, native-image calls, subagents, or edits to other workers' modules were made. Native-image quality and release review remain coordinator-owned work.
