# Logo Land v0.3.1 release plan

## Objective

Publish the first tagged release, make English the default project presentation, and place linked release and language badges at the top of both root READMEs.

## Decisions and review

Continue the existing internal 0.3.0 plugin version with v0.3.1. Track the same 0.3.1 version in the plugin manifest, helper metadata, and lockfile. Personal installation cachebusters are local metadata. Preserve the separate Korean README, actual sample lettering, historical records, repository visibility, and existing installation method. No new runtime features or CI are needed.

The independent planning review required a real release link, an explanation of the first tag's version, no comparison against a nonexistent tag, a current installation record, and verification of the exact tagged commit. These are included below.

## Work and verification

1. Update `README.md` and `README.ko.md`: center all badges in the first HTML paragraph; link separate English/Korean badges and a v0.3.1 badge. Keep English labels and narrative in the default README. Verify the first rendered block, badge/link counts, local paths, and the unchanged ten sample images. Fail if a badge links to a missing language file.
2. Update `.codex-plugin/plugin.json`, `pyproject.toml`, and `uv.lock` to 0.3.1. Use English plugin descriptions and starter prompts. Add `CHANGELOG.md` and `docs/releases.md` for release history and the manual version/tag process. Verify all three versions agree, the manifest validates, and `uv lock --check` passes. Reject dependency drift or a tracked cachebuster suffix.
3. Run the existing test suite, Ruff, and basedpyright. Validate document links and release notes. These checks must pass before publication; no new tests are needed for presentation-only changes.
4. Sync the existing personal plugin source, run the official cachebuster helper, reinstall, and record the actual local version in `docs/qa/installation.md`. Recheck that the repository version is still 0.3.1. A failed install must be reported without claiming it succeeded.
5. Review and commit the authorized files, push `main`, publish an annotated `v0.3.1` tag and an English GitHub release at that exact commit, and update the GitHub About description to English. Verify the release is published/latest, both remote refs resolve to the tested commit, the worktree is clean, and the repository visibility is unchanged. Do not overwrite an existing tag or release.

## Dependencies and completion

Steps 1–2 precede 3; step 4 follows the validated metadata; step 5 follows all checks. Completion requires the centered linked badges, versioned release, English default presentation, current local installation record, and verified remote commit/tag. Publication is authorized by the user's request; it does not require a separate confirmation.
