# OFFCUT public sample QA

Status: **passed and cleaned up**. Final native delivery dependency received at revision 47, phase `delivered`, selected `e2`.

## Scope and sequence

1. Complete: pin canonical read-only revision, original SHA256 and dimensions; reproduce missing entrypoint and direct originals.
2. Complete: publish an offline, English-default curated example with byte-exact originals.
3. Complete: bind publication metadata and delivery links to the coordinator's final native receipt.
4. Complete: validate links, bytes, decoded images and actual Chrome interactions; record screenshots.
5. Complete: remove exact owned runtime resources and record absence receipts.

Only `docs/hermes-demo/`, this report and `public-sample/` QA artifacts are owned by this worker. Other workers' edits and four unrelated `logo-land-next-*.md` drafts are preserved. No commits, source Python changes, model/image calls, profile changes or new agents are authorized.

## Resource register (before creation)

All runtime resources below are exclusively task-owned. Raw logs stay under the already ignored `output/` tree.

| Resource | Intended use | Cleanup |
| --- | --- | --- |
| `output/hermes-preflight/public-sample-task9f041573/` | Task-local temporary root and retained raw logs | Remove all contents except raw `.log` files |
| `…/pin.json`, `…/foreign-before.json` | Read-time canonical and foreign-file pins | Remove after sanitized evidence is retained |
| `…/final-pin.json`, `…/delivery.json` | Coordinator-announced final snapshot and verified delivery allowlist | Remove after public projection is verified |
| `…/inert-fixture.html` | Escaped markup-looking note browser check | Remove exact file |
| `…/red.cjs`, `…/verify.cjs`, `…/render.cjs` | Temporary browser, content and byte checks | Remove exact files |
| `…/playwright/` | Task-local Playwright package if existing installation is unavailable | Remove exact directory |
| `…/npm-cache/` | Task-local package cache if installation is needed | Remove exact directory |
| `…/chrome-profile/` | Owned isolated installed Google Chrome profile | Close owned browser, remove exact directory |
| `…/chrome-public-final/`, `…/chrome-native/` | Fresh task-only profiles for final independent browser passes | Close each owned context, remove exact directories |
| `…/downloads/` | Browser download and cancellation checks | Remove exact directory |
| `…/chrome-artifacts/` | Owned browser transient files | Remove exact directory |
| Browser and Node child PIDs | PID receipts are recorded as soon as allocated | Close/reap only exact owned processes |
| Port | None planned; file URL browser checks | No server cleanup expected |

Screenshots and sanitized QA receipts under `docs/qa/hermes-workflow/public-sample/` are intentional retained artifacts. No task-local resource is created before registration here.

## Initial hypotheses

- Missing public entrypoint: file navigation will fail before an `index.html` exists; build the page.
- Missing direct originals: public candidate PNG paths will fail although canonical originals decode; copy exact bytes.
- Existing unpublished or stale sample: repository search and snapshot binding will distinguish a stale page from absence; publish only final named receipt metadata.

Live provider cancellation and model execution are N/A for this worker because the coordinator owns the native workflow. Local browser cancellation is in scope.

## PIN and RED evidence

Read-time revision **37**, phase `revising`, at `2026-09-14T16:34:06.895Z`. This is an initial read pin, not publication metadata or a final approval. Exact original SHA256, PNG header dimensions and byte lengths are in [initial-pin.json](public-sample/initial-pin.json); complete browser decoding is verified in the final browser pass.

Installed Google Chrome **152.0.7977.83**, driven headed through task-local Playwright **1.63.0**, returned `net::ERR_FILE_NOT_FOUND` for the entrypoint and all three future public original paths. [RED receipt](public-sample/red-receipt.json) and [first failure screenshot](public-sample/missing-entrypoint.png) retain the observed failures before public files were built. The RED browser context closed normally.

The first intermediate browser pass passed every direct original click/decoded size, keyboard navigation, 390px exact document width, reload/back/repeated clicks, inert markup-looking note, no page errors and no external requests. This was a preparation snapshot; the final pass must replace screenshots and bind them to revision 47.

The first final-snapshot pass completed the actual ZIP download/hash check, then correctly cancelled another download. Its cleanup harness initially treated Playwright's `download.delete: canceled` response as a failure. [First final-pass failure](public-sample/verification-first-failure.json) is retained. A second bounded check proved that Chrome also leaves an owned `.crdownload` after context closure; [that failure](public-sample/verification-cancel-cleanup-failure.json) is retained. The corrected harness accepts only the exact cancelled response, closes the context, removes each exact owned `.crdownload`, and verifies the directory is empty. Any other error or unexpected file still fails. No product source or canonical artifact changed for these harness corrections.

A subsequent pass using the already-used profile reported `download.saveAs: Target page, context or browser has been closed`. Its actual [failure receipt](public-sample/verification-context-close-failure.json) is retained. The final public/native passes use separate fresh task-only profiles, browser lifecycle logging and a 30-second save deadline. Candidate causes checked are profile reuse after cancelled downloads, external browser termination, and download completion behavior; the error alone does not establish which closed the context.

## Final native dependency

Coordinator message `msg_c795c1a910a4` explicitly announced **FINAL NATIVE DEPENDENCY READY**: revision **47**, phase **delivered**, selected **e2**, final snapshot `output/hermes-demo/final-workflow.json`, receipt `output/hermes-demo/final-binding.json`. These files are read-only sources; neither the private snapshot nor receipt is copied into the public page. All five originals remain available, including e1 with its failed preservation checks. A separate [native Studio browser report](native-gallery.md) covers the additional read-only scope assigned in `msg_07dc8c76e845`.

## Final verified result

[Public offline page](../../hermes-demo/index.html), [English README](../../hermes-demo/README.md), [Korean README](../../hermes-demo/README.ko.md), and [curated record](../../hermes-demo/example.json) are frozen to **r47 / delivered / e2**. The source snapshot SHA256 is `16eea6dc8c32e979c432fbdffee137d76cb68a230aad9e5b65cc740d59e26e04`; the read-time and final pins are separate. The native export manifest's revision **8** is its helper-session export revision, not the workflow revision **47**.

| Original | Parent | Decoded size | SHA256 |
| --- | --- | --- | --- |
| c1 | none | 1774 × 887 | `30e46b31716db37cfa51d7fb2f5406e48275727c9ccaef6d54a0d1ee4a2a878f` |
| c2 | none | 1254 × 1254 | `f7962dee46e27c406039da75e1bd314322e4cd3510cfc8d9686d5cd64a3961c3` |
| c3 | none | 1254 × 1254 | `68734a451c89f499e54f5366e5fe04cc49d6b58ca329604373ee6657c9720aea` |
| e1 | c1 | 1774 × 887 | `08196269c02184cd99237a0e2a8306e039f1d13eac0a9261ce652f6c5b0a6560` |
| e2 | e1 | 1774 × 887 | `882dd3318064ef2573344d9b4dfef5bf9d460f5a9bb0aaf2f585dd2473c887bb` |

[The final verification receipt](public-sample/verification.json) records **64 local href/src references checked**, all five exact source/public PNG byte comparisons, actual browser decoding and clicks for every `a[data-original]`, and these observed outcomes:

- Headed installed Chrome 152.0.7977.83 on the requested local `index.html`: 1440px desktop and **390px document width exactly**, including expanded exact feedback.
- `page.click('a[data-original="c1"]')` opens the exact original; repeated for c2, c3, e1 and e2 on desktop and mobile. Keyboard navigation, skip link, review disclosure, three reload/back/repeated c1 cycles all passed.
- `page.click('#download-package')` downloads the actual **711,451-byte ZIP**, SHA256 `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04`. Its selected PNG, manifest and guide are byte-identical to the verified root package and the direct public files.
- Actual cancellation returns `canceled`; after exact owned cleanup the download directory contains **zero files**. The fresh-profile final pass exited 0.
- The shared escaping path rendered `<note data-kind="example">…</note>` as literal text in an isolated temporary fixture, with no `note` element or executable script. No example data executed.
- **Zero page errors, external requests or failed requests**. Public HTML uses no JavaScript or external dependencies; public JSON uses explicit allowlisted fields. Exact requested export ZIP/manifest/guide bytes are preserved, including their design request and color evidence, and contain no absolute local paths, authentication or private native receipts.

Visual inspection passed for [desktop](public-sample/desktop.png), [mobile](public-sample/mobile.png), and [exact feedback at mobile width](public-sample/mobile-exact-feedback.png). No artwork was edited, cropped, resized into derivative files or rendered into scripted thumbnails; all inline views reference the source PNG bytes.

## Scope, review and limits

Goal/constraint, content quality, defensive handling, actual usability and surrounding documentation/provenance were reviewed directly. The request prohibits new agents, so these are not represented as independent agent reviews. The meaningful documentation checks above replace markup-mirroring tests. `git diff --check` and the temporary browser runners' syntax checks passed; no production language source, build input or Python file changed in this task. The coordinator's 907-test T2 baseline is contextual evidence, not a test run claimed by this worker.

[Foreign-file preservation](public-sample/foreign-preservation.json) confirms all **170** baseline foreign paths still exist and the four unrelated drafts remain byte-identical. Seven shared documentation files changed concurrently under other owners; their changes were preserved. The public page makes no new provider calls, automatically resumed jobs or human approval claims. Provider execution/cancellation, remote target experiments and native state mutation remain N/A for this worker.

## Cleanup receipt

[Exact cleanup evidence](public-sample/cleanup.json) records **17 registered temporary resources removed**: three isolated Chrome profiles, browser artifacts, downloads, task-local Playwright/npm cache, private pins, fixtures and four runners. **Zero owned Chrome processes, temporary profiles, scripts or downloaded files remain**; no server or port was opened. All contexts closed, all five original hashes and the final canonical/native-gallery bytes still match. Only ten ignored raw `.log` files remain under the task's runtime root; public files, reports, sanitized receipts and screenshots are intentional deliverables. No task-owned work remains outstanding.

The final absence audit initially counted its own shell command text as a profile match. Restricting the scan to actual Chrome executable identities before checking each process's profile argument confirmed **zero owned Chrome processes**. [Publication file hashes](public-sample/publication-files.json) retain the final public artifact inventory and final local-link audit.
