# Logo Land v0.4.0 — Color workflow implementation plan

## TL;DR

> **Summary:** Add conversational palette selection, composable color constraints, and an honest measurement report for each generated logo. Keep native Codex image generation and the existing Python helper.
> **Deliverables:** Four conversational entry points; immutable palette history; local palette/contrast/color-difference calculations; reference-image extraction; per-artifact reports; a comparison HTML page; English/Korean documentation; a tested v0.4.0 release.
> **Effort:** Large; nine implementation tasks plus independent final verification.
> **Parallel:** Yes, after the shared contract is implemented. Use Orca tasks with explicit file ownership.
> **Critical path:** T1 → T2/T3 → T4 → T5 → T8 → final verification → T9.
> **Current status:** Execution authorized on 2026-09-13 KST. Also research fonts and implement explicit symbol-plus-text lockups, then update samples, bilingual README and version. Orca run: `run_c07646c87b07`.

## Execution checkpoint — 2026-09-13

T1–T7 and font research are implemented. The final integrated 315 tests, static checks, installed-helper execution, eight-request native gallery, original-byte checks and Chrome QA are recorded under `docs/qa/color-workflow/`. Five independent reviews are complete; their C1 legacy-export finding is corrected and independently rechecked. G3 is corrected for future galleries. The final 55-file personal installation passed 29 CLI checks, including two expected strict refusals. Development-source readiness is PASS; whole-goal/public-release readiness remains blocked by the native gates below. Source/personal development version is 0.4.0, while the published release remains 0.3.1. The review integration records each checkpoint separately.

T8's native success gate remains unmet: restricted-color and white-transparent candidates are indeterminate or failed after the bounded repairs. The white candidate looks clean in Chrome, but its declared alpha sampling policy remains indeterminate. Keep T8/T9 unchecked until the required evidence passes; do not infer completion from a prepared version or passing software tests.

The tested development implementation was committed and pushed as `b391ca8e2b463589efc870ff478a51b9f5f6f32c`. GitHub draft release `387630647` targets that commit and remains unpublished; no v0.4.0 tag exists. See `docs/qa/color-workflow/release.md` for the read-back evidence. All assigned Orca workers are complete and released. Remaining work is the unresolved native acceptance and consequent public release, not an uncommitted implementation.

Continuation escalation independently confirmed that all three white-native attempts fail the same partial-alpha criterion. The explicit three-failure stop condition and contract 12 end this bounded automation run with unresolved findings. T8, VERIFY and T9 remain unchecked; no additional native attempt, threshold change or public release is authorized by continuation. The plan and project remain available for subsequent user-directed work. See [the escalation audit](../docs/qa/color-workflow/continuation-escalation.md) for exact artifact identities, the unavailable specialist limitation and cleanup receipts.

## TODOs

- [x] T1 — Typed color/state contracts, v1 compatibility, dependencies and lockup types.
- [x] T2 — Deterministic constrained palette proposals.
- [x] T3 — Reference extraction and color analysis.
- [x] T4 — CLI, prompt/import intent binding and lockup inheritance.
- [x] T5 — Color-aware delivery and truthful typography metadata.
- [x] T6 — Conversational skill and optional Leonardo guidance.
- [x] T7 — Portable palette/result/lockup comparison HTML.
- [ ] T8 — Real native samples, font/lockup cases, portability and bilingual docs.
- [x] FONTS — Primary-source font/typography skill, MCP and service research.
- [ ] VERIFY — Five independent final reviews and fixes.
- [ ] T9 — Aligned version, personal installation, commit/push/main/tag/release.

### Authorized extension: fonts and symbol-plus-text logos

The user explicitly asked to implement the plan, research fonts, support logos with both a symbol and text, and update README/samples/version. Existing `logo_type=combination` remains; add an optional structured `LockupIntent` at brief/artifact level: `layout` horizontal/stacked, `symbol_position` start/end (left/right for horizontal, above/below for stacked), `text_alignment` start/center/end, `typography_style` plain-language text, and optional `font_reference` as a requested visual reference only. Preserve exact brand/slogan strings. Prompt/import accept the same optional lockup JSON, edits inherit their parent's intent unless overridden, and old artifacts remain unknown. Font names never prove a generated raster uses an actual licensed font file. Do not install/bundle font binaries or introduce a separate typesetting/image-editing engine in this release.

Research is saved in `docs/research/font-tools.md` with official/community and skill/MCP/API/library distinctions, actual source/license evidence, Hangul/Latin coverage and a practical shortlist. Feed findings into a concise typography reference and into real horizontal/stacked/Hangul samples. Eight planned live cases may be assigned these layouts so the new scope does not unnecessarily multiply generations. T1 owns shared lockup models, T4 owns prompt/import plumbing, T5 owns delivery metadata, T6 owns skill guidance, and T8 owns final samples/docs.

## Context

### Original request and accepted context

The user requested an improvement plan after researching Adobe Leonardo, Pantone, and public color skills/MCPs. Logo Land must continue creating and editing actual logos through the native image tool, including transparent PNGs. The user prefers Orca orchestration with the coordinator supervising parallel work. The default README, repository About and releases remain English; the Korean README remains available with centered language/release badges.

Baseline inspected on 2026-09-12: local `main`, commit `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`, plugin/helper v0.3.1. Recheck the base when implementation starts. This plan is the sole execution plan; previous research findings are incorporated below rather than requiring temporary reports at execution time.

### Current implementation facts

- `skills/logo-land/scripts/logo_helper/models.py`: `Brief.palette` is free-text intent, `Session.schema_version` is 1, and JSON models forbid unknown fields. There is no existing anchor-HEX contract.
- `prompts.py:build_prompt`: sends the original palette to the image tool and preserves exact parent paths. It does not calculate or validate colors.
- `workflow.py:import_image`: saves original PNG bytes with stable IDs, hashes, parent relationships, and optimistic revisions.
- `storage.py:Store.load`: reparses state and verifies all saved PNG hashes and decoded facts. Mutations use locks and atomic state writes.
- `delivery.py:export`: checks visual review and background requirements and stages an original PNG, manifest, guide and ZIP. Palette values currently describe historical intent.
- `images.py:inspect_png`: validates static PNG, visibility and alpha; it does not perform ICC-aware color measurement.
- `tests/`: pytest tests exercise actual CLI subprocesses, state portability, rollback, background inheritance, path safety and export bytes. Do not confuse these synthetic tests with native-image quality checks.

### Architecture decision

Use **Pillow + ColorAide 8.12.1 inside the existing Python helper**. Pillow already decodes images; ColorAide supplies color conversion, harmony and distance calculations. Pin the same ColorAide version in `pyproject.toml`, `uv.lock` and the PEP 723 header of `logo_project.py`. Import the color engine lazily so legacy read/PNG operations do not unnecessarily depend on it.

Use **Leonardo as an optional, already-connected host MCP suggestion source** and incorporate a small attributed selection guide derived from Leonardo/color-expert. Every suggested palette passes the same local constraint checks. The helper does not start MCP servers or invoke the image tool. No Node bridge, Culori, Color Thief, or new standalone color MCP is required in this release; those would duplicate functionality and add a second runtime.

ColorAide's Python implementation, MIT license, version and compatibility were checked through its official documentation and PyPI metadata. This is an integration choice based on repository fit, not a claim that ColorAide universally produces better palettes than the JavaScript alternatives.

### Metis review incorporated

Orca run `run_eaec79686c24` contains the independent code/test mapping and Metis gap review. Decisions below resolve their findings: composable constraints instead of mutually exclusive modes; explicit v1 migration; per-artifact palette binding; no inferred legacy HEX; preserved white pixels; ICC handling; sampled rather than exact-pixel claims; bounded repairs; aligned project/script dependencies. The existing background-import default is a tested contract and must remain unchanged.

## Work objectives and product decisions

### User-visible behavior

| Entry point | Example request | Behavior |
|---|---|---|
| Automatic | “Choose warm colors for a bakery logo.” | The assistant translates the brief into up to three distinct candidate palettes and selects when choice is delegated. |
| Anchor | “Keep #247A52 and suggest warmer companion colors.” | Preserve that normalized RGB value in palette data; change only unlocked companion colors. |
| Restricted | “Use only black and ivory, at most two colors.” | Apply an allowed set and maximum visible design-color count; forbid gradients by default. |
| Reference | “Use the colors of this photo.” | Extract actual colors from a local PNG/JPEG, show the extraction scope, and turn selected colors into a candidate. |

These are conversational entry points, not an exclusive enum. A reference image can be combined with a locked HEX and a two-color limit. Store the **proposal source** separately from **constraints**.

When a logo request already authorizes generation, do not insert mandatory palette approval. If the user delegates the choice, record `selected_by=assistant` and a rationale. If the user asks to compare colors first, show palette cards and wait for selection without generating logos. Follow the existing concept-count behavior instead of multiplying logo concepts by all palette candidates.

### Locked implementation contract

1. **Colors:** public structured inputs accept `#RGB` or `#RRGGBB`, normalize to uppercase six-digit sRGB, and reject alpha HEX, CSS expressions and names. Free-text legacy `Brief.palette` remains unchanged. The assistant may propose a concrete HEX for a named color, but must not describe it as a measured historical value.
2. **Constraints:** `locked_hex`, optional `allowed_hex`, optional `max_colors` (1–8; null means no explicit count constraint), `required_hex`, and `allow_gradients` (default false). Ordinary proposals prefer three colors without making that preference a strict output constraint. Deduplicate after normalization; each locked/allowed/required list is bounded to eight unique colors. Locks and required colors must be members of an allowed set when one exists; required/locked distinct count cannot exceed `max_colors`. Return `constraint_conflict` before any image call. `required_hex` expresses an explicit request that particular colors must appear; an allowed list alone does not require every color. Reject a gradient request combined with a strict allowed-set/count limit instead of silently relaxing either.
3. **Count scope:** v0.4.0 counts visible colors in the declared image/ROI scope, including an opaque background. Transparency and CSS preview surfaces are excluded; intentional white/black artwork is included. Explain this scope when an opaque background consumes a color slot. Do not claim foreground segmentation or count raw unique antialiased RGB values as design colors.
4. **Palette proposals:** source is `assistant`, `local_harmony`, `reference`, or `leonardo`; constraints compose independently. Default suggestions are three arrays with roles, HEX and a short rationale. Local harmony supports monochromatic, analogous and complementary recipes in OKLCH; preserve locked sRGB values verbatim and gamut-map only generated companions. For achromatic anchors, use documented preset companion hues 45°, 145° and 250° rather than an undefined hue. Given the same structured seed, recipe and version, local results and ordering are deterministic. No such guarantee applies to conversation or generated images.
5. **Immutable intent:** introduce `PaletteVersion` with ID, parent palette ID, normalized swatches/roles, constraints, source, source evidence, selected-by, rationale, canonical content digest and calculation version. `Session` stores an append-only palette list plus the active palette ID for new generations. Each `Artifact` records its actual palette ID; old artifacts keep `null`.
6. **Edits:** explicit palette ID → parent's palette ID → no structured intent for a legacy edit. New generations use the explicit or active palette. The initial brief never overrides a parent's revised palette. A color-change request creates a new palette version; a geometry-only edit inherits. `PromptResult` returns effective palette ID/digest and session revision; import uses the same revision and palette binding. Preserve the existing `--background` omission behavior separately.
7. **State v2:** keep strict schema-1 models in a compatibility module and parse by version. `show`, `list` and `prompt` convert in memory without changing v1 JSON bytes or revision. The first successful explicit mutation writes a verified `session.v1.backup.json` once and atomically saves v2 under the current lock. Reject unknown schema versions and corrupt state. Do not infer palettes/reports for old artifacts. Document forward reading of v1, not v0.3.1 reading v2.
8. **Reference provenance:** accept bounded static PNG/JPEG only, using the existing 64 MiB and 40M-pixel limits. Copy original bytes to immutable session-local `references/<id>.png|jpg`; record hash, actual format, dimensions, EXIF orientation and optional integer ROI. Interpret orientation for analysis in memory. References are separate from edit-parent artifacts. No URL fetching or hidden dependence on an external absolute path after import.
9. **Reports:** append immutable `ColorReport` records keyed by report ID and bind them to artifact ID/hash, palette ID/digest, analysis-policy ID, ColorAide/Pillow versions, profile treatment and sampling/ROI settings. Status is `pass`, `mismatch`, `indeterminate` or `unverified`; report the reason and actual quantities. A display can name the latest matching report, but cannot overwrite earlier evidence. Color-analysis failure must not erase an imported image or become a fictitious generation failure.
10. **Exports:** legacy palette-less artifacts keep the existing export behavior, labeled color-unverified. Auto/reference without explicit locks/limits is advisory. Any explicit lock, allowed set, required-color constraint or explicit count limit enables strict checking. A strict export with missing/indeterminate evidence returns `color_review_required`; mismatch returns `color_mismatch`. Visual review cannot override either. Export recomputes the selected report from verified original bytes, rather than trusting a stored `pass`. No blanket bypass flag or automatic threshold relaxation. An explicit user decision to change constraints creates a new palette/version and, if necessary, a new native edit.
11. **Delivery truth:** include intended swatches, measured swatches/coverage, delta-E, method/limits and contrast guidance in the existing manifest/brand guide. Embed the color report into the manifest; retain the ZIP's three payload files (`logo.png`, `manifest.json`, `brand-guide.md`). Preserve PNG bytes, prior exports and existing rollback behavior. Version the expanded manifest as 2; old exported packages remain untouched.
12. **Native repair:** after a mismatch, the host may make at most two additional native edits for the same user request, using the exact previous artifact and preserving lettering/layout/background. Record each attempt and re-inspect it. Stop with truthful unresolved findings if the limit is reached; retain candidates. No Python recoloring, image regeneration through a paid API, or automatic weakening of intent.

### Measurement policy `logo-color-v1`

The numbers below are product heuristics for sampled raster checks, not a Pantone match, print proof, accessibility certification, or exact-pixel guarantee.

- Preserve original file bytes. ICC conversion, orientation and sampling operate only on decoded memory used for analysis; do not save an altered master.
- Use declared sRGB directly; transform a supported embedded RGB ICC profile to sRGB with Pillow ImageCms. Untagged images are explicitly `assumed_srgb`. Unsupported/malformed ICC or unsupported non-sRGB gamma-only metadata produces `indeterminate`, never an unqualified sRGB pass.
- Sampling: use all pixels up to 16,384 positions; otherwise use a deterministic 128×128 grid over the explicit ROI or full image, with integer pixel-center coordinates and no resize interpolation. Record dimensions, coordinates policy and sampled fraction. Keep exploration quantization separate from conformance calculations.
- Exclude alpha=0. For color conformance use alpha≥250; record alpha 1–249 as edge/partial-alpha coverage. Never ignore white or relax alpha thresholds to obtain a result. Fewer than 128 core samples, or partial-alpha samples exceeding 10% of visible samples, makes strict conformance `indeterminate`.
- Convert sampled core RGB and target swatches to the same Lab D50 coordinates and call ColorAide with `method="2000"` explicitly. Compute nearest-target distance from original sampled colors, caching duplicate RGB values. Do not use the library's default distance method implicitly.
- Initial closeness threshold is ΔE00≤5. Restricted conformance requires at least 99% of sampled core pixels within the allowed colors; record both matched and unmatched fractions. Count observed matched design colors with ≥1% share against `max_colors`; report smaller groups separately rather than deleting them.
- A locked or required color needs at least 32 matching core samples and ≥0.5% core share. Insufficient evidence is `indeterminate`, not proof the color is absent. A clearly different, sufficiently sampled color distribution is `mismatch`. Color roles/placement still require visual inspection; a histogram cannot prove that a color belongs to a particular letter or symbol.
- A full-image opaque report is a global composition check. A manually specified ROI narrows that claim; it is not an automatic foreground mask. Every report and gallery card names its scope. Sampling may miss a tiny accent; do not market sampled coverage as a census of all pixels.
- Contrast uses explicit foreground/surface pairs, WCAG 2 ratio, and alpha compositing on those surfaces. Default preview surfaces are `#FFFFFF` and `#171717`; use a requested surface when supplied. Ratios are readability guidance and do not gate a logo by a blanket AA threshold.
- Quantized palette extraction uses Pillow median-cut on eligible RGB samples, at most eight candidates, ordered by sample share then HEX. It keeps white. Extracted colors are estimates, not locked values or conformance evidence by themselves.

### Scope boundaries

Include the above local workflow, optional already-connected Leonardo usage, attributed guidance, real samples, a comparison page, bilingual docs and the eventual v0.4.0 release. Defer Pantone data/API licensing, paid palette services, automatic MCP setup, a second runtime, UI-token systems, automatic semantic segmentation, editable vectors and color-vision raster variants. Do not change branding, repository name/visibility, storage-root naming or unrelated background semantics.

## Verification strategy

- Use focused TDD with existing pytest subprocess/transaction fixtures. Pair implementation and regression tests in each task; no synthetic test is evidence that the native image tool ran.
- Run Ruff/basedpyright for changed Python and then the documented full checks once the integrated changes pass. Keep modules under 250 lines through small typed modules; do not disable strict parsing or add broad lint exemptions.
- Every task has a positive and negative scenario below. Save command outputs, fixture descriptions and live observations under `docs/qa/color-workflow/` during execution. Use `output/` for temporary artifacts until intentionally selecting public samples.
- Check both the locked project invocation and a copied-scripts PEP 723 invocation. Initial dependency preparation may use the existing uv install workflow during authorized implementation; normal color calculation must not download tools, call paid services or modify host MCP configuration. Do not claim cold-cache offline installation.
- All verification is agent-executed. Normal success does not require another user approval gate. Implementation and publication are authorized by the current execution request and prior release instructions.

## Execution strategy

### Dependency matrix and ownership

| Task | Owner | Dependencies | Exclusive responsibility |
|---|---|---|---|
| T1 | State worker | — | Color/state types, compatibility adapter, storage contract, dependencies |
| T2 | Palette worker | T1 | Local proposal/constraint functions and their tests |
| T3 | Analysis worker | T1 | Reference decoding, alpha/profile sampling and measured reports |
| T4 | Workflow worker | T2, T3, T7 | Palette/reference/report/gallery commands, prompt/import binding, mutations |
| T5 | Delivery worker | T4 | Strict/advisory export checks, manifest and guide |
| T6 | Skill/docs worker | T1 | Conversational guide and attributed optional Leonardo integration |
| T7 | Gallery worker | T1 | Read-only HTML palette/results presentation using the fixed report contract |
| T8 | QA/integration worker | T5, T6, T7 | Real native-image scenarios, portability, README/docs and integrated checks |
| T9 | Release owner | T8 + all final reviewers | Version metadata, installation verification, commit/push/tag/release |

Wave 0: T1. Wave 1: T2, T3, T6 and T7 in parallel. Wave 2: T4 then T5. Wave 3: T8 and final review. Wave 4: T9. Deliberately do not split tasks solely to fill a parallelism quota; state and export integration have real dependencies.

The coordinator owns the Orca DAG and integration decisions. Each worker receives exact file ownership and a reminder not to revert other workers. Read-only reviewers share the checkout; create another worktree only for an actual filesystem/checkout conflict. Process all delivery messages, release each completed worker, and preserve evidence. Shared files move to the next owner only after the prior task settles.

## Implementation tasks

### T1 — Establish typed state, compatibility and dependency contracts

**Owner/files:** state worker; existing `models.py`, `storage.py`, `pyproject.toml`, `uv.lock`, the PEP 723 header only in `logo_project.py`; new `logo_helper/color_models.py`, `logo_helper/legacy_state.py`, `tests/test_palette_compatibility.py`, `tests/test_color_models.py`. Paths under `logo_helper/` refer to `skills/logo-land/scripts/logo_helper/` throughout this plan.

**Work:** Implement the locked data contract above, including separate proposal source/constraints, PaletteVersion/Reference/ColorReport append-only records, consistent IDs/digests and schema-1 reader. Break type definitions into an additional `color_reports.py` if needed to keep modules below 250 lines. Do not weaken unknown-field rejection. Add the exact ColorAide dependency to both execution paths and resolve its lock once; avoid unrelated upgrades. Migration backup must be verified/reused on retry rather than overwritten.

**References:** existing `models.py:FrozenModel`, `Session.consistent_lineage`; `storage.py:Store.load/expect/save`, `atomic_state`; `tests/test_background_compatibility.py`; `tests/test_transactions.py`; ColorAide package reference above.

**Acceptance/QA:**
- Happy: create schema-1 fixtures with free-text `green`, an edited navy prompt and missing/null background overrides; run `show/list/prompt` and assert state bytes/revision unchanged. A successful explicit mutation produces v2 and a byte-identical v1 backup; artifact hashes/selection/exports remain intact.
- Edge: duplicate normalized colors, unknown field, future schema, missing palette parent, changed palette digest and locked count conflicts each return a typed error. Inject state-save failure and assert no partial v2 state and no overwritten backup. Keep existing background-default tests unchanged.
- Commands: `uv run --locked pytest tests/test_palette_compatibility.py tests/test_color_models.py tests/test_background_compatibility.py tests/test_transactions.py`; `uv lock --check`.
- Evidence: `docs/qa/color-workflow/t1-state.txt` plus documented fixture versions.

**Parallelization:** first task; blocks T2/T3/T6/T7. **Commit:** `feat(color): add compatible palette and report state`.

### T2 — Build deterministic palette proposals and constraint validation

**Owner/files:** palette worker; new `logo_helper/palettes.py`, `logo_helper/color_math.py`, `tests/test_palette_engine.py`. Do not edit shared state/CLI files.

**Work:** Implement normalized candidate input, local harmony recipes, lock preservation, source/rationale metadata and deterministic sorting. The public `palette-propose` result contract is `{session_id, revision, candidates, warnings}`; it does not save state or generate images. Accept assistant/Leonardo candidates through the same typed validation function. A malformed or lock-breaking external suggestion is rejected with a reason; the host can then request local candidates. Constraints are validated independently of the source. Use explicit ColorAide algorithms; cache repeated calculations within a call and lazy-load the engine.

**References:** T1 `ColorConstraints/PaletteVersion`; `prompts.py:PromptResult` for read-only result conventions; `models.py:ProjectError`; official ColorAide harmony/distance references.

**Acceptance/QA:**
- Happy: with anchor `#247A52`, produce three supported recipe candidates. Repeating the same input yields byte-equivalent normalized colors/order, and every candidate retains the anchor RGB exactly. A reference-derived candidate plus lock and max 2 satisfies all three conditions.
- Edge: `#abc`/`#AABBCC` duplicates collapse; three locked colors with max 2 fail before persistence; `#GG0000` and an external candidate that replaces the anchor are rejected. A neutral anchor produces valid deterministic companions rather than NaN. Missing engine returns `color_engine_unavailable`, not an auto-install.
- Commands: `uv run --locked pytest tests/test_palette_engine.py tests/test_color_models.py`.
- Evidence: `docs/qa/color-workflow/t2-palettes.txt` with concrete input/output JSON.

**Parallelization:** after T1; parallel with T3/T6/T7; blocks T4. **Commit:** `feat(color): calculate constrained palette candidates`.

### T3 — Implement bounded reference extraction and honest raster analysis

**Owner/files:** analysis worker; new `logo_helper/color_sampling.py`, `logo_helper/color_analysis.py`, `logo_helper/references.py`, `tests/test_color_analysis.py`, `tests/test_reference_colors.py`. Keep `images.py` and the master PNG unchanged. Consume T1 types and the fixed ColorAide method contract; coordinate any common math helper additions through T2's owner.

**Work:** Implement PNG/JPEG reference inspection, orientation/ICC processing in memory, deterministic sampling and extraction; then the `logo-color-v1` checks. Reference extraction and artifact conformance are separate functions. Preserve white and report sample/profile limitations. A lock-only policy tests lock presence; it does not restrict unspecified companion colors. Allowed-set/count constraints compare against their explicit or selected-palette targets. Return structured metrics and reasons rather than a single unqualified score. Cap work by existing input limits and the 16,384-position sample limit.

**References:** `images.py:inspect_png`, `storage.py:read_source/MAX_FILE_BYTES`, `tests/test_boundaries.py`, T1 report/reference models and the measurement policy above.

**Acceptance/QA:**
- Happy: deterministic 256×256 PNG with 50% `#000000`, 50% `#F6F3EC` passes the two-color policy. White lettering in transparent RGBA remains in the palette; alpha-zero red RGB is excluded. Same input/configuration gives the same measured quantities. All image hashes are unchanged.
- Edge: a 5% visible red patch causes restricted mismatch; all-alpha-zero reference and no-core/mostly-semitransparent fixtures return explicit insufficient evidence. Test supported ICC, malformed ICC, untagged sRGB assumption, EXIF-oriented JPEG, invalid ROI and non-PNG/JPEG input. Test both sides of the declared coverage/distance/required-color thresholds using independent fixed fixtures, not production functions to derive expected answers.
- Performance: analyze a 4096×4096 solid/antialiased fixture on the test machine in at most 30 seconds; record runtime and at most 16,384 sampled positions. Reject >40M pixels and >64 MiB before expensive processing. This is a project budget, not a universal performance claim.
- Commands: `uv run --locked pytest tests/test_color_analysis.py tests/test_reference_colors.py tests/test_boundaries.py`.
- Evidence: `docs/qa/color-workflow/t3-analysis.txt`, fixture descriptions and raw metric JSON.

**Parallelization:** after T1; parallel with T2/T6/T7; blocks T4. **Commit:** `feat(color): inspect reference palettes and logo color fidelity`.

### T4 — Wire palette selection, imports, edits and reports into the CLI

**Owner/files:** workflow worker; existing `logo_project.py`, `logo_helper/prompts.py`, `logo_helper/workflow.py`; new `logo_helper/color_cli.py`, `logo_helper/color_workflow.py`, `tests/test_palette_workflow.py`; extend `tests/test_transactions.py`. Shared type changes return to T1's owner before this task starts.

**Work:** Register these additive flat commands without breaking current commands:

| Command | Required inputs | Effect |
|---|---|---|
| `reference-add` | `--session --reference --image --revision` | Copy bounded immutable reference and record provenance. |
| `palette-propose` | `--session --request-file`; optional `--reference` | Return validated candidates; no state change. |
| `palette-add` | `--session --palette --palette-file --revision` | Append a selected palette version and make it active for new generations. |
| `color-analyze` | `--session --artifact --revision`; optional `--roi-file` | Analyze original bytes and append a bound report. |
| `color-gallery` | `--session --artifacts --output` | Render explicitly listed artifact IDs into a new portable gallery directory; no session mutation. |

Add optional `--palette` to `prompt` and `import`. Parse the same effective palette binding in both and use the optimistic revision returned by `prompt`. If intent exists, `import` preserves the PNG and appends its initial report even when the report is mismatch/indeterminate; generation succeeded independently of fidelity. Errors during analysis produce an explicit unverified report/error reason, not a nonexistent artifact. Run all writes under the existing lock/rollback discipline. Factor command registration instead of expanding the entry file beyond its module limit.

**References:** `logo_project.py` existing Typer options and error JSON; `workflow.py:advance/import_image/record_failure`; `prompts.py:build_prompt`; `tests/conftest.py:Harness`; `tests/test_background_compatibility.py` for the independent legacy background contract.

**Acceptance/QA:**
- Happy: init → add green palette → prompt/import `a-v1` → add navy palette → prompt/import `a-v2` using `a-v1` → geometry-only `a-v3`. `a-v3` inherits navy even if active future-generation palette is changed back to green; reselecting `a-v1` still resolves green. Reference copy works after the external reference file is moved away.
- Edge: state changes between prompt and import produce `stale_revision` and no new artifact. A missing palette/reference ID, duplicate ID, malformed report input, symlink, or save failure cannot overwrite previous state/files. No command accepts an arbitrary caller-supplied `passed=true` measurement.
- Commands: `uv run --locked pytest tests/test_palette_workflow.py tests/test_transactions.py tests/test_cli_safety.py tests/test_background_compatibility.py`; run helper `--help` and each new command's help.
- Evidence: `docs/qa/color-workflow/t4-cli.txt`, with the actual prompt's revision/palette and imported report IDs.

**Parallelization:** after T2/T3/T7; blocks T5. **Commit:** `feat(color): preserve palette intent across logo revisions`.

### T5 — Make exports reflect the selected logo's real color evidence

**Owner/files:** delivery worker; existing `logo_helper/delivery.py`, `tests/test_delivery_guide.py`; new `logo_helper/color_delivery.py`, `tests/test_color_reports.py`. Keep color report presentation out of the original PNG bytes.

**Work:** Resolve selected artifact intent, recompute measurements from verified original bytes, enforce strict/advisory policy and embed the current report into manifest v2 and the brand guide. Successful exports append their report/state changes atomically; a failed export leaves state and output directories unchanged. A user cannot bypass strict conformance through `review` or by editing a stored report's status. Preserve the existing three ZIP payloads and original bytes. Missing optional Leonardo is irrelevant to local export verification.

**References:** `delivery.py:Manifest/guide/export`, `storage.py:Store.load`, `tests/test_reserved_output.py`, `tests/test_transactions.py`, `tests/test_delivery_guide.py`, T1/T3 report and analysis contracts.

**Acceptance/QA:**
- Happy: the selected green artifact exports its green intent/report even after a navy child exists. Original PNG bytes match the archive entry. Advisory mismatch exports with explicit measured limitations; legacy export reports no invented HEX or measured success.
- Edge: strict fixture with a visible third color fails with `color_mismatch` even after all visual booleans are true. Missing profile/core evidence fails with `color_review_required`. Change stored report status/metrics/palette binding and verify recomputation prevents a false pass; a changed PNG hash still fails before export. Inject a publish/state-write failure and preserve prior files.
- Commands: `uv run --locked pytest tests/test_color_reports.py tests/test_delivery_guide.py tests/test_transactions.py tests/test_reserved_output.py`.
- Evidence: `docs/qa/color-workflow/t5-export.txt` and representative manifests/guides.

**Parallelization:** after T4; blocks T8. **Commit:** `feat(color): export measured palette evidence and enforce constraints`.

### T6 — Teach the skill conversational color selection and optional Leonardo use

**Owner/files:** skill/docs worker; `skills/logo-land/SKILL.md`, new `skills/logo-land/references/color-workflow.md`, `skills/logo-land/references/color-providers.md`, new `THIRD_PARTY_NOTICES.md`. Defer command-schema edits in `references/project-files.md` and root READMEs to T8.

**Work:** Add the four entry points, composable constraints, roles, automatic-selection behavior, palette-to-concept mapping, version-preserving edits, sampled-check limitations and two-repair limit. Include six concise example palette directions as ordinary sRGB suggestions, not universal industry rules. Attribute any adapted Leonardo/color-expert instructions with author, pinned source, license and modification note. Do not copy whole external reference collections or install a second conflicting skill.

When the host already exposes Leonardo, allow one suggestion attempt using its documented `generate-theme`/`create-palette` tools as appropriate; record source and actual tool response. Normalize output and preserve locks locally. `check-contrast` can supplement advice, but local report policy remains authoritative. If the tool is absent, errors or produces invalid output, record that state and continue with the local/assistant proposal. Do not fabricate a Leonardo call, claim its interpolated scale is semantic brand judgment, or invoke `npx` automatically. Do not add a mandatory `.mcp.json` connection in v0.4.0.

**References:** existing `SKILL.md` execution/start/generate/refine sections; `references/native-image.md`; pinned upstream skill/MCP/license references in this plan.

**Acceptance/QA:**
- Happy: a written trace for “Use this photo, keep #247A52, at most two colors, choose for me” reaches one coherent constraint object, a selected palette and generation without an extra mandatory approval. A geometry-only edit inherits the selected parent palette.
- Edge: a trace with unavailable Leonardo uses the local path and never claims external generation/checking. A conflicting locked/allowed set stops before image calls. A two-repair failure preserves candidates and does not promise a final compliant export.
- Check examples against T1's parser once available; use T2's invalid-provider fixtures for normalization. Live optional MCP evidence is recorded in T8 only if the capability actually exists.
- Evidence: `docs/qa/color-workflow/t6-conversation.md` with positive/failure transcripts and attribution checklist.

**Parallelization:** after T1; parallel with T2/T3/T7; blocks T8. **Commit:** `docs(skill): add conversational palette and Leonardo guidance`.

### T7 — Build a read-only palette and result comparison page

**Owner/files:** gallery worker; new `skills/logo-land/assets/color-gallery.template.html`, `logo_helper/color_gallery.py`, `tests/test_color_gallery.py`. Use the visual language of existing `docs/samples/index.html` and `docs/transparency/index.html`; do not redesign the brand or overwrite the existing ten samples.

**Work:** Render a local HTML page from selected session/artifact/report data: palette cards with roles/HEX/rationale, intended-versus-measured swatches, source, parent/version, report scope/status, delta-E and visible limitations. Include light/dark/background toggles and small/large preview sizes using CSS only. Provide `render_color_gallery` for T4's `color-gallery` command; it writes a new directory containing `index.html` and byte-identical copies of explicitly listed PNGs referenced by relative paths. Use staging, workspace containment and no-overwrite checks; use a separate path such as `output/color-galleries/demo-r4` so gallery creation does not occupy the normal export destination. Rendering is read-only with respect to session/selection/image contents. Exclude absolute local paths, unselected private references and full prompts from public output by default. Escape untrusted brand names, notes and JSON; embed no external script/font/network dependency.

**References:** `docs/samples/index.html`, `docs/transparency/index.html`, T1 report contract, `delivery.py:guide` for historical/current intent distinctions.

**Acceptance/QA:**
- Happy: render four fixture cards including transparent white artwork and a mismatched restricted palette. Browser toggles preserve image bytes and show distinct intended/measured labels, HEX and warning states at 360px and 1440px widths.
- Edge: a brand name containing `<script>` is displayed as text and never executes; missing/unverified reports cannot render as passed; missing image paths show a named error instead of silently substituting another image. The page opens from a relocated output directory without developer-home paths or external requests.
- Commands: `uv run --locked pytest tests/test_color_gallery.py`; browser inspect the generated fixture page. Use Chrome Computer Use for visual/OS interactions under the existing session authorization; apply applicable UI/debugging skills if a real runtime issue is encountered.
- Evidence: `docs/qa/color-workflow/t7-gallery.md`, desktop/mobile screenshots.

**Parallelization:** after T1; parallel with T2/T3/T6; blocks T4/T8. **Commit:** `feat(color): present palette intent and measured logo colors`.

### T8 — Verify the integrated plugin with real logos and bilingual documentation

**Owner/files:** QA/integration worker; `tests/test_resume_and_portability.py`; root `README.md`/`README.ko.md`; `skills/logo-land/references/project-files.md` and `delivery-checks.md`; `skills/logo-land/assets/brief.example.json`; new `docs/colors/` sample gallery and `docs/qa/color-workflow/`. Coordinate any behavior fix back to its exclusive owner.

**Work:** Add runnable command/JSON examples for all entry points and the combined mode, explain first-use dependency setup versus offline calculation, and test an installed/copy-only skill outside the checkout. Update English/Korean READMEs consistently while keeping top-centered badges and English defaults. Document original-intent versus sampled-measurement truth and the v1 migration/backup/downgrade boundary. Preserve existing samples and create the new gallery at `docs/colors/index.html` from deliberately selected public-safe assets.

Run **eight real native-image cases** using the updated skill, with separate call/artifact IDs and final prompts:

| Case | Prompt intent | Required observation |
|---|---|---|
| 1 | Automatic warm bakery palette | Assistant selects a reasoned palette without redundant approval; actual PNG/report recorded. |
| 2 | Automatic professional technology palette | A distinct appropriate palette and exact requested lettering. |
| 3 | Transparent logo with anchor #247A52 | Exact intent retained; sampled anchor evidence and transparency checked. |
| 4 | Edit case 3 to warmer companions | Anchor, lettering and silhouette remain; real parent and new palette recorded. |
| 5 | Transparent black/ivory, maximum two colors | Restricted report and visual review agree; no invented exact-pixel promise. |
| 6 | Reference-derived palette from a public-safe local image | Reference hash/scope and extraction are real; background dominance is explained. |
| 7 | Reference + anchor + maximum two colors | Combined constraints persist through prompt/import/report. |
| 8 | White-letter transparent variant of a selected logo | White remains visible on dark preview and excluded only when truly transparent; background request remains correct. |

Cases are eight planned outputs, not an instruction to generate every candidate/combination. Repairs follow the two-additional-native-edits-per-request limit. Record failed attempts. A release needs at least one successful anchor output, one successful restricted output and the white-transparent case, plus truthful pass/failure evidence for every attempted case. If the host image tool is unavailable or these essential live cases remain unresolved, preserve work and report the verification gap; do not substitute synthetic logos or publish a fully verified release claim.

**References:** `tests/test_resume_and_portability.py:test_cli_runs_when_only_skill_scripts_are_copied`, `README.md` helper/installation sections, `references/native-image.md`, `docs/qa/live/README.md`, `docs/releases.md`.

**Acceptance/QA:**
- Happy: actual skill execution from a separate workspace produces the selected original PNG, correct report/guide/ZIP and an HTML comparison page. Check light/dark and small-size views, exact English/Hangul text, intended-role placement and edit preservation. Keep real image call evidence separate from synthetic fixtures.
- Edge: run a deterministic strict mismatch, missing engine, unavailable MCP, missing profile/core samples and schema-1 resume in a clean subprocess environment. All failure paths retain prior artifacts; copied scripts use the declared ColorAide version without a checkout import path. Prime the dependency cache explicitly before claiming an offline test.
- Full commands: `uv lock --check`; `uv run --locked pytest`; `uv run --locked ruff check .`; `uv run --locked ruff format --check .`; `uv run --locked basedpyright`. Run the applicable installed `plugin-creator` manifest validator by its actual discovered path. Record outputs, not assumed success.
- Evidence: `docs/qa/color-workflow/README.md` links commands, actual tool calls, image IDs, metric JSON, screenshots, sample licenses/provenance and failures. Open `docs/colors/index.html` in Chrome for the user after visual checks.

**Parallelization:** after T5/T6/T7; final reviews follow. **Commit:** `test(color): verify native logo color workflows and document usage`.

### T9 — Publish the verified v0.4.0 release

**Owner/files:** release owner; `.codex-plugin/plugin.json`, `pyproject.toml`, `uv.lock`, `CHANGELOG.md`, README release badges, `docs/releases.md`, `docs/qa/installation.md` and a release validation record under `docs/qa/color-workflow/`.

**Work:** Follow the existing release guide after all reviewers approve. Recheck remote/main state and whether v0.4.0 already exists. Align clean versions and prepare English notes covering color features, sampled-match limits, v1 migration and actual validation. Update the personal installation with the existing marketplace/cachebuster workflow without placing a cache version in the public manifest. Verify installed behavior, commit/push the integrated work to main, create an annotated tag at the validated commit, and publish its GitHub release. Maintain English About and repository visibility. If a version collision exists, choose the next unused version and update every reference consistently; never retag.

**References:** `docs/releases.md`, `docs/qa/installation.md`, `docs/qa/release-031.md`, the installed `plugin-creator` skill. Read that skill at execution time for its current validation/reinstall commands.

**Acceptance/QA:**
- Happy: locked checks/manifest validation pass on the assembled release commit; remote main, peeled tag and published release target that commit; English notes describe observed image tests accurately; local installed version and clean repo version are recorded separately. The sample HTML still opens in Chrome.
- Edge: an existing published tag is not moved; local cachebuster metadata never leaks into release files. If any required live QA/reviewer check remains unresolved, leave the release unpublished and report the exact gap rather than presenting a partial release as complete.
- Commands: use the existing guide's checks, `git ls-remote origin refs/heads/main refs/tags/v0.4.0 refs/tags/v0.4.0^{}`, and `gh release view v0.4.0 --json tagName,isDraft,isPrerelease,publishedAt,url`. Use the substituted version if a collision required the next unused one. Inspect default branch/About/visibility through read-only repository metadata.
- Evidence: `docs/qa/color-workflow/release.md`, commit/tag IDs and release URL.

**Parallelization:** after T8 and all final reviews; release ownership is exclusive. **Commit:** `chore(release): publish Logo Land 0.4.0`.

## Final verification wave

Run after T8, before release publication. Apply `omo:review-work` through real Orca dispatches: goal/constraint audit, code-quality review, security/integrity review, hands-on QA, and git/context review. All five must approve or their concrete findings must be fixed and rechecked. No reviewer may infer live image success from synthetic fixtures.

- Goal audit: all four entry points plus a combined reference/anchor/count request; original native-image boundary and transparent output retained.
- Quality: strict typed contracts, bounded modules, one math engine, no duplicated truth in original brief versus selected artifact.
- Integrity: v1 migration rollback, stale report/revision handling, path containment, untrusted reference metadata, HTML escaping, original PNG/ZIP bytes.
- Hands-on: read the eight-case evidence, independently open representative originals/refinements, inspect light/dark previews, run a strict mismatch export and a resumed legacy export.
- Context/scope: compare to this plan and actual diff; confirm licenses/attribution, English default metadata, no repo visibility change and no unrequested services.

## Commit and release strategy

The original planning turn produced this plan; implementation was subsequently authorized. Commit the integrated work after its checks, preserving all existing history. Follow `docs/releases.md` for v0.4.0, checking first whether that version exists. Never move a published tag. Revalidate the assembled commit before publishing. Existing session authorization for commit/push/main/release work applies when implementation is requested; a planning request itself does not publish anything.

## Success criteria

- Four entry points work and constraints compose; no mandatory extra approval when selection is delegated.
- Locks remain exact in intent; measurement describes sampled raster fidelity honestly. Strict mismatch/indeterminate exports cannot claim compliance.
- Green → navy → geometry-only edit → reselect-green preserves the correct palette, parent and report for every artifact.
- Intentional white survives reference/analysis handling; hidden transparent RGB is excluded; original files are unchanged.
- A schema-1 project resumes without mutation and can explicitly migrate with rollback; existing background and export regressions pass.
- Native-image and fixture evidence are distinguished; docs and HTML display intended versus measured colors separately.
- The checked release has aligned versions, the validated remote main/tag commit, English release/About metadata, and an unchanged repository visibility.

## Primary references

- Adobe [Leonardo skill](https://github.com/adobe/leonardo/blob/eb6481da40df27654ac8efa42038007f6fad2431/skills/leonardo-colors/SKILL.md) and [MCP tools](https://github.com/adobe/leonardo/blob/eb6481da40df27654ac8efa42038007f6fad2431/packages/mcp/README.md): suggestions/contrast/conversion/interpolation; Apache-2.0. Web-app features must not be assumed to exist in the four-tool MCP.
- [color-expert skill](https://github.com/meodai/skill.color-expert/blob/6514810aaab15cdd0e4202af52a6afed27ed314d/SKILL.md) and [license](https://github.com/meodai/skill.color-expert/blob/6514810aaab15cdd0e4202af52a6afed27ed314d/LICENSE): CC-BY-4.0 guidance; do not copy its third-party reference collection.
- [ColorAide introduction](https://facelessuser.github.io/coloraide/), [harmony API](https://facelessuser.github.io/coloraide/harmonies/), [delta-E API](https://facelessuser.github.io/coloraide/distance/), [8.12.1 package metadata](https://pypi.org/pypi/coloraide/8.12.1/json): Python-native calculation choice. Specify methods rather than relying on defaults.
- [Pantone API](https://www.pantone.com/eu/fr-fr/license/pantone-api): a later licensed integration path, not a bundled public official MCP.
- [W3C contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): logo/brand-name text exception; do not turn contrast guidance into a logo certification claim.
