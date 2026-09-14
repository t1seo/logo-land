# Native Hermes host evidence

Owner: host worker, task `task_9b996f375656`, dispatch `ctx_b3ce8b923f51`.
Scope: native manifest/registration, host adapter, director skill and host tests.
No model/image calls, profile changes, upstream edits, commits or subagents are authorized.

## Execution ledger

1. Complete: missing-adapter/registration RED tests and installed public API inspection.
2. Complete: strict host transport, action/settings boundaries and director guidance.
3. Complete: 64 host tests, scoped lint/type checks, actual Python 3.11 import and native doctor.
4. Complete: contract/adversarial review, evidence consolidation and owned-resource teardown.

The coordinator supplies `tests/hermes/test_existing_helper.py` (reported baseline: two passing tests).
Core models/protocol/engine and gallery are named dependencies owned by other workers.
No shadow core models are introduced.

## Resources

- `output/hermes-host/`: retained ignored raw QA evidence.
- Owned tmux session: `logopia-hermes-host`; close after final doctor capture.
- Native public-manager registration probe uses one `TemporaryDirectory` prefixed
  `logopia-hermes-host-`, process-local environment overrides and a copied plugin;
  unload the manager and remove the directory before that process exits.
- Pytest temporary settings/PNG fixtures: pytest-managed temporary directories only.
- Final test fixtures use the owned `output/hermes-host/pytest-final/` directory;
  remove that exact directory after retaining the terminal test output.
- The real preflight receipt already exists at `output/hermes-preflight/image-capability-session.jsonl`.
  It is read-only source evidence, not a host-worker-generated image.

## Result and boundaries

The native manifest declares `logopia_start` and `logopia_action` under the
`logopia-studio` toolset. Registration also supplies the namespaced
`logopia-studio:director` skill. `HermesHost` implements the core `DesignHost`
protocol using only the public structured-completion facade and native image
dispatcher. Settings are not read at import/registration time; invocation requires
strict schema-1 absolute workspace/helper roots in the installed local settings file.

Planning performs two bounded role calls. Critique performs two independent calls
with actual candidate original/target-view PNG bytes and, for an edit, exact parent
original/target-view bytes. Views use the core's canonical `checks.review_view`;
the host binds unique call IDs, attribution and all original/view digests. It checks
originals again before returning results. A critic supplies only summary/criteria,
so fabricated attribution or evidence fields fail validation.

Generation dispatches exactly once with `prompt`, `aspect_ratio: square`, and the
exact `image_url` for an edit. The unadvertised `upscale` field is omitted, as agreed
with the coordinator; the installed native default performs no upscale pass.
Receipt success is insufficient: the returned path must identify a regular,
single-frame, decoded local PNG. The host retains the exact accepted native receipt
and rejects reuse/change of the parent.

Action schemas share the core `FeedbackEnvelope` instead of duplicating it.
`host_requests.StartRequest`, `ActionRequest`, `parse_start`, `parse_action` and
`tool_json` are available to the coordinator's launcher without importing Hermes.
Mutation arguments require an explicit revision; feedback checks the candidate hash
before the core's compare-and-swap mutation. Status does not call the publisher.
Other successful actions publish to a fresh unique output path. Tool summaries
contain paths and concise state, not PNG bytes or full critique reports.

The director bundles craft/typography/color guidance and separate IP character
guidance with s1dashu's pinned source credit and complete MIT notice. It distinguishes
advisory palette roles, selection and delivery approval; no beauty score, market
research, human expert review, font-file use or legal clearance is claimed.

## PIN / RED / GREEN

The coordinator-owned existing helper baseline was reported as two passing tests;
this worker did not edit or rerun that baseline or run the full suite.

Before production files existed, the two host contract test modules failed during
collection with `ModuleNotFoundError: No module named 'logopia_studio'`. The original
terminal output is retained in `output/hermes-host/red-missing-adapter.txt`.

Further failing-first tests found two host history gaps:

- A second-critic timeout propagated without the first raw report. The direct host
  reproduction rules out core persistence as the cause; the first fake completion
  had already succeeded. `red-second-critic-timeout.txt` retains the original failure.
- Removing the original during the second critic caused the final PNG check to lose
  both reports. `red-missing-original-history.txt` shows `raw_reports == ()` before the fix.

The transport and final-image checks now attach the already-collected reports to
typed errors, retaining the original exception as the cause. Neither path retries
or dispatches another image. Both same-input regressions pass in the final run.

Final commands and observed results:

| Check | Observed result | Raw evidence under `output/hermes-host/` |
|---|---|---|
| `uv run --locked pytest -q tests/hermes/test_host*.py --basetemp output/hermes-host/pytest-final` | **64 passed in 0.29s**, exit 0 | `green-host.txt` |
| Scoped `uv run --locked ruff check --target-version py311` over the entry point, host modules, registration and host tests | **All checks passed**, exit 0 | `ruff.txt` |
| Same file scope with `uv run --locked basedpyright --pythonversion 3.11` | **0 errors, 0 warnings, 0 notes**, exit 0 | `basedpyright.txt` |
| Programming skill no-excuse audit | **No violations in 14 files**, including the 250 logical-line ceiling | `no-excuse.txt` |
| Actual installed Hermes interpreter import | **Python 3.11.16; Pydantic 2.13.4; Pillow 12.3.0; HermesHost/register imported** | `python311-import.txt` |
| Skill creator `quick_validate.py` in the installed Hermes interpreter | **Skill is valid**, exit 0 | `skill-validation.txt` |

The first skill-validator invocation in the helper environment failed because that
environment lacks PyYAML. The installed Hermes environment already supplies it; the
validator passed there without installing or changing any dependency.

## Actual native manual QA

Created only the owned tmux session `logopia-hermes-host`, then used:

```sh
tmux send-keys -t logopia-hermes-host 'hermes plugins doctor /Users/cillian/Documents/Github/Projects/logo-generator/integrations/hermes --ci' Enter
tmux capture-pane -p -t logopia-hermes-host -S -200
```

The final captured output was:

```text
manifest: logopia-studio 0.1.0 (standalone)
OK: runtime discovery, manifest parsing, import, and registration passed
registrations: 2 tool(s), 0 hook(s)
HERMES_DOCTOR_SETTLED_EXIT=0
```

The actual native public `PluginManager` also discovered a copied plugin in one
owned temporary home, resolved `find_plugin_skill('logopia-studio:director')`, and
confirmed the skill, craft resource and IP license files. It returned
`list_plugin_skills('logopia-studio') == ['director']`, then `unload() == True`.
The temporary directory was removed on exit. This probe made no model/image calls
and used no real profile. See `native-skill-registration.txt` and
`doctor-tmux-final.txt`. The shell printed an existing missing-theme warning; it did
not affect doctor, and shell/global configuration was not changed.

**Binary registration PASS:** actual native import/doctor exit 0, both declared
tools registered, director resolved through the installed public manager, no missing
imports/dependencies. This is registration proof, not native image-generation or
real visual-review proof.

The separately existing preflight native receipt parsed successfully through the
host and its local original decoded as PNG **1254 × 1254**, despite requested-size
metadata **1024 × 1024**. Its SHA-256 was
`79fd22cebe5303e7e67d42be7b6766f5194acccbb2032746243283b834422ba6`.
The recorded provider/model were `openai-codex` / `gpt-image-2-medium`.
`preflight-receipt-check.txt` explicitly records **zero new model/image calls**.

## Adversarial coverage and applicability

| Case | Evidence / outcome |
|---|---|
| False, malformed, string-boolean, unknown-field or unattributed native receipts | Rejected; bounded original response retained; one dispatch and no fallback |
| Missing, corrupt, JPEG-disguised, symlink or directory image path | Native success cannot approve it; PNG decoding fails closed |
| Wrong/missing/unknown action fields, coercible revisions, malformed feedback, oversized Unicode payload | Strict request models reject before settings/engine mutation; 32 KiB boundary checked |
| Missing/malformed/relative/unknown-field settings | Clear typed error, no implicit workspace/model defaults; registration still works without settings |
| Instruction-like brief data | Kept in JSON input blocks, absent from role instructions; no command/provider fields exposed; this is boundary evidence, not a guarantee about arbitrary model interpretation |
| Independent image review | Both calls receive two actual PNGs for a new original or four for an edit; exact bytes, target dimensions and digests asserted; neither receives the other's report |
| Malformed, duplicate-key-criterion, invalid-N/A or evidence-spoofing critique | Rejected, with prior raw reports retained; no invented approval |
| Changed/missing originals and exact parent | Hash mismatch prevents initial review; changes/deletion during review retain failure history; native return of parent as child rejected |
| Timeout / interruption / repeated calls | One native dispatch on timeout; second-critic timeout preserves the first report; repeated core unknown-outcome errors remain visible and trigger no fallback/publication |
| Stale feedback | Revision/hash mismatch produces no choose/revise/image call; no silent substitution of latest state |
| Status and gallery routing | Status calls no publisher and changes no file bytes; successful action routes pass exact arguments and receive distinct fresh output paths |
| Global worker cancellation, provider cancellation, launcher deadline, cross-process overlap, two-store recovery | **N/A for this host dispatch:** owned by core/launcher/coordinator; host tests prove transport/error propagation, not those global behaviors |
| Browser interaction and actual gallery rendering | **N/A for this host dispatch:** gallery worker owns these; host tests use the public publisher boundary |
| Actual model/image quality or generation/revision/delivery run | **N/A:** explicitly prohibited for this worker and serialized by the coordinator |

Review covered goal/contract, code quality, input boundaries, observed QA and installed
source context locally. The task prohibited new agents; no independent review or
real expert assessment is claimed. Native generation/critique transport still needs
the coordinator's actual end-to-end run. All named core/gallery import dependencies
had landed before the final native doctor; no unresolved import dependency remains.

## Cleanup and shared workspace

- Final doctor was captured before `tmux kill-session -t logopia-hermes-host`.
  A subsequent exact-session check confirmed it was closed.
- Removed only the owned `output/hermes-host/pytest-final/` fixtures after saving
  output; the exact path no longer exists. Earlier default pytest temporary paths
  follow pytest's normal managed retention. No handles/processes remain from them.
- The public-manager probe unloaded registrations and removed its temporary home.
- Retained requested raw evidence in ignored `output/hermes-host/`, including every
  first-failure log. No installed-local settings file was added to the public package.
- No new agents, commits, branch changes, global configuration changes, upstream
  Hermes edits or actual model/image calls were made. All four unrelated
  `.omo/drafts/logo-land-next-*.md` drafts remain present; no edit command targeted them.
- Coordinator-owned metadata/install/launcher files and core/gallery edits were
  preserved. The initial and final shared worktree both contained other workers'
  uncommitted changes; no reset, cleanup of foreign files or full-suite run occurred.
