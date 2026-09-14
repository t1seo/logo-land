# Installer foreign-marker fix

Status: complete. Task `task_85a7c3f2995d`, dispatch `ctx_4b6cf28e96fb`.

## Ownership and plan

Only `integrations/hermes/logopia_studio/installer.py`,
`tests/hermes/test_installer_foreign_marker.py`, `tests/hermes/test_installer_interruption.py`,
this report and `fix-installer/`
are owned. Other workers' files, root `.debug-journal.md`, native profiles,
canonical r47, five originals and the four unrelated drafts stay outside this task.

1. Complete: preserve unchanged source and reviewer evidence; PIN valid updates
   and ordinary-file refusal; reproduce the nested-marker RED with exact bytes.
2. Complete: restrict the exemption to the root-relative marker; verify GREEN and
   existing installer/CLI tests, Python 3.11 compatibility, Ruff and type checks.
3. Complete: incorporate the coordinator's second installer acceptance condition:
   PIN OSError rollback, reproduce KeyboardInterrupt deletion, minimally restore
   the old installation while propagating the interrupt, and verify recovery.
4. Complete: run the actual `install_payload` fixture in the requested tmux channel,
   verify repeated refusal and absence of staging/lock artifacts, report nine
   adversarial classes, remove all registered temporary resources and report once.

## References and hypotheses

Read `omo:programming` and Python README/one-liners, `omo:debugging` Python runtime,
setup, investigation and fix references; `orchestration` and the installed CLI guide.
Read the coordinator's journal without editing it. No new agents or dependencies.

- H1: basename-only exemption treats a nested foreign marker as the root record.
  Distinguishing evidence: same bytes/source, ordinary filename refuses and nested
  marker succeeds; changing only the exemption reverses the nested outcome.
- H2: the nested file is legitimately listed as managed. Distinguishing evidence:
  inspect `ManagedInstall.files`; an explicitly owned nested marker stays accepted,
  an unlisted marker must refuse. Fix if true: ownership fixture.
- H3: stale payload/manifest or wrong imported source creates the difference.
  Distinguishing evidence: exact source/module hashes and root-record byte snapshots
  before each call, plus a separate stale-hash refusal control. Fix if true: fixture pin.

Reviewer first failures remain in `review-code/defensive-tests.txt` and
`review-code/defensive-probes.py.txt`; neither is edited. The reviewer also recorded
an interrupted-rename rollback defect in `review-code/install-rollback-tests.txt`.
Coordinator message `msg_d9df0c3c4731`, read in full after the first marker code-ready
notice, and the coordinator's same-terminal reminder add this defect to the same ownership.
No rollback source change occurred before its additional PIN/RED steps.

- H4: `KeyboardInterrupt` bypasses the OSError rollback handler, allowing temporary
  directory cleanup to delete the previous plugin. Compare the same second-rename
  fault with `PermissionError` and `KeyboardInterrupt`. Fix if true: catch interrupt.
- H5: the fixture fails before the old installation is moved or has already changed
  its old payload. Distinguish with recorded backup existence and exact prior bytes
  at the real publication boundary. Fix if true: fixture seam.
- H6: a foreign replacement already occupies the target, so restoring would overwrite
  it. Distinguish the absent-target restoration case from a newly occupied target;
  preserve foreign replacement bytes in the latter. Fix if true: retain guard.

## Resource ledger (registered before creation)

| Resource | Purpose and cleanup |
| --- | --- |
| `fix-installer/` | Retained sanitized evidence directory: source/test snapshots, PIN/RED/GREEN logs, diffs, hashes, static/manual/cleanup receipts. |
| `/tmp/logopia-fix-installer-080` | Exclusive scratch root; confirmed absent before creation; remove exact directory at completion. |
| Scratch `pin/`, `red/`, `pytest/`, `native/`, `toggle/` | Pytest basetemps and their source/profile/workspace/file/symlink fixtures, all beneath scratch; remove with scratch. |
| Scratch `rollback-pin/`, `rollback-red/`, `rollback-green/` | Additional same-task recovery regression fixtures, all synthetic; remove with scratch. |
| Scratch `toggle/logopia_studio/`, `toggle/pytest/` | Isolated copy of the current native package with only installer restored from the saved pre-edit source; rerun the unchanged regression without toggling the shared working tree; remove with scratch. |
| Scratch `manual.py`, `native_audit.py`, `runner.py` | Bounded local verification scripts; retain sanitized `.py.txt` copies, remove originals with scratch. |
| Scratch `manual/`, `native-manual/` | Synthetic source, workspace and named fixture profile only; no actual Hermes profile access. |
| Scratch `processes.jsonl`, `manual.pid`, `native-manual.pid`, `pane.pid` | Registry of exact owned process roles and numeric PIDs; record each allocated PID before doing fixture work, check OS absence before cleanup. |
| tmux `logopia-fix-installer-080` | One owned shell pane, no service/port; register its pane PID immediately at creation, close exact session and verify PID/session absence. |
| Manual child / native manual child | Actual installer fixture with a 30-second self-deadline; synchronous parent owns/reaps the child; record exact PID before fixture creation. |
| Foreground pytest / Ruff / basedpyright / audit processes | Scoped finite tool commands; completion exit codes retained; do not terminate unrelated processes. |
| Command-local `PYTHONDONTWRITEBYTECODE=1`, `TMPDIR` | Prevent new imported-module caches and route temporary fixture data to scratch; no persistent environment change. |
| tmux-local `PYTHONPATH`, `PYTHONDONTWRITEBYTECODE`, `TMPDIR` | Import the working native package and keep temporary data local; removed with the owned session. |

Repository runtime is locked Python 3.12.12. Bare `python3.11` is 3.11.16 but lacks
Pydantic; its first import check raised `ModuleNotFoundError`, without fixture work.
The already installed native runtime will be checked without adding dependencies.

## Evidence

PIN: `pin.txt`, 2 passed / 10 deselected in 0.05s on unchanged source.
RED: `red.txt`, 1 failed in 0.05s; exact persisted observation:

```json
{"scenario":"nested_marker","update_result":"succeeded","foreign_file_preserved":false,"sentinel_sha256":"bafd9c15abf567fd467e03a691382c6e49177bf7e4fddaee271223333f7d6a7b","source_unchanged":true,"installation_unchanged":false}
```

`cmp` proved source still matched `installer.before.py.txt` after RED;
`red-source.sha256` binds source and the first test, retained as `test-first.py.txt`.
H1 matches the observed filename toggle; H2 is refuted by the nested path's absence
from the manifest and H3 by exact unchanged source snapshots in the same fixture.
Existing native runtime `/Users/cillian/.hermes/hermes-agent/venv/bin/python` reports
Python 3.11.16 and Pydantic 2.13.4; no install/config operation was needed.

GREEN: the exact requested three-file pytest scope passed **25 tests in 7.78s**
(`green.txt`). Scoped Ruff passed, formatting found four files already formatted,
and `basedpyright --pythonversion 3.11` reported zero errors/warnings/notes.
`installer.diff` contains exactly one changed condition; symlink checking still
precedes the exemption. Code-ready notice sent as `msg_6a25fa0da204` before manual QA.

Additional rollback RED: `rollback-red.txt` records an exact prior backup at the
second rename, but `KeyboardInterrupt` leaves `target_exists=false` and no plugin
entries. OSError restores exact bytes. The first `-k` selectors also matched the
test filename/function, so both cases ran; their unchanged first outputs remain
in `rollback-pin.txt` and `rollback-red.txt`. The exact `[io]` node PIN then passed
in `rollback-pin-exact.txt`. This was a selector correction, not a changed assertion.
`installer.before-interruption.py.txt` and `rollback-red.sha256` prove the rollback
handler was unchanged during these observations. H4 is confirmed; H5 is refuted by
`backup_exact_before_failure=[true]`. No failed investigation round occurred.

Rollback GREEN: `rollback-green.txt`, **4 passed in 0.06s**. The original exception
instance propagates for both OSError and KeyboardInterrupt; original bytes restore,
two interrupted attempts preserve exact bytes, subsequent retry publishes the new
payload, and an externally occupied target is not overwritten. The latter tests
preservation of the foreign replacement, not restoration over an occupied target.
The production delta is now two changed conditions, with no new dependency or API.

## Final automated evidence and source freeze

- `green-final-checked.txt`: **29 passed in 6.81s** across the requested installer,
  foreign-marker and launcher-install files plus the additional interruption file.
- `ruff-final.txt`: all checks passed for the changed source and two test files.
  `format-final.txt`: six files already formatted, including existing installer/CLI
  tests and the manual script.
- `types-final.txt`: native Python 3.11 mode, **0 errors, 0 warnings, 0 notes** for
  source, both regression files and the manual script.
- `no-excuse.txt`: the programming skill's audit found **no violations in 4 files**.
- `native-audit.json`: actual CPython **3.11.16** parsed every changed Python file
  plus the manual script; no Any/object/cast escape names or type-ignore comments.
  Nonblank/noncomment lines: installer 130, marker tests 168, interruption tests 99,
  manual script 162, all below 250.
- `toggle-red.txt`: only the installer source was restored to its original bytes
  in an isolated copied package; both unchanged regression assertions failed again.
  The shared working tree was never reverted. Original installer SHA-256:
  `5e286d8dc7ae88899c6f335f3a0721c3699f4c25b633efe424918b3b38710099`.
- Final installer SHA-256:
  `768da32cdf90da78fd519a39b9b65bd3bdd4cf81c20dc4e45452ffc3e060708b`.
  `final.sha256` binds source/tests and original reviewer evidence. The marker
  regression file remains byte-identical to the first RED snapshot.
- Initial expanded static checks found a redundant pytest fixture alias/private
  test-helper import and a missing manual-script module description. The test helper
  is now local and fixture registration uses `pytest_plugins`; assertions were not
  weakened. First diagnostics remain in `ruff-expanded-first.txt`,
  `types-expanded-first.txt` and `manual-ruff-first.txt`.

Final two-line source diff is `installer.diff`; the earlier marker-only diff remains
in `marker-only.diff`. Both-fixes code-ready notice: `msg_970a9e165bc7`; source/test
freeze confirmation: `msg_aad70b3b7948`. Root owns integrated checks, independent
reviewer settlement and actual named-profile refresh.

## Actual tmux QA

The owned session `logopia-fix-installer-080` executed the exact requested channel:

```sh
tmux send-keys -t logopia-fix-installer-080 'uv run --locked python /tmp/logopia-fix-installer-080/manual.py' Enter
tmux capture-pane -p -S -200 -t logopia-fix-installer-080
```

`tmux-manual.txt` contains **PASS**, Python **3.12.12**, PID **40611**,
`manual_exit=0`. `tmux-native-manual.txt` additionally contains **PASS**, native
Python **3.11.16**, PID **40957**, `native_manual_exit=0`. Each script sets a
30-second self-deadline before fixture creation. The native interpreter was the
already installed Hermes venv Python; only synthetic profiles under scratch were
passed to `install_payload`. No real Hermes configuration/install command ran.

The manual script (`manual.py.txt`) calls the actual installer, performs actual
staging/old-directory renames, and injects a real `signal.raise_signal(SIGINT)` at
the second rename boundary. It verifies the backed-up old bytes before signaling,
checks KeyboardInterrupt propagation, restores the old install twice, and then
publishes a successful explicit retry. A separate occupied-target attempt proves
the foreign replacement is not overwritten. No model/image/provider call occurs.

Observed hash evidence:

| Runtime/scenario | SHA-256 before and after both attempts |
| --- | --- |
| 3.12 interrupted update | `c337d15d2b20bf1238af7cd7aba956ab10d7e12772a0e69b5c6d005f3011dbba` |
| 3.11 interrupted update | `3acd098af01c4a13df7925e05c6217e45801cb28028ab3a0809bb2c210368c57` |
| 3.12 nested-marker refusal | `962d32e410ee4734a14be2134b2269cd1fc46f6196cdeb1c055754eb29d89660` |
| 3.11 nested-marker refusal | `0b8811596400cb965feac9bdef3737d93712c5ca57373736b2869135fa71cc03` |
| Literal sentinel bytes, both runtimes | `bafd9c15abf567fd467e03a691382c6e49177bf7e4fddaee271223333f7d6a7b` |

Tree hashes differ across runtimes because the synthetic workspace/settings paths
differ. Within each run, exact byte tuples and hashes both remain equal. Every
scenario reported `lock_and_staging_absent=true` before any final scratch cleanup.

## Nine adversarial classes

| Class | Result and evidence |
| --- | --- |
| 1. Malformed/unmanaged input and symlinks | PASS: three invalid root manifests, existing unmanaged-plugin/source-symlink tests, and root/nested marker symlinks with present/absent destinations refuse; fixture bytes/links remain. |
| 2. Instruction-like content | PASS: the literal sentinel includes an instruction-like sentence; it is preserved as bytes and never executed or treated as authority. |
| 3. Cancellation and recovery | PASS: reviewer OSError rollback PIN, dedicated KeyboardInterrupt RED/GREEN, then actual tmux SIGINT with old-backup read-back and a successful later update. |
| 4. Stale state/hashes | PASS: modified managed bytes with stale manifest hashes reject as `modified_install`, source and full installed snapshot unchanged. |
| 5. Dirty/foreign data | PASS: ordinary and nested-marker refusal preserves exact bytes; explicitly managed nested marker still updates; an occupied target preserves its foreign replacement. |
| 6. Finite budget/deadline | PASS: both manual children have a 30-second self-deadline; inherited CLI tests use bounded fixture invocations; no model call, retry loop or real profile change. No provider budget behavior is claimed. |
| 7. First failures and retry discipline | PASS: first marker/rollback REDs and selector/static diagnostics retained; isolated-original replay deterministically fails both regressions; no flaky retry or assertion relaxation. |
| 8. Misleading success | PASS: the original `succeeded` plus missing sentinel fails the regression; manual success additionally requires exact bytes, expected typed error/interrupt and absence of lock/staging artifacts. |
| 9. Repetition/idempotency | PASS: two SIGINT attempts preserve the same old tree, a later managed update succeeds, and two nested-marker refusals preserve the same full tree and sentinel on both runtimes. |

## Cleanup

`cleanup.json` records PASS: owned manual PIDs **40611**, **40957** and tmux pane
PID **40608** are absent; session `logopia-fix-installer-080` is absent; the exact
scratch directory `/tmp/logopia-fix-installer-080` was removed and checked absent.
The pre-removal scan found **499** owned scratch entries and **zero** installer
locks/staging directories. Only the owned session was closed; no global process
or session cleanup ran. Sanitized scripts, raw first failures, final outputs and
hashes remain in `fix-installer/` as requested evidence. Command/session-local
environment settings ended with their owning process/session. Reserved
`runner.py` and `native_audit.py` were unnecessary and never created; the native
audit ran as a foreground Python 3.11 stdin command. No server, port, browser,
download, dependency installation, commit, push or additional agent was created.

All planned outcomes are complete; no task-local blocker or required work remains.
Actual named-profile refresh and integrated reviewer settlement remain root-owned.
The demonstrated cancellation boundary is SIGINT/KeyboardInterrupt at publication
rename, including repeated attempts; no hard-kill/power-loss guarantee is inferred.
