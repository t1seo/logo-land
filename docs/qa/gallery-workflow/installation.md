# Personal installation: gallery workflow 0.6.0

**PASS, including final cleanup.** Official `codex plugin add logo-land@personal --json` ran once and returned **0.6.0+codex.20260913004309**. Actual fresh-cache CLI and tmux verification passed. Source remains pure `0.6.0`; this does not claim the current agent reloaded the plugin. Start a new Codex thread to use the refreshed skill.

Task `task_714900aa21c0`, dispatch `ctx_aa5d1e982cb6`. Full normalized actual command responses, file inventories, PNG/prompt hashes, source bindings and process receipts are in [installation.json](installation.json).

## Execution ledger

1. Complete: all 68 previously recorded personal/cache files matched; no unexpected edits.
2. Complete: coordinator `METADATA READY` (`msg_64a6eb999aca`), source freeze, second old-byte check, selective copy, default official cachebuster and one official installation.
3. Complete: installed COMMON/Drip init/prompt/import/show, source/installed/historical IP equality, actual tmux comparison and refusal/injection/resume checks.
4. Complete: receipts preserved; owned tmux, all 128 temporary files/directories and all 70 registered PIDs confirmed absent; installed payload/cache retained.

## Installation identity

| Binding | Actual result |
|---|---|
| Previous personal/cache | `0.5.0+codex.20260912181948`, 68 files, aggregate `42d842d896a0988b041cc0f12c3467e236e85215524b84c1efd752a3610bbb0b` |
| Source freeze | 74 files, aggregate `4f44c4a751ae012b2cd348011c45dfc23bf051bb2cdc950e1560fedbf14fd7e6` |
| Coordinator freeze | 73-file integration inventory `b0e13ca5c8e7bccee4136c3aab37e25c7e3899e9d7426af5aa92e7057814f210`; our inventory additionally preserves existing `THIRD_PARTY_NOTICES.md` and uses the documented different aggregate format |
| Refreshed personal/cache | `0.6.0+codex.20260913004309`, 74 files, aggregate `b5880955f2bc9a5d3ebdaecf1f20c9ac623dbae5af95afdb6c680203de2c5dd2` |
| Source equality | All 73 non-manifest files match exactly; manifest differs only by the official single timestamp suffix |
| Executed helper | Returned cache `0.6.0+codex.20260913004309` / `skills/logo-land/scripts/logo_project.py`; returned and resolved absolute paths were captured privately, never guessed |
| Selective copy | 16 changed/new paths, including 6 additions; no deletion or recursive mirror |
| Official checks | Source/personal/cache plugin validation, plus pre-suffix personal validation, all passed; three `uv lock --check` calls passed |
| Marketplace | Existing `personal` → local `./plugins/logo-land`, confirmed actual personal payload; unchanged SHA `422580558aa3790de35022394fc5b29eb3e15af1bea4e419bd615c95169598e6` |

The old cache matched all 68 hashes immediately before official add. It disappeared after successful official installation; this worker did not delete any cache. No marketplace/configuration edits or marketplace-add command were used. The unrelated configured `astral-codex` marketplace caused auxiliary `codex plugin list --json` to fail with “marketplace root does not contain a supported manifest”; the authorized personal add succeeded without a retry or configuration change.

## Fresh installed CLI and manual QA

COMMON and Drip used the current native originals and exact native prompts from `docs/gallery-workflow`. Actual init/prompt responses supplied revision 0 to each import; imported/show responses supplied current revision 1 to comparison. Both artifact IDs are `v1`, in distinct sessions `common` and `drip`.

| Scenario | Observed result |
|---|---|
| COMMON brand | 1774 × 887 opaque PNG; exact horizontal lockup metadata, original PNG and prompt preserved |
| Drip app icon | 1254 × 1254 opaque PNG; exact pictogram metadata, original PNG and prompt preserved |
| Actual comparison | JSON `count: 2`, `comparison/index.html` exists, two distinct source identities, six published files |
| Body hash | `744669daf4b9a7ee00a346c38ca3e868eb4b2ecb03e5473e23aa4d261374c700` |
| Existing IP recipe | Source and installed prompts equal historical `ip-a1.txt` bytes, SHA `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| Resume | Fresh `show` and repeated prompt preserve exact saved state and prompt |
| Refusals | Stale comparison/import → `stale_revision`; duplicate source → `invalid_selection`; truncated JSON → `json_invalid`; selected but unreviewed clone export → `review_required` |
| Injection | Literal quoted argv and hostile notes are inert; markup escaped; no marker created |

The review-refusal probe selects only a disposable copied session. Original COMMON/Drip selection remains null, reviews remain null, and no source approval changes. All 37 protected native image/prompt/saved-state files and the complete source payload stayed byte-identical. No native call was made.

Registered tmux `ll060-install`, temporary root `/tmp/ll-060-install`, and script `run-installed-compare.sh` before creation. The script contains exact returned-cache helper invocations, explicit selection/workspaces and no source-helper variable. Executed:

```sh
tmux send-keys -t ll060-install 'sh /tmp/ll-060-install/run-installed-compare.sh' Enter
tmux capture-pane -p -t ll060-install -S -200
```

The completion receipt is `exit_status=0`; actual per-command JSON, capture hash and source/byte/refusal assertions agree. tmux and pane PID 89451 are now absent. No dry-run, Chrome or server was used.

## Nine adversarial classes

| Class | Evidence or justified limit |
|---|---|
| Malformed input | Actual malformed JSON and duplicate CLI inputs refused; no partial output |
| Prompt injection | Fixed argv, quoted hostile text, escaped notes and absent sentinel |
| Cancel/resume | Old cache verified until official success; fresh reads preserve state; deliberate install cancellation N/A |
| Stale state | Frozen source, complete old-byte recheck, stale import/comparison refused |
| Dirty worktree | Unowned changes preserved; source file-set/hashes and 37 protected files unchanged |
| Hung commands | Helper/validation 30s, installation 120s; actual installation 0.0778s; all wrapper children reaped, no timeout |
| Flaky results | One installation, no blind retries, no native calls; auxiliary list error disclosed |
| Misleading success | Actual returned path/version/74-file hashes, JSON count, index identities, PNG/prompt bytes and metadata all checked |
| Repeated interruptions | One durable task/dispatch/receipt/version; no actual interruption or reset; destructive install interruption N/A |

## Resource ownership and cleanup

Only `installation.md` and `installation.json` are owned in the shared repository. Existing personal runtime payload and official cache are intentionally retained. No source manifest/project/lock/README, marketplace/configuration, `.omo`, test, commit or push change was made by this worker.

Registered before creation: the temporary root; `admin.rb`, `baseline.rb`, `refresh.rb`, `smoke.rb`, `verify.rb`, `report.rb`, `cleanup.rb`, `run-installed-compare.sh`; evidence/inputs/workspace trees and separate source-IP/export-probe workspaces; tmux/pane and every wrapper subprocess argv/PID. Exact private path receipts are normalized in the public JSON with hashes of the original captures. Cleanup removes only inventoried owned files followed by empty directories, with final absence/PID verification appended below.

This installation task adds no production code or tests. Full source pytest/lint and final combined review belong to the integration/coordinator tasks. New-thread plugin pickup and visual platform approval were not claimed.

Reporting-only correction: system Ruby 2.6 lacks `filter_map`; the disposable receipt collector was changed to `map.compact`. This did not repeat installation or plugin/native operations.

Owned temporary cleanup: 128 individually hash-verified files removed, aggregate `83d2da34d75f92200e3946e084789bc6d36ffc6a7dac3f3af4c54c80a69e1c8e`; only empty directories were then removed. `/tmp/ll-060-install` is absent; all other registered PIDs were already absent, and final cleanup-driver PID verification follows. Source/personal/cache hashes still match after removal.

**Final cleanup PASS:** all 70 registered PIDs, including cleanup driver, are absent; tmux absence exited 1 as expected; temporary root is absent. Source remains pure `0.6.0` with every frozen payload hash unchanged. Personal payload and the official cache remain installed at `0.6.0+codex.20260913004309`.
