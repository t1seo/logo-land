# App icon quality core: Q2 evidence

Completed implementation of the five non-IP emitted prompt recipes in `style_direction`; this is an instruction-contract change, not evidence of better native artwork. Final source SHA-256: `d59ff54a2c77a368390be832bda5643af92dbab75d1a6431838687397e847080`.

Task `task_bed94163884a`, dispatch `ctx_d6c245a53279`, 2026-09-13 KST / 2026-09-12 UTC. Read the active plan's [Finalized quality extension contract](../../../plans/logo-land-app-icons.md), [Metis contract](quality-metis.md), [research](../../research/app-icon-quality.md) and [audit](quality-audit.md). The final contract supersedes the preliminary 24-grid and contact-shadow alternatives. Applied programming/Python and orchestration guidance. No new research, external provider, native image generation, GUI, installation, child agent or commit was performed.

## Scope and completed work ledger

| Deliverable | Status / evidence |
|---|---|
| Preserve baseline, historical prompts and all original bytes | Complete: [baseline log](quality-fixtures/baseline.log), [initial hashes](quality-fixtures/hashes-before.json), [IP expectations](quality-fixtures/ip-pins.json) |
| Author expectations before production, then demonstrate RED | Complete: [reviewed directions](quality-fixtures/directions-v1.json), [full quality cases](quality-fixtures/quality-cases-v1.json), [RED log](quality-fixtures/red.log), [RED source/fixture hashes](quality-fixtures/red-source-sha256.txt) |
| Implement only five returns | Complete: [exact source diff](quality-fixtures/source.diff), [pre-change source](quality-fixtures/app_icon_prompts-before.txt), [boundary/hash verification](quality-fixtures/integrity.json) |
| Automated gates and real CLI | Complete: 239 affected tests, Ruff, format, strict basedpyright; 47 recorded helper commands plus the required tmux discovery command |
| Nine adversarial classes, evidence and cleanup | Complete: ledger and cleanup receipts below; no native/beauty claim |

The production diff changes only `pictogram`, `abstract`, `monogram`, `soft_3d`, and `pixel_art` return bodies. Removing those five bodies from the pre-change/current source produces byte-identical remainder, including the entire IP block, shared builder, placement, metadata path and length check. No schema, public field, CLI flag, policy layer, preset ID, font, renderer, color gate, provider or image processing was added.

Pictogram now specifies compact distinctive filled construction and open identifying overlaps/gaps; abstract specifies one coherent gesture with deliberate ends/intersections/openings; monogram preserves exact script structure while balancing strokes, counters, joins and visible glyph spacing; soft 3D specifies a supplied material or smooth matte/satin default, broad light and subject-only palette-constrained shading, omitting incompatible extra tones and external shadows; pixel art specifies one coarse module, repeated contour steps, matching thickness and broad connected clusters. Every new block explicitly yields to supplied subject/concept/changes and the authoritative lettering/placement/palette tail. Product-specific input remains in quoted JSON.

Source and tests own narrow responsibilities: emitted icon construction, quality output contracts, and existing icon prompt compatibility. Substantive nonblank/noncomment lines: source **154**, quality tests **129**, prompt tests **143**, all under 250. Existing typed boundaries and exhaustive match remain intact; strict fixture models parse JSON, and no `Any`, ignore/cast escape, new exception layer or production helper was introduced.

## Baseline → PIN → RED → GREEN

All pytest invocations used `uv run --locked`, `-q -p no:cacheprovider`, an exact task-owned `--basetemp`, `PYTHONDONTWRITEBYTECODE=1`, a bounded outer process and the existing 20-second Harness CLI timeout. The baseline also used `--no-sync`. The complete commands and process lifecycle are retained in [process registry](quality-fixtures/processes.jsonl).

| Phase | Result | Evidence |
|---|---|---|
| Existing eight app-icon suites before source edits | **118 passed in 35.28s**, exit 0 | [baseline.log](quality-fixtures/baseline.log) |
| New full IP PINs, old IP/monogram snapshots, historical import/gallery test | **27 passed in 0.62s**, exit 0 | [pin-corrected.log](quality-fixtures/pin-corrected.log) |
| New contracts against unchanged production | **85 failed, 43 passed in 10.89s**, exit 1 | [red.log](quality-fixtures/red.log) |
| Changed/new test files after recipe implementation | **128 passed in 6.49s**, exit 0 | [green-targeted.log](quality-fixtures/green-targeted.log) |
| All affected suites plus quality tests after formatting | **239 passed in 30.43s**, exit 0 | [green-affected.log](quality-fixtures/green-affected.log) |
| `uv run --locked ruff check` on three changed Python files | **All checks passed**, exit 0 | [ruff-final.log](quality-fixtures/ruff-final.log) |
| `uv run --locked ruff format --check` on three changed Python files | **3 already formatted**, exit 0 | [format-final.log](quality-fixtures/format-final.log) |
| `uv run --locked basedpyright` on three changed Python files | **0 errors, 0 warnings, 0 notes**, exit 0 | [types-final.log](quality-fixtures/types-final.log) |

The affected suites were `test_app_icon_prompts`, `test_app_icon_compatibility`, `test_app_icon_models`, `test_app_icon_workflow`, `test_app_icon_workflow_invariants`, `test_app_icon_workflow_palette`, `test_app_icon_gallery`, `test_app_icon_delivery`, plus the new `test_app_icon_quality`. They include pre-icon generation/edit full snapshots, parent-null precedence, immutable history, failed-save rollback/resume, malformed inputs and strict export rejection after visual review. No full repository 433-test rerun was performed; final integration belongs to the coordinator. This Python helper has no separate compilation build; actual CLI execution and strict diagnostics are recorded above.

The PIN contains **18** complete pre-edit IP outputs: three placements × fallback/free-text/strict palette × generation/parent edit, plus **six** complete existing native IP outputs rebuilt from their saved source briefs and quoted concepts/changes. The original six outputs also matched their existing `docs/app-icons/prompts/ip-*.txt` files before source edits. Current PIN tests reconstruct all 24 against saved, frozen expected outputs, and final original hashes remain equal.

New fixed expectations were authored **before** production edits. `directions-v1.json` was written from the contract; full expected prompts were assembled from that text and the unchanged historical envelope without calling the builder. [pre-red-sha256.txt](quality-fixtures/pre-red-sha256.txt) and [red-source-sha256.txt](quality-fixtures/red-source-sha256.txt) bind them to pre-change source `38fbf3cfdb3efd97da4b96eb554cd392f5ae06cb1d8cb12a27822729b280c015`. RED fails on absent agreed instructions, style isolation, exact complete output and the changed complete-length boundary, including actual inherited CLI output. The 24 IP PINs keep passing. These assertions verify emitted instructions, never typography, pixel craft or beauty.

The old [monogram fixture](core-fixtures/prompt-icon-monogram.txt) remains byte-identical, SHA-256 `d0a3101fadf8efc676bcda11c6023b746caf40e06ab1470a2534f7d5cd687af1`. Only the current monogram snapshot is deliberately retargeted to [prompt-icon-monogram-v1.txt](quality-fixtures/prompt-icon-monogram-v1.txt); the IP snapshot remains on its old file. A new historical import → `icon-gallery` test ran before production edits and again after them, proving the old prompt and a clearly synthetic original remain byte-identical when published, without changing session history.

The test matrices cover two distinct concepts (including quotes, newline and shell-like text), all placements, generation/edit, no cross-style recipe leakage including IP, monogram-only lettering, exact `모`, `한글`, `메모`, decomposed `e` + U+0301, palette precedence, inherited metadata and exactly **20,000 accepted / 20,001 rejected** complete prompt characters for every new style.

Corrections are preserved rather than hidden: the first new historical test mistakenly called a Pydantic method on the dataclass `GalleryResult`; it was corrected to `TypeAdapter(GalleryResult)` before the successful PIN and before source edits ([initial log](quality-fixtures/pin.log)). Initial lint found source string wrapping over 100 columns, a parameter container and quote escaping; formatting/line wrapping corrected them without changing emitted text. Final checks passed once after those corrections. No failed test was deleted or weakened, and no golden expectation was regenerated from the changed builder.

## Actual CLI channel and parsed observations

Resource registration was sent as `msg_88fb302895eb` before creating exact `/tmp/ll-icon-quality-core`, the new fixture directory and tmux `ll-icon-quality-core`. Every subprocess command/PID/timeout was registered before launch in the process ledger. Native sources were read only; manual imports use **only `core-fixtures/synthetic-baseline.png`**, never a newly generated image.

Executed the required channel exactly:

```sh
tmux send-keys -t ll-icon-quality-core 'uv run --locked python skills/logo-land/scripts/logo_project.py icon-presets' Enter
tmux capture-pane -pt ll-icon-quality-core -S -200
```

The [captured terminal transcript](quality-fixtures/tmux-presets.txt) contains all six unchanged IDs in order: `ip_mascot`, `pictogram`, `abstract`, `monogram`, `soft_3d`, `pixel_art`, followed by `exit_status=0`. Only the unrelated shell startup banner before the executed command was omitted from the durable text to avoid retaining machine/network details; the executed command and output are unchanged. The shell's existing missing-theme startup warning did not affect helper execution.

[cli-transcript.json](quality-fixtures/cli-transcript.json) records all **47** actual bounded commands, expected/actual exit, exact argv and response paths. Every successful stdout and rejected error is saved in [cli/](quality-fixtures/cli/). The six ordinary examples use complete existing sample-plan briefs, their explicit concepts and no parent. Parsed generation results agree with the exact brief icon, revision 0, mode generation, no parent/palette and requested opaque background. Each non-IP trusted section contains its exact fixed direction and none of the other directions; the IP prompt equals the saved native `ip-a1` text.

| Scenario | Expected = observed | Actual JSON |
|---|---|---|
| IP / pictogram / abstract / monogram / soft 3D / pixel | Exact brief icon; generation; revision 0; requested background opaque; proper isolated direction | [IP](quality-fixtures/cli/02-manual-ip-a1-prompt.json), [pictogram](quality-fixtures/cli/04-manual-pictogram-prompt.json), [abstract](quality-fixtures/cli/06-manual-abstract-prompt.json), [monogram](quality-fixtures/cli/08-manual-monogram-prompt.json), [soft 3D](quality-fixtures/cli/10-manual-soft-3d-prompt.json), [pixel](quality-fixtures/cli/12-manual-pixel-art-prompt.json) |
| Exact Unicode, explicit lower-right | `모`, `한글`, `메모`, `e` + U+0301 retained exactly; revision 0; lower-right instruction | [모](quality-fixtures/cli/14-unicode-0-prompt.json), [한글](quality-fixtures/cli/16-unicode-1-prompt.json), [메모](quality-fixtures/cli/18-unicode-2-prompt.json), [decomposed](quality-fixtures/cli/20-unicode-3-prompt.json) |
| Strict soft 3D | Revision 1; palette `strict` and exact saved digest; two allowed colors, locked primary, required background, `allow_gradients:false`; no fallback color | [strict prompt](quality-fixtures/cli/23-strict-prompt.json) |
| Inherited edit after new active palette | Edit; revision 3; parent `parent`; original soft 3D intent; requested/parent background opaque; original `strict` ID/digest, excluding future red | [inherited edit](quality-fixtures/cli/26-inherited-edit.json) |
| Malformed and truncated icon input | Exit 1; explicit validation/JSON error; saved session and (truncated case) all workspace files/hashes unchanged | [malformed](quality-fixtures/cli/28-malformed-no-write-confirmed.json), [truncated](quality-fixtures/cli/43-truncated-json-no-tree-writes.json) |
| Stale import / reviewed strict export | Exit 1, `stale_revision` / `color_mismatch`; exact state preserved; no export output | [stale](quality-fixtures/cli/29-stale-import.json), [strict rejection](quality-fixtures/cli/38-strict-export-rejected.json) |
| Injection in subject/concept/changes/color text | Exact escaped quoted data; authoritative generic directions after it; marker absent | [injection edit](quality-fixtures/cli/42-injection-edit.json) |
| Legacy parent-null despite icon brief | Edit bound to `v1`, no effective app-icon/requested-background metadata; exact state preserved | [parent-null](quality-fixtures/cli/44-legacy-parent-null.json) |

The first manual driver expected exit 2 for malformed JSON but observed the correct rejection at **1** ([original record](quality-fixtures/cli/27-malformed-no-write.json)). That expectation error is retained; the driver resumed from the same saved workspace/session and performed a separately recorded no-write confirmation with expected exit 1, then completed the remaining cases. No earlier successful init/import was repeated, no production correction was needed, and this was not a flaky retry. [manual-resumed.log](quality-fixtures/manual-resumed.log) and [manual-adversarial.log](quality-fixtures/manual-adversarial.log) record completion. A temporary Ruby integrity expression initially used unsupported `filter_map`; the corrected compatible expression produced [integrity.json](quality-fixtures/integrity.json) without touching protected files.

## Nine adversarial classes

| Class | Executed probe and result / precise limit |
|---|---|
| 1. Malformed input | Actual extra-field JSON and truncated JSON rejected at CLI exit 1; complete file path/hash snapshot unchanged for truncated input. Existing malformed/model/extra/null/no-write tests also passed. |
| 2. Prompt/shell injection | Actual payload containing quotes, newline, command substitution and backticks went through subject, concept, requested changes and free-text colors; parsed quoted fields equal inputs and `/tmp/ll-icon-quality-core/INJECTED` was absent. No shell interpretation or model-level immunity is claimed. |
| 3. Cancel/resume | Executed existing publication `KeyboardInterrupt` rollback/resume cases, including repeated interruption, plus failed-save → same-ID import recovery. Actual CLI prompt/show were then repeated in fresh processes three times with identical output, exact state and saved `parent` identity. **N/A:** no live native job or mid-execution CLI process was killed; none was necessary for this prose-only source change. |
| 4. Stale/binding/color | Actual stale import rejects; actual legacy parent-null wins over icon brief; strict inherited edit preserves parent palette despite a new active palette; actual strict export rejects after synthetic visual review. Existing immutable-history and all seven export-gate cases passed. |
| 5. Dirty shared tree | Initial status saved. Of 150 registered pre-existing files, exactly the two owned existing files changed; the other 148, including all saved originals/prompts and core fixtures, retained SHA-256. New files are within assigned test/QA ownership. Unrelated concurrent work was preserved. |
| 6. Bounded processes | Outer tests 90–240 seconds, manual drivers 90–150 seconds, each real CLI 30 seconds, existing Harness CLI 20 seconds. All owned recorded subprocesses exited, with no timeout or background network process. Owned tmux PID/session and exact temporary tree cleanup are recorded below. |
| 7. Flakiness/retries | Deterministic RED was followed by source implementation and GREEN. Tooling/test-harness corrections are explicitly recorded above. No native calls, artistic retries, pixel repairs, hidden filtering or unchanged flake retries occurred. |
| 8. Misleading success | Passing instructions, CLI metadata and byte preservation do not prove typography, material, grid regularity, native artistic improvement, strict measured palette PASS or store readiness. Synthetic review was deliberately followed by a real strict export rejection. |
| 9. Repeated interruptions/identities | Existing repeated publisher interruption and failed-save/same-ID tests executed; three fresh-process inherited prompt/show cycles and three legacy parent-null prompt cycles preserved exact output/state. The 24 frozen IP outputs and all original IDs/hashes remain stable. **N/A:** repeated real native interruptions; no native attempt or new image identity exists in this task. |

## Integrity, cleanup and remaining work

[hashes-before.json](quality-fixtures/hashes-before.json) preserves the 150 pre-existing source/test/original/fixture hashes; [integrity.json](quality-fixtures/integrity.json) verifies unchanged ownership boundaries. [hashes-final.json](quality-fixtures/hashes-final.json) identifies the final source, tests and durable fixtures/logs. Frozen IP and quality fixtures were not rewritten after production edits. The six native IP prompts still reproduce their original saved bytes; every old gallery/native image and prompt in the registered set remains unchanged.

Process and cleanup evidence: [processes.jsonl](quality-fixtures/processes.jsonl), [cleanup.json](quality-fixtures/cleanup.json), [temporary inventory](quality-fixtures/temp-inventory.json). Only the owned `ll-icon-quality-core` tmux session and exact `/tmp/ll-icon-quality-core` are terminated/removed. Durable source/tests, expectations and logs remain. No other tmux server/session, foreign worktree, original artwork or coordinator resource is removed.

The stable source hash was sent to the coordinator and Q3 as `msg_0ff42d2790fd` and `msg_d1c5815ce9b9` before cleanup, so guidance verification can proceed independently. Coordinator-owned downstream work remains: final full integration/review/install, five actual native comparison draws and their visual comparison. This worker does not claim those outcomes and did not spawn review children because the explicit dispatch prohibits them.
