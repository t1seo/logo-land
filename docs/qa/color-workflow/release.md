# Development commit and unpublished release record

Date: 2026-09-13 KST. **The implementation is committed and pushed to main. v0.4.0 remains an unpublished draft, not a public release.**

| Item | Observed result |
|---|---|
| Implementation commit | [`b391ca8e2b463589efc870ff478a51b9f5f6f32c`](https://github.com/t1seo/logo-land/commit/b391ca8e2b463589efc870ff478a51b9f5f6f32c) |
| Push | `origin/main` advanced from `fd1d89c` to `b391ca8`; the remote ref was read back and matched. |
| Source version | Plugin manifest, Python project and locked helper package: `0.4.0` |
| Personal installed version | `0.4.0+codex.20260912161802`; 55 files, source-equal except the manifest cachebuster |
| GitHub draft | Release ID `387630647`, `tag_name=v0.4.0`, `draft=true`, `published_at=null` |
| Draft target | The tested implementation commit `b391ca8e2b463589efc870ff478a51b9f5f6f32c` |
| Public tags | No `v0.4.0` ref exists. Existing `v0.3.1` remains unchanged and peels to `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`. |
| Published release | `v0.3.1` remains the latest published release. |
| Repository presentation | `t1seo/logo-land`, default branch `main`, visibility `PUBLIC`, English About text |

The [maintainer draft](https://github.com/t1seo/logo-land/releases/tag/untagged-0044a49035267a9661c7) contains the English [release notes](release-notes.md). It was created with `--draft --latest=false` and the exact implementation commit target. GitHub reports it as unpublished; the remote tag list independently confirms that no v0.4.0 tag was created. Drafts require repository push access to appear in release listings, so this is not a public download link. [GitHub release API documentation](https://docs.github.com/en/rest/releases/releases#list-releases).

This audit record is a subsequent documentation-only commit. Its addition can advance main beyond the implementation commit; the draft deliberately retains the tested implementation target. No source, plugin payload, generated image or export is changed by recording publication evidence.

## Verification at the implementation checkpoint

- **315 tests passed**, with clean Ruff, basedpyright, formatting and locked dependencies. The [validation index](README.md) distinguishes the final checks from earlier checkpoints.
- Five independent Orca reviews completed. Their C1 legacy-export and G3 preview findings were corrected and independently rechecked; see [review integration](review-summary.md).
- The final installed helper executed **29 calls**, with 27 successes and two expected strict refusals. See [installed-cache evidence](installation-040-final.md).
- Eight native requests, 16 new native outputs and the reused parent are preserved. NORTHLINE, GROVE and TIDE have approved deliveries; the other outcomes remain explicit. See [native results](native-cases.md).
- Chrome QA recorded 46 screenshots, real controls/links and three matching downloads. The task's Chrome tab was left on the persistent local `docs/colors/index.html` page. See [Chrome evidence](chrome-live.md).
- Captured trailing spaces in five guide/log files are preserved; the authored-file staged whitespace check passes. See the [exact exception](whitespace.md).

## Why publication remains blocked

The plan requires approved restricted-color and white-transparent native outputs. These remain indeterminate or unsuccessful after the two permitted repairs per affected request. The final white preview looks clean in Chrome, but still exceeds the unchanged partial-alpha policy. Source tests, successful anchor cases and an unpublished draft do not satisfy those native requirements.

No further image calls, threshold relaxation, programmatic pixel repair or public release publication were performed to close that gap. T8, overall verification acceptance and T9 therefore remain incomplete. The development source and local installation are available with that limitation stated explicitly.

Read-back commands used after the push and draft creation:

```sh
git ls-remote origin refs/heads/main 'refs/tags/*'
gh release view v0.4.0 --repo t1seo/logo-land \
  --json tagName,isDraft,isPrerelease,publishedAt,url
gh api repos/t1seo/logo-land/releases \
  --jq '.[] | select(.tag_name=="v0.4.0") | {id,target_commitish,draft,published_at,html_url}'
gh repo view t1seo/logo-land \
  --json name,url,description,visibility,defaultBranchRef
```

Selected observed fields are saved in [release-state.json](release-state.json). Existing release tags, repository visibility, historical samples and native originals were preserved.
