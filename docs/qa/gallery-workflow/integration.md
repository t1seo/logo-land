# 0.6.0 source integration

Status: **PASS for T3 source metadata, automated checks, integrity and CLI/HTTP validation**. Dispatch: `task_d46183b983cb` / `ctx_649d5f722e66`. Branch: `feat/logo-land-gallery-workflow`. Base: `06b94c41922973fc98392fadde25fff9aa498f6e`.

## Execution ledger

- Complete: dirty baseline, unchanged 0.5.0 JSON/TOML version consistency and preservation hashes.
- Complete: owned 0.6.0 metadata, bilingual version substitutions and installation handoff.
- Complete: required broad automated checks, public links and native provenance checks.
- Complete: real CLI/HTTP adversarial checks and source/test/document hash manifest.
- Complete: final evidence and verified resource cleanup.

## Resources registered before creation

- `/tmp/ll-060-integration`: exclusive temporary root for command logs, copied real fixtures and downloaded responses. Initial path absence checked. Record device/inode after exclusive creation; remove only verified owned files and empty directories after evidence capture.
- `127.0.0.1:8793`: initial `lsof -nP -iTCP:8793 -sTCP:LISTEN` found no listener. Serve the repository, record the owned server PID, bound its lifetime, stop/reap that PID and confirm the port is free.
- All CLI/HTTP/check subprocesses receive explicit time bounds. No Chrome, image calls, installation, commits, pushes, staging or `.omo` edits belong to this task.

Installation and browser controls have separate owners. Existing source/docs/sample changes are foreign and are preserved.

## Metadata and preserved scope

Before edits, `uv run --locked python -` parsed the plugin JSON, project TOML and locked `logo-land-helper` package and asserted exactly `['0.5.0', '0.5.0', '0.5.0']`. A repository-wide `rg` search of Python/shell files found no existing metadata-consistency unit test. Historical `test_legacy_version_requires_a_json_integer` tests concern session schema types, not package versions. This task therefore reused the direct parsed-consistency assertions documented by earlier release checks; no metadata-mirroring test or production fix was added.

After edits, the same parsed values are exactly `['0.6.0', '0.6.0', '0.6.0']`. Normalizing only the project/helper versions back to 0.5.0 makes both complete parsed TOML documents equal to the pre-edit snapshots: all **22 third-party package records** and dependency declarations are unchanged. Source manifests have no cache suffix. README content matches its T3 baseline after reversing only `0.6.0` substitutions, including unchanged public release links to **v0.3.1**.

The new Unreleased entry describes cross-project comparison, preserved decision notes, illustrative contexts, the legacy null-parent-lockup fix, inline/one-click sample discovery and six initial samples plus two children. It retains Relay geometry drift, the unachieved Sprig bend and Leaflet extra-color observations. Historical 0.4.0/0.5.0 entries remain, with only stale current-version phrasing clarified. English remains the default, IP MIT attribution remains intact, and source archives remain distinct from installation packages.

`METADATA READY` was sent to the coordinator before broad checks, with the 73-file source payload hash below. Personal cache refresh belongs to the [installation owner](installation.md); this worker performed no installation or source copy into a personal plugin.

## Automated commands and actual results

Every command ran once through a captured subprocess with a 600-second bound. Full stdout, stderr, elapsed times and argument arrays are in [integration.json](integration.json).

| Exact command | Result |
|---|---|
| `uv run pytest -q` | **622 passed in 142.64s**, exit 0 |
| `uv run ruff check .` | **All checks passed!**, exit 0 |
| `uv run ruff format --check .` | **308 files already formatted**, exit 0 |
| `uv run basedpyright` | **0 errors, 0 warnings, 0 notes**, exit 0 |
| `uv lock --check` | **Resolved 23 packages in 3ms**, exit 0 |
| `git diff --check` | No output, exit 0 |
| `git diff --cached --name-only` | Empty; no paths staged |

No historical-evidence scope exception or narrower Ruff rerun was needed. No failed/flaky full-suite result was hidden by a rerun. There is no separate compiled build for this Python helper; its actual CLI and the complete type check are covered here. T3 changed no Python production or test file.

## Public links and immutable source evidence

The local Markdown/HTML target walker checked the two root READMEs, CHANGELOG and every `docs/**/*.md` outside historical `docs/qa/**`: **110 Markdown files, 1,492 local targets, including 38 anchors; zero missing paths or anchors**. Targets outside the walked set were still opened for anchor checks. HTML `href`/`src`, Markdown images/links and reference links were included. External links were excluded from this local-target check; published-release identity follows the task's given baseline. The exact document scope is recorded in JSON. The completed integration report's **three additional local links** also pass.

Before metadata changes, T3 inventoried **1,446** existing tracked/untracked files and captured the **534-line** dirty diff. JSON retains the initial status, diff digest, full-inventory digest and exact changed-path list. All **942 protected files** outside owned metadata/docs and concurrent QA evidence match the baseline; `.omo` was neither inventoried nor edited. The installation owner's evidence changed independently and was preserved. Existing sample assets and failed color-gate evidence were never edited or approved by this task.

The durable hash groups in [integration.json](integration.json) are per-file maps plus aggregates. Aggregate encoding is UTF-8, sorted by relative path, one record per file: `<sha256><two spaces><relative path><LF>`.

| Group | Files | Aggregate SHA-256 |
|---|---:|---|
| Installable source payload: `.codex-plugin/`, `assets/`, `skills/` excluding `__pycache__`, plus `pyproject.toml` and `uv.lock` | 73 | `b0e13ca5c8e7bccee4136c3aab37e25c7e3899e9d7426af5aa92e7057814f210` |
| Current Python tests | 40 | `f3c3c8fc360a3f06b2caf4bec2ec6439e1801f74ff37de17bd2b60ae0291e242` |
| Current public Markdown and gallery-workflow assets | 183 | `5b2ec826376812e921d696690d681d2e55003cb4fce34e85abf00ee4741c000e` |

Source and tests match before/after the full suite and CLI/HTTP probes. Later QA-only artifacts do not require another whole-suite run. Source/test changes invalidate the corresponding binding and require appropriate checks; public-doc changes require relevant target revalidation.

## Eight native originals and real copied fixture

The verifier independently read all eight private native receipts and each actual tool-returned file, public receipt, `samples.json` entry, public image, exact submitted prompt, live helper session, portable snapshot and comparison-manifest entry. It checked all four decision fields, hashes, parent IDs, current revisions, receipt event order and decoded PNG facts. The private receipt contents and native absolute output paths remain private; only receipt digests and successful comparisons appear in JSON.

- **Eight unique identities**, six sessions, seven app-icon artifacts and one brand lockup; all unselected and unreviewed.
- **Six initials and two edits**: `relay/v2 → relay/v1` and `sprig/v2 → sprig/v1`. Both native referenced-image paths equal the recorded parent helper path, and input hashes equal the parent original hashes.
- Seven actual **1254 × 1254 RGB PNGs** and COMMON at **1774 × 887 RGB PNG**. Requested approximately 1536-square prompt wording is not reported as the returned size.
- Public source, private session state, imported original, exact prompt and native file hashes match. The earlier publication receipt's state digests still match all six live sessions.

Copied the six real session directories into `/tmp/ll-060-integration/workspace/.logo-generator`, copied the final real selection, and ran actual `show` for all six sessions; every returned state equals its copied session JSON. Ran this exact production CLI, without `--dry-run`:

```sh
uv run --locked python /Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-integration/workspace compare-gallery --selection-file /tmp/ll-060-integration/workspace/selection-valid.json --output gallery-valid
```

Result: `{"path":"gallery-valid","index_path":"gallery-valid/index.html","count":8}`, exit 0. **All 18 portable output files equal the published comparison byte-for-byte**. Real malformed and stale selections returned exit 1 with no destination; a hostile title/notes selection returned an escaped gallery with one authored script and no injected event attributes or sentinel file. All ten real CLI command arrays and outputs are retained in JSON. All original private/public/fixture source bytes remained unchanged after each probe.

## Exact HTTP channel

Server command: `/Users/cillian/Documents/Github/Projects/logo-generator/.venv/bin/python -m http.server 8793 --bind 127.0.0.1 --directory /Users/cillian/Documents/Github/Projects/logo-generator`. The registered owned PID was **87897**. Started only after a fresh successful bind probe; startup had a 10-second bound and each request had a 25-second outer bound. The finite request sequence terminated/reaped the server in `finally`, including on failure.

```sh
curl -i --fail --max-time 20 http://127.0.0.1:8793/docs/gallery-workflow/comparison/index.html
```

Actual result: **HTTP/1.0 200 OK**, exit 0. The response body equals the on-disk index, SHA-256 **`7d90d12a54e901d2b6033a062103870efbd5ab1104108cc563c2b3d69759496c`**. Parsed eight distinct HTML `(session, artifact, revision)` identities. The verified manifest includes the brand candidate and both child-parent bindings. Full headers are retained in JSON.

Then ran `curl --fail --max-time 20` against each manifest-bound `images/001.png` through `images/008.png` and `prompts/001.txt` through `prompts/008.txt` under the same URL prefix. All **16 downloads** equal the actual public files and native/exact-prompt digests, yielding **17 successful requests** in total. This establishes served bytes, not Chrome controls or visual artwork acceptance; actual Chrome/T4 remains separately assigned.

## Nine adversarial classes

| Class | Evidence and outcome |
|---|---|
| Malformed | Full focused input/boundary tests pass within the 622-test suite. A real copied selection with revision `-1` returns exit 1, creates no gallery and preserves sources. |
| Injection | Existing hostile-text tests pass. The real CLI receives script/img/event/shell-looking text only as JSON data; HTML escapes it, has exactly one authored script and no event attributes, and creates no sentinel. Downloaded prompts remain exact bytes and are never executed. This is parser/CLI evidence; Chrome interaction is T4. |
| Cancel/resume | The current suite executes `test_cancel_repeat_then_retry_removes_partial_publication` at image, prompt, manifest and index publication: rollback and successful real retry, bound to this report's unchanged source/test hashes. All six actual copied native snapshots also resume through `show`. |
| Stale | Real Relay revision-1 selection is rejected at current revision 2 with `stale_revision`, exit 1 and no output. Existing during-staging revision/hash tamper tests pass. Six real source-state publication hashes and all eight PNG/prompt bindings still match. |
| Dirty | Initial status/diff/hash inventory captured; owned version edits are isolated, all 942 protected non-QA files are unchanged, foreign installation evidence is retained and nothing is staged. Existing foreign-inode rollback tests pass. |
| Hung | Automated commands bound to 600 seconds, real CLI calls to 30 seconds, HTTP to 20 seconds plus a 25-second outer bound. Server startup is bounded and its owned PID is terminated/reaped; no timeout or hung child occurred. |
| Flaky | All 622 tests passed on the one full-suite execution. No rerun hid a failure, and no native calls/retries were made. Earlier T1/T2 failures and artistic variance remain in their historical records. |
| Misleading | Assertions compare HTTP bodies, all original/prompt bytes, PNG facts, identities, parent input hashes, exact parsed metadata and unchanged dependency records. Source 0.6.0 is unreleased; the manifest remains unapproved; preview contexts do not claim platform deliverables. |
| Repeated interruptions | Reuses T1's four phase-specific twice-cancel-then-retry cases, executed again by this current full suite with source/test hash bindings. Paid native-call destructive interruption is N/A: this task makes no image call and resets no budget or receipt. |

## Remaining independently owned gates

The personal installation receipt and installed-helper checks belong to the installation owner. Actual Chrome controls, desktop/narrow layout, interaction and final user-viewing resources belong to coordinator T4. Final independent reviews belong to T5. T3's passing CLI/HTTP/code checks do not substitute for those gates.

## Cleanup receipt

- Registered temporary root device/inode: **16777230 / 35009500**. Rechecked before cleanup and again before removing the root.
- Inventoried and removed **72 owned regular files**, verifying each file's device, inode and SHA-256 immediately before unlinking; then removed **22 empty subdirectories** and the empty owned root. No force-removal command, symlink traversal or foreign-file deletion was used.
- Removed-file inventory SHA-256: `14792e094968c465cf4ba4790e121050063bdf1b1c749f6eb5a5a657988bd9b8`.
- `/tmp/ll-060-integration` is absent. Server PID **87897** was terminated and reaped; `ps` confirms it is absent and `lsof -nP -iTCP:8793 -sTCP:LISTEN` returns no listener. The 17-request server log is retained in JSON.
- Source, test and public-document hash maps were rechecked successfully at completion. `git diff --check` passes; the staged-path list is empty. Pytest's ordinary retention-managed temporary directory is framework-owned and was not force-cleaned.
- No T3 server, browser tab, copied fixture, temporary verifier, downloaded response, installer, native image call, commit or push remains active. The original private native workspace and other workers' resources remain untouched.
