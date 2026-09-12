# Release README presentation QA

Date: 2026-09-12 (Asia/Seoul). Scope: `README.md` and `README.ko.md` for v0.3.1.

## Change

Corrected one English cross-reference: after the new release section was inserted, “the next section” no longer pointed to the verification records. The sentence now links directly to `#research-and-verification`. The coordinator's existing badge and release edits were preserved; this worker made no changes to the Korean README.

## Checks and results

| Check | English | Korean |
|---|---|---|
| First source and rendered block | Centered paragraph before H1 | Centered paragraph before H1 |
| Badge images in that paragraph | 6 | 6 |
| Linked release badge | `t1seo/logo-land/releases/tag/v0.3.1` | Same target |
| Linked language badges | `README.md`, `README.ko.md` | Same targets |
| Distinct local file targets, with exact filename case | 38 exist | 38 exist |
| Sample previews and catalog matches | 10, each 240px wide | 10, each 240px wide |

- Refreshed both files through `gh api --method POST markdown -F text=@<README> -f mode=gfm`; both requests exited successfully. Inspected the resulting HTML with jsdom from `/tmp/logo-gallery-qa/node_modules/jsdom`.
- Verified the six rendered badge URLs match the source, retain `flat-square` and `labelColor=f6f3ec`, and preserve their release/language destinations. Each rendered document has exactly one H1.
- Checked every rendered local image/link target for existence and exact filename case, including both READMEs, changelog, release guide, workflow files, historical records, and sample PNGs. The new English fragment link matches the “Research and verification” heading.
- Matched all ten preview paths, brand names, and English logo types to `docs/samples/catalog.json`; each row retains its original PNG link and nonempty alt text. All ten English sample descriptions are English. The only Hangul remaining in the English source is the intentionally preserved brand text `고요` and `물결`.
- Read both narratives; confirmed the default README uses English instructions and the English workflow, while the alternate uses Korean instructions and the Korean workflow. Historical documentation, sample requests, and images were not translated or changed.
- Parsed the supplied release SVG (`Release: v0.3.1`, 98×20) and English Korean-language badge SVG (`Docs: Korean`, 86×20). Also fetched and parsed the Korean README's localized Shields endpoint successfully (`Docs: 한국어`, 80×20).
- `git diff --check -- README.md README.ko.md` passed.

## Evidence and limits

GitHub Markdown API HTML: `/tmp/logo-land-readme-release-en.html` and `/tmp/logo-land-readme-release-ko.html`. Supplied badge evidence: `/tmp/logo-land-release-badge.svg` and `/tmp/logo-land-korean-badge.svg`.

Source SHA-256 at verification:

- `README.md`: `23dc038698afa0f81254e7061e2a575ea4d14a60fbc6e65561ead6bd6fab2e4a`
- `README.ko.md`: `55ab9ca2baeeb04b62efe75d0c0c5e3bcbf8bb58188c8c84658171e56ebb5b6b`

No unresolved README issue was found within these checks. This was source, Markdown API HTML/DOM, filesystem-link, and badge-SVG inspection; no browser visual QA, screenshots, responsive layout inspection, or image-content review was performed. Release URL structure and version text were checked, but publication and live release availability were not checked. No application code changed, so application tests and builds were not run for this task.
