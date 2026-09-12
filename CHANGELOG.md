# Changelog

Logo Land's plugin and local helper share one release version. Tagged releases and their notes are available on [GitHub Releases](https://github.com/t1seo/logo-land/releases). See the [release guide](docs/releases.md) for versioning and publication steps.

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
