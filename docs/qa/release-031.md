# Logo Land v0.3.1 release validation

Date: 2026-09-12. Scope: pre-publication metadata and release prose in the shared worktree, compared with baseline commit `ab1d4b04f88274c8525f9942f194eb5a6c5daa62`. This record does not attest a published tag or the final release commit.

## Execution provenance

The coordinator supplied the live Orca Run `run_84598bb28609` and its three parallel assignments:

| Responsibility | Task | Dispatch |
|---|---|---|
| README validation | `task_cbf6d2ddbf19` | `ctx_47027bb9960a` |
| Release metadata and notes (this review) | `task_2cfae99662e7` | `ctx_9d79562cd92b` |
| Installation record | `task_46bbf3f3c823` | `ctx_67e2118a93c3` |

Publication task `task_f35228673764` depends on all three. The earlier planning review used a native subagent before Orca orchestration was requested; it was not an Orca worker.

## Independently executed checks

| Check | Result |
|---|---|
| Parsed `.codex-plugin/plugin.json`, `pyproject.toml`, and `uv.lock` | All three release versions are exactly `0.3.1`, without a local cachebuster suffix. |
| Parsed project comparison against baseline | After normalizing only `project.version`, the entire TOML structure is unchanged. Runtime and development dependency declarations are unchanged. |
| Parsed lockfile comparison against baseline | After normalizing only the `logo-land-helper` version, the entire lock structure is unchanged. All 21 third-party package records, including sources, hashes, and artifacts, are identical; there are 22 packages including the helper. |
| Manifest presentation and interface | All 10 checked description, interface label, and starter-prompt strings are nonempty English ASCII text. Four starter prompts are present; the first invokes `$logo-land`. Skills and logo paths exist, the brand color matches `#RRGGBB`, and capabilities remain an empty array. |
| `uv lock --check` | Passed; resolved 22 packages in 20 ms. |
| `git diff --check` | Passed. |
| `git tag --list` and `git ls-remote --tags origin` | Both returned no tags at review time. |
| `gh release list --repo t1seo/logo-land --limit 10 --json tagName,isDraft,isPrerelease,publishedAt` | Returned `[]` at review time. |
| Release-document links and whitespace | Passed across all four owned documents; 13 local or tag-mapped links resolve to local files, including both installation anchors. No nonexistent-tag comparison links are present. |
| GitHub Markdown rendering of release notes | Passed through `gh api markdown` in GFM mode. Inspected the rendered text, four section headings, and exact tag-specific installation link; the validation attribution and no-new-image-run statement are preserved. |

The metadata diff changes the plugin from internal `0.3.0+codex.20260912135514` to `0.3.1` and the helper from `0.1.0` to `0.3.1`. The helper and dependency lock now follow the plugin release version. The first tag therefore has no earlier tagged release for a comparison link.

## Coordinator-run evidence

The coordinator reported the following freshly completed checks in this worker's dispatch. These are coordinator-run results, not a second execution by this metadata reviewer.

| Check | Coordinator-reported result |
|---|---|
| Existing full test suite | **96 passed in 39.70s** |
| Ruff | **All checks passed!** |
| basedpyright | **0 errors, 0 warnings, 0 notes** |
| `uv lock --check` | Passed |
| Official plugin validator | Passed |

This worker changed release documentation only. No runtime source or tests were changed in the reviewed release diff, so the full suite was not repeated.

## Release prose and limits

- The changelog and release notes cover existing conversational logo creation, eight logo types, reference-based revisions, saved history, verified PNG/ZIP/brand-guide delivery, and transparent-background generation or removal.
- The release preparation changes are centered release and language badges in the English and Korean READMEs, English default presentation, aligned versions, and release documentation. Existing sample artwork and its Korean lettering remain existing examples.
- The release notes point to the tag-specific [Codex plugin installation instructions](https://github.com/t1seo/logo-land/blob/v0.3.1/README.md#install-as-a-codex-plugin). The target section exists in the local README; the tag-specific URL requires publication.
- No image-generation call was made during this release preparation. Generation and editing still require the host's native Codex image tool; the helper manages prompts, provenance, checks, and files. Earlier live-image evidence is available in the [live QA record](live/README.md) and [transparency record](../transparency/README.md).
- GitHub source archives are repository snapshots, not plugin installation packages. Installation continues through the documented local marketplace route.

## Handoff

English GitHub release notes are prepared in `/tmp/logo-land-release-notes.md`. The coordinator owns the current personal installation record, README rendering checks, final commit review, publication, and verification that remote `main` and the peeled `v0.3.1` tag identify the exact validated commit. Confirm the published/latest release state, working tree cleanliness, and unchanged repository visibility after publication; none is claimed by this pre-publication review.
