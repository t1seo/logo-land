# Independent context and provenance review

**PASS. No blocking findings within this review's requirements, history, attribution and provenance scope.** Confidence is high for exact file/request/install bindings and current publication status; this is not a new native inference run, a human design certification, or a measured aesthetic comparison.

Reviewed on 15 September 2026 KST against `f7dd3268313d2422b87efea63eef8257b0e651b9`. Orca task `task_6e1b3a7d8e45`, dispatch `ctx_64dfb852f7e9`. Only this report and `review-context/` were authored. The four protected unrelated drafts, source, real workflow, artwork, installed profiles and release state were preserved. No branch change, nested agent, commit, push, release or external message was made.

## Findings and requirements

There are no blocking defects to route for a fix. Two informational distinctions are important when interpreting the saved evidence:

1. **Informational, installation history:** `output/hermes-demo/installed-payload.json` is the original 00:58 installation record with 55 entries. The current refreshed 0.8.0 managed marker has **59 entries: 58 source payload files and one generated local settings file**. All 58 source files match the installed bytes and hashes; the settings entry matches its hash and exact workspace/helper paths. The later `installed-080-binding.json` agrees. The old record remains historical evidence, not the current installation manifest. [Current bindings](review-context/installed-bindings.tsv), [first comparison failure](review-context/binding-first-failure.txt).
2. **Informational, preservation precision:** raw pre-recovery job JSON differs from final j1–j7 only because the new optional field `retry_of: null` was serialized. Every pre-existing field, including the original error, reports and request identity, is unchanged; equality after the declared `Job.retry_of = None` default passes. Do not call those raw JSON objects byte-identical. The actual original PNG bytes are identical. [Exact differences](review-context/history-first-comparison.json), [normalized result](review-context/history-normalized.json).

| Requirement | Result and evidence |
| --- | --- |
| Real Hermes direction beyond a Codex skill | PASS. Native host uses separate structured strategy/direction calls and separate image-input design/production calls; `image_generate` owns original creation/editing. Core state and helper delivery are separate. Source read included host, request, installer, production, recovery and neighboring model/fixture modules, not only tracked diffs. |
| Concrete brief, distinct directions and critique | PASS. OFFCUT's saved brief and three directions match the curated fields. Ten persisted critiques have unique call IDs, the actual candidate/parent hashes and 192px view width; all match their successful canonical jobs. Provider/model attribution is `openai-codex / gpt-5.6-sol` for planning and critiques. [Bindings](review-context/history-critique-bindings.json). |
| Native originals, exact-parent revisions, choice and delivery | PASS. Exactly three initial image jobs plus two edit jobs; image receipts match saved prompts and `openai-codex / gpt-image-2-medium`. Edits report one input image each. Source resolves the reserved parent to its exact canonical image path; saved lineage is c1 → e1 → e2. Both e1 preservation reports remain `needs_revision`; both fresh e2 reports pass all five criteria. [Native receipts](review-context/native-image-receipts.json), [public/canonical comparison](review-context/public-canonical.json). |
| Seven real request-to-tool bindings | PASS. Inspected only session IDs and allowlisted `messages[].tool_calls[].function` action metadata. Each session contains one expected deferred `tool_call` to `logopia_start` or `logopia_action`; its parsed arguments match its saved request after known schema defaults. No system, reasoning or conversational content was copied into artifacts. [Seven bindings](review-context/request-bindings.json), [exact jq](review-context/binding-query.txt). |
| Native actual, curated sample and fake fixtures remain distinct | PASS. Canonical workflow is r47/delivered/e2. `example.json` explicitly identifies a frozen curated public example and coordinator-owned choice; its source SHA, brief, direction fields, feedback, model attribution and review fields match canonical records. Deterministic test hosts label themselves `fixture/stub`; their generated fixture PNGs are not native demo evidence. The earlier ring is a diagnostic, not OFFCUT. |
| English default, Korean counterpart, direct white samples | PASS. Both root READMEs show c1/e2 as direct image/href pairs before the existing showcase. All 16 previous direct hrefs remain in the same order and all 16 originals equal the base commit. Existing c1/e2 were opened visually and present white canvases; no repainting or image processing occurred. Research remains outside README exposition, with no research diagram added. [HTTP hashes](review-context/http-body.sha256), [links](review-context/readme-link-checks.txt), [old originals](review-context/old-originals.sha256). |
| Explicit IP-as-logo reference | PASS. Both READMEs, both Hermes guides and the native director reference identify s1dashu's upstream. The full pinned skill was read; its character geometry, semantic colors, corner placement and independent candidate principles support the stated adaptation. The bundled MIT notice is byte-identical to the pinned upstream license. [Source audit](review-context/primary-source-audit.md). |
| Preserve first timeout and failure rather than imply success | PASS. Native-run records the first 420-second native executor timeout separately from the 1,800-second launcher. Canonical j7 retains its original, historically generic error and is superseded by successful critique j8 through `retry_of: j7`. Initial planning, directions, image identities and the first two critique pairs are unchanged. The prior continuation receipt reports r23 → r27 and zero new images; this reviewer did not repeat inference. [Native execution](native-run.md), [history checks](review-context/history-critique-bindings.json). |
| Named-profile installation and defaults | PASS. Source explicitly targets named profile configuration; current named limits are 1,800 seconds each. The default configuration digest still equals its pre-install digest `2bd35fc1d58229630b5a625d7cc7c48ca50bfbd9cfd6fc23e5af3a29798635bd`. Local Hermes is Python 3.11.16; locked helper interpreter is Python 3.12.12. [Runtime metadata](review-context/runtime-metadata.txt). |
| Truthful release state | PASS. Source/plugin/helper are 0.8.0, while GitHub's latest published release is v0.7.0. v0.4.0 remains an unpublished historical draft. Remote main is the reviewed base; no v0.8.0 tag was returned. README and release docs explicitly call 0.8.0 unreleased, and prepared tag links are labeled publication-dependent. Root-owned T6 publication is pending, not an implementation defect. [Latest release](review-context/github-latest-release.json), [all release metadata](review-context/github-releases.json), [remote refs](review-context/remote-refs.txt). |

## Prior decisions and source support

The repository's [merged PR #1](https://github.com/t1seo/logopia/pull/1) explicitly addressed repeated sample navigation by showing originals in both READMEs and added cross-project comparison with exact PNG/prompt provenance. Commits `49e9ae7` and `fa6c142` carry that direct-access and white-showcase history. Commit `fd1d89c` records English-default presentation; `6d946e6` records bilingual simplification and IP work. The earlier failed v0.4.0 draft is preserved in committed release history rather than retroactively approved. [Git history](review-context/git-history.txt), [README blame](review-context/readme-blame.txt), [PR record](review-context/github-prs.json).

Read-only GitHub issue listing returned no issues; PR listing returned one merged PR. The public About description remains English and describes the already published Codex capabilities. It does not announce an unshipped Hermes release. No Slack, Notion or Mobbin evidence was available or used; those sources are explicitly skipped, not invented.

The [primary-source audit](review-context/primary-source-audit.md) checks Mozilla, Figma critique/version history, Adobe, COLLINS, GOV.UK, Microsoft HAX, Hermes and pinned IP guidance. Each product decision is labeled an inference from its actual supporting content. No source establishes AI superiority, legal uniqueness or a human review. Two bounded initial curl fetches returned 200, but acceptance additionally checked API semantics and exact license bytes; the third pinned skill fetch also returned 200 and its full content was read.

The local Hermes checkout SHA is exactly `d3e2ace1dde9f1d279f99c9ebc6bce2e761b025d`. The research document correctly labels it a local verification identifier, not a verified public permalink. Current online Hermes documentation has newer features, so this review did not infer installed support from documentation alone.

## G1–G7 contract alignment

| Contract | Context/provenance observation |
| --- | --- |
| G1 | Documented Python 3.11 native / 3.12 helper split matches actual interpreters and source subprocess boundary. Dependency ranges and locked helper argv are explicit. Earlier doctor/typecheck evidence is reused, not re-executed here. |
| G2 | Exact request identity and finite logical budgets are recorded; the real demo used 3 initial + 2 edit jobs. Small owned-process deadline and interruption tests passed in this review. |
| G3 | Public delivery equals canonical PNG/manifest/guide/ZIP; ZIP has exactly three expected members, each byte-identical. Earlier idempotent no-inference delivery is attributed to the coordinator. |
| G4 | All ten final reports bind exact image/parent hashes and separate call IDs. The public review text matches canonical fields. These are model observations, not numerical quality certification. |
| G5 | Native docs and data say advisory colors; revision scope preserves text/colors/background. The guide routes strict palettes and other presets to the existing workflow. |
| G6 | Request schema, copy-back feedback hash/revision identity and raw request data rules were read. Malformed and stale request tests passed with zero fake Hermes invocations. |
| G7 | Actual 420-second first failure remains documented; current named-profile limits are 1,800 seconds. Explicit critique-only recovery has an exact supersession link, preserves prior data, and cannot authorize another image. |

## Direct verification and all nine adversarial classes

Before probes, [214 source/public/canonical/protected hash records](review-context/before.sha256) passed on unchanged files. The same records passed after probes. The baseline is broader than `git diff`: it includes untracked Hermes source/tests, both guides, public sample files and the exact private receipt files by hash. [After check](review-context/after-check.txt).

One justified, bounded run of existing defensive tests passed **13/13 in 11.33 seconds**, exit 0, with fake transports and isolated scratch homes. No production test was added, deleted, weakened or rerun to obtain green. The full **907-test** run, Ruff, basedpyright, 458-file format check, doctor and full Chrome evidence are **reused coordinator evidence from [integration.md](integration.md)**, not this review's executions. No new Python was authored, so new-code Ruff/typechecks are N/A.

| Adversarial class | Result | Concrete observable |
| --- | --- | --- |
| 1. Malformed input | PASS, new execution | Five CLI cases (broken JSON, array, string instruction, empty object, oversized file) return an error before any fake Hermes invocation. |
| 2. Instruction-like brief/feedback as inert data | PASS, new execution plus source inspection | Existing literal-note fixture preserves exact quoted query data, supplies only a query-file path in argv, and creates no marker file. Both planning/critique and feedback prompts explicitly treat project text as data. This tests local handling, not universal model injection resistance. |
| 3. Cancel/resume | PASS, new execution plus attributed native record | Critique recovery fixture retains original image hash and error, makes one explicit continuation, and records an empty image-call file. Existing native r23 → r27 continuation is separately attributed. |
| 4. Stale state | PASS, new execution | Revision 4 against saved revision 5 returns `stale_revision`; fake Hermes invocation file is absent. Raw-vs-default-normalized history differences are preserved separately. |
| 5. Dirty worktree/foreign files | PASS, new execution and actual hash checks | Existing foreign output sentinel and directory contents are unchanged when output reuse is rejected. The real shared dirty tree and four unrelated drafts retain every pinned byte. |
| 6. Hung/long commands | PASS, new execution | A real owned sleeping child settles after a 1-second deadline with a nonzero exit. All network calls have finite limits; HTTP server had a 180-second safety limit and was intentionally reaped earlier. |
| 7. Flaky tests | N/A for recovery; no flake observed | The scoped suite passed on its first run, with no automatic retry. The pre-existing 907 result is not a reliability distribution. Reviewer harness failures are retained below rather than hidden; no test was relaxed. |
| 8. Misleading success | PASS, new execution and byte checks | Fake successful prose plus exit 0 and unfinished canonical state returns `outcome_unknown`, without inventing a deadline. HTTP 200 required exact body equality; ZIP required exact members and hashes. |
| 9. Repeated interruptions | PASS, new execution | A second interruption during shutdown still reaps the owned child. A second unknown critique exhausts the remaining budget; three repeated interrupt/reconcile/produce attempts create no further model/image work. |

[Exact commands and limits](review-context/commands.txt), [13-test output](review-context/defensive-tests.txt), [binding command](review-context/binding-command.txt), [binding results](review-context/binding-run.txt).

The required manual HTTP channel was executed exactly:

```sh
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8817/README.md
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8817/README.ko.md
```

Both returned HTTP/1.0 200 and exit 0. Body sizes were 12,538 and 13,918 bytes. English SHA-256 is `077c932532866e4dba4fe247bdfaa0dee4f765a129dbc20c9f02bab3e616ca86`; Korean is `d05d87e663dfad1c848349639902e5eca91968d9a9201d8c4b9981428d5886be`. After removing only HTTP headers, `cmp` matched each exact source body. [English headers](review-context/http-english-headers.txt), [Korean headers](review-context/http-korean-headers.txt).

Five public originals match canonical SHA-256 records. The delivered ZIP SHA-256 is `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04`; its only members are `logo.png`, `manifest.json` and `brand-guide.md`. Each member matches both public and canonical files. [Originals](review-context/original-bindings.tsv), [delivery hashes](review-context/delivery.sha256), [ZIP checks](review-context/zip-bindings.txt).

## Preserved first failures

These are reviewer harness/inspection issues, not product failures, and remain visible:

- Initial discovery referenced nonexistent `src/`; `rg` emitted an error although the enclosing pipeline exited 0. The correct `skills/` helper tree was added before behavioral probes, producing the 214-record passing pin.
- First installation comparison used the historical 55-entry manifest against the current 59-entry install and exited 1. The original command/output remain; the corrected verifier checks each current source/settings hash. No old evidence was overwritten.
- A metadata projection assumed an array where `review-source-binding.files` is an object; jq rejected it. A nonexistent historical-directory glob also failed. Neither was used to infer product support.
- The first raw job comparison returned false because of `retry_of: null`; [raw result](review-context/history-critique-bindings.json) and [field-level differences](review-context/history-first-comparison.json) remain alongside exact default-normalized equality.
- Automatic command review rejected the initial cleanup command's force option before shell execution. The safer, non-force removal succeeded after checking owned root identity and absent processes. No approval request or workaround bypass was used.

The product's actual first native timeout and e1 preservation failure remain intact in [native-run.md](native-run.md) and public sample data. They are not relabeled as passing.

## Cleanup receipt and completion

Resource TODOs were written before the owned directory, scripts, downloads, server and fixture run started; the original ledger is retained in [review-ledger.txt](review-context/review-ledger.txt). Cleanup completed at `2026-09-14T17:00:28Z`:

- HTTP PID **13482**, execution session **91437**, was checked against its exact command, sent SIGTERM, and reaped with expected exit **143**. PID is absent; port **8817** has no listener.
- The test process and all read-only GitHub command sessions settled. The owned-process scan returned zero matches after excluding the inspecting process.
- `/tmp/logopia-review-context-080` is absent, including both scripts, fixture basetemp, temporary helper roots, downloaded pages/license/skill, HTTP bodies and isolated cache.
- No browser profile/context, tmux session, installed package, live inference, profile/auth write or nested agent was created. Existing user Chrome processes were untouched.
- Only this report and its sanitized durable artifacts remain. No private exports, system content, reasoning or credential data were published. `git diff --check` passed; all 214 protected file hashes passed.

[Machine-readable cleanup receipt](review-context/cleanup.json), [owned process check](review-context/owned-process-check.txt), [diff check](review-context/diff-check.txt).

Completed plan: PIN/baseline; requirements/history/provenance; HTTP and bounded defensive scenarios; verdict and cleanup. No review work remains. Root retains ownership of T6 publication and the other independent review roles.
