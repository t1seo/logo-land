# Integrated repeated-interrupt process follow-up

Owner: task `task_b2eaf12f12ba`, dispatch `ctx_1624d2deb018`.
Only the four previously owned process modules, two process tests, this report and
`fix-process-integration/` evidence may change. Other owners' files, root journal,
installer/profile, native originals and unrelated drafts are outside this task.

Result: the confirmed poll acquisition race is fixed. Scoped tests pass 39 cases,
the independent reviewer passes 6 original/targeted cases, and actual tmux QA passes
with the original interrupt object, all helpers reaped, exact resumed stdout and no
ResourceWarning. All registered temporary resources have been removed and verified.
Unqualified artifact filenames below refer to `fix-process-integration/` beside this report.

## Plan and hypotheses

1. COMPLETE: original full failure and matching six-file source PIN retained; unaffected PIN 12 pass.
2. COMPLETE: real SIGINT at lock acquisition produces a held lock and zombie on both runtimes;
   actual run_cli regression is RED before production changes.
3. COMPLETE: bounded shared interrupt deferral fixes the acquisition race without changing limits.
4. COMPLETE: scoped 39 pass, strict checks pass, independent 6 pass and actual tmux QA PASS.
5. COMPLETE: final source hashes verified; owned scratch, tmux and all recorded PIDs/PGIDs absent.

- H1: SIGINT interrupts CPython's nonblocking Popen poll between lock acquisition and its
  protected release region, leaving poll permanently unable to reap the child.
- H2: SIGINT interrupts after OS waitpid consumes exit status but before Popen stores it;
  a gone PID and stale `returncode=None` differ from a live group.
- H3: a live owned group or incomplete force-signal bookkeeping prevents settlement;
  distinguish actual PID/PGID/stat, wait/reap state and signal boundary from Popen state.
- H4: fixture teardown, stale imports/runtime or an unrelated color test creates the
  warning; compare exact PID, source manifest, runtime and destruction timing.

## Resource register (before creation)

- [x] Permanent `fix-process-integration/` directory for sanitized evidence; retain.
- [x] `/tmp/logopia-fix-process-integration-080` exact temporary root; remove when complete.
- [x] `/tmp/logopia-fix-process-integration-080/pin` PIN pytest basetemp; remove with root.
- [x] `/tmp/logopia-fix-process-integration-080/probe.py` deterministic boundary probe;
  preserve text in evidence then remove.
- [x] `/tmp/logopia-fix-process-integration-080/probe` finite probe receipt directory;
  each child records PID/PGID before any action, 10s alarm, exact-PID kill/wait in finally.
- [x] Probe runner SIGALRM watchdog (20s) and signal/trace hooks; restore all in finally.
- [x] `/tmp/logopia-fix-process-integration-080/red` targeted regression basetemp;
  finite fixtures and exact PID/PGID receipts, bounded finally cleanup even on RED.
- [x] `/tmp/logopia-fix-process-integration-080/pytest` final scoped basetemp;
  same existing finite fixture ownership and cleanup contracts.
- [x] `/tmp/logopia-fix-process-integration-080/manual.py` finite actual run_cli tmux driver;
  preserve text before removing.
- [x] `/tmp/logopia-fix-process-integration-080/manual` runner/ready/child receipts;
  child alarm 10s, driver watchdog, bounded caller interrupt and finally cleanup.
- [x] Manual `terminal`, `resume` and `thread` cases: record every Popen PID/PGID immediately
  after creation, finite child alarms, captured Popen owner and bounded kill/wait finally.
- [x] Manual readiness notifier and worker-context thread: bounded joins, no persistent watcher;
  SIGINT/SIGALRM handlers and temporary Popen capture patch restored in finally.
- [x] tmux session `logopia-process-integration-080`, pane `:0.0`; record exact pane/server
  PIDs before use, close only named session and verify owned PIDs absent.
- [x] `/tmp/logopia-fix-process-integration-080/tmux-pids.txt` exact tmux ownership receipt.
- [x] Numeric OS observation commands use `/bin/ps -p <recorded IDs>` only, 2s deadline;
  no process-name scans, unowned signals or broad process termination.

## Initial failure evidence

The original `output/hermes-final-checks/pytest.txt` reports 2 failures and 954 passes.
`run_cli` first receives `KeyboardInterrupt: caller interrupt 1`, then its settlement loop
expires after 12 seconds with Popen returncode still None. Fixture finally reports PID/PGID
78509 absent. Later, during a color test, Popen destruction reports ResourceWarning for
the same PID 78509; this identifies delayed helper cleanup state, not a color assertion.
This trace alone does not establish which reap/lock boundary was interrupted.

All fixtures are local and harmless; no model/provider/image calls or actual profile changes.
Existing coordinator-owned review is used; no nested workers will be created.

## Confirmed boundary and first results

`pin.txt`: unchanged launcher/stdout/typed-error behavior, 12 passed, 7 deselected in 2.34s.
`probe-py312.txt`: without boundary interrupt, PID 93473 reaped with -9 and lock false;
with a real SIGINT immediately after lock acquisition, PID 93479 remains Z, returncode null,
lock true and TimeoutExpired at 0.154s. `probe-py311.txt` gives the same distinction:
control PID 93472 settled, injected PID 93476 Z/null/locked and TimeoutExpired at 0.156s.
Every probe restores its own original lock before exact kill/wait, records absence and
ResourceWarning 0. Instrumentation is confined to the harmless fixture, not production.

The targeted existing repeated-interrupt test adds one acquisition-boundary parameter.
`red-acquisition.txt`: 1 failed / 1 passed before native edits; PID 97297 is Z with the
same original KeyboardInterrupt followed by forced TimeoutExpired, then safely reaped in
finally. Its forced budget is shortened only in the fixture to preserve a finite fast RED.
All existing original-error, absence, warning and elapsed assertions are retained.

`green-acquisition-first.txt`: both cases pass; PID 99264 absent at 0.130s before fixture
cleanup, returncode recorded and acquisition lock released. `green-scoped.txt`: final
required five-file suite, 39 passed in 29.43s. Native Python 3.11 basedpyright, repository
test typing and no-excuses checks pass. The first native type check found untyped fields
on TimeoutExpired; final code keeps that exact exception and updates only its public
timeout field to the original invocation budget, without copying unknown payloads.

After the fix, unchanged probes also pass under both real interpreters:
`probe-py312-green.txt` PID 2161 absent/code -9/lock false at 0.027s;
`probe-py311-green.txt` PID 2157 absent/code -9/lock false at 0.047s.
This confirms the acquisition mechanism. The historical full-suite trace does not record
the second interrupt's exact instruction, so it is supporting symptom evidence rather
than a retrospective instruction-level capture.

The shared guard invokes the original callable SIGINT handler, retains its KeyboardInterrupt
object, and restores the handler before propagation. It operates only in the main thread;
other thread calls and non-callable SIGINT policies pass through unchanged. Wait/communicate
use at most 0.1s protected slices under one original absolute deadline; cleanup poll and
the existing at-most-0.25s exact probe reap are protected too. No private Popen state is
changed in production, no warnings are suppressed, and no grace or force budget is widened.

## Verification commands and binding

```sh
uv run --locked pytest -q tests/hermes/test_launcher_process.py tests/hermes/test_process_group_settlement.py tests/hermes/test_helper_interrupt.py tests/hermes/test_helper_bridge.py tests/hermes/test_helper_recovery.py --basetemp /tmp/logopia-fix-process-integration-080/pytest
uv run --locked basedpyright --pythonversion 3.11 integrations/hermes/logopia_studio/launcher_process.py integrations/hermes/logopia_studio/helper_process.py integrations/hermes/logopia_studio/process_group.py integrations/hermes/logopia_studio/process_scope.py
uv run --locked basedpyright tests/hermes/test_process_group_settlement.py tests/hermes/test_helper_interrupt.py
```

- `green-scoped.txt`: **39 passed in 29.43s**, including all original malformed-input,
  output, timeout, descendant, nested-helper, foreign-session and OS-denial assertions.
- `types-native-final.txt`, `types-tests.txt`, `types-drivers.txt`: zero errors/warnings.
- `ruff-final.txt`, `format-final.txt`, `no-excuses.txt`: all checks pass; six files already
  formatted and no forbidden type escape or logical-size violation.
- `native-311-parse.txt`: all six frozen source/test files parse with actual Python 3.11.
  The common settlement/interrupt code was executed under real 3.11.16 and locked 3.12.12;
  actual run_cli, pytest and manual thread cases used the repository's locked 3.12.12 runtime.
- `source-frozen.sha256`: exact four native module and two test hashes;
  `source-frozen.diff`: changes relative to this dispatch's original full-suite source PIN.
  `test_process_group_settlement.py` remains byte-for-byte unchanged; the helper test adds
  one parameterized acquisition regression while preserving the original case/assertions.
- SOURCE_FROZEN `msg_00b55b48aada` was sent after scoped/static verification so the
  coordinator could run full integration in parallel. No production/test bytes changed
  afterward; only this report and evidence were completed.

This worker did not repeat the full 956-case suite, change installer/profile metadata,
install dependencies or invoke model/image/provider operations. The existing installer
already includes the same four process modules; there is no new module to include.

## Independent verification

Reviewer dispatch `ctx_c84701fbe9de`, message `msg_66bc76d7a3c7`, verified the frozen
hashes before/after execution and actual Python 3.11 parsing. Its
`review-code/settled-tests.txt` and `review-code/settled-receipt.json` show
**6 passed in 5.45s, exit 0**: unchanged descendant/helper/installer-boundary/nested probes
plus original and acquisition-injected repeated-interrupt cases.

Descendant 6089, helper 6251, nested helper 6259 and repeated helpers 6432/6442 were absent
at result time. Original repeated interruption completed at 0.432s and injected acquisition
at 0.114s, preserving the first KeyboardInterrupt identity and warning/group expectations.
The unrelated installer probe is reviewer-owned coverage; this worker did not change it.

## Actual tmux QA

Registered session `logopia-process-integration-080:0.0`, script
`/tmp/logopia-fix-process-integration-080/manual.py`. The exact channel was used:

```sh
tmux send-keys -t logopia-process-integration-080:0.0 'uv run --locked python /tmp/logopia-fix-process-integration-080/manual.py' Enter
tmux send-keys -t logopia-process-integration-080:0.0 C-c
tmux send-keys -t logopia-process-integration-080:0.0 C-c
tmux capture-pane -p -S -200 -t logopia-process-integration-080:0.0 > docs/qa/hermes-workflow/fix-process-integration/manual.txt
```

A bounded outer driver waited for the child readiness marker, then sent the first Ctrl-C
after 0.1s and the second after 0.4s. The actual manual driver PID 6226 reports:

| Scenario | Exact observation |
| --- | --- |
| Two real terminal interrupts | helper PID/PGID 6227 absent and Popen reaped at 0.575s; original exception object preserved; handler count 2 |
| Resume and multiple communicate slices | helper 6244 returns exact quoted Korean/CRLF-normalized stdout at 0.326s, spanning more than one 0.1s wait slice |
| Native worker-thread call context | helper 6258 returns the same exact output at 0.328s; no main-thread-only signal API error and original main handler unchanged |
| Final receipt | three helpers absent and reaped; `MANUAL_PASS`, `resource_warnings: 0`, `manual_exit=0` |

`manual.txt` retains the required capture after removing unrelated shell startup information;
`manual-joined.txt` joins wrapped terminal lines. The same run is preserved as `manual.py.txt`.
`manual-capture-first-error.txt` records an outer automation assertion: the echoed exit-code
command satisfied an overly early capture condition before its output. The finally capture
already contains actual manual exit 0. Reading that same pane confirmed it; no manual-driver
rerun, test relaxation or source edit was used to obtain the PASS.

## Nine adversarial classes

| Class | Applicable evidence |
| --- | --- |
| Malformed arguments/existing fixtures | Unchanged launcher guards and existing fixture cases pass in scoped 39 |
| Inert shell punctuation | PIN exact stdout/nonzero error tests; actual resumed quoted Korean text and CRLF behavior preserved across wait slices |
| Cancel/resume | Actual Ctrl-C twice preserves first exception; subsequent actual run_cli succeeds |
| Stale completed leader | Existing normal/nonzero exited-leader descendant tests remain unchanged and pass |
| Dirty source pins | Six initial hashes match the failed full-suite manifest; final frozen hashes match before/after independent review and cleanup; other owners' files untouched |
| Deadline/OS rejection | Original global invocation/grace/force budgets remain; existing denied-signal and typed inspection-failure tests pass without assertion changes |
| Actual intermittent failure | Deterministic real SIGINT at successful acquisition reproduces Z/null/locked/timeout on both runtimes; toggling that boundary and applying the fix changes the outcome; first full failure and first RED retained |
| Misleading gone PID/unreaped state | Original delayed ResourceWarning is tied to PID 78509; regression requires actual Popen returncode and released lock before fixture cleanup, plus PID/PGID absence; no fabricated success status |
| Repeated interrupts | Original automatic and new acquisition cases plus actual terminal interrupts pass; original object and handler restored; final ResourceWarning count zero |

Unrelated gallery/native logo behavior, remote cancellation and provider outcomes are N/A
for this local process race. No new native logo/profile/provider action was performed.

## Cleanup and final scope

`pid-final.jsonl` records exact receipt-based checks, including earlier targeted-run IDs
whose pytest basetemp was later replaced. All **43 recorded owned PIDs and 31 PGIDs** are
absent. `cleanup.txt` confirms named tmux session removal, pane PID 6103 and exclusive
server PID 6102 absent, and exact `/tmp/logopia-fix-process-integration-080` tree absent.
Only recorded numeric IDs were observed; no unowned process was signalled.

All scoped evidence remains in this directory. There are no pending fixture processes,
threads, signal hooks, named temporary files or worker-owned tmux sessions. Source hashes
remain frozen; integration/full-suite execution and native profile refresh are coordinator-owned.
