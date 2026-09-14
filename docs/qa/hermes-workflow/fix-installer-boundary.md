# Installer publication-boundary preservation follow-up

Status: complete for the bounded installer follow-up. Task `task_8aa6c56bce98`, dispatch `ctx_6ffaa5298aa4`, run `run_ad4a666ccb76`.

## Ownership and execution steps

Only `installer.py`, new `tests/hermes/test_installer_backup_interrupt.py`, the
explicitly authorized stronger assertion in `test_installer_interruption.py`, this
report and `fix-installer-boundary/` are writable. The existing installer report,
two independent reviewer reproductions, root plan/journal, metadata, process
modules, real profiles, canonical artwork and other workers' edits are preserved.

1. Complete: pin unchanged source, valid managed update and second-rename
   OSError/KeyboardInterrupt identity/byte restoration; retain first-rename RED.
2. Complete: add failing-first persistent boundary/recovery regressions, then make
   the minimal exception-safe publication and cleanup change.
3. Complete: exact original probes GREEN, requested scoped tests, Ruff/format,
   strict Python 3.11 checks and bounded tmux/manual native-runtime checks.
4. Complete: source freeze to root/existing reviewers, independent original probe
   confirmation, nine-class evidence and exact owned-resource cleanup.

No `update_plan` tool is exposed, so this ordered ledger tracks execution. The
user's exact pre-existing plan and no-agent/no-plan-edit scope take precedence over
the planning skill's generic planning/delegation defaults. Programming Python
README/error handling/one-liners, debugging Python/setup/investigation/fix/QA/cleanup,
and the runtime Orca orchestration guide have been consulted; this owned report
serves as the debug journal instead of creating or changing a root journal.

## Hypotheses and distinguishing observations

- H1: the real first rename completes outside the recovery handler; automatic
  temporary cleanup deletes the only old payload. Observe exact backup bytes
  before actual SIGINT, absent target and absent backup after unwinding. If true:
  cover both renames.
- H2: invalid marker/source prevents a real managed move. Observe a successful
  unchanged-source PIN and exact old bytes at the moved backup. If true: fix fixture.
- H3: stale imported code or concurrent edits explain inconsistent behavior.
  Record imported path and source SHA before and after each run. If true: rebind source.
- H4: restoration failure or an occupied foreign target strands the old payload
  inside an automatically deleted directory. Inject bounded restoration failure
  and occupied file/directory/symlink cases, asserting both old and foreign bytes.
  If true: make backup retention explicit and never issue a success receipt.

No inconclusive investigation round so far. The prior independent REDs remain at
`review-goal/first-rename-*` and `review-security/first-rename-*`, with original
installer SHA `768da32cdf90da78fd519a39b9b65bd3bdd4cf81c20dc4e45452ffc3e060708b`.

## Resource registry, before creation

| Resource | Ownership, purpose and cleanup |
| --- | --- |
| This report and `fix-installer-boundary/` | Retained sanitized commands/exits, source/test snapshots, hashes, first PIN/RED/diagnostics, GREEN/manual/reviewer/cleanup receipts. |
| `/tmp/logopia-fix-installer-boundary-080` | Exclusive registered scratch; confirm absent before creation; remove exact root after evidence capture. |
| Scratch `runner.py`, `manual.py`, `native_audit.py`, `test_goal_original.py`, `test_security_original.py` | Finite local harnesses and byte-identical independent probes; retain `.py.txt` copies and remove originals with scratch. |
| Scratch `pin/`, `red/`, `red-recovery/`, `green/`, `goal-pin/`, `goal-red/`, `goal-green/`, `security-green/`, `pytest/`, `cache/` | Exact pytest basetemps and caches including all synthetic source, named profiles, config, workspace, external sentinel files, symlinks and fault-retained recovery directories. Remove with scratch. |
| Scratch `manual/`, `native-manual/` | Synthetic named profiles/source/workspaces only, including every installer `plugins/.logopia-install-*` stage/recovery directory and foreign target fixture. Remove with scratch. |
| Scratch `processes.jsonl`, `manual.pid`, `native-manual.pid`, `tmux-pane.pid`, `manual.json`, `native-manual.json` | PID ownership and finite-child receipts; copy sanitized evidence before removing scratch. |
| Scratch `typecheck.json` | Optional strict native-config supplement if needed; remove with scratch. |
| tmux `logopia-fix-installer-boundary-080` and its sole shell PID | Register exact pane PID immediately after creation; send finite manual commands, capture output, kill only exact owned session, verify PID/session absence. |
| Foreground scoped test/static children and manual/native children | Reserve each command before spawn in `processes.jsonl`, record PID immediately, wait/reap with 30-second deadline; terminate only owned process group on timeout. |
| Command/session-local `PYTHONDONTWRITEBYTECODE`, `PYTHONPATH`, `TMPDIR`, `RUFF_CACHE_DIR` | Route artifacts/imports to owned scratch and checkout; no global environment changes. |

Existing foreign-occupation test currently expects only the foreign target to
remain. A stronger no-old-payload-loss invariant necessarily replaces that single
cleanup assertion with exact old recovery-directory bytes plus no lock/stage;
its foreign-byte assertion and exception expectation must remain intact.

## First observations, before production edit

`pin.txt`: 3 passed, exact complete staged/installed byte equality for managed
update and exact original exception identity/full old-byte restoration for the
existing second-rename OSError and KeyboardInterrupt cases. PID 57364 reaped.

`red.txt`: persistent real first-rename SIGINT regression failed on the empty
installed snapshot. `goal-red.txt`: the byte-identical independent probe retained
its valid control and reproduced `backup_exact_before_signal=[true]`,
`target_exists=false`, `prior_bytes_preserved=false`, `remaining_entries=[]`.
PIDs 57810 and 57811 reaped. Source SHA before/after every run is exactly `768da32c…`.
H1 confirmed, H2/H3 refuted. No production line was edited before these REDs.

`red-recovery.txt`: both I/O restoration cases raised the restoration exception
instead of the original publication instance. Its real restoration SIGINT then
escaped pytest's expected PermissionError and ended the run with exit 2; first
output retained, PID 58392 reaped. This is an observed failure, not a flaky test.
Remaining independent cases will use exact selectors without altering assertions.

Additional registered basetemps before creation: scratch `red-foreign/` and
`red-restored-sigint/` for the remaining distinct first-failure observations.

## Code-ready source freeze

Installer SHA-256: `8f75ba7f123f2550d405f4015de54319453b867044f635e0c7d3ed4b4de02116`.
`goal-green.txt` and `security-green.txt` each pass the two exact original cases
without probe edits. Both show exact old bytes before/after first-rename SIGINT and
only the restored target remaining. `scoped.txt`: requested five-file scope,
**42 passed in 9.63s**. `ruff-code.txt` and `types-code.txt` pass (strict native
Python 3.11: zero errors/warnings/notes). Production/source tests now frozen.

The change replaces automatic temporary-directory cleanup with explicit owned
stage disposal. Both real moves are in the recoverable publication block. A
failed recovery catches its OSError/KeyboardInterrupt and annotates the original
publication exception; a still-existing backup is retained with its exact path.
The cleanup path can only select `new` when an uncommitted `previous` remains.
A dangling foreign symlink is treated as occupied. No success receipt is returned
from any error path. Cleanup failures also annotate the original error.

`red-foreign.txt`: all five cases failed before the production edit. Existing
foreign-byte and exception assertions were preserved; only the old test's claim
that no recovery directory should exist was replaced by the stronger old-byte
retention assertion. First snapshots and all prior task evidence are retained.

First static diagnostics remain in `ruff-first.txt`, `format-first.txt` and
`types-first.txt`: test-only complexity/exception construction, capture-pattern
exhaustiveness, scratch script executable/path spelling and formatting. Fixed
without production changes or weaker assertions. Test source is 226 logical lines,
installer 152 and existing interruption test 104, all within the ceiling.

Before creation, also register scratch `toggle/logopia_studio/`, `toggle/tests/`,
and `toggle/pytest/` for a copied-package cause-toggle if needed. Its installer is
the saved original, never a revert of the shared working tree; cleanup removes
the exact scratch copy. Review-work's generic new-agent fan-out is superseded by
the task's no-agents rule and root's existing independent reviewers.

## Final automated and native checks

- `scoped-final.txt`: **42 passed in 8.06s**, PID 69983, exit 0, no timeout,
  reaped. This repeats only the requested five-file scope because another worker
  changed the two imported process modules after the first run; their final hashes
  remain stable across this run (`dependencies-before-final.sha256`,
  `dependencies-final-check.txt`). Root owns broader integration checks.
- `ruff-final-checked.txt`: all six changed/authored Python files pass.
- `format-final.txt` plus `native-format-final.txt`: all files formatted.
- `types-final.txt` plus `native-types-final.txt`: strict
  `basedpyright --pythonversion 3.11`, zero errors/warnings/notes.
- `native-audit-final.txt`: actual Hermes CPython **3.11.16**, Pydantic **2.13.4**;
  all six files parse as Python 3.11, with no Any/object/cast names. Logical lines:
  installer 152; new regression 226; existing regression 104; manual 202; runner
  69; native audit 50. No dependency was added or upgraded.
- `no-excuse.txt`: programming skill audit passes the source, regressions and
  manual/runner. The native audit additionally passed its own strict checks.
- `toggle-red.txt`: isolated copied package with the saved original installer
  `768da32c…` fails the exact original first-rename probe, original-exception
  restoration assertion and stronger foreign-target preservation assertion,
  **3 failed in 0.12s**. Its emitted imported path/hash proves the cause toggle;
  the shared source remains `8f75ba7f…` before and after.

The manual script's initial style diagnostics (print calls, exception assertions
inside except blocks and function complexity) remain in `manual-ruff-first.txt`;
the native audit's initial numeric-constant diagnostic remains in `ruff-final.txt`.
They were fixed only in the owned scratch scripts, with unchanged production/tests.
The standalone manual script applies only the existing pytest-style `S101`
assertion exemption; it uses stdlib exception capture so it needs no pytest in the
native environment. No checks or assertions were suppressed to obtain a pass.

## Actual tmux and native manual QA

Registered session `logopia-fix-installer-boundary-080` ran:

```sh
tmux send-keys -t logopia-fix-installer-boundary-080 'uv run --locked python /tmp/logopia-fix-installer-boundary-080/manual.py' Enter
tmux capture-pane -p -S -220 -t logopia-fix-installer-boundary-080
```

The same pane additionally ran the existing interpreter:

```sh
/Users/cillian/.hermes/hermes-agent/venv/bin/python -B /tmp/logopia-fix-installer-boundary-080/manual.py --native
```

`tmux-manual.txt` records **PASS**, Python **3.12.12**, PID **66288** and
`manual_exit=0`; `tmux-native-manual.txt` records **PASS**, native **3.11.16**,
PID **67024** and `native_manual_exit=0`. Both manual drivers installed a
30-second alarm before synthetic fixture creation. Every fixture profile is
named `logopia-boundary-fixture` under the registered scratch root; no real/default
profile or native model API was read or modified.

Each runtime performs actual first old-target→backup movement, reads every backup
byte, then raises real SIGINT before returning from the first rename. The second
boundary is interrupted immediately before new→target publication, matching the
previous accepted second-rename case. Each case repeats twice, checks the original
KeyboardInterrupt instance, complete prior tree and no lock/staging entries, then
performs an explicit normal update and compares every installed byte to the whole
staged tree. A normal update is never inferred from process exit or error text.

Each runtime additionally repeats foreign target occupation, denied restoration,
and a second actual SIGINT during restoration. Every failed install preserves the
original exception and the exact old tree at the path named in its notes, with no
success receipt. These retained backups are deliberately restored by the fixture
driver only after verifying old and foreign bytes; it first removes only its own
known synthetic foreign sentinel. Stale manifest hashes refuse twice with exact
installed-byte preservation. `manual.py.txt` is the executed driver.

| Runtime | First-rename old/after SHA-256, identical on both attempts |
| --- | --- |
| 3.12 | `ae09f4756950250e2e96fe1de9495f84af2a02d915bcc017f7a7845f2040d87c` |
| 3.11 | `b1a56fcf419a456950c2a277d84e58c11246e356d923165d82a42d932683cad6` |

The paths/settings differ between runtimes, so hashes are compared within each
scenario. Full byte tuples are also compared, independently of these displayed hashes.

## Nine classes

| Class | Result and evidence |
| --- | --- |
| 1. Malformed/foreign input and symlinks | PASS: existing strict malformed-marker, unowned/nested marker and source/root/nested symlink refusal tests in the scoped suite. New occupied-target checks cover directories, files, valid links and dangling links, preserving foreign and old bytes. |
| 2. Instruction-like sentinel | PASS: literal source/foreign sentinel bytes are compared exactly; they are never executed or treated as instructions. |
| 3. Cancel/resume | PASS: real SIGINT at both specified rename boundaries, twice per runtime, followed by an explicit full-byte verified update; original exception identity preserved. |
| 4. Stale state | PASS: stale managed hashes refuse in automated tests and twice in each manual runtime without changing the installed tree. |
| 5. Dirty worktree/canonical/protected files | PASS for owned scope: 85/87 original pins unchanged, including metadata, four protected drafts, canonical workflow, five originals and all prior installer evidence. Only the concurrent worker's launcher_process.py/helper_process.py changed; neither was edited here. The updated dependency hashes stay equal across final scoped verification. |
| 6. Bounded fixtures/children | PASS: every runner-owned verification child has a 30-second outer deadline and a reaping receipt; both actual manual processes have 30-second self-alarms. No service, port, new agent, inference/provider request or real profile operation. Provider budget/hard-kill behavior is outside this local installer scope. |
| 7. First failures/retry discipline | PASS: original source, first persistent/independent REDs, interrupted recovery run and all first diagnostics retained; deterministic isolated source toggle fails again. No flaky retry or removed failure assertion. |
| 8. Misleading success | PASS: full installed/prior byte tuples, backup read-back, exact exception instances, refusal codes and resource state determine success. Retained recovery always remains a failed attempt. |
| 9. Repeated interruption/restoration/cleanup | PASS: repeated SIGINT attempts, denied restoration, actual SIGINT during restoration before/after its real move, and OSError/SIGINT while discarding an unpublished stage preserve exact old bytes and the original error. A cleanup failure may retain the new stage too, with an explicit cleanup note; it never permits disposal of the only old tree. |

Ordinary successful/refused/recovered attempts leave no lock/staging resource.
Uncompleted restoration intentionally leaves `plugins/.logopia-install-*/previous`
as an explicitly identified recovery directory; cleanup failure may additionally
leave `new`. This is a failed-install recovery outcome, not a successful receipt.
No hard-kill/power-loss guarantee or native installation refresh is claimed.

## Independent verification and cleanup status

Code-ready/freeze messages: root `msg_3c9d390b6e0c`, goal reviewer
`msg_4748adcada2d`, security reviewer `msg_0a2d075d8578`. Inbox was checked before
freeze. Goal reviewer `msg_f99a723feb90` independently passed both exact unchanged
original probe cases on `8f75ba7f…`; root accepted the pair/cleanup in
`msg_28cb4b108fb4` and also reported the code reviewer's independent two original
second-rename cases passing. Security confirmation is complete, as recorded below.

Cleanup is complete (`cleanup.json`, `tmux-absence.txt`): the exact owned session
is absent; its shell PID **66257**, both manual PIDs **66288/67024**, and all
runner-recorded verification PIDs are absent (**35 total**). Every runner child
was waited/reaped with no deadline reached. The registered scratch root is absent
after removing **1097** owned entries, including **16** intentionally retained
synthetic recovery directories. Their pre-removal file hashes are retained in
`recovery-before-cleanup.json`; no non-synthetic directory was removed.

Only sanitized code/probe copies, logs, exact command/exit/PID receipts, diffs,
hashes and this report remain. Reserved but unused scratch paths (goal-pin,
red-restored-sigint, typecheck config, copied tests) were never created. Session
and command environment overrides ended with their owning shells/processes.
Final source/test hashes match `final.sha256` after cleanup. Root still owns the
real named-profile refresh, overall T5 review and publication.

Coordinator reply on question `msg_b07e7e6c1524` explicitly accepted the installer's
code/manual QA/cleanup completion and instructed keeping the frozen source while
waiting for security's final pair. The coordinator separately reported broader
helper/existing color-test failures under its investigation; this worker did not
run the broad suite or attribute those failures to the installer.

Security reviewer `msg_aa97c72e7128` independently passed its byte-identical
original control and real first-rename SIGINT cases, **2 passed in 0.11s**, exit 0,
on the frozen `8f75ba7f…` source. The original probe, source/canonical/protected
hashes and cleanup all agree (`review-security/first-rename-fixed.txt`,
`review-security/first-rename-fixed-cleanup.json`). The observed interrupt has
`target_exists=true`, `prior_bytes_preserved=true`, and only `logopia-studio`
remaining. Both original independent first-rename pairs are now verified.

Root `msg_f4bf255cc4b7` read and accepted the security pair together with goal/code
pairs and this worker's 42-test/manual/cleanup evidence, and explicitly requested
the terminal completion report. The inbox was checked before completion, final
source/test hashes match, and scratch remains absent. Every scoped step is
complete; no installer work remains. The separate process race, broader T5,
actual install refresh and publication remain root-owned.
