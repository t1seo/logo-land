# Owned process and installer checks

Scope: the coordinator-owned process wrapper and payload installer. This record does not claim a completed native logo workflow; that requires the separate real Hermes scenario.

## Failing-first evidence

Two baseline tests pinned the existing helper's behavior with an unrelated workflow sidecar and an unapproved imported PNG. Eight initial process tests and five installer tests passed before the repeated-interruption probe.

`test_second_interrupt_during_cleanup_still_reaps_child` then failed on the real subprocess path:

```text
Failed: A second interrupt escaped cleanup instead of settling the owned child
1 failed in 1.19s
```

The second interrupt escaped the grace-period wait. Including `KeyboardInterrupt` on the existing forced-stop path produced:

```text
16 passed in 2.93s
```

The initial probe also had a missing parent for its pytest basetemp; that fixture setup error was corrected before the captured RED. A test-only generic method annotation was subsequently corrected for Python 3.11 strict typing. Ruff passed; basedpyright reported zero errors, warnings or notes.

## Real terminal scenario

Registered an owned tmux session and temporary runner before starting them. The runner called the actual `run_process` with an isolated child that ignored SIGINT and slept for 30 seconds. Commands:

```sh
tmux send-keys -t logopia-process-qa 'PYTHONPATH=integrations/hermes uv run --locked python output/hermes-process-probe/manual.py' Enter
tmux send-keys -t logopia-process-qa C-c
tmux send-keys -t logopia-process-qa C-c
tmux capture-pane -p -S -60 -t logopia-process-qa
```

Captured observable (two Ctrl-C events, roughly 350 ms apart):

```json
{"interrupted":true,"exit_code":-9,"timed_out":false,"child_pid":20753,"child_absent":true}
```

PASS requires an interruption receipt, a nonzero exit and that exact owned child no longer existing. This does not establish cancellation of a remote image provider; interrupted native image outcomes remain unresolved in workflow state.

## Adversarial coverage

| Class | Observable or scoped reason |
| --- | --- |
| Malformed input | Default, traversal, whitespace and empty profile names rejected before launch. |
| Instruction-like input | The command builder passes a query file and workspace as literal argv; no shell interpolation. Full feedback/data handling belongs to host and launcher QA. |
| Cancel/resume | Actual two-interrupt process settled; log paths remain available. Workflow resume belongs to core QA. |
| Stale state | Reusing an existing log directory failed without replacing its sentinel. |
| Dirty worktree | Installer refused foreign/edited managed files, preserving them. Existing helper/artwork and unrelated drafts were not changed. |
| Long calls | Actual sleeping child exceeded its one-second deadline and was reaped. |
| Flaky tests | First failures retained; fixture and typing corrections disclosed. No model call was retried to turn a failure green. |
| Misleading success | Process receipt records exit/logs only. It is explicitly not proof of selected or approved artwork; launcher checks canonical state separately. |
| Repeated interruption | Actual repeated Ctrl-C and the focused failing-first grace-wait test both completed with owned children reaped. |

## Cleanup

The exact tmux session, temporary runner, manual-run directory, pytest basetemp directories and debug journal were removed after capture. Child PID 20753 and the tmux session were independently absent. The first force-flag cleanup command was rejected by automatic command review; the inventoried owned paths were then removed with ordinary recursive removal, without a force flag. The final process-only check passed nine tests in 2.09 seconds; a subsequent scan found no retained process-test fixture files in the default pytest root. Private red/green/terminal logs remain under ignored `output/hermes-process-probe/` as evidence; no server, listener, container or browser context was created. The intentional Hermes profile is unrelated to this sleeping-child probe.
