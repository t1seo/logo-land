# Independent Hermes workflow hands-on QA

Status: historical execution journal; final verdict is in ../review-qa.md. Scope: review only against f7dd3268313d2422b87efea63eef8257b0e651b9; source and canonical state are frozen.

## Plan

1. COMPLETED: pin sources, canonical state, protected drafts and review full relevant files.
2. COMPLETED: execute Chrome, CLI and bounded defensive scenarios.
3. COMPLETED: compare final hashes, remove owned resources and publish verdict.

## Scenario brainstorm before execution

Initial brainstorm: 25 scenarios, augmented by 7 adversarial/boundary scenarios before browser execution.

| Priority | ID | Expected behavior |
|---|---|---|
| P0 | S01 | Public sample opens from exact file URL; five identities visible |
| P0 | S02 | All five direct original PNG links decode and preserve exact hashes |
| P0 | S03 | Public package click downloads actual ZIP and exact e2 payload |
| P0 | S04 | Native r47 page opens with canonical e2 selected |
| P0 | S05 | Native package click downloads exact ZIP/manifest/guide |
| P0 | S06 | Canonical show returns r47/delivered/e2 without mutation |
| P0 | S07 | Parent lineage c1 → e1 → e2 is explicit and originals unchanged |
| P0 | S08 | Failed e1 preservation remains visible; e2 has two fresh passing reviews |
| P1 | S09 | Actual 192px views render without missing images |
| P1 | S10 | Public 390px viewport has no horizontal overflow |
| P1 | S11 | Native 390px viewport has no horizontal overflow |
| P1 | S12 | Keyboard Tab focus reaches useful controls with visible outline |
| P1 | S13 | Native comparison selection shows exact chosen parent and child |
| P0 | S14 | Feedback JSON binds workflow/revision/candidate/hash correctly |
| P0 | S15 | Draft choose/revise changes only browser draft, never canonical choice |
| P1 | S16 | Clipboard success copies the exact draft where available |
| P1 | S17 | Clipboard unavailable/denied gives manual-copy fallback |
| P1 | S18 | Reload resets local draft and preserves canonical e2 |
| P1 | S19 | Back from original returns usable gallery |
| P1 | S20 | Cancel navigation/download leaves canonical state intact |
| P1 | S21 | Repeated compare/feedback/download remains deterministic |
| P0 | S22 | Browser requests stay file/local; no external page requests |
| P1 | S23 | English README renders visible white samples and direct sample link |
| P1 | S24 | Korean README renders visible white samples and direct sample link |
| P1 | S25 | Docs describe actual native process, limitations and IP credit |
| P0 | A01 | Malformed harmless CLI requests fail clearly without inference |
| P0 | A02 | Instruction-like local feedback remains inert data |
| P0 | A03 | Existing stale-state tests reject changed revision/hash before calls |
| P0 | A04 | Existing cancel/resume/repeated-interruption guards preserve outcomes |
| P1 | A05 | Dirty worktree and four protected drafts remain unchanged |
| P1 | A06 | Owned command deadlines and misleading success checks are finite |
| P2 | A07 | First harness failures retained; flakiness evidence attributed precisely |

## Resource ledger

- TODO: create and retain `docs/qa/hermes-workflow/review-qa/` only for reviewed evidence and screenshots.

## First harness errors

- Node REPL module discovery called `.catch` on synchronous `import.meta.resolve`; TypeError was caught by the tool before any browser, source mutation or native action. Correct discovery will use try/catch; this is not product evidence.
- Second harness discovery error: bundled Node REPL `import("playwright")` failed with missing default export from `./index.js`; this happened before any browser or scratch root existed. Existing absolute package entry points will be resolved.
- Browser tooling hypotheses: H1 package absent (inspect existing package paths); H2 REPL ESM bridge misinterprets CommonJS (compare createRequire with dynamic import); H3 browser binary/profile failure (only evaluate after a module loads). Both virtual playwright imports had the same loader error; shell package resolution was absent in this repository. No browser was launched by those attempts.
- Module-loader resolution: existing `/opt/homebrew/lib/node_modules/openclaw/node_modules/playwright-core` loads through `createRequire`; no package installed. The default REPL import bridge was the failed surface, before product execution.
- TODO: create exact scratch `/tmp/logopia-review-qa-080/`; remove the entire owned root after receipts are saved.
- TODO: launch isolated headed Chrome profile `/tmp/logopia-review-qa-080/chrome-profile`, managed downloads `/tmp/logopia-review-qa-080/downloads`, and Playwright pipe transport. Close context, remove directories, verify owned descendants gone.
- TODO: download public package to `/tmp/logopia-review-qa-080/downloads/public-package.zip`; inspect members without extraction and delete it at cleanup.
- Native first browser assertion: Node REPL `deepStrictEqual` rejected a cross-realm Playwright array despite identical five IDs (`Values have same structure but are not reference-equal`). Exact serialized identity comparison resolves the harness boundary; the first result is retained here.
- Existing renderer discovery: `uv run --locked python -m markdown_it --help` exited 1 because the package has no __main__; its installed console entry point is `markdown-it=markdown_it.cli.parse:main`.
- TODO: download native package to `/tmp/logopia-review-qa-080/downloads/native-package.zip` and guide to `/tmp/logopia-review-qa-080/downloads/native-guide.md`; delete at cleanup.
- TODO: bounded owned child `uv run --locked python integrations/hermes/studio.py show --workflow offcut-hermes-demo --json` (30 s); await settlement, retain concise receipt, no persistent process.
- TODO: bounded owned child `uv run --locked python integrations/hermes/studio.py --help` (30 s); await settlement, retain concise receipt, no persistent process.
- TODO: bounded owned child `uv run --locked python integrations/hermes/studio.py show --workflow review-qa-080-no-such-workflow --json` (30 s); await settlement, retain concise receipt, no persistent process.
- TODO: bounded owned child `uv run --locked python integrations/hermes/studio.py show --workflow invalid id --json` (30 s); await settlement, retain concise receipt, no persistent process.
- Public first detail selector was ambiguous for e1 because the real page has separate exact-feedback and review disclosures; Playwright strict mode stopped the action. Narrowing by the visible review summary text preserves both product disclosures and assertions.
- TODO: exercise clipboard permissions only in the isolated Chrome context; clear permissions and detach owned CDP session at cleanup.
- Clipboard fallback harness first wait timed out at 7 s after denying the unsanitized descriptor; the UI still truthfully reported a successful copy. Hypotheses: descriptor mismatch for sanitized text, file-origin scoping, or active user-gesture permission. Saved queried permission states distinguish these before retry.
- TODO: start two owned cancelled package download attempts inside the registered downloads directory, then one recovery download; cancel through Playwright and remove all files at cleanup.
- TODO: create one JavaScript-disabled incognito context in the owned Chrome instance for no-JS snapshot checks; close this context after the check.
- TODO: render `README.md` and `README.ko.md` through installed `uv run --locked markdown-it` into exact scratch files `readme-en.html` and `readme-ko.html`, each child limited to 30 s. Wrapper only supplies local base URL and display CSS; remove both files at cleanup. No server/port 8816 is needed.
- TODO: run only 14 selected defensive pytest cases (listed in tests-receipt.json) with basetemp `/tmp/logopia-review-qa-080/pytest`, no pytest cache provider, bytecode disabled, outer 120 s deadline; fixture child commands already use finite timeouts. This closes failure-state gaps that cannot be triggered against the frozen real demo. Remove exact basetemp after settlement.
- TODO: run existing seven-case `node --test tests/hermes/gallery-feedback.mjs` with 30 s deadline; await settlement, no new file fixture expected.
- Direct public Markdown guide navigation: Playwright response-body hash differed from raw download bytes. The first failure and screenshot are retained. Hypotheses: file source changed; browser text decoding changes CDP response bytes; wrong navigation response selected. Verify URL, raw source digest, browser encoding and exact decoded-text equivalence before classifying.
- Direct-guide diagnosis resolved: canonical/raw/download guide SHA is unchanged; rendered `<pre>` text equals original UTF-8 exactly. CDP/Playwright response.body on charset-less text/markdown instead equals Windows-1252-decoded bytes, so it is not raw-byte evidence for this text resource. The first failed assumption is preserved; binary downloads remain exact and user-visible guide text is correct.
- Horizontal comparison harness initially used End, which did not move the horizontal region. First observation retained; use directional ArrowRight on the focused region for the intended horizontal interaction.

## Cleanup execution

- All bounded CLI/test/renderer children have settled. Chrome root PID 12556 and initially observed descendant PIDs 12611, 12612, 12626, 12638, 12642, 12643 belong to the exact registered profile.
- Completed: CDP detached, isolated permissions cleared, both contexts closed, all recorded Chrome PIDs absent and zero profile process matches. Exact scratch root (including 575 entries of browser cache, tests, renders and downloads) removed and absence checked; port 8816 has no listener.

### Final dependency hold
- Source drift detected after the completed original QA and cleanup: installer.py changed under coordinator authorization. No reviewer source edit occurred.
- Named dependency FIXES_READY covers launcher_process.py, helper_process.py, optional process_group.py, installer.py and dedicated regressions, plus native-run.md precision wording.
- The original browser/artifact evidence remains bound to the pre-fix pins. Final integrated PASS and worker_done are withheld until narrow revalidation.
- No new temporary resource has been created during this hold.

- msg_34e840ac7f11: original four failures independently GREEN; installer owner settled. Added process-boundary defects keep FIXES_READY pending. No further browser/inference/test run or temporary resource was started by this reviewer.

- Read final process-owner manual/cleanup summary and current code-review gate. Code-review gate reports a root integration failure in repeated-helper interruption; final FIXES_READY remains pending. This reviewer did not rerun any tests, reopen Chrome or recreate scratch.

- First final-binding harness failure retained: managed_records is a map, not an array; .slice failed before verification. Corrected map iteration only; no product source, fixture or inference was changed.

### Final gate completed
- FIXES_READY msg_38ec653e2ac0: coordinator final pytest 957 passed / exit 0; all eight gates exited 0. Original 2-failure integration trace is retained and attributed.
- Independently read final changed modules/regressions, matched 209 root-pinned input hashes, hashed all 61 installed records (60 source plus local settings), verified canonical five PNGs/r47/e2 and all 21 native-gallery files.
- No new resources, inference, profile writes or test reruns during final revalidation. Original cleanup and post-cleanup receipt confirm absence.
- QA verdict PASS; lifecycle completion will be sent once after final report validation.
