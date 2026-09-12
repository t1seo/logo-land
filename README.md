# Logo Land

**English** · [한국어](README.ko.md)

<p align="center"><img src="assets/logo.png" alt="Logo Land logo" width="320"></p>

[How we made this logo](docs/brand/README.md)

![Codex Plugin](https://img.shields.io/badge/Codex-Plugin-191917?style=flat-square&labelColor=f6f3ec)
![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-191917?style=flat-square&labelColor=f6f3ec)
![PNG output](https://img.shields.io/badge/Output-PNG-a64b32?style=flat-square&labelColor=f6f3ec)
![English and Korean docs](https://img.shields.io/badge/Docs-EN%20%2F%20KO-191917?style=flat-square&labelColor=f6f3ec)

**Create, refine, and deliver logos through a conversation with Codex.** Describe your brand and the feeling you want, compare concepts, then refine your chosen image into a final PNG with a short brand guide. Logo Land (로고랜드) saves originals and revision history so you can continue in another conversation.

![You and Codex turn a conversation into a brief, generate and revise logos with the native image tool, then review and export a PNG, ZIP, and guide](docs/diagrams/workflow-en.svg)

[Workflow with a text explanation](docs/diagrams/workflow-en.html) · [Gallery of 10 samples](docs/samples/index.html)

GitHub displays HTML links as source code. After cloning the repository, open `docs/diagrams/workflow-en.html` or `docs/samples/index.html` in local Chrome to view the complete pages. The workflow SVG and sample PNGs display directly in this README.

## Get started

Use a Codex environment with access to native image generation and editing. Installing the plugin does not grant access to an unavailable image tool. Local file management requires Python 3.12+ and `uv`; the plugin does not require a separate OpenAI API key or accounts with competing logo services.

### Use the repository directly

```sh
git clone https://github.com/t1seo/logo-land.git
cd logo-land
uv sync --locked
codex
```

In a Codex conversation opened in that folder, ask it to read the skill instructions:

> Read skills/logo-land/SKILL.md and follow it to create a logo. The brand is Goyo, a meditation studio. Show me two calm concepts combining a symbol and the exact Korean text 고요.

### Install as a Codex plugin

The installation command is `codex plugin add`. This repository contains plugin source; it does not provide a public marketplace or a release ZIP as an installation route. You can register the checkout in your own local marketplace:

1. Clone the repository above and note its **absolute path**.
2. Create `.agents/plugins/marketplace.json` inside a separate marketplace folder. Replace `path` below with the checkout's actual absolute path. On Windows, use `/` in the JSON path.

```json
{
  "name": "logo-land-local",
  "plugins": [
    {
      "name": "logo-land",
      "source": {
        "source": "local",
        "path": "/absolute/path/to/logo-land"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

3. Register the marketplace root, the folder containing `.agents`, and install the plugin. Replace the placeholder path with your actual location.

```sh
codex plugin marketplace add /absolute/path/to/local-marketplace
codex plugin add logo-land@logo-land-local
```

4. Open a **new Codex conversation** and start with `$logo-land`. Enable the plugin if your environment requires it.

These commands follow Codex CLI `0.154.0` help for `codex plugin marketplace add --help` and `codex plugin add --help`. Check those help pages if your installed version differs. The [local installation record and verification limits](docs/qa/installation.md) also include records from before the rename.

## Use natural language

You do not need to complete a form before starting. Share the brand name, exact lettering, industry, desired feel, and intended use; Codex asks about the details that matter.

> $logo-land Create a logo for an eco-conscious design studio called Morrow Studio. Show me two concepts with a simple symbol and the brand name.

> Choose the second concept. Keep the shape and lettering, but change the color to navy.

> Make the chosen logo's background transparent, and create a separate icon-only version.

> Resume the saved morrow-live project and export the final PNG.

Concepts are generated as separate images. The default is three directions unless you specify another count. Revisions use the chosen image as their reference. You can also supply an existing logo image to work from.

## Eight logo types

| Type | Form | Example request |
|---|---|---|
| Wordmark | The brand name is the logo | “Use only the Korean name 물결.” |
| Lettermark | Clearly readable initials | “Make the letters NL easy to recognize.” |
| Monogram | Combined or interwoven initials | “Interlock the two L letters into one shape.” |
| Symbol | A recognizable object or pictorial mark | “Use a fern silhouette with no lettering.” |
| Abstract | A concept expressed through shapes | “Suggest upward movement with simple geometry.” |
| Combination | Symbol and lettering together | “Pair the name 고요 with a calm circular symbol.” |
| Emblem | Lettering and a mark inside a badge | “Create a circular badge for a neighborhood bakery.” |
| Mascot | A character represents the brand | “Build the logo around a friendly cat character.” |

Type and style are separate choices. A wordmark can be minimal, serif, or handwritten in appearance. See the [logo direction guide](skills/logo-land/references/logo-directions.md).

## Ten real samples

These fictional brands were generated with the Codex native image tool. The [sample gallery](docs/samples/index.html) and [catalog](docs/samples/catalog.json) contain each request, prompt, review status, and delivered file. The previews below display the actual delivery PNGs at 240px wide.

The samples were created before the Logo Land rename, so their original requests still contain `$logo-generator`. Those records are preserved as created. Start new work with **`$logo-land`**.

| Brand | Logo type | Generated logo |
|---|---|---|
| **01 · LUMA** | Wordmark | <img src="docs/samples/items/01-luma/delivery/logo.png" alt="LUMA wordmark logo" width="240"><br>Black and ivory serif lettering<br>[Original PNG](docs/samples/items/01-luma/delivery/logo.png) |
| **02 · LOOP LAB** | Monogram | <img src="docs/samples/items/02-loop-lab/delivery/logo.png" alt="LOOP LAB monogram logo" width="240"><br>Lime LL monogram<br>[Original PNG](docs/samples/items/02-loop-lab/delivery/logo.png) |
| **03 · 고요** | Combination | <img src="docs/samples/items/03-goyo/delivery/logo.png" alt="고요 combination logo" width="240"><br>Forest green symbol and Korean lettering<br>[Original PNG](docs/samples/items/03-goyo/delivery/logo.png) |
| **04 · BREAD & BLOOM** | Emblem | <img src="docs/samples/items/04-bread-bloom/delivery/logo.png" alt="BREAD &amp; BLOOM emblem logo" width="240"><br>Terracotta bakery badge<br>[Original PNG](docs/samples/items/04-bread-bloom/delivery/logo.png) |
| **05 · KITE** | Abstract | <img src="docs/samples/items/05-kite/delivery/logo.png" alt="KITE abstract logo" width="240"><br>Geometric shapes suggesting ascent<br>[Original PNG](docs/samples/items/05-kite/delivery/logo.png) |
| **06 · MISO** | Mascot | <img src="docs/samples/items/06-miso/delivery/logo.png" alt="MISO mascot logo" width="240"><br>Warm, friendly cat character<br>[Original PNG](docs/samples/items/06-miso/delivery/logo.png) |
| **07 · NORTHLINE** | Lettermark | <img src="docs/samples/items/07-northline/delivery/logo.png" alt="NORTHLINE lettermark logo" width="240"><br>Clear NL initials<br>[Original PNG](docs/samples/items/07-northline/delivery/logo.png) |
| **08 · 물결** | Wordmark | <img src="docs/samples/items/08-mulgyeol/delivery/logo.png" alt="물결 wordmark logo" width="240"><br>Blue Korean lettering<br>[Original PNG](docs/samples/items/08-mulgyeol/delivery/logo.png) |
| **09 · FERN** | Symbol | <img src="docs/samples/items/09-fern/delivery/logo.png" alt="FERN symbol logo" width="240"><br>A distinct botanical silhouette<br>[Original PNG](docs/samples/items/09-fern/delivery/logo.png) |
| **10 · NOVA NOTES** | Combination | <img src="docs/samples/items/10-nova-notes/delivery/logo.png" alt="NOVA NOTES combination logo" width="240"><br>Burgundy art deco identity<br>[Original PNG](docs/samples/items/10-nova-notes/delivery/logo.png) |

## Transparent-background logos

Generate a logo on a transparent background from the start, or remove the background of an existing logo:

> $logo-land Create a logo for Goyo with the exact Korean text 고요. Deliver a transparent-background PNG with no white backing panel or shadow.

> Remove only this logo's background. Keep the lettering, colors, and shape, and deliver a transparent PNG.

Logo Land requests genuine PNG transparency, preserves intentional white foreground details, and checks actual transparent pixels before exporting. You can also request a solid-color background. The same PNG can be previewed on light and dark surfaces without changing its pixels.

<img src="assets/logo-transparent.png" alt="Logo Land logo with a genuinely transparent background" width="400">

[Transparent PNG](assets/logo-transparent.png) · [Light/dark preview](docs/transparency/index.html) · [Generation and verification](docs/transparency/README.md)

This example keeps the original black LAND lettering, so it is best suited to light backgrounds. Ask for a white-lettering variant when needed for dark surfaces.

## Revisions and delivery

Ask for changes to color, letterform appearance, spacing, proportions, symbols, backgrounds, or horizontal and stacked layouts. Each revision sends the selected original to the image tool and records a new image ID with its parent relationship. Earlier images and delivered packages are preserved.

The final delivery includes the **selected PNG, a ZIP, and a short brand guide**. The helper checks actual PNG format, dimensions, visible pixels, hashes, and background requirements. Codex opens the image to review lettering, margins, and recognition at the intended size. Transparent delivery requires actual transparent pixels; an alpha channel alone is insufficient. See the [delivery checks](skills/logo-land/references/delivery-checks.md).

Logos are **raster images**. The plugin does not provide editable SVG/EPS/AI files, vector paths, font files, or CMYK print files. Korean lettering and small text may need further correction, and a requested revision cannot guarantee pixel-for-pixel preservation of other elements. Trademark availability and exclusive rights require separate checks.

## Image generation and the file helper

| Component | Responsibility |
|---|---|
| Codex native image tool | Generate new logo images and edit an existing image using it as a reference |
| Codex conversation | Build the brief, compare concepts, follow the user's selection, and visually review results |
| Local Python helper | Prepare prompts, save sessions and image history, inspect PNGs, and package files |

**Running the helper alone does not generate a logo.** If the image tool is unavailable or fails, the failure and existing work are preserved. Sessions live in `.logo-generator/sessions/<id>/`; the default delivery path is `output/logo-generator/<id>/`.

The `logo-generator` names in these two storage paths are intentional compatibility paths for existing projects. The plugin, skill, and repository use `logo-land`; you do not need to move old project folders because of the rename.

These file management examples run from the repository root. `prompt` prints instructions for the image tool.

```sh
uv sync --locked
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace . --help
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace . init --session demo --brief skills/logo-land/assets/brief.example.json
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace . prompt --session demo --concept 'A simple geometric monogram'
```

To use an installed plugin from another workspace, pass its root to `uv run --locked --project /absolute/path/to/logo-land python ...` and your project folder to the helper's `--workspace` option. The [project file guide](skills/logo-land/references/project-files.md) documents the full commands and JSON formats.

Development checks are available below. Their recorded results are linked in the next section.

```sh
uv run --locked pytest
uv run --locked ruff check .
uv run --locked basedpyright
```

## Research and verification

- [Research and implementation index](docs/README.md)
- [Five-service comparison and product decisions](docs/research/comparison.md)
- [Official feature research](docs/research/official-features.md)
- [Implementation plan](plans/logo-generator.md)
- [Automated check record](docs/qa/helper-tests.md)
- [Background variant checks](docs/qa/background-variants.md)
- [Real image generation and revision verification](docs/qa/live/README.md)
- [Service screenshot gallery](docs/research/gallery.html)
- [Final verification record](docs/qa/final.md)

The research compares Looka, Brandmark, Tailor Brands, Fiverr Logo Maker, and Design.com. They inform the creation workflow; actual logo generation happens in Codex. Research and historical verification documents are primarily in Korean and may retain the earlier project name.

The workflows follow [diagram-design](https://github.com/cathrynlavery/diagram-design/tree/8d8b2993ee2256ee7dfc0eeb3b5713aba3b60792), with a [project-specific style guide](docs/diagrams/style-guide.md) and [document validation record](docs/diagrams/validation.md).
