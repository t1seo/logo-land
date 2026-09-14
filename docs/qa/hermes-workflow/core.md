# Durable core workflow QA

Core worker task `task_63b6de5caa51`, dispatch `ctx_4f61988ea8d6`.

Implemented and verified the assigned models/protocol, workflow store, finite engine, existing-helper subprocess bridge, and owned tests. Production source is frozen; all owned work and cleanup are complete. No helper implementation, upstream Hermes, credentials, global configuration, metadata, other worker files, pre-existing drafts, or production sample PNGs were changed by this worker.

## Public contract and behavior

- `Studio.create/status/produce/revise/choose/deliver` implement the contract. `create` is local and exactly idempotent for an equal brief. Repeated completed production and delivery reuse existing artifacts/receipts.
- `interrupt(workflow_id: str, expected_revision: int, reason: str) -> Workflow` marks reserved/returned calls unknown after the caller settles its owned runner. It never claims provider cancellation. A cancelled draft remains visibly cancelled and makes no calls on `produce`.
- `reconcile(workflow_id: str, expected_revision: int, job_id: str) -> Workflow` invokes no model. It uses only an exact recorded return/hash or helper commit; missing evidence remains unresolved. No cache discovery or native retry is performed.
- `Critique.parent_view_sha256: str | None` binds edit-parent target views. `StudioError(code, detail, raw_reports=())` carries raw malformed report evidence into the durable job history. Both additions were announced to the coordinator/consumers.
- `checks.review_view(path, width) -> bytes` provides canonical RGBA/LANCZOS target-width PNG review aids. Original/parent/view hashes, dimensions, role identities, and fresh call identities are verified. Reviews never replace originals.
- Each operation/attempt is persisted before the external call. Short advisory locks are released before native calls. Planning is attempted once, initial images consume the exact agreed budget, edits consume at most two calls including failed/unknown calls, and each candidate has at most two critique attempts. Request identities, original provenance, raw reports and completed jobs cannot be rewritten through the store.
- Existing helper runs through `uv run --locked --project <repo> python <repo>/skills/logo-land/scripts/logo_project.py --workspace <workspace> <command>` with a finite subprocess deadline and no shell. Imports always carry the saved background and exact parent/prompt. The original Python 3.12 helper is never imported into Python 3.11.
- Helper imports and exports recover from committed writes followed by lost replies by verifying their deterministic IDs/paths, saved intent, hash, parent, prompt, ExportRecord, manifest, PNG and ZIP contents. Foreign outputs are preserved.
- Choosing records an explicit decision. Delivery requires two valid image critiques with all required criteria; allowed N/A is limited to empty text and new-image preservation. The helper's decoded PNG/background/color gates remain authoritative.
- Brand retains white presentation. IP uses character-only lower-corner composition and its chosen solid background; app icons retain centered pictograms and their chosen filled square background. Both reject unsupported lettering/transparent-mode intent before inference. Native prompts are bounded by the existing helper's 20,000-character limit before dispatch.

## PIN → RED → GREEN

Raw evidence is retained under `output/hermes-core/`; the first failures were not overwritten or hidden by rerunning unchanged tests.

| Stage | Observable evidence |
| --- | --- |
| Existing helper PIN | `pin.log`: `2 passed in 0.95s`; sidecar isolation and import without approval. The coordinator-owned test file was not edited. |
| Public API RED | `red-models.log`: 12 assertion failures because the core API did not yet exist. No production model files existed before this run. |
| Public API GREEN | `green-models.log`: 12 passed. |
| Engine RED | `red-engine.log`: 8 failures for the not-yet-implemented engine, with complete produce/edit/delivery/recovery assertions already written. |
| Helper RED | `red-helper.log`: 4 failures for the not-yet-implemented bounded helper bridge. |
| Initial integration GREEN | `green-first.log`: 24 passed with real locked helper subprocesses. |
| Recovery adversarial pass | `adversarial-first.log`: 8 passed, including import/export commit-lost-reply recovery and late native output. |
| Final integration GREEN | `complete-tests.log`: **44 passed in 39.47s**. |
| Final existing helper compatibility | `final-pin-compatibility.log`: **2 passed in 0.86s**. |

Additional failing-first corrections:

| Failure | Correction and exact evidence |
| --- | --- |
| Phantom feedback after rejected edit reservation | `red-reservation.log`: `assert after == produced` failed after `Steps.reserve` was deliberately rejected. H1 (feedback committed before reservation) was confirmed; H2 (extra host call) and H3 (helper mutation) were excluded. Feedback now commits with the attempt reservation; `green-reservation.log` passes. |
| Child reused parent's critique call IDs | `red-report-identity.log`: actual `awaiting_choice`, expected `failed`. Core now rejects IDs used by earlier jobs. `green-report-reservation.log`: 9 passed. |
| Intermediate continuation regression | `green-report-identity.log` retains the failed first correction: `len(host.reviews)` was 1 instead of 2 because the old failed phase prematurely stopped continuation across an already imported direction. Existing originals are now skipped before the generation failure gate; the final suite verifies critique-only continuation and the two-attempt ceiling. |
| Rewriting a consumed request digest | `red-attempt-identity.log`: `DID NOT RAISE StudioError`. Store now enforces immutable attempt identity and completed evidence; `green-attempt-identity.log` passes. |
| Oversized prompt accepted before native dispatch | `red-prompt-bound.log`: 20,001 characters did not raise. The shared prompt bound now matches the existing helper; `green-prompt-bound.log` passes. |
| IP background overridden by brand white | `pin-brand-prompt.log` passed; `red-ip-prompt.log` records unwanted `Pure white`. Mode-specific assembly preserves the chosen IP background; `green-ip-prompt.log` passes. |
| App background overridden by brand white | `red-app-prompt.log`: 1 failed, 2 passed. Centered pictograms now keep their chosen filled background; `green-app-prompt.log`: 3 passed. |

## Automated checks and Python 3.11 boundary

Final commands used the repository's locked environment and the exact owned module/test globs:

```sh
uv run --locked pytest -q tests/hermes/test_core*.py tests/hermes/test_helper*.py
uv run --locked basedpyright --pythonversion 3.11 integrations/hermes/logopia_studio/__init__.py integrations/hermes/logopia_studio/{models*,store*,helper*,engine*,checks*,prompts,protocols}.py tests/hermes/test_core*.py tests/hermes/test_helper*.py
uv run --locked ruff check integrations/hermes/logopia_studio/__init__.py integrations/hermes/logopia_studio/{models*,store*,helper*,engine*,checks*,prompts,protocols}.py tests/hermes/test_core*.py tests/hermes/test_helper*.py
```

The final pytest invocation used an explicitly owned `--basetemp` via command-local `PYTEST_ADDOPTS`; that directory was removed afterward.

- `complete-types.log`: `0 errors, 0 warnings, 0 notes`.
- `complete-lint.log`: `All checks passed!`.
- `complete-no-excuse.log`: `no violations in 31 file(s)`.
- `module-size-and-syntax.log`: every production module parses as Python 3.11 and has at most 142 nonblank/noncomment lines, below the 250 limit.
- `native-import.log`: actual installed Hermes interpreter **3.11.16**, Pydantic **2.13.4**, Pillow **12.3.0**, `NATIVE_CORE_IMPORT_PASS Studio Workflow`.
- Native pytest was unavailable (`ModuleNotFoundError: No module named 'pytest'`). Nothing was installed or upgraded. The actual Python 3.11 interpreter instead executed the complete public-API scenario with the real helper subprocess, as recorded below.

## Manual channel: tmux and actual Hermes interpreter

The owned `logopia-hermes-core` session ran:

```sh
tmux send-keys -t logopia-hermes-core 'uv run --locked python output/hermes-core-scenario.py' Enter
tmux capture-pane -p -t logopia-hermes-core -S -200
```

The same temporary script was also executed by the Python interpreter referenced by the installed Hermes launcher. The scenario used actual `Studio` methods and actual locked helper subprocesses: create one candidate, produce, repeat produce, revise against its exact canonical parent, choose the child, deliver, validate original and ZIP hashes/content, reload, repeat delivery, and verify an unrelated dirty sentinel. It asserted one plan, two total image stub calls (initial plus edit), two critique pairs, and no duplicate call/package. All temporary originals were deleted after assertions.

Initial surface failures are retained in `tmux-surface.log` and `native-surface.log`. The script compared an unresolved `/var` temporary-root spelling with the correctly canonicalized `/private/var` parent reference. Resolving the script's configured root fixed this harness-only assertion; production source did not change. The shell also emitted a pre-existing missing `powerlevel10k` theme warning, which was left untouched.

Successful tmux capture (`tmux-surface-pass.log`):

```text
HOST=DETERMINISTIC_FIXTURE; not model-generation proof
PYTHON=3.12.12
ORIGINAL_SHA256=56ae7fc8c6462fcd4a4d11b378a15b86dc23b597884c04b30ad589adcac74526
ZIP_SHA256=57a17906b82bd5de8716e8bc709707a5f2d49a345082fd74d3aa3c1e85c91a23
CALLS=plan:1,image:2,critique_pairs:2
PHASE=delivered; CANONICAL_ORIGINALS=2
OWNED_TEMP_REMOVED
CORE_SURFACE_PASS
SCENARIO_EXIT=0
```

Successful actual Hermes Python capture (`native-surface-pass.log`):

```text
HOST=DETERMINISTIC_FIXTURE; not model-generation proof
PYTHON=3.11.16
ORIGINAL_SHA256=56ae7fc8c6462fcd4a4d11b378a15b86dc23b597884c04b30ad589adcac74526
ZIP_SHA256=65344f1e43edc0797af34b9832ae2edadf820338feb239db3c717bd7ae2671fc
CALLS=plan:1,image:2,critique_pairs:2
PHASE=delivered; CANONICAL_ORIGINALS=2
OWNED_TEMP_REMOVED
CORE_SURFACE_PASS
```

ZIP hashes differ across independent runs because the real helper records each export's timestamps. Each ZIP was checked against its own receipt and original bytes.

## Adversarial coverage

| Class | Observable result |
| --- | --- |
| Malformed schema/count/JSON | Strict model and helper boundary tests reject unsupported fields, coercible counts/revisions, malformed JSON and misleading success-only responses. Wrong direction count stops before the first image call. |
| Instruction-like brief/feedback | Verbatim notes/exact text/feedback survive as inert saved data; subprocess execution uses fixed argv and prompt files. No instruction text is executed as a command. |
| Unknown native output and repeated interruption | Repeated interrupt/reconcile/continue retains one consumed initial image attempt without retry. Late returns retain evidence and stop the sequence before a second image/review. |
| Cancelled draft | Visible `cancelled` state, zero planning/image calls on repeated produce. |
| Failed and unknown edit budgets | Two failed edits block a third after reload. A failed edit followed by an unknown second edit survives three interrupt/reconcile rounds and blocks a third dispatch; exactly two edit reservations remain. |
| Malformed or mismatched critique | Raw reports remain in job history; candidate approval remains empty. Explicit continue can retry the critique pair once; further continuation makes no additional critique/image call. |
| Stale revisions / changed originals | Stale choices fail before inference. Modifying an original makes status/resume fail through the helper's actual hash/decode verification. |
| Helper import/export commit interruption | Lost replies after real helper commits recover exact artifacts/receipts without another image/export call. |
| Misleading helper success / missing file | Removing the imported file after helper success prevents core acceptance; no candidate is invented. |
| Authoritative background gate | Fixture critics pass an RGB original requested as transparent; helper export still fails with `background_mismatch` and creates no package. Strict color-policy requests are rejected at the brief boundary. |
| Foreign/dirty work | Dirty sentinel survives create/edit/delivery; foreign export directories/files survive collisions. Existing four unrelated drafts were outside every write target. |
| Bounded helper deadline | A real sleeping subprocess hits a 0.05-second test deadline and raises typed `helper_timeout`; normal bridge deadline is 60 seconds. Owned helper processes are reaped. |
| First failures / flaky reruns | All first RED and surface failure logs remain. Reruns followed explicit fixes; no failed test was deleted or weakened. |

Browser UI, real provider image generation/visual quality, credentials, provider-internal retries, installation and global configuration are outside this core worker's ownership. The fixture host does not prove model quality or independent human approval. Those integrations and the plan's five independent reviews belong to the coordinator/host/gallery workers. This worker performed the `omo:review-work` checklist locally and did not spawn subagents, as explicitly required by its dispatch.

## Cleanup and completion

- Owned pytest basetemps, temporary scenario script, fixture originals and temporary surface workspaces removed.
- Owned tmux session killed; no owned scenario/helper child remains.
- No global environment/configuration changes, commits, paid fallbacks or upstream edits.
- Source tests and this report remain; raw logs remain intentionally under ignored `output/hermes-core/`.
- `cleanup.log` contains teardown receipts; `source-freeze.sha256` and `final-source.sha256` identify source/test snapshots. Production code remained unchanged after source freeze; only the final two adversarial tests were added.
- No core blocker or unfinished owned requirement remains. Cross-worker native-generation/gallery/installer evidence is tracked by the coordinator, not represented by fixture QA.
