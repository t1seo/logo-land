# Offline gallery delivery follow-up

**Result: implemented; 43 pytest tests and 10 Node tests pass, with zero browser skips.** Actual installed Chrome downloaded byte-identical ZIPs and guides from the published file URL. This report extends, and preserves, the previous [gallery evidence](gallery.md).

## Scope and execution ledger

- Dispatch `task_7b1360964b5d` / `ctx_266c0bc431e3`: gallery modules, assets, tests and this evidence only; no model/image calls, new agents, commits or shared configuration changes.
- PIN passed: awaiting-choice publication has no ZIP action and retains every exact original.
- RED → GREEN passed: delivered core `Workflow`/`Delivery`, verified real ZIP/manifest/original/guide, stale and malformed delivery, portable publication and unchanged canonical state.
- Coordinator message `msg_b742dd8f57b1`: capture the read-only actual OFFCUT snapshot before the change, then compact long strategy text with complete keyboard-accessible disclosure. Preserve source values and originals; do not expose native cache receipts.
- Final gates passed: targeted pytest and Node tests, normal Ruff and formatting, basedpyright targeting Python 3.11 (0 errors/warnings/notes), actual installed Chrome via file URLs, desktop/mobile screenshots and exact downloaded ZIP/contained PNG hashes. Cleanup is recorded below.

## Implementation

`publish_gallery(workspace, state, output)` still exclusively creates a fresh folder and returns its `index.html`; it never mutates the canonical workflow. `gallery_delivery.py` consumes core `Delivery`, `HelperManifest`, `HelperBrief`, and core image-review checks. It verifies the delivered phase, selected candidate, exact original/prompt/parent/dimensions/brief/background provenance, both passing bound critiques, saved ZIP/manifest hashes, and the selected PNG hash.

All source paths are workspace-contained and symlink-free through core `safe_path`. PNG/ZIP reads are capped at 64 MiB; manifest/guide are capped at 1 MiB. The ZIP must contain exactly one each of `logo.png`, `manifest.json` and `brand-guide.md`, with matching bounded bytes. Unexpected, duplicate, encrypted, unsupported compression, directory and special-file members are rejected. ZIP inspection uses in-memory bytes and bounded member reads; it never extracts paths.

Only verified bytes become `delivery/logo.png`, `delivery/logo-package.zip`, `delivery/manifest.json` and `delivery/brand-guide.md`. Existing publication rollback also owns these copies; interrupted writes retain foreign files. Missing, changed, foreign, unreviewed or unbound delivery raises typed `gallery_delivery` before a new publication exists. Awaiting-choice pages have no package panel or invented ZIP. Existing immutable publications retain their own verified copies after source removal or a folder move.

The ivory/ink package panel contains the actual ZIP and guide actions, a visible workflow/revision/candidate binding, and optional file/hash details. ZIP and guide downloads use byte-identical data URLs so Chrome's file-URL download behavior works without fetch or JavaScript. Direct relative links remain available for the selected original, guide, manifest and package. This duplicates the verified ZIP/guide payload inside HTML intentionally; no repackaging or image transformation occurs.

`gallery_strategy.py` presents short escaped excerpts with an ellipsis when truncated. The closed native `details` element retains all complete strategy fields and assumptions; no source text or workflow field is shortened or rewritten. The existing feedback draft remains bound to its original snapshot and never changes selection or delivery.

## Resource registration (before creation)

- Owned temporary root pattern `/tmp/logopia-gallery-delivery-ctx_266c0bc431e3.XXXXXX`, allocated once with `mktemp`; task-local Playwright 1.63.0 installation and npm files remain only inside it.
- Owned children: `fixture-*`, `chrome-*`, `downloads-*`, `pytest-*` and `baseline-native` for generated fixture/publication data, isolated browser profiles, downloaded bytes and the read-only OFFCUT baseline publication. Remove these after QA; never remove the source OFFCUT workspace.
- Installed Chrome executable `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, launched only through isolated persistent contexts with profiles below this root. No user profile, existing tabs, server, tmux session or fixed port is used; close only owned contexts in `finally`.
- Retained evidence: this report, source tests, `gallery/delivery-*.png`, `gallery/delivery-*.json`, `gallery/native-strategy-*.png` and a separate `gallery/delivery-regression/` for rerunning prior browser checks without overwriting their evidence.

## First failures

- Initial delivery/strategy test run: **1 PIN passed, 3 RED failures** — missing `#download-package`, missing copied package, and no full-strategy disclosure. Production changes followed these failures.
- Initial adversarial run: **23 RED failures**, because delivery was ignored even when files, saved identity or review evidence were invalid. The corrected publisher rejects these states before writing an index.
- Actual native Chrome baseline: **1 RED failure** at `Candidates begin at 1541.5234375px`; strategy height was **1081.84375px**. [First failure receipt](gallery/delivery-native-first-failure.json) and [before screenshot](gallery/native-strategy-before.png) are retained. Hypotheses: long strategy fields (confirmed by the measured strategy height), unusually tall header (refuted by unchanged header dimensions), or unloaded originals (refuted by all images completing with nonzero dimensions). The fix changes only strategy presentation.
- Final defensive review added a failing regression for a ZIP whose exact PNG bytes were marked as symlink members; it initially failed with `DID NOT RAISE StudioError`. The member-type check now rejects it. While placing that test, misplaced existing rollback assertions were immediately restored to their original test before final QA.
- The delivered-download browser test passed on its first run; no flaky browser rerun or harness workaround was needed. Prior gallery file-URL failure evidence was preserved separately. Static-check feedback was resolved through explicit typing, normal formatting and native per-file Ruff settings, without ignore annotations.

## Verification and cleanup

Environment: Python 3.12.12 repository runtime, Node 26.8.1, Playwright 1.63.0 installed only in the owned temporary directory, installed **Google Chrome 152.0.7977.83**. Python 3.11 syntax was additionally parsed and basedpyright ran with its 3.11 target. Every owned Python module is below 250 logical lines (largest: 159); no `Any`, `object`, `cast` or type-ignore annotations were introduced.

```sh
uv run --locked pytest -q tests/hermes/test_gallery*.py --basetemp=<owned-root>/pytest-final
LOGOPIA_GALLERY_QA_ROOT=<owned-root> \
LOGOPIA_GALLERY_QA_EVIDENCE=<repo>/docs/qa/hermes-workflow/gallery/delivery-regression \
node --test --test-concurrency=1 tests/hermes/gallery*.mjs
uv run --locked ruff check integrations/hermes/logopia_studio/gallery*.py tests/hermes/test_gallery*.py
uv run --locked ruff format --check integrations/hermes/logopia_studio/gallery*.py tests/hermes/test_gallery*.py
uv run --locked basedpyright --pythonversion 3.11 integrations/hermes/logopia_studio/gallery*.py tests/hermes/test_gallery*.py
```

Final results: **43 pytest passed; 10 Node passed, 0 failed, 0 skipped; Ruff/format clean; basedpyright 0 errors, 0 warnings, 0 notes**. Original comparison baseline pins still pass. The previous browser suite writes this run's screenshots/receipt into `gallery/delivery-regression/`, preserving every earlier gallery artifact.

| Scenario | Measured result |
| --- | --- |
| Actual file-URL package action | PASS: `page.goto(fileURL)` → `waitForEvent('download')` → `page.click('#download-package')` → completed `saveAs` |
| Downloaded ZIP | PASS: **6,387 bytes**, SHA-256 `0260e56c062840819fb1c2736457692f66096dce764d1bc613d25e69e1a860e1`, exactly equal to saved `state.delivery.zip_sha256` and source bytes |
| Selected PNG inside downloaded ZIP | PASS: candidate-2 SHA-256 `cf9efc33175d74fd801fb2ef32e265f31a91b1724154eb7d7f43b99834fb27fe`, exact candidate digest |
| Guide download and manifest opening | PASS: actual guide bytes equal source; opened manifest response hash equals saved manifest hash |
| Repeated download/reload/back | PASS: three completed ZIP downloads with reloads, then manifest navigation/back and keyboard ZIP download |
| No JavaScript | PASS: actual completed ZIP download with the same saved hash |
| Snapshot and canonical immutability | PASS: canonical workflow and source ZIP bytes unchanged; newer/unreviewed snapshots have no package; going back retains explicit old r7 identity and its feedback draft |
| Malformed/missing/changed ZIP, manifest, guide and original | PASS: typed failure before publication |
| Foreign/stale manifest or selection, absent/invalid review | PASS: no publication or inferred approval |
| Unexpected/duplicate/special ZIP entries; escaping or symlink paths; oversized guide | PASS: rejected; no extraction or outside file created |
| Dirty output / write interruption | PASS: foreign sentinel retained; retry into the dirty folder rejected |
| Inert HTML-looking text | PASS: no injected guide DOM; full strategy text is escaped and preserved |
| 390px delivered page | PASS: document width **390px**, package action visible in [mobile screenshot](gallery/delivery-mobile.png) |
| Errors and requests | PASS: **0 page errors, 0 external page requests** |

[Delivered desktop](gallery/delivery-desktop.png) and [browser receipt](gallery/delivery-browser-receipt.json) show the actual tested publication. The synthetic delivery fixture is explicitly local QA data; its critiques are not live inference.

The read-only actual OFFCUT sample has three imported originals. Its strategy is identical across the baseline r16 and final r23 snapshots (strategy JSON SHA-256 `250834d7049592a5f2f1c171d810cefb88e24d239353c2a99879a4a4afbf0006`); the coordinator advanced workflow status independently between captures. Strategy height fell **1081.84 → 368.77px**, and the candidate section moved **1541.52 → 828.45px** on desktop. Mobile candidates begin at **1009.05px**, with zero horizontal overflow. Enter opens/closes the disclosure, every complete original strategy value is present, every copied original hash matches, and the canonical file remained byte-identical during final QA. Evidence: [after](gallery/native-strategy-after.png), [mobile](gallery/native-strategy-mobile.png), [actual originals](gallery/native-strategy-originals.png), [native receipt](gallery/delivery-native-receipt.json). Screenshots were opened and visually reviewed; private native cache receipts are not exposed.

Goal/contract, code quality, defensive handling, actual-browser usability and surrounding-consumer review were performed directly because the task prohibits new agents. Live inference, image generation/edit calls, provider cancellation and live-server shutdown are **N/A** for this offline task. No new package dependencies, global profile changes, commits, upstream Hermes edits or changes to other workers' files were made.

**Cleanup complete:** [owned-resource receipt](gallery/delivery-cleanup-receipt.json) records `contextsClosed: true`, `ownedChromeProcesses: 0` and `temporaryRootExists: false`. The exact allocated root `/tmp/logopia-gallery-delivery-ctx_266c0bc431e3.SchZkw` was removed, including the task-local Playwright/npm files, baseline publication and all five bounded pytest fixture directories. Test contexts closed in `finally` and removed their own profiles/downloads/fixtures; gallery-specific Python caches were removed separately. No QA server, fixed port or tmux session was started, and no global/user profile was touched. Only gallery source, tests, screenshots and reports/receipts remain. No gallery-owned work remains outstanding.

To repeat: register and allocate a new temporary root, install `playwright-core@1.63.0` there with `npm install --prefix <owned-root> --no-audit --no-fund --ignore-scripts`, then run the commands above and remove only that root after its contexts settle. The native sample test explicitly skips when the local OFFCUT sample is absent; the documented acceptance run had the sample and skipped zero tests. `LOGOPIA_GALLERY_NATIVE_BASELINE=1` was used only for the retained pre-change failure capture and is unset for normal QA.
