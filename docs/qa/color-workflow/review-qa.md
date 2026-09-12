# Independent hands-on QA review

Review date: 2026-09-13 KST. Base: `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`; working-tree changes and new files are included. Reviewer owns this report and `output/review-qa/` only. Source and shared evidence are read-only. No new image generation, image edits, installation, browser control, commit or publication is authorized for this review.

## Verdict: FAIL for whole-goal completion and public release (HIGH confidence)

Required restricted-color and white-transparent native outputs remain unapproved after the permitted repairs. The helper correctly refuses those exports; passing deterministic checks cannot satisfy the missing native gates. The code and truthful documentation are suitable to commit as an explicitly **unreleased development preview** from this QA perspective (MEDIUM-HIGH confidence), with no newly discovered CLI blocker. This is one independent QA verdict, not approval on behalf of the other four reviewers.

## Scenario brainstorm and task list

The first 25 scenarios were written before executing the application. Five additional scenarios follow from a fresh misuse/environment review. Fixtures exercise logic only and never count as native generation. Each row is one task. Core CLI safety scenarios were prioritized, followed by gallery/evidence checks and selective dependent rechecks; actual command order is retained in the numbered receipts.

| ID | Priority | Steps and expected result | Result |
|---|---|---|---|
| 01 | P0 | Run source CLI help/init/show/list in a new workspace; usable JSON and revision 0. | PASS |
| 02 | P0 | Propose an automatic warm palette; advisory policy and real rationale, no mutation. | PASS |
| 03 | P0 | Propose anchor palette; normalized exact green lock survives. | PASS |
| 04 | P0 | Propose black/ivory allowed+required+max-two palette; strict constraints compose. | PASS |
| 05 | P0 | Add real local PNG reference then propose palette; copied bytes, hash and extraction match. | PASS |
| 06 | P0 | Combine reference+anchor+max-two; normalized provenance and constraints survive save/prompt. | PASS |
| 07 | P0 | Submit locked/allowed conflict, overfull mandatory set, gradients with limit, bad HEX; named errors without mutation. | PASS |
| 08 | P0 | Prompt then mutate then import old revision; stale import leaves no artifact. | PASS |
| 09 | P0 | Import green parent, navy child, geometry child with active green; parent palette and lockup win. | PASS |
| 10 | P0 | Reselect green original after navy child; export reflects green original intent. | PASS |
| 11 | P0 | Export fully visually approved strict mismatch fixture; color_mismatch and no output/state change. | PASS |
| 12 | P0 | Export strict native indeterminate case; color_review_required persists after visual approval. | PASS |
| 13 | P0 | Resume schema 1 with show/list/prompt; state bytes unchanged and old palette unknown. | PASS |
| 14 | P0 | First successful schema-1 mutation; exact backup and schema 2 transition. | PASS |
| 15 | P0 | Select/review/export palette-less legacy artifact; no invented HEX or measured pass. | PASS |
| 16 | P0 | Reuse existing reviewed native original in isolated workspace; actual CLI export preserves original/ZIP bytes. | PASS |
| 17 | P0 | Inspect public successful original and failed repaired PNG independently; distinguish color pass from background correctness. | PASS |
| 18 | P0 | Audit eight native cases and bounded repairs; anchor/restricted/white release gates match actual evidence. | FAIL native release gate; evidence audit PASS |
| 19 | P1 | Render gallery of parent/children; session revision and PNG bytes unchanged. | PASS |
| 20 | P1 | Render script-like brand/notes; text escaped with no absolute paths or executable injection. | PASS |
| 21 | P1 | Relocate gallery directory and resolve local resources; all PNG hashes and links preserved. | PASS |
| 22 | P1 | Duplicate IDs, unknown parent/palette/reference, stale palette addition; named errors and no partial writes. | PASS |
| 23 | P1 | Move original external reference away; subsequent extraction uses intact copied source. | PASS |
| 24 | P1 | Read Chrome evidence and representative screenshots; scope and failures agree with public prose. | PASS |
| 25 | P1 | Read installation evidence, bilingual examples and font/lockup claims; documented limits remain explicit. | PASS |
| 26 | P0 | Tamper a stored report to passed; export recomputes and rejects actual mismatch. | PASS |
| 27 | P0 | Alter imported PNG bytes; export rejects hash mismatch before delivery. | PASS |
| 28 | P1 | Retry gallery into existing or reserved/outside directory; no overwrite or state mutation. | PASS |
| 29 | P1 | Supply malformed ROI and forged reference extraction; reject without state mutation. | PASS |
| 30 | P1 | Migrate with conflicting existing v1 backup; fail and preserve both byte sequences. | PASS |

## Completed execution

1. Completed: P0 CLI behavior in the isolated workspace, including strict rejection, stale revisions, migration, original-byte export and inherited palette/lockup intent.
2. Completed: P1 CLI safeguards, portable gallery checks and independent native/Chrome/installation evidence inspection.
3. Completed: all 30 scenarios reconciled and development-preview readiness separated from whole-goal/public-release completion. No implementation edits are required by a newly discovered CLI failure.

## Coverage and evidence

- **30 scenarios assessed:** P0 20 assessed, 19 pass, 1 native release-gate failure; P1 10 assessed, 10 pass; P2 none planned. Scenario 18's evidence-integrity assertions passed while the required native success gate failed.
- **98 actual source-CLI invocations:** 67 exited 0 and 31 exited 1. Negative cases deliberately require exit 1. The final logic/evidence harness has 30 successful assertions; this does not mean 30 successful native workflows.
- Local exact argv, stdout, stderr and exit status are preserved in `output/review-qa/receipts/001-*.json` through `098-*.json`; `command-index.json` maps every command. Final results are in `results.json`, native hash/count checks in `native-evidence.json`, and source/evidence snapshot hashes in `reviewed-file-hashes.json`. These local records contain absolute workspace paths and are intentionally not published.
- Runner: `output/review-qa/run.mjs`. Execution logs: `terminal.txt`, `terminal-recheck.txt`, `terminal-evidence.txt`. Workspace: `output/review-qa/workspace/`; relocated gallery: `output/review-qa/relocated-gallery/`. The runner is a retained execution record, not a native-generation test or an idempotent rerun command against its already populated workspace.
- Initial harness mistakes are preserved in `results-initial.json`: two hand-authored QA palettes omitted required `selected_by`/`rationale`, and an unknown-parent test omitted required `--changes`. The helper correctly rejected them. Six scenario failures were fixture/dependency/expectation failures; corrected inputs and dependent scenarios were rerun selectively, including reselect/export after the child actually existed. No production code was changed to make a check pass.

### Actual observations by scenario

| IDs | Observed behavior | Exact local receipt numbers |
|---|---|---|
| 01–04 | Help/init/show/list returned usable responses; fresh revision 0. Automatic candidates were local-harmony proposals; anchor lower-case input normalized to #247A52; black/ivory allowed+required+max-two stayed exactly two colors. Proposals did not mutate state. | 001–007 |
| 05–06 | GROVE reference copied byte-for-byte; SHA-256 768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06. Extraction used 16,384 positions with explicit full-image scope. Combined reference+green lock+max-two saved and prompted as palette combined, revision 2, with extraction response and reference hash. | 008–012 |
| 07–08 | Conflicting locks/allowed set, too many mandatory colors, gradients+limit, named color, and max_colors=0 all failed. Prompt revision 2 became stale after palette-add raised revision to 3; import returned stale_revision, with no stale.png or state change. | 013–020 |
| 09–10 | Green parent → navy child with stacked/end/center lockup → active green palette → geometry child. Prompt and import bound geometry to navy and the parent's stacked lockup. Reselecting green exported green's strict passing report and original bytes after children existed. | 061–068 |
| 11 | Reused real green PNG under an incompatible strict black-only fixture palette. All five visual booleans were true; export returned color_mismatch (less than 99% target coverage; no required black samples). No delivery directory or state update. | 069–073 |
| 12 | Original 밤결 reimport returned indeterminate with 615 partial-alpha samples / 2,697 visible. All-true review did not override color_review_required; state and output remained unchanged. | 030–035 |
| 13–15 | Historical LUMA export.json reconstructed a schema-1 session with original PNG. show/list/prompt preserved exact bytes and created no backup. Select revision 4 wrote schema 2 revision 5 with byte-exact backup; subsequent review/export succeeded. Manifest intended_palette=null, policy/status=unverified, explicit unknown-intent warning. | 036–041 |
| 16 | NORTHLINE used its existing native original, actual saved prompt, existing structured palette and recorded Chrome review. Export yielded schema 2/advisory/pass/appearance-reference-only. ZIP had exactly logo.png, manifest.json and brand-guide.md; every member matched its standalone file. | 042–047 |
| 17 | Viewed successful GROVE PNG and final warm a-v4 PNG. The latter visibly contains a painted checkerboard; fresh import measured zero transparent pixels while its anchor-only report passed. All-true review still produced background_mismatch, with unchanged state. | 086–091 |
| 18 | Verified 8 overview hashes, 17 public-vs-live artifact hashes and all 16 recorded native-source PNGs. Reanalysis of unchanged white-v3 reproduced 2,560 core / 923 partial / 3,483 visible samples, indeterminate, then color_review_required despite all-true fixture review. Required native release success remains absent. | 092–098 |
| 19–21 | Three-artifact gallery preserved state and all PNG hashes. Script/img-event payloads in brand, rationale and role were HTML-escaped; no full prompt, absolute home path, file URL or external HTTP dependency appeared. Relocated escape gallery's image and download links both resolved to the unchanged PNG. | 050–053, 075 |
| 22–23 | Duplicate palette/reference, missing palette/parent/reference and stale palette mutation returned named errors without changing state. Moving the external reference did not break subsequent extraction from its stored copy. | 057, 076–081 |
| 24–25 | Read complete Chrome and installation records, inspected saved screenshots, checked current corrected white report prose and current English/Korean development-version labels. Installation scope stays at 15 installed-cache CLI calls without fresh generation. | Evidence inspection; no browser/install call |
| 26–27 | Tampered saved mismatch status to pass and cleared reasons in the isolated fixture; export recomputed and rejected the PNG. Appending bytes to the isolated NORTHLINE artifact caused hash_mismatch before delivery. Original fixture bytes were restored after each test. | 048, 074 |
| 28–30 | Gallery collision, reserved .logo-generator/.git and outside-workspace destinations rejected. Oversized ROI and forged reference digest rejected. A conflicting v1 backup caused backup_conflict, preserving both original session and conflicting backup bytes. | 058–060, 082–085 |

### Reproduction commands

The following are workspace-relative equivalents of the recorded argv. They use the actual source entry point; input JSON and PNGs are retained in the review workspace. The remaining revisions are intentionally unchanged after rejected exports.

```sh
ll() {
  uv run --locked python skills/logo-land/scripts/logo_project.py \
    --workspace output/review-qa/workspace "$@"
}

# Strict mismatch, even after all visual booleans were true: exit 1 / color_mismatch.
ll export --session mismatch --revision 4 --output deliveries/forbidden

# Native restricted original: exit 1 / color_review_required.
ll export --session indeterminate --revision 4 --output deliveries/indeterminate

# Native white result, including explicit reanalysis: exit 1 / color_review_required.
ll export --session white-review --revision 5 --output deliveries/white-review

# Final warm repair: exit 1 / background_mismatch.
ll export --session warm-repair --revision 4 --output deliveries/warm-repair

# Parent wins over active green for a geometry edit: palette navy; stacked/end/center.
ll prompt --session inherit --parent navy --changes 'Spacing only'

# These successful export commands were executed at the recorded pre-export revisions.
# A repeat now must use a fresh destination and the current show revision.
ll export --session sample-01-luma --revision 6 --output deliveries/legacy
ll export --session northline --revision 4 --output deliveries/native
ll export --session inherit --revision 11 --output deliveries/green-after-child
```

The NORTHLINE source/imported/delivery/ZIP-entry PNG hash was `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534`. The independent review ZIP hash was `6eb96266d5660b0c8e1929aa73b9b3403b66ca275cf82dec7665b81bbba20873`; it is a new locally verified export and need not equal the earlier ZIP, which contains different export timestamps. No copied or reimported image in this review is counted as a new native generation or successful native edit.

## Blocking findings and release decision

### F1 — MAJOR / P0: required restricted-color native success is absent

Evidence: `docs/qa/color-workflow/native-cases.md:13`, `:15`; release acceptance at `plans/logo-land-color-workflow.md:291`. Original 밤결 is indeterminate (615/2697 partial alpha, 22.80%); FIELD NOTE is indeterminate (371/3019, 12.29%). Their two permitted repairs are documented opaque checkerboard/mismatch failures. The independent 밤결 export reproduction above returned color_review_required and preserved state/output. This blocks whole-goal/public-release PASS; deterministic constrained-palette success is not a substitute. Preserve the originals and failed attempts; keep the release unpublished under the current gate.

### F2 — MAJOR / P0: required white-transparent native success is absent

Evidence: `docs/qa/color-workflow/native-cases.md:16`; threshold enforcement at `skills/logo-land/scripts/logo_helper/color_delivery.py:45`; release acceptance at `plans/logo-land-color-workflow.md:291`. Independent color-analyze of the unchanged final white-v3 reproduced **923/3483 partial-alpha samples (26.50%)**, with 2,560 core samples. Export stayed color_review_required after all-true fixture review. This is a quantitative gate failure, not a claim that the Chrome preview has damaged lettering. Two additional white edits were already used, so this review neither generates again nor relaxes the policy.

### F3 — MAJOR / P1 native-output limitation: warm companion edit has no transparent deliverable

Evidence: `docs/qa/color-workflow/native-cases.md:12`, actual `docs/colors/assets/04-grove-warm.png`, background gate at `skills/logo-land/scripts/logo_helper/delivery.py:126`. I independently saw the dense gray checkerboard in a-v4 and confirmed zero transparent pixels through import. Its anchor-only report passes but export correctly returns background_mismatch. The requested preserved transparent edit remains unsuccessful after two repairs; the public failed status is accurate. This does not identify a helper-code defect.

### F4 — MINOR / P1 native-output limitation: SUNROOM subtitle fails the intended small-size review

Evidence: `docs/qa/color-workflow/native-cases.md:9` and `docs/qa/color-workflow/chrome-live.md:17`. Existing Chrome evidence records exact SUNROOM/BAKERY spelling but an overly small BAKERY subtitle at 128 px. The saved small_size_ok=false and absent delivery accurately preserve this limitation. This reviewer read the existing evidence and did not perform a new SUNROOM browser review.

**Explicit blockers:** F1 and F2 prevent the required native release gate; F3 remains an unresolved requested native edit. No newly reproduced source-CLI defect blocks committing code/docs as a development preview. The plan's `T8`, `VERIFY` and `T9` must remain incomplete until their actual conditions are satisfied; no public tag/release is approved by this report.

## Independent visual observations and evidence scope

I opened the actual public PNGs with view_image: GROVE a-v1, warm GROVE a-v4, NORTHLINE a-v1 and white 밤결 white-v3. GROVE has the expected leaf/mountain/river symbol with GROVE / SUPPLY at the right; the warm repair keeps this recognizable composition but includes a painted checkerboard. NORTHLINE has exact uppercase lettering below a centered two-part navigation symbol, clear central gap and intended opaque silver background. These observations support the selected original's identity and requested arrangement, not an exact installed-font claim.

The raw white PNG tool preview shows much more apparent sparse edge detail than the saved Chrome composited view. I independently opened `chrome/public-white-small.jpg`, which shows readable white 밤결 and a clean moon/book silhouette at the displayed size on dark gray, without an obvious checker rectangle. I also opened `chrome/grove-large-light.jpg` and `chrome/northline-small-light.jpg`. The existing alpha diagnostic's many alpha-1–5 samples provides a plausible explanation for the preview difference; it is not a threshold waiver or proof of a specific renderer defect. The final finding is the reproduced quantitative indeterminate result. I did not treat raw tool preview rendering as proof of visible damage in Chrome.

The dedicated worker's complete `chrome-live.md` records actual light/dark/transparency and size/reset interactions, sampled links, three completed downloads with matching hashes, final white observations and 46 screenshots. I read that evidence and verified the current supplemental white report removed the earlier unsupported visible-speckle wording. Browser execution belongs to that worker: I did not control Chrome, open a concurrent browser session or claim to repeat its interactions.

## Documentation, installation and remaining coverage limits

The current READMEs explicitly identify 0.4.0 as unreleased development source and 0.3.1 as the published release. Their constraints, migration, sampled-color, font-appearance and original-PNG boundaries match the exercised CLI surface. The structured lockup survives actual prompt/import/export plumbing; the visual samples distinguish horizontal, stacked and Hangul arrangements. This review did not revalidate external font repositories, font binaries, licenses or every research citation.

Installation evidence documents successful personal-cache validation and 15 actual installed-helper CLI calls using `0.4.0+codex.20260912153655`, with the public manifest remaining 0.4.0. It explicitly identifies PEP 723 execution, warmed caches, no fresh-thread skill invocation and an unrelated astral-codex marketplace error on plugin list. I read this record but did not install, alter host settings or independently repeat installed-cache execution.

The existing integrated **299-test/static/format/locked-check results were reviewed as prior implementation evidence and were not rerun**. This review's primary evidence is source CLI execution, existing-original reanalysis/export, original/source hashes and independent image inspection. No new native image calls, programmatic raster edits, font installation, paid service/MCP calls, commit, push or release occurred.

Not independently exercised here: cold-cache or network-isolated startup, missing-engine/profile corruption, maximum file/pixel bounds, disk-full/save-failure injection, adversarial concurrent writers, an interactive relocated-gallery browser session, every public link click or screenshot viewport, and Windows execution. These limits are not presented as passing tests. The gallery's relocation was checked by resolving its real relative resources and original-byte hashes; the broader public-gallery HTTP portability and Chrome behavior remain supported by the designated workers' recorded evidence.

The review changed only this Markdown report and temporary `output/review-qa/` records. All original/native and public/source files were read-only.
