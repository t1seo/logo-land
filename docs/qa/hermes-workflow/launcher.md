# Launcher CLI verification

Worker: `task_97865c2354fe` / `ctx_f5ea00f8dc86`.
Scope: launcher entry point, request/preflight/result logic, profile serialization,
CLI tests and this report. No actual Hermes model/image calls or real profile writes.
Plan and binding contract G1–G6 read; shared engine/host/gallery APIs are reused.

## Result and integration seams

Implemented `studio.py`, `launcher.py`, `launcher_requests.py`, `launcher_state.py`,
`launcher_profile.py`, `launcher_runner.py`, `launcher_output.py`, `launcher_install.py`,
and the `test_launcher_cli*` / `test_launcher_request*` suites. Existing process,
installer, host, core, gallery, project metadata and unrelated work were preserved.

The CLI reuses `StartRequest` and `ActionRequest`; it does not define another request
schema. UTF-8 files are capped at 32 KiB, parsed as one exact JSON value, and reject
duplicate keys, non-finite constants, extra fields and coerced revisions. The original
JSON, including user strings, is carried verbatim inside a labelled query file.

`run` reads the installed `HostSettings`, checks saved revision/candidate hash before
starting Hermes and never substitutes a new revision. `Studio.status` validates
actual durable state and originals. Success additionally requires the requested
production, selection, child/feedback or delivery postcondition. Production must
preserve the previous selection; a prose success or exit 0 with no saved result fails.
`run` with a status request, `show` and `gallery` make no Hermes call. `NoInferenceHost`
cannot plan, generate or critique. Installation uses only copy, doctor and enable.

The runner calls the existing `hermes_command` / `run_process`, with a default
1800-second deadline and 10-second grace. Only after the owned process settles may it
call `Studio.interrupt` on the observed saved revision. Unknown calls remain unknown;
the launcher neither retries them nor claims that a provider request was cancelled.
Errors retain a fresh gallery when state exists and point to the exact process logs.
Normal output is a short summary and gallery path; `--json` exposes a small receipt.

Each install/run holds a per-profile `fcntl.flock` across its owned process lifetime.
This supports macOS/Linux local filesystems. The kernel releases the lock when its
owner exits. `.logopia-launch.lock` intentionally remains: unlinking it would allow
different inodes to be locked concurrently. Workflow locks are separate and short.
This serializes this CLI's launches; it does not claim control over independently
started Hermes sessions.

## Exact CLI syntax

Options follow their command; there are no global workspace/profile options.

```sh
uv run --locked python integrations/hermes/studio.py --help
uv run --locked python integrations/hermes/studio.py install --profile logopia --workspace PATH
uv run --locked python integrations/hermes/studio.py run --profile logopia --request FILE --timeout 1800
uv run --locked python integrations/hermes/studio.py show --workflow ID --workspace PATH
uv run --locked python integrations/hermes/studio.py gallery --workflow ID --workspace PATH --output FRESH_FOLDER
```

`--workspace` is optional: install/show/gallery use the current directory, while run
uses installed settings and rejects a conflicting explicit workspace. Install/run
require a pre-created nondefault named profile. Normally its exact path is
`~/.hermes/profiles/NAME`. A custom `HERMES_HOME` requires an explicit matching
`--profile-home /absolute/root/profiles/NAME`; profile routing is never guessed.
No profile is created, selected globally or given different model/auth settings.
Every command also accepts `--json`. Successful receipts go to stdout; application
error receipts go to stderr with exit 1. Usage errors retain the CLI's normal help.

Captured `run --help`:

```text
Usage: studio.py run [OPTIONS]

  Submit one validated request and verify its saved result.

Options:
  --profile <str>        Existing nondefault Hermes profile, e.g. logopia.
                         [required]
  --request <path>       Exact StartRequest or ActionRequest JSON, at most 32
                         KiB.  [required]
  --timeout <int range>  Owned Hermes deadline in seconds; grace is 10
                         seconds.  [default: 1800; 1<=x<=3600]
  --workspace <path>     Workspace; run must match installed settings.
  --profile-home <path>  Exact absolute profiles/NAME for custom HERMES_HOME.
  --json                 Print a small machine-readable command receipt.
  --help                 Show this message and exit.
```

Installer argv after the managed copy is exactly profile-specific:

```text
hermes -p NAME plugins doctor /absolute/profile/plugins/logopia-studio --ci
hermes -p NAME plugins enable logopia-studio --no-allow-tool-override
```

The plugin source is the repository's `integrations/hermes`; `helper_repo` is its
repository root. Existing foreign/modified installations and output folders are
preserved. Doctor failure prevents enablement and reports the retained logs.

## Resources registered before creation

- `output/hermes-launcher-qa/`: this worker's raw RED/GREEN/check/tmux logs and explicit
  pytest basetemps; evidence is transcribed below before removing this owned directory.
- Pytest fixture directories: `tmp_path` owns profile, workspace, fake Hermes executable,
  invocation receipts and process logs. The final fixture uses `TemporaryDirectory`
  under `tmp_path`, so assertion failures also remove its payload. Subprocess contexts
  reap owned children; initial pytest-managed temporary roots are not globally deleted.
- `output/hermes-launcher-scenario.py`: temporary labelled fixture driver; remove after QA.
- Scenario `TemporaryDirectory(prefix="logopia-launcher-")`: isolate profiles and workspace;
  context manager removes them after verifying no model calls or foreign-file mutation.
- tmux `logopia-hermes-launcher`: create only if absent; capture, then kill that session only.
- No debugger, listener, browser, global environment change, or sub-worker is required.
- The root `.debug-journal.md` belongs to the coordinator and is preserved.

## Baseline

PIN2 tests were reported passing by the coordinator. A concurrent baseline invocation
observed `1 failed, 15 passed in 3.12s`: the coordinator's newly added
`test_second_interrupt_during_cleanup_still_reaps_child` is currently RED and outside
this worker's ownership. Existing helper/installer and original process cases passed.

## Runtime hypotheses and checks

1. Exit 0/prose could falsely imply a produced workflow: a fake Hermes process prints
   success without writing any state; require a missing-state/postcondition error.
2. Stale feedback could dispatch inference: use the exact saved revision/hash and
   assert no fake Hermes invocation receipt is created on preflight failure.
3. Parallel CLI processes could mutate one Hermes profile: hold its actual POSIX flock,
   run a second CLI, and require an immediate busy error with no dispatch.

## RED and GREEN evidence

First actual-entry-point RED, before implementation:

```text
FFFFFFF                                                                  [100%]
test_help_lists_usable_commands_when_cli_is_invoked
>       assert result.returncode == 0, result.stderr
E       assert 2 == 0
7 failed in 0.17s
```

The subprocess error identified the missing `integrations/hermes/studio.py` entry
point. The first GREEN was `16 passed in 3.47s`.

Additional adversarial RED preserved before the selection fix:

```text
E       Failed: DID NOT RAISE LaunchError
FAILED tests/hermes/test_launcher_request_state.py::test_start_rejects_unrequested_selection
FAILED tests/hermes/test_launcher_request_state.py::test_continue_preserves_prior_selection
2 failed, 3 passed in 5.25s
```

Machine-readable boundary errors were also added failing-first:

```text
FAILED tests/hermes/test_launcher_request.py::test_json_error_is_machine_readable
1 failed in 0.20s
```

The final automated commands use the locked repository environment:

```sh
uv run --locked pytest -q tests/hermes/test_launcher_cli*.py tests/hermes/test_launcher_request*.py
uv run --locked pytest -q tests/hermes/test_launcher_process.py
```

Captured final suite and process output:

```text
49 passed in 20.06s
9 passed in 2.08s
All checks passed!
0 errors, 0 warnings, 0 notes
```

Targeted `ruff check --target-version py311` and `basedpyright --pythonversion 3.11`
cover all eight production entry/launcher modules and all ten owned test modules.
The programming checker reports `no violations in 18 file(s)`. The largest production
module is 161 logical lines, below the 250-line ceiling; all owned tests are also below it.

The installed Hermes interpreter is Python 3.11.16. Its actual import probe returned:

```text
3.11.16
native request/runner/profile/state imports OK; Hermes runtime modules: 0
```

Hermes's existing environment does not include Typer. It was not changed. The CLI
uses the repository's existing Typer dependency or its declared PEP 723 dependencies;
`uv run --python <Hermes Python3.11 interpreter> --script integrations/hermes/studio.py --help`
completed successfully in a separate uv-managed environment. This is distinct from
the actual Hermes interpreter's successful import of the native runner modules.

Actual invalid/missing profile invocations returned exit 1 before any installation:

```text
Use a named profile such as logopia
Error: invalid_profile
Create it first: hermes profile create logopia-launcher-absent-97865
Error: missing_profile
```

## Manual tmux evidence

The owned session was `logopia-hermes-launcher`. Commands were sent using the required
surface, then captured with `tmux capture-pane -p -t logopia-hermes-launcher -S -200`:

```sh
tmux send-keys -t logopia-hermes-launcher 'uv run --locked python integrations/hermes/studio.py --help' Enter
tmux send-keys -t logopia-hermes-launcher 'uv run --locked python output/hermes-launcher-scenario.py; tmux wait-for -S logopia-launcher-scenario-done' Enter
```

The temporary driver uses the same CLI with a PATH-local fake `hermes`, separate
profile and workspace, actual core/helper/gallery operations and labelled deterministic
PNG fixtures. These images are test fixtures, not evidence of provider image generation.

Two concrete fixture defects were corrected, without changing production code:
the driver initially passed macOS `/var` instead of its resolved `/private/var` root
to the core Store (`unsafe_path: Path escapes the workspace`); then the test host
reused critique IDs across separate fake CLI processes. The latter was first locked
by this regression output before the fixture began assigning unique per-call IDs:

```text
invalid_report: Critique call identity was already used
Workflow: fixture-logo | revision 18 | failed | 2 original(s)
FAILED tests/hermes/test_launcher_cli_feedback.py::test_revision_across_cli_processes_preserves_parent_and_saves_reviewed_child
1 failed in 2.66s
```

Relevant final tmux output, with transient gallery/log path lines omitted:

```text
LABELLED FIXTURE: deterministic test images; zero actual Hermes/model calls.
FIXTURE install | exit=0
Logopia installed, doctor checked and enabled in the named profile
FIXTURE produce saved original | exit=0
Requested result verified in saved state
Workflow: fixture-logo | revision 11 | awaiting_choice | 1 original(s)
FIXTURE show saved state | exit=0
Saved workflow
Workflow: fixture-logo | revision 11 | awaiting_choice | 1 original(s)
FIXTURE fresh gallery | exit=0
Saved workflow
Workflow: fixture-logo | revision 11 | awaiting_choice | 1 original(s)
FIXTURE CHECK: install/show/gallery added zero fixture image calls.
FIXTURE stale revision refused | exit=1
Expected 10; saved 11
Error: stale_revision
FIXTURE targeted fixture child | exit=0
Requested result verified in saved state
Workflow: fixture-logo | revision 19 | awaiting_choice | 2 original(s)
FIXTURE misleading successful prose refused | exit=1
Hermes returned without saving the requested workflow
Error: workflow_missing
FIXTURE owned deadline | exit=1
Owned Hermes deadline reached; provider outcome may be unknown
Workflow: paused | revision 2 | outcome_unknown | 0 original(s)
Error: run_timed_out
FIXTURE unknown outcome cannot resubmit | exit=1
Inspect saved state; do not resubmit an unresolved request
Error: outcome_unknown
FIXTURE saved unknown state | exit=0
Saved workflow
Workflow: paused | revision 2 | outcome_unknown | 0 original(s)
FIXTURE CHECK: parent preserved; unknown not resubmitted; default config preserved.
FIXTURE PASS: temporary profiles, workspace, fake executable and logs removed.
```

## Adversarial and review coverage

| Class | Evidence / boundary |
| --- | --- |
| Malformed, oversized, instruction-like input | Exact JSON parser tests cover duplicate keys, extra data, code fences, NaN, UTF-8, coerced/bool revisions, and the exact 32768-byte limit. Actual query and argv are compared; shell-like notes create no file. |
| Stale revision/hash | Real saved states reject stale feedback before any fake Hermes invocation. No revision refresh. |
| Cancellation/resume/unknown | Actual one-second owned deadline settles the fake process, retains its reserved job as unknown and rejects subsequent submission; read-only status still works. |
| Missing workflow/misleading success | Exit 0 and successful prose with missing state or unchanged draft return explicit failure; selected ID/child/delivery postconditions are checked. |
| Shared profile memory | A held POSIX lock rejects a second actual CLI; abrupt owner exit proves kernel lock release. Lock symlinks preserve their foreign target. |
| Dirty profile/output | Unmanaged plugin, profile config and existing gallery output are preserved; conflicting workspace configuration is rejected. |
| Repeated interruptions | Coordinator-owned process regression now passes, including its second interrupt cleanup case; no process implementation was edited here. |
| Flaky reruns | No blind retries. RED cases are tied to a specific missing behavior or a diagnosed fixture defect before rerunning. |
| Native provider calls/cancellation | Not performed by this worker; coordinator T3 owns real inference. Local process termination does not prove provider cancellation. |
| Core import/export crash reconciliation | Core-owned recovery tests; launcher passes the exact action/job and refuses blind unknown retries. No shadow recovery implementation was added. |
| Browser/visual quality | Gallery worker and coordinator own browser QA and real-image review; this task verifies fresh HTML publication and paths through the CLI. |

The review-work skill's goal, code, security, QA and context criteria were checked
locally. The task explicitly prohibited agents, so no independent-agent review is
claimed. Coordinator T5 remains the separate integrated review stage.

## Teardown and remaining work

The three manual `TemporaryDirectory` profiles/workspaces were removed by their
contexts, including both failed fixture attempts. All three exact paths were checked
absent. The owned raw evidence directory/basetemps and temporary script were removed
after transcription; the owned tmux session was killed and confirmed absent.

```text
Removed owned scenario script and QA logs/basetemps; all three manual temporary roots absent.
Owned fixture Python processes: 0; temporary script/log directory absent.
tmux has-session -t logopia-hermes-launcher: exit 1 (no server running)
```

No real profile, provider, model/auth configuration, unrelated process or foreign
output was modified by this worker. No subagents or commits were created. The shared
worktree includes coordinator/other-worker edits to README, pyproject and the native
integration; those edits were preserved. Implementation, automated checks, manual QA
and owned-resource teardown are complete. Real generation and integrated release
remain coordinator-owned.
