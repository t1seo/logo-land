# App icon quality audit

Independent Q1 audit, 2026-09-13 KST. Owner: `task_928e07bfd869`, dispatch `ctx_85f521656059`. Scope: five existing non-IP originals, one IP reference, their exact prompts, existing Chrome evidence, relevant source/tests, and bounded local HTTP verification. Source baseline HEAD: `ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5`; the shared worktree already contained substantial modified/untracked icon and branding work, so HEAD alone does not identify the audited implementation.

**Finding:** The examples establish recognizable subjects and functioning provenance, but several subjects remain generic category symbols. Monogram needs stronger optical presence and authored lettering; Soft 3D needs controlled material; Pixel art needs a more coherent coarse grid and simpler sand topology. Abstract already uses the canvas boldly, so indiscriminately enlarging every style would be counterproductive. These are visual judgments about these particular samples, not measured beauty scores or proof that any style is inherently weaker.

**Verified:** All eleven gallery originals match the actual native files, local originals, source imports and catalog artifacts; all eleven exact prompts reconstruct byte-for-byte from the current helper and their saved source briefs. The actual public CLI returns six prescribed IDs. Targeted existing tests: **34 passed in 30.78s**. Monogram HTTP: **200, original body SHA-256 equal**. No native generation, browser interaction, image editing, source/test edit, child worker or commit occurred.

Read requirements in [.omo draft](../../../.omo/drafts/app-icon-quality.md) and the active [plan, Q1](../../../plans/logo-land-app-icons.md). The coordinator owns contract changes and implementation. The user's preference for IP is preserved as creative feedback; this audit neither approves exports nor certifies product/store readiness.

## Evidence and viewing limits

All six PNGs below were opened directly using `view_image`; these are **native-original observations**, not newly resampled assets. File dimensions were verified through the immutable manifest as 1254 × 1254. Texture/contour observations refer to these original views; no pixel counts, occupancy percentages, contrast ratios or exact grid measurements were invented.

Existing, untouched Chrome screenshots were independently opened using `view_image`:

| Evidence | What it supports |
|---|---|
| [128 middle](chrome/08-square-128-middle.jpg), [128 bottom](chrome/09-square-128-bottom.jpg) | Pictogram/abstract/monogram and Soft 3D/pixel display comparisons |
| [32 middle](chrome/12-square-32-middle.jpg), [32 bottom](chrome/13-square-32-bottom.jpg) | Small-preview recognition and loss of fine detail |
| [64 dark middle](chrome/16-square-64-dark-middle.jpg), [64 dark bottom](chrome/17-square-64-dark-bottom.jpg) | Legibility against dark preview surroundings; opaque artwork backgrounds persist |
| [128 abstract filter](chrome/21-filter-abstract.jpg) | Abstract center without the pointer overlay in the middle-row captures |
| [32 IP](chrome/11-square-32-ip.jpg) | Reference owl face/book color masses survive reduction |
| [Exact Korean prompt](chrome/29-exact-korean-prompt-file.jpg) | Existing Chrome display of the UTF-8 prompt and exact `모` |

The size labels mean gallery CSS display settings, not verified physical-device pixels. JPEG/viewer scaling limits detailed pixel judgments. The pointer highlight overlaps abstract's center in the middle-row 32/64/128 captures: those captures cannot establish fine gap/interlock quality there. The unobstructed 128 filter and native original support the larger-scale abstract observations. No Chrome session was driven or new screenshot manufactured for this audit.

## Concrete visual findings

### Pictogram: Pocket Forecast

[Original PNG](../../app-icons/images/pictogram.png) · [Exact prompt](../../app-icons/prompts/pictogram.txt) · [Source brief](sample-plan.json)

- **Native strengths:** Sun behind one broad cloud reads immediately as weather. Yellow, pale cloud and blue field separate clearly. The cloud is a strong primary mass; rounded rays share a friendly shape vocabulary. There is no frame, label, scenery or unrelated object.
- **Native weaknesses:** The familiar sun/cloud arrangement has no distinctive product-specific construction. Numerous detached rays add secondary pieces; the pale cloud dominates the lower-right while the sun/rays spread upper-left. This is understandable weather symbolism, but its silhouette could stand for many forecast products. Subtle tonal variation is visible in nominally flat fills; this is an observation, not a failed strict-color result.
- **Intent → prompt → pixels:** The assistant-chosen concept asks for two or three clean filled shapes and generous separation; the helper adds only generic flat silhouette/geometry/negative-space guidance. The actual sun is decomposed into a disc and multiple rays, so the composition is more component-heavy than the concept suggests. Treat “two or three” as the descriptive goal, not a retrospectively enforced component-count metric.
- **Chrome sizes:** At 128/64 the cloud and rays remain clear; at 32 it remains a tiny weather symbol dominated by the pale cloud. There is no evidence it becomes unrecognizable. The weak distinction from generic weather artwork matters more than raw legibility.
- **Smallest improvement:** Specify one intentional sun/cloud relationship and a reduced, consistent ray rhythm, flat color regions, and optical balance of the combined symbol. Do not add weather scenery or a new generic badge to make it “more designed.”

### Abstract: Quiet Focus

[Original PNG](../../app-icons/images/abstract.png) · [Exact prompt](../../app-icons/prompts/abstract.txt) · [Unobstructed 128 view](chrome/21-filter-abstract.jpg)

- **Native strengths:** Two broad indigo/coral arcs occupy the canvas confidently. Large center negative space and low component count produce a coherent circular gesture. Broad forms already provide a stronger silhouette presence than the monogram.
- **Native weaknesses:** The composition suggests a generic circular cycle to this reviewer; “focus” is not specifically expressed beyond the supplied label. At opposing joins, thick rounded ends approach the other arc with very tight separation rather than a clear over/under or clearly open relationship. Their swollen ends and almost-touching boundaries weaken the intended interlock. Coral against pale pink separates less strongly by eye than indigo against pink; no numerical contrast claim is made.
- **Intent → prompt → pixels:** “Balanced continuous rhythmic gesture,” “calm balanced center” and “interlocking shapes” do not settle whether the arcs touch, overlap or leave deliberate openings. The model delivered plausible curved shapes but had little guidance about what their relationship means.
- **Chrome sizes:** Both color masses remain visible at 128/64 and the two-color circular impression survives at 32. Pointer obstruction prevents a confident 32px assessment of the center gap. Do not claim the fine joins pass small-size inspection from that screenshot.
- **Smallest improvement:** Give the arcs one clear relationship around an intentional quiet center, with consistent weight and deliberate openings rather than accidental tangencies. Preserve current generous scale; don't add a target, eye, arrow, face or extra center dot to force the meaning.

### Monogram: 모아 Notes

[Original PNG](../../app-icons/images/monogram.png) · [Exact prompt](../../app-icons/prompts/monogram.txt) · [32 view](chrome/12-square-32-middle.jpg)

- **Native strengths:** The image shows the exact Hangul syllable **모**, with a clear rectangular counter, heavy blue strokes and rounded terminals on ivory. The type is high-contrast by visual inspection, symmetrical and uncluttered. It does not substitute `메모`, `모아`, a Latin letter or an added wordmark.
- **Native weaknesses:** The glyph occupies noticeably less of its canvas than abstract or Soft 3D. Large top/bottom margins make it feel like a plain glyph placed on a background rather than a distinctive app mark. Its rounded rectangle, connector and base bar are generic; no deliberate counter/terminal relationship communicates the notes product beyond the actual letter. The heavy upper enclosure and broad base need optical consideration, not just geometric centering.
- **Intent → prompt → pixels:** The saved concept explicitly asks for “comfortable margins”; the style asks for readable lettering, deliberate strokes and balanced **letter spacing**, despite this example being one Hangul syllable. Those instructions explain the competent but conservative result. Letter spacing alone does not govern the counter or internal Hangul component proportions.
- **Chrome sizes:** `모` stays recognizable at 128, 64 and 32; it is not a text-correctness failure. At 32 its mark is conspicuously small within the square relative to neighboring symbol artwork. The ivory field also blends visually into the light preview surface, whereas the 64 dark view reveals its full square extent.
- **Exact Unicode:** Saved `app_icon.text`, `brief.exact_text`, quoted `exact_lettering` and native/session/gallery prompt all retain `모` = **U+BAA8**. Existing decomposed-character tests also preserve code points rather than normalizing them. Styling must not change the requested spelling or add a font-file/vector claim.
- **Smallest improvement:** Enlarge the glyph's optical presence while retaining breathing room; author the counter, shared corner rhythm and terminals as one coherent letterform. For a single syllable, direct internal proportions and counter openness; use spacing guidance when multiple characters are actually supplied. Do not break Hangul topology to insert a notes pictogram.

### Soft 3D: Pocket Sprout

[Original PNG](../../app-icons/images/soft-3d.png) · [Exact prompt](../../app-icons/prompts/soft-3d.txt) · [128 view](chrome/09-square-128-bottom.jpg)

- **Native strengths:** A single plump heart-shaped green leaf has a clean dominant outline, clear central fold, generous scale and understandable volume. Green separates from the butter background; the bottom point and shadow anchor the object. It is simple in object count.
- **Native weaknesses:** Pronounced highlights and fine pitted/waxy surface texture make it look like a natural leaf or produce close-up rather than a carefully simplified soft object. The middle crease is a conspicuous light seam. The green heart/leaf template is familiar, with little ownable gesture beyond the fold. The background appears softly shaded around its contact shadow rather than perfectly uniform.
- **Intent → prompt → pixels:** “Tactile,” “gentle lighting” and “soft contact shadow” do not specify a material or exclude botanical texture. The subject asks for a jade leaf and the concept asks for soft sculpture; the rendering takes that ambiguity toward organic realism. More generic “3D” adjectives would not resolve it.
- **Chrome sizes:** At 128 the highlight and fold still convey a shiny leaf. At 64/32 the green heart and center ridge dominate; microscopic texture no longer provides useful identity. The small image remains recognizable, but native surface detail is doing little useful work at icon size.
- **Smallest improvement:** Specify one smooth matte molded material, broad controlled light/shadow regions, a shallow fold, and a subdued contact shadow. Preserve the leaf silhouette and palette; omit pores, veins, wet gloss and realistic surface noise. Strict palette/gradient constraints must still override any material/shading default.

### Pixel art: Little Timer

[Original PNG](../../app-icons/images/pixel-art.png) · [Exact prompt](../../app-icons/prompts/pixel-art.txt) · [32 view](chrome/13-square-32-bottom.jpg)

- **Native strengths:** A tall turquoise hourglass frame and peach sand are strongly separated from navy. The centered silhouette and stepped outline clearly communicate a timer without digits or scenery. Frame scale is ample.
- **Native weaknesses:** Step lengths, shoulder/waist widths and grain sizes appear inconsistent; some corners and boundaries look softened instead of cleanly square. Tonal texture appears inside the large color fields. The result resembles a raster drawing of a pixel icon more than a coherent coarse sprite. Two peach reservoirs plus a column of individual grains add small detail at the narrow waist.
- **Intent → prompt → pixels:** Both the concept and helper explicitly request a consistent coarse grid, so grid inconsistency is not simply absent instruction. The subject also says **a single visible sand region**, while the output has upper and lower sand masses with discrete grains. This is a concrete mismatch between saved descriptive intent and output, not a reason to erase or silently reroll the sample.
- **Chrome sizes:** At 128/64 the hourglass remains clear; at 32 the basic frame survives but stair steps and individual grains compress into much finer detail. The screenshots do not support an exact grid-alignment measurement or an exact count of surviving device pixels.
- **Smallest improvement:** Specify a single coarse square module, matching frame thicknesses and deliberate staircase cadence, no smoothing/texture/dithering, and only one sand mass. Avoid an exact promised integer grid size at the returned 1254px raster; prompt intention cannot guarantee mathematically uniform pixels.

### IP reference: Bori Reading owl (`ip-a1`)

[Original PNG](../../app-icons/images/ip-a1.png) · [Exact prompt](../../app-icons/prompts/ip-a1.txt) · [32 view](chrome/11-square-32-ip.jpg)

The owl combines a large tilted face, readable expression, lower-left anchoring and a navy open book. It has an understandable relationship to reading, and strong face/book color masses survive the existing 32px view. This gives it personality beyond naming a category symbol. It also contains shading, small feather/finger marks and extra light facial regions; the preference for this sample does not prove literal two-color raster compliance or absence of small detail. Preserve its recipe, placement defaults and semantic-color behavior exactly. Do not generalize its book, face, corner placement or illustrative detail into mandatory non-IP instructions.

## Minimal implementation boundary and compatibility PINs

The principal gap is **concept construction**, followed by style-specific execution. The helper intentionally omits historical brand/industry/use-case text in icon mode; putting product meaning into `subject` and `concept` before prompting is therefore necessary. Its omission from the rendered prompt is not itself a regression.

| Source location | Observed behavior and proposed boundary |
|---|---|
| [SKILL.md](../../../skills/logo-land/SKILL.md), lines 25–32; [app-icons.md](../../../skills/logo-land/references/app-icons.md), lines 5–19 | Add a short non-IP concept step: choose one product-relevant visual relationship, one distinctive construction decision, and the small-size feature to preserve. Avoid vague adjective stacks and generic examples becoming default final concepts. Keep the IP three-direction/two-candidate recipe intact. |
| [app_icon_prompts.py](../../../skills/logo-land/scripts/logo_helper/app_icon_prompts.py), lines 17–51 | Five non-IP branches currently provide one generic style sentence each. Enrich only those branches with the concrete geometry/material/type/grid guidance above. IP lines 19–26 are a compatibility boundary. |
| [app_icon_prompts.py](../../../skills/logo-land/scripts/logo_helper/app_icon_prompts.py), lines 56–67, 80–128 | Preserve explicit placement, quoted JSON, trusted-tail order, Unicode, structured-palette precedence, background/shape exclusions and complete 20,000-character check. Avoid changing the shared placement sentence to impose an IP-breaking margin or center rule. |
| [app_icon_models.py](../../../skills/logo-land/scripts/logo_helper/app_icon_models.py), lines 10–47; [app_icon_presets.py](../../../skills/logo-land/scripts/logo_helper/app_icon_presets.py), lines 18–57 | Retain the six public IDs, complete intent shape and Unicode constraints. New quality scores, presets, session schemas or approval states are unnecessary for these observations. |
| [prompts.py](../../../skills/logo-land/scripts/logo_helper/prompts.py), lines 60–85; [intent.py](../../../skills/logo-land/scripts/logo_helper/intent.py), lines 31–43 | Dedicated icon branch and explicit → parent (including null) → brief precedence already exist. Preserve exact metadata/revision binding and suppression of historical lettering/lockup. |
| [app_icon_gallery.py](../../../skills/logo-land/scripts/logo_helper/app_icon_gallery.py), lines 19–41, 115–123 | Original/prompt hashes and intent are stored together, and publication reads original bytes. Do not rewrite the existing published prompts when generator wording changes. |
| [delivery.py](../../../skills/logo-land/scripts/logo_helper/delivery.py), lines 117–140 | Selection, explicit visual review, background, source hash and fresh color evidence remain mandatory for approved export. Quality advice must never create a bypass. |

Audited `app_icon_prompts.py` SHA-256: `38fbf3cfdb3efd97da4b96eb554cd392f5ae06cb1d8cb12a27822729b280c015`. Audited `references/ip-mascot.md` SHA-256: `08f93b78555246ea3b71a11d4879a53790808df4cab400bd5ed84b6d409e4850`.

Relevant existing test inventory:

| Existing test file / lines | What it actually establishes |
|---|---|
| [test_app_icon_prompts.py](../../../tests/test_app_icon_prompts.py), 21, 58, 72, 88, 99, 116 | Image-only IP/trusted tail, semantic fallback versus strict colors, full prompt length, full IP/monogram snapshots, six distinct prompt texts and monogram-only lettering. Six different strings do **not** establish six good designs. |
| [test_app_icon_compatibility.py](../../../tests/test_app_icon_compatibility.py), 29, 49, 57, 66 | Real pre-icon v1/v2 byte-preserving reads/backup behavior, exact legacy generation/edit prompts, old import defaults and stale rejection. |
| [test_app_icon_models.py](../../../tests/test_app_icon_models.py), 18, 50, 66, 76, 100 | Preset/placement combinations, invalid shapes, Unicode length/control rules, exact code points including decomposed `e\u0301`, matching monogram brief text. The parameterized exact-Unicode cases do not yet include this particular `모` sample. |
| [test_app_icon_workflow.py](../../../tests/test_app_icon_workflow.py), 68, 91, 123, 137, 149, 162, 176, 199 | Real CLI init/prompt/import/show; inheritance/override; malformed intent rejection; transparent/lockup conflicts; six IDs; immutable gallery; oversized import. |
| [test_app_icon_workflow_invariants.py](../../../tests/test_app_icon_workflow_invariants.py), 19, 37, 72, 88, 102, 134, 160 | Legacy null, overrides, null rejection, immutable history, failed-save rollback and same-ID retry, no successful artifact for unreturned call, inert shell metacharacters. |
| [test_app_icon_workflow_palette.py](../../../tests/test_app_icon_workflow_palette.py), 16, 43 | Parent/explicit/active palette binding and actual strict-color export rejection despite a passed visual review. |
| [test_app_icon_gallery.py](../../../tests/test_app_icon_gallery.py), 80, 107, 161, 193, 206, 259 | Exact originals/prompts/intent, inert metadata, invalid selections/paths, failure cleanup and stable snapshot during later state advance. |
| [test_app_icon_delivery.py](../../../tests/test_app_icon_delivery.py), 54, 101, 171, 212 | Exact ZIP/image pairing, seven export gates, publication rollback/resume and no clobber on destination races. |

Before any change, retain the existing exact IP snapshot plus pre-icon generation/edit snapshots as explicit compatibility PINs. Extend the IP PIN matrix to lower-left, lower-right and explicit center; semantic fallback, user colors and strict palette; generation and parent edit. Reuse the eleven historical prompt files as immutable lineage references, not golden expected wording for future non-IP generation. The old monogram prompt snapshot documents behavior intentionally changed by a typography improvement; preserve its historical fixture and scope any new expectation to a new prompt case rather than replacing history.

**Meaningful baseline and new RED proposal:** Current tests above are baseline/PIN evidence. For new non-IP behavior, test decisions and parsed rule data rather than merely checking that a new adjective occurs. If the implementation needs conditional quality rules, keep them as a small internal rendering policy, not a new public or persisted schema: (1) one-character versus multi-character monogram treatment must preserve the original Unicode sequence while selecting internal-counter treatment versus inter-character spacing; (2) a strict palette that forbids extra tones/gradients must suppress incompatible soft-material/shading defaults while preserving palette ID, digest, locks and actual export rejection; (3) pixel construction must select a uniform coarse module/cluster policy while the same subject through another preset does not inherit pixel instructions. The old implementation has no such conditional decisions, so a behavioral test would fail for that missing decision before implementation. Test multiple inputs and precedence relationships, not a mirror of one new literal sentence.

Do not introduce an internal policy abstraction solely to obtain a RED test; the default is the existing subject/concept/changes/palette interface. If the final change is only revised prose in the existing branches, do not manufacture a software RED claiming improved aesthetics: keep baseline/PIN checks, check trusted-boundary/metadata invariants, and use the new same-subject native comparisons below as the actual quality evaluation. A new deterministic test cannot prove that generated pixels will obey a grid or look better. The coordinator/Metis contract should state which logical behavior is added before requiring its RED. No tests were added or weakened by this audit.

## Decision-complete same-subject comparison briefs

The coordinator's later comparison proposal was read: a separate gallery containing all original eleven plus five new originals (sixteen total), preserving the current gallery. This is consistent with the audit and remains pending research/Metis contract; no comparison gallery was created here.

These are proposed fresh draws for the user's improvement request, not approval or calls made by this worker. Preserve each existing `app_icon` subject, preset, centered placement and text, along with the same fictional product and color descriptions from [sample-plan.json](sample-plan.json). Change the construction concept/guidance, not the product or palette. Use one independent draw per proposed new ID, a new session/receipt, and no old-image reference for a fresh comparison. Record the exact final prompt before the call; never replace or rebind the original IDs. The coordinator may map these proposed IDs once before dispatch; a returned/unknown attempt keeps its mapped ID on every resume.

| Proposed new ID / unchanged subject | New concept brief | Inspect in the returned original and actual 32/64/128 comparison |
|---|---|---|
| `pictogram-quality-v1` / sun partly behind one broad cloud / Pocket Forecast | One cloud with a broad asymmetric crown and stable flat base; a large partly revealed sun nestles into its upper-left contour. Use three broad, consistently rounded visible rays as one sparse rhythm. Two foreground color families on the original blue; flat surfaces, no texture/shadow, no extra objects. Balance the sun/cloud as one large central mark. | Does the cloud/sun relationship feel intentional and distinguishable while weather still reads? Is the small silhouette coherent without scattered ray noise? Is the symbol optically balanced and separate from its field? |
| `abstract-quality-v1` / two interlocking rounded arcs / Quiet Focus | Two equally substantial arcs turn around one calm open center. Give both ends a shared radius/weight rhythm; use two deliberate openings with clear separation rather than almost-touching tips. The gesture should suggest gathering attention toward a quiet middle. Original indigo/coral/pink; no face, arrows, target dot, extra rings or material effects. | Are the openings and common center intentional at native size and 128? Do both arcs remain distinguishable at 64/32? Does the concept communicate quiet focus more clearly than the old circular-cycle impression? Preserve present bold canvas use. |
| `monogram-quality-v1` / exact `모` / 모아 Notes | Draw only `모` (U+BAA8), with larger optical presence. Author a wide open ㅁ counter, a controlled central stem and broad ㅗ base using one consistent rounded-terminal family. Balance upper enclosure and lower bar while preserving normal Hangul topology; maintain clear margins without a timid central glyph. Original sapphire/ivory; no extra symbol, glyph, word or font claim. | Is the exact syllable unchanged and readable? Is the counter open at 32? Does it occupy its square more confidently without cramped/cropped strokes? Is the letterform more distinctive than a plain rounded glyph? |
| `soft-3d-quality-v1` / plump heart-shaped jade leaf with shallow fold / Pocket Sprout | One smooth matte molded leaf, a broad heart silhouette with softly asymmetric lobes and one shallow central fold. One broad gentle highlight and restrained depth, subdued contact shadow; no botanical pores/veins, wet gloss, granular texture, extra stems or scenery. Retain jade/pale-leaf/butter palette descriptions and obey explicit color constraints. | Does material read as a deliberate simplified soft object? Is the fold subordinate to the main silhouette? At 32 do green shape and broad light region remain clear without relying on texture? Is the background calm and separate? |
| `pixel-art-quality-v1` / chunky hourglass, broad frame, single sand region / Little Timer | Build the whole hourglass from one consistent coarse square module and repeated staircase cadence. Broad equal-weight top/bottom bars and matching sides frame one peach sand mass in the upper chamber; the lower chamber stays empty. No individual falling grains, sub-grid accents, smoothing, gradients, texture, glow, dithering, numerals or scenery. Original turquoise/peach/navy. | Is the silhouette still an hourglass? Is there exactly the requested single visible sand mass? Do steps/frame thickness form a coherent grid language at native size and readable clusters at 32? Do not claim exact integer-grid compliance without separate measurement. |

The monogram component references above describe typography, not permission to replace the exact character. The pixel brief intentionally resolves the old single-sand-region mismatch. All evaluation questions are review prompts; record both improvements and regressions, include every returned candidate, and ask for selection when needed rather than assigning automatic artistic PASS/FAIL. If a prompt detail conflicts with explicit user colors, lettering or placement, the user intent wins.

## Executed verification

### Immutable native → gallery binding

Typed `GalleryManifest` parsing and saved native-lineage receipts were used. For **each of eleven IDs**, the audit rehashed: the actual native path from the existing exact-basename locator, `output/app-icons-native/<id>/original.png`, its source-session imported artifact, the catalog artifact, and the published PNG. All five locations were equal to the saved manifest/native hashes. No timestamp/newest-file search was used. Source receipt and source-session SHA values also matched their saved lineage records.

Every published prompt matched its original prompt file and imported source-session prompt, its manifest/native prompt digest, and the quoted subject/exact text in that artifact's intent. Rebuilding from the saved source brief, saved concept/changes and current `build_app_icon_prompt` returned all **eleven byte-identical prompts**. This establishes the audited pixels' binding to today's baseline prompt source; future changed non-IP prompts must get new sample IDs, not be attached to these images.

The eleven IDs remain `ip-a1`, `ip-a2`, `ip-b1`, `ip-b2`, `ip-c1`, `ip-c2`, `pictogram`, `abstract`, `monogram`, `soft-3d`, `pixel-art`. Full individual hashes are retained in [manifest.json](../../app-icons/manifest.json) and [native-samples.json](native-samples.json). Focused audit hashes:

| ID | Original PNG SHA-256 | Exact prompt SHA-256 |
|---|---|---|
| pictogram | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| abstract | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| monogram | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| soft-3d | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
| pixel-art | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| ip-a1 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |

Manifest SHA-256: `fe6b2183a34beadf3932f00a63999ba17015792f15f87511b14a0ed9d9801dc9`. Gallery HTML SHA-256: `e87c1e9d3a78b6404d5560d8e778e8ef812618e7f13d1e7ed7a1d3b18e74a1bd`.

### Actual CLI and focused baseline tests

Executed the public CLI through bounded `subprocess.run(..., timeout=30)`, exit 0:

```sh
uv run --locked --no-sync python skills/logo-land/scripts/logo_project.py icon-presets
```

Parsed its actual JSON as `tuple[AppIconPresetChoice, ...]`; exact ordered IDs: `ip_mascot`, `pictogram`, `abstract`, `monogram`, `soft_3d`, `pixel_art`. Hyphenated sample filenames are not additional preset IDs.

Executed once, with a 180-second outer timeout and the existing harness's 20-second command bounds:

```sh
PYTHONDONTWRITEBYTECODE=1 uv run --locked --no-sync pytest -q -p no:cacheprovider \
  --basetemp=/tmp/ll-icon-quality-audit/pytest-temp \
  tests/test_app_icon_prompts.py \
  tests/test_app_icon_compatibility.py \
  tests/test_app_icon_models.py::test_unicode_monogram_is_preserved_exactly \
  tests/test_app_icon_workflow_invariants.py \
  tests/test_app_icon_workflow_palette.py \
  tests/test_app_icon_delivery.py::test_icon_metadata_never_bypasses_existing_export_gates
```

Result: `34 passed in 30.78s`, exit 0. Tests use explicitly synthetic disposable PNG/session fixtures; their success is software baseline evidence, not a native visual score. Other inventory entries above were read, not rerun. No full-suite, build, source formatter or LSP rerun was needed for this Markdown-only audit.

### Manual HTTP channel

`/tmp/ll-icon-quality-audit` and `127.0.0.1:8792` were registered in `resources.txt` before server launch; the directory and listener were absent beforehand. Served the existing `docs/app-icons` directly using a foreground `.venv/bin/python -m http.server`, PID **58908**, exec session **25964**. Executed exactly:

```sh
curl -i --fail --silent --show-error --connect-timeout 2 --max-time 10 \
  http://127.0.0.1:8792/images/monogram.png \
  -o /tmp/ll-icon-quality-audit/monogram.http
```

Returned headers:

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:44:30 GMT
Content-type: image/png
Content-Length: 832716
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

Split the saved bytes at the first CRLF/CRLF header boundary without changing the image. Body length **832716 bytes**; body SHA-256 **964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b**; body equals `docs/app-icons/images/monogram.png` exactly. The HTTP 200/body check establishes delivery, while actual `view_image` inspection establishes this audit's visual channel.

## Nine adversarial classes

| Class | Actual probe, outcome and limit |
|---|---|
| 1. Malformed/truncated manifest | In registered disposable copies, changed the actual manifest kind to `wrong_kind` and separately truncated its bytes halfway. The real `GalleryManifest.model_validate_json` rejected them with `literal_error` and `json_invalid`. The original was untouched. This tests parsing, not a nonexistent CLI manifest-import feature. |
| 2. Prompt injection | Executed existing image-only/trusted-tail and shell-metacharacter tests. Subject strings containing shell syntax stayed quoted data; the marker file was not created, and imported intent retained the input. Native prompts were parsed as quoted JSON, never executed. No model-level injection immunity is claimed. |
| 3. Cancel/resume | Executed the existing failed-save rollback → same-ID resume fixture; state/source bytes survived and no partial artifact/lock remained. Real original hashes were reread after the pause between audit phases. Killing a live native call is N/A: none was started and no foreign process was interrupted. |
| 4. Stale source/prompt binding | All eleven actual source/receipt/prompt bindings were rehashed and prompts rebuilt. An in-memory copied monogram entry with an all-zero prompt digest failed the explicit digest comparison; schema validity alone does not authenticate bytes. Existing stale-state and immutable-intent tests passed. Actual history was never rebound. |
| 5. Dirty shared worktree | Captured initial `git status --short`, including pre-existing tracked changes and untracked icon/branding files. Preserved them. Registered source/test/IP hashes were reread to ensure this audit's evidence remained tied to the inspected source; this worker owns only this report in the repository. |
| 6. Hung/bounded commands and server | HTTP connect/max bounds 2/10 seconds; CLI bound 30 seconds; targeted test subprocess bound 180 seconds and existing harness commands 20 seconds. Server ownership was checked by PID/command/listener before SIGTERM; port 8792 is no longer listening. No broad kill, service restart or browser control. |
| 7. Artistic flakiness | No artistic reroll or automatic beauty PASS/FAIL. Native originals show texture/grid/shape variation and all remain visible. Focused tests passed once without retry; randomized native quality is evaluated through visible comparisons, not deterministic unit assertions. |
| 8. Misleading success | HTTP and tests are explicitly separated from visual preference, strict color approval, selected export and platform readiness. Seven actual export-gate cases passed, including forged/missing strict evidence. No production-ready or store-accepted claim is made. |
| 9. Repeated interruptions | The executed rollback/resume test retries stale/current IDs repeatedly and rejects duplicates without changing saved state/source. The eleven original gallery IDs/order and hashes were reread across audit phases. Multiple real generation interruptions are N/A because this worker made zero native calls; no unknown attempt was reset or replaced. |

## Cleanup and remaining ownership

Before stopping, `ps` and `lsof` confirmed PID 58908 was precisely this task's server on `127.0.0.1:8792`. Only that PID received SIGTERM; exec session 25964 exited 143, and `lsof -nP -iTCP:8792 -sTCP:LISTEN` found no listener. The test process exited 0. No browser/tab/window resource was created.

The registered temporary root contains only this task's raw HTTP response, hash registries, typed-lineage/CLI JSON, malformed manifest copies, test log and disposable pytest fixtures. Essential results are transcribed above. Final integrity/link verification and exact temporary-root removal are recorded below. All original PNGs, original prompts, Chrome screenshots and pre-existing changes are preserved.

Remaining work belongs to the coordinator: resolve the final Q1 contract with research/Metis, implement the chosen non-IP guidance with meaningful compatibility/behavior checks, and dispatch fresh same-subject samples under new IDs for the user's explicit improvement request. This audit does not claim those changes or samples already exist.

Final integrity verification: **24** original/prompt/manifest/HTML files, **29** existing Chrome screenshots and **22** relevant source/test/guidance files all match the registered pre-probe SHA-256 values; **43** unique report links resolve and authored whitespace is clean. Other owners continued unrelated branding documentation work during this audit; no clean-worktree claim is made and those changes were preserved.

Cleanup verified at 2026-09-12T17:50:35.080635+00:00: exact `/tmp/ll-icon-quality-audit` removed after evidence transcription; port 8792 has no listener. Repository deliverable: this report only.
