# Process settlement fix evidence

Owner: task `task_d9d453f29ed6`, dispatch `ctx_bf378afcde38`.
Scope: `launcher_process.py`, `helper_process.py`, announced `process_group.py` and `process_scope.py`,
`test_process_group_settlement.py`, `test_helper_interrupt.py`, and this report/artifacts.
The root journal and every other owner's changes remain outside this scope.

Final source and tests are frozen after the nested helper correction: all six hashes match
the independent reviewer's `review-code/process-final-source.sha256`. The required scoped
suite passed 38 tests; the reviewer's unchanged original probes passed 3 tests and its
unchanged nested probe passed 1 test. Final tmux QA reports `MANUAL_PASS`, exit 0,
zero ResourceWarning, and every observed owned PID/PGID absent before result propagation.
Freeze notification: `msg_23d32d9fe44a`; report and cleanup are the only subsequent changes.

## Plan

1. COMPLETE: unchanged launcher 9 passed; helper stdout/typed error PIN 3 passed.
2. COMPLETE: first RED retained; corrected finite fixture RED shows 7 failures / 9 passes.
3. COMPLETE: exact group/session settlement includes the actual nested helper regression.
4. COMPLETE: final scoped 38 passed, strict checks passed, independent original 4 passed,
   final tmux manual PASS with two real Ctrl-C events.
5. COMPLETE: sanitized evidence retained; exact temporary root, tmux session, shell and
   sole-session server removed; all numeric cleanup receipts checked before completion.

## Hypotheses

- H1: leader `poll/wait` is mistaken for complete group settlement; distinguish by
  a ready descendant's exact PID/PGID/stat after leader exit and after return.
- H2: the helper's new session isolates it from caller interrupts; distinguish by
  real caller-only SIGINT, original exception propagation, and owned helper state.
- H3: stale import/runtime or a transient zombie explains the failure; distinguish
  using imported absolute paths, interpreter/version, recorded OS states and source hashes.
- H4: repeated interrupts abort cleanup; distinguish initial and cleanup interrupts
  with finite fixtures, original error identity and group absence before return.

## Resource register (registered before creation)

- [x] `/tmp/logopia-fix-process-080` temporary root; remove this exact tree.
- [x] `/tmp/logopia-fix-process-080/pin-launcher` baseline pytest directory; remove with root.
- [x] `/tmp/logopia-fix-process-080/pin-helper` helper PIN pytest directory; remove with root.
- [x] `/tmp/logopia-fix-process-080/red` RED pytest directory; remove with root.
- [x] `/tmp/logopia-fix-process-080/pytest` required GREEN pytest directory; remove with root.
- [x] `/tmp/logopia-fix-process-080/manual.py` manual runner; retain sanitized text then remove.
- [x] `/tmp/logopia-fix-process-080/manual` manual fixture files/logs/receipts; remove with root.
- [x] `/tmp/logopia-fix-process-080/manual-final` final manual fixture tree, runner receipt and
  readiness thread; cases `deadline`, `exited`, `nested`, `automatic`, `terminal`, `helper-timeout`.
- [x] `/tmp/logopia-fix-process-080/manual-final/control.pid`: finite manual foreign-session
  control, explicit Popen PID registered immediately; own finally kill/wait and absence receipt.
- [x] `/tmp/logopia-fix-process-080/manual-final2`: final manual fixture/runner/control receipts,
  same finite cases; readiness detection and both tmux Ctrl-C sends occur in one bounded driver
  command to avoid inter-tool latency consuming the fixture's 7s input deadline.
- [x] tmux session `logopia-fix-process-080`; record pane PID, close only this session,
  verify exact PID absence.
- [x] `/tmp/logopia-fix-process-080/tmux-pane.pid` owned pane-shell receipt; remove with root.
- [x] `/tmp/logopia-fix-process-080/manual/runner.txt` manual runner PID/version/import receipt;
  remove with root after verifying exact runner PID absence.
- [x] Manual readiness notification thread: bounded 5s, stop Event and 1s join in finally.
- [x] Manual caller signal handlers: SIGINT records original and repeats, SIGALRM 45s watchdog;
  restore original handlers and cancel the alarm in finally.
- [x] Manual case directories `deadline`, `exited`, `automatic`, `terminal`, `helper-timeout`:
  each owns one `finite_fixture.py`, ready marker, exact `.pid` receipts and optional launcher logs;
  finite-fixture finally settles every recorded numeric ID, then temporary root is removed.
- [x] Baseline launcher child processes created only by unchanged tests; tests reap each child.
- [x] PIN helper subprocesses created with exact literal argv; fixture owns and reaps each leader.
- [x] RED/GREEN process-tree leaders and descendants: finite 10s alarm, readiness pipe,
  exact PID/PGID receipt before exercising signal; each fixture finally settles its own IDs.
- [x] RED/GREEN caller interrupt fixtures: finite 10s alarm, own fresh group, exact PID/PGID
  receipt before caller signal; signal handler restored and exact IDs settled in finally.
- [x] RED/GREEN foreign-session control subprocess: literal 10s alarm fixture, captured Popen
  PID before launching the tested group, own kill/wait finally; verify exact PID absence.
- [x] `/tmp/logopia-fix-process-080/red-fixture-corrected` RED directory after correcting
  the fixture's transient macOS zombie EPERM observation; remove with temporary root.
- [x] `/tmp/logopia-fix-process-080/red-force-bound` pytest directory for rejected group
  delivery fixture; child has its own 10s alarm and direct-PID finally cleanup, restore OS patch.
- [x] `/tmp/logopia-fix-process-080/green-bound-observables` final bounded failure / foreign
  control pytest receipts after assertion formatting; remove with temporary root.
- [x] `/tmp/logopia-fix-process-080/red-nested` persistent nested RED fixtures, including
  `finite_leaf.py`, leader script, ready marker and both exact PID/PGID receipts; finally cleanup.
- [x] `/tmp/logopia-fix-process-080/green-nested` nested GREEN pytest directory; exact finite
  leader/helper PID receipts and finally cleanup; remove with temporary root.
- [x] SID receipt files `helper.sid` and `leader.sid` in registered fixture directories;
  prove helpers share the captured launcher session while retaining distinct PGIDs.
- [x] Planned registration pipe: not created; replaced by the coordinator-approved numeric
  PID/session membership design before any IPC implementation.
- [x] Numeric PID query subprocesses: exact literal `/bin/ps -A -o pid=`, context-owned unnamed
  temporary output file, 0.25s query and at most 0.25s exact-PID kill/reap; no watcher or named files.
- [x] Manual runner and finite fixture processes: record own caller/leader/descendant IDs
  before each scenario; final cleanup confirms all recorded child/group IDs absent.
- [x] Final cleanup verification: fixed `/bin/ps -p <recorded numeric IDs> -o pid=,ppid=,pgid=,stat=`
  with a 2s subprocess deadline and signal-zero checks only for recorded PGIDs; no process signals.
- [x] `fix-process/` permanent sanitized evidence directory; keep as task artifact.

## Evidence

- PIN: `fix-process/pin-launcher.txt` (9 passed, unchanged source),
  `fix-process/pin-helper.txt` (3 passed, unchanged source).
- Locked interpreter: repository `.venv/bin/python3`, Python 3.12.12.
- Native interpreter available: `/Users/cillian/.local/bin/python3.11`.
- Both imported process modules resolve to this exact repository's
  `integrations/hermes/logopia_studio/` directory.
- Shared module announcement: `integrations/hermes/logopia_studio/process_group.py`
  will own only settlement of the freshly created session's numeric PGID. It is
  auto-included by installer's existing recursive regular-file payload collection.
- No new agents will be created; coordinator already owns five independent reviewers.
- Automatic comment feedback: new test comments are required Given/When/Then
  behavior descriptions, retained under the comment-checker BDD exception.
- First RED: `fix-process/red-first.txt`, 6 failed / 8 passed. Actual leftover
  descendant states were `33339 1 33338 S`, `33376 1 33374 S`, `33397 1 33396 S`,
  `33403 1 33402 S`; helper `33384 33337 33384 Ss` survived interruption.
  The signal-handling control (`ignores=no`) passed unchanged.
- Fixture correction required: after killing helper 33384, macOS briefly returned EPERM
  for `killpg(33384, 0)`. Treating EPERM as still present ensures the fixture continues
  its bounded absence check rather than escaping cleanup. No test assertion is weakened.
- Corrected RED: `fix-process/red-fixture-corrected.txt`, 7 failed / 9 passed, including
  a real repeated-interrupt launcher failure. All registered group/PID cleanup receipts
  report absence; the old helper also produces a subprocess ResourceWarning.
- New implementation explicitly probes group absence after reaping the leader, tracks
  one fixed graceful deadline plus a 10s forced deadline, and retains the first cleanup
  interrupt. A later interrupt accelerates SIGKILL without resetting the deadline.
  A group observed absent is never signalled again. No process-name searches are used.
- Initial GREEN: required scoped suite 34 passed in 30.84s; native 3.11 type check clean.
- Additional finite-bound concern: `Popen.__exit__` can start an unlimited leader wait if
  group signalling fails beyond the forced deadline. A harmless fixture rejects delivery
  only at the owned signal boundary; no real permission/profile changes are performed.
- Additional RED confirmed: `fix-process/red-force-bound.txt`, both routes waited
  approximately 10.03s for fixture SIGALRM despite 1.2/2.3s settlement limits.
  Launcher now owns its output streams directly; helper uses ExitStack only for its
  pipes. Both settle in finally, so Popen context exit cannot introduce an unbounded wait.
  Failure to settle remains an explicit error, never a successful process receipt.
- Before the nested extension, scoped GREEN reached 36 passed in 31.83s.
  The final retained `fix-process/green-scoped-final.txt` is the post-nested 38-test run below.
- Native Python 3.11 basedpyright: zero errors/warnings; repository tests: zero issues
  before manual script inclusion. Ruff and formatting pass; no-excuses scan finds no violations.
- Manual runner's sole type issue (unused flush return) was corrected before execution.
- Initial manual tmux passed before nested extension: exact timeout, two real Ctrl-C events,
  first exception retained, all observed groups absent, zero ResourceWarning, exact resumed stdout.
  Retained as `fix-process/tmux-before-nested.txt`; it is not final evidence for the nested fix.
- Freeze withdrawn on explicit user/coordinator instruction: independent reviewer observed
  actual nested helper `42613 1 42613 Ss` after launcher -9 receipt. Reviewer cleaned this PID.
  Original evidence is `review-code/nested-helper-tests.txt` and `nested-helper-probe.py.txt`.
- Announced new scoped module: `integrations/hermes/logopia_studio/process_scope.py`.
  Final design approved by coordinator's durable ask reply and independent reviewer:
  `run_cli` uses Python 3.11 `process_group=0`, preserving literal argv and locked environment;
  launcher owns its newly created SID and enumerates numeric PIDs only, with immediate
  `os.getsid`/`os.getpgid` verification before signalling each observed group representative.
  Standalone helper cleanup remains restricted to its own PGID. No IPC/preexec_fn/watcher.
- Persistent nested RED: `fix-process/red-nested.txt`, helper `52907 1 52907 Ss` survives
  launcher receipt after 2.215s; fixture cleanup confirms both exact groups absent.
- Numeric enumeration failure is a typed `process_inspection_failed` launcher error.
  A failed or incomplete ownership query cannot yield a successful receipt.
- First nested GREEN: `fix-process/green-nested-first.txt`, both owned groups absent at
  2.342s before the timeout receipt. Refactor only separates mutable group observations
  from the bounded deadline loop; caller API and signal sequence are unchanged.
- Retained post-nested verification failure: `fix-process/green-scoped-nested-first.txt`
  (37 passed, one failure). At the forced deadline's last 5.7ms, the remaining-time-limited
  PID probe expired and incorrectly replaced the original force timeout with inspection failure.
  Refresh now reports incomplete verification without replacing the original timeout once
  the fixed forced deadline has expired; genuine earlier inspection failures remain typed errors.
- Final manual first attempt retained in `fix-process/tmux-final-input-timeout.txt`:
  deadline/exited/nested/foreign-control cases passed, but the terminal input arrived after the
  7s helper invocation deadline between separate tool calls. The helper was settled by its
  timeout cleanup; this attempt is not counted as a manual PASS. Retry changes the bounded
  input driver, not source behavior or time limits.

## Final behavior and limits

`run_process` captures a fresh session through `start_new_session=True`. `run_cli` starts
its own group with Python 3.11 `process_group=0`, keeping the enclosing session so that a
forced launcher shutdown can also settle the nested helper group. Standalone helper cleanup
targets only that helper's fresh PGID. Existing helper locked-runtime, literal argv, exact
stdout, typed error detail, timeout cause and commit-reconciliation message remain pinned.
ExitStack owns helper streams without Popen's implicit unbounded context-exit wait.

`process_group.py` accumulates active/finished groups and retains the first cleanup interrupt.
Leader reaping and group absence are separate conditions, including normal/nonzero returns.
One graceful deadline and one forced deadline govern every owned group; repeated interrupts
accelerate forced termination without extending either deadline. Once absent, a group is
not signalled again. `process_scope.py` reads only numeric PIDs from the fixed `/bin/ps`
invocation, selects the captured SID using OS getsid/getpgid, and rechecks the representative
before each signal. IDs <= 1 and the caller's current group/session are rejected.

| Operation | Bound after its invocation deadline | Evidence/qualification |
| --- | --- | --- |
| Launcher | configured grace + 10s force + at most 0.25s for an in-flight probe's exact-PID reap | Default grace 10s gives 20.25s, plus OS scheduling overhead; one shared budget, not per group |
| Helper | 2s grace + 10s force | Original typed timeout is preserved when settlement succeeds |
| Numeric PID query | at most 0.25s, clipped to remaining outer deadline; exact-PID cleanup at most another 0.25s | Anonymous output file is closed; query subprocess is killed/reaped on all normal tested paths |
| Repeated caller SIGINT | same fixed cleanup deadlines | CPython may spend up to 0.25s handling the first interrupted wait before entering cleanup |

Unverifiable ownership raises typed `process_inspection_failed`; exhausted force budget
raises `TimeoutExpired`, not a receipt. An exhausted final numeric probe does not replace
the original force timeout. The injected signal-denial cases intentionally observe a still
live finite fixture at this explicit error, then kill/reap its exact PID in test finally;
those are bounded failure cases, not claims of successful settlement.

The scope is local process settlement. There is no provider-cancellation claim, no guarantee
for arbitrary software deliberately escaping the captured session, and no model/image call.
No IPC, preexec_fn, watcher, dependencies, process-name/argv/environment scans, pkill,
parent-group signals, installer edits or profile installation were introduced. Both new
modules are automatically included by the installer's existing recursive `_source_files`
collection. The coordinator owns integration and actual profile refresh.

## Final verification

Required command (locked repository runtime Python 3.12.12):

```sh
uv run --locked pytest -q tests/hermes/test_launcher_process.py tests/hermes/test_process_group_settlement.py tests/hermes/test_helper_interrupt.py tests/hermes/test_helper_bridge.py tests/hermes/test_helper_recovery.py --basetemp /tmp/logopia-fix-process-080/pytest
```

- `fix-process/green-scoped-final.txt`: **38 passed in 29.58s**.
- `fix-process/green-nested-boundaries.txt`: 5 passed, 15 deselected in 8.50s;
  forced-delivery failure returned at 1.208s launcher / 2.304s helper, nested settlement
  at 2.334s, typed inspection failure at 1.203s, independent control PID 68699 preserved.
- `fix-process/types-native-final.txt`: basedpyright `--pythonversion 3.11` on the four
  native modules, 0 errors/warnings; `types-tests-final.txt`: repository test configuration
  for both tests and the manual runner, 0 errors/warnings.
- `fix-process/ruff-final.txt`, `format-final.txt`, `no-excuses.txt`: all checks pass,
  six files already formatted, no forbidden type escapes or file-size violations.
- Reviewer `msg_2796d309f7d2` and coordinator `msg_c720b48b4401` confirm unchanged probes:
  `review-code/defensive-final-tests.txt` 3 passed in 2.65s and
  `review-code/nested-helper-final-tests.txt` 1 passed in 2.33s. Descendant 71206,
  helper 71268 and nested helper 71528 are absent at receipt time; ResourceWarning 0.
  The third defensive probe concerns the separately owned installer fix; this worker
  did not modify its implementation. All six source/test hashes agree before/after review.
- The independent reviewer parsed all 52 native modules with actual Python 3.11;
  this worker's executions use the requested locked 3.12 runtime and native 3.11 static checks.
  This worker did not run the whole repository suite or install/refresh any real profile.

## Final manual tmux

Session `logopia-fix-process-080`, runner `/tmp/logopia-fix-process-080/manual.py`.
The required commands were used with readiness-gated control delivery:

```sh
tmux send-keys -t logopia-fix-process-080 'uv run --locked python /tmp/logopia-fix-process-080/manual.py' Enter
tmux send-keys -t logopia-fix-process-080 C-c
tmux send-keys -t logopia-fix-process-080 C-c
tmux capture-pane -p -S -250 -t logopia-fix-process-080
```

The final bounded driver waits for `manual-final2/terminal/ready`, sends the first Ctrl-C
after 0.1s and the second after 0.4s, then waits at most 6s for the exact runner PID.
`fix-process/tmux-final-raw.txt` retains capture including prior attempts;
`fix-process/tmux-final.txt` contains only the final joined transcript segment.
`fix-process/manual-final.py.txt` preserves the runner; all fixtures have 10s alarms,
the runner has a 45s watchdog, and every fixture records exact IDs before the action.

| Final scenario | Receipt-time observation |
| --- | --- |
| Deadline, leader exits first | PIDs 73544/73545, PGID 73544 absent; timeout receipt exit -2 at 1.288s |
| Normal exited leader | PIDs 73573/73575, PGID 73573 absent; normal receipt exit 0 at 0.319s |
| Actual nested run_cli helper | Leader 73597 and helper 73599, distinct PGIDs in one SID, all absent at 2.317s; timeout receipt exit -9 |
| Foreign session control | PID/PGID 73596 alive at nested receipt; only its own finally kills/reaps it, then absent |
| Automatic repeated caller SIGINT | Helper 73647 absent at 0.444s; two interrupts and first exception identity retained |
| Actual tmux Ctrl-C twice | Helper 73661 absent at 0.660s; two interrupts and first exception identity retained |
| Timeout cleanup interrupted | Helper 73678 absent at 0.315s; `helper_timeout` and original `TimeoutExpired` cause retained |
| Resume | New actual run_cli returns exact quoted Korean stdout; ResourceWarning 0 |

Runner PID 73542 / PGID 73540 exited; final output is `MANUAL_PASS` and `manual_exit=0`.
Prior input-timeout attempt remains recorded separately and is not counted as PASS.

## Nine adversarial classes

| Class | Concrete observable |
| --- | --- |
| Malformed argv/deadline | Empty argv, deadline 0/3601 fail before process/log creation; unchanged launcher guards pass |
| Harmless quoted literal | PIN and manual resume preserve quotes, `$()` punctuation, Korean text and trailing newlines exactly |
| Cancel/resume/repeated SIGINT | Both automatic and actual tmux caller interrupts occur twice; first helper exception preserved; next invocation succeeds |
| Stale/exited leader | Normal exit and SIGINT-exited leaders leave ready descendants in RED; GREEN requires PID and group absence; imported paths/hashes identify exact source |
| Dirty source/foreign PIDs | Other owners' files are untouched; independent session control survives settlement; mismatched SessionGroup representative refuses real SIGKILL |
| Hung SIGINT-ignoring child/bounded kill | 10s finite fixtures ignore SIGINT; launcher/helper groups vanish before successful result; injected delivery failure exits within fixed bounds and has exact-PID finally cleanup |
| First RED retained | Original 6-failure capture, fixture-corrected 7-failure RED, force-bound 2-failure RED, nested RED and final-boundary failure all retained; each rerun follows a documented code/driver correction |
| Misleading exit 0 | Normal leader result and exact stdout remain valid only after the descendant/group is absent; both launcher and helper normal/nonzero paths covered |
| Repeated interrupts during cleanup | Timeout cleanup keeps the original typed error/cause, caller cleanup keeps first KeyboardInterrupt, forced deadline is not reset, no final ResourceWarning |

N/A: remote/provider cancellation, actual image generation and profile installation are
outside this local fixture task. No runtime install or external application changes were made.

## Final cleanup and retained artifacts

Cleanup is restricted to the registered temporary root and named tmux session. The permanent
evidence directory retains PIN/RED/GREEN logs, source snapshots, final diff/hash binding,
manual runner/transcripts, and exact numeric PID/PGID verification. Completed cleanup receipts
are recorded in `fix-process/cleanup.txt`: all 95 distinct recorded fixture/runner PIDs and
66 recorded PGIDs were absent before removing the temporary tree. Owned tmux pane PID 47170
and sole-session server PID 47169 are absent; session `logopia-fix-process-080` and exact
`/tmp/logopia-fix-process-080` tree are absent. The resource checklist is fully reconciled.

`fix-process/pid-final-before-cleanup.jsonl` retains every available numeric receipt and the
final zero-signal absence query. Earlier replaced pytest basetemp receipts remain in their
original RED/GREEN transcripts, including bounded finally cleanup; the 95/66 totals describe
the final retained temporary files, not every process ever started by the suite. Numeric
probe subprocesses are handled by their exact Popen owners without a persistent watcher.

`fix-process/source-final.diff` records the two baseline-to-final native changes and the
four new source/test files; `source-final.sha256` exactly matches the independent reviewer
manifest. `source-native-audit.txt` records actual Python 3.11 parse success for all six files
and tokenized logical-line counts (maximum 140; each below 250). No source/test bytes changed
after final freeze. Artifact scanning found no dispatch capability, API-key or authorization
header strings; captured text contains only local harmless fixture input, OS values and paths.
