# Metadata export compatibility fix

Task: `task_4d71958a5150`; dispatch: `ctx_b905034407de`.

## Scope and work plan

1. Complete: reproduce accepted PNG metadata failures with focused red tests.
2. Complete: preserve non-strict export using truthful unavailable color evidence and retain strict/integrity gates.
3. Complete: run focused CLI regressions, Ruff, basedpyright, and record exact evidence.

## Investigation journal

- Runtime: existing locked uv Python environment; local synchronous Typer CLI; no network, image generation, or personal installation required.
- Baseline: shared dirty worktree based on `fd1d89c`; all other agents' changes remain outside this task.
- H1: unconditional export analysis introduces reference EXIF validation beyond the old PNG contract. Distinguish by orientation 0 versus 1 with identical decoded pixels; expected fix: unavailable evidence.
- H2: schema migration or palette inference causes the failure. Distinguish schema 1 from palette-free schema 2 using the same metadata; expected fix if true: migration binding.
- H3: damaged bytes or ICC conversion prevents base PNG integrity checks from succeeding. Distinguish raw PNG inspection from color analysis and preserve byte/hash checks; expected fix if true: reject source.
- Existing reviewer reproduction: baseline orientation 0 exports with exit 0; current orientation 0 imports with exit 0 then exports with exit 1 and `invalid_reference: EXIF orientation must be an integer from 1 to 8`; current orientation 1 exports with exit 0.

Planned artifacts: this permanent report, the owned focused test module, and the owned export-policy implementation. Pytest fixtures use managed temporary directories; any extra QA workspace will be temporary and removed. No debugging instrumentation, global environment changes, watchers, or servers are needed.

## Red evidence

`uv run --locked pytest tests/test_color_export_compatibility.py -q` exited 1: **6 failed, 7 passed in 11.06s**.

- All three non-strict EXIF cases failed at real CLI export: `invalid_reference: EXIF orientation must be an integer from 1 to 8`.
- Schema-1 and schema-2 palette-free ICC cases exported, but their report reasons omitted the known ICC limitation.
- Strict EXIF with a forged stored pass remained blocked, but exposed `invalid_reference` instead of a color-review-required result.
- Strict ICC, original hash tampering, and direct integrity/programming error propagation already passed.

H1 confirmed; H2 refuted by the same failure in both schemas; H3 refuted for these metadata fixtures by successful full `inspect_png`, identical decoded pixels, and byte-preserving import. Minimal supporting change: preserve `samples.reasons` in palette-free analysis reports. The export fallback accepts only explicitly raised `ProjectError(code="invalid_reference")` without a wrapped exception, rechecks the complete PNG and stored image facts, and emits no color measurements. Wrapped decoder or programming exceptions remain errors rather than being relabeled unavailable.

## Resulting contract

- Palette-free and schema-1 exports retain `color_policy=unverified` and `status=unverified`; advisory intent remains bound and reports `status=indeterminate` when EXIF/ICC prevents verification.
- EXIF rejection creates a fresh report with `profile_treatment=unsupported`, zero samples and no measured swatches, target distances, match fractions, observed color count or contrast values. Its explicit error reason appears in the manifest and guide; no original pixels or metadata are rewritten.
- Malformed ICC already follows the profile analyzer's unsupported path. The supporting one-line change retains that reason for palette-free reports instead of dropping it. Existing sampled alpha counts are retained; unverified RGB measurements remain absent.
- Strict requirements still require prior determinate evidence and fresh verification. A forged stored pass cannot convert unavailable EXIF/ICC evidence into a pass; export fails with `color_review_required` without changing state or publishing a directory.
- Existing source hash, PNG completeness, stored image-fact validation and export transaction gates remain intact. Direct integrity/ValueError failures propagate; a ValueError wrapped by the reference decoder also remains a failure with its original cause.
- No threshold, report schema, dependency, source-integrity parser or public gallery change was needed. The coordinator accepted the one-line supporting analysis change in message `msg_a33af29be604`.

## Green and quality evidence

The initial 13-case regression suite changed from **6 failed, 7 passed in 11.06s** to **13 passed in 10.73s** after the implementation. The final suite adds truncated-source, mismatched-facts, and wrapped-programming-error checks; a first expanded run exposed a test expectation issue (stored-fact validation correctly returns `invalid_state` before color analysis), which was corrected without changing product behavior. The final focused run exited 0: **94 passed in 50.85s**, including all 16 new compatibility cases and 78 existing color/export/migration/transaction cases.

```sh
uv run --locked pytest tests/test_color_export_compatibility.py tests/test_color_reports.py tests/test_palette_compatibility.py tests/test_color_analysis.py tests/test_delivery_guide.py tests/test_transactions.py tests/test_reserved_output.py -q
uv run --locked ruff check skills/logo-land/scripts/logo_helper/color_delivery.py skills/logo-land/scripts/logo_helper/color_analysis.py tests/test_color_export_compatibility.py
uv run --locked ruff format --check skills/logo-land/scripts/logo_helper/color_delivery.py skills/logo-land/scripts/logo_helper/color_analysis.py tests/test_color_export_compatibility.py
uv run --locked basedpyright skills/logo-land/scripts/logo_helper/color_delivery.py skills/logo-land/scripts/logo_helper/color_analysis.py tests/test_color_export_compatibility.py
```

Ruff: `All checks passed!`; format: `3 files already formatted`; basedpyright: `0 errors, 0 warnings, 0 notes`. The programming skill's `check-no-excuse-rules.py` also reports `no violations in 3 file(s)`. Physical module lengths are 152, 205 and 215 lines respectively, so each is below 250 even before excluding comments and whitespace. `git diff --check` passed.

## Actual v0.3.1 session QA

Copied `output/review-code/metadata-probe/base-orientation-0` into a managed temporary directory and ran the current helper against that genuine baseline-generated schema-1 session, already at revision 4 after its historical export:

```sh
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace "$COPIED_WORKSPACE" export --session demo --revision 4 --output fixed-delivery
```

Observed:

```text
export_exit: 0 stderr: ''
original_and_zip_sha256: fe3433fe90168197446e4df3cd1f472a555759db5aa7cff8fe2703f6d729f87e
color_policy: unverified
status: unverified
profile: unsupported
samples: 0
reason: Color evidence unavailable: invalid_reference: EXIF orientation must be an integer from 1 to 8
schema1_backup_identical: true; all_zip_members_identical: true
temporary_workspace_removed: True
```

All ZIP members matched their standalone files, the delivered PNG matched the accepted original, and the migration backup matched the schema-1 bytes from before this export. The reviewer's original workspace was not changed. The command ran through the actual CLI using the existing repository environment; no personal installation or image generation was performed.

## Boundaries and cleanup

This resolves the bounded metadata compatibility regression; the coordinator owns independent correction review and final installation checks. Full release/native success gates documented in `review-context.md` remain separate and unresolved by this fix. No commits, pushes, installs, global configuration changes, debug instrumentation, or background processes were created; managed QA workspace cleanup succeeded. Only the two implementation files, the new focused test file and this report belong to this fix.
