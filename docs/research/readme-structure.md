# Logo Land README structure decision

Research-only handoff for `task_afd0760f6417` / `ctx_f5fa76030bf5`, observed 2026-09-13 KST (2026-09-12 UTC), branch `main`, HEAD `ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5`. The shared tree is dirty; [baseline hashes and HTTP evidence](../qa/app-icons/readme-ia.md) identify the actual files read. No README, skill, gallery or image was changed by this task.

## Decision and evidence

Make the README a short entrance: identity, what the plugin does, a working start path, three useful requests, capabilities, sample links and explicit adaptation credit. Give every showcased sample a real detail page. Keep English as default and provide complete Korean counterparts. This follows the user's repeated simplification request and coordinator clarification `msg_ce343d32c9bd`; it is not a GitHub requirement to use exactly these headings or this page count.

| Primary source inspected | Observation and application |
|---|---|
| [GitHub: About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | GitHub describes purpose, usefulness, getting started, help and contributors as README concerns. It recommends relative repository links and putting longer documentation elsewhere. Use short entry content and linked detail pages; GitHub's built-in outline removes the need for a long manual contents list. |
| [s1dashu/ip-as-logo-skill README](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/README.md), `acb834c717bcd0a487c49732d08397ba280d690b` | A short product definition, showcase, installation and practical request make the skill tangible. Retain that useful sequence, with Logo Land's own images and commands. Its model preferences, approval rules and commercial-use language are upstream claims, not Logo Land behavior. |
| [Anthropic skills README](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/README.md), `34040c9c568585f6929bedeaad110ad08f079624` | Installation is followed by a concrete request, and larger skill sets live behind folder links. Apply the install-to-first-prompt transition; do not import Claude commands or its broader catalog explanation. `main` resolved to this commit on inspection. |
| [meodai/color-expert README](https://github.com/meodai/skill.color-expert/blob/6514810aaab15cdd0e4202af52a6afed27ed314d/README.md), `6514810aaab15cdd0e4202af52a6afed27ed314d` | Separates immediately loaded guidance, an index and deeper references, and distinguishes original-material licensing from third-party sources. Apply that separation and attribution clarity; its long research narrative is inappropriate for this user's requested README. |

These are three original publishers, not summaries or installation authority for Logo Land. Exact external HTTP status, hashes and capture dates are in the QA report. Remote instructions were read as data; no remote command was executed.

## What exists now

Both root READMEs have 282 lines (English 27,091 bytes; Korean 31,117). `docs/README.md` has 52 lines/5,614 bytes and is currently a research/implementation index. Installation occupies 55 root lines; the remaining primary path mixes prompts with generation receipts, exact dimensions, color mathematics, schema migration, release history and QA links.

| Current surface | Actual coverage | User-facing treatment |
|---|---|---|
| `assets/logo-land-studio.png`, `docs/brand/README.md` | Current open-frame LOGO LAND identity; opaque ivory master | Keep the original hero bytes and 320px presentation. Rename the nearby action to “Logo Land identity” / “Logo Land 로고”; simplify the existing brand page to image, short description, example request and downloads. |
| `docs/samples/index.html`, `data.js`, `catalog.json` | Ten fictional brands across eight logo types; detail modal, not standalone sample pages | Add ten Markdown detail pages beside existing item files; preserve the HTML/JS/CSS and all downloads. |
| `docs/colors/index.html`, `manifest.json` | Eight showcased cases across seven projects; GROVE original/edit share a project; existing per-project HTML includes histories | Add concise per-project Markdown entrances and reuse existing HTML comparison links. Preserve the difference between downloadable originals and delivered packages. |
| `docs/app-icons/index.html`, `manifest.json` | Eleven originals: six separate IP candidates and five other styles | Add eleven individual pages. The five non-IP pages later hold old/new pairs only when new originals actually exist. |
| `docs/transparency/README.md`, `index.html` | Historical Logo Land transparency edit | Preserve both historical paths. Add a current transparency overview using GROVE; link the historical edit with a clear old-identity label. |
| `docs/brand/legacy.md`, `assets/logo.png`, `assets/logo-transparent.png` | Previous opaque and transparent identity, separate from current hero | Keep originals and old links. Do not describe the new opaque hero as having a transparent variant. |

The color manifest records eight requests, sixteen independent calls and seventeen stored artifacts; these are different counts. Only NORTHLINE, original GROVE and TIDE have delivery entries. The warmer GROVE has no delivery entry; 밤결, FIELD NOTE and white 밤결 retain indeterminate color reports. A fresh docs pass must not reinterpret them as successful examples of restricted-color delivery.

## Exact root outline, English and Korean

Target approximately 80–110 lines per root README, with equivalent information and links in both languages. The length is an editorial target, not a test of functionality. Use the following order and copy; all named new paths below are proposed, not created yet.

| Position | English default | Full Korean counterpart |
|---|---|---|
| Centered opening | Existing seven badges; English / 한국어 / Docs / Samples links; `# Logo Land`; existing `assets/logo-land-studio.png` hero | Same badges/order/image; localized alternative text; `# Logo Land (로고랜드)`; 문서 / 샘플 links |
| One-sentence value | “Create logos and app icon artwork through a conversation with Codex.” | “Codex와 대화하며 로고와 앱 아이콘 아트워크를 만드실 수 있습니다.” |
| `Installation` / `설치` | Short prerequisites and repository start block below; one full plugin-install link | Same prerequisites, commands and translated direct-use instruction |
| `Try it` / `이렇게 요청해 보세요` | Exactly three example requests below | All three fully translated below |
| `What you can make` / `만들 수 있는 것` | Four compact bullets: eight logo types; six icon styles; palettes/exact lettering/horizontal or stacked layouts; revise/resume and reviewed PNG/ZIP/guide | Same four bullets, with Korean labels and no extra technical narrative |
| `Samples` / `샘플` | Five short links: brand logos; colors & typography; app icons; transparent logos; Logo Land identity | Same five destinations in Korean; these lead to real individual sample pages |
| `Credits` / `출처` | Mandatory IP adaptation paragraph below, plus Changelog and Docs links | Same direct upstream credit, license notice and localized navigation |

The short prerequisite sentence must say: “Requires Codex native image generation/editing, Python 3.12+ and uv; plugin installation does not enable a missing image tool.” Korean: “Codex 내장 이미지 생성·편집 도구, Python 3.12 이상과 uv가 필요합니다. 플러그인 설치만으로 없는 이미지 도구가 활성화되지는 않습니다.” This names the requirement once, without a tool-provenance story.

```sh
git clone https://github.com/t1seo/logo-land.git
cd logo-land
uv sync --locked
codex
```

Follow with: “In this checkout, ask Codex to read `skills/logo-land/SKILL.md`, then use an example below. To enable `$logo-land` in other projects, follow the plugin installation guide.” The root implementation must link that guide at proposed relative target `docs/installation.md` after creating it. Korean conveys the same distinction: “이 저장소의 Codex 대화에서 `skills/logo-land/SKILL.md`를 읽도록 요청한 뒤 아래 예제를 사용해 주세요. 다른 프로젝트에서 `$logo-land`를 사용하시려면 플러그인 설치 안내를 따라 주세요.”

| Example | English | Korean |
|---|---|---|
| Brand | `$logo-land Create two calm logo concepts for Goyo, a meditation studio, combining a simple symbol with the exact Korean text 고요.` | `$logo-land 명상 스튜디오 고요의 차분한 로고 시안 두 개를 만들어 주세요. 단순한 심볼과 정확한 한글 고요를 조합해 주세요.` |
| IP app icon | `$logo-land Create six independent IP character candidates for my reading app, using three product-related directions. Choose the colors for me.` | `$logo-land 독서 앱에 어울리는 IP 캐릭터를 제품과 관련된 세 방향으로 정하고 독립 시안 여섯 개를 만들어 주세요. 색은 알아서 골라 주세요.` |
| Revision | `Use the second logo. Keep its lettering and shape, change the main color to navy, and make the background transparent.` | `두 번째 로고를 사용해 주세요. 글자와 형태는 유지하고 주 색상을 남색으로 바꾼 뒤 배경을 투명하게 만들어 주세요.` |

After capabilities, keep two concise limits: “Outputs are raster PNGs; editable vectors and font files are not included. App icon previews require separate platform preparation.” Korean: “결과는 래스터 PNG이며 편집 가능한 벡터와 폰트 파일은 포함되지 않습니다. 앱 아이콘은 별도의 플랫폼별 준비가 필요합니다.” Keep actual font-reference and restricted-color limitations on the relevant sample/usage page, without blanket success claims.

Keep the existing release/development badges truthful. Place one short note under installation: “This checkout is v0.5.0 development; the published release is v0.3.1.” This is the current local record, not a fresh release audit. Recheck it before implementation; never imply the unpublished v0.4.0 draft or v0.5.0 was published.

### Mandatory direct credit

Put this visible paragraph under `Credits`, and a short matching attribution on each IP detail page. Do not bury it only in a research document, a generic “inspiration” link or a tool list.

**English copy:** IP character guidance is adapted from [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill). See the [pinned adaptation reference](../../skills/logo-land/references/ip-mascot.md), [MIT license notice](../../skills/logo-land/assets/ip-as-logo.LICENSE), and [third-party notices](../../THIRD_PARTY_NOTICES.md).

**Korean copy:** IP 캐릭터 지침은 [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)을 바탕으로 각색했습니다. [고정된 원본과 각색 안내](../../skills/logo-land/references/ip-mascot.md), [MIT 라이선스 고지](../../skills/logo-land/assets/ip-as-logo.LICENSE), [제3자 출처 고지](../../THIRD_PARTY_NOTICES.md)를 확인해 주세요.

The links above resolve from this report; root README targets are `skills/logo-land/references/ip-mascot.md`, `skills/logo-land/assets/ip-as-logo.LICENSE`, and `THIRD_PARTY_NOTICES.md`. Keep existing credit to Adobe/Leonardo and meodai in third-party notices. There is no repository-root `LICENSE` at this baseline: do not invent a broken `LICENSE` link or declare all Logo Land materials MIT-licensed.

## Page map and navigation

Use Markdown for the primary GitHub path, relative links everywhere and unchanged originals. New English pages use `.md`; their complete Korean counterparts use `.ko.md`. Directory entries use `README.md` / `README.ko.md`. Do not create separate language copies of PNGs, prompts or gallery engines.

Primary path: **root README → category Markdown index → individual Markdown sample → original PNG download → back to category/root**. Coordinator clarification `msg_6379e73b6bd5` reinforces this same decision. Existing interactive HTML is an optional “Interactive view (open locally)” link on category/detail pages; the root Samples links never open HTML source. No long GitHub-HTML explanation, new hosted site, GitHub Pages deployment or duplicate HTML galleries is needed.

| Entry | Proposed English path | Purpose / next click |
|---|---|---|
| Docs | `docs/README.md` (rewrite existing) | Short index: installation, sample categories, user reference guides, Changelog, notices. Add `docs/README.ko.md`. |
| Plugin installation | `docs/installation.md` | Move the existing complete local-marketplace JSON, actual two CLI commands and new-conversation step here. Keep repository route first; no unsupported public marketplace or ZIP install shortcut. |
| Brand samples | `docs/samples/README.md` | Ten named links, type label and optional small preview; each points to its own page below. |
| Color/typography samples | `docs/colors/README.md` | Eight named cases linked to seven project pages; original and warmer GROVE use distinct sections of its one page. Label layout/typography beside the project, without another duplicate gallery. |
| App-icon samples | `docs/app-icons/README.md` | Six style groups containing all eleven individual links; the five non-IP entries become named old/new product comparisons after verified assets arrive. |
| Transparency | `docs/samples/transparency.md` | GROVE original preview, simple request, PNG link and light-surface guidance; link current GROVE page and preserved historical `docs/transparency/README.md`. |
| Current identity | `docs/brand/README.md` (simplify existing) | Current hero, brief user example, original/ZIP/guide and legacy link. Add a full Korean counterpart. Existing provenance stays in current audit files and `2026-identity/` records. |
| Historical index | `docs/archive.md` | Preserve the current `docs/README.md` content in this same-depth file so its relative links still work; link only as a small “Archive” entry at the bottom of the docs index. Do not reproduce the research table in the root README. |

### Ten brand detail pages

For every row, create `docs/samples/items/<id>/README.md` and `README.ko.md`. Each original already exists at `delivery/logo.png`, package at `delivery/logo-package.zip`, guide at `delivery/brand-guide.md`, and exact historical prompt at `prompt.txt`, relative to that item directory.

| `<id>` | Display title | Form |
|---|---|---|
| `01-luma` | LUMA | Wordmark / 워드마크 |
| `02-loop-lab` | LOOP LAB | Monogram / 모노그램 |
| `03-goyo` | 고요 | Symbol + Korean lettering / 한글 조합형 |
| `04-bread-bloom` | BREAD & BLOOM | Emblem / 엠블럼 |
| `05-kite` | KITE | Abstract / 추상형 |
| `06-miso` | MISO | Mascot / 마스코트 |
| `07-northline` | NORTHLINE · NL | Lettermark / 레터마크 |
| `08-mulgyeol` | 물결 | Korean wordmark / 한글 워드마크 |
| `09-fern` | FERN | Symbol / 심볼 |
| `10-nova-notes` | NOVA NOTES | Combination / 조합형 |

Use the existing `data.js` request's brand/type/style for a short “Try a similar request” with current `$logo-land`. Do not rewrite the historical `$logo-generator` request in `data.js`, `catalog.json` or `prompt.txt`, or call the new paraphrase the exact original prompt. NORTHLINE's old `NL` sample and its later full-name color sample must remain distinguishable.

### Eight color cases, seven project pages

Create `docs/colors/projects/<project>/README.md` plus its Korean counterpart. Existing `index.html` and `reports.html` remain at each project path. `docs/colors/` is the base for the image paths below.

| Project page | Current image(s) | Example request and necessary case note |
|---|---|---|
| `sunroom` | `assets/01-sunroom.png` | Choose a warm SUNROOM bakery palette; original PNG only, no delivery package exists. |
| `northline` | `assets/02-northline.png` | Create a stacked NORTHLINE symbol and exact name using a chosen navy palette; link existing `deliveries/northline/`. |
| `grove` | `assets/03-grove.png`, `assets/04-grove-warm.png` | Keep #247A52 and warm the companion color; `#original` and `#warmer` sections each link their own original. Only the first has `deliveries/grove/`; use on light surfaces. |
| `bamgyeol` | `assets/05-bamgyeol.png` | Crescent above exact 밤결, near-black/ivory on transparency; recorded restriction result remains indeterminate. |
| `tide` | `assets/06-tide.png` | Use SUNROOM as a color reference for horizontal TIDE & TYPE lettering; link `deliveries/tide/`. |
| `fieldnote` | `assets/07-fieldnote.png` | Use the GROVE reference and #247A52 with two colors; recorded restriction result remains indeterminate. |
| `white-bamgyeol` | `assets/08-bamgyeol-white.png` | Make the existing 밤결 design white for a dark surface; recorded result remains indeterminate, no approved transparent delivery. |

Sample pages show requested lettering appearance and horizontal/stacked layout from the saved project, as applicable. Mention font names only as visual references; do not imply an actual font file, editable text or font license. Use one short factual outcome note for unresolved samples; move tables of hashes/retries/measurements to the already-existing deeper comparison/report links.

### Eleven individual app-icon pages

Create English `docs/app-icons/samples/<id>.md` and matching `<id>.ko.md` for every row. For each existing ID, its original and exact prompt are already `docs/app-icons/images/<id>.png` and `docs/app-icons/prompts/<id>.txt`. Each IP candidate gets its own page, even where two show the same subject.

| `<id>` | Product/subject and page purpose | Future additional original, pending |
|---|---|---|
| `ip-a1` | Reading owl, lower-left | None |
| `ip-a2` | Reading owl, lower-right | None |
| `ip-b1` | Calm reading capybara, lower-left | None |
| `ip-b2` | Calm reading capybara, lower-right | None |
| `ip-c1` | Friendly reading puppy, lower-left | None |
| `ip-c2` | Friendly reading puppy, lower-right | None |
| `pictogram` | Weather, sun/cloud; one old/new page | `pictogram-quality-v1` |
| `abstract` | Focus, interlocking arcs; one old/new page | `abstract-quality-v1` |
| `monogram` | Notes, exact Korean `모`; one old/new page | `monogram-quality-v1` |
| `soft-3d` | Plant care, jade leaf; one old/new page | `soft-3d-quality-v1` |
| `pixel-art` | Timer, hourglass; one old/new page | `pixel-art-quality-v1` |

For an IP example request, name its subject and placement and request **one** candidate; otherwise the six-candidate default would not match that individual sample. Other example requests describe the product, visible subject and style; monogram must retain `모`, not the generic README example `메모`.

The root quality plan reserves `docs/app-icons-quality-v1/index.html` and five new IDs. When its manifest actually contains all sixteen entries, the app-icon index can link that comparison and the five named pages can display both original/new PNGs with exact dimensions, separate original downloads and optional exact prompts. Resolve new file names from that manifest, then use relative paths such as `../../app-icons-quality-v1/images/<verified-file>.png`; do not guess filenames from the requested subject. Keep `docs/app-icons/index.html` and its eleven originals untouched. No new separate history pages or duplicate quality landing page are needed: each named product page is its own before/after page. Before assets exist, link only the current eleven and omit future counts, thumbnails, claims of improvement and dead links.

### One small detail-page template

1. Title and English / 한국어 switch; back to its category and root README in the same language.
2. One-sentence result description and one original image (two for GROVE or a verified non-IP comparison).
3. One short user request, accurately labelled as an example rather than the saved native prompt.
4. Original PNG download per displayed image; existing ZIP/brand guide only when present. Optional exact prompt link without embedding the long prompt.
5. One relevant limitation/outcome sentence where needed; IP pages also contain the explicit upstream adaptation credit.

Use descriptive alt text. Ordinary pages should stay near 15–30 lines per language; paired pages can be 30–45. No file receipt tables, generation model/tool names, QA counts, design-process essays, scores, store/platform badges or inferred quality verdicts. Keeping every sample requires 28 substantive detail pages across brand/color/icon categories; this is not a reason to create pages for each of the seventeen historical color artifacts.

## Preservation and implementation handoff

| Existing link family | Preserve / new entry |
|---|---|
| `docs/samples/index.html`, `gallery.js`, `gallery.css`, `data.js`, `catalog.json`, `items/*/{prompt.txt,delivery/*}` | Byte-identical originals and engine; new Markdown item pages and category index provide the primary entry. |
| `docs/colors/index.html`, `manifest.json`, `assets/*`, `projects/*/{index.html,reports.html,prompts/*,session.json}`, `deliveries/*` | Byte-identical; Markdown project pages link the existing comparisons rather than duplicating histories. Keep all `#artifact-*` anchors. |
| `docs/app-icons/{index.html,manifest.json,images/*,prompts/*}` | Byte-identical; add individual pages without overwriting the old eleven-entry gallery. |
| `docs/brand/README.md`, `legacy.md`, `2026-identity/*`, `assets/logo*.png`, `docs/transparency/*` | Existing URLs continue to resolve; current identity page is simplified in place, old identity assets/records remain. |
| `docs/diagrams/{workflow-en.svg,workflow.svg,workflow-en.html,workflow.html}` | Preserve files and links that exist elsewhere; remove the diagram and its tool discussion from the root entrance. |
| `skills/logo-land/references/*`, `docs/research/*`, `docs/qa/*`, `plans/*`, `CHANGELOG.md`, `docs/releases.md`, `THIRD_PARTY_NOTICES.md` | Existing paths stay available as deeper reference. Root replaces narrator/research/QA tables with short user-oriented links. |

Preserve old root section anchors with unobtrusive explicit `<a id="…"></a>` anchors immediately before the relevant compact new section: installation anchors → Installation; usage/revision/helper anchors → Try it; six-icon/four-color/lettering/eight-type anchors → Capabilities; ten-sample/transparency anchors → Samples; release/research anchors → Credits/Docs links. Include both the old English and old Korean IDs in their respective READMEs. Preserve `docs/README.md#logo-land-research-and-implementation` and `#earlier-research-and-releases` beside its small archive link, and `docs/brand/README.md#historical-identity` beside its legacy link. The exact old root heading inventory is in the QA report.

Root owns final contract/dispatch, including any adaptation of these proposed paths. Suggested implementation order: preserve the current docs index in `docs/archive.md`; create complete bilingual installation/category/detail pages from existing data; integrate the five new pairs after Q5's verified manifest; then reduce both root READMEs and the docs/brand indexes. Recheck local paths, language symmetry, original bytes, old fragments, installation prerequisites, and explicit credit in the final render. This research does not run production tests, approve icon quality, install a plugin or certify the eventual page implementation.
