# Offline gallery implementation and QA

**Result: implemented and verified through actual Chrome.** The gallery publishes a fresh standalone snapshot, preserves canonical selection and original/prompt bytes, and drafts strict core feedback for Hermes. The retained artwork is deterministic local QA fixture art, not model-generated work or live critique evidence.

Scope: gallery-owned modules/assets/tests only, plus this report and its screenshot directory. Existing comparison baseline is `f7dd3268313d2422b87efea63eef8257b0e651b9`. Core `Workflow`, `Candidate`, `FeedbackEnvelope`, and `StudioError` are named dependencies; no shadow domain models are permitted.

## Execution ledger

1. Complete: baseline pin passed; publisher RED 9 failures (explicit missing publisher); interaction RED 7 failures (explicit missing feedback implementation).
2. Complete: original publication/feedback behavior, plus failing-first stale review, offline download and workspace-alias regressions.
3. Complete: **15 pytest tests passed**, **8 Node tests passed, zero skipped in the actual browser run**, Ruff clean, formatting clean, and basedpyright targeting Python 3.11 reports **0 errors, 0 warnings, 0 notes**.
4. Complete: actual Chrome file-URL interaction, original byte download/open, 390px viewport, keyboard, parent comparison, stale/reload, no-JavaScript and adversarial QA.
5. Complete: owned browser contexts/profiles/downloads/fixtures closed and removed; task-local Playwright, final pytest fixture directory and gallery Python caches removed. No owned Chrome process or task temporary root remains.

## Implementation and integration

- Public entry point: `logopia_studio.gallery.publish_gallery(workspace, state, output) -> Path`. **`output` is the new publication directory**, not a reusable parent. Existing files, directories and symlinks are rejected with `StudioError` rather than overwritten. The caller provides a fresh path each time.
- `gallery_files.py` validates the actual PNG bytes, original digest and measured dimensions, copies exact UTF-8 prompt bytes and a prompt SHA-256 sidecar, verifies written bytes and rolls back only owned files. A simulated disk-full failure leaves a concurrently created foreign note intact.
- `gallery_review.py` consumes core `review_input`, `verify_critiques`, `unmet_criteria` and their target-view evidence. The gallery does not create replacement domain models or infer approval from a selected candidate. New children remain unreviewed until their own records exist.
- Ivory/ink page, white original cards, short strategy, every candidate, exact CSS display width, two critique summaries, parent/child comparison, expandable provenance, and explicit revision-bound feedback. No remote scripts, fonts, fetch, live server or unsafe HTML insertion.
- `FeedbackEnvelope` supplies the embedded candidate templates. The browser copies exact workflow ID, expected revision, candidate ID/hash, action and keep/change data. Previewing, copying, choosing a draft action and clearing a draft do not mutate the canonical workflow. Old revisions and mismatching stored hashes are rejected rather than silently rebound.
- PNG download uses a data URL containing the verified original bytes; a separate direct file link opens the original. This intentionally adds one base64 copy of each original to the HTML so Chrome can download locally without JavaScript or fetch. Published original files remain separate byte-identical PNGs. No ZIP is fabricated or linked by this gallery.
- No-JavaScript originals and identity remain usable. Clipboard rejection selects the complete JSON for manual copy; the page says the draft still needs to be sent to Hermes.

## Verification evidence

Environment: repository Python **3.12.12**, Pydantic **2.13.5**, Pillow **12.3.0**, Node **26.8.1**, task-local Playwright **1.63.0**, installed Google Chrome **152.0.7977.83**. Python compatibility was checked with basedpyright's **3.11** target; native Hermes runtime/doctor and inference are coordinator scope.

Commands run against gallery ownership:

```sh
uv run --locked pytest -q tests/hermes/test_gallery*.py
LOGOPIA_GALLERY_QA_ROOT=/tmp/logopia-gallery-ctx_18edf8576e12.H4SYBo node --test tests/hermes/gallery*.mjs
uv run --locked ruff check --target-version py311 integrations/hermes/logopia_studio/gallery*.py tests/hermes/test_gallery*.py
uv run --locked ruff format --check --target-version py311 integrations/hermes/logopia_studio/gallery*.py tests/hermes/test_gallery*.py
uv run --locked basedpyright --pythonversion 3.11 integrations/hermes/logopia_studio/gallery*.py tests/hermes/test_gallery*.py
```

The browser runner generates and publishes actual fixture workspaces, launches the installed Chrome executable with an isolated profile, uses `page.goto(fileURL)`, and performs the exact requested sequence:

```text
click [data-feedback="candidate-2"]
fill #keep = 색과 열린 중심
fill #change = 간격만 넓혀 주세요
click #copy-feedback
assert #feedback-output contains exact workflow/revision/candidate/hash/notes
assert canonical workflow.json bytes are unchanged
```

The copied envelope is workflow **`gallery-fixture`**, revision **7**, candidate **`candidate-2`**, action **`revise`**, keep **`["색과 열린 중심"]`**, change **`간격만 넓혀 주세요`**. Both the actual downloaded file and opened PNG response match SHA-256 **`cf9efc33175d74fd801fb2ef32e265f31a91b1724154eb7d7f43b99834fb27fe`**. [Machine-readable browser receipt](gallery/browser-receipt.json).

| Scenario | Result / evidence |
| --- | --- |
| Exact original, prompt, prompt digest and state | PASS; publisher tests compare actual bytes for all four fixture candidates |
| Existing comparison unchanged | PASS; both baseline SHA-256 values pinned in `test_gallery_baseline.py` |
| Existing foreign/dirty output | PASS; prior index preserved; injected write failure removes owned files and retains the foreign note |
| Missing, changed, malformed PNG, dimension mismatch, escaping source | PASS; typed errors, no published index |
| Publication independent of source | PASS; source originals removed after publication without changing any published bytes |
| Core-valid feedback schema, exact notes, inert instruction-like text | PASS; core model parsing plus Node strict envelope tests |
| Real copy action and immutable canonical choice | PASS; [desktop feedback](gallery/desktop-feedback.png) |
| Actual original download and original opening | PASS; both measured hashes match the canonical candidate hash |
| Repeated reload/back/draft actions | PASS; three reloads and repeated activation retain the exact draft |
| Clipboard denied | PASS; full output is selected, with explicit manual-copy guidance |
| Keyboard Enter and Tab | PASS; candidate → keep → change → copy; parent disclosure also works |
| Parent and child at equal 192px | PASS; [parent/child comparison](gallery/parent-child.png) |
| Mobile page width | PASS; `documentElement.scrollWidth === 390`, including the 1024px preview fixture |
| Actual target display widths | PASS; DOM bounding boxes equal **192px** and **1024px**, with bounded inner scrolling |
| Normal vs stale critique evidence | PASS; [normal mobile candidate](gallery/mobile-candidate.png); deliberate view-hash mismatch stays visible |
| New revision, stale stored revision and candidate digest | PASS; no silent substitution or borrowed draft |
| Choice draft / clear / reload | PASS; canonical selection remains candidate-1 and the cleared draft stays empty |
| HTML-looking user text | PASS; literal text visible, zero injected DOM nodes |
| No results / no JavaScript | PASS; [empty state](gallery/empty-state.png); static originals and identity remain usable |
| External calls / runtime errors | PASS; zero external page requests and zero page errors |

Other inspected screenshots: [desktop overview](gallery/desktop-overview.png), [desktop comparison](gallery/desktop-comparison.png), [mobile overview](gallery/mobile-overview.png), [mobile feedback](gallery/mobile-feedback.png). Screenshots were opened and visually reviewed; the final feedback screenshot shows the full JSON including both notes.

All owned modules are below 250 lines even when counting blank lines and comments: largest Python file **162 lines**, largest JavaScript test **207 lines**. No `Any`, `object`, `cast`, type-ignore or pyright-ignore annotations were introduced in Python.

## Review and limits

The review-work skill's goal, QA, code quality, defensive handling and surrounding-contract checks were performed directly. No new agents were launched because this dispatch explicitly prohibited them. Local history and current launcher/registration consumers were checked; their fresh publication paths match this API. No blocking finding remains in the gallery-owned scope.

Live inference, native image generation/editing, provider cancellation, server shutdown and native Hermes doctor are **N/A** for this offline assignment; no model/image call was made. No commits, upstream Hermes edits, shared dependency changes, global config changes or edits to other workers' drafts were made. Broader integration acceptance remains with the coordinator.

## First observations

- Core modules are not yet present at dispatch start. Gallery work begins with independent feedback tests and assets; publisher tests will consume the delivered core models.
- Legacy comparison SHA-256 is pinned by `test_gallery_baseline.py` for both the Python implementation and HTML template.
- Mobbin tools are unavailable as stated in the task. The supplied design research and the specified ivory/ink direction are the UI reference.
- Additional review-evidence RED: a deliberately stale `view_sha256` lacked a visible mismatch label; the gallery now delegates original/parent/target-view evidence to core `checks` instead of maintaining partial duplicate checks. The next targeted run passed 13 tests.
- First real Chrome run: exact feedback/canonical immutability and three reloads passed. The download event failed after its bounded 7-second deadline; `browser-first-failure.png` shows the native image viewer, not a download. Receipt retained in `gallery/browser-first-failure.json` and its owned profile/fixture/download folders were closed/removed in `finally`.
- Download hypotheses: H1 file-URL download attribute ignored (confirmed by native image-viewer navigation); H2 missing/invalid PNG (refuted by decoded visible source and publisher hash tests); H3 clipboard/reload state prevented click (refuted by successful click navigation). Fix: a byte-identical PNG data-URL download alongside the existing direct original link. This intentionally duplicates PNG bytes inside HTML to guarantee offline download without fetch or JavaScript.
- Visual review found the normal candidate tagged as mismatching when its workspace used macOS `/tmp`. A failing workspace-alias regression isolated the cause: core `safe_path` expects an already-resolved root. `review_labels` now resolves the explicitly supplied workspace before invoking core checks. The normal and deliberately stale cases remain distinct.

## Resource ledger

- Registered before creation: `/tmp/logopia-gallery-ctx_18edf8576e12.XXXXXX` from `mktemp`, containing task-local Playwright 1.63.0, generated publication fixtures, isolated Chrome profiles and downloaded test PNGs. Remove the exact allocated directory after closing owned contexts.
- Registered before creation: actual Google Chrome launched with `launchPersistentContext` using only a profile beneath that temporary root, no user profile and no fixed port. Each context closes in `finally`.
- Registered retained artifacts: `docs/qa/hermes-workflow/gallery/` screenshots and browser receipt, this report and source tests.
- Live model calls, image calls, provider cancellation and server QA are N/A for this offline task.
- Browser setup references: [isolated context API](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context), [download byte capture](https://playwright.dev/docs/downloads).

**Cleanup verified:** [cleanup receipt](gallery/cleanup-receipt.json) records `ownedChromeProcesses: 0`, `contextsClosed: true`, and `temporaryRootExists: false`. The allocated root `/tmp/logopia-gallery-ctx_18edf8576e12.H4SYBo`, its node tooling/package files and the final bounded pytest fixture directory were removed. Gallery-specific Python caches were removed without touching other modules' caches. Only source/tests/report/screenshots and QA receipts remain as gallery artifacts. No user tabs, existing profile, server, fixed port or global configuration was touched.

To repeat the browser QA after cleanup, install `playwright-core@1.63.0` with `npm install --prefix <new-temporary-directory> --no-audit --no-fund --ignore-scripts`, then supply that directory as `LOGOPIA_GALLERY_QA_ROOT`. The runner owns and closes its contexts, profiles, downloaded files and fixture directories even if setup or an assertion fails. Remove that temporary tooling directory afterward. Without the variable the ordinary Node run clearly skips the real-browser test; the reported run above set it and skipped **zero** tests.
