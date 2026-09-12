---
name: logo-land
description: Create, compare, refine, and export brand logos through conversation using Codex native image generation. Use for new logos, transparent-background PNG logos, removing a logo's background, reference-guided revisions, and resuming saved logo projects.
---

# Logo Land

Turn the user's brand brief into actual logo images, refine their selected direction, and deliver verified files. Respond in the user's language; use polite Korean when speaking Korean.

## Execution boundary

The host's native image generation tool creates and edits images. This skill's Python helper only builds prompts, persists projects, checks images, and packages files. Running the helper alone does not generate a logo. A plugin cannot grant an unavailable image tool.

Read [native-image.md](references/native-image.md) before the first image call. Use the current tool schema, not API arguments. If the tool is absent or fails, report the actual limitation, preserve the brief and previous images, and do not invent a result or silently switch to a paid API.

## Start or resume

- For an existing project, read its state using `show` as described in [project-files.md](references/project-files.md). Use saved artifact IDs and verified file paths. If several sessions exist and the user has not identified one, present their names for selection.
- For a new logo, extract information already supplied. Ask only consequential missing questions, usually brand name/exact text, what the business does, audience, and desired feel or use. Offer a short choice when useful. Never make a user re-enter a complete brief.
- A concrete request to create or edit is authorization to perform that operation. Do not insert another mandatory approval gate. When the user asks only to discuss directions, keep the work at that stage.
- If the user has no visual preference, propose distinct directions in ordinary language. Use [logo-directions.md](references/logo-directions.md) to distinguish logo type from style. Record assumptions. Default to three separate concepts unless the user specifies another count or only one image is appropriate.
- Resolve the skill folder from the location of this file; its plugin root is two directories above it. Store data in the user's workspace, never in the plugin installation. Create a brief and session with the helper. The complete schema is in [project-files.md](references/project-files.md), with a working [example](assets/brief.example.json).

## Generate and compare

1. Build a focused prompt per concept. Include intended use, exact lettering, logo type, subject, palette, composition, background, and exclusions. Keep explicit user choices. Favor a legible silhouette and useful negative space; avoid adding unsolicited slogans or symbols.
2. Call the actual native image tool once per separate concept. A contact sheet is a presentation, not several independent logo files. Save the exact final prompt used, including any additions to the helper's proposed prompt.
3. Inspect each returned image. Copy/import only the artifact identified by that call; never choose the newest file from a shared generation folder. Preserve every requested concept in the workspace with stable IDs such as `a-v1`, `b-v1`, `c-v1`.
4. Show the images with their IDs and one sentence explaining each direction. Ask which direction to refine when selection is still needed. Do not call any option user-approved until the user selects it or explicitly delegates the choice.

## Refine

- Interpret “the second one” using the displayed IDs. Read the chosen file with the image viewer before editing when it has not been seen in the current context.
- Use that exact image as the edit target. State the requested change and what should remain constant: wording, silhouette, layout, or palette as appropriate. A style reference is not automatically an edit target.
- Record the real `parent` artifact and write a new ID, for example `b-v2`. Keep the original unchanged. Reopen the result and check that the requested change occurred without unintended drift.
- Support natural-language adjustments to text, typography appearance, spacing, proportions, symbol, color, background, arrangement, and style. These are raster edits; do not promise editable font layers or pixel-perfect preservation.
- For supplied images, import the exact original with provenance before editing if project continuity is desired. If required references cannot be supplied to the tool, ask for the missing image again.
- Treat monochrome, reversed, icon-only, horizontal, stacked, avatar, or application mockups as explicit variants. Generate requested variants using the chosen image; retain parent relationships. Do not deliver a mockup as the master logo.
- Record each artifact's intended background with import `--background opaque|transparent` when it differs from the original brief, including later edits preserving that variant. Export checks the selected artifact's requirement; do not change it merely because generation returned the wrong background.

## Verify and deliver

### Transparent backgrounds

- Interpret requests such as “투명 배경”, “배경 없이”, “누끼”, or “transparent PNG” as an actual transparent-background requirement. For a new logo, set the brief's `background` to `transparent`; keep a requested opaque color otherwise.
- Ask the native image tool for a genuine RGBA PNG with a fully transparent exterior, visible foreground, clean anti-aliased edges, and no painted checkerboard, white backing panel, or background shadow. Preserve intentional white foreground details, such as white lettering.
- For background removal, edit the exact existing logo with its wording, colors, shape and layout preserved. Import the new child with `--parent <id> --background transparent`; keep this override on later transparent edits even if the initial brief was opaque.
- Open the result on light and dark CSS backgrounds to check the cutout, letter counters, halos and contrast. Changing the preview background never changes the PNG. If the artwork is too dark on a dark surface, describe that limit or create an inverted variant when requested.
- Verify actual transparent pixels before delivery. If the image still has a solid or painted background, request another native edit; never remove background pixels with an unrequested script, rename a JPEG to PNG, or weaken the requirement to pass export.

### Final checks

Read [delivery-checks.md](references/delivery-checks.md) for final QA. Inspect exact text (especially Hangul), margins, recognizable shape at small display size, background, and edit preservation. Report actual findings; do not mark every check true by default.

Use the helper to select the final ID, record the visual review, and export. It verifies actual PNG format, visible content, hashes, and transparency requirements before packaging. If a transparent brief produces an opaque image, request a real background edit and inspect it; do not lower the requirement to make export pass.

Deliver links to the selected PNG, ZIP, and brand guide with actual dimensions and transparency status. Mention the selected ID and any material limitation briefly. Native image output is raster: SVG/EPS/AI, font files, vector paths, CMYK, trademark availability, and exclusive rights must never be claimed unless separately produced and verified.

Keep the project open for further edits. A later change creates another version and another export; it must not overwrite the previously delivered package.
