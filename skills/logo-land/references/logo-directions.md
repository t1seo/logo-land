# Logo directions

Use these categories to help the user choose. They are design directions for native image generation, not promises of vector or font-layer output.

| `logo_type` | Meaning | Useful guidance |
|---|---|---|
| `wordmark` | Brand name is the logo | Build identity into the exact letters' silhouette, counters, spacing and readable joins; no separate unsolicited icon. |
| `lettermark` | Supplied initials as distinct readable letters | Confirm the literal initials; stacked or side-by-side arrangement does not imply interweaving or a symbol. |
| `monogram` | Interwoven or integrated supplied characters | Use deliberate shared strokes or interlocks while keeping each character identifiable; do not invent an acronym. |
| `symbol` | Recognizable pictorial mark | Establish the subject; an icon-only output may use empty `exact_text`. |
| `abstract` | Nonliteral geometric or organic mark | Tie shape and negative space to a concept without relying on stock motifs. |
| `combination` | Symbol plus exact brand text and any requested slogan | Record horizontal/stacked layout, symbol position, text alignment and typeface appearance; inspect symbol/text balance. |
| `emblem` | Text integrated into a badge, seal or shared decorative backplate | Keep borders, pattern and lettering distinct at the intended size; a game-title plate can have an irregular silhouette. |
| `mascot` | Character represents the brand | Clarify expression, personality and detail level; keep a compact silhouette. |

Styles are a separate list: minimal, geometric, organic, playful, elegant, premium, vintage, hand-drawn, bold, futuristic, or another user-defined direction. Avoid describing a type as universally suitable for an industry. Intended use matters more than a category label.

For natural Korean/English text-logo requests, read [lettering.md](lettering.md).
It routes full names, readable initials and integrated initials, then gives construction
guidance for playful sculpted, forward-slanted athletic and geometric stacked lettering.
These use existing `exact_text`, `styles` and `concept`; they are not additional types.

For expressive titles, use [game-title-logos.md](game-title-logos.md): lettering on a
shared plate is an emblem, lettering alone is a wordmark, and an independent motif
plus title is a combination mark. Per-letter keylines are not themselves a badge.

Combination marks are existing functionality. Their structured layout and typography intent make requested variants and later inheritance explicit; see [typography.md](typography.md). A wordmark does not gain an icon unless requested, and an icon-only variant does not fulfill required lettering. Color direction is independent of logo type: use [color-workflow.md](color-workflow.md) for composable anchor/reference/count constraints and preserve one selected palette per requested concept.

## Conversation routes

**Guided:** “상호와 어떤 일을 하는 브랜드인지 알려주세요.” After the answer, ask one concise question about audience or style only if it will materially change the result. Summarize the brief and generate when authorized.

**Complete brief / quick start:** Extract all supplied fields, record modest assumptions and generate directly. Do not run a fixed questionnaire just because competing sites do.

**Reference-led:** Identify which image is a style reference, an existing logo, or a sketch. Ask only if the role cannot be inferred. Use the source as a tool input, not a verbal guess about its contents.

Read [logo-craft.md](logo-craft.md) to extract observable reference traits, connect the
brief to a distinguishing construction and inspect that construction at its intended
size. A professional-looking result requires visible judgment, not a promise attached
to adjectives such as “premium” or “timeless.”

**Explore:** Offer genuinely different design concepts, for example typographic, geometric-symbol, and organic-symbol. If these use different logo types, create separate briefs/sessions or retain the concept's true type in its saved prompt; do not silently mislabel the resulting artifact.

For a lettering-only request, keep exploration within letters: vary silhouette,
proportion, counters, kerning or legible joins. Do not substitute symbol concepts for
the requested wordmark or present the same typesetting recolored as distinct concepts.

**Revise / extend:** Start from the selected artifact. Handle one targeted request or a clearly specified set of changes. Monochrome, reversed, lockup variations, and avatar variants reuse the chosen identity as an input.

## Korean lettering

Preserve the exact Hangul, spacing, English capitalization, and punctuation in both brand and slogan. Check the actual image against both source strings, including after a horizontal/stacked or color-only edit. If text remains wrong after a targeted correction, report it; a text-free mark plus separately typeset wordmark is a separate user-selected workflow requiring suitable fonts and verification. Do not label the image final while required lettering is wrong or claim that a generated font-like appearance proves use of a font file. See [typography.md](typography.md) for the detailed workflow.

## Avoiding generic outputs

Use the brand's actual differentiator and requested tone. Specify silhouette and composition rather than adding decorative adjectives. Do not copy competitors' sample logos or copyrighted screenshots into the user's deliverable. Research informs interaction design; it is not a library of assets to resell.
