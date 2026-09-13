<p align="center">
  <a href="https://github.com/t1seo/logo-land/releases/tag/v0.3.1"><img src="https://img.shields.io/badge/Release-v0.3.1-191917?style=flat-square&amp;labelColor=f6f3ec" alt="Release v0.3.1"></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/Development-v0.6.0-a64b32?style=flat-square&amp;labelColor=f6f3ec" alt="Development version 0.6.0; unreleased"></a>
  <img src="https://img.shields.io/badge/Codex-Plugin-191917?style=flat-square&amp;labelColor=f6f3ec" alt="Codex Plugin">
  <img src="https://img.shields.io/badge/Python-3.12%2B-191917?style=flat-square&amp;labelColor=f6f3ec" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/Output-PNG-a64b32?style=flat-square&amp;labelColor=f6f3ec" alt="PNG output">
  <a href="docs/README.md"><img src="https://img.shields.io/badge/Docs-English-191917?style=flat-square&amp;labelColor=f6f3ec" alt="English documentation"></a>
  <a href="docs/README.ko.md"><img src="https://img.shields.io/badge/Docs-Korean-191917?style=flat-square&amp;labelColor=f6f3ec" alt="Korean documentation"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="docs/README.md">Docs</a> · <a href="docs/gallery.md">Gallery</a>
</p>

# Logo Land

<p align="center"><img src="assets/logo-land-studio.png" alt="Logo Land open-frame symbol and LOGO LAND wordmark" width="200"></p>

**Create logos and app icon artwork through a conversation with Codex.**

<a id="samples"></a><a id="ten-real-samples"></a><a id="transparent-background-logos"></a>

[**See every original in one visual gallery →**](docs/gallery.md)

Click an image to open its original PNG.

<p>
  <a href="docs/samples/items/03-goyo/delivery/logo.png"><img src="docs/samples/items/03-goyo/delivery/logo.png" width="160" alt="고요 · Korean combination logo"></a>
  <a href="docs/gallery-workflow/images/common-v1.png"><img src="docs/gallery-workflow/images/common-v1.png" width="160" alt="COMMON · shared-workspace logo"></a>
  <a href="docs/samples/items/06-miso/delivery/logo.png"><img src="docs/samples/items/06-miso/delivery/logo.png" width="160" alt="MISO · mascot"></a>
</p>

<p>
  <a href="docs/app-icons/images/ip-a1.png"><img src="docs/app-icons/images/ip-a1.png" width="160" alt="Reading owl · IP character"></a>
  <a href="docs/app-icons-quality-v1/images/pictogram-quality-v1.png"><img src="docs/app-icons-quality-v1/images/pictogram-quality-v1.png" width="160" alt="Weather · revised pictogram"></a>
  <a href="docs/gallery-workflow/images/relay-v2.png"><img src="docs/gallery-workflow/images/relay-v2.png" width="160" alt="Relay · abstract refinement with a wider opening"></a>
</p>

<a id="get-started"></a><a id="use-the-repository-directly"></a><a id="image-generation-and-the-file-helper"></a>

## Installation

Requires Codex native image generation/editing, Python 3.12+ and uv; plugin installation does not enable a missing image tool.

```sh
git clone https://github.com/t1seo/logo-land.git
cd logo-land
uv sync --locked
codex
```

In this checkout, ask Codex to read [skills/logo-land/SKILL.md](skills/logo-land/SKILL.md), then use an example below.

<a id="install-as-a-codex-plugin"></a>

To enable `$logo-land` in other projects, follow the [full plugin installation guide](docs/installation.md).

<a id="releases-and-versioning"></a>

This checkout is **v0.6.0 development**; the published release is [v0.3.1](https://github.com/t1seo/logo-land/releases/tag/v0.3.1).

<a id="use-natural-language"></a>

## Try it

> $logo-land Create two calm logo concepts for Goyo, a meditation studio, combining a simple symbol with the exact Korean text 고요.

> $logo-land Create six independent IP character candidates for my reading app, using three product-related directions. Choose the colors for me.

> Compare the candidates from my projects in one gallery, with app-home, website-header and 16px previews. Keep the chosen design’s shape and widen only its opening.

<a id="six-app-icon-directions"></a><a id="choose-colors-in-four-ways"></a><a id="pair-a-symbol-with-exact-lettering"></a><a id="eight-logo-types"></a><a id="revisions-and-delivery"></a>

## What you can make

- **Eight logo types:** wordmarks, lettermarks, monograms, pictorial marks, abstract marks, combination marks, emblems and mascots.
- **Six app icon styles:** IP characters, pictograms, abstract forms, monograms, soft 3D and pixel art.
- **Colors and lettering:** choose palettes, request exact brand text, and arrange a symbol beside or above it.
- **Refine and resume:** revise a chosen image, return to saved projects, and export reviewed logos as PNG, ZIP and a short brand guide.

Outputs are raster PNGs; editable vectors and font files are not included. Font names are visual references. App icon artwork requires separate platform preparation.

<a id="research-and-verification"></a>

## Credits

IP character guidance is adapted from [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill). See the [pinned adaptation reference](skills/logo-land/references/ip-mascot.md), [MIT license notice](skills/logo-land/assets/ip-as-logo.LICENSE), and [third-party notices](THIRD_PARTY_NOTICES.md).

[Documentation](docs/README.md) · [Changelog](CHANGELOG.md) · [Get help](https://github.com/t1seo/logo-land/issues)
