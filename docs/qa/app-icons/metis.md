# App icon intent: Metis gap review

Date: 2026-09-13 KST. **Verdict: ready to plan and implement with the decisions below.** This is a documentation-only pre-planning review, not implementation acceptance or native sample acceptance. The user already authorized planning, implementation and sample generation; no additional approval is required for those steps.

## Highest-priority gaps

1. **Icon intent must change the prompt branch, not append another style sentence.** [prompts.py:57](../../../skills/logo-land/scripts/logo_helper/prompts.py) currently requests the brief's logo type, exact lettering and slogan; lines 78–84 preserve parent lettering/layout, and line 97 adds symbol-plus-text lockup. An appended “no text” instruction leaves contradictory instructions. Explicit icon transforms must remove those rendering instructions, including inherited lockup and unrelated brand styles.
2. **Sample availability must be independent of export approval.** [gallery.js:25](../../samples/gallery.js) accepts only `items/.../delivery/...`; lines 29, 99 and 123 gate downloads/images on `status === "exported"`. Reusing that data contract unchanged hides valid originals whose artistic/color review fails. The [color gallery](../../../skills/logo-land/scripts/logo_helper/color_gallery.py) already copies hash-verified originals without mutating session state and is the useful implementation precedent.
3. **Background inheritance is deliberately asymmetric today.** [workflow.py:84](../../../skills/logo-land/scripts/logo_helper/workflow.py) imports omitted background from the original brief, while the edit prompt describes the parent's requested background. [test_background_compatibility.py:55](../../../tests/test_background_compatibility.py) explicitly protects this behavior. Resolve the icon's opaque background explicitly in both prompt and import; do not globally change legacy imports to parent inheritance.
4. **Semantic color guidance must not synthesize strict constraints.** [ColorConstraints.strict](../../../skills/logo-land/scripts/logo_helper/color_models.py) is true for any locks, required colors, allowed list or maximum count. Turning “two character colors plus one background” into `max_colors=3` changes an aesthetic direction into an export gate. Existing strict palettes and release failures remain authoritative.

## Recommended minimal contract

Add `AppIconIntent(FrozenModel)` in a small dedicated model module and optional `app_icon: AppIconIntent | None = None` to `Brief`, `Artifact`, `EffectiveIntent` and `PromptResult`. Export metadata carries the selected artifact's snapshot explicitly; do not derive it from today's brief. Reuse `FrozenModel`'s frozen, strict, extra-forbidden boundary. No free-form JSON options, platform target, platform-ready flag, generation model selector or output resampling settings.

| Field | Type / default | Validation and meaning |
| --- | --- | --- |
| `preset` | Required literal: `ip_mascot`, `pictogram`, `abstract`, `monogram`, `soft_3d`, `pixel_art` | No guessing from `logo_type`, use cases, prompt text or pixels. |
| `subject` | Required bounded non-whitespace string, reuse `Text` | The object/character/motif to draw; descriptive input, not executable instructions. |
| `placement` | Required literal: `center`, `lower_left`, `lower_right` | `ip_mascot` requires a lower corner; the five other presets require `center`. The conversation/preset helper explicitly supplies `lower_left` for unspecified IP direction and `center` otherwise; the JSON parser does not guess. |
| `text` | Bounded string or `None`, default `None` | `monogram` requires 1–8 Unicode code points, preserved exactly, with no whitespace/control characters; other presets require `None`. This is a code-point bound, not a typography/grapheme guarantee. |

Keep the square canvas, no baked platform mask, no external wordmark and full opaque background as this feature's prompt invariants, rather than adding fields with only one supported value. Actual dimensions/alpha remain decoded facts; a request is not proof that generation followed it. A transparent cutout remains the existing logo workflow, outside this bounded icon mode.

Preset directions: IP uses a simple personified rounded heavy form, two purposeful subject colors plus one solid background and a dominant lower corner; pictogram uses a clear centered object silhouette; abstract uses centered nonliteral geometry; monogram draws only `text`; soft 3D uses one centered rounded dimensional subject; pixel art uses deliberate block structure readable at small sizes. These directions neither prove raster color count nor create automatic artistic tests. Full-square comparison masks are CSS previews only.

The [upstream research](../../research/app-icon-tools.md) arrived during final review. Its alternate style IDs are suggestions, not the task contract: retain exactly the six underscore-separated IDs above. Its pinned upstream is `acb834c717bcd0a487c49732d08397ba280d690b`; retain the complete MIT notice and adaptation provenance with copied/substantially adapted guidance. The research worker reports installed/pinned source equality; this reviewer did not repeat those network probes.

For `ip_mascot`, use the upstream square **image** prompt vocabulary: no “logo”, “brand mark”, “app icon” or “icon asset” framing, and describe a solid background without “alpha”, “transparency” or “opaque” prompt tokens. Typed metadata may still use `app_icon` and `opaque`. Remove generic safe-margin/centered-mark instructions from this branch; the large lower-corner subject is intentional. The other five presets do not inherit IP-only corner/color rules. Native tool identity stays truthful even if the upstream expresses a model preference that the exposed tool cannot select or report. Corner masking may crop important features; show that preview honestly and preserve the draw rather than promise platform fitness.

### New briefs and explicit transforms

- A new brief containing `app_icon` must have `background="opaque"`, empty `slogan`, and `lockup=None`. For non-monogram icons `exact_text` must be exactly `""`; for monograms it must exactly equal `app_icon.text`. Reject contradictions at initialization, preserving explicitly supplied text rather than quietly dropping it. `brand_name`, industry and audience remain context. `logo_type` remains a legacy field and does not select rendering in icon mode.
- Add the same `--app-icon-file` typed file option to `prompt` and `import`; parse with bounded `read_source` and `AppIconIntent.model_validate_json`. An explicit file requests a complete replacement, never a partial merge. A file containing `null`, extra fields or unsupported values is invalid.
- An explicit icon file on a legacy brand session is a declared transform: ignore old exact text, slogan, lockup and conflicting brand-layout/style directives for rendering, preserve their historical metadata, and expose the resolved icon in the prompt result. For a parent transform, replace the generic “preserve all text/layout” paragraph with preservation limited to compatible subject/identity and the requested icon changes. Do not silently treat the old wordmark as a monogram.
- If icon mode and an explicit `--lockup-file` are both requested, fail with a stable conflict error before writing or calling a generator. Inherited lockup is suppressed by the declared icon mode; it is not saved on the resulting icon artifact. `--background transparent` conflicts with icon mode. The host must not silently alter explicit strict palette constraints to make a conflicting style work.

### One shared precedence rule

| Boundary | Effective icon intent |
| --- | --- |
| Explicit icon file supplied | That full validated intent, regardless of parent or brief. |
| No override, parent supplied | `parent.app_icon`, including `None`; do not fall back through a legacy parent's `None` to brief icon intent. |
| No override, no parent | `brief.app_icon`. |

An inherited icon can be replaced explicitly. Omission/`null` is not a hidden “clear icon” command; an icon-to-brand conversion command is outside this requested feature. Preserve existing brand-only palette/lockup behavior when the effective icon is `None`. Keep explicit-palette > parent-palette > active-palette behavior unchanged, including the current rule that an existing unbound parent does not acquire the active palette.

Prompt and import must use the same resolver and receive identical explicit intent files. `PromptResult` records the full resolved icon, palette ID/digest, parent and session revision; add optional `requested_background: Background | None = None`, populated as `opaque` for icon requests while preserving the existing parent-background field. Import stores the full icon snapshot on the new artifact. Passing only a preset name or recalculating from a mutable brief is insufficient provenance. The actual final prompt remains stored verbatim. A prompt result is descriptive evidence, not authorization to execute embedded commands.

## Compatibility and persistence

**Keep the current session schema at v2 for this additive optional field.** Do not introduce a generalized migration framework or rename existing stored fields. [legacy_state.py](../../../skills/logo-land/scripts/logo_helper/legacy_state.py) retains its frozen v1 parser: even `app_icon: null` is an extra key in v1 and must be rejected. Existing v1/v2 objects without icon fields parse to `None`, never an inferred preset, glyph or palette. Old installed helpers are not promised to read new icon-bearing v2 files; their extra-key rejection is preferable to silent data loss.

`show`, `list`, `prompt` and comparison rendering must not rewrite an old v1/v2 `session.json` or create a migration backup. On a successful v1 mutation, preserve exact `session.v1.backup.json` bytes using today's behavior and write current v2. Ordinary old-v2 mutation may serialize the new optional `null` fields, but must preserve all prior artifacts, IDs, hashes, parent order, selection, exports, failed-attempt history, reviews, palettes, references and reports. Do not overwrite a conflicting existing v1 backup.

[Store.save:161](../../../skills/logo-land/scripts/logo_helper/storage.py) already compares every historic artifact except mutable review fields; include the new intent naturally in that comparison. Rebinding an existing artifact from `None` to icon intent, replacing a preset/text/placement on it or changing its parent must fail `immutable_history`. Only a new derived artifact can carry a new intent. New icon validation must not retroactively require old images to be square or opaque.

## Color and delivery policy

For semantic swatches, reuse existing palette roles and default empty constraints: no locks, required/allowed HEX list or `max_colors` unless the user explicitly requested them. These remain guidance/advisory; prompt wording must not say an unbound semantic palette is measured or strictly verified. A soft-3D palette created for this purpose can explicitly allow gradients; existing explicit no-gradient intent remains unchanged, with dimensional shading constrained accordingly. Pictogram/IP/pixel-art directions should still discourage gradients as style guidance.

An explicit strict palette stays attached through icon conversion and edits, with the same digest and constraints. Preset choice does not switch `strict` off, invent an ROI, relax alpha/coverage thresholds, remove required colors or hide a background from full-image measurements. If strict allowed colors cannot support the suggested IP colors, adapt the semantic colors within that palette rather than expand the allowed set. Hard contradictions must be returned before generation; an aesthetic preference is not a contradiction requiring a new user approval gate.

Deliver every valid original as a creative sample, even if it has unexpected text, alpha, dimensions, color mismatch or an unfavorable visual assessment. Preserve tool outputs that cannot be imported too, with a truthful failed/import-limited record; do not call them validated PNG artifacts. No auto-reroll, selection-based deletion, contact-sheet slicing, pixel repair, resizing, alpha replacement or palette quantization. A failed/missing image cannot count as one of the 11 required originals.

Original downloads are independent of `selected_id`, `review.passed`, color status and export records. Keep raw SHA-256, actual pixel dimensions, prompt, native provider/tool and model identity (`unreported` if unavailable) next to sample provenance; provider/tool truth does not require API credentials. Review/measurement fields stay unset until actually performed. A separate optional approved export uses existing [delivery.export](../../../skills/logo-land/scripts/logo_helper/delivery.py) and [export_colors](../../../skills/logo-land/scripts/logo_helper/color_delivery.py) with all current selection, visual review, background, fresh color evidence, integrity, path and atomicity gates intact.

Use a new project-local icon sample collection without changing historical sample statuses. Reuse safe original-copy and HTML-escaping patterns; use DOM `textContent` for dynamic text and allow-listed relative download paths. Provide square/rounded/circular CSS previews and 32/64/128 CSS-pixel comparisons without modifying downloads. Labels state “PNG artwork / preview”; never infer Android adaptive layers, Apple layered assets, platform approval, app-store readiness, vector editability or licensed fonts from one raster or a passing helper command.

## Native sample execution and interrupted attempts

Define all 11 candidate IDs before the first call: three distinct IP subjects × (`lower_left`, `lower_right`) = six independent draws, plus one draw each for pictogram, abstract, monogram, soft 3D and pixel art. Each is a new native generation with no parent/reference to a previous candidate and one call per candidate. Keep every returned draw if a call produces more than one; record its actual candidate/call association. User taste must not become a PASS prerequisite or a reason to repeat a finished candidate.

Use a small durable sample attempt ledger owned by the implementation/sample task, not new orchestration infrastructure in `AppIconIntent`. Minimum per call: candidate ID, logical attempt ID, exact prompt hash/path, resolved intent/palette binding, starting session revision, tool/provider, start time, returned call identity when exposed, outcome (`planned`, `running`, `returned`, `failed`, `cancelled`, `unknown`), and every returned original path/hash. Model identity may be unreported. Artifact lineage and workflow `FailedAttempt` alone do not identify a native call: [artifact_models.py:75](../../../skills/logo-land/scripts/logo_helper/artifact_models.py) has no durable attempt ID.

Before continuing after interruption, reconcile that same candidate/attempt and its exact tool receipt. An unknown/running call is not permission for another draw. If original bytes already exist and import was interrupted, resume validation/import from that exact receipt; never scan for the newest generated file. If a session revision changed, retain the returned original and reconcile current state before importing; do not rerun generation to resolve `stale_revision`. Duplicate imports must preserve old bytes. A late return after cancellation is retained and labeled as such, never silently selected or promoted to a new attempt. Explicit stop cancels future calls, with available outputs and unmet coverage reported truthfully.

Timeouts, failed calls and interrupted calls do not become artistic reroll budgets. Repeated continuation messages retain the same logical attempt identities; infrastructure recovery must first establish that no call is active and document any authorized retry. Keep this new icon candidate set separate from earlier color requests.

## Baseline and implementer tests

The following existing tests were read/mapped, **not executed by this worker**. No RED test is appropriate for this documentation-only review. Implementers should first run the relevant existing tests and add failing cases for the new boundaries before editing production:

| Existing baseline | Proposed new Given / When / Then case |
| --- | --- |
| [test_boundaries.py](../../../tests/test_boundaries.py), [test_color_models.py](../../../tests/test_color_models.py) | Given each of six presets, when JSON enters init/prompt/import, then valid intent round-trips and malformed types, extra keys, whitespace subject, invalid placements, missing/illegal monogram text, mismatched exact text, slogan, explicit lockup and transparent icon requests fail without mutation. |
| [test_palette_compatibility.py](../../../tests/test_palette_compatibility.py) | Given byte snapshots of real v1 and pre-icon v2 states, when each read command and first mutation runs, then reads remain byte-identical, v1 backup remains exact, lineage/color/export history survives, absent intent stays `None`, strict version types and v1 extra-key rejection remain enforced. Test failed-save and conflicting-backup cases. |
| [test_palette_workflow.py](../../../tests/test_palette_workflow.py) | Given parent intent differing from the brief, when prompt and import omit/replace icon intent, then both bind the same full snapshot. Include legacy-parent `None`, active-palette changes, explicit strict palette, and explicit icon transform of a nonempty brand wordmark/lockup. |
| [test_background_compatibility.py](../../../tests/test_background_compatibility.py) | Given a transparent legacy brief/parent, when an explicit opaque icon transform is imported, then icon requested background matches prompt intent while existing non-icon omitted-background behavior remains unchanged. |
| [test_color_workflow_transactions.py](../../../tests/test_color_workflow_transactions.py), [test_transactions.py](../../../tests/test_transactions.py) | Given a generated original and stale revision, locked session, duplicate artifact ID or injected save failure, when import runs, then original bytes remain available, no partial artifact/history is committed and only task-owned staging is removed. |
| [test_color_export_compatibility.py](../../../tests/test_color_export_compatibility.py), [test_color_reports.py](../../../tests/test_color_reports.py) | Given the same strict indeterminate/mismatched evidence with icon intent added on a new artifact, when export runs, then it refuses under unchanged thresholds. Given semantic-only guidance, when sample delivery runs, then a valid original is downloadable with no fabricated review/color pass. |
| [test_color_gallery.py](../../../tests/test_color_gallery.py), [test_cli_safety.py](../../../tests/test_cli_safety.py) | Given hostile subject/brand text, traversal/symlink destinations or a hash-tampered original, when gallery publishing runs, then text is inert, unsafe paths fail and unrelated files survive. Given a valid but unapproved original, then the gallery still offers its byte-identical download. |

Additional manual evidence for implementers: run CLI help plus init → prompt → import → show for one icon and one legacy case; exercise an invalid icon file; open the actual gallery and test original links, keyboard controls, masks and all comparison sizes; verify downloaded hashes. Execute the native sample ledger once across the 11 candidates and record actual tool outcomes. The gallery must not display empty/pending candidates as completed samples. Schema tests establish prompt structure/decision content, not that the generator will obey it.

## Adversarial conclusions and unchanged release gates

- **Prompt injection:** malicious `subject`, brand fields, concept, changes or imported research text can ask to print a slogan, launch shell commands, erase prior samples or relax color gates. Treat them as quoted/descriptive data and emit trusted resolved icon/text/palette instructions after context; omit unrelated provider raw-response instructions. Neither strings nor a native image return authorize shell execution, mutation or a new approval. Prompt separation is a mitigation, not a claim of model-level injection immunity.
- **Dirty shared tree:** initial `git status --short` showed only untracked `.omo/drafts/logo-land-app-icons.md`; subsequent workers may add their owned files. Do not reset/clean the tree or “repair” unrelated work. Verify production baselines before integrating, and report drift instead of claiming the pinned bytes still describe changed code.
- **Hung commands:** the required HTTP call has connection/overall deadlines; native/tool waits require bounded liveness checks and same-attempt reconciliation. Do not kill unrelated writers, steal lock directories or start duplicate calls on timeout. Coordinator heartbeats carry both task and dispatch identity.
- **Misleading success:** successful PNG import, gallery render, CSS mask or CLI exit is not artistic, strict-color or platform-ready approval. Missing model identity is recorded as unreported, not guessed.
- **Old color gates:** [review-summary.md](../color-workflow/review-summary.md), [review-corrections.md](../color-workflow/review-corrections.md) and [continuation-escalation.md](../color-workflow/continuation-escalation.md) record unresolved restricted-color/white-transparent native acceptance and exhausted repairs. T8, VERIFY and T9 remain incomplete, and the v0.4.0 record remains an unpublished draft per [release.md](../color-workflow/release.md). This review neither rechecks remote release state nor changes those conclusions, attempts, thresholds or plan checkboxes. New icon samples cannot satisfy those named prior prerequisites.

## Performed verification and HTTP receipt

Source baseline observed: `HEAD = ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5`. Read the brief, artifact, session, legacy parser, prompt, intent, workflow, storage, CLI, palette/lockup, delivery/export and gallery implementations plus the linked tests and historical color gate reports. Initially the parallel research/code-map files were absent; during final review `docs/research/app-icon-tools.md` and `docs/research/app-icon-sources.json` appeared, so the full research report and the manifest's upstream/provenance fields were inspected and incorporated above. `docs/qa/app-icons/code-map.md` remained absent at that check; no waiting or speculative citation was needed. Incorporated coordinator message `msg_0f81ea105e6c` requiring a small explicit integration, native provider/tool truth and unconditional original sample delivery. The concurrent research files and `plans/logo-land-app-icons.md` were left untouched.

Executed the required live HTTP probe, adding only an output receipt path:

```sh
curl -i --fail --silent --show-error --connect-timeout 10 --max-time 30 https://raw.githubusercontent.com/t1seo/logo-land/ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5/skills/logo-land/scripts/logo_helper/brief_models.py -o /tmp/logo-land-icons-metis-task_3d4c91ed85ef.http
```

Compared the raw response body byte-for-byte with the local source using binary reads; also calculated SHA-256 independently on both buffers. **PASS: HTTP/2 200; curl exit 0; exact byte equality; both bodies 840 bytes.**

| Receipt field | Observed value |
| --- | --- |
| HTTP Date | `Sat, 12 Sep 2026 16:47:48 GMT` |
| Content-Type / Content-Length | `text/plain; charset=utf-8` / `840` |
| GitHub request ID | `3A72:10B26E:92CA6:2E2C99:6AA58234` |
| Remote body SHA-256 | `cf3467616aeb0264fdf7931d1f203a980205acaf802f3461601865a0b063227e` |
| Local source SHA-256 | `cf3467616aeb0264fdf7931d1f203a980205acaf802f3461601865a0b063227e` |
| Full raw HTTP receipt SHA-256 | `bcaebfe8a927d35346256808868875811db469657faf88e55f7b5f92855f6bb5` |

This HTTP/file comparison and source/report inspection were performed; malformed-input, cancellation, gallery, native generation and export cases above are proposed implementation verification, not probes performed by this worker. No production edits, automated tests, native generation, browser/server launches or release mutations occurred.

## Resource register

- Task: `task_3d4c91ed85ef`; dispatch: `ctx_09566314e6b6`.
- Owned deliverable: `docs/qa/app-icons/metis.md` only.
- Registered before creation: `/tmp/logo-land-icons-metis-task_3d4c91ed85ef.http`, a bounded raw HTTP receipt for the required pinned-source comparison. Status, hashes and byte equality are recorded above; the receipt was removed and `test ! -e` exited 0.
- No native image calls, server, child workers, browser, or Boulder mutations are authorized for this review.
- Final document verification: all 27 relative links resolve; no trailing whitespace; no tracked production diff; local pinned-source hash remains unchanged. Other workers' untracked draft, plan and research files remain intact. No task-only temporary resource remains.

## Work sequence

1. Read draft and current contracts: complete.
2. Check pinned HTTP baseline and map compatibility/edge-test gaps: complete.
3. Finalize decisions, verify report references and remove the registered receipt: complete.
