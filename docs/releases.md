# Releases and versioning

Logo Land uses `MAJOR.MINOR.PATCH` versions and Git tags named `vMAJOR.MINOR.PATCH`. The plugin and local helper are released together. The first tagged release is [v0.3.1](https://github.com/t1seo/logo-land/releases/tag/v0.3.1), continuing the earlier internal 0.3.0 plugin builds.

Current source is **0.5.0, unreleased**, for the [app icon artwork update](../plans/logo-land-app-icons.md). The published release remains **0.3.1**. The prior **0.4.0 draft remains unpublished** because its required native color samples failed; this update does not rename its gates, erase failure records or publish/retarget that draft. See the [historical validation](qa/color-workflow/README.md). All sixteen app icon originals now have verified native receipts, gallery hashes and [Chrome comparison evidence](qa/app-icons/quality-comparison.md). This development task does not authorize public release publication.

The helper's earlier 0.1.0 metadata is aligned to 0.3.1 with this first tag. Initial release notes summarize existing capabilities and release preparation changes; do not link a comparison against a nonexistent v0.3.0 tag.

## Choosing a version

| Change | Version increment |
|---|---|
| Fixes, documentation, presentation, or metadata without an incompatible behavior change | Patch, such as 0.3.1 → 0.3.2 |
| New functionality during the 0.x development series | Minor, such as 0.3.1 → 0.4.0 |
| Incompatible changes during the 0.x series | Minor, with migration instructions in the release notes |
| A stable public compatibility contract | 1.0.0; later incompatible changes increment the major version |

After 1.0.0, compatible new functionality increments the minor version and compatible fixes increment the patch version. Do not move or replace a published tag; publish another version for corrections.

## Preparing a release

1. Set the same clean version in `.codex-plugin/plugin.json` and `pyproject.toml`, then run `uv lock` to update the helper entry in `uv.lock`. Do not upgrade dependencies as part of a version-only change.
2. Update both root README badges and links, add an entry to [CHANGELOG.md](../CHANGELOG.md), and prepare English release notes. The Release badge must continue to identify the actual published release; the Development badge identifies current source, even while unreleased. Keep the default README and GitHub About description in English. Link generated samples only after their native receipts and actual files exist.
3. Run `uv lock --check`, `uv run --locked pytest`, `uv run --locked ruff check .`, and `uv run --locked basedpyright`. Validate the plugin manifest using the installed `plugin-creator` skill's `scripts/validate_plugin.py`. Check the README badge links and sample images.
4. When validating a personal installation, sync the existing personal plugin source, apply its local cachebuster, reinstall, and update the [installation record](qa/installation.md) with the returned version. Recheck that the repository version remains clean. Record release checks with their execution source, as in the [v0.3.1 validation record](qa/release-031.md).
5. Review and commit the release files on `main`, then push the commit. Create an annotated tag at the exact validated commit and push that tag. Publish with `gh release create`, `--verify-tag`, an English `--title`, and `--notes-file` pointing to the prepared notes.
6. Verify that the remote `main` and peeled tag refer to the validated commit, that GitHub reports the release as published and latest, and that the worktree is clean. Record the checks without claiming an image was generated during a documentation-only release. Keep repository visibility unchanged.

Before creating a tag or release, check whether the intended version already exists. If it does, inspect it and select a new version for new changes. Do not overwrite it.

## Local plugin installations

Personal development installations may use a version such as `0.5.0+codex.<timestamp>` to refresh the Codex cache. Apply the official cachebuster helper to the personal plugin source and reinstall it from its existing marketplace. Keep the repository manifest, `pyproject.toml` and `uv.lock` at clean `0.5.0`; create a release tag only through a separately authorized publication workflow. The cachebuster is not a separate public release. Existing installations can retain an older payload until refreshed, so record source and installed-cache versions/hashes separately rather than inferring one from the other.

Open a new Codex conversation after reinstalling so the updated plugin is discovered. The [installation record](qa/installation.md) distinguishes release versions from local cache versions.

## Using a release

Check out a tag in the cloned repository, then follow the [English installation instructions](../README.md#install-as-a-codex-plugin) or [Korean instructions](../README.ko.md#codex-플러그인으로-설치). GitHub's automatic ZIP and tar.gz downloads contain source snapshots. They do not replace the documented local marketplace installation process.
