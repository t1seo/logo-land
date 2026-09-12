# Changelog

Logo Land's plugin and local helper share one release version. Tagged releases and their notes are available on [GitHub Releases](https://github.com/t1seo/logo-land/releases). See the [release guide](docs/releases.md) for versioning and publication steps.

## 0.4.0 — Unreleased

Prepared on 2026-09-13. Publication is withheld because the required restricted-color and white-transparent native samples did not pass after the bounded repair attempts. Source and personal development versions are 0.4.0; the latest published release remains 0.3.1.

### Added

- Automatic, anchor, restricted and reference-derived palettes with composable constraints and immutable version history.
- Local ColorAide calculations, bounded PNG/JPEG reference extraction, sampled color reports and strict export checks.
- Structured horizontal/stacked symbol-plus-text layouts, exact lettering and inherited typography appearance references.
- Font/typography research covering official services, community skills/MCPs and Korean/Latin family references.
- Portable color comparison pages with light/dark and small-size previews.

### Changed

- Session schema 2 reads schema 1 without rewriting it; the first successful mutation preserves an exact v1 backup. Earlier releases cannot read v2 sessions.
- Manifest schema 2 separates intended palettes and requested font appearance from measured raster evidence. Export recomputes color checks while preserving original PNG bytes and the three ZIP payload files.
- English and Korean instructions cover the new color, lockup and migration workflows.

### Compatibility

- Otherwise valid legacy and advisory PNGs remain exportable when optional EXIF color analysis is unavailable. The report records unavailable evidence; strict exports still require determinate conformance, and original-byte integrity checks remain enforced.
- Palette-less reports retain unsupported ICC profile reasons. Newly generated Dark previews use the same `#171717` surface as the default contrast measurements.

Color checks use sampled raster heuristics; they do not certify exact pixels, Pantone/CMYK matching, fonts or accessibility. A font reference describes requested appearance, and no font files or additional MCP server are installed. Native image generation remains the only creation/editing path.

See the [live samples](docs/colors/index.html) and [validation record](docs/qa/color-workflow/README.md) for observed outcomes, limitations and repair attempts.

## 0.3.1 — 2026-09-12

This is the first tagged GitHub release, continuing the internal 0.3.0 plugin builds. Earlier work was distributed through local development installations without release tags. This entry covers the capabilities accumulated before the first tag as well as the release preparation changes; there is no earlier tagged release to compare against.

### Included

- Conversational logo creation with native Codex image generation, eight logo types, concept comparison, and reference-based revisions.
- Transparent PNG generation and background removal, with pixel checks and visual review before export.
- Saved sessions, original image history, and verified PNG, ZIP, and brand guide delivery.
- Ten real logo samples, the Logo Land brand logo, and a transparent logo preview.
- Separate English and Korean READMEs with centered release, feature, and language badges.

### Changed

- English is the default README and plugin presentation language; the Korean README remains available separately.
- The plugin manifest, helper metadata, and lockfile now use the same release version: 0.3.1. The helper previously used 0.1.0; its version now follows the plugin, with no dependency upgrades or runtime changes in the alignment.
- Added a documented versioning and release process.

### Fixed

- Replaced empty sample table headers with explicit brand, logo type, and generated logo columns.
- Made English and Korean documentation badges link to their respective READMEs.

The helper manages files and provenance; image generation requires the native Codex image tool. GitHub source archives are repository snapshots, not plugin installation packages.

See the [release validation record](docs/qa/release-031.md) for checks and their scope. No new image-generation run was performed for this release preparation.
