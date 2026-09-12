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

## Final handoff

Include the selected original PNG, an archive, and a short guide identifying palette intent, exact text, usage notes, and known limitations. Treat palette values in the brief as intended design values unless actual sampled colors were verified. Generated typography does not identify a licensed font file.

Report actual format, dimensions, transparency, selected version and saved path. Do not promise editable vector paths, outline fonts, EPS/AI, CMYK, physical-print readiness, exclusivity or trademark clearance from a raster image. If the user requests vectors, describe the additional vector reconstruction and validation that would be required.
