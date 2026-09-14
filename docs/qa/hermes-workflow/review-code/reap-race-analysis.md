# Independent reaping-race source inspection

Root's actual `output/hermes-final-checks/pytest.txt` ends with **2 failed, 954 passed in 309.89s**. Both failures identify helper PID 78509: its repeated-interruption case raised `TimeoutExpired` after the 12-second settlement limit with `Popen.returncode=None`; the later color test received that same Popen object's delayed `ResourceWarning`. The latter is not a failed color assertion. The fixture's final cleanup receipt reports the PID absent and its group nonexistent. This is root-executed evidence, read independently, not a fresh reviewer execution.

Three explanations were considered:

1. A waitpid bookkeeping lock remains acquired after asynchronous interruption. The actual CPython 3.12 and native 3.11 `_internal_poll` acquire `_waitpid_lock` before entering their `try/finally`. A signal in that gap could cause all later polls to return `None` and eventually produce the reported delayed Popen warning. This is a plausible source-level mechanism, not proof of the exact timing in root's run.
2. An owned process/group continues running despite attempted termination. Final absence alone is insufficient to reconstruct its state at the timeout, because fixture cleanup follows the exception. The child's ten-second alarm and the twelve-second failure make the bookkeeping hypothesis worth isolating, but do not substitute for a deterministic probe.
3. A separate color regression or unrelated object's delayed warning. The exact same PID in the two tracebacks contradicts that interpretation; the color assertion itself is not the observed failure.

Read the installed stdlib sources directly: CPython 3.11.16 and 3.12 `subprocess.py`, `_internal_poll` lines 1973–2005, `_wait(timeout)` lines 2021–2061 and `send_signal`/`kill` around lines 2178–2225. Both `_internal_poll` and finite `_wait` have acquisition-before-try windows; `kill` also calls `poll` internally. Accordingly, final review must consider the launcher's initial wait and the numeric query's shutdown as well as the settlement loop. No proposal was made to block SIGINT for a long command or to infer a successful exit merely from group absence.

The production/stdlib pin is [reap-race-source.sha256](reap-race-source.sha256). No source edits, runtime private-lock mutation, new fixture, inference or process kill were performed by this reviewer. Root's follow-up process owner `ctx_1624d2deb018` owns the deterministic PIN/RED/GREEN and source fix. Findings were sent through Orca messages `msg_5b16d513a209`, `msg_8bebcf1205e9` and `msg_ccf3323867cb`; final reruns await `SOURCE_FROZEN`.

## Owner's deterministic RED, independently read

Message `msg_c6ca76039d83` supplied real-SIGINT control/toggle results on both runtimes. This reviewer read the complete registered `probe.py`: it substitutes an otherwise ordinary acquire/release lock on the one owned Popen object, emits one actual SIGINT immediately after successful acquisition, and restores the original lock before exact child kill/wait cleanup. The unchanged control settles with exit -9 and unlocked state. Injection yields a zombie PID, `returncode=null`, a held poll lock and `TimeoutExpired` in 0.154s (3.12) / 0.156s (3.11); both exact PIDs are then reaped and absent. No warnings remain after fixture cleanup. [3.12 owner receipt](../fix-process-integration/probe-py312.txt), [3.11 owner receipt](../fix-process-integration/probe-py311.txt).

This isolates H1 as a reproducible defect in both actual runtimes. It does not retroactively expose the precise instruction at which the original integration run received its second interrupt. Production was still unchanged when these owner receipts were produced; source remediation and final unchanged independent reruns remain pending.

## Resolution

The frozen shared guard protects short poll/wait/communicate/query operations, restores the original callable SIGINT handler and propagates its original KeyboardInterrupt object; it bypasses signal-handler changes outside the main thread. This reviewer fully read the four-module correction and independently ran the unchanged four original boundary cases plus both original/injected repeated-interruption variants: 6 passed in 5.45s, with recorded exit status, unlocked/reaped children and no warnings. Root subsequently completed 957 tests successfully and issued FIXES_READY. See [final independent report](../review-code.md) for exact commands, hashes, installed binding and actual cleanup receipts. The race finding is resolved; its original RED evidence remains intact.
