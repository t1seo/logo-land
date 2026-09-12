# Font tools and Korean/Latin logo references

Research date: 2026-09-13. Scope: the authorized font extension in [the implementation plan](../../plans/logo-land-color-workflow.md). Machine-readable companion: [font-shortlist.json](font-shortlist.json).

## Decision for Logo Land

Use official family pages and pinned publisher metadata to choose **appearance references**. Start with Noto Sans KR or Pretendard for mixed Korean/Latin brands, Noto Serif KR for a literary direction, and Gowun Dodum for a warm direction. Montserrat, Fraunces and Space Grotesk are useful Latin references with a separately chosen Korean companion.

Keep native image generation responsible for the whole symbol-plus-text image. A requested `font_reference` is intent: it does not establish that a raster contains that font, reproduce its outlines exactly, verify its license, or supply an editable font file. Exact brand and slogan strings remain the task's text requirement; a known family name does not prove spelling or Hangul shaping succeeded. No font installation, separate typesetter, font-file bundle, or new MCP connection is recommended for this release.

**Correction to the preliminary shortlist:** Black Han Sans has conflicting official script evidence. Its metadata lists Latin, but its description says Latin alphabet characters are absent and identifies only 2,580 Korean characters. Keep it conditional for short Hangul display references; do not use it as the mixed-script default. Both sources are retained below.

## Six tool candidates

“Official” refers to the named publisher's own service or repository. A community project mentioning Google, Adobe or Typekit does not become their official skill/MCP. These categories describe actual surfaces inspected, not hypothetical integrations.

| Candidate | Provenance and actual kind | Use in this release |
| --- | --- | --- |
| Google Fonts | Official Google catalog, CSS web API and Developer metadata web API | Primary font facts and appearance references |
| Adobe Fonts / documented Typekit API | Official Adobe catalog/subscription service and HTTP API | Optional family browsing; account/license-dependent exact-font work remains outside this release |
| sliday/google-fonts-skill | Community Markdown skill, Python CLI and MCP server | Optional advisory selection source after source review |
| wondelai/web-typography | Community Markdown skill | Selection and pairing vocabulary |
| Microck/font-mcp | Community MCP server | Exclude: download side effects and unresolved license evidence |
| fontTools ttLib | Upstream open-source Python library | Defer: useful if a future authorized workflow inspects actual font files |

### 1. Google Fonts: separate CSS delivery from catalog metadata

The [CSS2 documentation](https://developers.google.com/fonts/docs/css2) exposes family/axis/style requests, variable ranges and `text=` subsetting. Public CSS requests work without an API key, as the live checks below confirm. The [Developer API](https://developers.google.com/fonts/docs/developer_api) supplies family metadata, variants, subsets and file URLs, and explicitly requires a Google API key. Both are web APIs, not agent skills or MCP servers.

Network is needed for the hosted catalog, CSS and font delivery. CSS creation alone does not fetch the linked font binary. `text=` sends the requested characters to Google and applies once across all families in the request; it can omit future characters. Axis order/ranges must satisfy CSS2 rules, and unsupported weights can fail. No numeric Developer API quota was verified, so this report does not promise unlimited requests.

Check each family's license and script evidence in the [official distribution](https://github.com/google/fonts/tree/809e4d8b8d7e9364a914909bb777679606c178b8/ofl). All seven Google-hosted shortlist families have an OFL-1.1 file at this pin; this finding is not a claim about every item shown by Google's websites. Metadata such as `subsets: "latin"` is a catalog declaration, not a character-by-character test.

### 2. Adobe Fonts: a service license and a real, separately documented API

The [catalog](https://fonts.adobe.com/) provides specimens, language/style browsing and pairings. Adobe documents a [Typekit HTTP API](https://fonts.adobe.com/docs/api) for family metadata and kit management; its continued public documentation is verified, but this research did not authenticate or exercise it. Do not describe Adobe Fonts as having no API. No official font-specific agent skill or MCP server was established by the inspected sources.

[Activation requirements](https://helpx.adobe.com/fonts/web/introduction/system-subscription-requirements.html) include a signed-in, named-user Adobe subscription and the Creative Cloud desktop application for desktop fonts. Available fonts depend on the account/plan; the catalog also advertises free account access, so do not label every font “purchase required.” Hosted usage needs network. [API authentication](https://fonts.adobe.com/docs/api/auth) uses `X-Typekit-Token` over HTTPS for private information and kit operations; some public endpoints do not require it. [Pagination](https://fonts.adobe.com/docs/api/pagination) documents `page`/`per_page`, oversized-page HTTP 400 and out-of-range HTTP 404, without a numeric limit on that page. New-token availability and account-specific quotas were not verified.

The [licensing FAQ](https://helpx.adobe.com/fonts/web/font-licensing/font-licensing.html) allows commercial logos and rasterized/outlined artwork, but does not permit transferring subscription font files to collaborators or installing them on servers under the standard service license. A client editing live text needs their own font access. Existing rasterized/outlined artwork survives subscription cancellation. These service rules are not a blanket license for independently installed fonts.

For Korean, use Adobe's [language support guidance](https://helpx.adobe.com/fonts/web/language-support-and-opentype-features/language-support-subsetting.html) and inspect the specific family. [Source Han Sans KR](https://fonts.adobe.com/fonts/source-han-sans-korean) explicitly documents 11,172 contemporary Hangul syllables and additional Korean coverage, and identifies an open-source licensing route. That family is a coverage example, not a ninth selected reference, and its separate upstream rights should not be conflated with all Adobe catalog families.

### 3. sliday/google-fonts-skill: useful local data, community judgment

Inspected the actual [SKILL.md](https://github.com/sliday/google-fonts-skill/blob/f86afc07d1cf28a36ab4f2807cee91c9c651b4da/SKILL.md), [MCP server definitions](https://github.com/sliday/google-fonts-skill/blob/f86afc07d1cf28a36ab4f2807cee91c9c651b4da/src/google_fonts_mcp/server.py), [core implementation](https://github.com/sliday/google-fonts-skill/blob/f86afc07d1cf28a36ab4f2807cee91c9c651b4da/src/google_fonts_mcp/core.py), [package metadata](https://github.com/sliday/google-fonts-skill/blob/f86afc07d1cf28a36ab4f2807cee91c9c651b4da/pyproject.toml) and [MIT license](https://github.com/sliday/google-fonts-skill/blob/f86afc07d1cf28a36ab4f2807cee91c9c651b4da/LICENSE). This is not published by Google.

The five registered tools are `search_fonts`, `generate_typography_system`, `lookup_font`, `list_scales` and `list_pairings`. They return recommendations, metadata and CSS/Tailwind/embed text. The pinned packaged CSVs contain 1,923 font rows, 73 pairing rows and eight scale rows, counted during research. They are a bundled snapshot, not live Google API responses. Search is limited to 500 characters and 1–50 results; system generation has a 1–512 base-size range and 200-character family/weight-string bounds.

The MCP package requires Python >=3.10, FastMCP >=3.4.7,<4 and rich. Inspected runtime selection reads local CSV files and requires no Google API key; initial package acquisition and use of generated Google web embeds need network. Skill-only scripts are another surface, not an already-connected MCP.

**Relevant limits:** there is no script/glyph validation tool. `Subsets` is searchable in the CSV but omitted from the normal lookup output columns. The data gives Black Han Sans a Latin tag, propagating the same conflict found in Google's metadata. The skill's single-font/body mode excludes single-weight display faces, which can still be appropriate logo references. Pairing counts and A/B/C ratings are community curation, not independent quality or licensing certification. Adopt vocabulary or optional suggestions; do not copy its complete dataset into Logo Land.

Discovery observed [193 skill installs](https://skills.sh/sliday/google-fonts-skill/google-fonts) and 13 repository stars. This is an early community candidate, not a maturity guarantee. Optional future installation syntax from the discovery CLI is `npx skills add sliday/google-fonts-skill@google-fonts`; it was not run.

### 4. wondelai/web-typography: a selection skill, not a font engine

The full [SKILL.md](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/web-typography/SKILL.md) distinguishes short display work from sustained reading, discusses structure/weight contrast, and asks for representative content and actual-size checks. Its [repository license](https://github.com/wondelai/skills/blob/c172996495bed0fcd26896a9416b2093fd7073f0/LICENSE) and skill header say MIT. No API key, font binary or server is intrinsic to this Markdown guidance; following external font links introduces network needs.

Use its pairing vocabulary as advisory context. Body-size, line-height and payload heuristics are web-content guidance, not logo acceptance gates, and should not be imposed on Hangul wordmarks. The author's reference to a former Typekit designer/book does not make this an Adobe-authored skill or relicense the book. No code or prose from that book was imported.

Discovery observed [7.6K skill installs](https://skills.sh/wondelai/skills/web-typography) and 2,155 repository stars. Optional future syntax is `npx skills add wondelai/skills@web-typography`; no skill was installed.

### 5. Microck/font-mcp: inspected and excluded

The [README](https://github.com/Microck/font-mcp/blob/e73f9befcef48a9d7fcf694a1576495e800fd33d/README.md) and actual [server tool definitions/handlers](https://github.com/Microck/font-mcp/blob/e73f9befcef48a9d7fcf694a1576495e800fd33d/src/index.ts) expose `consult_font_expert`, `analyze_project_and_recommend`, `analyze_website` and `setup_font_config`. The code calls external research sites, reads project paths and, for `setup_font_config(is_paid=true)`, invokes a font-file hunter. This is not a recommendation-only interface.

[Configuration defaults](https://github.com/Microck/font-mcp/blob/e73f9befcef48a9d7fcf694a1576495e800fd33d/src/config.ts) specify ten download attempts, 30,000 ms per download, `./public/fonts` output and free fallback disabled. These are download defaults, not an overall tool deadline. [ResearchService](https://github.com/Microck/font-mcp/blob/e73f9befcef48a9d7fcf694a1576495e800fd33d/src/services/ResearchService.ts) and [RedditService](https://github.com/Microck/font-mcp/blob/e73f9befcef48a9d7fcf694a1576495e800fd33d/src/services/RedditService.ts) show direct external requests; no API key configuration was found in these inspected paths. This is source inspection, not proof the remote services currently allow or complete those requests.

The README claims MIT, but its [linked root LICENSE](https://github.com/Microck/font-mcp/blob/e73f9befcef48a9d7fcf694a1576495e800fd33d/LICENSE) is absent in the inspected tree and the raw path returned HTTP 404. GitHub's license field was null; nine stars were observed. A downloader's assumption that the user owns a license does not establish download rights, glyph coverage or legitimate provenance. Do not install, connect or use its setup tool in this workflow.

### 6. fontTools ttLib: possible future file inspection

The upstream [MIT license](https://github.com/fonttools/fonttools/blob/e74dcee6b032586c1b15f8481bd341bc9e3b4a0b/LICENSE), [ttFont source](https://github.com/fonttools/fonttools/blob/e74dcee6b032586c1b15f8481bd341bc9e3b4a0b/Lib/fontTools/ttLib/ttFont.py) and [documentation](https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html) describe reading font contents. `getBestCmap()` returns a Unicode code-point mapping or `None` if there is no suitable Unicode cmap. This is a library, not a hosted API, font catalog, pairing skill or MCP server.

A future workflow could inspect an already-authorized local font without a service key or runtime network, after installing the library. A cmap check does not verify shaping, kerning, raster appearance or the input font's license. No fontTools installation, font-file inspection or typesetting was performed here.

## Eight practical family references

Style and pairing judgments below are this researcher's suggestions; factual weights/script/license claims come from the linked publisher files. “Declared” means publisher evidence, not a binary cmap or rendered specimen test. All eight selected upstream font families identify OFL-1.1; each exact license is linked. [SIL's FAQ](https://openfontlicense.org/ofl-faq/) permits logos/artwork without requiring the artwork itself to adopt the OFL, while modifying or redistributing font software has separate conditions, including notices and any Reserved Font Names.

| Family and suggested use | Weight evidence | Korean / Latin evidence and important limit | Pinned primary evidence |
| --- | --- | --- | --- |
| **Noto Sans KR**: neutral/professional mixed-script horizontal lockup | Variable 100–900; reference 500–700 | Hangul and Latin declared; use KR regional family | [Metadata](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/notosanskr/METADATA.pb), [description](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/notosanskr/DESCRIPTION.en_us.html), [OFL](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/notosanskr/OFL.txt) |
| **Noto Serif KR**: heritage, editorial, tea, stacked lockup | Variable 200–900; reference 500–700 | Hangul and Latin declared; thin strokes need actual-size review | [Metadata](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/notoserifkr/METADATA.pb), [description](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/notoserifkr/DESCRIPTION.en_us.html), [OFL](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/notoserifkr/OFL.txt) |
| **Pretendard**: balanced modern Korean/Latin product brand | Nine static weights documented; pinned variable CSS declares **45–920**; practical reference 400–700 | Base family supports Korean/Latin; Std is Latin-oriented; current source differs from README's v1.3.9 CDN examples | [README](https://github.com/orioncactus/pretendard/blob/7aeb0698819be2b4097dae8ec8fe6a795e5cf3ae/packages/pretendard/README.md), [CSS](https://github.com/orioncactus/pretendard/blob/7aeb0698819be2b4097dae8ec8fe6a795e5cf3ae/packages/pretendard/dist/web/variable/pretendardvariable.css), [subset text](https://github.com/orioncactus/pretendard/blob/7aeb0698819be2b4097dae8ec8fe6a795e5cf3ae/packages/pretendard/subset_glyphs.txt), [OFL](https://github.com/orioncactus/pretendard/blob/7aeb0698819be2b4097dae8ec8fe6a795e5cf3ae/packages/pretendard/dist/LICENSE.txt) |
| **Gowun Dodum**: warm café, wellness, gentle humanist mark | Static 400 only | Korean and Latin declared; do not invent bold/italic variants | [Metadata](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/gowundodum/METADATA.pb), [description](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/gowundodum/DESCRIPTION.en_us.html), [OFL](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/gowundodum/OFL.txt) |
| **Black Han Sans**: conditional short Hangul display | Static **400**, despite heavy appearance | Description: 2,580 Korean characters, no Latin alphabet; metadata: Korean + Latin. **Conflict unresolved; no mixed-script default** | [Metadata](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/blackhansans/METADATA.pb), [conflicting description](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/blackhansans/DESCRIPTION.en_us.html), [OFL](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/blackhansans/OFL.txt) |
| **Montserrat**: confident geometric Latin wordmark | Variable 100–900, upright/italic; reference 600–700 | Latin declared; Hangul not declared in selected distribution | [Metadata](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/montserrat/METADATA.pb), [description](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/montserrat/DESCRIPTION.en_us.html), [OFL](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/montserrat/OFL.txt) |
| **Fraunces**: soft retro café/craft or editorial Latin | Variable 100–900; SOFT 0–100, WONK 0–1, opsz 9–144; upright/italic | Latin declared; Hangul not declared. Font axes are not native imagegen controls | [Metadata](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/fraunces/METADATA.pb), [description](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/fraunces/DESCRIPTION.en_us.html), [OFL](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/fraunces/OFL.txt) |
| **Space Grotesk**: technical/creative Latin wordmark | Variable 300–700; reference 500–700 | Latin declared; Hangul not declared. It is proportional despite its monospace ancestry | [Metadata](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/spacegrotesk/METADATA.pb), [description](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/spacegrotesk/DESCRIPTION.en_us.html), [OFL](https://github.com/google/fonts/blob/809e4d8b8d7e9364a914909bb777679606c178b8/ofl/spacegrotesk/OFL.txt) |

Practical pairings: Noto Serif KR + Noto Sans KR for editorial structure; Fraunces + Gowun Dodum for a Latin brand with Korean secondary text; Space Grotesk + Pretendard for a technology mark; Montserrat + Noto Sans KR for a geometric brand. These are appearance suggestions, not tested pairings or exact font selections in generated artifacts.

## Guidance for skill and sample owners

Translate references into visible traits: “balanced modern Korean sans serif, medium-bold strokes, open counters, even spacing” is more useful than treating a family name as a font engine. Specify horizontal/stacked layout, symbol position and alignment separately from typography. For mixed scripts, identify which text gets which visual treatment and preserve the original strings exactly.

Suggested native sample directions, for the coordinator to execute: a horizontal Noto Sans KR-like Korean/Latin brand; a stacked Noto Serif KR-like heritage mark; and a Space Grotesk-like Latin name with Pretendard-like Korean slogan. The family names should be labeled **requested visual references** in metadata. This research did not create or review those samples.

Review the native image's exact spelling, Hangul syllable composition, spacing, symbol/text separation and small-size readability. If a future task requires exact font outlines, glyph completeness, editable text or font files, that is a separate typesetting workflow with specific font-file and license evidence. Browser fallback and a successful CSS response cannot supply that evidence.

## Verification, adversarial checks and cleanup

The deliverables are research Markdown/JSON only. No Python/TypeScript/Go/Rust or SKILL.md was changed; programming TDD, Ruff, basedpyright, build and LSP checks are not applicable to these owned files. No code-baseline or native-image success is claimed. The coordinator owns integrated tests and native image QA.

Actual checks performed:

- Read the authorized plan extension; modified only the two assigned research files.
- Applied find-skills: checked [the leaderboard](https://skills.sh/), ran `npx --yes skills find 'font pairing'`, then owner-filtered typography/Google Fonts searches. CLI results supplied the install counts above; `gh api` supplied commit SHAs, stars, trees and license metadata. No `skills add` or server start was run.
- Read actual community SKILL.md files and registered MCP definitions/handlers, not just search-directory summaries. Counted the three sliday CSV datasets and examined Korean rows and omitted lookup subset fields.
- Retrieved the seven pinned Google metadata, description and OFL files; inspected Pretendard's actual monorepo README, variable CSS, subset text and distribution license. The root Pretendard README is a path pointer, not its substantive documentation.
- **Live CSS boundary checks:** unauthenticated Noto Sans KR 700 with synthetic text `모로 MORROW` returned HTTP 200 and CSS naming family/weight; Black Han Sans 700 with `모로` returned HTTP 400; Black Han Sans 400 returned HTTP 200. Only CSS responses were read; linked font binaries were not fetched. These observations prove response/weight behavior, not rendering or glyph coverage.
- Microck's pinned root LICENSE URL returned HTTP 404, matching the absent tree entry and null GitHub license metadata. This is a known missing source, not a broken citation accidentally treated as license proof.
- Parsed the JSON and checked family/tool counts, unique IDs, HTTPS source links, 40-character repository pins, and the Black Han Sans conflict marker; checked both deliverables for whitespace errors.

Reproducible, read-only CSS check:

```sh
curl -sS -G 'https://fonts.googleapis.com/css2' \
  --data-urlencode 'family=Noto Sans KR:wght@700' \
  --data-urlencode 'text=모로 MORROW' \
  --data-urlencode 'display=swap' \
  -w '\nHTTP_STATUS=%{http_code}\n'
```

Applicable adversarial classes and outcomes:

| Class | Evidence and handling |
| --- | --- |
| Official/community confusion | Google/Adobe services separated from sliday, wondelai and Microck projects |
| License laundering through a downloader | Missing Microck license and automatic paid-font hunting identified; excluded |
| Script metadata contradicting glyph claims | Black Han Sans metadata/description conflict preserved; default recommendation corrected |
| Unsupported weight or visual-weight confusion | Black Han Sans 700 negative HTTP check paired with 400 positive check |
| Wrong family variant or source version | Pretendard base/Std distinction and source 45–920 versus older CDN examples recorded |
| Catalog data mistaken for complete glyph coverage | No exact-code-point or shaping claims; no binary inspected |
| Generated raster mistaken for actual licensed font output | Appearance-reference boundary explicit in both artifacts |
| Hidden network/write side effects | CSS/network requirements and MCP download/filesystem behavior documented; no MCP executed |
| Unicode and data integrity | Korean synthetic strings preserved in UTF-8 JSON; counts/IDs and pin shapes checked |

Cleanup: no font binaries, installed fonts, installed skills, running servers, generated images, temporary repository artifacts or credentials were introduced. The discovery CLI may use its normal npm execution cache outside the repository; no shared cache was deleted. No commits, pushes, API signups or purchases were performed. Authenticated Adobe/Google metadata APIs, live MCP calls, fontTools execution, per-character cmap coverage and native image quality remain untested by design and are not prerequisites for this bounded research deliverable.
