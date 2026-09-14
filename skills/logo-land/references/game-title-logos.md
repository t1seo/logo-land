# Expressive game-title lettering

Use when the user wants a colorful game title, outlined sticker-like lettering or a
specific title-logo reference. This is a construction recipe using existing fields,
not a new preset, font installation or separate rendering service.

## Inspect and route the reference

The inspected [official Pokopia artwork](https://pokopia.pokemon.com/assets/en-us/pages/index/logo-pokopia.png)
on the [Pokémon Pokopia site](https://pokopia.pokemon.com/en-us/) has lowercase letters
in several bright colors, individually varied rotations and heights, broad white
outlines, angular color facets, shallow offset depth and a lime patterned irregular
backplate. These are direct visual observations. The source also contains a separate
parent-brand title and character-specific letter details; those are not needed to
adopt its general rhythm, color or layering for another name.

| Requested structure | Existing `logo_type` and intent |
|---|---|
| Lettering sits on one shared decorative badge/backplate | `emblem`; keep `lockup` null unless a separate symbol/text layout is actually requested. |
| Expressive letters and their outlines/depth, without a shared plate or separate symbol | `wordmark`; keep `lockup` null. |
| An independent mascot or motif accompanies the title | `combination`; use the actual horizontal/stacked symbol/text lockup. |

A keyline following each glyph is not by itself a badge. A shared decorative silhouette
behind the whole title is. Route from the intended composition, not the phrase “text
logo.” A different reference may call for a different recipe; inspect it instead of
applying Pokopia's features to every game.

## Construct a new title

1. **Letter skeleton first.** Use `exact_text` verbatim, including case, spacing,
   punctuation and Hangul. Choose broad letter bodies and sufficient counters for the
   intended title size. If case was not supplied and the user delegated the design,
   record the chosen spelling in the brief before generating; do not silently change
   an existing exact string because the reference happens to be lowercase.
2. **Controlled rhythm.** Choose a readable variation in letter rotation, baseline
   and width. Keep a coherent stroke family and reading order. Avoid tangencies where
   a rotated letter nearly touches another or an outline closes a counter.
3. **Outline hierarchy.** A broad keyline can separate adjacent letter colors and
   unite the title. A narrow darker edge or shallow offset can add depth when useful;
   keep it subordinate to the face of the letters and inside the artwork's clear space.
4. **Purposeful color.** Assign colors to letters or letter groups and use limited
   angular facets within them when requested. Make the boundary and face readable
   before texture. Honor existing color locks/counts and gradient policy; adapt or
   omit facets rather than adding colors forbidden by the user's intent.
5. **Backplate when requested.** Give the plate a broad, deliberate contour that
   supports the word rather than becoming a scene. A quiet geometric pattern can
   add atmosphere at title size; keep enough separation from the letters. A lime plate
   is one reference-led choice, not a mandatory game-logo palette.

For example, a fictional exploration game with user-supplied `exact_text="Wonder Bay"`
can use `logo_type="emblem"`, styles such as `playful`, `outlined`, `faceted`, and:

> A welcoming discovery-game title: broad custom letters with open counters and a
> measured up-and-down rhythm; a thick white keyline unites the colored letter faces,
> restrained angular facets add playful depth, and one shallow offset sits behind the
> letters. A broad irregular backplate supports the complete name, with a quiet
> low-contrast geometric pattern. Keep Wonder Bay readable at 360px wide.

The example is descriptive input, not an extra schema. Supply the user's actual colors
and background separately through the brief and effective palette. A title requested
on white needs opaque #FFFFFF exterior canvas with no scene or exterior shadow; the
colored plate, if requested, remains part of the foreground. Other briefs retain their
chosen opaque color or actual transparent background.

Do not import a reference's literal title, exact letter contours, character faces or
recognizable mascot-shaped counters unintentionally. Build the new name's own letter
relationships. Avoid a global ban list containing unrelated franchise names; exclusions
should address the current reference and actual user request.

## Review at title size

Check every required character before assessing style. At the intended width, inspect
whether thick outlines swallow counters, shallow depth doubles a letter, facet lines
look like cuts, or the pattern competes with the name. For Hangul, inspect each syllable
block's component arrangement rather than replacing it with pseudo-letter shapes.
Inspect the white exterior separately from a colored plate.

Record specific limits: “The title reads at 360px; the plate pattern merges at 128px”
does not establish a 32px app icon. If a compact companion is requested, create and
inspect it as a separate variant with the appropriate logo/icon intent. Correct required
spelling, background or clipping failures with a targeted native edit of the actual
parent, preserving successful letter shapes and color relationships. See
[lettering.md](lettering.md#inspect-the-lettering) and [logo-craft.md](logo-craft.md#inspect-and-refine).
