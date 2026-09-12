# App icon core QA

Task: `task_058008b49769`, dispatch `ctx_e3c39b1f4194`.
Baseline: `ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5`.

## Work ledger

- Completed: pin existing behavior and genuine pre-icon compatibility fixtures (78 + 6 passed).
- Completed: RED icon model/init/prompt/import tests (5 actual CLI failures before edits).
- Completed: implement owned core modules and CLI registration (66 focused passed).
- Completed: focused regressions, static checks, actual tmux CLI, adversarial evidence.
- Completed: exact resource cleanup and final result.

## Registered resources (before creation)

- `docs/qa/app-icons/core-baseline.log`, `core-pin.log`, `core-red.log`, `core-green.log`,
  `core-checks.log`, `core-manual.log`, `core-dirty-before.log`: retained evidence.
- `docs/qa/app-icons/core-fixtures/`: retained pre-icon v1/v2 JSON, prompts and
  synthetic PNG captured using unchanged baseline models.
- `/tmp/ll-icons-core-task058008`: task-only CLI fixture workspace; remove after QA.
- `/tmp/ll-icons-core-pytest-task058008`: explicit pytest base temp; remove after QA.
- tmux session `ll-icons-core`: task-only manual CLI shell; record pane PID after creation,
  terminate exact session after captures. No servers or native generation.
- `core-ruff.log`, `core-types.log`, `core-adversarial.log`, `core-loc.log`,
  `core-regression.log`, `core-snapshots.log`, `core-format.log`, `core-final.log`,
  `core-cleanup.log`: retained core check evidence.
- Pytest framework-managed tmp_path fixtures: task-scoped and isolated; subsequent final
  runs use the registered explicit base temp. No task servers are created.
- tmux pane shell PID: `53502`. Registered session created after confirming name absent.
- Retained icon prompt snapshots: `core-fixtures/prompt-icon-ip.txt` and
  `core-fixtures/prompt-icon-monogram.txt`; these are post-implementation expected prompts,
  separate from the genuine pre-icon `session-v1.json`/`session-v2.json` fixtures.

No commits, pushes, releases, or edits outside assigned files. Existing dirty changes are
preserved; prior color release gates and receipts are immutable history.

## Implemented contract

- Frozen, strict, extra-forbidden `AppIconIntent`; six exact preset IDs; required explicit
  placement accepts all three values for every preset. Monogram text retains 1–8 Unicode
  code points exactly and rejects whitespace/control/format characters; other styles have
  null text. Discovery defaults live in `app_icon_presets.py`, outside the parser.
- Additive optional snapshots on Brief, Artifact, EffectiveIntent and PromptResult, with
  session v2 retained. Absent optional icon fields are omitted during serialization so
  legacy JSON and the frozen v1 parser remain compatible. Actual icon-bearing v2 is forward-only.
- New icon briefs reject transparent backgrounds, slogans, lockups and conflicting exact
  lettering at the JSON boundary. A complete icon file explicitly transforms legacy brand
  rendering while retaining the original brief and previous artifacts.
- One resolver is shared by prompt and import: explicit icon file, otherwise parent snapshot
  including null, otherwise brief. A JSON-null file is invalid, never a clearing instruction.
  Icon rendering suppresses inherited lockups; explicit lockup conflicts fail `intent_conflict`.
- Icon imports request opaque backgrounds by default and reject explicit transparent requests;
  ordinary imports retain original brief fallback behavior. PromptResult distinguishes the
  new opaque request from historical parent_requested_background.
- IP prompts use a separate image-only branch, omitting historical brand/use-case/lockup and
  opacity framing. Descriptions are quoted before trusted constraints; six styles have
  distinct directions and only monograms request lettering. The full prompt is limited to
  20,000 characters. This is structural hygiene, not a claim of model injection immunity.
- Existing free-text and structured palette resolution remains authoritative. Semantic IP
  colors create no strict color constraint. Existing fresh color analysis and export gates
  remain intact; a deliberately red image with white-only intent fails `color_mismatch`.
- `icon-presets` returns six typed choices. `icon-gallery` calls T2's real
  `render_app_icon_gallery(store,state,artifact_ids,output_relative)` API and serializes the
  established GalleryResult. Gallery rendering and delivery implementation remain T2-owned.
- Prompt text requests approximately 1536-square artwork; actual decoded dimensions and
  source bytes are preserved. Runtime/native provenance is owned by the sample receipts;
  this worker performed no native generation or platform export claim.

## PIN → RED → GREEN evidence

1. Before source edits, ran:

   ```sh
   uv run --locked pytest -q tests/test_background_variants.py tests/test_background_compatibility.py tests/test_palette_workflow.py tests/test_palette_compatibility.py tests/test_transactions.py tests/test_color_workflow_transactions.py tests/test_cli_workflow.py tests/test_cli_safety.py tests/test_color_cli_integration.py --basetemp=/tmp/ll-icons-core-pytest-task058008
   ```

   `core-baseline.log`: **78 passed in 54.53s**.

2. Captured real pre-icon `LegacySession` and v2 `Session` constructor output with the
   unchanged baseline classes, fixed timestamp and a 19x23 synthetic PNG. The v1 fixture was
   built directly from the frozen legacy models, not by deleting new fields from new dumps.
   Preserved full baseline generation/edit prompts in `core-fixtures/`.
   `core-pin.log`: **6 passed in 3.36s**, covering exact old prompts, byte-preserving reads,
   v1 byte-exact backup on first mutation, old import behavior and stale no-write behavior.

3. Added real CLI behavior tests before implementation. `core-red.log` begins with **5 failed,
   5 passed in 4.56s**: both icon JSON init cases failed at the Brief extra-field assertion;
   explicit transform and conflict cases failed because `--app-icon-file` was absent.
   Appended missing-model collection failures separately as an initial module checkpoint.
   The behavioral RED is the first 130 lines, not merely the collection failures.

4. Initial implementation: `core-green.log`: **66 passed in 10.23s**.
   Expanded affected regression run: `core-regression.log`: **169 passed in 214.10s**.
   Final core-only run, including reviewed full IP/monogram prompt snapshots, discovery,
   real gallery CLI dispatch and oversized import rejection: `core-final.log`,
   **81 passed in 20.54s**.

5. Full-project `uv run --locked ruff check .`, `uv run --locked basedpyright` and
   `uv run --locked ruff format --check .` are recorded in `core-ruff.log`, `core-types.log`,
   and `core-format.log`. `git diff --check` passed. No broader integrated suite was added;
   T5 owns the all-project test run and native/gallery/browser integration.

The adversarial log retains two QA harness issues: an initially incorrect expected error
name was corrected to the established `color_mismatch`, and overlapping pytest runs briefly
reused the same base temp, causing a fixture directory to disappear. Subsequent runs were
serialized after the process completion was observed. Neither required a production fix or
a weakened assertion. The clean regression/final logs record the corrected execution.

## Actual tmux surface

`core-manual.log` contains literal commands and pane output from the registered session:

```sh
tmux send-keys -t ll-icons-core 'uv run --locked python skills/logo-land/scripts/logo_project.py icon-presets' Enter
tmux capture-pane -pt ll-icons-core -S -200
```

Observed six IDs: `ip_mascot`, `pictogram`, `abstract`, `monogram`, `soft_3d`, `pixel_art`.
Markers: PRESETS_EXIT=0, INIT_EXIT=0, PROMPT_EXIT=0, IMPORT_RETRY_EXIT=0,
SHOW_IMPORTED_EXIT=0, MALFORMED_EXIT=1. Init/import/show used session `manual` under the
registered `/tmp/ll-icons-core-task058008` workspace. The brief explicitly labels its subject
as synthetic QA with no native generation. The full prompt result was parsed with the actual
PromptResult model and written exactly before import.

The first manual import encountered a missing prompt file because the capture driver read
before the queued prompt command completed. It returned `invalid_file`, left revision 0 and
created no artifact. After observing PROMPT_EXIT=0, the driver wrote the complete prompt and
retried the same artifact ID successfully. Both the original failure and recovery are retained.

`core-snapshots.log` verifies the full prompt/app_icon/background snapshot against the imported
and resumed Artifact, actual 19x23 dimensions, no malformed artifact, and unchanged source bytes.
Source and stored PNG SHA-256:
`f2b10f82ea768cb2669294a3e1bd2dbd8b87afaeff3a66a7df8a17bce9de6e7e`.
Session SHA-256 before and after malformed import:
`6e113a8c43da9abdb7c13d5739c4043b1fbf96d4c86081963df3a6723baf0ef0`.

## Nine adversarial classes

| Class | Observed evidence |
|---|---|
| Malformed input | JSON syntax/null/list/unknown preset/extra keys, invalid placement, empty/oversized subject and invalid monogram; both CLI boundaries reject without state/image writes. Actual tmux malformed import exits 1. |
| Prompt injection | Injection-shaped subject and shell-metacharacter filename travel through the real CLI as data; no INJECTED marker appears. Quoted descriptions precede trusted constraints. Unicode and shell-shaped monogram strings remain exact. |
| Cancel/resume | Owned Store.save full-disk fault removes uncommitted icon PNG, preserves exact session and releases lock; real CLI retry of the same ID succeeds. Missing-prompt manual import also recovers without phantom state. No user process was interrupted. |
| Stale state | Stale revisions, explicit parent null vs brief icon, explicit overriding icon, and attempted retroactive icon rebinding are tested; state stays byte-identical on rejection. |
| Dirty worktree | Started with the recorded untracked plan/research/QA files and preserved them. Only assigned paths were edited; other workers' concurrent changes were not reverted. No commits, reset, checkout or clean commands. |
| Hung commands | Harness CLI subprocesses have 20-second timeouts; all observed commands settled. Core tool processes were tracked by returned session IDs and awaited before cleanup. No network/native call is made by this helper. |
| Flaky tests | The fixture-collision harness issue is explicitly retained above and resolved by serialized execution, not repeated blind reruns. Deterministic final runs follow actual source/test changes. |
| Misleading success | Failure records create no artifacts; export without selection and invented --force/--skip-review flags fail. Transparent synthetic pixels remain truthful metadata; strict white palette rejects a red PNG after explicit review. |
| Repeated interruptions/IDs | Faulted import retries its original ID once successfully; stale and repeated ID attempts then fail without changing bytes. JSON null cannot clear an icon parent. No native attempt IDs were reset or fabricated. |

## Architecture and compatibility review

The four new modules own icon validation, style instructions, discovery choices and CLI
registration respectively. External JSON is parsed once into frozen types at the CLI boundary;
shared intent resolution is used by prompts and imports. Preset and placement dispatch uses
exhaustive match with assert_never. No Any annotations, cast, type-ignore, broad exception
handler or placeholder production implementation was added. Existing transaction and
immutable-history storage code is reused. `core-loc.log` records every owned source/test file;
new modules are 32–118 substantive lines and every touched source is below 200.

The review-work checklist was read and applied as a self-review. The task explicitly forbids
children, so this worker did not create the skill's five review agents or claim their verdicts;
the coordinator owns the independent final review wave.

Dependency discovery: `Field(exclude_if=...)` was introduced in Pydantic 2.12, as confirmed by
the [official 2.12 release announcement](https://pydantic.dev/articles/pydantic-v2-12-release#exclude_if-field-option).
The locked environment and standalone helper already use 2.13.5. The coordinator assigned the
declared `>=2.12,<3` minimum alignment to metadata worker `ctx_400758a4181d`; no dependency file
outside this worker's ownership was edited. Final read confirmed the metadata worker has
aligned `pyproject.toml` to `pydantic>=2.12,<3`.

## Final outcome and cleanup

T1 core implementation is complete. Final Ruff passes, basedpyright reports 0 errors /
0 warnings / 0 notes, and Ruff format reports 176 files already formatted. The affected
regression run passed 169 tests; the final core run passed 81 tests. The actual CLI,
full immutable snapshots, error behavior and nine adversarial classes are recorded above.

`core-cleanup.log` confirms removal of only tmux `ll-icons-core` (shell PID 53502 exited),
`/tmp/ll-icons-core-task058008` and `/tmp/ll-icons-core-pytest-task058008` after processes
settled. Retained evidence includes the original synthetic PNG and exact prompts. No server,
child worker or native call was created. Shared dirty changes remain intact. Remaining
native samples, independent review and full integration belong to the
coordinator and their assigned workers.
