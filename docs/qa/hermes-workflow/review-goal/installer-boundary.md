# First-rename interruption investigation

Status: **PASS at code-ready for the exact independent regression; original RED retained.** This is a review-only follow-up to the accepted two-line installer repair, not a production fix. Coordinator was informed before the probe in `msg_e38f7a712021`, received the exact observed failure, and received independent GREEN in `msg_c45e281bfc09`. Overall final acceptance still waits on root `FIXES_READY`.

## Environment and scope

Existing locked repository Python 3.12/Pydantic environment; current installer read directly from `integrations/hermes/logopia_studio/installer.py`. No debugger listener, watcher, provider, real profile, user artwork or config is involved. The existing full installer suite is prior evidence; the new check addresses a distinct first-rename boundary outside the repaired second-rename handler.

Read debugging skill plus Python, setup and investigation references. The task's explicit ownership/no-sub-agent rules override the skill's root journal and delegation defaults: this owned artifact is the journal, and no `.debug-journal.md`, git ignore or other worker file is changed.

## Hypotheses before probes

1. H1 — Exception scope: moving the old target to backup succeeds, then SIGINT lands before the publication `try`; temporary-directory unwinding removes the un-restored backup. Distinguish by observing exact old bytes at `previous`, real SIGINT, missing final target. If confirmed, route “cover transition” to root.
2. H2 — Fixture/ownership invalidity: the management marker or source is invalid, causing rejection before the move. Distinguish with a passing valid managed-update PIN, a recorded reached first rename and exact saved backup bytes. If confirmed, correct only the fixture.
3. H3 — Wrong runtime/source: the invoked installer is a stale installed copy or source changes during execution. Distinguish exact imported module path/hash and before/after source pins against the accepted `768da32c…` installer. If confirmed, correct only import binding or await the owner.

No failed investigation round has occurred. Fixing, live installation and final verdict remain coordinator-owned.

## Observed PIN/RED

`first-rename-pin.txt`: unchanged managed-update control **1 passed in 0.07s**, PID 50193, exit 0. `first-rename-red.txt`: **1 failed in 0.08s**, PID 50390, exit 1; no timeout. Both were reaped. Exact commands and 60-second outer receipts are retained beside those logs. The module's 20-second self-alarm was not reached.

The RED performs the real old-target→backup filesystem rename, confirms exact previous bytes, and then raises a real SIGINT in the invoking process before that call returns. Observables:

```json
{"scenario":"sigint_after_first_real_rename","source_sha256":"768da32cdf90da78fd519a39b9b65bd3bdd4cf81c20dc4e45452ffc3e060708b","backup_exact_before_signal":[true],"target_exists":false,"prior_bytes_preserved":false,"remaining_entries":[]}
```

H1 is supported by the observed complete backup followed by absent target/backup after unwinding. H2 is refuted by the passing update control and exact reached backup. H3 is refuted by the actual imported checkout path and equal source SHA before/PIN/RED. Production code was not toggled or changed; a fix/cause-toggle test remains root-owned. The exact initial probe is `first-rename-probe.py.txt`; no assertion was removed or weakened.

First authored-harness Ruff check found only missing package initializer/module documentation; strict 3.11 basedpyright already had zero errors. First diagnostics are retained in `first-rename-lint-first.txt` and `first-rename-types.txt`; these do not alter the observed product failure.

The repository's existing `pyproject.toml:43` exempts pytest modules from `S101`, `D` and `INP001` (among other test-specific rules). The standalone scratch test is outside that glob. Reapplying only those existing pytest exemptions to this exact temporary path makes scoped Ruff pass (`first-rename-lint.txt`); no test/code/assertion was changed, and the reserved package initializer was not needed or created. The initially added module docstring had already been removed after comment-checker feedback; no documentation churn is required for a pytest module under the actual test policy.

The initial CLI spelling for those exemptions was rejected with exit 2 before linting because Ruff requires a repeated file pattern for each code; `first-rename-lint-option-error.txt` retains it. The corrected three `--extend-per-file-ignores path:rule` flags passed, without changing the test source.

Coordinator `msg_70e7d79e940e` clarifies that the acceptance invariant is no loss of prior install data, distinguishing restoration to target from a preserved backup elsewhere. The initial observed `remaining_entries=[]` proves neither target nor backup survived in the synthetic plugins directory. The retained regression additionally asserts target restoration; a future implementation that retains a recoverable backup must report that outcome explicitly rather than claiming this stronger assertion passed.

Coordinator `msg_1a4114a3d787` confirms independent goal/security observations of this same failure and routes follow-up task `task_8aa6c56bce98`. Its owner may change `installer.py`, add `test_installer_backup_interrupt.py`, and strengthen existing interruption assertions to preserve old backup data when restoration fails or a foreign target is occupied. This reviewer will rerun the exact unchanged original first-rename probe only after code-ready; no production edits or broad reruns are authorized here.

Code-ready message `msg_4748adcada2d` freezes installer SHA `8f75ba7f123f2550d405f4015de54319453b867044f635e0c7d3ed4b4de02116` with 42 owner tests and scoped static checks. Those are attributed owner results, not this review's execution. The original independent probe is now authorized for unchanged revalidation; final overall acceptance remains dependent on root `FIXES_READY`.

## Independent GREEN and source review

The exact original probe SHA remains `1ce32b0063e7b2d420291f8cdaff9de10577d98e8f6123a848a030d5f1725e71` (`first-rename-code-ready.json`). Re-executing its same test node against code-ready installer **passed in 0.10s**, exit 0, PID 63580 reaped; `first-rename-green.txt` and `first-rename-green-receipt.json` retain the exact command and result. Only the registered basetemp changes from RED to GREEN; the test bytes and assertions are identical.

```json
{"scenario":"sigint_after_first_real_rename","source_sha256":"8f75ba7f123f2550d405f4015de54319453b867044f635e0c7d3ed4b4de02116","backup_exact_before_signal":[true],"target_exists":true,"prior_bytes_preserved":true,"remaining_entries":["logopia-studio"]}
```

I read the complete final installer, new backup-interruption tests and strengthened existing interruption tests. Both renames now occur inside recovery handling. Explicit stage disposal cannot remove an un-restored `previous`; a failed restoration or occupied foreign path retains exact prior data and annotates the original exception with its location. Ordinary recovery restores the target and removes staging; normal update still verifies the management marker and rejects unknown files. The added tests cover interrupted restoration before/after its move, occupied directory/file/symlink/dangling symlink, repeated first/second rename interruption followed by explicit retry, and cleanup interruption without deleting the old backup. Those additional executions are the owner's attributed 42-test evidence, not my new execution.

## Resource TODOs before creation

- TODO: recreate only registered `/tmp/logopia-review-goal-080`, currently absent; it will contain `test_first_rename.py`, exact PIN/RED pytest basetemps, isolated pytest/Ruff cache if needed, and a strict typecheck config if needed. Remove this entire exact root again after preserving evidence.
- TODO: one authored `test_first_rename.py` with a valid-update control and a real SIGINT immediately after the actual old-target→backup rename, using only synthetic profiles under pytest basetemp. Preserve exact text in this artifact directory. No production patch.
- TODO: bounded foreground PIN and RED child commands; outer process-group limit 60 seconds, five-second termination grace, pytest-module self-alarm 20 seconds; record child PID, exit and source hashes. Every fixture source/profile lives in the registered root. Command-local `PYTHONDONTWRITEBYTECODE` and isolated pytest cache avoid persistent environment changes.
- TODO before creation: scratch `__init__.py` to satisfy package discovery for the authored temporary test only. Restore a necessary one-line module purpose declaration required by the scoped Python documentation gate; keep all test assertions identical. No production/test-suite file changes.
- CANCELLED: the reserved initializer/documentation change was unnecessary under the repository's existing pytest lint policy; neither was added to the retained test.
- TODO before creation/execution: `/tmp/logopia-review-goal-080/first-rename-green` as the sole new revalidation basetemp, using the exact unchanged original test node with the same 60-second outer/20-second inner deadlines. Retain code-ready source/test hashes and exit/PID receipt; remove this basetemp with the registered root after final review.
- DONE: independent original GREEN recorded; final source and original probe copies retained, exact scratch root removed at 2026-09-14 17:29:57 UTC. `cleanup-final.json` confirms the eight original/follow-up child PIDs absent and port 8813 free. No temporary script, fixture profile, pytest cache, or reserved initializer remains.
- TODO before creation: coordinator `msg_d65509b2b2de`, received after the prior cleanup, explicitly requests the unchanged **control and SIGINT pair together** on final code. Recreate only `/tmp/logopia-review-goal-080`, copy the byte-identical retained probe to `test_first_rename.py`, and use `final-pair/` plus isolated pytest cache. Run both existing tests with the same 60/20-second deadlines, then remove the exact root again and retain a new cleanup receipt. This required follow-up is not a broad or flakiness rerun.
- DONE: final requested pair **2 passed in 0.07s**, PID 67600 reaped, with original test SHA and frozen installer SHA in `first-rename-final-pair-receipt.json`. `first-rename-final-pair.txt` retains exact SIGINT/restoration observables. Results were sent to root (`msg_f3784335a5d0`) and the fix dispatch (`msg_f99a723feb90`). `cleanup-final-pair.json` confirms the recreated root absent, all nine recorded PIDs absent and port 8813 free at 2026-09-14 17:31:30 UTC. This is the latest cleanup checkpoint.
