# Interrupted critique recovery — core evidence

Date: 2026-09-15 KST. Dispatch: `ctx_11bfae4740c3`, task: `task_7343b802e35e`.

Implemented the CONTRACT G2/G4/G7 clarification: explicit `Studio.produce(id, exact_revision)` may replace one unresolved read-only critique using its remaining second attempt. Initial planning, originals, completed reviews, selection, feedback and the old unknown attempt stay intact. Unknown plan/generate/edit/delivery, active reserved/returned calls, missing originals and exhausted review budgets remain blocked. No model calls, demo writes, upstream Hermes changes, global configuration changes, commits or subagents were used.

The actual `offcut-hermes-demo` schema-1 record was inspected read-only: revision 23, three originals, two complete critique pairs, and unknown critique `j7` without reports. Under the real Hermes Python 3.11.16 interpreter it passes the new eligibility predicate and its saved request digest exactly matches the reconstructed request. Baseline/final SHA-256 comparison covers all five actual files: the workflow, helper session and three originals; they remain unchanged. This is compatibility evidence, not execution of the actual demo.

## Public additions and persistence

- `Job.retry_of: Identifier | None = None` is optional within schema 1. It is written only on the replacement critique. Old records missing the field still parse without migration.
- `engine_recovery.can_resume_critique(state: Workflow) -> bool` is a pure eligibility query. It does not interrupt, reconcile or call a host.
- `engine_jobs.unresolved_jobs(state: Workflow) -> tuple[Job, ...]` supports launcher/core idle checks. Every reserved/returned job stays unresolved; only an unknown job referenced by a validated critique replacement is excluded.
- Retry links require the earlier unknown critique, the same candidate and request digest, no saved critique pair, and no preceding replacement. The original unknown job/error/raw history is never rewritten. Both attempts count toward the existing two-attempt ceiling.
- The replacement and its link are committed under the existing short lock before the native call. The lock is released during the call. Exact revision compare-and-swap protects reservation.
- Superseded `record`, `fail`, attachment, reconciliation and caller continuations return the current state without accepting the old reply or changing its revision. Successful or failed late responses cannot replace fresh reports, resume an old generation/edit sequence, or change a ready/cancelled selection.
- Successful review recovery permits later explicit choose/revise/deliver. `interrupt` and `reconcile` retain their no-inference behavior. No reset/force endpoint was added.

Coordinator was informed when the predicate/model became available and when the pending-job helper was ready; launcher consumes both. Host/launcher implementation and native 420-second executor configuration belong to the other worker/coordinator.

## PIN → RED → GREEN

Raw evidence is retained under `output/hermes-critique-resume/`.

| Stage | Observable result | Raw log |
| --- | --- | --- |
| Existing behavior PIN | 46 passed: prior 44 core/helper cases plus two unchanged coordinator-owned helper compatibility cases | `pin-existing-prepared.log` |
| Unknown-call PIN | Unknown plan, generation and second edit remain blocked after repeated interrupt/continue; three cases passed, zero resubmissions | `pin-unknown-prepared.log` |
| RED: continuation | Existing implementation returns `outcome_unknown` instead of `awaiting_choice`; remaining critic is called zero times instead of once | `red.log` |
| RED: late return | Both success/error cases fail because explicit recovery remains `outcome_unknown` before the late response can settle | `red-late-corrected.log` |
| RED: public predicate | ImportError for absent `can_resume_critique` before production edits | `red-eligibility.log`, `red-model.log` |
| Public model/predicate GREEN | 11 eligibility/link validation cases passed | `green-public.log` |
| Initial recovery GREEN | 16 focused cases passed | `green-target.log` |
| Full owned regression GREEN | 69 cases passed in 73.57 s | `green-all.log` |
| Additional cancelled-choice fence | Five late-return cases passed, including two added cancelled-choice variants; the other three were already in the full run | `final-cancellation.log` |
| Final collection | 71 distinct core/helper/compatibility cases collected | `final-collection.log` |
| Strict checks | Ruff passed; basedpyright `--pythonversion 3.11`: zero errors/warnings/notes | `ruff-final-expanded.log`, `types-final.log` |
| Native grammar/size/types | All 14 changed Python files parse with Python 3.11, stay below 250 nonblank/noncomment LOC, and contain no `Any`, `object`, `cast`, suppression or noqa | `source-audit.log` |

Commands used for the full regression and final strict checks:

```sh
uv run --locked pytest -q tests/hermes/test_core*.py tests/hermes/test_helper*.py tests/hermes/test_existing_helper.py --basetemp output/hermes-critique-resume-fixtures/green-all
uv run --locked ruff check integrations/hermes/logopia_studio/engine_{jobs,steps,production,recovery,pipeline,actions}.py integrations/hermes/logopia_studio/models{,_jobs}.py tests/hermes/test_core_{critique_resume,critique_late,resume_eligibility,resume_fixtures,resume_adversarial}.py
uv run --locked basedpyright --pythonversion 3.11 integrations/hermes/logopia_studio/engine_{jobs,steps,production,recovery,pipeline,actions}.py integrations/hermes/logopia_studio/models{,_jobs}.py tests/hermes/test_core_{critique_resume,critique_late,resume_eligibility,resume_fixtures,resume_adversarial}.py
```

The three confirmed failure points were paused-state early return, global unknown-job idle/reservation checks, and unfenced late job writes/sequence continuation. The fix uses an immutable relationship between attempts and one shared pending-job calculation.

First failures were preserved rather than discarded or blindly rerun:

- The initial read-only inspection used the incorrect key `path` and raised `KeyError`; it was corrected to the existing `Candidate.image_path` field. No demo mutation occurred (`first-inspection-error.txt`).
- Initial PIN attempts failed fixture setup because the registered `--basetemp` parent had not yet been created: 17 passed/29 setup errors, and three setup errors respectively. The missing owned parent directory was created before the prepared PIN runs (`pin-existing.log`, `pin-unknown.log`).
- The first late-response fixture referenced nonexistent `ReviewInput.candidate_id`, producing two `AttributeError`s. Its trigger was corrected to the canonical `image_path.stem`; behavioral assertions were unchanged, and both corrected RED cases then failed on the intended blocked recovery (`red.log`, `red-late-corrected.log`).
- Initial Ruff found one import-order issue and four long lines; a later check found the regex alternation needed a raw string. Only formatting and regex literal syntax changed. All original lint logs remain (`ruff-first.log`, `ruff.log`).
- The coordinator later identified one pre-existing formatting chain in `tests/hermes/test_core_prompts.py`; only Ruff formatting was applied, with identical before/after AST and passing lint/types (`format-correction.log`, `types-format-correction.log`). All 14 changed Python files pass `ruff format --check` (`format-final.log`).
- No failed behavioral assertion was weakened to match the implementation. Both manual channels passed on their first execution.

## Manual channel and native interpreter

Only owned tmux session `logopia-critique-resume` was created, using a clean zsh. The required channel commands were:

```sh
tmux send-keys -t logopia-critique-resume 'uv run --locked python output/hermes-critique-resume.py' Enter
tmux capture-pane -p -S -100 -t logopia-critique-resume
/Users/cillian/.hermes/hermes-agent/venv/bin/python output/hermes-critique-resume.py native311
```

The labelled fixture host creates three real fixture PNG files through the actual helper JSON subprocess bridge. Setup records schema 1/revision 23, all originals, two valid pairs and an unknown third critique; the optional retry field is omitted to exercise old JSON. Explicit continuation then asserts zero planning/image calls, one fresh critique pair, exact original/history preservation and `awaiting_choice`. The same scenario explicitly chooses, edits from the exact original parent, chooses the child, delivers with the real helper, verifies PNG/ZIP hashes and ZIP payload, reloads, and confirms idempotent repeated continue/delivery.

It also refuses unknown-image and exhausted-review states after three further interrupts, and deterministically overlaps a late old critic with successful replacement and user choice. These are fixtures, not proof of real model design quality or a real provider timeout.

Native output (`native311-scenario.log`; tmux's equivalent output is captured in `tmux-capture.txt`):

```text
FIXTURE_HOST_ONLY interpreter=3.11.16 pid=64701 label=native311
CRITIQUE_RESUME_PASS plan_calls=0 image_calls=0 critique_calls=1 originals=3 roles=2 phase=awaiting_choice
POST_RECOVERY_LIFECYCLE_PASS choose revise deliver reload original_zip_hashes=True duplicate_calls=0
BLOCKED_CASE_PASS unknown-image additional_native_calls=0
BLOCKED_CASE_PASS exhausted-review additional_native_calls=0
LATE_REPLY_PASS old_unknown_retained=True fresh_choice_unchanged=True stale_revision_blocked=True
CORE_CRITIQUE_RESUME_PASS fixture_host_only=True model_quality_not_tested=True
```

The tmux channel used Python 3.12.12 and scenario PID 64682; real Hermes Python 3.11.16 used PID 64701. Both child processes exited zero. Original fixture hashes and the real helper session bytes remain unchanged across the read-only review recovery; the later authorized edit adds only its child and fresh review.

## Adversarial coverage

| Class | Observable evidence |
| --- | --- |
| Malformed JSON/schema/types/count | New malformed-sidecar and boolean/negative revision tests refuse without host calls; existing strict model/count and malformed helper-response tests pass |
| Wrong/malformed reviews | Retry malformed report is retained as raw evidence; both attempts remain, a third is refused and delivery stays gated; existing evidence/role/call-identity tests remain green |
| Unknown plan/image/edit/delivery | Plan/image/edit no-resubmission PIN; eligibility rejects all other unknown kinds; manual unknown-image repeats have zero additional calls |
| Reserved/returned active calls | Eligibility rejects both statuses; shared pending helper always retains them; existing reservation and stale-write tests remain green |
| Exhaustion/repeated interrupt | Two attempts including unknown are retained across reloaded interrupt/reconcile/produce cycles; no third call or reset |
| Cancel/resume | Cancelled draft has no calls; late success/error after ready or cancelled choice leaves the exact chosen snapshot intact |
| Late/stale return | Four initial-critic variants plus an edited-child late return preserve new report/choice/revision; stale explicit requests refuse before host calls |
| Inert brief/feedback | Instruction-like strings and `$(touch ...)` remain saved data; no marker is created; exact keep/change and existing selection survive child-critique recovery |
| Changed originals | Tampered fixture PNG blocks resume; every original is checked by existing status/helper verification; initial/final actual demo hashes match |
| Dirty worktree | Unrelated fixture sentinel survives; shared files, four pre-existing drafts and other workers' modules were not edited |
| Bounded subprocesses | Existing actual 30-second sleeping child is stopped by `run_cli`'s 0.05-second test deadline; production helper calls retain their finite timeout and process-group settling behavior |
| Misleading helper success/missing PNG | Existing malformed-success and missing canonical import tests remain green; no fabricated original is accepted |
| Helper commit recovery | Existing lost import/export-reply tests reconcile exact commits without image/package duplication |
| Real provider quality / real 420-second process timeout | Scoped N/A: no real model calls were authorized; launcher/executor configuration belongs to the parallel launcher task |
| Credentials, paid fallback, global profile/installation | Scoped N/A: no such action is required or performed in this core-only fixture task |

## Cleanup and remaining integration

Cleanup entries were registered in `output/hermes-critique-resume/cleanup.md` before or immediately upon creating owned resources. Raw logs, source hashes, source tests and this report remain; fixture PNGs, helper workspaces and the temporary scenario script are removed after capture. Only the owned tmux session is terminated, and scenario/helper children are reaped. `cleanup.log` records the final resource and private-file checks: 231 owned fixture PNGs and their complete fixture root removed, temporary scenario removed, tmux session killed, scenario PIDs 64682/64701 and pane PID 64679 absent, zero remaining owned fixture subprocesses, and all five private files unchanged. All cleanup register entries are settled; no temporary home/profile was created.

The core has no remaining blocker. The coordinator owns the combined launcher/host integration run, installation and any explicitly authorized real-demo continuation. No actual workflow continuation was performed by this worker.
