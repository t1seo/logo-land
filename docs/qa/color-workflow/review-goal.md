# Goal and constraint review

Date: 2026-09-13 KST. Reviewer task: `task_3398fc120c4d`, dispatch `ctx_2f32f498cc7f`. Base: `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`. Scope includes the uncommitted tracked diff and untracked implementation, tests, research and public evidence.

**Whole-goal verdict: FAIL. Confidence: HIGH.** The required successful restricted-color and white-transparent native cases are absent. The plan explicitly makes both prerequisites for publication; recording their failures accurately does not satisfy those prerequisites.

**Development-code readiness: PASS with one minor preview discrepancy. Confidence: HIGH for the reviewed scope.** The code, research, documentation and truthful unsuccessful samples can be committed as an explicitly unreleased development preview. This is one goal review, not an aggregate approval from the other four reviewers, and it does not authorize a public v0.4.0 tag or release.

## Findings and blocking issues

### G1 · MAJOR / public-release blocker: no successful restricted native output

- Requirement: `plans/logo-land-color-workflow.md:281`, `:285`, `:307`.
- Evidence: `docs/qa/color-workflow/native-cases.md:13`, `:15`; `docs/colors/projects/bamgyeol/session.json:100`; `docs/colors/projects/fieldnote/session.json`.
- Original 밤결 has 615 partial-alpha samples out of 2,697 visible samples, or 22.80%. FIELD NOTE has 371 out of 3,019, or 12.29%. Both exceed the unchanged 10% policy. Their two repairs each contain an opaque checkerboard and have color mismatches. Neither provides a reviewed restricted delivery.
- Reproduction: copy the native workspace into a disposable review workspace, run `show --session bamgyeol`, then `color-analyze --session bamgyeol --artifact a-v1 --revision <current>`. This review independently reproduced `indeterminate`, 615 partial samples and 100% core color match. Core match does not negate insufficient alpha evidence.
- Required resolution: retain the block until an authorized native case satisfies the existing restricted policy and visual/background review. The two repairs for the current requests are exhausted; do not generate a third repair or relax thresholds merely to close this finding.

### G2 · MAJOR / public-release blocker: white-transparent native gate remains indeterminate

- Requirement: `plans/logo-land-color-workflow.md:283`, `:285`, `:307`.
- Evidence: `docs/qa/color-workflow/native-cases.md:16`; `docs/colors/projects/white-bamgyeol/session.json:786`; `docs/qa/color-workflow/chrome-live.md:57`.
- `white-v1`, `white-v2` and `white-v3` remain indeterminate. The final image has 923 partial-alpha samples among 3,483 visible samples, or 26.50%; its 2,560 core samples match white, but the alpha gate still fails. No final white package exists.
- Reproduction: on the copied session, run `color-analyze --session white-bamgyeol --artifact white-v3 --revision <current>`. This review reproduced every measurement field of the saved report, excluding the intentionally new report ID and timestamp.
- The saved Chrome screenshot shows readable 밤결 and a clean-looking small white logo. This review does not infer visible damage from the numerical result, or numerical compliance from the screenshot. `alpha-explanation.json` is diagnostic evidence, not a replacement policy.
- Required resolution: the existing white-transparent gate must pass before public release, within an authorized subsequent scope. Preserve all three attempts, current policy and no-delivery status in the meantime.

### G3 · MINOR / nonblocking for a development commit: generated Dark preview differs from the planned default measurement surface

- Requirement: `plans/logo-land-color-workflow.md:104` names default surfaces `#FFFFFF` and `#171717`.
- Files: `skills/logo-land/assets/color-gallery.template.html:36`; `skills/logo-land/scripts/logo_helper/color_analysis.py:151`.
- The generated gallery's Dark radio selects `#252a32`, while default contrast measurements use `#171717`. The public overview uses `#171717`. The recorded ratios are honest about their surface, but the generated comparison preview does not reproduce that default surface.
- Reproduction: compare the template's `#surface-dark:checked` CSS with `analyze_png`'s `surfaces` default. No browser control is needed to establish these literal values.
- Suggested resolution: align future generated previews to `#171717`, or explicitly name the distinct preview surface. Preserve existing evidence pages as historical snapshots if changing the production template.

### G4 · Observed unsuccessful native cases, correctly withheld

- `docs/qa/color-workflow/native-cases.md:9`: SUNROOM has exact text and a color pass but `small_size_ok=false` for BAKERY at 128 px. It is not delivered.
- `docs/qa/color-workflow/native-cases.md:12`: GROVE warm `a-v2` through `a-v4` have zero transparent pixels. Anchor-only color passes do not establish transparency. The latest warm PNG visibly contains the checkerboard; it is not delivered.
- These prevent describing all eight cases as successful. The plan permits truthful failed case records provided its essential success gates are met, so these are not additional independent publication prerequisites beyond G1/G2.

### Resolved during this review: release wording and unsupported white-damage claims

The initial README review found a v0.3.1 badge with Korean v0.4.0 alternative text and lower sections linking the unpublished v0.4.0 release as the version record. The coordinator corrected both READMEs; this reviewer reread `README.md:2`, `:13`, `:224` and `README.ko.md:2`, `:13`, `:224`. They now distinguish the published 0.3.1 release from unreleased 0.4.0 source. No source code was changed for that correction.

The white supplemental report now says `Not delivered · alpha review required`. The earlier unsupported assertions of visible speckles or damaged lettering are removed from the current editorial result. The actual prompts, PNGs and quantitative indeterminate reports remain preserved. This is a file recheck, not another Chrome session.

## Requirement coverage

Paths beginning with a module name below are under `skills/logo-land/scripts/logo_helper/`. ACHIEVED denotes the specified software/documentation behavior; native acceptance is evaluated separately.

| Requirement | Status | Implementation and evidence |
| --- | --- | --- |
| Automatic conversational palette selection, delegated choice and unchanged concept count | ACHIEVED | `skills/logo-land/SKILL.md:22`, `references/color-workflow.md`; SUNROOM assistant source/rationale and NORTHLINE local-harmony source in `native-cases.json`. No candidate/concept Cartesian product. |
| Anchor, restricted and reference entry points compose | ACHIEVED in software; native restricted/combined success PARTIAL | `color_models.py:31`, `palettes.py:71`, `palette_proposals.py:36`; actual FIELD NOTE keeps reference source, locked green and maximum two colors. G1 covers its failed output. |
| Strict `#RGB`/`#RRGGBB` normalization; deduplicate and limit to eight; conflict before generation | ACHIEVED | `color_models.py:18`, `:42`, `:53`, `:128`; all parameterized color-model and palette-engine tests passed. Allowed colors do not imply required presence. Gradient/count conflicts reject. |
| Three deterministic local recipes, exact locks, achromatic fallback, lazy single engine | ACHIEVED | `color_math.py:20`, `:32`; `palettes.py:138`; deterministic, achromatic, tight-count and missing-engine tests. Only ColorAide was added to the dependency lock. |
| Separate proposal source/evidence from constraints and selection authority | ACHIEVED | `PaletteContent`, `SourceEvidence`, `PaletteRequest`; reference evidence recomputed at proposal/add boundaries; provider data remains inert text. |
| Immutable palette IDs, lineage, digest, active palette and per-artifact binding | ACHIEVED | `color_models.py:145`, `session_models.py:68`, `storage.py:161`; digest tampering, retroactive rebinding and history-removal tests reject. |
| Explicit palette then parent precedence; new generations use active palette; geometry edits inherit | ACHIEVED | `intent.py:20`, `prompts.py:35`, `workflow.py:54`; green/navy/geometry/future-green CLI regression passed; reselected parent export retains its own palette and lockup. |
| Prompt/import effective revision and intent; stale operations fail without artifacts | ACHIEVED | `PromptResult`, shared `resolve_intent`, `Store.expect`; real CLI stale/missing-palette tests and import rollback tests passed. The host still must pass the same saved options and actual final prompt. |
| Read schema 1 without writes, strict version parsing, byte-exact backup, successful migration and retry | ACHIEVED | `legacy_state.py:163`, `storage.py:161`; all 11 palette compatibility tests passed, including backup conflict and injected atomic-save failure. No invented legacy palettes or lockups. |
| Existing background omission behavior and storage paths retained | ACHIEVED | `workflow.py:84`; background compatibility/variant suites passed unchanged. Omitted import background still uses the original brief; host guidance explicitly preserves overrides. |
| Static PNG/JPEG references, 64 MiB/40M limits, EXIF/ROI, immutable local bytes | ACHIEVED | `reference_decode.py:45`, `reference_models.py`, `color_workflow.py:36`; moved external source, profile/orientation/ROI and unsafe-input tests passed. No URL retrieval. |
| Immutable bound report IDs/hashes/versions/status/reasons; analysis failure retains import | ACHIEVED | `color_reports.py:81`, `session_models.py:97`, `import_reports.py:21`; append/failure tests passed; all 17 real stored artifacts remain present. |
| Original-coordinate sampling, alpha-zero exclusion, white retention, fixed evidence thresholds | ACHIEVED | `color_sampling.py:35`, `:92`, `color_analysis.py:94`; boundary tests and independent native recomputation match policy exactly. No threshold relaxation. |
| Profile treatment, Lab D50/explicit CIEDE2000, 99% fit, count and required-color evidence | ACHIEVED | `color_profiles.py:28`, `color_math.py:70`, `color_analysis.py:47`; ICC/gamma, exact 99%, 1% design-color and 32/0.5% presence tests passed. Quantization is separate from matching. |
| Contrast guidance on explicit composited surfaces, no blanket AA gate | ACHIEVED with G3 preview discrepancy | `color_math.py:78`, `color_analysis.py:130`, `color_guide.py:14`; translucent black/white contrast test passed. Measurement ratios do not gate export. |
| Strict/advisory/legacy export, recomputation, no boolean override | ACHIEVED | `color_delivery.py:58`, `delivery.py:107`; forged status/metrics/threshold, missing evidence, unsupported profile and third-color tests passed. Visual review alone cannot make strict failure exportable. |
| Schema-2 manifest/guide and unchanged original PNG/three ZIP payloads/rollback | ACHIEVED | `delivery.py:34`, `color_guide.py`, `export_bundle.py:19`; actual three public archives passed CRC, member-list and PNG-hash checks, with transaction regression tests. |
| At most two additional native repairs per request, exact previous parent, no pixel repairs | ACHIEVED as host workflow | GROVE warm uses `a-v2 → a-v3 → a-v4`; 밤결 and FIELD NOTE use `a-v1 → a-v2 → a-v3`; white uses `white-v1 → white-v2 → white-v3`. Eight initial requests plus eight repairs produce sixteen calls. Helper does not invoke generation. |
| Optional already-connected Leonardo, one attempt/fallback and attribution; no new service | ACHIEVED | `references/color-providers.md`, `THIRD_PARTY_NOTICES.md`, T6 trace; no live Leonardo call is claimed. Optional MCP absence is not a release blocker. |
| Structured horizontal/stacked symbol-plus-text lockup with exact brand/slogan and inheritance | ACHIEVED in software; native observations recorded | `lockup_models.py`, `brief_models.py`, `intent.py`, `prompts.py`, `color_guide.py:98`; lockup CLI tests and horizontal GROVE/TIDE, stacked NORTHLINE/밤결 evidence. Exact font identity is never claimed. |
| Font research: official/community and skill/MCP/API/library distinctions, license/script evidence, shortlist | ACHIEVED | `docs/research/font-tools.md`, `font-shortlist.json`, `references/typography.md`: six tool candidates, eight families, pinned primary-source links, explicit Black Han Sans conflict, no binary/glyph-validation claims or font installation. |
| Portable comparison with explicit selected originals, intent/measurement separation and safe presentation | ACHIEVED with G3 | `color_gallery.py:49`, `color_gallery_data.py`, template; all 26 gallery tests passed. Public `verification.json` records relocation/link checks; Chrome record covers controls and actual downloads. No external script/font required. |
| English default, matching Korean coverage, samples/brand preserved, runnable examples and migration docs | ACHIEVED | Both current READMEs, `references/project-files.md`, T8 documentation evidence; `git diff` shows no changes to existing `assets/`, ten samples or transparency gallery. Public case outcomes are explicit. |
| Eight actual native requests, independent IDs/final prompts, essential anchor/restricted/white successes | PARTIAL | All eight attempted; sixteen source PNGs and seventeen stored artifacts, including one reused parent. Anchor succeeds. G1/G2 prevent this row from being ACHIEVED. |
| Source versions aligned; personal installed/copy-only execution verified | ACHIEVED as development preparation | Plugin/project/lock metadata use clean 0.4.0; PEP 723 pins ColorAide 8.12.1/Pillow 12.3.0. `installation-040.md` records cache `0.4.0+codex.20260912153655`, 15 actual installed CLI calls and unchanged NORTHLINE delivery. |
| All five final reviews, validated release commit/main/tag and published release | MISSED / correctly withheld | T9 depends on essential native successes and final review. This checkout remains uncommitted; no completed v0.4.0 publication evidence exists. Other reviewers are independent and are not presumed approved. |

## Three representative workflow traces

### 1. Automatic palette to successful symbol-plus-text delivery

NORTHLINE selects the local monochromatic candidate with navy `#183A56` and silver `#CDD4DB`, retaining `source=local_harmony`, assistant selection, rationale and palette digest. `palette-add` saves immutable intent; `prompt` returns its binding and stacked lockup; native generation yields `a-v1`; `import` stores original PNG plus advisory report. Explicit visual review/select and `export_colors` recomputation produce manifest 2 and the three-file ZIP. The historical cyan/white brief cannot override the selected palette. The installed-cache record independently exercises this same path without a new generation. This reviewer verified the public ZIP PNG hash `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` and all archive members.

### 2. Anchor edit, inherited intent and safe reselected-parent delivery

GROVE `a-v1` binds `p1`, exact locked `#247A52`, horizontal lockup and transparent background. The requested warmer companion change creates `p2`, then `a-v2` records parent `a-v1`. The two repairs preserve `p2` and follow the previous artifact as parent. Their anchor-only reports pass, but decoded opacity and visible checkerboards fail transparent delivery. Reselecting and exporting `a-v1` retains its `p1` intent and original PNG, independent of active `p2`. The synthetic green → navy → geometry-only regression independently verifies palette precedence under a different active palette. This reviewer remeasured GROVE `a-v1` as pass and visually opened its original and warm `a-v4`.

### 3. Combined reference constraints and unresolved white variant

FIELD NOTE imports the actual GROVE reference, records extraction/hash/scope, combines it with locked green and maximum two colors, and binds a stacked symbol/text lockup before generation. Import preserves the original despite its indeterminate alpha evidence; both native repairs are retained with mismatch and opaque-background findings. Separately, the white request copies 밤결 `a-v1` as explicitly reused `parent-v1`, adds a white-only required palette and makes three native white attempts including the two repairs. `white-v3` remains `indeterminate`; strict export cannot obtain approval from its 100% matching core or its good-looking preview. No white ZIP appears. This reviewer remeasured the saved white original and obtained identical measurements.

## Edge cases traced and exercised

| Edge case | Expected boundary and reviewed outcome |
| --- | --- |
| `#abc` duplicates `#AABBCC`; names/alpha HEX/unknown keys/boolean count | Normalize duplicates; reject unsupported values and schema coercion before calculation or persistence. Color-model and palette-engine tests passed. |
| Three mandatory colors with max two, locked color outside allowed set, gradient plus count | `constraint_conflict`; no image call or state write. Palette-engine negative cases passed. |
| Geometry-only child after the active palette changes | Parent palette/lockup win. Real CLI regression retains navy while future-generation green is active. |
| Old artifact without palette/lockup and schema-1 null/missing background | Unknown stays unknown; background fallback stays historical. Read-only and migration/background regression suites passed. |
| State changes between prompt and import | `stale_revision`, no orphan PNG or state mutation. CLI and transaction tests passed. |
| Reference source disappears, invalid ROI, path escape, symlink or duplicate ID | Stored reference survives external movement; unsafe/missing/conflicting input fails without overwriting state. Reference/CLI tests passed. |
| Hidden red at alpha zero beside visible white | Hidden RGB excluded; white survives extraction and strict conformance. Independent synthetic fixture passed. |
| 127 versus 128 core pixels, 10% versus over 10% partial alpha | Below-minimum/excess partial alpha is indeterminate. All threshold cases passed; actual 밤결/white reproduce the latter. |
| 99% fit, 1% observed color, 31/32 matches and 0.5% required share | Fixed boundary fixtures distinguish pass, mismatch and indeterminate without deriving expected values from production functions. All passed. |
| Unsupported ICC, non-sRGB gamma, absent ColorAide | Explicit unsupported/indeterminate or named unavailable-engine result. Imported artifact retained; strict export cannot trust a forged pass. |
| Stored pass/coverage/threshold tampering and all-true visual review | Export recomputes current fixed policy from original bytes. Red/third-color source still returns `color_mismatch`; uncertain source returns `color_review_required`. |
| Failed state/publish write after earlier successful export | New files/report roll back and prior PNG/ZIP/state remain. Migration backup is preserved and verified on retry. |
| HTML-shaped brand, role or report reason; missing report; relocated gallery | Escaping makes text inert; unknown cannot render as pass; explicit PNG copies and relative links survive relocation. Gallery tests passed. |
| All warm repairs have a color pass but zero transparency | Separate background/visual checks prevent delivery; public labels correctly avoid calling the image transparent or ready. |

## Independently executed checks

All new writes were confined to this report and `output/review-goal/`. No source, real session, native image, installed cache, browser, commit, push or release was changed by this reviewer.

| Check | Actual result | Local review evidence |
| --- | --- | --- |
| Full source test suite | 299 passed in 104.14 seconds | `output/review-goal/pytest.txt` |
| Ruff on production scripts and tests | Pass | `output/review-goal/ruff.txt` |
| Basedpyright | 0 errors, 0 warnings, 0 notes | `output/review-goal/types.txt` |
| Formatting on production scripts and tests | 58 files already formatted | `output/review-goal/format.txt` |
| Offline lock consistency | 23 packages resolved; exit 0 | `output/review-goal/lock.txt` |
| CLI `show` for seven copied real sessions | All succeed, validating all stored artifact hashes/facts | `output/review-goal/*-show.json`, `native-state-summary.json` |
| Native color recomputation: GROVE original, 밤결 original, final white | pass / indeterminate / indeterminate; all metrics equal saved reports after excluding only ID/time | `output/review-goal/*-reanalyzed.json`, `*-fresh-metrics.json`, `*-saved-metrics.json` |
| Exact native source identities | 16 distinct recorded source PNG hashes match the public provenance set | `output/review-goal/native-source-hashes.txt` |
| Public session PNG copies | 17 hashes match saved evidence | `output/review-goal/public-artifact-hashes.txt` |
| Actual final prompt strings | 17 public prompt files match saved strings byte-for-byte | `output/review-goal/prompt-byte-checks.txt` |
| Public NORTHLINE/GROVE/TIDE archives | Three CRC checks pass; exactly three expected members; archived PNG matches standalone/original | `output/review-goal/public-delivery-hashes.txt` |
| Source scope and whitespace | Existing brand/ten samples/transparency files unchanged; `git diff --check` passes | Base diff; `output/review-goal/reviewed-status.txt`, `reviewed-files.sha256` |

Reproducible test command, using the existing environment without installation:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q \
  -p no:cacheprovider --basetemp output/review-goal/pytest
```

The native recomputation used a private copy of `.logo-generator/` under `output/review-goal/native/`, existing PNGs, the copied session's current revision and the real helper `color-analyze` command. It made no native generation/edit calls and no pixel modifications. Public verification is not based on synthetic logos.

## Review limits and disposition

Full production modules for models, migration/storage, palette/reference math, prompt/import workflow, analysis, delivery and gallery were read, along with the new regression suites and relevant legacy background/delivery tests. The full plan, review context, both READMEs, skill/reference guides, font research, native-case records, Chrome record, installation record and version diff were inspected. Generated public session evidence was traversed for every case/artifact; repeated generated HTML was assessed through its production renderer, structured evidence and the saved Chrome observations.

This reviewer opened the real GROVE original/warm PNGs and saved final white Chrome screenshot, but did not control Chrome or claim a new visual rendering at all sizes. The 46 screenshots and three downloaded ZIP comparisons belong to the named Chrome worker. Installed-cache commands were read from their detailed receipt, not repeated here. No cold-cache offline install, fresh GUI skill selection, authenticated font API, font binary validation or new native call is claimed. The unrelated `codex plugin list` marketplace failure remains documented in `installation-040.md:111` and does not negate the successful direct installed-cache checks.

No unrequested runtime, font installation, paid image API, Pantone data, vector engine, brand replacement or existing-sample rewrite was found. The model split and staging helper are proportionate to typed immutable state and the explicit module-size constraint. The complete goal and public release remain **FAIL** until G1/G2 and the final review/publication prerequisites are actually fulfilled; a development commit can preserve the implemented behavior and evidence without claiming those outcomes.
