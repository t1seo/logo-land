# Logo Land v0.4.0 final personal installation verification

Verified **2026-09-13 KST** after the C1 metadata export correction and G3 gallery template correction. The installed version is **`0.4.0+codex.20260912161802`**. All **29 installed-helper CLI calls** behaved as expected: **27 succeeded and 2 strict exports were refused**. Public source remains clean-version **`0.4.0`, unreleased**; the published version remains **`0.3.1`** because the native generation/edit acceptance gates remain unmet.

This supersedes the installed payload tested in [installation-040.md](installation-040.md), which remains unchanged as historical evidence. The correction contract is documented in [metadata-export-fix.md](metadata-export-fix.md). This run reused an approved native original; it made no native image call and does not satisfy the outstanding native gates.

## Completed work

1. Compared the existing personal installation with the prior installed receipt, refreshed the allowed payload, and used the official cachebuster/reinstall flow.
2. Drove the absolute installed helper through the NORTHLINE prompt/import/show/review/select/export workflow in a fresh disposable workspace.
3. Verified generated Dark CSS, original/ZIP identity, legacy EXIF0 compatibility, advisory unavailable evidence, and strict refusals.
4. Rechecked source, personal/cache payload and protected evidence hashes, and recorded this report with raw local receipts.

## Personal edit protection and official reinstall

Before any personal write, every one of the **55 personal files** and **55 previous cache files** matched `output/install-040-workspace/evidence/installed-validation.json` for `0.4.0+codex.20260912153655`. No missing files, extra files or changed hashes were found. A second comparison immediately before copying confirmed that no intervening personal edits required a merge.

The validated `personal` marketplace entry still identified `logo-land` at local `./plugins/logo-land`, resolved to `~/plugins/logo-land`. Only `.codex-plugin/`, `assets/`, `skills/`, `pyproject.toml`, `uv.lock`, and `THIRD_PARTY_NOTICES.md` were synchronized. Runtime bytecode, environments, tests, output and research were excluded. No marketplace/configuration or unrelated plugin was changed.

The only source changes since the previous installed payload were the corrected `color_delivery.py`, `color_analysis.py`, and `color-gallery.template.html`, plus the expected local manifest cachebuster difference. The repository manifest itself was never edited by this worker.

The following official plugin-creator flow completed successfully. Aliases below sanitize local account paths; exact absolute argv and output are retained in the private receipts.

```sh
python3 "<plugin-creator>/scripts/read_marketplace_name.py"
# personal
uv run --isolated --no-project --with PyYAML==6.0.2 python \
  "<plugin-creator>/scripts/validate_plugin.py" "<repository-root>"
# Copy only the allowed source payload to ~/plugins/logo-land.
python3 "<plugin-creator>/scripts/update_plugin_cachebuster.py" "$HOME/plugins/logo-land"
# 0.4.0 -> 0.4.0+codex.20260912161802
uv run --isolated --no-project --with PyYAML==6.0.2 python \
  "<plugin-creator>/scripts/validate_plugin.py" "$HOME/plugins/logo-land"
codex plugin add logo-land@personal --json
uv run --isolated --no-project --with PyYAML==6.0.2 python \
  "<plugin-creator>/scripts/validate_plugin.py" \
  "<codex-home>/plugins/cache/personal/logo-land/0.4.0+codex.20260912161802"
```

The repository, personal installation and installed-cache validators all exited 0. The installation receipt records `pluginId=logo-land@personal`, `marketplaceName=personal`, `authPolicy=ON_INSTALL` and the exact version above. The active account plugin directory resolves through its existing symlink to `~/.codex/plugins`.

| Payload evidence | Result |
| --- | --- |
| Enumerated personal/cache files, before and after CLI execution | 55 / 55, byte-identical |
| Non-manifest files matching source | 54 / 54 |
| Manifest comparison | Byte-identical after removing only the exact `+codex.20260912161802` suffix |
| `pyproject.toml` / `uv.lock` helper package version | `0.4.0` / `0.4.0` |
| Installed helper SHA-256 | `ccbe591a8ba0f3a1445da80726a3f9d4c706f33759bb361363c96c189bbc4e79` |
| Complete installed payload SHA-256 | `5712571d23f4013479ea5692d0b31cf3a1eb16274e1cac3e61185562ca3af457` |

The aggregate hash is SHA-256 of lexicographically sorted relative paths, each encoded as `path + NUL + file_sha256_hex + LF`. Full per-file hashes are in `payload-identity.json`. Source package hashes remained unchanged throughout this worker's run; 82 protected files covering the live NORTHLINE session/inputs, saved Chrome evidence and original metadata probe also remained unchanged.

## Actual installed CLI workflow

Every helper call passed the **absolute newly installed script path** to `uv run --no-project --script`, unset `PYTHONPATH`, set `PYTHONDONTWRITEBYTECODE=1`, and ran with the relevant disposable workspace as its working directory. The helper's PEP 723 environment was used; these calls did **not** use the packaged project lock environment. Recorded color reports identify ColorAide `8.12.1` and Pillow `12.3.0`.

```sh
LOGO_REPO='<repository-root>'
LOGO_CACHE='<codex-home>/plugins/cache/personal/logo-land/0.4.0+codex.20260912161802'
LOGO_WORKSPACE="$LOGO_REPO/output/install-040-final-workspace"
LOGO_HELPER="$LOGO_CACHE/skills/logo-land/scripts/logo_project.py"
LOGO_INPUT="$LOGO_WORKSPACE/inputs"
LOGO_NATIVE="$LOGO_REPO/output/color-live-workspace/.logo-generator/sessions/northline/artifacts/a-v1.png"
cd "$LOGO_WORKSPACE"
ll() {
  env -u PYTHONPATH PYTHONDONTWRITEBYTECODE=1 uv run --no-project --script \
    "$LOGO_HELPER" --workspace "$LOGO_WORKSPACE" "$@"
}
ll init --session northline --brief "$LOGO_INPUT/brief.json"
ll palette-propose --session northline --request-file "$LOGO_INPUT/palette-request.json"
ll palette-add --session northline --palette p1 --palette-file "$LOGO_INPUT/palette.json" --revision 0
ll prompt --session northline --concept "$(cat "$LOGO_INPUT/concept.txt")" \
  --palette p1 --lockup-file "$LOGO_INPUT/lockup.json"
ll import --session northline --artifact a-v1 --image "$LOGO_NATIVE" \
  --prompt-file "$LOGO_INPUT/prompt.txt" --palette p1 \
  --lockup-file "$LOGO_INPUT/lockup.json" --background opaque --revision 1
ll show --session northline
ll color-analyze --session northline --artifact a-v1 --revision 2
ll color-gallery --session northline --artifacts a-v1 --output output/gallery/northline
ll review --session northline --artifact a-v1 --review-file "$LOGO_INPUT/review.json" --revision 3
ll select --session northline --artifact a-v1 --revision 4
ll export --session northline --output output/verified-delivery/northline --revision 5
```

All 11 NORTHLINE calls exited 0. Brief, concept, palette request, palette, lockup and final prompt inputs were copied byte-for-byte from the existing native workflow and compared with the prior installation inputs. The constructed prompt matches the original final prompt prefix; the original standalone-image suffix remains intact in the imported artifact. The saved brief, complete palette versions, prompt, lockup, requested background, image facts and original hash match the live source session. The palette digest remains `fb565c763e30a26c17b0745288cdaa41bbd11713c950856464580cf8f79a2b1f`.

The effective structured palette remains navy `#183A56` for symbol/wordmark and silver `#CDD4DB` for the opaque background. The historical brief's cyan/white context was not substituted for that saved intent. Import, explicit analysis and export recomputation each report advisory `pass`. Final revision is 6, with `a-v1` selected; `transparency_verified=false` correctly describes the opaque original. This sampled pass is not exact raster HEX equality or proof of every prompt constraint.

The original PNG and saved [128 px light](chrome/northline-small-light.jpg) and [128 px dark](chrome/northline-small-dark.jpg) screenshots were reopened. The exact NORTHLINE lettering, centered symbol above the wordmark, central gap, margins and intended silver rectangle remain visible. The existing review input was reused unchanged with its actual [Chrome review provenance](chrome-live.md); no new browser interaction or font-file verification is claimed.

### Generated Dark background

The newly generated `output/gallery/northline/index.html` contains the working input/label IDs and this exact selector/value:

```css
#surface-dark:checked ~ .artifact-grid .surface { background: #171717; }
```

This verifies G3 in output generated by the installed template. It is a static output check, not a new browser/computed-style test. Historical screenshots retain the historical surface and were not changed. Generated HTML SHA-256: `ce7f2f7a9eb5c93c0f83b5e1542b35b1d02b8e35e6761bb48c22446a48cef7f1`.

## Metadata compatibility through the installed helper

The existing accepted v0.3.1 schema-1 probe at `output/review-code/metadata-probe/base-orientation-0` was copied into a fresh disposable subworkspace. Its EXIF orientation is 0; decoded RGBA pixels match the actual NORTHLINE original, but its metadata-altered PNG hash differs. **This synthetic fixture is code compatibility evidence only and is never counted as native generation, edit or approval evidence.** No real native original or public evidence PNG was edited.

| Installed scenario | CLI calls | Observed result |
| --- | --- | --- |
| Copied schema-1 session, revision 4, export | 1 successful | Migrates to schema 2/revision 5; `color_policy=unverified`, report `unverified` |
| Fresh advisory fixture: init, palette-add, prompt, import, show, review, select, export | 8 successful | `color_policy=advisory`, report `indeterminate` |
| Fresh strict fixture: same sequence | 7 successful, 1 expected refusal | `color_review_required`; unchanged state and no delivery directory |
| Strict fixture with synthetic stored `pass` | 1 expected refusal | Fresh recomputation returns `color_review_required`; unchanged forged state and no delivery directory |

The advisory/strict scenarios use explicitly labeled fixture prompts and reviews, with a test palette; these are not claimed to be the image's native generation instructions. Strict constraints set `max_colors=2`. The temporary forged-pass state was saved as code-test evidence and the disposable session was restored afterward.

Both successful metadata exports preserve the accepted fixture PNG bytes. Their reports record `profile_treatment=unsupported`, `color_engine_version=not_used`, zero samples, no measured swatches/targets/contrasts and null match fractions/observed color count. The explicit reason is included in both manifest warnings and the brand guide:

```text
Color evidence unavailable: invalid_reference: EXIF orientation must be an integer from 1 to 8
```

The schema-1 backup is byte-identical to the copied pre-export state. Initial import evidence is `unverified`; advisory export produces a fresh `indeterminate` report. A verification-harness assertion initially expected the import report to be `indeterminate` and stopped after the successful first strict refusal. Correcting that harness assumption allowed the forged-pass check to finish; no production code changed and no helper command was retried. ICC-specific installed scenarios were not rerun here; the correction report records their separate focused source coverage.

## Export and archive identity

All three new ZIPs pass CRC/integrity checks and contain exactly `brand-guide.md`, `logo.png` and `manifest.json`. Every archive member matches its standalone file. For NORTHLINE, original, imported artifact, gallery copy, standalone delivery and archived PNG bytes all match.

| New delivery | PNG SHA-256 | ZIP SHA-256 |
| --- | --- | --- |
| NORTHLINE approved original | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` | `8ea27c84b413fdef7f260151c2a3780ba56da71b5a4d8d6e6491fac817582348` |
| Legacy EXIF0 code fixture | `fe3433fe90168197446e4df3cd1f472a555759db5aa7cff8fe2703f6d729f87e` | `32f99f1033cdafa8fb976efe02c35d2e003ee40d07d8c91cec614050a394ed58` |
| Advisory EXIF0 code fixture | `fe3433fe90168197446e4df3cd1f472a555759db5aa7cff8fe2703f6d729f87e` | `2e479fe1bc1519a7b454ff5ffa4eb03b036760f3fcdc3d20f45166d25a463d94` |

The new NORTHLINE manifest SHA-256 is `fbee25e06101560028ab4f710f8c7c653feacfd81ada871d476c81da26945a1e`. Full reports, all manifest hashes and transaction checks are recorded in `verification.json`.

## Limits and local evidence

- Dependency caches were warm. No cold-cache, fresh-clone, offline/network-isolated install or fresh GUI-thread skill pickup was tested. Start a new Codex thread and invoke `$logo-land` to pick up the refreshed skill; that remains a handoff instruction, not completed GUI QA.
- No full source suite or browser control was run in this task. The 29 calls above are real installed-cache CLI executions, separate from the coordinator's source checks. Six recorded administrative/helper commands cover marketplace-name validation, cachebuster, plugin add and the three validators.
- The previous `codex plugin list` failure caused by the unrelated `astral-codex` marketplace remains outside this task. Plugin listing was not repeated and no host patch or unrelated plugin repair was attempted.
- Public development version `0.4.0` remains unreleased; published `0.3.1` remains current because native acceptance gates are unmet. No commit, push, tag or release occurred.

Raw evidence is retained under `output/install-040-final-workspace/evidence/`: `preinstall.json`, `source-validation.json`, `marketplace-name.json`, `cachebuster.json`, `personal-validation.json`, `plugin-add.json`, `install-receipt.json`, `installed-validation.json`, `payload-identity.json`, numbered **01–29** CLI records, legacy/strict state snapshots, `harness-note.json` and `verification.json`. The disposable workspace contains copied inputs, sessions, generated gallery and all three deliveries. Local receipts include absolute account paths and are not copied into this public report.
