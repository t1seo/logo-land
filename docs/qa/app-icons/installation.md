# Logo Land 0.5.0 personal development installation

Task `task_a0fb416de8be`, dispatch `ctx_260a5957592a`; installation-only QA on 2026-09-13 KST. **PASS: final installation `0.5.0+codex.20260912172956`, actual CLI/tmux/HTTP QA, payload identity and cleanup verified.** This run uses the immutable repository `assets/logo.png` as a clearly labeled installation fixture, not as a generated app icon or native-image acceptance result. No image calls, commits, releases, source-code edits, or manual marketplace/configuration edits are authorized by this worker. Official CLI installation writes are authorized.

## Execution plan

1. Completed: record source 0.5.0, prior personal/cache 0.4.0, marketplace mapping and dirty-tree baseline.
2. Completed: stage the allowed plugin payload, apply the official default cachebuster, reinstall through the actual Codex CLI, and verify payload identity and official validators.
3. Completed: exercise the actual installed helper from the registered independent workspace, including adversarial and non-icon cases, tmux and HTTP gallery download.
4. Completed: retain evidence in this report, remove only registered temporary resources, verify retained installation/source and report completion.

## Resource registry (registered before creation)

| Resource | Exact location / ownership | Disposition |
| --- | --- | --- |
| Independent temporary workspace and staging | `/private/tmp/logo-land-icons-install-task_a0fb416de8be` | Owned exclusively by this task; remove after evidence is retained. |
| Local receipts and logs | Workspace `evidence/`, including command JSON, baseline hashes, tmux capture, HTTP headers/body and server log | Embed results/hashes in this report, then remove with workspace. |
| Input fixtures | Workspace `inputs/`: exact bundled `logo.png`, icon/non-icon brief copies, explicit intent JSON, malformed intent JSON, Unicode intent/brief JSON, exact prompt text, shell/script-text fixture and execution sentinel path | Fixture-only; remove with workspace. |
| Disposable project state | Workspace `.logo-generator/`, `.git/`, `dirty.txt`, and generated `gallery/` outputs | Remove with workspace; repository dirty files are protected. |
| Download | Workspace `downloads/original.png` | Compare SHA-256 to source and gallery original, then remove. |
| tmux | Session `ll-icons-install`, started in the independent workspace | Record exact pane PID; kill only this owned session. |
| Gallery server | `python3 -m http.server 8782 --bind 127.0.0.1 --directory <workspace>/gallery`; listener `127.0.0.1:8782` | Record exact child PID before HTTP QA; bounded lifetime, terminate/reap only that child. Verify port absent before/after. |
| Personal payload | `/Users/cillian/plugins/logo-land` | Authorized update retained; only `.codex-plugin/`, `assets/`, `skills/`, `pyproject.toml`, `uv.lock`, `THIRD_PARTY_NOTICES.md`. |
| Installed cache | Actual Codex CLI result under `/Users/cillian/.codex/plugins/cache/personal/logo-land/` | Intended installed deliverable retained; no broad cache deletion. |

Every subprocess launched for validation or QA is bounded by a timeout; HTTP calls additionally use `--connect-timeout 2 --max-time 10`. Unexpected failures are recorded without suite retries. The planned cancel/resume check stops after prompt construction and resumes through a fresh helper process; it does not simulate a native call.

## Initial pin and reinstall receipt

Previous personal/cache version: `0.4.0+codex.20260912161802`; all 55 payload files were identical before copying. Source has 67 payload files and remains pure `0.5.0`. The old installed `icon-presets` exited 2 with `No such command`; official source plugin/skill validators and `uv lock --check --project /Users/cillian/Documents/Github/Projects/logo-generator` exited 0.

The official marketplace helper returned `personal`; its existing local `./plugins/logo-land` resolves in this environment to `/Users/cillian/plugins/logo-land`, which was verified against the previous installation. Source payload was copied through owned staging after a second per-file hash check.

Installed version: `0.5.0+codex.20260912171735`. Actual cache root: `/Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735`. Actual helper: `/Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py`. The account plugin directory is an existing symlink to `/Users/cillian/.codex/plugins`. No marketplace/configuration file was manually edited.

Registered running tmux session `ll-icons-install`, pane PID `8507`, before sending helper input.

Registered owned HTTP server PID `8625` on `127.0.0.1:8782` before requests; exact command `python3 -m http.server 8782 --bind 127.0.0.1 --directory /private/tmp/logo-land-icons-install-task_a0fb416de8be/gallery`.

## Initial installed verification results

**PASS:** 21 installed-helper calls: 16 successful and 5 expected refusals; one additional actual helper invocation through tmux exited 0. All calls ran from the separately registered Git workspace `/private/tmp/logo-land-icons-install-task_a0fb416de8be`, using the absolute installed cache helper, with `PYTHONPATH` unset and `PYTHONDONTWRITEBYTECODE=1`. The `uv run <absolute-script>` PEP 723 environment was used; the three project `uv lock --check` checks independently verify the packaged lock, not that the script environment uses that lock.

| Scenario | Observed outcome |
| --- | --- |
| Preset discovery | Exact ordered IDs: `ip_mascot`, `pictogram`, `abstract`, `monogram`, `soft_3d`, `pixel_art`. |
| Bundled icon example | Exact copy of installed `app-icon.example.json`; revision 0 and Korean `메모` intent preserved. |
| Prompt and explicit import | Exact final prompt bytes and explicit intent carried from prompt revision 0 into artifact `fixture-logo`; revision advanced once to 1; opaque request preserved. |
| Malformed intent | Unknown field rejected by both prompt and import with `extra_forbidden`; session and artifact file hashes unchanged. |
| Cancel/resume | Workflow stopped deliberately after prompt generation; fresh helper `show` and repeated `prompt` preserved revision 0 and byte-identical state. This is a safe-boundary cancellation, not a mid-write signal test. |
| Stale revision | Import at revision 0 after successful import refused with `stale_revision`; no state or image changes. |
| Duplicate artifact | Importing existing ID at correct revision 1 refused with `conflict`; no state or image changes. |
| Read-only operations | `show`, repeated `prompt`, and `icon-gallery` preserve every session file hash; repeat gallery rejects existing destination and preserves gallery files. |
| Unicode exactness | `메모é` retains code points U+BA54 U+BAA8 U+0065 U+0301 without NFC normalization in intent and prompt. |
| Shell/script text | Literal command substitutions, backticks, quotes and `<script>` text were passed as argv/file data; marker file never appeared, exact prompt remained intact, and HTML subject escaped script tags. |
| Non-icon regression | Installed standard brief init/prompt/import/show succeeded; absent optional app-icon output stayed absent/null, ordinary lockup persisted, original PNG and prompt matched. |
| Dirty workspace | Existing `dirty.txt` remained byte-identical; source code and historical installation evidence were not rewritten. |

### Manual terminal and HTTP channel

The following actual command was sent to the owned tmux session from the independent workspace. It exited 0 and displayed all six exact IDs. The pane PID was `8507`; the session was killed after capture.

```sh
tmux send-keys -t ll-icons-install 'uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py icon-presets' Enter
tmux capture-pane -pt ll-icons-install -S -200
```

HTTP server PID `8625` served only the generated fixture gallery; the response status was `HTTP/1.0 200 OK`. The exact requested HTTP and download commands were:

```sh
curl -i --fail --connect-timeout 2 --max-time 10 http://127.0.0.1:8782/index.html --output /private/tmp/logo-land-icons-install-task_a0fb416de8be/evidence/http-response.txt
curl --fail --connect-timeout 2 --max-time 10 http://127.0.0.1:8782/images/fixture-logo.png --output /private/tmp/logo-land-icons-install-task_a0fb416de8be/downloads/original.png
```

The downloaded bytes matched source, copied input, stored artifact and gallery PNG. The owned server was terminated and reaped; `lsof -nP -iTCP:8782 -sTCP:LISTEN` returned 1 with no listener, and a socket check agreed.

### Key SHA-256 evidence

| Object | SHA-256 |
| --- | --- |
| Previous personal/cache aggregate (55 files) | `5712571d23f4013479ea5692d0b31cf3a1eb16274e1cac3e61185562ca3af457` |
| Initial source aggregate (67 files) | `d9adbd19e60aa043a922c6bd946c39300099d6a751dcbd84b304e55540719bb2` |
| Initial installed aggregate (67 files) | `a6752b3045f7df3570511139d53916d3a4fa20b3d65aec93dbc496388f003c8e` |
| Immutable PNG and HTTP original | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| Exact icon fixture prompt | `32407a02666547103ac62863b339e9b6c0cc49c1f3170626ae87655d477b9b5b` |
| Exact Unicode fixture prompt | `e54613f0b28b40f2ccb74dc76ad15179297deea48ab30a99281db77e8682865c` |
| Icon session after import | `e10112bd1fa1d24625f457b1bc26bf4f868b9411e32ddd8425199d1fbe975071` |
| Non-icon session after import | `18d66cad8f5c64636f134a4fc6ed383e0fa725a9eec4b6a88239dc3a68d1a13e` |
| Unicode session after import | `f3f98df50dfc0eaf7ce498016e1cc637c4a00ff71fcbbbc609d7048c28afd968` |
| Generated gallery HTML | `30f1701b94fd9711fdcbab3a484a151e3a049682ace9ff2219c41ece3dba3bd5` |
| Generated gallery manifest | `262b0d21b4e56c1f2e8c9e6108bd5097b5ed0f15b28b45f0c63c34d951af0c65` |
| Personal marketplace unchanged baseline | `422580558aa3790de35022394fc5b29eb3e15af1bea4e419bd615c95169598e6` |

Aggregate hashes use sorted relative paths encoded as `path + NUL + file_sha256_hex + LF`. Runtime bytecode and environments are excluded from payload enumeration and were not copied.

All 66 non-manifest payload files match source bytes; all 67 personal/cache files match each other. Parsed manifests match after changing only the cachebuster version back to `0.5.0`. The official helper additionally serializes Korean `메모` as JSON Unicode escapes, so raw manifest bytes differ by the version suffix **and that equivalent serialization**; raw byte-only equality after suffix removal is not claimed.

### Exact installed helper invocations

Each line was executed once in sequence, with a 60-second subprocess bound; repeated prompt/gallery cases are deliberate scenarios, not retries. The numbered exit codes are preserved below. Concept text is fixture data passed through an argv list; the displayed shell quoting is for readable reproduction.

```sh
# cli-01-presets.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py icon-presets
# cli-02-icon-init.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py init --session icon-fixture --brief /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon-brief.json
# cli-03-icon-prompt.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py prompt --session icon-fixture --concept 'INSTALLATION FIXTURE ONLY; preserve exact Unicode 메모 and literal data: $(touch /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/SHOULD_NOT_EXIST) `touch /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/SHOULD_NOT_EXIST` <script>globalThis.fixtureExecuted=true</script>' --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon.json
# cli-04-cancel-resume-show.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py show --session icon-fixture
# cli-05-repeat-prompt.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py prompt --session icon-fixture --concept 'INSTALLATION FIXTURE ONLY; preserve exact Unicode 메모 and literal data: $(touch /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/SHOULD_NOT_EXIST) `touch /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/SHOULD_NOT_EXIST` <script>globalThis.fixtureExecuted=true</script>' --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon.json
# cli-06-malformed-prompt.json; exit 1
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py prompt --session icon-fixture --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/malformed-icon.json
# cli-07-malformed-import.json; exit 1
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py import --session icon-fixture --artifact fixture-logo --image /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/logo.png --prompt-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon-prompt.txt --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/malformed-icon.json --revision 0
# cli-08-icon-import.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py import --session icon-fixture --artifact fixture-logo --image /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/logo.png --prompt-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon-prompt.txt --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon.json --revision 0
# cli-09-stale-import.json; exit 1
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py import --session icon-fixture --artifact fixture-logo --image /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/logo.png --prompt-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon-prompt.txt --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon.json --revision 0
# cli-10-duplicate-import.json; exit 1
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py import --session icon-fixture --artifact fixture-logo --image /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/logo.png --prompt-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon-prompt.txt --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/icon.json --revision 1
# cli-11-icon-show.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py show --session icon-fixture
# cli-12-icon-gallery.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py icon-gallery --session icon-fixture --artifacts fixture-logo --output gallery
# cli-13-repeat-gallery.json; exit 1
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py icon-gallery --session icon-fixture --artifacts fixture-logo --output gallery
# cli-14-brand-init.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py init --session brand-fixture --brief /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/brand-brief.json
# cli-15-brand-prompt.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py prompt --session brand-fixture --concept 'INSTALLATION FIXTURE ONLY: existing logo PNG for non-icon compatibility'
# cli-16-brand-import.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py import --session brand-fixture --artifact brand-logo --image /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/logo.png --prompt-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/brand-prompt.txt --revision 0
# cli-17-brand-show.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py show --session brand-fixture
# cli-18-unicode-init.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py init --session unicode-fixture --brief /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/unicode-brief.json
# cli-19-unicode-prompt.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py prompt --session unicode-fixture --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/unicode-icon.json
# cli-20-unicode-import.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py import --session unicode-fixture --artifact unicode-logo --image /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/logo.png --prompt-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/unicode-prompt.txt --app-icon-file /private/tmp/logo-land-icons-install-task_a0fb416de8be/inputs/unicode-icon.json --revision 0
# cli-21-unicode-gallery.json; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land/scripts/logo_project.py icon-gallery --session unicode-fixture --artifacts unicode-logo --output unicode-gallery
```

### Official administrative commands

```sh
# marketplace; exit 0
python3 '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/read_marketplace_name.py'
# source-plugin-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/validate_plugin.py' /Users/cillian/Documents/Github/Projects/logo-generator
# source-skill-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/skill-creator/scripts/quick_validate.py' /Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land
# source-lock-check; exit 0
uv lock --check --project /Users/cillian/Documents/Github/Projects/logo-generator
# cachebuster; exit 0
python3 '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py' /Users/cillian/plugins/logo-land
# plugin-add; exit 0
codex plugin add logo-land@personal --json
# personal-plugin-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/validate_plugin.py' /Users/cillian/plugins/logo-land
# personal-skill-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/skill-creator/scripts/quick_validate.py' /Users/cillian/plugins/logo-land/skills/logo-land
# personal-lock-check; exit 0
uv lock --check --project /Users/cillian/plugins/logo-land
# cache-plugin-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/validate_plugin.py' /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735
# cache-skill-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/skill-creator/scripts/quick_validate.py' /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735/skills/logo-land
# cache-lock-check; exit 0
uv lock --check --project /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735
```

Actual initial Codex installation receipt:

```json
{
  "pluginId": "logo-land@personal",
  "name": "logo-land",
  "marketplaceName": "personal",
  "version": "0.5.0+codex.20260912171735",
  "installedPath": "/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/plugins/cache/personal/logo-land/0.5.0+codex.20260912171735",
  "authPolicy": "ON_INSTALL"
}
```

### Verification wrapper corrections and limits

- The first payload-check wrapper used system python3 without tomllib and exited before checking anything; TOML reading now uses the existing repository Python.
- The second wrapper expected raw manifest equality after suffix replacement and stopped: the official cachebuster also JSON-escapes Korean 메모 as \uba54\ubaa8. Parsed manifest objects are equal after replacing only version. No product failure or helper/suite retry occurred.
- The smoke wrapper stopped after successful brand-prompt because it expected app_icon:null in PromptResult; the compatible CLI omits absent optional fields. The remaining workflow uses get(app_icon), resumes the existing state, and does not repeat completed calls.

No failed helper suite was retried and no production code was changed for QA. No new image, synthetic generated-icon claim, visual approval, native-image gate, export/store acceptance, cold dependency-cache install, or fresh Codex GUI-thread skill pickup is claimed. Published `0.3.1` and prior draft `0.4.0` release state are unchanged; the 0.5.0 payload is a personal development installation. A new Codex thread is required to pick up the refreshed skill in the UI.

The coordinator requested a final refresh after another owner updates the demonstration paragraph in `skills/logo-land/references/app-icons.md`; initial CLI evidence above remains valid for the initial installed version. Final refresh and cleanup evidence follow when that dependency settles.

### Captured tmux preset output

```json
[
  {
    "id": "ip_mascot",
    "label": "IP mascot",
    "description": "Simple personified character with rounded heavy forms and two subject color families on a solid background.",
    "default_placement": "lower_left"
  },
  {
    "id": "pictogram",
    "label": "Pictogram",
    "description": "One immediately recognizable silhouette with clean flat shapes.",
    "default_placement": "center"
  },
  {
    "id": "abstract",
    "label": "Abstract",
    "description": "A compact geometric composition with clear negative space.",
    "default_placement": "center"
  },
  {
    "id": "monogram",
    "label": "Monogram",
    "description": "One to eight exact Unicode characters shaped as readable lettering.",
    "default_placement": "center"
  },
  {
    "id": "soft_3d",
    "label": "Soft 3D",
    "description": "A tactile, softly rounded object with restrained depth and lighting.",
    "default_placement": "center"
  },
  {
    "id": "pixel_art",
    "label": "Pixel art",
    "description": "Deliberate block geometry on a consistent pixel grid.",
    "default_placement": "center"
  }
]
```

No cooperative session locks remained after the installed commands. The complete stored icon brief matches the bundled example, and the non-icon artifact lockup matches the unchanged non-icon input brief. All 131 protected historical installation evidence files remained byte-identical at this checkpoint.

## Initial per-file payload comparison

The 55 previous personal/cache files were byte-identical before update. The following table retains every source and installed digest; a dash means the path was new in 0.5.0. The personal 0.5.0 column is identical to installed in every row. A final documentation-only refresh, if any, is recorded separately below.

| Relative path | Previous 0.4.0 SHA-256 | Initial source 0.5.0 SHA-256 | Initial installed SHA-256 |
| --- | --- | --- | --- |
| `.codex-plugin/plugin.json` | `730f24dc6f11f8a9cb0e6a8045b6b2ae1e098b0b1537759342d344ef599528cf` | `ad9560c7b0db2a2b17286022834100d1b3c41f6a8b6a044223cef382577f2b9f` | `883fd74a778067752f192651184c5f4c373fe69d167e6473b8b8906dcfa1e91a` |
| `THIRD_PARTY_NOTICES.md` | `5cc1decfc100d23ab9d79c9b893c108db9aa40dc08465489ef1adf250434a4d2` | `ba5f0db63846caf31dd049f2d171442701767692f3825c38c0cccfa79c714b99` | `ba5f0db63846caf31dd049f2d171442701767692f3825c38c0cccfa79c714b99` |
| `assets/logo-transparent.png` | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |
| `assets/logo.png` | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| `pyproject.toml` | `3873f84390ebb17f3b3faaeb1483525f15f099da405e79b4d40569d7d4c3814d` | `27098c173db9c4c3e69d760501e19fde7877f69af2b592c951499c649fcf7fac` | `27098c173db9c4c3e69d760501e19fde7877f69af2b592c951499c649fcf7fac` |
| `skills/.gitkeep` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `skills/logo-land/SKILL.md` | `885ffeea30d8cea3a18a78dcc8a0636b5c9d47cdbdc9b2d0a153dc178b9d4208` | `3dac44b63f34d89a49990ff818105c664bc1953cbb1bd60e102a6dae2ef2cc0a` | `3dac44b63f34d89a49990ff818105c664bc1953cbb1bd60e102a6dae2ef2cc0a` |
| `skills/logo-land/agents/openai.yaml` | `26e73fa8f7fa5c8296639b69e2eab5feaf014b2ad73f54581278c2230a659a74` | `26e73fa8f7fa5c8296639b69e2eab5feaf014b2ad73f54581278c2230a659a74` | `26e73fa8f7fa5c8296639b69e2eab5feaf014b2ad73f54581278c2230a659a74` |
| `skills/logo-land/assets/app-icon-gallery.template.html` | - | `960c682d45807c8a7f1a0dfb5f031f6a17f3fb6d4ca0c84501514375bd8cb9dd` | `960c682d45807c8a7f1a0dfb5f031f6a17f3fb6d4ca0c84501514375bd8cb9dd` |
| `skills/logo-land/assets/app-icon.example.json` | - | `2477e1384ba781a44a0116f4a86c71a85cdea3e4030ae6c388e28c1779685fbc` | `2477e1384ba781a44a0116f4a86c71a85cdea3e4030ae6c388e28c1779685fbc` |
| `skills/logo-land/assets/brief.example.json` | `2841dbbba9e3d94759c1a1b5ccc2885b8a94a87e7ede81f0786d0b7d31155342` | `2841dbbba9e3d94759c1a1b5ccc2885b8a94a87e7ede81f0786d0b7d31155342` | `2841dbbba9e3d94759c1a1b5ccc2885b8a94a87e7ede81f0786d0b7d31155342` |
| `skills/logo-land/assets/color-gallery.template.html` | `65c0745614f866f670a94068503552c9982ef48c1a6697f05943ac999cea6773` | `65c0745614f866f670a94068503552c9982ef48c1a6697f05943ac999cea6773` | `65c0745614f866f670a94068503552c9982ef48c1a6697f05943ac999cea6773` |
| `skills/logo-land/assets/ip-as-logo.LICENSE` | - | `b8f39925b1c36ca531c5e663aeb7ba427f94a526495785b4d1b2797fae8f2546` | `b8f39925b1c36ca531c5e663aeb7ba427f94a526495785b4d1b2797fae8f2546` |
| `skills/logo-land/references/app-icons.md` | - | `1ce8dcbd2899b796640414c3ab811666236eda243cc0426a86ea58b754fb09e7` | `1ce8dcbd2899b796640414c3ab811666236eda243cc0426a86ea58b754fb09e7` |
| `skills/logo-land/references/color-providers.md` | `285199155af770b052e1d7aa2ec92bb687320d1f5aebe6008eadc3ca0e61af8f` | `285199155af770b052e1d7aa2ec92bb687320d1f5aebe6008eadc3ca0e61af8f` | `285199155af770b052e1d7aa2ec92bb687320d1f5aebe6008eadc3ca0e61af8f` |
| `skills/logo-land/references/color-workflow.md` | `3f2f3d941fc5f72f64b0900059477e3f1fb2748b2bcdd4fdea24c1361f897b06` | `3f2f3d941fc5f72f64b0900059477e3f1fb2748b2bcdd4fdea24c1361f897b06` | `3f2f3d941fc5f72f64b0900059477e3f1fb2748b2bcdd4fdea24c1361f897b06` |
| `skills/logo-land/references/delivery-checks.md` | `2f6aad601457654886dc6edb8065e4a91ef8719a3c2982becfc62a217ad604d8` | `2f6aad601457654886dc6edb8065e4a91ef8719a3c2982becfc62a217ad604d8` | `2f6aad601457654886dc6edb8065e4a91ef8719a3c2982becfc62a217ad604d8` |
| `skills/logo-land/references/ip-mascot.md` | - | `08f93b78555246ea3b71a11d4879a53790808df4cab400bd5ed84b6d409e4850` | `08f93b78555246ea3b71a11d4879a53790808df4cab400bd5ed84b6d409e4850` |
| `skills/logo-land/references/logo-directions.md` | `06eaf7c2e48bc93743f2dd76915105687bacc5a25a810932d5514bcf771049bc` | `06eaf7c2e48bc93743f2dd76915105687bacc5a25a810932d5514bcf771049bc` | `06eaf7c2e48bc93743f2dd76915105687bacc5a25a810932d5514bcf771049bc` |
| `skills/logo-land/references/native-image.md` | `13034c5cd62ef5e982f6cc976f64187577ede26e6b47aa6ade8d94369b1e2735` | `34056909420a4db68be7d00b09a18aabd450221529f814d73b7642369f096c3f` | `34056909420a4db68be7d00b09a18aabd450221529f814d73b7642369f096c3f` |
| `skills/logo-land/references/project-files.md` | `68070bae3c5d693365644e152191f421071ffc2ecc136a152f29cc6fc11141ac` | `f3f635a78005d3059885f6c55b69d3e07cd1e7fc92026a38be66555b155fcb42` | `f3f635a78005d3059885f6c55b69d3e07cd1e7fc92026a38be66555b155fcb42` |
| `skills/logo-land/references/typography.md` | `137a3f88cb1287e31650d327399b66061e0ab6a5da8f246a48f005433ca8b56d` | `137a3f88cb1287e31650d327399b66061e0ab6a5da8f246a48f005433ca8b56d` | `137a3f88cb1287e31650d327399b66061e0ab6a5da8f246a48f005433ca8b56d` |
| `skills/logo-land/scripts/logo_helper/__init__.py` | `23c8d2ce225a99efe9832a41c20b46d139f5b31049dd641a04e13ff83b84f4d0` | `23c8d2ce225a99efe9832a41c20b46d139f5b31049dd641a04e13ff83b84f4d0` | `23c8d2ce225a99efe9832a41c20b46d139f5b31049dd641a04e13ff83b84f4d0` |
| `skills/logo-land/scripts/logo_helper/app_icon_cli.py` | - | `e09075977adfd8c0b98202242ab3759fb1145227df987aeaac33c31896d35ada` | `e09075977adfd8c0b98202242ab3759fb1145227df987aeaac33c31896d35ada` |
| `skills/logo-land/scripts/logo_helper/app_icon_gallery.py` | - | `71a2a7873af195cdeefe312f6d0462552fd1bb8856c117b5a20349649371e43f` | `71a2a7873af195cdeefe312f6d0462552fd1bb8856c117b5a20349649371e43f` |
| `skills/logo-land/scripts/logo_helper/app_icon_guide.py` | - | `c063bf22bbcfa82c982caa2c066db2b069b34f8d633ba3f6afdb1e9d4fd17012` | `c063bf22bbcfa82c982caa2c066db2b069b34f8d633ba3f6afdb1e9d4fd17012` |
| `skills/logo-land/scripts/logo_helper/app_icon_models.py` | - | `21ba823e490677f5e70ce9d05c782b1fa12884f405c4ba4601fd052bb1209c2d` | `21ba823e490677f5e70ce9d05c782b1fa12884f405c4ba4601fd052bb1209c2d` |
| `skills/logo-land/scripts/logo_helper/app_icon_presets.py` | - | `0b7a5a4e01363a7f1bc1513a1c4bdba423d906edf722b322dab3253abfd849ae` | `0b7a5a4e01363a7f1bc1513a1c4bdba423d906edf722b322dab3253abfd849ae` |
| `skills/logo-land/scripts/logo_helper/app_icon_prompts.py` | - | `38fbf3cfdb3efd97da4b96eb554cd392f5ae06cb1d8cb12a27822729b280c015` | `38fbf3cfdb3efd97da4b96eb554cd392f5ae06cb1d8cb12a27822729b280c015` |
| `skills/logo-land/scripts/logo_helper/app_icon_publish.py` | - | `fb4dea5c484a4c617e898626d324a1aed5335e7b853299f45827d15d8a652ae5` | `fb4dea5c484a4c617e898626d324a1aed5335e7b853299f45827d15d8a652ae5` |
| `skills/logo-land/scripts/logo_helper/artifact_models.py` | `e2c4303d722fb888fe9291c99d07926a9865b160a8620297817ef3a665db96ee` | `f35d32f2da234e92dd5144d48eb62fbddfac3039dd079b4d0a5d35eccd3231f0` | `f35d32f2da234e92dd5144d48eb62fbddfac3039dd079b4d0a5d35eccd3231f0` |
| `skills/logo-land/scripts/logo_helper/brief_models.py` | `cf3467616aeb0264fdf7931d1f203a980205acaf802f3461601865a0b063227e` | `caea33b207c181391fde6d9bc4fc7826335a8d2eb47f7124b51e5fbb18d16b12` | `caea33b207c181391fde6d9bc4fc7826335a8d2eb47f7124b51e5fbb18d16b12` |
| `skills/logo-land/scripts/logo_helper/cli_options.py` | `211702fc69d598742f2f2f0ffd0b2dadaf89f9f8ff7032615e4303a4fd7b8814` | `e3f697458b482079c27b446cbb56aef4c6cf38ce3cd49ca94f1600ab76f4c8d3` | `e3f697458b482079c27b446cbb56aef4c6cf38ce3cd49ca94f1600ab76f4c8d3` |
| `skills/logo-land/scripts/logo_helper/color_analysis.py` | `cfcef1c51c0f7a4067b7e9317df5b6f4acdb5312036e37516c9aab16f2d0ba30` | `cfcef1c51c0f7a4067b7e9317df5b6f4acdb5312036e37516c9aab16f2d0ba30` | `cfcef1c51c0f7a4067b7e9317df5b6f4acdb5312036e37516c9aab16f2d0ba30` |
| `skills/logo-land/scripts/logo_helper/color_cli.py` | `d731f309d0dc877eb9f0ec71bf733c2461cda8757f9f15ac38fe7d0d7b9e3809` | `d731f309d0dc877eb9f0ec71bf733c2461cda8757f9f15ac38fe7d0d7b9e3809` | `d731f309d0dc877eb9f0ec71bf733c2461cda8757f9f15ac38fe7d0d7b9e3809` |
| `skills/logo-land/scripts/logo_helper/color_delivery.py` | `7e7f0a4745def5b15ad08699dc57b113eca97eeeaa9b2aefaba35ef138d98f55` | `7e7f0a4745def5b15ad08699dc57b113eca97eeeaa9b2aefaba35ef138d98f55` | `7e7f0a4745def5b15ad08699dc57b113eca97eeeaa9b2aefaba35ef138d98f55` |
| `skills/logo-land/scripts/logo_helper/color_gallery.py` | `05076788df31137f3ca6576a58346533130f2dd710779e35eb9311370ae6b56d` | `05076788df31137f3ca6576a58346533130f2dd710779e35eb9311370ae6b56d` | `05076788df31137f3ca6576a58346533130f2dd710779e35eb9311370ae6b56d` |
| `skills/logo-land/scripts/logo_helper/color_gallery_cards.py` | `253ba8f0a439a4bb8129d2cb43463d5897df2d42cc9528ee627f8c709d669a53` | `253ba8f0a439a4bb8129d2cb43463d5897df2d42cc9528ee627f8c709d669a53` | `253ba8f0a439a4bb8129d2cb43463d5897df2d42cc9528ee627f8c709d669a53` |
| `skills/logo-land/scripts/logo_helper/color_gallery_data.py` | `81dbf0876dc5cdc6e21493e80098489f54bc8e39dcb13bd3e61a38c5b998a030` | `81dbf0876dc5cdc6e21493e80098489f54bc8e39dcb13bd3e61a38c5b998a030` | `81dbf0876dc5cdc6e21493e80098489f54bc8e39dcb13bd3e61a38c5b998a030` |
| `skills/logo-land/scripts/logo_helper/color_guide.py` | `34cdb38dddc6b398376fe5b492eef1799052b0b82a47bb48f3f4b801ea6f424a` | `34cdb38dddc6b398376fe5b492eef1799052b0b82a47bb48f3f4b801ea6f424a` | `34cdb38dddc6b398376fe5b492eef1799052b0b82a47bb48f3f4b801ea6f424a` |
| `skills/logo-land/scripts/logo_helper/color_math.py` | `aa677d064632e48a9d108ba5d0b818c57f589ba1bcb61406261d8502cdc86288` | `aa677d064632e48a9d108ba5d0b818c57f589ba1bcb61406261d8502cdc86288` | `aa677d064632e48a9d108ba5d0b818c57f589ba1bcb61406261d8502cdc86288` |
| `skills/logo-land/scripts/logo_helper/color_models.py` | `d3b4093611e2aa2d095c6c4f9027e65c794ef8b836c89d4a24c554f4a720f547` | `d3b4093611e2aa2d095c6c4f9027e65c794ef8b836c89d4a24c554f4a720f547` | `d3b4093611e2aa2d095c6c4f9027e65c794ef8b836c89d4a24c554f4a720f547` |
| `skills/logo-land/scripts/logo_helper/color_profiles.py` | `055a299c1bd6738add1b44ad8977ffb48b9a3310bb9387665daa6efe04ca34df` | `055a299c1bd6738add1b44ad8977ffb48b9a3310bb9387665daa6efe04ca34df` | `055a299c1bd6738add1b44ad8977ffb48b9a3310bb9387665daa6efe04ca34df` |
| `skills/logo-land/scripts/logo_helper/color_reports.py` | `95cf4f2605c8ca248a489d4e53fafee9f18b663d6effd38f3b5e5d080dd5596d` | `95cf4f2605c8ca248a489d4e53fafee9f18b663d6effd38f3b5e5d080dd5596d` | `95cf4f2605c8ca248a489d4e53fafee9f18b663d6effd38f3b5e5d080dd5596d` |
| `skills/logo-land/scripts/logo_helper/color_sampling.py` | `71946e9eda8b329b5cafffc0163161abd2b17ddab3c92184bc5d4ba99ad94330` | `71946e9eda8b329b5cafffc0163161abd2b17ddab3c92184bc5d4ba99ad94330` | `71946e9eda8b329b5cafffc0163161abd2b17ddab3c92184bc5d4ba99ad94330` |
| `skills/logo-land/scripts/logo_helper/color_workflow.py` | `7ef6e5c33c7f56d2320a643f5cd99428555b9eb4fa24fe65857b96147379cc42` | `7ef6e5c33c7f56d2320a643f5cd99428555b9eb4fa24fe65857b96147379cc42` | `7ef6e5c33c7f56d2320a643f5cd99428555b9eb4fa24fe65857b96147379cc42` |
| `skills/logo-land/scripts/logo_helper/delivery.py` | `06769f0caafd791125ac29b91e8b0ff45b655ca976a36461e04c7c898a82f77a` | `ed3713421b316e43568641451f41fc5a71332608acc8b8b2bf6c1db6f4469859` | `ed3713421b316e43568641451f41fc5a71332608acc8b8b2bf6c1db6f4469859` |
| `skills/logo-land/scripts/logo_helper/export_bundle.py` | `33de44fb7677569d65c7b883c6d5b098c998e19bd9f731a6138ee9c09a1de612` | `33de44fb7677569d65c7b883c6d5b098c998e19bd9f731a6138ee9c09a1de612` | `33de44fb7677569d65c7b883c6d5b098c998e19bd9f731a6138ee9c09a1de612` |
| `skills/logo-land/scripts/logo_helper/images.py` | `bd3d03ce8ab8fc7c6767da8fe8269e688ee63f16e14f04bf21d0e9d631a15f0a` | `bd3d03ce8ab8fc7c6767da8fe8269e688ee63f16e14f04bf21d0e9d631a15f0a` | `bd3d03ce8ab8fc7c6767da8fe8269e688ee63f16e14f04bf21d0e9d631a15f0a` |
| `skills/logo-land/scripts/logo_helper/import_reports.py` | `69ffb9f6a9dbe5ac149fb9113f36ff63067cbad244c8c3a48af919e30223691c` | `69ffb9f6a9dbe5ac149fb9113f36ff63067cbad244c8c3a48af919e30223691c` | `69ffb9f6a9dbe5ac149fb9113f36ff63067cbad244c8c3a48af919e30223691c` |
| `skills/logo-land/scripts/logo_helper/intent.py` | `e07e81a6b2827057e7159edcdc311fbd596b4c411daffbff8057d7e3a1174c37` | `244d7f1f4b0b07fa733c968ad130b84f9084719059f562385d55891e749b47fa` | `244d7f1f4b0b07fa733c968ad130b84f9084719059f562385d55891e749b47fa` |
| `skills/logo-land/scripts/logo_helper/legacy_state.py` | `09119091b50d9a4b8d9e4782636a8cddbd93b0d0fd197c774c129d2bc8ac3c5d` | `09119091b50d9a4b8d9e4782636a8cddbd93b0d0fd197c774c129d2bc8ac3c5d` | `09119091b50d9a4b8d9e4782636a8cddbd93b0d0fd197c774c129d2bc8ac3c5d` |
| `skills/logo-land/scripts/logo_helper/lockup_models.py` | `0c0fb574ca59d4e6bb72ef26df4dcc36e013e354901840f4bf7cb30291c035cc` | `0c0fb574ca59d4e6bb72ef26df4dcc36e013e354901840f4bf7cb30291c035cc` | `0c0fb574ca59d4e6bb72ef26df4dcc36e013e354901840f4bf7cb30291c035cc` |
| `skills/logo-land/scripts/logo_helper/model_base.py` | `0051b0fc239944f0143da201848f98d8c414c9d2d520f5de4f4718c88756c49e` | `0051b0fc239944f0143da201848f98d8c414c9d2d520f5de4f4718c88756c49e` | `0051b0fc239944f0143da201848f98d8c414c9d2d520f5de4f4718c88756c49e` |
| `skills/logo-land/scripts/logo_helper/models.py` | `e5d1fb3c9306ffea0f91a95dc6307f8a739e6bd51bec92ebc1521cfc9d1596de` | `dc28d55027542510328ebdf80a820ed3456e6f6cfbd00cae102395026a0079ca` | `dc28d55027542510328ebdf80a820ed3456e6f6cfbd00cae102395026a0079ca` |
| `skills/logo-land/scripts/logo_helper/palette_proposals.py` | `6968ca4356be8197ffdd68500ea2f53c72dff935c743e57305bb7ae4e10aca4b` | `6968ca4356be8197ffdd68500ea2f53c72dff935c743e57305bb7ae4e10aca4b` | `6968ca4356be8197ffdd68500ea2f53c72dff935c743e57305bb7ae4e10aca4b` |
| `skills/logo-land/scripts/logo_helper/palettes.py` | `6c60dffcca290bd390e1259600cdd91e190589995af6c42152ba42f719d77e08` | `6c60dffcca290bd390e1259600cdd91e190589995af6c42152ba42f719d77e08` | `6c60dffcca290bd390e1259600cdd91e190589995af6c42152ba42f719d77e08` |
| `skills/logo-land/scripts/logo_helper/prompts.py` | `bdd82290a025c747c7f5962a48d693f955f9ac0309a68feb1e60c80ee98409c9` | `340974db2816c5f0deecc766cfcabd8036d8e59e2608be5f1688657b57967a1b` | `340974db2816c5f0deecc766cfcabd8036d8e59e2608be5f1688657b57967a1b` |
| `skills/logo-land/scripts/logo_helper/reference_decode.py` | `b55055f40a5fee8a01943acd082bfe8b7a521b61bb1773f36a208f5e5f9c453f` | `b55055f40a5fee8a01943acd082bfe8b7a521b61bb1773f36a208f5e5f9c453f` | `b55055f40a5fee8a01943acd082bfe8b7a521b61bb1773f36a208f5e5f9c453f` |
| `skills/logo-land/scripts/logo_helper/reference_evidence.py` | `ab80fa6b9a19f77b525566c9f4b8129720dee403daea9994155e0888e2d0d1f4` | `ab80fa6b9a19f77b525566c9f4b8129720dee403daea9994155e0888e2d0d1f4` | `ab80fa6b9a19f77b525566c9f4b8129720dee403daea9994155e0888e2d0d1f4` |
| `skills/logo-land/scripts/logo_helper/reference_models.py` | `87da637a01602f5dd0655ff6e8bfefae9ca2c609513dcbfe43a9f5e07553064e` | `87da637a01602f5dd0655ff6e8bfefae9ca2c609513dcbfe43a9f5e07553064e` | `87da637a01602f5dd0655ff6e8bfefae9ca2c609513dcbfe43a9f5e07553064e` |
| `skills/logo-land/scripts/logo_helper/references.py` | `a02f6d9bf3775820bc4d394d539186c64da7ce96cb00a359e34e266acec4d3b7` | `a02f6d9bf3775820bc4d394d539186c64da7ce96cb00a359e34e266acec4d3b7` | `a02f6d9bf3775820bc4d394d539186c64da7ce96cb00a359e34e266acec4d3b7` |
| `skills/logo-land/scripts/logo_helper/session_models.py` | `3d5917431dd8c8f7f43c2acc91dd845682b0d8483e1de835ba5794eda3dcdaea` | `3d5917431dd8c8f7f43c2acc91dd845682b0d8483e1de835ba5794eda3dcdaea` | `3d5917431dd8c8f7f43c2acc91dd845682b0d8483e1de835ba5794eda3dcdaea` |
| `skills/logo-land/scripts/logo_helper/storage.py` | `e0a9bd8c18458beeda1a0ad9479afbec68ac6c4690b42f795dc3cdbd813b42a6` | `e0a9bd8c18458beeda1a0ad9479afbec68ac6c4690b42f795dc3cdbd813b42a6` | `e0a9bd8c18458beeda1a0ad9479afbec68ac6c4690b42f795dc3cdbd813b42a6` |
| `skills/logo-land/scripts/logo_helper/workflow.py` | `df902eecc517bd89deeac3f14537b7c1eb96129e683682e31fee530f42d5d417` | `a82d1cd1c02a16b4c202c1a01d08a6a5e44f18491d297bc01857c663dbbbd6d6` | `a82d1cd1c02a16b4c202c1a01d08a6a5e44f18491d297bc01857c663dbbbd6d6` |
| `skills/logo-land/scripts/logo_project.py` | `ccbe591a8ba0f3a1445da80726a3f9d4c706f33759bb361363c96c189bbc4e79` | `1bc33dbe2f06accd050aa069315d4b7bed0470a95bed10e18b5090b98eddd5fa` | `1bc33dbe2f06accd050aa069315d4b7bed0470a95bed10e18b5090b98eddd5fa` |
| `uv.lock` | `2f021b71a126f5007c9e08692b46f63769cb5bbec2225e8ea28fd105d8574b80` | `58f67b2fddede767b60e03d368bf694fac788f96f024360f867f59c17a672150` | `58f67b2fddede767b60e03d368bf694fac788f96f024360f867f59c17a672150` |

Final-refresh smoke reuses registered tmux session name `ll-icons-install` from the same independent workspace; new owned pane PID `29514` was registered before input.

## Final installed payload and smoke

**PASS, final retained version `0.5.0+codex.20260912172956`.** The coordinator confirmed the final reference was stable before refresh. The only source payload change since initial QA is `skills/logo-land/references/app-icons.md`, correcting legacy style guidance and recording the eleven native catalog samples produced by other workers. This worker made no native call and does not claim their samples as this installation fixture. All runtime Python files, templates, examples and dependency files are byte-identical to the initially exercised payload.

The existing personal files were rechecked against the initial installation hashes before copying the single changed reference through registered staging. The official marketplace-name helper, default cachebuster and `codex plugin add logo-land@personal --json` succeeded again. Source remains pure `0.5.0`; no manual marketplace/config edits occurred.

- Repository source: `/Users/cillian/Documents/Github/Projects/logo-generator`.
- Personal source: `/Users/cillian/plugins/logo-land`.
- Actual CLI-returned cache: `/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956`.
- Resolved cache used for CLI QA: `/Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956`.
- Actual final helper: `/Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956/skills/logo-land/scripts/logo_project.py`.

The CLI-returned and resolved cache directories were verified to be the same filesystem directory. All **67** final personal/cache files are byte-identical. All **66** non-manifest files match final source bytes, and manifests differ only in the version value plus the official equivalent Unicode JSON serialization already described. Final source aggregate: `a121e39419fd8c8254139dcccf33f1b59b1f12941ee34ba47e1c590d7eb07c97`; final installed aggregate: `74f05b70165cf04c0b3c0efb8684c127ffbece0eff99c274644f02c856a9a6e9`.

Only these rows change from the complete initial comparison table; all other rows remain exact:

| Path | Final source SHA-256 | Final personal/cache SHA-256 |
| --- | --- | --- |
| `.codex-plugin/plugin.json` | `ad9560c7b0db2a2b17286022834100d1b3c41f6a8b6a044223cef382577f2b9f` | `f6395a77a9e4f57aa94566c3bad339078835c1013840ddfd3e316aaa73aaa307` |
| `skills/logo-land/references/app-icons.md` | `6c2abb131dcc66db64fa0c701a97a9e291d0da42e430b43a3331a8e7f19ed2f2` | `6c2abb131dcc66db64fa0c701a97a9e291d0da42e430b43a3331a8e7f19ed2f2` |

Official plugin and skill validators passed again for source, personal payload and final cache; final installed `uv lock --check` passed. The retained helper SHA-256 is `1bc33dbe2f06accd050aa069315d4b7bed0470a95bed10e18b5090b98eddd5fa`.

The short final smoke ran `show` against the previously imported icon fixture from a fresh installed-helper process and verified exact state bytes, then invoked the final absolute installed helper in tmux to verify the six preset IDs and exit 0. The final pane PID was `29514`; it was killed after capture. The 21-call suite and HTTP download were not repeated for a documentation-only update. Across both versions there were **24 new-cache helper invocations: 19 successes and 5 expected refusals**, including two tmux invocations; the separate prior-0.4.0 RED check exited 2.

```sh
tmux send-keys -t ll-icons-install 'uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956/skills/logo-land/scripts/logo_project.py icon-presets' Enter
tmux capture-pane -pt ll-icons-install -S -200
# final-marketplace; exit 0
python3 '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/read_marketplace_name.py'
# final-cachebuster; exit 0
python3 '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/update_plugin_cachebuster.py' /Users/cillian/plugins/logo-land
# final-plugin-add; exit 0
codex plugin add logo-land@personal --json
# final-source-plugin-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/validate_plugin.py' /Users/cillian/Documents/Github/Projects/logo-generator
# final-source-skill-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/skill-creator/scripts/quick_validate.py' /Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land
# final-personal-plugin-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/validate_plugin.py' /Users/cillian/plugins/logo-land
# final-personal-skill-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/skill-creator/scripts/quick_validate.py' /Users/cillian/plugins/logo-land/skills/logo-land
# final-cache-plugin-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/plugin-creator/scripts/validate_plugin.py' /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956
# final-cache-skill-validator; exit 0
uv run --isolated --no-project --with PyYAML==6.0.2 python '/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/skills/.system/skill-creator/scripts/quick_validate.py' /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956/skills/logo-land
# final-cache-lock-check; exit 0
uv lock --check --project /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956
# final-smoke-show; exit 0
uv run /Users/cillian/.codex/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956/skills/logo-land/scripts/logo_project.py show --session icon-fixture
```

Final actual Codex installation receipt:

```json
{
  "pluginId": "logo-land@personal",
  "name": "logo-land",
  "marketplaceName": "personal",
  "version": "0.5.0+codex.20260912172956",
  "installedPath": "/Users/cillian/Library/Application Support/orca/codex-accounts/f2ae4d55-4afe-4e94-88a3-ace3a4ff86da/home/plugins/cache/personal/logo-land/0.5.0+codex.20260912172956",
  "authPolicy": "ON_INSTALL"
}
```

### Final evidence preservation before cleanup

All original dirty-tree paths still exist. The worker preserved the source/runtime payload and **131** historical installation-evidence files; the final reference change was owned by the catalog worker and explicitly requested for installation. The personal marketplace SHA-256 remained `422580558aa3790de35022394fc5b29eb3e15af1bea4e419bd615c95169598e6`. The independent dirty fixture, three session trees, original fixture PNG, exact prompt files and gallery files retained their verified hashes through final smoke. No lock or shell/script execution sentinel remained.

The following receipt digests preserve the complete temporary evidence inventory. Command argv, principal outcomes, state/PNG/prompt/payload hashes and actual install receipts are retained above; temporary full CLI stdout/log files are intentionally removed with the workspace.

| Temporary evidence file | SHA-256 |
| --- | --- |
| `cache-lock-check.json` | `8a2579df8cdb045667e53f5eb01c4d903b8c762cf12e0fc698ac2673e24d50d7` |
| `cache-plugin-validator.json` | `479c249d0c7db132cd001be810c8172c9a1040838c02a7ad812b2b06947e36a3` |
| `cache-skill-validator.json` | `d84233cc8030756b56efb008c510b1240b4369bfc8f4b663f39e90109fffa32f` |
| `cachebuster.json` | `274afe6f071c830127aed2e20b46cd3ef776fcacee18cc09eca067aec224c87a` |
| `cli-01-presets.json` | `ee11d2d39fb4cd4289bd4f1a82b0d206fbd3f7de3a62b723648873e31ed81a2c` |
| `cli-02-icon-init.json` | `6168eb3eaadef45db357106dd5b3be19df51f4e78a5c6f9ce7896f6d19288220` |
| `cli-03-icon-prompt.json` | `f74bafb871ede17c231a4e91508628b85d384897045fbd2da056a5a2c8f19df1` |
| `cli-04-cancel-resume-show.json` | `92d39c1cd78d6d2978f6cc33997be38ddaa64d8c020eaaa1d56a105dff07d051` |
| `cli-05-repeat-prompt.json` | `c8b72316f0714239f5fd3e4ddf0ffd57d6c20d1fbf7cc827a211f5df3d420a14` |
| `cli-06-malformed-prompt.json` | `ed56b35cc83418847f5440b21aa9f2cfbc48908129277f5821720a80e18ad630` |
| `cli-07-malformed-import.json` | `4a068c42857aa171195695a1632722484c954daac10cab8ec2adac81322e462e` |
| `cli-08-icon-import.json` | `cccab760eaca6b3f18cd4cef6494f774767c434e04b414ce26460649a08b5344` |
| `cli-09-stale-import.json` | `dd9edcd0f132a1a59aedfff6c4ddd4b71cc7ab8a45efe0ff66d8c59f902c76fa` |
| `cli-10-duplicate-import.json` | `c2de795769a1b85a288f0f7c9bed7d43edc51eb1dd4bde3d8c28160f5e198cb7` |
| `cli-11-icon-show.json` | `2f6111f0cd4309344dfd4280423f6ba232548e2f8d7f0ae450346507f975d883` |
| `cli-12-icon-gallery.json` | `f875213b8492efe0e8c7d810dd56d073cde16d570c77d657774d4e798e41c86e` |
| `cli-13-repeat-gallery.json` | `c86b5b72ab734c87ed71220f90ff0c5757d0859e3569f6ef406605ba71442242` |
| `cli-14-brand-init.json` | `674b61c7752d70910d368131a841c253f5ba2f656d15a0a1040fe89a599a909b` |
| `cli-15-brand-prompt.json` | `b1f10ff17480ea5864ccc42f43582295895f8e7a5ff553fdb7f10cc0da930158` |
| `cli-16-brand-import.json` | `029ebd616271d9332c6f57b3fdee7784943b9554bf7f1a6e0f03254ff0eebe8c` |
| `cli-17-brand-show.json` | `ffbb7c56dff367e68a375f312915be0ad16248e47ba407099cd1b79ae72f462a` |
| `cli-18-unicode-init.json` | `e146951f65b2dfa6dbc0d6e3a60187afabdca4368d8e873fe1591e59578f53c8` |
| `cli-19-unicode-prompt.json` | `a9c9d581cbed833075ad07a6ecf56ac20d0b486f34a55b4437bbc5684d5b81bd` |
| `cli-20-unicode-import.json` | `0307b2f9f14d11e3ca10ba3caeab02b67a004091a8766b93f286a85e08c10280` |
| `cli-21-unicode-gallery.json` | `e702c2f91ceb9b18c940f896fced0cce12d4a5024796e94fb5898ee7ecdec378` |
| `cli-summary.json` | `195dd480ecca69b3920eb28fb3e74ffb00395f3f1dafd020eb5bbe691cd73639` |
| `final-cache-lock-check.json` | `538e13bea9e075e7e34856800f7972be03b36851d8c45281111d0c5e7bdee14c` |
| `final-cache-plugin-validator.json` | `01b3b0158a564a9d01074cfaa5e74434c68529f56cdcf4b2e96b2a7a8fa5e1d7` |
| `final-cache-skill-validator.json` | `d96ae89c6c53798d12a6b038c8e64ec6410db6837df8b60c9057136738cfe52a` |
| `final-cachebuster.json` | `3158c75917bd66ea9ac56a04e96adbf74b4e236d58961846225c1b9cb562baed` |
| `final-installed-path.json` | `d6f080f5f67b107f92e2d153e8e43305c33bd89ec8d8f88a0d99a9cc1d86b242` |
| `final-marketplace.json` | `1ba4ec5dc06376f0ecb2a3dc24493fe84b287b629bafcf4235e835e39194608a` |
| `final-payload-identity.json` | `b3f253479971dc8f960d0bb6fd10931492e75701de95e597c16c9a809cc84c4e` |
| `final-personal-plugin-validator.json` | `5b5a23e35baf030e47de40b082c6ea0f665af2658caeaa6927d40e4cfecffbf1` |
| `final-personal-skill-validator.json` | `0dcfdb587aea6c25d5e1f1f5667533513e667ae78538ad0f4f5f910e6026732d` |
| `final-plugin-add.json` | `dc83ac6de176fc8d88d9d40c109ebc5d745d1dd399773515ecd1dd869ef9618e` |
| `final-smoke-show.json` | `8d74bde0f2e31d178b3b7074008ad12155d7b189564f31b511147c448dcbabea` |
| `final-source-plugin-validator.json` | `484aa385c81f589cf7ad1f016310efa92a8d3c673cff0d30b2f6a77550cb9942` |
| `final-source-skill-validator.json` | `1dd59823dd84a3ce86afbd7f3cb5c372171304cfd59868cfb35c006e0cdfb1c7` |
| `final-tmux-capture.txt` | `bae1cd04f86a57e1416ce4ad495b6d97803a466c2097fc3b5d8156cfd0360eb4` |
| `final-tmux-exit.txt` | `277b5f4604001695c96baf2f24a26baea496d46a9c947fb6706d4d00ccab9c39` |
| `final-tmux-qa.json` | `4b49fe292839b34d049132208a7602d394e20f7b55f7c68a1e252c8215ffbf9f` |
| `harness-note.json` | `8c6c20087315e3a219f3500985eb2dc0291bb07cd1b0260583d435d6b41cf7bc` |
| `http-qa.json` | `4474d3a88b7c68cf133290321a370d4227d65a5baf7efaf8c43f499bf801117d` |
| `http-response.txt` | `2b2ebece05dbe8de98f8c66e4d903f2677fa1085ad54a3bc74f5d09a0a06fd40` |
| `installed-path.json` | `d8f1f12eeec15b2eb79af0518800d7130f35f9b818dcc03de2173a49c36d69a3` |
| `marketplace.json` | `db58cf72d889812b2c85233d31b199308a7fb4b243f34c73febce02eb27227b8` |
| `payload-identity.json` | `1f71c364896c5136a0ae42a8d119a761033f107ed5bb55f090e9432ab89679fe` |
| `personal-lock-check.json` | `d42fa3ac72fc16f4b87dd87def1d15e012c9c4d9f35a1c851af51c68b96e3803` |
| `personal-plugin-validator.json` | `5b5a23e35baf030e47de40b082c6ea0f665af2658caeaa6927d40e4cfecffbf1` |
| `personal-skill-validator.json` | `0dcfdb587aea6c25d5e1f1f5667533513e667ae78538ad0f4f5f910e6026732d` |
| `plugin-add.json` | `ce8b49707075e524436844a4589303480b3dc8b32ef318aafc5d2148524bd3bd` |
| `preinstall.json` | `7c44cfd87c40c60c9b1c25b00d6b5e3f78340cfa40db6b16283dd41e0a995987` |
| `prior-icon-presets-red.json` | `ec0e41f06929430a0a64051ab614a2655466c074ecf4529654ddc06475fb6fbc` |
| `server-pid.json` | `1cc9690abc35a3d5dc7ce589b5e03dd0e08dde70917156a259ffb7168cfed6f0` |
| `server.log` | `254ae8902dda19e5eb8d163bb7a841a7104c5f25937abfe7a2ec7d121bdf2923` |
| `source-lock-check.json` | `bf1684ce67b030f4772e29ae33e945e85decbcd014e5668ea03637530d29a1cd` |
| `source-plugin-validator.json` | `5a656bc9c4e211d6ed88c4bd42c0d35ef4b024b61f6cc4d5053ad6f0483c749c` |
| `source-skill-validator.json` | `78a350f8ddaa4de9fa061095162c67b22699b1d4b3b460d3a2963b7644d501c1` |
| `tmux-capture.txt` | `45d884d543a4c2a307baf90fd264578186f88a4e6f9207d20905b496064e77d7` |
| `tmux-exit.txt` | `277b5f4604001695c96baf2f24a26baea496d46a9c947fb6706d4d00ccab9c39` |
| `tmux-qa.json` | `378e53b8a974fcbbc674a195850acb11e18c2a3c9932e7b56aa865f7e4621c54` |
| `workspace-registration.json` | `20ca24d0ba853003d929e5b1a38bb1a5187f5bf190a1d7b967d759ff0e9e7458` |

## Cleanup receipt

**PASS.** Exact owned tmux sessions (initial pane PID `8507`, final pane PID `29514`) were terminated; `tmux has-session -t ll-icons-install` confirmed absence. HTTP server PID `8625` was terminated and reaped. After all cleanup, port `8782` had no listener by both `lsof` (exit 1, empty output) and socket connection checks.

The exact registered workspace `/private/tmp/logo-land-icons-install-task_a0fb416de8be`, including staging, fixture copies, generated galleries, download, temporary Git metadata, sessions and raw logs, was removed after report evidence was retained. Its absence was verified. No other workspace, plugin or cache tree was deleted.

The intended personal payload and final installed cache remain installed and were hash-checked again after cleanup; source remains `0.5.0`. All execution-plan steps are complete. To use the updated skill in the Codex UI, start a new thread and invoke `$logo-land`; this handoff is not a claim that fresh GUI-thread pickup was tested.
