# Named-profile native tool deadlines and truthful settlement

Dispatch: `task_45e51da98f39` / `ctx_e06374c7e7c7`.

Scope: launcher installation, settlement reasons, and the public core predicate for explicit critique-only continuation. Runtime source and the live/default Hermes profiles remain read-only; no model or image provider is called.

## Resource ledger (registered before creation)

| Owned resource | Purpose | Teardown |
| --- | --- | --- |
| `output/hermes-timeout-qa/` | PIN, first RED, GREEN, static-check and tmux captures; pytest basetemps | Transcribe evidence here, then remove this exact directory |
| `output/hermes-timeout-scenario.py` | Labelled manual scenario | Remove after capture |
| `logopia-timeout-qa` tmux session | Required manual CLI channel | Create only if absent; kill only this owned session after capture |
| `TemporaryDirectory(prefix="logopia-timeout-")` | Fake binary, named fixture profiles, native-resolver homes | Context-manager cleanup, including on assertion failure |
| Pytest `launcher-*` fixture directories under the owned basetemp | Real CLI subprocess fixtures | Fixture context cleanup, then remove owned basetemp |
| Child CLI/fake/resolver processes | Bounded command execution | Synchronous subprocess completion with finite deadlines; verify no surviving scenario child |

Original evidence `output/hermes-demo/start-result.json` and session `20260915_005825_705e1e` are coordinator-owned and remain untouched. At initial inspection the result file was zero bytes; it is not used as evidence of a successful operation.

## Result and integration seams

The installer now runs these four public commands, in order, under the existing named-profile kernel lock:

```text
hermes -p logopia plugins doctor <installed-plugin> --ci
hermes -p logopia config set timeouts.tools.sequential_call 1800
hermes -p logopia config set timeouts.tools.concurrent_batch 1800
hermes -p logopia plugins enable logopia-studio --no-allow-tool-override
```

Each command retains the existing 120-second owned process deadline and process-helper grace. The two native executor limits are finite 1800-second profile settings; the independent run deadline remains 1800 seconds by default. Configuration is delegated to the public CLI, without loading the Hermes runtime into the launcher or rewriting model/auth configuration. A failed first or second setting returns `sequential_call_failed` or `concurrent_batch_failed`, names the exact setting, retains process logs and stops before subsequent commands. Earlier completed steps remain; installation is not an atomic config transaction.

Successful installation plainly prints:

```text
Logopia installed, doctor checked and enabled in named profile logopia.
timeouts.tools.sequential_call=1800 seconds
timeouts.tools.concurrent_batch=1800 seconds
Plugin: <named-profile>/plugins/logopia-studio
```

`launcher_runner._settled_state` runs only after `run_process` returns. It records the observed cause separately:

| Process evidence | Durable reason |
| --- | --- |
| Owned deadline flag | `Owned Hermes process settled after its deadline` |
| Owned interruption flag | `Owned Hermes process settled after an interruption` |
| Exit with reserved/returned work | `Owned Hermes process exited with unfinished operation (exit code N)` |

All three retain the statement that provider cancellation is unconfirmed. Exit 0 with unfinished work becomes `outcome_unknown`; successful prose cannot create a successful workflow receipt. The actual provider/native cause of an ordinary unfinished exit is not inferred.

The coordinator additionally requested the G7 recovery seam. `launcher_state` uses the core's public `engine_recovery.can_resume_critique(state)` only for explicit `ContinueRequest`, after exact revision validation. It uses `engine_jobs.unresolved_jobs(state)` for canonical pending-job checks, so a validated `retry_of` link can resolve old unknown critique history. Tests exercise actual CLI review continuation with zero new fixture image/planning calls, preserved image hash and original 420-second error/raw report, then local choose/revise/deliver preflight. Unknown plan/image/edit/delivery, exhausted unknown review attempts, stale continuation and start/choose/deliver on the unresolved review remain no-call errors; status stays read-only. Core retry eligibility, retry-link validation, late-return handling and budgets remain core-owned.

## Exact CLI syntax and help

```sh
uv run --locked python integrations/hermes/studio.py --help
uv run --locked python integrations/hermes/studio.py install --profile logopia --workspace PATH
uv run --locked python integrations/hermes/studio.py run --profile logopia --request FILE --timeout 1800
uv run --locked python integrations/hermes/studio.py show --workflow ID --workspace PATH
uv run --locked python integrations/hermes/studio.py gallery --workflow ID --workspace PATH --output FRESH_FOLDER
```

Options follow the command. Every command supports `--json`; success goes to stdout and application errors to stderr. The profile must already exist at `~/.hermes/profiles/<validated-nondefault-name>`. A custom `HERMES_HOME` requires matching `--profile-home /absolute/root/profiles/NAME`; the launcher never guesses or installs into the default profile. `--workspace` defaults and platform scope remain as documented in [launcher.md](launcher.md): install/show/gallery use the current directory, run uses installed settings, and the profile lock supports macOS/Linux via `fcntl`.

Captured install help:

```text
Usage: studio.py install [OPTIONS]

  Copy, doctor and enable the plugin without any model calls.

Options:
  --profile <str>        Existing nondefault Hermes profile, e.g. logopia.
                         [required]
  --workspace <path>     Workspace; run must match installed settings.
  --profile-home <path>  Exact absolute profiles/NAME for custom HERMES_HOME.
  --json                 Print a small machine-readable command receipt.
  --help                 Show this message and exit.
```

The coordinator owns actual profile installation and any further native generation/review. This worker did neither.

## Original failure and runtime evidence

Read-only original output remains at `output/logopia-runs/offcut-hermes-demo-4c4d395ab32b41f3a30fd778f12d3633/process/stdout.txt`:

```text
Warning: Unknown toolsets: logopia-studio
The Logopia workflow timed out after 420 seconds. Stopped without retrying, as requested.
```

The actual session is `20260915_005825_705e1e`. The coordinator reported three saved originals, two critique pairs and one unknown final critique. Those originals were not regenerated or modified here. The empty `output/hermes-demo/start-result.json` was not treated as success.

The investigation distinguished three hypotheses: an owned launcher deadline, an independent native executor deadline, and misleading successful process/prose evidence. Installed source confirmed the second: `/Users/cillian/.hermes/hermes-agent/agent/tool_executor.py` has `_DEFAULT_CONCURRENT_TOOL_TIMEOUT_S = 420.0`, resolves `tools.concurrent_batch` through `agent.deadline.resolve_timeout`, and resolves `tools.sequential_call` with the concurrent value as fallback. The public resolver reads `timeouts` from the active profile config. No per-tool timeout override or runtime patch was introduced.

`test_launcher_cli_native_timeout.py` invokes the **actual installed Python 3.11 interpreter and public `agent.deadline.resolve_timeout`** in a temporary Hermes home. Its environment excludes credentials and uses an isolated managed-config directory; bytecode writes are disabled for the installed runtime. It checks the resolved config path, verifies `(420.0, 420.0)` before the fixture config, then `(1800.0, 1800.0)` with both settings, including precedence over the legacy 420-second environment value. It does not instantiate an agent or call a model/tool. The temporary config is a resolver fixture, distinct from the fake CLI's recorded installation commands. The portable test skips only when that installed interpreter is absent; it ran and passed on this machine.

## PIN, first RED and GREEN

Baseline command:

```sh
uv run --locked pytest -q tests/hermes/test_launcher_cli_install.py tests/hermes/test_launcher_cli_run.py --basetemp output/hermes-timeout-qa/pin-tmp
```

```text
..........                                                               [100%]
10 passed in 6.12s
```

The first timeout RED was saved before implementation, then transcribed here before log cleanup:

```text
FAILED test_install_sets_only_named_profile_native_deadlines
FAILED test_failed_timeout_configuration_stops_install[sequential_call-2]
FAILED test_failed_timeout_configuration_stops_install[concurrent_batch-3]
FAILED test_reinstall_managed_payload_reapplies_finite_deadlines
FAILED test_install_preserves_literal_unusual_workspace
FAILED test_all_install_commands_remain_bounded
FAILED test_settlement_reports_only_observed_cause[0-False-False-exited with unfinished operation-deadline]
FAILED test_settlement_reports_only_observed_cause[1-False-False-exited with unfinished operation-interruption]
FAILED test_settlement_reports_only_observed_cause[-2-True-False-settled after its deadline-interruption]
FAILED test_settlement_reports_only_observed_cause[-2-False-True-settled after an interruption-deadline]
FAILED test_successful_prose_with_partial_state_never_invents_deadline
11 failed, 2 passed in 6.44s
```

The cause assertion exposed the actual old message:

```text
assert 'exited with unfinished operation' in receipt.message
E AssertionError: ... 'Owned Hermes process settled after deadline/interruption; provider cancellation is not confirmed. Inspect saved jobs before any explicit reconciliation.'
```

After the timeout changes: `13 passed in 9.66s`.

Recovery tests initially exposed fixture mistakes around monotonic revision and immutable job history; the fixtures were corrected to obey the existing store contract. The final pre-integration recovery RED was:

```text
FAILED test_explicit_continue_allows_eligible_read_only_review
FAILED test_cli_review_resume_preserves_image_and_original_error
2 failed, 7 passed in 12.93s
E AssertionError: {"success":false,"message":"Inspect saved state; do not resubmit an unresolved request",...,"error":"outcome_unknown",...}
```

One additional synthetic snapshot used an invalid workflow ID for existing candidate paths; that invalid setup was removed without weakening storage validation. The preserved tests cover the original unknown history and the actual linked retry. No failures were blindly rerun.

Final automated command:

```sh
uv run --locked pytest -q tests/hermes/test_launcher_cli*.py tests/hermes/test_launcher_request*.py --basetemp output/hermes-timeout-qa/green-all-tmp
```

```text
.....................................................................    [100%]
69 passed in 39.14s
```

Targeted Ruff with `--target-version py311`, `ruff format --check` and `basedpyright --pythonversion 3.11` covered the three changed launcher modules and five changed/new test modules:

```text
All checks passed!
8 files already formatted
0 errors, 0 warnings, 0 notes
no violations in 8 file(s)
3.11.16 native launcher modules imported without Hermes runtime
```

The final line is an actual installed-interpreter import of `launcher_install`, `launcher_runner` and `launcher_state`. The programming skill checker found no forbidden type escapes or modules above 250 logical lines. The temporary manual script also passed native-version basedpyright. Existing process helper tests were not edited or owned by this dispatch.

## Required tmux manual channel

Commands used in the owned session:

```sh
tmux send-keys -t logopia-timeout-qa 'uv run --locked python output/hermes-timeout-scenario.py' Enter
tmux capture-pane -p -S -120 -t logopia-timeout-qa
```

The first manual execution caught a script-only spelling mistake: it expected `profile_missing`, while the existing CLI correctly returned `missing_profile`. The temporary context cleaned itself on failure. The assertion was corrected before the second execution; application error handling was unchanged.

The final capture, with shell startup decoration omitted and terminal wrapping joined:

```text
LABELLED TIMEOUT FIXTURE: no live installation or generation
INSTALL 1: Logopia installed, doctor checked and enabled in named profile logopia.
INSTALL 2: Logopia installed, doctor checked and enabled in named profile logopia.
EXACT ARGV: ["hermes","-p","logopia","config","set","timeouts.tools.sequential_call","1800"]
EXACT ARGV: ["hermes","-p","logopia","config","set","timeouts.tools.concurrent_batch","1800"]
PASS managed reinstall; literal Unicode/quote/dollar workspace
PASS failing sequential_call: sequential_call_failed; enable not called
PASS failing concurrent_batch: concurrent_batch_failed; enable not called
PASS default: invalid_profile; no fake call
PASS missing: missing_profile; no fake call
PASS default/config sentinels preserved; fake delegates recorded, no native calls
NATIVE PUBLIC RESOLVER: (420.0, 420.0) -> (1800.0, 1800.0); isolated home; no model
PARTIAL EXIT0: Owned Hermes process exited with unfinished operation (exit code 0); provider cancellation is not confirmed. Inspect saved jobs before any explicit reconciliation.
OWNED DEADLINE: Owned Hermes process settled after its deadline; provider cancellation is not confirmed. Inspect saved jobs before any explicit reconciliation.
PASS unknown resubmit blocked; show is read-only; fixture/native image calls=0
PASS live default config digest unchanged; temporary homes/binary/children removed
BINARY PASS
```

This is CLI, filesystem and timeout-resolution evidence. It is not native image-generation proof. The live default config was checked by digest only; its contents were never printed or modified.

## Adversarial coverage and scope

| Class | Evidence / scope |
| --- | --- |
| Missing/invalid/default profile | Existing real-CLI tests and labelled manual scenario; zero fake calls |
| Either config command fails | Exact-key error and immediate stop before later commands; both tested |
| Literal unusual workspace | Unicode, spaces, quote, semicolon and dollar syntax survive literal argv/settings without shell execution |
| Default/foreign data | Default and named fixture sentinels, live default digest, unmanaged plugin and foreign gallery output preserved |
| Managed reinstall | Two installs record the same four commands and preserve non-timeout fixture configuration |
| Bounded commands | Every installer command checked at 120 seconds; actual one-second owned timeout preserves unknown work after child settlement |
| Misleading exit0/prose | Missing, unmodified and unfinished saved workflows cannot be reported as produced |
| Malformed/oversize/instruction-like JSON | Existing parser/CLI tests included in the 69-test run; rejected before dispatch |
| Stale revision/hash | Existing feedback tests plus stale review continuation; zero dispatch, no silent revision refresh |
| Unknown/cancel/resume | Unresolved operations remain no-call; only public-predicate-eligible explicit critique continuation is allowed |
| Resolved history | Actual successful `retry_of` review preserves old error and original hash; local choose/revise/deliver preflight succeeds afterward |
| Hidden model calls | show/gallery/status remain local; install uses fake config commands and the isolated actual resolver only |
| Profile contention | Existing actual-CLI lock contention and lock tests included; process helper unchanged |
| Repeated OS interruption | Delegated to coordinator-owned `test_launcher_process.py` (nine-test process suite), including second interruption during cleanup |
| Active core jobs, late review returns, review budgets and invalid retry links | Core worker's recovery tests; launcher consumes its canonical public functions without duplicating policy |
| Actual native recovery/image quality | N/A to this worker; coordinator owns exact-revision recovery and native evidence; no native retries/images here |
| Flaky rerun handling | Only explained fixture/assertion fixes were rerun; first failures are transcribed above |

Local review checked named-profile routing, finite argv, error propagation, canonical recovery predicates, post-settlement interruption and test evidence. No subagents were created, as instructed; no independent-agent review is claimed.

## Cleanup

Manual fixture homes and fake executables were removed by `TemporaryDirectory`, including the first failed run. All child CLI/fake/resolver commands completed under finite deadlines. The owned `logopia-timeout-qa` session was killed; `output/hermes-timeout-scenario.py` and the entire owned `output/hermes-timeout-qa/` directory (including pytest basetemps and all captured logs) were removed after transcription.

Final concrete checks:

```text
CLEANUP PASS: owned script, QA logs, fixture homes and matching child processes absent; original420 output retained
tmux has-session -t logopia-timeout-qa: absent (exit 1)
```

The absence check inspected the owned temporary-name prefix and matching Python/uv/fake-Hermes process commands without terminating unrelated processes. No live profile was installed, no native model/image call was made, and no coordinator-owned source, original session or result file was modified by this worker.
