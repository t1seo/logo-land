# Per-artifact background variants

Completed on 2026-09-12 using Python 3.12.12 and the existing uv environment.
The reproduction, implementation, focused tests, full checks, and direct CLI QA are complete.

## Contract

- `import --background opaque|transparent` optionally declares the requested background
  for that artifact, including a child imported with `--parent`.
- Omitting the option stores the **original brief's** background. It does not inherit
  a parent's override or infer intent from the PNG or prompt text. When retaining a
  parent's nonoriginal background on later edits, pass `--background` explicitly.
- New artifacts persist `requested_background`. Existing schema-version-1 sessions
  with that field missing or `null` still load; their effective background falls back
  to `brief.background`. Read-only resume and prompt commands do not rewrite state.
- Export resolves the selected artifact's effective request and compares it with
  decoded PNG transparency. An all-passing visual review cannot bypass a mismatch.
  Mismatch errors leave the revision and destination untouched.
- The manifest keeps the original `brief`, the immutable `source` artifact, and an
  explicit top-level `requested_background` for the effective export requirement.
  Legacy `source.requested_background` remains `null`; no new historical request is
  fabricated. `transparency_verified` continues to describe actual decoded alpha.
- The guide labels initial background as historical intent and separately names the
  selected artifact's requested background, alongside measured pixel facts.
- Edit prompts label original background as historical, identify the parent's
  effective request, and make the latest requested changes authoritative. Their JSON
  includes `parent_requested_background` (`null` for generation without a parent).
- Original PNG bytes, parent IDs, review gates, selection, and transaction checks
  retain their existing behavior. No migration or dependency change is required.

For an opaque starting brief and a transparent child, the import portion is:

```sh
uv run --no-sync python skills/logo-generator/scripts/logo_project.py \
  --workspace /path/to/workspace import \
  --session demo --artifact transparent-v2 --parent opaque-v1 \
  --background transparent --image /path/to/returned.png \
  --prompt-file /path/to/actual-prompt.txt --revision 1
```

## Root cause and failing-first evidence

Three hypotheses were checked: (1) export incorrectly uses the original brief,
(2) import/state lack a per-artifact intent field, and (3) alpha decoding or selection
targets the wrong artifact. The first two were confirmed; the third was refuted by
the selected child ID, parent lineage, decoded alpha, and byte-preserving export.

The same two parametrized CLI scenarios covered opaque → transparent and
transparent → opaque throughout the staged change:

1. Before implementing the option: `2 failed in 1.08s`, both at import with
   `No such option: --background` (exit 2).
2. After import/state support but before fixing export: `2 failed in 2.35s`, both
   reached export and failed with the incorrect original-brief requirement (exit 1):

   ```text
   background_mismatch: Requested opaque background differs from decoded transparency (True)
   background_mismatch: Requested transparent background differs from decoded transparency (False)
   ```

3. After using selected-artifact intent and updating delivery records:
   `2 passed in 2.10s`.
4. The prompt-context regression separately failed twice because
   `PromptResult` had no `parent_requested_background`; it passed after the prompt change.

## Automated verification

| Check | Result |
| --- | --- |
| `uv run --no-sync pytest tests/test_background_variants.py tests/test_background_compatibility.py -q` | 17 passed in 13.02s |
| `uv run --no-sync pytest -q` | 84 passed in 38.15s; prior 67 plus 17 new cases |
| `uv run --no-sync ruff check .` | All checks passed |
| `uv run --no-sync ruff format --check .` | 37 files already formatted |
| `uv run --no-sync basedpyright` | 0 errors, 0 warnings, 0 notes |
| `uv lock --check --offline` | Exit 0; resolved 22 packages |
| Programming skill's `check-no-excuse-rules.py` on scripts and tests | No violations in 18 files |
| `git diff --check` | Exit 0 |

The new cases cover both successful direction changes, both mismatches, selecting
the original after a newer opposite-background child, latest prompt context,
missing/null legacy state for both backgrounds, original-brief defaults despite
parent overrides, invalid CLI values, and invalid persisted background types/values.
Successful deliveries verify original PNG bytes, lineage, manifest intent, guide
intent, ZIP contents, and subsequent resume. Existing transaction and safety tests
remain in the full suite.

## Direct CLI QA

The real CLI was driven in a PTY through init → import base → import child with
`--background` → select → review → export → prompt → show, in a newly allocated
`/tmp/logo-background-qa.w4QrTZ` workspace. It reused synthetic PNGs from the focused
tests; no image tool or image API was called. tmux was absent, so the existing PTY
was used without installing anything.

Observed manifest summaries:

```json
{"session_id":"opaque-to-transparent","initial_background":"opaque","requested_background":"transparent","selected":"child","parent":"base","transparency_verified":true}
{"session_id":"transparent-to-opaque","initial_background":"transparent","requested_background":"opaque","selected":"child","parent":"base","transparency_verified":false}
```

Both fresh resumes reported revision 5 with `selected_id: "child"` and preserved
the respective `["opaque", "transparent"]` / `["transparent", "opaque"] intent
sequences. Prompt JSON reported each child's effective requested background.
`cmp` confirmed byte-identical PNG delivery, and `unzip -t` reported all three ZIP
members OK for each package.

A further explicitly mismatched child in each temporary session failed at export
with exit 1 and the two `background_mismatch` messages above. `cmp` confirmed the
session JSON did not change, and neither requested mismatch output directory existed.

This verifies the local helper contract and real CLI surface, not generated logo
quality or actual host visual review. Synthetic all-true review fixtures are labeled
as test fixtures. External image generation was outside this dispatch.

## Scope and review

Modified only five script files (`models.py`, `workflow.py`, `delivery.py`,
`prompts.py`, `logo_project.py`), two new test files (`test_background_variants.py`,
`test_background_compatibility.py`), and this report. The Typer import callback has
one narrowly documented argument-count lint exception for its CLI options; it has
no type-check suppression. No accounts, installs, commits, or subagents were used.

The review-work dimensions were checked locally under the explicit no-subagents
constraint: task coverage, actual CLI behavior, typed boundary/legacy handling,
transaction/path safety, and surrounding tests/callers. No blocking findings remain.
The implementation files were already untracked in this shared worktree, so Git
does not provide an implementation diff against HEAD or prior file history.

All four files under `.logo-generator/sessions/morrow-live/` retained their initial
SHA-256 hashes. The session JSON hash remained
`43a38d8e69378d40ed2ef4a9b471cda137dbd34821f1d2667f9c1e65523e901d`.
Of the 29 initially snapshotted session/live-QA files, 28 were unchanged and only
`docs/qa/live/README.md` changed concurrently; this worker never wrote that file
and did not revert it. No root QA session or image was edited.

The temporary manual-QA workspace is removed after its results are recorded here.
No source instrumentation, root debug journal, or persistent QA session is left by
this change. Pytest's normal temporary fixture retention remains unchanged.
