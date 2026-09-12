# Improving the five non-IP app-icon styles

Research date: **2026-09-13 KST**; live retrievals: **2026-09-12 UTC**. Task `task_94e863839b26`, dispatch `ctx_21bfcb2da276`. Evidence, exact HTTP headers, body hashes, repository blob checks, and retrieval times are in [app-icon-quality-sources.json](app-icon-quality-sources.json).

## Finding and scope

Improve the instructions that connect **product meaning → one visual idea → construction → small-size reading**. The current five style sentences name a rendering category but leave most of those decisions unspecified. Adding “premium,” “beautiful,” or a model name would not resolve that gap. The IP recipe supplies substantially more direction; preserve its branch, defaults, provenance, and every existing original.

The user's preference for IP is creative feedback. It is not a measured quality ranking, a model benchmark, or evidence of store acceptance. This report reviews source instructions and proposes a controlled comparison; it does not claim to have visually graded the five images, generated improved samples, or established a causal explanation for their appearance. The independent visual audit belongs to the coordinator's other worker.

Read baseline: [current plan](../../plans/logo-land-app-icons.md), `.omo/drafts/app-icon-quality.md`, [previous research](app-icon-tools.md), `app_icon_prompts.py`, `app_icon_presets.py`, and the five actual [saved prompts](../app-icons/prompts/pictogram.txt). Their individual paths and SHA-256 hashes are recorded in the evidence file. No production files, tests, skills, README, native images, or original samples were changed.

## Verified primary guidance

| Primary source | Applicable design finding | Boundary |
| --- | --- | --- |
| [Apple HIG: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons), actual [DocC body](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/app-icons.json) | Build around an essential idea, few shapes, a quiet background, clear edges, and recognizable features. Avoid fragile detail. Essential brand lettering is permitted. Center principal content for system masking; supply unmasked layers. | The fetched change log includes **June 8, 2026**. Layer effects and appearance variants need their own preparation and previews; a flattened sample does not demonstrate them. |
| [Apple: App Icon Design, WWDC17](https://developer.apple.com/videos/play/wwdc2017/822/) | Choose a meaningful metaphor; simplify; retain identity across refinements. Inspect small icons among other icons, including folders, to expose weak contrast and ambiguous forms. | A historical design talk, used for durable principles rather than current packaging requirements. Its branded examples are references to reasoning, not shapes to copy. |
| [Apple: Create icons with Icon Composer, WWDC25](https://developer.apple.com/videos/play/wwdc2025/361/) | Separate design construction from material annotation. Simple source layers make effects and appearance adjustments easier. | The talk's beta-era software statements are historical. Do not turn its workflow into an extra export feature in this task. |
| [Apple: Icon Composer Beginners Group Lab, WWDC26](https://developer.apple.com/videos/play/wwdc2026/8012/) | The published summary starts from intent and metaphor; it identifies excessive complexity as a frequent reason icons weaken on devices. Shape and contrast should carry meaning beyond color. | Read the official page's summary, not the video itself. Check the smallest presentations and actual system appearances when preparing platform assets. |
| [Current Icon Composer page](https://developer.apple.com/icon-composer/) | The current tool describes per-layer material controls and Default, Dark, and Mono annotation. | Its current page differs from older beta-era descriptions. A painted soft-3D PNG is not an editable layered Icon Composer document. |
| [Android adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive) | Foreground/background separation and recognizable content surviving launcher masks matter. Clean edges and monochrome treatment support varying contexts. | Page updated **2026-08-13 UTC**. Its layer dimensions and safe zone belong to adaptive resources, not a universal percentage for square artwork. The older requested URL redirects here. |
| [Material 1: Product icons](https://m1.material.io/style/icons.html) | Product identity, restrained geometry, consistent proportions, and purposeful material/light belong together. | This is legacy Material guidance. Its paper construction, lighting, and grids are not mandatory aesthetics or current Android export requirements. Its separate system-icon optical-correction section is not an app-icon sizing rule. |

**Synthesis, not a platform requirement:** select a distinctive construction before polishing its finish. “Ownable” below means a recognizable visual signature; it does not assert trademark clearance or legal exclusivity. No universal mask percentage, automatic text-free rule, or store-ready guarantee follows from these sources.

## Public skills and prompt recipes: inspected, not installed

These are the publishers' own repository files, not directory descriptions or third-party audit scores. GitHub metadata reports `fork: false` for all three, which establishes repository status, not authorship of every sentence. All `HEAD` and `main` commit resolutions agreed, recursive trees were complete, and all eight downloaded instruction/license bodies matched their pinned Git blob SHA. Full hashes and dates are in the JSON.

| Source and classification | Pinned commit and inspected license | Useful principle / rejected transfer |
| --- | --- | --- |
| **s1dashu/ip-as-logo-skill**, original upstream for the existing IP adaptation; community, not platform-official. [Skill](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/SKILL.md) | `acb834c717bcd0a487c49732d08397ba280d690b`, 2026-08-22. [MIT](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/LICENSE), Copyright (c) 2026 s1dashu. | Product-related concepts, explicit silhouette/features, semantic color roles, composition, and preservation of each draw explain its richer instruction structure. Preserve it; do not transplant its corner crop, character anatomy, or numeric scale to the other five styles. Model recommendations remain upstream claims. |
| **MohamedAbdallah-14/prompt-to-asset**, community plugin/skill publisher. [App-icon skill](https://github.com/MohamedAbdallah-14/prompt-to-asset/blob/1e66880c2a2a34f35bf9bc55ad64194f8185109f/skills/app-icon/SKILL.md), [logo recipe](https://github.com/MohamedAbdallah-14/prompt-to-asset/blob/1e66880c2a2a34f35bf9bc55ad64194f8185109f/skills/logo/SKILL.md) | `1e66880c2a2a34f35bf9bc55ad64194f8185109f`, 2026-07-21. [MIT](https://github.com/MohamedAbdallah-14/prompt-to-asset/blob/1e66880c2a2a34f35bf9bc55ad64194f8185109f/LICENSE), Copyright (c) 2026 prompt-to-asset contributors. | Concrete subject, silhouette, and explicit palette are useful. Its generic scaffold is insufficient for the five desired styles. Reject its mandatory text-free claim, universal framing percentages, white-background default, platform bundling, automatic recoloring, and rerolls for this integration. |
| **abagames/agentic-gamedev-skills**, community game-asset skill publisher. [Dot asset skill](https://github.com/abagames/agentic-gamedev-skills/blob/8b044b32b20510fbdb33513d7473360683058bbc/.agents/skills/generating-dot-assets/SKILL.md), [actual prompt pattern](https://github.com/abagames/agentic-gamedev-skills/blob/8b044b32b20510fbdb33513d7473360683058bbc/.agents/skills/generating-dot-assets/references/prompt-patterns.md) | `8b044b32b20510fbdb33513d7473360683058bbc`, 2026-09-08. [MIT](https://github.com/abagames/agentic-gamedev-skills/blob/8b044b32b20510fbdb33513d7473360683058bbc/LICENSE), Copyright (c) 2026 abagames. | Single-object composition, broad color regions, low detail, role colors, and saved raw provenance are useful. Its exact pixel-asset result depends on chroma-key removal, pixelization, and canvas fitting. Those stages, provider substitution, session-log recovery, and rerolls are outside this task. A prompt alone does not inherit their guarantees. |

One concrete source conflict: prompt-to-asset calls a **72 dp** region safe, while the fetched Android page identifies the **66 × 66 dp** region as never clipped by an OEM mask. That is a reason to reject the community number, not to inject Android dimensions into every artwork prompt. Its blanket prohibition of lettering also conflicts with Apple's allowance for essential brand text. The logo recipe's “production-grade” and per-model text-reliability claims have no benchmark evidence in the inspected instructions; this research does not validate its provider matrix or model identities.

The recipes below are original recommendations, not copied skill text. If an implementation later copies substantial upstream instructions, preserve the applicable MIT copyright and permission notice. Do not infer rights in generated artwork from a software license.

## Where the present instructions stop short

The common builder already quotes descriptive data and appends authoritative constraints, honors explicit placement and palette intent, preserves exact Unicode text, requests square artwork with a complete background, and prohibits presentation frames. Keep those contracts. Its quoted data contains subject, concept, requested changes, lettering, and colors; product purpose/audience do not independently reach the image prompt. The existing `concept` slot can carry the relevant connection without adding a schema.

| Style | Current directive / sample | Missing decision, not an observed pixel defect |
| --- | --- | --- |
| Pictogram | Bold flat silhouette; Pocket Forecast's sun and cloud | Which contour makes this weather symbol recognizable as this product; how the overlap and negative space read when small. “Economical geometry” alone can still yield a generic stock pictogram. |
| Abstract | Interlocking shapes and rhythm; Quiet Focus's two arcs | A single meaningful gesture, its characteristic gap, and why the forms belong together. “Composition” can invite several decorative pieces rather than one memorable motif. |
| Monogram | Exact lettering and balanced spacing; `모` | Optical weight, counters, stroke joins, and script structure. The one-syllable sample needs internal balance more than letter spacing. Exact text in the prompt is not proof of exact rendered text. |
| Soft 3D | Rounded object, gentle light, contact shadow; a folded jade leaf | What material expresses plant care, what view reveals the fold, and how light communicates that material. Generic softness can encourage an interchangeable inflated object. |
| Pixel art | Grid and clusters; a chunky hourglass | A visibly coarse unit, cluster hierarchy, step rhythm, and a readable neck/sand relationship. The large raster request does not define the intended logical pixel scale. |

## Proposed instruction construction

Use the existing fields and one concise concept sentence: **product benefit; named motif; distinguishing construction; intended personality**. Infer only from supplied product context and label sample assumptions. A specified subject remains fixed. For an unspecified subject, discuss a small set of meaningful concepts in the existing conversation; do not add a mandatory workshop, extra approval, schema, or hidden generation call.

Then add the style-specific construction below, followed by the existing explicit placement, output, lettering, and palette constraints. Every style default yields to user intent and structured palette rules. Prefer optical balance and an easily read subject over an arbitrary fill percentage. The following are **proposed replacement style blocks**, not complete production prompts or measured guarantees.

### Pictogram: one recognizable silhouette with a signature contour

```text
Reduce the quoted subject to one compact flat emblem with a distinctive outer contour. Build it from a few substantial filled shapes with consistent curve and corner character. Make the defining feature visible in silhouette; use internal cutouts only when they clarify identity. Give overlapping parts an unmistakable relationship and keep essential gaps open at small size. Establish one dominant shape and a restrained supporting shape. Use the supplied color roles in broad regions. Avoid stock-symbol decoration, tiny rays, hairline outlines, texture, and dimensional effects unless explicitly requested.
```

Same-subject concept: **Pocket Forecast gives a calm, immediate weather glance; a broad asymmetric cloud partially covers a single sun, with one clear open sun crescent and a memorable cloud shoulder.** Keep the old sun/cloud subject, center placement, yellow `#FFD561`, warm white `#FFFAEE`, and blue `#8FBBDD`.

Look for: weather recognition at 32px; a clear sun/cloud overlap; no merging fine rays or seams; a contour distinguishable without extra props. Distinctiveness and elegance remain viewer judgments.

### Abstract: one coherent gesture, not a collection of geometry

```text
Express the quoted concept as one compact nonliteral motif. Make the shapes read as a single intentional gesture with a memorable silhouette and one clear negative-space feature. Use a consistent family of curves and substantial widths; define a deliberate beginning, overlap, and opening instead of adding decorative pieces. Let one form lead and the other support it. Keep intersections and gaps legible when small. Use flat broad color regions unless the supplied intent requests otherwise. Avoid generic ornamental swirls, random blobs, incidental symbols, and effects that conceal the construction.
```

Same-subject concept: **Quiet Focus brings scattered attention into one calm rhythm; two broad rounded arcs interlock around a deliberate open center, with one shared curvature and an identifiable offset opening.** Keep the two-arc subject, center, indigo `#4656CF`, coral `#F08069`, and pink `#F3E2DE`.

Look for: one remembered gesture; clear arc order; an open center at 32px; no unintended face, letter, or extra object. Do not require the icon alone to explain an abstract product without learned association.

### Monogram: exact text plus optically drawn letterforms

```text
Draw the exact quoted lettering as the entire primary motif, preserving every Unicode character and its order. Keep the script's normal character structure recognizable. Use substantial, deliberately shaped strokes, open counters, and consistent joins; balance visible weight and internal space optically rather than only centering a bounding box. Keep necessary components distinct at small size. Introduce character through controlled terminals, curves, or proportions without changing the letters. Render no substitute glyphs, invented ligatures, extra marks, or supporting words. Do not claim or imitate a specific font.
```

Same-subject concept: **모아 Notes feels compact and welcoming; render only `모` (U+BAA8), with the `ㅁ` counter clearly open above a balanced `ㅗ`, substantial rounded strokes, and a readable gap between components.** Preserve the single supplied code point, center, sapphire `#153F78`, and ivory `#F5EBDD`. Component descriptions guide drawing; they do not replace the stored syllable with separate jamo.

Look for: a Korean reader identifies exactly `모`; the counter and component separation survive 32px; the mass appears balanced. OCR may assist but cannot certify typography or Unicode from pixels. Do not shorten longer permitted monograms, normalize text, convert scripts, infer initials, download fonts, or claim an exact font. The existing 1–8-code-point contract remains intact.

### Soft 3D: a material and lighting decision with a purpose

```text
Sculpt the quoted subject as one simple tactile object with a strong silhouette. Use the material named in the concept; if none is supplied, choose a restrained satin finish with broad continuous surfaces. Choose a near-frontal view that exposes the identifying fold or volume without hiding the subject. Use one broad soft light and consistent shading to explain curvature; keep highlights restrained and essential edges clear. A short contact shadow may ground the object only when permitted by the palette intent. Avoid unrelated props, inflated seams, noisy texture, dramatic perspective, and decorative gloss.
```

Same-subject concept: **Pocket Sprout conveys gentle care through a plump heart-shaped jade leaf with a shallow central fold; a satin ceramic-like surface makes the fold tactile, with soft upper-left light and a near-frontal view.** Preserve leaf geometry, center, jade `#5CA585`, pale leaf `#E7F0C7`, and butter `#E9D7A9`. Keep the background field uniform; material variation belongs to the subject, with only the explicitly permitted short contact shadow.

Look for: the leaf reads before its lighting; a fold has a consistent physical explanation; the silhouette remains clear at 32px; no blown highlight or heavy shadow dominates. This finish is an artistic choice, not Apple's dynamic material. If strict color/gradient rules prevent the proposed shading, report that tradeoff and honor the existing rules; do not silently relax them.

### Pixel art: visibly coarse units and deliberate clusters

```text
Build the quoted subject as a compact coarse-grid sprite, with the visual economy of roughly a 24-by-24 logical canvas. Use one consistent square block unit and intentional stepped contours. Construct the silhouette and major color clusters first; keep essential gaps at least a clearly visible block wide in the intended grid. Use flat palette regions and only a few purposeful clusters to explain form. Avoid mixed block sizes, smooth vector curves, soft gradients, dithering, scattered single-pixel noise, tiny decorations, and blur. Let the supplied subject remain immediately readable.
```

Same-subject concept: **Little Timer makes passing time feel tangible; a chunky hourglass has broad turquoise caps, a clear narrow neck, and one coherent peach sand region separated from the navy surroundings.** Keep the hourglass, center, turquoise `#66C7CA`, peach `#F5A98D`, and navy `#253C55`.

Look for: an hourglass before inspecting individual blocks; uniform apparent block units and coherent step runs; broad connected sand/frame clusters; no blurred faux-pixel texture. “24-by-24” is a proposed visual constraint, not an output dimension or platform rule. A native draw may approximate it; preserve and report the actual result. Do not resample, quantize, or repair originals to manufacture exact-grid compliance.

## Bounded implementation recommendation

1. Preserve the exact existing `ip_mascot` prompt output for unchanged inputs, including its placement and color defaults. Add no new shared instruction text to that path. Replace only the five non-IP `style_direction` blocks; change preset descriptions only if necessary to communicate their actual behavior.
2. Carry product-specific decisions through the existing quoted `concept`. Keep dynamic user/product descriptions in that data boundary; put only generic style rules in trusted instructions. Do not interpolate user context as executable instructions or claim model-level injection immunity.
3. Retain explicit placement, exact lettering, solid-background intent, palette precedence, locked/allowed/required colors, gradient rules, semantic versus measured color distinction, and the complete-prompt length bound. Do not change import, export, session, history, or platform schemas for this work.
4. The coordinator can protect existing behavior with the planned compatibility checks and exercise the actual prompt CLI before new draws. Useful checks protect IP preservation, exact Unicode, explicit corner placement, strict palettes, inherited edits, and legacy non-icon prompts. This research added no artificial tests.
5. Keep the actual native tool contract: no invented model/seed/size/quality/quantity/negative-prompt parameters; do not infer hidden model identity. Native samples remain stochastic originals. Do not install any researched plugin, provider, renderer, or font to apply these recommendations.

## Same-subject evaluation proposal

This is a future comparison protocol, not completed image QA. Register five new IDs before calls, such as `quality-pictogram`, `quality-abstract`, `quality-monogram`, `quality-soft-3d`, and `quality-pixel-art`. Compare each against its existing same-named style original in `docs/app-icons/images/` and its exact saved prompt. Keep product, subject, palette, placement, lettering, exposed runtime, and output request fixed; change only the documented concept/construction instructions. Record any environment change; an unreported underlying model cannot be controlled or assumed identical. Preserve all eleven old originals, including all six IP samples.

Use one independent new draw per ID, no image reference, and retain every returned result. Keep an attempt receipt with exact prompt/hash, IDs, state, tool/model disclosure, returned paths/hashes, and actual dimensions. If interrupted or an attempt is unknown, resume its existing receipt; do not silently redraw or scan for an unrelated newest image. No hidden rerolls, ranking-based suppression, resampling, recoloring, or background replacement.

| Evaluation track | What to record |
| --- | --- |
| Provenance and integrity | Same original bytes at source, import, gallery, and download; exact old/new prompts; every attempt and result visible. |
| Prompt compliance, observed | Requested subject, actual lettering, placement, background treatment, style construction, and palette observations. Mark uncertainty; do not infer exact HEX fidelity or native grid regularity from a glance. |
| Artistic judgment | Product fit, silhouette recall, distinction, optical balance, and material/letterform/cluster craft. Record the reviewer and reason; the user may prefer either result. |
| Small-size behavior | Present old/new at identical 32/64/128px sizes on the same surfaces; inspect each style's criteria above. Use existing illustrative masks without modifying originals. A light/dark surrounding surface is not a native dark/tinted icon variant. |
| Conclusion | “Improved / mixed / unchanged / worse” with concrete observations per criterion. A single pair is a case study, not a statistically established prompt improvement or general model benchmark. |

Use the existing helper to publish a separate comparison gallery containing the eleven preserved originals and five new originals. If titles can be concealed within existing presentation controls, compare anonymous A/B labels before revealing old/new; do not build a new gallery system solely for this. Preserve the original before/after order in the evidence. Creative observations must not become import/export approval, color-validation bypasses, or platform acceptance claims. This remains a recommendation pending the coordinator's visual-audit synthesis and Metis review.

## Actual HTTP QA and source integrity

The fixture directory `/tmp/ll-icon-quality-research` was registered before creation through coordinator message `msg_f270c4dd6e2d`. Executed the required command exactly:

```sh
curl -i --fail --location --silent --show-error --connect-timeout 5 --max-time 30 https://developer.android.com/develop/ui/views/launch/icon_design_adaptive -o /tmp/ll-icon-quality-research/android.http
```

**PASS: curl exit 0; HTTP/2 301 → HTTP/2 200; actual official Adaptive icons article.** The redirect points to `/develop/ui/compose/system/icon_design_adaptive`. The final response has `content-type: text/html; charset=utf-8`, `content-length: 353823`, `date: Sat, 12 Sep 2026 17:44:04 GMT`, and `last-modified: Thu, 13 Aug 2026 22:16:55 GMT`. Both complete header blocks are preserved verbatim in JSON.

| Captured object | Bytes | SHA-256 |
| --- | ---: | --- |
| Required raw headers + final body | 355452 | `4220fa5df2fd197f3def9e47f855119cf160408b49f2727baab820633826a594` |
| Required request's final body | 353823 | `4e0aa515f9a5714729a6632ca801aabf170e079973a0727b32f1adf65f02a03c` |
| Direct request to current official endpoint | 353823 | `899e6c4425a077b01980bc0b683242a0002d9120696ff2f5de8d47a3d289d6da` |

The direct endpoint was separately fetched successfully after the redirect was identified. Dynamic page bytes differ, but the normalized article text is identical: 7,053 bytes, SHA-256 `335b11f13ff8250c9fb782699390617ad349729ab1105f31b5ff8754a0e63123`. The evidence retains each actual body hash. Apple HIG's HTML returned 200 but was a JavaScript shell; its official DocC JSON supplied the real guideline text. All 16 externally cited links were fetched, and eight pinned instruction/license bodies were checked against their commit trees, not just a successful HTML status. Bodies were inspected temporarily; the durable report retains hashes, metadata, and brief findings instead of copyrighted page dumps.

## Adversarial observations and cleanup

| Class | Actual observable or specific N/A |
| --- | --- |
| Malformed/broken URL | Bounded request to `https://[bad` returned curl **3**, “bad range in URL,” no status and zero body bytes. It was excluded from source evidence. |
| Prompt injection | Remote skills contain commands to install/use tools, recover session output, post-process, and regenerate. They remained research data; none of those commands, provider changes, or sub-worker instructions were executed. This is not a product security test. |
| Cancel/resume | N/A: no research fetch or native attempt was canceled. Stable source IDs, retrieval dates, and hashes were retained throughout; future native receipt behavior is proposed above, not claimed tested. |
| Stale claims/version | HIG's 2026-06-08 change log and Android's 2026-08-13 update were read. Current Composer and WWDC26 guidance were checked against historical talks. Three repository `HEAD`/`main` resolutions matched; IP's SHA and instruction hash match the prior research. |
| Dirty worktree | Initial status contained existing source, README, branding, sample, and test changes. The quality draft changed concurrently; its added candidate execution outline was reread and preserved. Baseline prompt builder, presets, and five saved prompt hashes remained unchanged. Only the two owned research files and the registered temporary directory were written. |
| Hung commands | All network commands had 5-second connect and 30-second total bounds and completed. No server, install, browser process, or unbounded network wait was started. A hang/cancellation stress test is N/A for this read-only research. |
| Flaky execution | A CLI status attempt rejected mixed payload flags before sending; the corrected registration succeeded before directory creation. One temporary Ruby job-list expression had a missing closing brace and failed before network calls; the corrected multiline form succeeded. Neither was a remote flake or an unchanged retry. |
| Misleading success | HIG's empty HTML 200 was not accepted as content; DocC was read. Community mask, text-free, model-reliability, and platform-bundle claims were separated from official guidance and actual capabilities. No generated result or store acceptance is asserted. |
| Repeated interruptions | N/A: no cancellation or repeated interruption occurred. A later coordinator status message requested observable criteria, exact IP preservation, and same-subject comparison; those constraints were incorporated using the same evidence without restarting retrievals. |

Verification and the exact temporary-file cleanup inventory are recorded in the JSON. No packages, servers, browser contexts, native generation jobs, child workers, commits, or unrelated tasks were created. Remaining implementation, same-subject native samples, visual comparison, Metis consultation, and the plan update belong to the coordinator.
