# Native color cases: public gallery evidence

Date: 2026-09-13 KST. Scope: the English static [overview](../../colors/index.html), its original PNG assets, seven session comparisons, complete stored reports, final prompt texts and three verified delivery copies. These are real native generation attempts for fictional demonstration brands. This page does not claim all eight requests passed.

## Current case outcomes

| Case | Overview artifact | Saved color result | Visual and delivery result |
| --- | --- | --- | --- |
| Automatic bakery | SUNROOM `a-v1` | pass | Not delivered: recorded `small_size_ok=false`; BAKERY is too small at 128 px. |
| Automatic technology | NORTHLINE `a-v1` | pass | Reviewed, selected and exported by the coordinator; original PNG and ZIP copied. |
| Green anchor | GROVE `a-v1` | pass | Reviewed, selected and exported; anchor-only constraints, recommended for light surfaces. |
| Warmer companion edit | GROVE `a-v4` | pass | **FAILED:** opaque baked checkerboard; zero transparent pixels. `a-v2` and `a-v3` are preserved with the same background defect. A stored anchor-only pass does not certify full palette fidelity or transparency. |
| Restricted black/ivory | 밤결 `a-v1` | indeterminate | No approved delivery: 615 / 2,697 visible samples have partial alpha (22.80%). Repairs `a-v2` and `a-v3` are opaque checkerboard failures with color mismatch. |
| Reference palette | TIDE `a-v1` | pass | Reviewed, selected and exported; palette extracted from the actual SUNROOM original. |
| Reference + anchor + two-color limit | FIELD NOTE `a-v1` | indeterminate | No approved delivery: 371 / 3,019 visible samples have partial alpha (12.29%). Repairs `a-v2` and `a-v3` are opaque checkerboard failures with color mismatch. |
| White reversed variant | 밤결 `white-v3` | indeterminate | **Not delivered after two native repairs:** the Chrome preview has readable lettering and a clean overall shape, but sampled alpha evidence remains indeterminate. Core white match is 100%, but 923 / 3,483 visible samples have partial alpha (26.50%). No compliant white delivery was produced. |

The display choices above do not mutate session selections or visual reviews. Only NORTHLINE, GROVE `a-v1` and TIDE have public ZIP links, sourced from the coordinator's actual successful exports. SUNROOM's failed small-size review is recorded rather than overwritten. The coordinator finalized white-v3 after reaching the two-additional-native-repair limit. The archive preserves parent-v1 plus white-v1/white-v2/white-v3; the initial white-v1 had 42.04% partial-alpha samples and white-v2 had 29.78%. Across eight requests there were 16 actual native calls and 17 saved artifacts, including the reused black/ivory parent. Required restricted and white live successes remain unmet; no fully verified release claim is made.

## Original-byte provenance

[Structured case evidence](native-cases.json) uses `gallery_root: ../../colors/`; all nested public paths resolve from that directory. The [public manifest](../../colors/manifest.json) provides the same case mapping from the gallery root. Each session's `session.json` includes frozen brief, bound palette history, lockup, saved reports and reviews; actual prompt texts are separate files. Native tool source records publish the source basename and SHA-256 only, along with the source record basename and SHA-256. Private source locations are omitted.

The input records were the actual `tool-result.json` and `*-tool-result.json` files under `output/color-live-inputs/`. Both observed source record shapes (`source` and `source_path`) were read. Every copied artifact was matched to its saved session SHA-256 and to the PNG at the precise recorded native source. The white session's `parent-v1` is explicitly labeled as the reused original from `bamgyeol/a-v1`, not an additional independent native generation.

The six stable sessions and their original artifacts/references were frozen in a new workspace at `output/final-galleries/t8-public-r2/`. The final white session was frozen separately at `output/final-galleries/t8-white-final/`. Comparisons were generated through the actual helper, using the explicit saved IDs:

```sh
uv run --locked python skills/logo-land/scripts/logo_project.py \
  --workspace output/final-galleries/t8-public-r2 \
  color-gallery --session grove --artifacts a-v1,a-v2,a-v3,a-v4 \
  --output output/grove
```

The same command was run for all seven sessions with their actual artifact lists. Each resulting `index.html` and `images/` directory was byte-copied into `docs/colors/projects/<session>/`; supplemental report pages and JSON were added alongside them. No CLI-generated comparison HTML or PNG was rewritten. A prior `t8-public-r1` snapshot is preserved in workspace output; the published six stable sessions use the review/export-aware `r2` snapshot. The final white comparison was generated separately with `--workspace output/final-galleries/t8-white-final --session white-bamgyeol --artifacts parent-v1,white-v1,white-v2,white-v3 --output output/white-bamgyeol`, then byte-copied into the same public session directory.

## Verification executed

[Machine-readable integrity verification](../../colors/verification.json) records every artifact and delivery hash.

- Eight overview PNG SHA-256 hashes matched the selected saved originals and the exact native source PNGs.
- Seventeen session artifact copies and all seventeen final prompt texts matched the saved originals. Seven public CLI comparison HTML files matched the actual generated files byte-for-byte.
- Three complete delivery directories were copied from actual successful exports. Each copied ZIP hash matched the source ZIP; each `logo.png` extracted with `unzip -p` matched the corresponding original PNG hash.
- A recursive static check resolved **261 local links and fragment targets** across **15 HTML pages** with no missing file or anchor. The eight custom inline scripts passed JavaScript syntax checks.
- The whole gallery was copied into a new `output/final-galleries/t8-portable-copy/` directory. A temporary localhost server successfully served all **93 linked files** from that relocated copy, with **zero HTTP failures** and no dependency on the original checkout paths. The server was stopped after verification.
- Public HTML, JSON, Markdown and prompt text contain no `/Users/`, `/private/` or `file://` paths. HTML links and resources are relative; no external script, font or service is required. No `.woff`, `.woff2`, `.ttf` or `.otf` file is present.
- No logo drawing, recoloring, alpha replacement, background removal or other raster editing was performed. Images were viewed or byte-copied only. Light/dark/transparency and large/128 px previews modify CSS only.

Chrome observations are owned by the separate browser worker and recorded in [chrome-live.md](chrome-live.md). Initial browser findings support the wording for the six original brand sessions; direct original-image inspection confirmed baked checkerboards in final warm/black/green repairs ; the native tool preview was insufficient to establish visible damage in the white variant. The Chrome worker has opened the final public page; the assembly worker also inspected the [public top/two-card screenshot](chrome/public-cards-01-02.jpg) and confirmed the default ivory layout, original previews and visible status explanation. The final 8th card is the unchanged white-v3 original on a dark default CSS surface, clearly marked not delivered / indeterminate. Gallery assembly, integrity and portability checks are complete. Full control/download observations and final browser screenshots remain with the separate Chrome worker and will be recorded in chrome-live.md; the coordinator will integrate any resulting wording corrections.

## Scope boundary

No font files were installed or bundled. Named typefaces are requested appearance references, not verified font identities, editable text or licenses. No session review, selection, export state, code outside the assigned public documentation paths, commit, push or release was changed by this assembly worker.
