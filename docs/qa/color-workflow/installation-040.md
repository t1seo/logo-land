# Logo Land v0.4.0 personal installation evidence

Verified **2026-09-13 KST**. Installation, CLI use and export succeeded against **`0.4.0+codex.20260912153655`**. Public manifest/package versions remain `0.4.0`. This record covers an installed helper using an existing successful native original; no new native generation or image edit occurred in this installation run.

## Personal source and installation

The existing `personal` marketplace entry pointed at `./plugins/logo-land`, resolved by the CLI to `~/plugins/logo-land`. Before synchronization, all 21 personal files matched the previous installed cache `0.3.1+codex.20260912140549`; comparison with repository `HEAD` also found no changes after normalizing only the manifest cachebuster. No personal edits or extra files needed merging.

Only `.codex-plugin/`, `assets/`, `skills/`, `pyproject.toml`, `uv.lock`, and `THIRD_PARTY_NOTICES.md` were copied from the working tree. Runtime bytecode, environments, output, tests, research, account details and private files were excluded. There were 55 packaged files after synchronization and after installed-helper execution. The public source and manifest were not changed by this worker.

The following official helper/CLI sequence was executed. `<plugin-creator>` is the installed official skill directory; `<codex-home>` is the active Orca account home. These aliases sanitize private paths, rather than naming another installation.

```sh
python3 "<plugin-creator>/scripts/read_marketplace_name.py"
# personal
python3 "<plugin-creator>/scripts/update_plugin_cachebuster.py" "$HOME/plugins/logo-land"
# Updated plugin version: 0.4.0 -> 0.4.0+codex.20260912153655
uv run --isolated --no-project --with PyYAML==6.0.2 python \
  "<plugin-creator>/scripts/validate_plugin.py" "$HOME/plugins/logo-land"
codex plugin add logo-land@personal --json
uv run --isolated --no-project --with PyYAML==6.0.2 python \
  "<plugin-creator>/scripts/validate_plugin.py" \
  "<codex-home>/plugins/cache/personal/logo-land/0.4.0+codex.20260912153655"
```

Both validators exited 0. The install receipt reported `pluginId=logo-land@personal`, `marketplaceName=personal`, `authPolicy=ON_INSTALL`, the exact cachebuster above and its installed path. The active account's `plugins` directory is a symlink to `~/.codex/plugins`; the validator reports that resolved path. No marketplace entry/configuration was rewritten.

Personal source and cache have identical 55-file sets and hashes. All 54 non-manifest files match the repository; manifest objects match after removing only the exact local suffix, and personal/cache manifest bytes are identical. `pyproject.toml` and the `logo-land-helper` entry in `uv.lock` are both `0.4.0`. New installed content includes `color_cli.py`, `color_analysis.py`, `color_workflow.py`, `palette_proposals.py`, `references.py`, `reference_evidence.py`, `lockup_models.py`, `color-gallery.template.html`, `export_bundle.py`, the color/typography references, and attribution notices.

## Execution from the installed cache

The runner passed the helper's **absolute installed path** to `uv`, used `output/install-040-workspace/` as its working directory, unset `PYTHONPATH`, and set `PYTHONDONTWRITEBYTECODE=1`. It did not import the repository helper. The equivalent quoted shell prefix for the recorded argv is:

```sh
LOGO_REPO='<repository-root>'
LOGO_CACHE='<codex-home>/plugins/cache/personal/logo-land/0.4.0+codex.20260912153655'
LOGO_WORKSPACE="$LOGO_REPO/output/install-040-workspace"
LOGO_HELPER="$LOGO_CACHE/skills/logo-land/scripts/logo_project.py"
LOGO_INPUT="$LOGO_WORKSPACE/inputs"
LOGO_NATIVE="$LOGO_REPO/output/color-live-workspace/.logo-generator/sessions/northline/artifacts/a-v1.png"
cd "$LOGO_WORKSPACE"
ll() {
  env -u PYTHONPATH PYTHONDONTWRITEBYTECODE=1 uv run --no-project --script \
    "$LOGO_HELPER" --workspace "$LOGO_WORKSPACE" "$@"
}
```

The installed script SHA-256 was `ccbe591a8ba0f3a1445da80726a3f9d4c706f33759bb361363c96c189bbc4e79`. Execution used the script's PEP 723 dependency environment, including ColorAide `8.12.1` and Pillow `12.3.0`; the installed `uv.lock` was inspected separately. This is not a claim that these CLI calls used the locked project environment.

`brief.json`, `concept.txt`, `lockup.json`, `palette-request.json`, `palette.json`, and `prompt.txt` were copied unchanged from `output/color-live-inputs/northline/`. The brief, structured palette, final prompt and lockup were also compared against the original saved session. The historical brief mentions cyan/white; its effective structured palette correctly remains navy `#183A56` for the symbol/wordmark and silver `#CDD4DB` for the opaque background. No constraints were weakened for this import.

These commands all exited 0; revisions below reflect the actual fresh workspace:

```sh
ll init --session northline --brief "$LOGO_INPUT/brief.json"
ll palette-propose --session northline --request-file "$LOGO_INPUT/palette-request.json"
ll palette-add --session northline --palette p1 --palette-file "$LOGO_INPUT/palette.json" --revision 0
ll prompt --session northline --concept "$(cat "$LOGO_INPUT/concept.txt")" \
  --palette p1 --lockup-file "$LOGO_INPUT/lockup.json"
ll import --session northline --artifact a-v1 --image "$LOGO_NATIVE" \
  --prompt-file "$LOGO_INPUT/prompt.txt" --palette p1 \
  --lockup-file "$LOGO_INPUT/lockup.json" --background opaque --revision 1
ll color-analyze --session northline --artifact a-v1 --revision 2
ll color-gallery --session northline --artifacts a-v1 --output output/gallery/northline
ll review --session northline --artifact a-v1 --review-file "$LOGO_INPUT/review.json" --revision 3
ll select --session northline --artifact a-v1 --revision 4
ll export --session northline --output output/verified-delivery/northline --revision 5
```

`palette-propose` returned three local candidates. The first candidate's HEX values matched the original selected palette; saving the exact original palette retained digest `fb565c763e30a26c17b0745288cdaa41bbd11713c950856464580cf8f79a2b1f`. `prompt` returned revision 1 and the correct palette/digest/stacked lockup. Its text matched the prefix of the previously submitted native prompt; the original final standalone-image instruction suffix was retained when importing. Prompt construction was not presented as an image-generation call.

The import, explicit analysis and export recomputation each reported `pass`. Review/select/export advanced the NORTHLINE session to revision 6. The generated gallery contains an unchanged copy of the original.

A separate `reference-smoke` session exercised the installed reference path without rebinding NORTHLINE's original palette:

```sh
ll init --session reference-smoke --brief "$LOGO_INPUT/brief.json"
ll reference-add --session reference-smoke --reference northline-original --image "$LOGO_NATIVE" --revision 0
ll palette-propose --session reference-smoke --reference northline-original \
  --request-file "$LOGO_INPUT/reference-request.json"
ll palette-add --session reference-smoke --palette extracted-v1 \
  --palette-file "$LOGO_INPUT/reference-palette.json" --revision 1
ll prompt --session reference-smoke \
  --concept 'Installation smoke check for a reference-derived palette; no generation requested' \
  --palette extracted-v1 --lockup-file "$LOGO_INPUT/lockup.json"
```

The request delegated selection with an installation-only rationale and no color restrictions. One candidate returned with `source=reference`, actual extraction evidence, the original reference hash and no warnings. The selected candidate object was saved unchanged, then used for prompt binding at revision 2. No logo was generated or imported under that extracted palette. The copied reference PNG remained byte-identical to the native original.

## Visible review and exported evidence

The actual prior browser review is in [chrome-live.md](chrome-live.md), with [128 px light](chrome/northline-small-light.jpg), [128 px dark](chrome/northline-small-dark.jpg), and [original-image view](chrome/northline-native-original.jpg) evidence. That reviewer observed NORTHLINE at large and 128 px sizes on both surfaces. This installation worker reopened the original PNG and both saved 128 px screenshots; it did not claim a new browser interaction.

The recorded review passes for exact `NORTHLINE` lettering, the centered symbol above the single-line wordmark, its central gap, ample margins, small-size recognition and the intended opaque silver background. All five review fields were saved with that specific evidence. The rectangle is intentional, and `transparency_verified=false` is correct. The Space Grotesk name is a requested appearance reference, not proof of an installed font file.

The output at `output/install-040-workspace/output/verified-delivery/northline/` contains a schema-2 manifest, brand guide, PNG and ZIP. ZIP CRC/integrity verification passed. The ZIP contains exactly `logo.png`, `manifest.json`, and `brand-guide.md`; each archive member matches its standalone file. Original, imported artifact, reference copy, gallery copy, standalone delivery and archived PNG bytes match.

| Evidence | Value |
| --- | --- |
| Original and every checked PNG copy SHA-256 | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| ZIP SHA-256 | `940f64d03c3d14f76be010048888a533b6105141f64c757748509e532c3735a3` |
| Manifest SHA-256 | `837fdb7cefdb20259687ebb5f20f20614307c003d906e9ddfac32288fbc1245b` |
| Image / requested background | PNG, 1254 × 1254, alpha 255 throughout / opaque |
| Export schema / revision | 2 / 6 |
| Color policy / result | advisory / `pass`, no reasons |
| Measurement | `logo-color-v1`, ColorAide 8.12.1, Pillow 12.3.0, `assumed_srgb` |
| Sampling | Full image, 16,384 core samples, zero partial-alpha samples |
| Target coverage | 99.70703125% matched, 0.29296875% unmatched |

The palette has no locked/allowed/required colors or maximum count restriction. This pass is advisory sampled evidence, not strict-color validation, exact raster HEX equality, whole-image pixel inspection, print proof or accessibility certification. The manifest records these limits, the effective palette, source hash, recomputed report, requested lockup and font-reference caveat. Exact brief/palette/prompt/lockup preservation and both original image/session hashes were checked; the live NORTHLINE workspace remained untouched.

## Limits and retained local evidence

- `codex plugin list --json` exited 1: the unrelated `astral-codex` marketplace root does not contain a supported manifest. The plugin add receipt and direct installed-cache checks succeeded independently. No unrelated marketplace was repaired.
- No cold-cache offline installation or fresh clone was run. Dependency caches were available; network isolation was not applied. No new native generation, native edit or new GUI-thread skill selection was performed.
- A verification harness first tried `tomllib` with the system Python and received `ModuleNotFoundError`; it was rerun successfully with `uv run --isolated --no-project --python 3.12 python`. This was the metadata-check harness, not a plugin-helper failure.
- The reported 299 source tests belong to the broader implementation verification; this worker did not rerun or claim them as installed-cache tests. This record's surface evidence is the 15 successful installed CLI calls and subsequent file/archive checks.
- Raw receipts and exact absolute argv are retained locally under `output/install-040-workspace/evidence/`: `preinstall.json`, `plugin-add.json`, `installed-validation.json`, numbered `01-init.json` through `15-reference-prompt.json`, `plugin-list.json`, and `verification.json`. Those files contain local paths and are not copied into public documentation. Input files, sessions, gallery and delivery remain within that disposable workspace.

No commit, push, tag or release was performed. Start a new Codex thread and invoke `$logo-land` to load the refreshed skill. The [installation overview](../installation.md) preserves the v0.3.1 and earlier records as history.
