# Delivery checks

The helper validates file facts; the assistant evaluates design. Both are required for a final export.

## File inspection

- Decode the image and confirm it is actually PNG, not another format with a renamed extension.
- Require visible pixels. All-transparent images are unusable.
- “Has an alpha channel” is not equivalent to transparency. Require actual non-opaque pixels and visible logo pixels for a transparent deliverable. A checkerboard painted into RGB pixels is not transparency.
- Check saved SHA-256 before resume/export so unexpected modifications cannot silently become the final logo.
- Preserve the original and register revisions with a real parent ID. Never overwrite the previous image to simulate versioning.

## Visual inspection

Open the actual image with the available viewer. For transparent files, view on light and dark backgrounds when the viewer/browser allows it; CSS backgrounds do not change the image bytes. Display the logo near its intended small usage size as well as large.

Record these review fields based on what was observed:

```json
{
  "reviewer": "Codex visual inspection",
  "notes": "Explain the specific observations, including any limitation.",
  "text_correct": true,
  "composition_ok": true,
  "small_size_ok": true,
  "preservation_ok": true,
  "background_checked": true
}
```

- `text_correct`: exact required words, letters and punctuation match; no unsolicited text. For a text-free symbol, verify no text appeared.
- `composition_ok`: useful margins, no clipping, balanced arrangement and recognizable subject.
- `small_size_ok`: the intended small use remains identifiable. A wordmark need not be readable at favicon size unless favicon use was requested.
- `preservation_ok`: an edit keeps the specified invariants; for a new generation, the requested constraints are respected.
- `background_checked`: observed background matches the selected artifact's requested background (the original brief unless explicitly overridden) and the stated transparency status.

Use false for a failed check and fix the image through the image tool. Never run a default all-true review to unlock export. The JSON above illustrates the schema, not a ready-made approval.

For a combination logo, compare the selected artifact's lockup with the actual image: horizontal/stacked arrangement, symbol before/after the text, alignment, clear space and requested typography character. Check the exact English or Hangul string and slogan, including spacing and punctuation. Confirm role placement visually, such as the fixed green in the symbol or white in the lettering. A histogram cannot prove those placements. A requested font family remains a visual reference; generated raster lettering does not identify an installed or licensed font file.

## Color evidence and export policy

Resolve the selected artifact's palette, not the session's active palette or the initial brief. A green original still exports its green intent after a navy child exists. Geometry-only edits inherit the actual parent's palette/lockup. A color edit creates a new palette version and keeps the earlier version intact.

Separate these facts in the handoff:

| Evidence | What it establishes |
|---|---|
| Intended swatches, roles and constraints | The exact normalized HEX values and placement that were requested |
| Measured swatches and target measurements | Estimates and distances from the stated image/hash and sampling scope |
| Visual review | Observed lettering, layout, role placement, preservation and small-size appearance |
| Profile/sampling limitations | The bounds on what the measurements can establish |

Reports name their artifact/hash, palette ID/digest, `logo-color-v1` policy, ColorAide/Pillow versions, profile treatment, scope/ROI, core/partial-alpha sample counts, target ΔE00, coverage and reasons. Measured display swatches are quantized estimates; conformance compares original sampled colors. Never copy intended HEX into a “measured” field or infer a passing report from a good-looking preview.

The policy samples at most 16,384 original pixel positions. It excludes fully transparent pixels, uses alpha ≥250 for core conformance and reports partial alpha separately. Intentional white and opaque backgrounds are included; CSS preview surfaces are excluded. Full-image analysis includes the composition's background. An explicit ROI limits the claim to that region and is not automatic foreground segmentation. Untagged images are `assumed_srgb`; supported ICC conversion takes place only in analysis memory. Unsupported profile evidence is indeterminate. The original PNG is not recolored or rewritten.

Initial tolerance is ΔE00 ≤5 in Lab D50. Restricted palettes require at least 99% matching core coverage; locked/required colors need at least 32 matching samples and 0.5% core share. Fewer than 128 core samples or more than 10% partial-alpha visible samples makes strict evidence indeterminate. Observed design-color counts use groups with at least 1% share; smaller groups remain reported. These are sampled product checks, not exact-pixel, Pantone, CMYK, print-proof or accessibility certification. A tiny accent can be missed. Contrast is guidance for named foreground/background pairs, not a blanket AA logo requirement.

| Selected intent/report | Export behavior |
|---|---|
| Explicit lock, allowed set, required color or maximum count | Strict policy; visual approval and current color evidence are both required |
| Strict report missing, `unverified` or `indeterminate` | `color_review_required`; run `color-analyze` after resolving the reported cause |
| Recomputed strict report is `mismatch` | `color_mismatch`; no final package is published |
| Unrestricted automatic/reference suggestion | Advisory policy; may export with its measured status and limitations |
| Legacy artifact with no structured palette | Color-unverified; do not invent old HEX intent or conformance |

Export verifies original bytes and recomputes evidence. It uses the latest matching report's explicit ROI when one was requested; a regional result must stay labeled regional. Stored statuses or visual booleans cannot authorize a false pass. A successful export appends its fresh report and export record atomically; a failed export preserves prior state and deliveries. If a prior strict report is missing or indeterminate, an explicit fresh analysis is required before export.

Use at most two additional native image edits for one failed color request, each using the exact previous image and preserving requested lettering, shape, layout and background. Retain each actual PNG, final prompt, parent and report. If both repairs fail, report the unresolved restriction and keep the candidates. Do not relax constraints or thresholds, submit a claimed pass, or recolor with Python. A later explicit request to change intent creates a new version.

## Manifest, gallery and package

New exports use manifest schema 2. Alongside the existing source/brief/background facts, inspect:

| Field | Meaning |
|---|---|
| `intended_palette` | Selected artifact's immutable palette, or null for unknown structured intent |
| `color_report` | Fresh report bound to the exported image and intent |
| `color_policy` | `strict`, `advisory` or `unverified` |
| `warnings`, `color_method`, `color_limits` | Actual caveats and the declared measurement policy |
| `lockup_intent` | Selected symbol/text layout and requested typography, or null |
| `font_reference_usage` | `appearance-reference-only` |

The ZIP still contains exactly `logo.png`, `manifest.json` and `brand-guide.md`. Verify the PNG hash against the selected original and the ZIP entry; earlier exports remain unchanged. The guide must distinguish historical brief text, selected palette intent and current measured evidence, including ROI/profile limitations. Do not replace the master with a preview.

`color-gallery` publishes a separate portable HTML directory with only explicitly selected PNGs, palette/report information and appearance references. Check light/dark backgrounds and small/large views, particularly for white transparent lettering. Gallery creation must leave state, selection and PNG hashes unchanged; avoid full prompts, absolute developer paths or private reference images in public output. Gallery success is not export approval or evidence that a native image call occurred. The [project file guide](project-files.md) contains runnable commands and JSON examples.

## Final handoff

Include the selected original PNG, an archive, and a short guide identifying selected palette intent, actual color-report status, exact text, usage notes, and known limitations. Keep historical free-text palette values separate from current structured intent and measurements. Generated typography does not identify a licensed font file. Font sources and requested-reference boundaries are documented in [typography.md](typography.md) and the [font research](../../../docs/research/font-tools.md).

Report actual format, dimensions, transparency, selected version and saved path. Do not promise editable vector paths, outline fonts, EPS/AI, CMYK, physical-print readiness, exclusivity or trademark clearance from a raster image. If the user requests vectors, describe the additional vector reconstruction and validation that would be required.
