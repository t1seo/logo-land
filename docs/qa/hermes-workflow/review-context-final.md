# Final context and provenance delta review

**PASS for the final context/provenance and installed-source delta. No blocking finding in this review's scope.** The actual current install has **61 managed records: 60 repository payload files plus one generated settings file**. Every record matches installed bytes; all source payload bytes, exact settings paths, immutable native/public history and the coordinator's final receipt independently agree. This is a scope verdict, not a claim that root's separate full integration suite or T6 publication has completed.

The sole named review dependency was satisfied by coordinator `FINAL_BINDING_READY`, message `msg_a3cd813f34b5` at `2026-09-14T18:01:32Z`, after source freeze and real reinstall. [Signal](review-context-final/final-binding-ready.json). No comparison of moving process-source hashes was treated as a defect.

Owner: Orca run `run_ad4a666ccb76`, task `task_2e671ebbef64`, dispatch `ctx_0e76a89d9bb1`.

## Review plan

1. COMPLETE: read the prior context review and delta evidence, then pin immutable native/public/protected records before probes. 208 unchanged historical records and 259 current immutable records are pinned; all seven saved request hashes match.
2. COMPLETE: exact bounded README/ZIP HTTP scenario passed with exact bodies; server PID 98366 was terminated and reaped, exit 143, port free. All scratch was removed and both `/tmp` and `/private/tmp` aliases are absent. `PARTIAL_READY` sent after cleanup.
3. COMPLETE: after `FINAL_BINDING_READY`, independently compared all 61 managed records, exact settings, complete source/installed inventories and every final coordinator binding; reviewed final integrated race source/regression/manual/cleanup evidence.
4. COMPLETE: nine classes reconciled, final preservation/cleanup recheck passed, scope PASS issued; exactly one truthful `worker_done` is the terminal completion action.

The explicit task supplies a complete review plan and prohibits nested agents, production edits, new inference, profile writes and publication. Planning/programming skill references were consulted; task ownership takes precedence over skill suggestions to delegate or create unrelated plan files. No `update_plan` tool is exposed, so this report tracks the four verifiable steps.

## Resource register (written before creation)

- Durable `review-context-final/` directory: retain sanitized command, hash, HTTP-header, source comparison and cleanup receipts only.
- Exact scratch root `/tmp/logopia-review-context-final-080`: verify absent before creation; remove only this root after HTTP checks, before the authorized dependency wait.
- Scratch scripts: `pin.sh`, `immutable.sh`, `http.sh`; retain exact text under the durable directory before execution, remove scratch copies with root. Final comparison may run from its durable `.sh` receipt without recreating scratch.
- HTTP downloaded temporary files: `readme.response`, `zip.response`, `readme.body`, `zip.body` beneath the scratch root. Headers and hashes retained; original bodies removed with root.
- Loopback HTTP server: port **8817**, bound only to `127.0.0.1`; confirm no listener before starting. Use a **120-second** alarm carried into the server process. Register exact child PID in `server.pid` and durable `server-pid.txt` immediately after spawn and before requests. Parent script owns kill/wait and verifies the PID absent.
- Curl calls: exact requested `-i --connect-timeout 2 --max-time 15` arguments; no retry. Keep stdout response and stderr separate, split headers/body without altering bytes, and require 200 plus source equality.
- Bounded shell verifier commands: **60-second** alarm wrappers, no external inference/network other than the two loopback requests. No persistent environment overrides are planned. If an override is required, register its name/value/purpose here before use.
- No browser, tmux, new environment/package installation, production test changes, private-session copies or profile/auth writes are planned.
- Final installed/source verifier `review-context-final/installed-final.sh.txt`: durable shell receipt, executed with a 60-second alarm only after `FINAL_BINDING_READY`; creates no new scratch root, service or environment override. It may read only the named plugin's managed marker/payload/settings, final binding, repository files and the explicitly allowed default-config digest.
- Final coordinator-receipt verifier `review-context-final/root-binding.sh.txt`: same 60-second bound and allowlisted reads; compares the coordinator JSON with independently verified current marker/canonical/delivery maps, then verifies the six frozen process-source hashes. No scratch or environment override.

## Completed immutable and public verification

All new executions below belong to this final context reviewer. The baseline is `f7dd3268313d2422b87efea63eef8257b0e651b9`; the worktree is shared and dirty. Six previously pinned paths were deliberately excluded from historical equality because their changes are authorized: launcher/helper process modules, installer, CONTRACT and the two Hermes guides. The new process support modules and their regressions await the final source freeze; a moving source hash is not a defect.

| Binding | New result |
| --- | --- |
| Historical preservation | **208/208** unchanged entries from the earlier 214-entry pin pass. The six authorized differences are not compared as immutable. |
| Current immutable pin | **259/259** records pass before and after local probes, including canonical state, public samples, requests, historical binding artifacts, unchanged source/tests/helper and protected files. [Pin](review-context-final/immutable-before.sha256), [after check](review-context-final/immutable-after-local-check.txt). |
| Native canonical | Exact `cmp` against `output/hermes-demo/final-workflow.json` passes: **r47 / delivered / e2 / five candidates**, SHA-256 `16eea6dc8c32e979c432fbdffee137d76cb68a230aad9e5b65cc740d59e26e04`. |
| Actual originals | All five canonical PNGs equal their public originals and recorded hashes. [Five bindings](review-context-final/original-bindings.tsv). Original pixels were not modified or generated by this reviewer. |
| Requests and provenance | All **seven** saved request hashes match the original independent binding records; the prior `session-bindings.json` hash also passes the historical pin. No private session export, system or reasoning content was read or copied. The prior tool/session-envelope inspection is explicitly reused. [Request checks](review-context-final/request-bindings-check.txt). |
| Delivery | All **four** public delivery files equal canonical files. ZIP has exactly `logo.png`, `manifest.json`, `brand-guide.md`; each member was streamed through `cmp` against both locations. [Delivery hashes](review-context-final/delivery.sha256), [ZIP member checks](review-context-final/zip-member-checks.tsv). |
| Preserved history | Seven old jobs match after adding only their declared `retry_of:null` default; raw equality is false. The original j7 error remains and j8 explicitly supersedes it. Exactly **three generate + two edit** jobs, c1 → e1 → e2, both e1 preservation failures and both fully passing e2 reports remain. [Normalized history](review-context-final/normalized-history.json). |
| Normalized-job wording | `native-run.md` explicitly distinguishes unchanged PNG bytes and prior fields from changed raw job serialization. Both continuation paragraphs now describe default-normalized equality. [Exact wording](review-context-final/normalized-wording.txt). |
| Protected content | All **four** named `.omo/drafts` match the prior pin. All **24** old showcase PNG files, including the **16** direct README originals and eight retained variants, match prior hashes. Both READMEs retain their exact 16 direct hrefs in the same order as the base commit. |
| Documentation/credit | Both READMEs retain direct c1/e2 image/href pairs before the old showcase, English-default navigation, explicit s1dashu IP-as-logo credit and source 0.8.0/public 0.7.0 distinction. Existing white artwork inspection is attributed to the earlier context review; unchanged hashes bind those observations. Both Hermes guides explain bounded local settlement and preserved installer recovery copies without treating model critiques as human certification. |
| Default profile | The default config digest equals `output/hermes-demo/default-config-before.sha256`; config contents and credentials are not displayed. No profile write occurred. |

The earlier review's history and primary-source audit are reused, rather than repeated: direct originals and English-default presentation derive from the recorded repository history; public guidance supports the stated adaptations, not legal uniqueness or measured AI superiority. Source attribution and bundled IP license bytes remain pinned. Root retains T6; this delta review does not recheck remote publication or assert a new release.

## Exact manual HTTP channel

The loopback server used port **8817**, exact PID **98366**, an inherited **120-second** alarm and `--bind 127.0.0.1`. `lsof` confirmed that exact listener before the first call. Both commands were executed once with no curl retry:

```sh
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8817/README.md
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8817/docs/hermes-demo/delivery/logo-package.zip
```

Both returned **HTTP/1.0 200 OK**, curl exit **0**, and their bodies exactly matched source via `cmp`. The downloaded ZIP additionally matched canonical delivery. Only the first CRLF header block was removed; no body decoding or transformation occurred. README SHA-256 is `077c932532866e4dba4fe247bdfaa0dee4f765a129dbc20c9f02bab3e616ca86`; ZIP SHA-256 is `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04`.

[Exact script](review-context-final/http.sh.txt), [README headers](review-context-final/readme-headers.txt), [ZIP headers](review-context-final/zip-headers.txt), [body hashes](review-context-final/http-body.sha256), [exit/cleanup receipt](review-context-final/http-cleanup.txt). Pin/immutable/HTTP shell commands each had an outer **60-second** alarm; none reached it. `pin.sh` exited 0, corrected `immutable.sh` exited 0, `http.sh` exited 0. The server was intentionally terminated/reaped with exit **143**, and port 8817 was free before scratch removal.

## Attributed process and installer executions

The original independent context suite's **13 passed in 11.33s** is prior reviewer evidence, not a new run. Its malformed input, literal prompt data, explicit critique recovery, stale-state, misleading-success and logical retry-budget fixtures retain their pinned source bytes. [Original command and limits](review-context/commands.txt), [13 results](review-context/defensive-tests.txt).

The code review's four original product failures remain actual failures: (1) interrupted second-rename publication deleted the previous plugin; (2) launcher returned while its descendant was alive; (3) caller interruption left the helper alive with ResourceWarning; (4) a nested foreign marker was deleted by update. These were not harness errors. The code reviewer independently reran the unchanged assertions after fixes: **3 passed in 2.65s** for descendant/helper/marker and **2 passed in 0.03s** for I/O/interruption rollback. Recorded children were absent before the success assertions and warnings were zero. [Three final probes](review-code/defensive-final-tests.txt), [rollback final probes](review-code/install-rollback-final-tests.txt).

The subsequent actual-helper separate-group defect also remains recorded as a first product failure; the code reviewer's unchanged final repro passed **1 in 2.33s**, with helper PID 71528 absent at receipt. [Nested helper result](review-code/nested-helper-final-tests.txt). First-rename installer recovery was independently reprobed by goal and security reviewers: **2 passed in 0.10s** each, exact prior bytes retained. [Goal result](fix-installer-boundary/goal-green.txt), [security result](fix-installer-boundary/security-green.txt). The current installer source was read: both rename boundaries are protected; unresolved previous backups survive temporary cleanup and the exception identifies their retained path.

The integrated **954 passed / 2 failed in 309.89s** remains the first final-suite result. Helper PID 78509 first exceeded the settlement bound, then its delayed destructor warning failed a later color test; the color assertion itself was not the failure. This reviewer did not run redundant broad pytest or any model calls.

The final process owner proved an acquisition-boundary race with finite real-SIGINT probes on Python **3.11.16** and **3.12.12**: controls settled; interrupted probes retained a locked Popen poll lock and zombie until explicit fixture cleanup. The actual `run_cli` regression was **1 failed / 1 passed** before production changes. After the fix, both acquisition cases pass and the requested five-file scope is **39 passed in 29.43s**. All original exception-identity, PID/group absence, warning and elapsed assertions remain, with one additional acquisition parameter. The historical suite trace does not reveal its exact interrupt instruction; the deterministic probe proves a matching mechanism, not a retrospective instruction-level capture. [RED](fix-process-integration/red-acquisition.txt), [GREEN](fix-process-integration/green-acquisition-first.txt), [scoped result](fix-process-integration/green-scoped.txt).

Read all four final process modules and both frozen regression files. The shared guard defers a callable SIGINT handler's original KeyboardInterrupt only through bounded Popen operations, restores the handler and retains exception identity. Main-thread waits/communicate use at most **0.1-second** slices under the original absolute deadline; poll and the existing **0.25-second** numeric-query reap are protected. Separate-thread/non-callable policies remain unchanged; no private Popen lock mutation, warning suppression or expanded grace/force budgets appears in production. The launcher owns a fresh SID, helper a separate PGID within that SID, and numeric session/group membership is rechecked before signalling. No process-name/argv/environment scan or remote cancellation claim was added. [Frozen diff](fix-process-integration/source-frozen.diff), [six-file hash check](review-context-final/process-frozen-check.txt).

The owner's actual tmux manual receipt records **two Ctrl-C events**, original exception identity, helper absent/reaped within **0.575s**, later exact stdout both directly and from a thread, zero ResourceWarnings and `manual_exit=0`. Its cleanup receipt records **43 PIDs / 31 groups absent**, owned session/scratch removed, and zero unowned signals. These are **process-owner executions**, not executions by this context reviewer. Native/test type checks report zero diagnostics, Ruff passes, six files are formatted and parse with real Python 3.11.16. [Manual](fix-process-integration/manual-joined.txt), [cleanup](fix-process-integration/cleanup.txt), [native types](fix-process-integration/types-native-final.txt).

The completed `fix-process-integration.md` was read before this verdict: all five steps are complete and its cleanup matches the receipts above. Its early progress labels were resolved without further source changes. The final independent code reviewer also ran **6 original/targeted cases, all passed in 5.45s**, exit 0: unchanged descendant/helper/nested-marker/nested-helper probes plus original and acquisition-injected repeated interruption. Original exception and PID/group/warning assertions remain; recorded helpers were absent at result time. These are executions by reviewer dispatch `ctx_c84701fbe9de`, not this reviewer. [Six results](review-code/settled-tests.txt), [exact command and deadline receipt](review-code/settled-receipt.json). Root's separate full integration gate remains outside this scope verdict.

## Final installed-source comparison and G1–G7

New independent verification executed after the named signal:

```sh
perl -e 'alarm 60; exec @ARGV or die $!' /bin/bash docs/qa/hermes-workflow/review-context-final/installed-final.sh.txt
perl -e 'alarm 60; exec @ARGV or die $!' /bin/bash docs/qa/hermes-workflow/review-context-final/root-binding.sh.txt
```

Both exited **0** on their first execution. The verifier checked each current marker record against installed bytes, compared each of the **60** payload files with repository source by SHA-256 and `cmp`, separately parsed the **one** settings file for exactly the schema/workspace/helper keys and exact workspace/helper repository paths, and independently enumerated both inventories. No payload file was missing or extra. Both `process_group.py` and `process_scope.py` are included; launcher, helper, installer and both support-module hashes all match final source. [61 individual bindings](review-context-final/installed-bindings.tsv), [summary](review-context-final/installed-summary.json).

The coordinator's final JSON was then checked against those independently observed records, actual canonical SHA/state, all five originals, all four delivery hashes and the three ZIP members. Every comparison is true. Historical 55-record marker equality is **false** and historical 59-record count equality is **false**, as expected; neither is presented as today's install. The final pin contains **274 repository/artifact records** and **62 installed records including the marker itself**, and both pins pass their after-comparison check. [Coordinator comparison](review-context-final/coordinator-binding-comparison.json), [repository pin](review-context-final/final-source.sha256), [installed pin](review-context-final/final-installed.sha256).

| Contract | Final delta assessment |
| --- | --- |
| G1 | Python 3.11 native / locked Python 3.12 helper split remains; frozen source, dependency declarations and exact helper argv match the attributed native parse/type evidence. |
| G2 | Final process ownership, finite grace/force/query bounds and repeated-interrupt settlement match source and owner evidence. Logical invocation budgets/unknown-outcome semantics are unchanged and pinned. |
| G3 | Exact native/public/ZIP delivery equality passes. Installer restoration protects both publication renames and retains an unresolved previous backup; recovery is not misrepresented as atomic or successful. |
| G4 | Actual image/parent/view bindings, distinct critique calls and conservative approval remain pinned. e1 failure and fresh e2 success are preserved; no human certification or new aesthetic inference is claimed. |
| G5 | Both guides retain advisory color policy and revision scope; strict palette/other preset routing remains explicit. |
| G6 | Unchanged strict request/feedback sources and seven exact request hashes preserve revision/candidate identity and inert-data handling. No private reasoning or credentials were accessed. |
| G7 | First native 420-second timeout, original j7 error, explicit critique-only continuation, and optional default normalization remain truthful. Named limits/doctor are coordinator executions; default config hash is independently unchanged. |

## Nine adversarial classes

| Class | Evidence and limit |
| --- | --- |
| 1. Malformed input | Attributed original context execution: five malformed request cases fail before any fake Hermes invocation. Those request-model files are unchanged. No new execution applies because this is a provenance/install delta, not a request parser change. |
| 2. Instruction-like data | Attributed literal-note fixture preserves quoted input, passes only a query-file path in argv and creates no marker. No new live-model injection probe applies; private prompt/session content is not published. |
| 3. Cancel/resume | PASS: preserved native jobs prove explicit critique-only recovery with no new image/planning call, original error retained and declared default normalization. Final installer/process fixture evidence is attributed above and bound to final source. |
| 4. Stale state | PASS: new comparison distinguishes historical **55** and **59** records from the actual current **61**, with both false-equality results recorded. Original stale-revision no-call fixture is attributed. |
| 5. Dirty worktree | New exact hashes protect all four unrelated drafts, old originals, immutable canonical/public content and unchanged source/tests. Authorized moving process files are deferred until source freeze. No foreign file is edited. |
| 6. Long commands | New HTTP calls have 2-second connect / 15-second total limits; server has 120-second alarm, wrapper 60 seconds and exact PID cleanup. Original fixed local-process deadline probes are attributed; no external or provider hang is created. |
| 7. Flake/first failures | No automatic retry. This review retains the first wrong-kind harness failure; prior discovery/schema/default-normalization/cleanup-review failures remain distinct from actual native, design, installer and process failures. No stochastic inference repeatability claim applies. |
| 8. Misleading success | PASS: new HTTP success requires exact bytes, package member equality, immutable history and all **61** actual current install/source records, not response 200 or doctor prose alone. Final coordinator JSON independently matches all observations. |
| 9. Repeated interruptions | PASS within this delta: prior context budget fixtures, independent fixed process/installer probes and the final source-bound **39-test** process scope plus two-Ctrl-C manual result are attributed executions. Original integrated failure remains. No new canonical interruption or broad rerun was performed; root's full integration gate is separate. |

## Retained inspection issues

- Initial applicable-rule discovery named three nonexistent ancestor `AGENTS.md` paths; `rg` exited 2. The provided Korean politeness instruction remains applicable; no repository-specific file was found. This is a read-only discovery issue, not a product failure.
- First immutable-history harness selected nonexistent job kind `image` rather than the actual `generate`, reporting zero initial image jobs and exit 1. Canonical records show three successful `generate` jobs. The original script, output and failed JSON are retained under `immutable-first*` and `normalized-history-first.json`; only this reviewer-owned selector was corrected, with no product change or weakened check.
- The earlier context review's absent `src/` discovery, 55-vs-59 first comparison, object-vs-array jq projection, missing historical glob, raw/default-normalized job comparison, and rejected force-cleanup command remain its disclosed harness/inspection issues. They were not rerun, erased or relabeled as product failures. The four actual original code-review failures and subsequent process/installer defects remain separately attributed above.

## Completion

Immutable/HTTP work and final installed-source comparison are complete. The **259** immutable hashes, **274** final repository/artifact hashes and **62** installed hashes (61 payload/settings records plus marker) pass. `git diff --check` passes. No Python/TypeScript/Rust/Go production or test code was authored, so new-code LSP/type/build/test work is N/A; shell verification was executed through its actual command surface. Existing/final product test and static results are explicitly attributed rather than duplicated.

The owned HTTP server PID **98366** was reaped with exit **143** and is absent; port **8817** is free. `/tmp/logopia-review-context-final-080` and its `/private/tmp` alias are absent, including all three scripts, responses, bodies and PID receipt. No browser/tmux, package/environment installation, environment override, inference, profile/auth write, source/README/version edit, nested agent, commit, push or publication was performed. Only this report and its sanitized `review-context-final/` artifacts remain. [HTTP cleanup](review-context-final/http-cleanup.txt), [scratch cleanup](review-context-final/cleanup-partial.json), [final checks](review-context-final/completion-verification.txt), [final receipt](review-context-final/cleanup-final.json), [command ledger](review-context-final/commands.txt).

No review-scope blocker remains. Root retains the separate full integration/reviewer settlement and T6 publication gates; their completion is not inferred from this PASS.
