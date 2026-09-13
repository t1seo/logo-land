# Comparison browser restoration

Task `task_b270364645e6`, dispatch `ctx_f303d0f5e223`; branch `feat/logo-land-gallery-workflow`.

## Execution ledger

- Completed: PIN existing initialized controls; record RED against the actual template script.
- Completed: distinguish lifecycle cause from predicate/stale-publication hypotheses; add one `pageshow` listener.
- Completed: exact regression GREEN and lifecycle toggle; 58 targeted tests; production regeneration and all 18 file comparisons.
- Completed: bounded HTTP HTML and 16 original/prompt download/hash checks; owned server stopped and reaped.
- Completed: retained evidence and final source inventory; exclusively owned temporary cleanup.
- Completed: root relayed actual Chrome PASS from browser owner `ctx_a04104359e84`; no remaining work.

## Registered resources and ownership (before creation)

This report is the task-scoped debug journal; the shared root journal and git exclusions are not touched.

- `/tmp/ll-060-browser-fix/`: exclusive temporary root; record device/inode on creation, remove only this root after evidence retention.
- Contents registered under that root: baseline inventories and template copy, test PIN/RED/GREEN logs, helper receipts, a copied `.logo-generator/` snapshot, generated `gallery/`, HTTP responses/downloads, server script/PID/log, final inventories.
- `tests/comparison_browser_restoration.test.mjs`: retained production-script regression, created before any template change.
- `127.0.0.1:8794`: requested bounded server, but initially occupied by foreign PID 94939 (Computer Use node kernel); coordinator notified, no process touched.
- Coordinator correction `msg_c90c00332469`: use `127.0.0.1:8802` for this worker; leave Chrome-owner port 8794 intact. Register `/tmp/ll-060-browser-fix/server.mjs` and `server.pid` before creation; finite 300-second lifetime and explicit SIGTERM/close teardown.
- Real user Chrome belongs exclusively to browser dispatch `ctx_a04104359e84`; source worker opens no browser, DevTools, or GUI.
- No source session, approval, selection, image, prompt, README, metadata, installation or commit writes.

## Hypotheses recorded before the regression

1. Lifecycle timing: form values are restored after the initial `update()`, without a form `change` event. Distinguish by restoring valid selects after script evaluation, dispatching `pageshow`, and comparing select values/cards/count; a `change` event with identical values should repair the view. If true: synchronize lifecycle.
2. Filter predicate/data mismatch: Brand logo or intersecting style values do not match card datasets. Distinguish by explicit change and preinitialized-state runs using the same values/cards; a predicate bug fails these too. If true: correct predicate.
3. Stale publication: the public HTML script differs from the source template and omits working filtering logic. Distinguish by hashing/extracting both actual scripts before editing and exercising the template itself. If true: regenerate publication.

Reported Chrome PIN: Kind Brand logo initially shows 1 of 8; Original PNG then toolbar Back restores Brand logo while showing 8 of 8 and all cards (`chrome/05-first-back-filter-mismatch.jpg`, message `msg_6b7ca8d42c11`). This is browser-owner evidence, not this worker's GUI observation.

## PIN and recorded RED before production edit

Node `v26.8.1`, constrained DOM with finite options, VM execution of the actual single production script (1-second VM timeout, 20-second command timeout), no dependencies or browser processes.

- `node --test --test-name-pattern=PIN: tests/comparison_browser_restoration.test.mjs`: exit 0; **2 passed, 0 failed**, 55.293166 ms. Explicit change updates kind/style, count, empty state, context/surround; reset waits for native defaults; preinitialized restored controls work.
- `node --test tests/comparison_browser_restoration.test.mjs`: exit 1; **2 passed, 4 failed**, 52.113084 ms. Both persisted=false/true scenarios report actual `8 of 8 candidates`, expected `1 of 8 candidates`; intersection reports actual 8, expected 0; restored surround reports actual light, expected dark. Full first-failure output retained in the JSON evidence.
- Baseline temporary root identity: device 16777230, inode 35034033. Source inventory: 14 saved state/original files; skill source inventory: 66 regular files excluding generated `__pycache__`; public comparison: 18 files.
- Source template and public HTML scripts were byte-identical before the fix. This rejects stale publication. Passing preinitialized and explicit-change PINs reject the predicate/data mismatch hypothesis for identical controls/cards.
- Minimal production edit after RED: `window.addEventListener("pageshow", update);`, retaining the initial update and all existing handlers.

## Root cause and GREEN

The initial script runs correctly, but it only synchronizes on initial evaluation, form change and reset. A browser can restore form values later without a form change, so the select shows Brand logo while the gallery retains the previous all-cards result. The same omitted synchronization affects style, empty/count and preview datasets.

The preserved pre-fix script was executed in three fresh runtimes with the identical `kind=brand` restored value. Toggling only delivery of the existing form change handler yielded `(no change, 8 visible) → (change, 1 visible) → (no change, 8 visible)`. Counts were correspondingly `8 of 8`, `1 of 8`, `8 of 8`. No production code was reverted for this toggle.

- Exact GREEN: `node --test tests/comparison_browser_restoration.test.mjs`, exit 0, **6 passed / 0 failed**, 51.60475 ms.
- Syntax: `node --check tests/comparison_browser_restoration.test.mjs`, exit 0.
- Targeted checks: `uv run pytest -q tests/test_comparison_baseline.py tests/test_comparison_cli.py tests/test_comparison_filesystem.py tests/test_comparison_inputs.py tests/test_comparison_limits.py tests/test_comparison_markup.py tests/test_comparison_publication.py`, exit 0, **58 passed in 4.70s**.
- No Python code changed, so Ruff/basedpyright were not rerun. The new module is dependency-free JavaScript; actual VM execution and Node syntax checking passed. No unavailable language-server result is claimed.
- Coverage: normal changes, preinitialization restore, postinitialization restore with persisted=false and true, two restore/reset cycles, kind/style intersection including zero results, exact visible-card indexes/count/empty state, all four preview contexts and both surrounds, unchanged select values, deferred reset and status clearing.

## Production regeneration and preserved bytes

The existing `output/gallery-workflow-native/workspace/.logo-generator/` was copied byte-for-byte into the exclusively owned temporary workspace; no source state was rewritten. The actual production helper was then invoked with the saved public selection:

```sh
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-browser-fix compare-gallery --selection-file docs/gallery-workflow/inputs/selection-final.json --output gallery
```

Exit 0, result `{"path":"gallery","index_path":"gallery/index.html","count":8}`. Compared all 18 relative output files against the public baseline: **17 unchanged, only index.html changed**. Copied only this generated index into `docs/gallery-workflow/comparison/index.html`; every final public file equals the generated file. Generated manifest still agrees with all 8 original and all 8 exact prompt hashes. The copied and original saved workspace inventories remain equal to the 14-file baseline, including all 6 sessions and their revisions.

| Artifact | SHA-256 |
|---|---|
| Template | `2e9760669f0aa2d9d34267fce0241452f43de435c9c4985bce80be70afb309a3` |
| Generated/public/HTTP index | `66e8ac8fd728f85a683ee041437a2a0fbe56a2f4b89902fb9eefc4c1d29610c6` |
| Regression test | `dba7111715f09b11af3f68b33a03f079451db72fc8a98345fe67200e759d4a3e` |

The full 66-file skill source inventory was recalculated: only the template changed. Before/after inventory, all originals/prompts hashes, saved source revisions and exact test/CLI receipts are retained in `browser-restoration.json`. Generated Python `__pycache__` files are excluded from the source inventory; no source entry is excluded.

## Actual HTTP surface

Coordinator correction `msg_c90c00332469` reserved 8802 for this worker and retained 8794 for the browser owner. Port 8802 had no listener before startup. Owned server PID **8814**, tool exec session **16364**, bind **127.0.0.1:8802**, 300-second maximum lifetime, 20-second request timeout.

```sh
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8802/gallery/index.html
```

Observed `HTTP/1.1 200 OK`, `Content-Type: text/html; charset=utf-8`, `Content-Length: 42459`, `Date: Sun, 13 Sep 2026 00:55:23 GMT`. The nonempty response body exactly matched generated and public HTML. Actual curl downloads of each of `images/001.png` through `008.png` and `prompts/001.txt` through `008.txt` returned 200 and matched their manifest/public/source hashes. All **17 HTTP requests** succeeded; individual argv/hash receipts are in the JSON evidence.

SIGTERM sent only to owned PID 8814; exec session 16364 reaped with exit 0 and all 17 successful access-log entries. The browser owner's PID 94939 and port 8794 were not signalled or reused.

## Nine adversarial classes

| Class | Evidence and result |
|---|---|
| 1. Malformed/boundary | Existing strict selection, size, identity and finite cardinality regressions included in 58 passing cases; lifecycle fixture admits only actual finite control options. |
| 2. Injection/hostile text | Existing hostile brand/notes parser regression passes; one authored script, escaped text and inert URLs remain intact. Added listener accepts no external data, HTML or network input. |
| 3. Cancel/resume/repeated interruption | Two simulated history/reset cycles pass; existing repeated KeyboardInterrupt publication/retry checks pass; gallery/source bytes preserved. |
| 4. Stale state | Restored select/card indexes/count/empty/context/surround now agree in runtime tests; wrong/current revision and concurrent advance tests pass; actual 6 source-session bytes/revisions preserved. Actual Chrome closure is separately attributed below. |
| 5. Dirty/foreign ownership | New exclusive temp root; all 18 publication files compared; 14 source files and 16 original/prompt hashes preserved. Existing dirty-path/symlink/foreign replacement tests pass. Only owned public index copied; foreign browser port untouched. |
| 6. Hung/resource budget | VM timeout 1s; Node checks/helper 20s; targeted test parent timeout 60s; curl connect 3s/total 20s; server request 20s/lifetime 300s. All completed within bounds; owned server reaped. |
| 7. Flaky/repeat | First failure captured before production edit; same regression rerun only after fix. Original-script event-delivery toggle confirms 8→1→8; repeated lifecycle cycles and existing deterministic regeneration test pass. |
| 8. Misleading success | Runtime assertions inspect actual count, hidden cards, empty state and datasets. Real helper result checked against 18 hashes; HTTP nonempty HTML and every download verified. HTTP/unit results are not described as Chrome PASS. |
| 9. Real surface/native cost/cleanup | Actual CLI and HTTP run; browser owner exclusively owns actual Chrome validation. No image generation, paid API, native edit, installation or approval call is required for a JavaScript lifecycle synchronization; these are N/A. Owned temp/server cleanup receipt retained. |

## Actual Chrome closure

`FIX READY` sent as `msg_71eaf118849a`, frozen hashes sent as `msg_ef43a5f8da4e`, requesting root/browser-owner confirmation of the exact Brand logo → COMMON Original PNG → toolbar Back flow on the refreshed public index and restored preview/surround controls. This source worker did not drive Chrome and does not infer Chrome success from the constrained DOM or HTTP evidence.

Root's blocking-ask reply confirms **PASS**, citing browser-owner message `msg_f1148b50391f`. Actual GUI actions belong to `ctx_a04104359e84`: fresh Reload → Brand logo / Web header / Dark → COMMON Original PNG → Chrome toolbar Back retained **1 of 8**, only **COMMON**, **Web header**, and **Dark**. The index hash remained `66e8ac8fd728f85a683ee041437a2a0fbe56a2f4b89902fb9eefc4c1d29610c6`. Root directly inspected the top-state screenshot.

- [Fixed Back restoration](chrome/44-fixed-back-restoration.jpg)
- [Fixed Back restored controls and 1-of-8 count](chrome/45-fixed-back-restoration-top.jpg)
- [Fixed reload controls](chrome/46-fixed-reload-controls.jpg)

The originally reported real-browser scenario is closed with owner-attributed evidence. All source-worker gates and the delegated actual Chrome gate pass; no outstanding dependency remains.

## Cleanup receipt

Owned PID 8814 was terminated and reaped with exit 0; `lsof -nP -iTCP:8802 -sTCP:LISTEN` returned exit 1 and empty output, proving no remaining listener. Before temporary deletion, device/inode again matched `(16777230, 35034033)`; removed only `/tmp/ll-060-browser-fix/`, then asserted nonexistence. All receipts and inventories were retained in the two owned report files first. No debug instrumentation, browser process, server, temporary script or scratch workspace remains owned by this worker. Final source/public/skill inventories matched the recorded post-fix hashes immediately before cleanup.
