---
name: logo-land
description: Create, compare, refine, and export logos and mobile app icon artwork through conversation using native image generation. Use for IP characters, pictograms, abstract icons, Unicode monograms, soft 3D, pixel art, transparent logos, guided palettes, exact lettering, and saved revisions.
---

# Logo Land

Turn the user's brief into actual logo images or app icon artwork, refine their selected direction, and deliver original files with truthful evidence. Respond in the user's language; use polite Korean when speaking Korean.

## Execution boundary

The host's native image generation tool creates and edits images. This skill's Python helper only builds prompts, persists projects, checks images, and packages files. Running the helper alone does not generate a logo. A plugin cannot grant an unavailable image tool.

Read [native-image.md](references/native-image.md) before the first image call. Use the current tool schema, not API arguments. If the tool is absent or fails, report the actual limitation, preserve the brief and previous images, and do not invent a result or silently switch to a paid API.

## Start or resume

- For an existing project, read its state using `show` as described in [project-files.md](references/project-files.md). Use saved artifact IDs and verified file paths. If several sessions exist and the user has not identified one, present their names for selection.
- Keep a short continuity note: intended use, source session/artifact, why the direction fits, what to keep, what to change and what was actually observed. Reuse `use_cases`, `assumptions`, `concept`, `changes` and review `notes`; comparison input metadata can preserve the decision across sessions. Follow [comparison-workflow.md](references/comparison-workflow.md) when comparing or resuming a selection, without adding session fields.
- For a new logo, extract information already supplied. Ask only consequential missing questions, usually brand name/exact text, what the business does, audience, and desired feel or use. Offer a short choice when useful. Never make a user re-enter a complete brief.
- A concrete request to create or edit is authorization to perform that operation. Do not insert another mandatory approval gate. When the user asks only to discuss directions, keep the work at that stage.
- If the user has no visual preference, propose distinct directions in ordinary language. Use [logo-directions.md](references/logo-directions.md) to distinguish logo type from style. Record assumptions. Default to three separate concepts unless the user specifies another count or only one image is appropriate.
- Read [color-workflow.md](references/color-workflow.md) when selecting or changing colors: automatic, anchor, restricted, and reference requests compose. Preserve exact locks, select when delegated, and map one palette to each concept without multiplying generation calls. For optional already-connected Leonardo, read [color-providers.md](references/color-providers.md).
- For symbol-plus-text layouts or typography changes, read [typography.md](references/typography.md). The existing `combination` type supports horizontal and stacked lockups; record layout and typeface appearance while preserving exact brand and slogan text. A requested font name is a visual reference, not proof of a font file used.
- Resolve the skill folder from the location of this file; its plugin root is two directories above it. Store data in the user's workspace, never in the plugin installation. Create a brief and session with the helper. The complete schema is in [project-files.md](references/project-files.md), with a working [example](assets/brief.example.json).

## Generate and compare

For mobile app icon artwork, first read [app-icons.md](references/app-icons.md) and use its dedicated prompt and comparison branch. The exact preset IDs are `ip_mascot`, `pictogram`, `abstract`, `monogram`, `soft_3d` and `pixel_art`; discover them with `icon-presets`. Infer style and subject through conversation. For IP, read the attributed [character recipe](references/ip-mascot.md): normally three product-related directions and six separate one-pass candidates, with every original retained. A creation request already authorizes generation. Never impose a palette, model-name or API-key gate.

For each non-IP concept, use the supplied product context to connect a product benefit to a named motif, one distinguishing construction and the personality or identifying feature that should survive at small size. Keep a specified subject and requested count; ask only for consequential missing input and record other assumptions. Put this concise idea in the existing `concept`, keep the literal motif in `app_icon.subject`, describe refinements in `changes`, and record colors in `brief.palette` or existing structured palette roles. Use the five [construction and comparison examples](references/app-icons.md#construct-a-non-ip-concept) to make a concrete shape, lettering, material or pixel-cluster decision. These are creative instructions, not guarantees of better images or another approval step.

Icons request a full-bleed square with square outer corners and a complete solid background. Defaults use lower corners for IP and center for other styles, while honoring explicit alternatives. Only monogram renders its supplied exact 1–8-code-point Unicode text; other icon presets have no text. A new icon brief has empty slogan and null lockup. User colors and explicit strict palettes take precedence over semantic style colors. Use the helper's dedicated icon prompt, save its resolved intent/revision and exact final text, and preserve actual output dimensions and bytes.

Use `icon-gallery` to compare every requested icon original and its exact prompt, irrespective of approval or color status. Do not filter or automatically retry artistic variation, resize originals, or claim platform readiness from CSS masks. Approved export is an optional later operation that retains every existing visual/background/integrity/strict-color gate. The steps below describe the ordinary brand-logo branch.

Use `compare-gallery` with an explicit selection file for candidates from several sessions or a mixture of brand logos and icons. Show one product-related reason and one visible limitation per candidate at the intended use size. The [comparison workflow](references/comparison-workflow.md) binds each card to its source session, artifact and revision; opening or copying a card does not select or approve it.

1. Build a focused prompt per concept. Include intended use, exact lettering, logo type, subject, selected palette/roles/constraints, lockup when relevant, background, and exclusions. Reject conflicting color constraints before image calls. Save the prompt's revision and effective intent for import. Favor a legible silhouette and useful negative space; avoid adding unsolicited slogans or symbols.
2. Call the actual native image tool once per separate concept. A contact sheet is a presentation, not several independent logo files. Save the exact final prompt used, including any additions to the helper's proposed prompt.
3. Inspect each returned image. Copy/import only the artifact identified by that call; never choose the newest file from a shared generation folder. Preserve every requested concept in the workspace with stable IDs such as `a-v1`, `b-v1`, `c-v1`.
4. Show the images with their IDs and one sentence explaining each direction. Ask which direction to refine when selection is still needed. Do not call any option user-approved until the user selects it or explicitly delegates the choice.

## Refine

- Interpret “the second one” using the displayed source session and artifact IDs, including the gallery's current filtering/order. Reopen `show` and the exact chosen original before editing. A saved gallery describes a historical revision; reconcile it with current state before using its source.
- Use that exact image as the edit target. State the requested change and what should remain constant: wording, silhouette, layout, or palette as appropriate. A style reference is not automatically an edit target.
- Carry the chosen reason and keep/change notes into the existing `changes` text as quoted data, using a file and safely quoted argv. Preserve supplied text, color roles and identifying geometry unless the requested change addresses them. After editing, compare parent and child against those same notes and record observed improvement, stability or regression; do not turn notes into approval or another automatic reroll.
- Record the real `parent` artifact and write a new ID, for example `b-v2`. Keep the original unchanged. Reopen the result and check that the requested change occurred without unintended drift.
- Geometry-only edits inherit the selected parent's palette and lockup even when the active palette or initial brief differs. A color change creates a palette version; an arrangement/typeface change supplies a new lockup intent. Legacy artifacts keep unknown structured intent unless explicitly supplied. Use the same effective intent and revision at prompt/import; handle stale revisions before attaching an image.
- Icon edits also inherit the parent's `app_icon`, including null for legacy parents. An explicit complete `--app-icon-file` overrides that intent and can transform a brand logo into icon artwork while preserving history. Use the same file with prompt/import; explicit lockup or transparent import conflicts with icon mode. Omitted icon import background resolves to opaque.
- Support natural-language adjustments to text, typography appearance, spacing, proportions, symbol, color, background, arrangement, and style. These are raster edits; do not promise editable font layers or pixel-perfect preservation.
- For supplied images, import the exact original with provenance before editing if project continuity is desired. If required references cannot be supplied to the tool, ask for the missing image again.
- Treat monochrome, reversed, icon-only, horizontal, stacked, avatar, or application mockups as explicit variants. Generate requested variants using the chosen image; retain parent relationships. Do not deliver a mockup as the master logo.
- Record each artifact's intended background with import `--background opaque|transparent` when it differs from the original brief, including later edits preserving that variant. Export checks the selected artifact's requirement; do not change it merely because generation returned the wrong background.

## Verify and deliver

For the initial app-icon candidate set, preserve all returned originals and show the creative gallery without approval badges. The checks below apply when an approved export is requested. Icon artwork remains raster; it does not include Icon Composer documents, Android adaptive layers, an app build or store acceptance. Do not apply brand-logo transparent-background instructions to an icon intent.

### Transparent backgrounds

- Interpret requests such as “투명 배경”, “배경 없이”, “누끼”, or “transparent PNG” as an actual transparent-background requirement. For a new logo, set the brief's `background` to `transparent`; keep a requested opaque color otherwise.
- Ask the native image tool for a genuine RGBA PNG with a fully transparent exterior, visible foreground, clean anti-aliased edges, and no painted checkerboard, white backing panel, or background shadow. Preserve intentional white foreground details, such as white lettering.
- For background removal, edit the exact existing logo with its wording, colors, shape and layout preserved. Import the new child with `--parent <id> --background transparent`; keep this override on later transparent edits even if the initial brief was opaque.
- Open the result on light and dark CSS backgrounds to check the cutout, letter counters, halos and contrast. Changing the preview background never changes the PNG. If the artwork is too dark on a dark surface, describe that limit or create an inverted variant when requested.
- Verify actual transparent pixels before delivery. If the image still has a solid or painted background, request another native edit; never remove background pixels with an unrequested script, rename a JPEG to PNG, or weaken the requirement to pass export.

### Final checks

Read [delivery-checks.md](references/delivery-checks.md) for final QA. Inspect exact text (especially Hangul and slogans), margins, recognizable shape at small display size, background, lockup, color-role placement, and edit preservation. Report actual findings; do not mark every check true by default.

Use the helper to select the final ID, record the visual review, and export. It verifies actual PNG format, visible content, hashes, and transparency requirements before packaging. If a transparent brief produces an opaque image, request a real background edit and inspect it; do not lower the requirement to make export pass.

Separate intended HEX values from sampled raster measurements. Strict color mismatch or insufficient evidence blocks a compliant export even after visual approval; advisory and legacy reports retain their limitations. For a color mismatch, make at most two additional native edits for the same request, re-inspect each, then preserve unresolved candidates and report the gap. Never recolor with Python or weaken constraints to obtain a pass.

Deliver links to the selected PNG, ZIP, and brand guide with actual dimensions and transparency status. Mention the selected ID and any material limitation briefly. Native image output is raster: SVG/EPS/AI, font files, vector paths, CMYK, trademark availability, and exclusive rights must never be claimed unless separately produced and verified.

Keep the project open for further edits. A later change creates another version and another export; it must not overwrite the previously delivered package.
