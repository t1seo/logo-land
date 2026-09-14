# What makes a logo work?

Researched September 14, 2026. This note informs Logopia's
[craft workflow](../../skills/logo-land/references/logo-craft.md) and
[game-title recipe](../../skills/logo-land/references/game-title-logos.md).
It separates published design practice, direct visual observation and our own
implementation choices. It does not certify generated artwork as professional design.

## What the primary sources show

| Source | Published observation | Implication for our workflow |
|---|---|---|
| [Pentagram: Slack](https://www.pentagram.com/work/slack) | The team explored several different forms, then retained the familiar organizing mark while rebuilding it from simple shapes on a grid to improve reproduction across contexts. | Explore different constructions when the requested count allows; connect a shape to the product, then check how its parts reproduce. |
| [Pentagram: Mastercard](https://www.pentagram.com/work/mastercard) | The redesign emphasized the connected circles while preserving existing recognition. The team tested colors against multiple backgrounds and developed a wider identity from the mark's geometry and colors. | Preserve valuable identifying features during edits; assign color roles and judge neighboring colors on the intended surface. Simplification is a project decision, not a universal style. |
| [IBM: 8-Bar](https://www.ibm.com/design/language/ibm-logos/8-bar/) | Positive and reversed versions use different stripe thicknesses and counter points to balance their optical appearance. | Equal numeric dimensions do not guarantee equal visual weight. Inspect gaps, counters and stroke relationships on the actual background. |
| [Google: Evolving the identity](https://design.google/library/evolving-google-identity) | The compact G has more visual weight than the logotype letter and optical refinements where its curve meets the crossbar. The system was tested across sizes and applications. | Review at intended display size. A compact alternate can require its own construction rather than simply shrinking a full name. |
| [Design Council: Framework for Innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/) | The Double Diamond alternates broad exploration with focused decisions and uses small-scale testing and iteration. | Use the supplied brief, develop meaningful alternatives when appropriate, then refine a selected direction against observed defects. A single-image request does not need extra candidate rounds. |
| [Apple: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons) | Apple recommends a recognizable core idea, few essential shapes, care at small sizes and consistent identifying features across appearances. Its platform workflow also distinguishes artwork from layers, masking and system effects. | Keep an icon's key contour readable in small previews. A PNG sample is artwork, not proof of an Icon Composer package or store-ready implementation. |

The last column is our synthesis. These projects support a process of contextual
decisions and visible refinement; they do not establish a universal aesthetic score,
required color count, compulsory monochrome test or guarantee of audience recognition.

## The actual Pokopia reference

We inspected the [official logo image](https://pokopia.pokemon.com/assets/en-us/pages/index/logo-pokopia.png)
linked by the [Pokémon Pokopia website](https://pokopia.pokemon.com/en-us/). The lower
title has lowercase multicolor letters, varied rotations and heights, broad white
keylines, angular facets, shallow offset depth and an irregular lime backplate with a
geometric pattern. This is a direct visual description, not a claim about the original
designer's process or intent.

The reusable recipe is controlled letter rhythm, clear outline hierarchy, color roles
and a supporting backplate. Each new title needs its own exact text and letter
construction. The source's parent-brand title and mascot-specific glyph details are
not necessary to use those broader attributes. The official image is a linked research
reference; it is not bundled as a Logopia sample or new deliverable.

In the existing model, a shared backplate makes this an `emblem`. Lettering with no
plate is a `wordmark`; an independent motif plus lettering is `combination`. These are
Logopia's routing decisions, not categories attributed to the source designers.

## The resulting skill changes

The assistant now connects audience meaning to a named construction before prompting,
uses references through observable features, and checks actual returned images for
optical spacing, counters, hierarchy and intended-size readability. A targeted native
edit names a visible defect and the features to preserve; its child keeps the original
as a parent. Review notes describe what was observed, without claiming consumer
testing, font files, vectors or ungenerated alternate versions.

For the refreshed showcase, the user's white-background request means an opaque
#FFFFFF exterior in each original PNG. A colored emblem plate remains foreground.
Composition-specific empty regions are declared before generation and sampled after
it; full-image inspection checks the remaining visual background. Those samples cannot
establish the color of every background pixel. White remains this collection's
requirement, not a new global default for future logos or icons.
