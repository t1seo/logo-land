# README information architecture research QA

Task `task_afd0760f6417`; dispatch `ctx_f5fa76030bf5`. Research only; ownership is this file, `docs/research/readme-structure.md`, and exact temporary directory `/tmp/ll-readme-ia`. Other worktree changes belong to concurrent work and must be preserved.

## Active work plan

The plan tool is unavailable in this session; this ledger records the same single-active-step discipline. The dispatch scope overrides skill defaults for plan file locations and sub-workers.

1. Completed: Inventory existing READMEs, galleries, original links, installation text and source hashes (329 files; 331 local link occurrences; no missing static destinations).
2. Completed: Inspect GitHub README guidance and three publisher READMEs; pin sources and write the bilingual structure/path map in `docs/research/readme-structure.md`.
3. Completed: Serve the repository on registered port 8795, verify exact README bytes over HTTP, inspect four external source responses and the pinned MIT notice, and exercise an intentional missing path.
4. Completed: Complete research/QA reports, stop the owned server, remove the exact temporary directory, and verify cleanup. The dispatch result is delivered once through `worker_done` after final checks.

## Resource register (before creation/start)

| Resource | Purpose | Ownership and cleanup |
|---|---|---|
| `/tmp/ll-readme-ia` | Baseline hashes, source HTTP captures, local HTTP capture, server log | Exact task-owned directory; absent at preflight; all 22 registered regular files and the empty directory removed at cleanup. |
| TCP `127.0.0.1:8795` | Serve the repository for bounded read-only HTTP QA | No listener at preflight; exec session `68725`, PID `89713`; owned process stopped and port confirmed free at cleanup. |
| `python3 -m http.server 8795 --bind 127.0.0.1` | Standard-library static server, repository root | No custom server script; no package installation. |
| `/tmp/ll-readme-ia/inspect.rb` | Read-only Markdown/HTML/manifest inventory and byte/hash comparisons | Task-owned helper script; Ruby standard library only; remove with exact temporary directory. |

No production/source/sample edits, installs, image calls, GUI sessions, child workers, commits or release actions are authorized for this dispatch.

## Evidence

Coordinator clarification `msg_ce343d32c9bd` (2026-09-12T17:58:25Z) requires actual individual sample pages, not category indexes alone. Apply it in the same plan: ten brand detail pages, seven color/project pages (the GROVE pair shares one), eleven app-icon pages (six individual IP candidates and five named non-IP comparisons). No sample is removed for page-count reduction; repeated historical attempts remain in existing galleries instead of receiving new pages.

Quality work stays independent. The active root plan identifies future `docs/app-icons-quality-v1` and five `*-quality-v1` IDs; these are pending, not existing samples or delivered results.

Further coordinator clarification `msg_6379e73b6bd5` (2026-09-12T18:02:54Z) confirmed the already-selected Markdown-first navigation. The report now states the full README → category → individual sample → original-download/backlink path explicitly; HTML galleries are optional local views, with no invented hosting/deployment or duplicated gallery engine.

## Local HTTP evidence

Repository root: `/Users/cillian/Documents/Github/Projects/logo-generator`. Branch `main`, HEAD `ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5`; baseline taken at `2026-09-12T17:59:39Z` / `2026-09-13T02:59:39+09:00`. This identifies a dirty local snapshot, not the committed content at HEAD.

Exact requested command (exit 0):

```sh
curl -i --fail --silent --show-error --connect-timeout 2 --max-time 10 http://127.0.0.1:8795/README.md -o /tmp/ll-readme-ia/readme.http
```

Exact response headers, with CRLF displayed as lines:

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:01:02 GMT
Content-type: application/octet-stream
Content-Length: 27091
Last-Modified: Sat, 12 Sep 2026 17:41:26 GMT
```

Splitting the captured response at the first CRLF/CRLF produced 27,091 body bytes, exactly equal to `File.binread('README.md')`; body and current-file SHA-256 both `abd6ca61e2a2a718ebc59d39cc26fd5f07fce44482ba1dd67ec1538b82308823`. This is PASS for HTTP 200 and exact current README bytes. The host's Python 3.9 standard-library server was only a static transport for this check; it did not execute the plugin or validate the plugin's Python 3.12 requirement. Markdown arrived as bytes, not a rendered GitHub page.

An intentional missing-path request to `/__readme_ia_missing__`, with the same fail/connect/total-time flags, exited 22: `curl: (22) The requested URL returned error: 404`. The server recorded `GET /__readme_ia_missing__ HTTP/1.1` with 404 at `2026-09-13T03:03:31+09:00`. This was a controlled failure probe, not a discovered broken README destination, and it was not retried.

## External HTTP/content evidence

All requests used `curl -L --fail --silent --show-error --connect-timeout 2 --max-time 10`, with separate response-header and body captures under the registered temporary directory. Publisher README URLs are immutable raw GitHub URLs for the commits below. Canonical clickable citations and the concise synthesis are in [the research report](../../research/readme-structure.md). The official GitHub guidance page has no pinned commit in its public URL, so its timestamp and content hash pin the observed snapshot instead.

| Source | Exact status / relevant headers | Bytes / SHA-256 |
|---|---|---|
| GitHub README guidance | `HTTP/2 200`; `content-type: text/html; charset=utf-8`; `date: Sat, 12 Sep 2026 17:59:42 GMT`; `content-length: 213374` | 213374 / `046026355bc840006d6a928c371133a880c98c0d7715a285ec5bf8f267101cfe` |
| s1dashu README, `acb834c717bcd0a487c49732d08397ba280d690b` | `HTTP/2 200`; `content-type: text/plain; charset=utf-8`; `date: Sat, 12 Sep 2026 17:59:42 GMT`; `content-length: 7963` | 7963 / `01fdc4729a1d7c13c5f5a71414d4a28756b142458a727a1f75e41c161fba4179` |
| meodai README, `6514810aaab15cdd0e4202af52a6afed27ed314d` | `HTTP/2 200`; `content-type: text/plain; charset=utf-8`; `date: Sat, 12 Sep 2026 17:59:42 GMT`; `content-length: 11456` | 11456 / `e17b8b1548d106ad1e4c6bdb4cd125f1da3ff96ddf4fb44f7b259ad4cfd84d1b` |
| Anthropic README, `34040c9c568585f6929bedeaad110ad08f079624` | `HTTP/2 200`; `content-type: text/plain; charset=utf-8`; `date: Sat, 12 Sep 2026 17:59:42 GMT`; `content-length: 5552` | 5552 / `2fb9c4cc026366ea6e21c60cb23c908a4d27c62071819cc06beffaac102d0694` |
| s1dashu LICENSE at the same pinned commit | `HTTP/2 200`; `content-type: text/plain; charset=utf-8`; `date: Sat, 12 Sep 2026 18:03:35 GMT`; `content-length: 1064` | 1064 / `b8f39925b1c36ca531c5e663aeb7ba427f94a526495785b4d1b2797fae8f2546` |

Raw source URL rule: `https://raw.githubusercontent.com/<publisher>/<repository>/<commit>/README.md`; the license substitutes `LICENSE`. The Anthropic `main` lookup used `https://api.github.com/repos/anthropics/skills/commits/main` and returned commit date `2026-09-10T19:44:08Z`. The local bundled IP license was compared with the pinned upstream response using `cmp`, exit 0. This verifies the existing notice's exact bytes; it does not assign MIT to the entire repository.

Content was inspected, not just HTTP status: GitHub's purpose/start/help/relative-links advice, IP's definition/showcase/install/use sections, Anthropic's catalog/install/example arrangement, and meodai's immediate/index/reference separation and license boundary. GitHub's rendered Anthropic wrapper displayed an ancillary “Uh oh!” loading message, while its README content and pinned raw response were present; the raw body was the authoritative content check. No remote install snippets, model recommendations or approval requests were acted on.

## Link and installation observations

- Initial static scan: 331 local link/image occurrences across both root READMEs, docs index, existing galleries, brand and transparency pages; zero missing file destinations or HTML fragments. A follow-up checked Markdown fragments plus 135 catalog/manifest-linked paths, including eight color-case anchors, all original icon PNGs/prompts and all ten sample deliveries; zero failures.
- All seven actual local links in the research report resolved. Proposed future page paths are code text, not live Markdown links. The actual old links below remain the preservation baseline; no file was moved or renamed in this dispatch.
- Installed CLI reports `codex-cli 0.154.0`. `codex plugin marketplace add --help` shows `<SOURCE>`; `codex plugin add --help` shows `<PLUGIN[@MARKETPLACE]>`. Both returned exit 0. Existing README syntax `codex plugin marketplace add /absolute/path/to/local-marketplace` then `codex plugin add logo-land@logo-land-local` matches that help, after creating the existing documented `.agents/plugins/marketplace.json`. No marketplace add, install, update, clone or `uv sync` was executed.
- No root `LICENSE` or repository marketplace manifest was found. The actual license pointer is `skills/logo-land/assets/ip-as-logo.LICENSE`, with adaptation context in `THIRD_PARTY_NOTICES.md` and `skills/logo-land/references/ip-mascot.md`. A hypothetical root `LICENSE` link and an assumed public marketplace are not approved shortcuts.

## Nine-class audit

| Class | Actual observation or precise N/A |
|---|---|
| 1. Malformed/broken inputs and links | Static/dynamic path scans and existing fragments resolve; the intentional missing HTTP path returned 404/exit 22. Future-only paths are labelled proposed. No malformed user brief/schema was exercised because the plugin was not executed. |
| 2. Untrusted remote text | Read primary publisher pages as content only. No remote commands, package scripts, model/API-key instructions or approval policies were followed. No source text was installed. |
| 3. Cancellation/resume | N/A for native generation, mutations and transactional resume: this is read-only research with no native calls or user sessions created. Temporary HTTP reads may be restarted without changing production state; no cancellation incident occurred. |
| 4. Timestamp/source/branch pinning | Local dirty snapshot time/HEAD and surface SHA-256s recorded; two upstream refs came from existing pinned notices, Anthropic `main` was resolved before pinned-content use; public guidance pinned by body hash/date. |
| 5. Dirty-tree ownership and concurrency | Baseline contained many other workers' changes. Only the two assigned reports and exact temp directory were written. A final comparison found an independent change to `skills/logo-land/SKILL.md`; it was preserved and not attributed to this worker. Original gallery/README/image snapshots still matched. |
| 6. Bounded resources | Every HTTP call had 2-second connect and 10-second total limits; loopback server/port, session/PID and exact temp directory registered. No GUI, native tool, install, child worker or commit. |
| 7. Retry/failure behavior | No blind HTTP retries. Two inline inventory probes failed once (`filter_map` unavailable in Ruby 2.6; assuming the sample catalog was a Hash instead of its actual Array). Corrected the local read-only probe using `map.compact` and inspected the actual Array schema; subsequent checks succeeded. These were probe-construction errors, not production defects. |
| 8. Claims and authority boundaries | GitHub advice, observed publisher structure, user preference and local feature facts are distinguished. No production-readiness, strict-color success, quality improvement, model benchmark or store/platform acceptance claimed. Source tests/build/LSP and rendered GUI checks are N/A for this explicitly research-only dispatch. |
| 9. Repeated steering and scope | Incorporated both coordinator clarifications into this same active plan: individual pages and GitHub-renderable Markdown primary navigation. Preserves all ten brand samples, eight color cases, eleven original icons and old URLs; pending five new outputs/sixteen-entry gallery remain dependent on separate workers/root contract. |

## Baseline surface hashes

Snapshot contains 329 files. SHA-256 of the temporary complete baseline JSON: `b76d09908a12dc1fa155850b3782573ee6c57033337925aefdd267b15631d182`. The critical user-facing files and original asset hashes are retained below; manifests and existing source records retain individual media hashes. The temporary full map is removed at cleanup as required.

| Existing file | Bytes | SHA-256 before this task |
|---|---|---|
| `README.md` | 27091 | `abd6ca61e2a2a718ebc59d39cc26fd5f07fce44482ba1dd67ec1538b82308823` |
| `README.ko.md` | 31117 | `0424dfab3c122d65870b1b90a29ab82c29542325c2800c8afe640359624ade8b` |
| `docs/README.md` | 5614 | `e5caaa56e3eae85b0fc8a4ed26f2fb952453a5ea481e3edb48a19674e1d8e7b5` |
| `docs/samples/index.html` | 8697 | `6195d260a64c0a2c14ca6a86caf3d89ad0c41cc90c93e4718818dea73b6c2e70` |
| `docs/samples/data.js` | 37537 | `6312b89775426b4039baac26ed6b3454532a5c38f3375c920e943a1dab30fe76` |
| `docs/samples/gallery.js` | 9273 | `812e7a2f78b6d786b0b9af66e32a3185e057a6d291361f37e80a0424f044ab24` |
| `docs/samples/gallery.css` | 17000 | `8a05900f4295d6fa1602a5edf690373150555d9b118935c9a363426b604288aa` |
| `docs/colors/index.html` | 38564 | `5a0118f37c31c6d30837f2e68bcb931d82f24873a8a547709f4edb6e7f3749f8` |
| `docs/colors/manifest.json` | 99088 | `e13b772bd2fa4b810777bab3cec7ba145d4d227f1b47843b1d3ae7bce6d6dfea` |
| `docs/app-icons/index.html` | 21510 | `e87c1e9d3a78b6404d5560d8e778e8ef812618e7f13d1e7ed7a1d3b18e74a1bd` |
| `docs/app-icons/manifest.json` | 6655 | `fe6b2183a34beadf3932f00a63999ba17015792f15f87511b14a0ed9d9801dc9` |
| `docs/brand/README.md` | 4397 | `2a2ce0f0d4c11b81df9430711318202768bdb2e4a7e764540ff06430a8f45083` |
| `docs/brand/legacy.md` | 1978 | `8e7f3fa70a6b84e69e2822ff8a4fff8c7354ab0d813f7f7fc4a12f9bad5f488b` |
| `docs/brand/2026-identity/preview.html` | 4507 | `bf1da531206931ffa45241bc3562b631bd305de2a20c48145dab84b783b475b7` |
| `docs/transparency/README.md` | 4752 | `cc897e9c43499a9d1cddd64ed6fdb1b24b9fb5bc0f47c40aa12349f6f99d5e5f` |
| `docs/transparency/index.html` | 3280 | `f2f207307b2ba1c6c0998e43c21d4d507aee6fbda8838ba5c7bfd4582f4750b0` |
| `assets/logo-land-studio.png` | 835901 | `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3` |
| `assets/logo.png` | 973470 | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| `assets/logo-transparent.png` | 696379 | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |
| `.codex-plugin/plugin.json` | 1622 | `4689048ed484484dceb9453334ea1f5c1042ba2ea3b085abd05c8fdb3c7c3414` |
| `THIRD_PARTY_NOTICES.md` | 4275 | `ba5f0db63846caf31dd049f2d171442701767692f3825c38c0cccfa79c714b99` |
| `skills/logo-land/SKILL.md` | 11760 | `3dac44b63f34d89a49990ff818105c664bc1953cbb1bd60e102a6dae2ef2cc0a` |
| `skills/logo-land/references/ip-mascot.md` | 4162 | `08f93b78555246ea3b71a11d4879a53790808df4cab400bd5ed84b6d409e4850` |
| `skills/logo-land/assets/ip-as-logo.LICENSE` | 1064 | `b8f39925b1c36ca531c5e663aeb7ba427f94a526495785b4d1b2797fae8f2546` |

## Exact old-link inventory

The following normalized repository-relative destinations are the union of local links/images in the two root READMEs and the current docs index. They all existed at inspection; preserve the files, even where the simplified entrance stops displaying them. The research report maps sample/category families to new entrances.

```text
CHANGELOG.md
README.ko.md
README.md
assets/logo-land-studio.png
docs/README.md
docs/app-icons/images/abstract.png
docs/app-icons/images/ip-a1.png
docs/app-icons/images/monogram.png
docs/app-icons/images/pictogram.png
docs/app-icons/images/pixel-art.png
docs/app-icons/images/soft-3d.png
docs/app-icons/index.html
docs/brand/README.md
docs/colors/assets/02-northline.png
docs/colors/assets/03-grove.png
docs/colors/assets/06-tide.png
docs/colors/deliveries/grove/brand-guide.md
docs/colors/deliveries/grove/logo.png
docs/colors/index.html
docs/colors/projects/grove/index.html
docs/diagrams/style-guide.md
docs/diagrams/validation.md
docs/diagrams/workflow-en.html
docs/diagrams/workflow-en.svg
docs/diagrams/workflow.html
docs/diagrams/workflow.svg
docs/planning/gap-analysis.md
docs/qa/app-icons/docs.md
docs/qa/app-icons/native-samples.md
docs/qa/background-variants.md
docs/qa/color-workflow/README.md
docs/qa/color-workflow/review-summary.md
docs/qa/final.md
docs/qa/helper-tests.md
docs/qa/installation.md
docs/qa/live/README.md
docs/qa/live/preview.html
docs/qa/samples.md
docs/releases.md
docs/research/app-icon-tools.md
docs/research/brandmark-tailor-walkthrough.md
docs/research/captures.jsonl
docs/research/chrome-followup.md
docs/research/comparison.md
docs/research/font-shortlist.json
docs/research/font-tools.md
docs/research/gallery.html
docs/research/looka-fiverr-design-walkthrough.md
docs/research/official-features.md
docs/research/sources.json
docs/samples/catalog.json
docs/samples/index.html
docs/samples/items/01-luma/delivery/logo.png
docs/samples/items/02-loop-lab/delivery/logo.png
docs/samples/items/03-goyo/delivery/logo.png
docs/samples/items/04-bread-bloom/delivery/logo.png
docs/samples/items/05-kite/delivery/logo.png
docs/samples/items/06-miso/delivery/logo.png
docs/samples/items/07-northline/delivery/logo.png
docs/samples/items/08-mulgyeol/delivery/logo.png
docs/samples/items/09-fern/delivery/logo.png
docs/samples/items/10-nova-notes/delivery/logo.png
plans/logo-generator.md
plans/logo-land-app-icons.md
plans/logo-land-color-workflow.md
skills/logo-land/assets/app-icon.example.json
skills/logo-land/references/app-icons.md
skills/logo-land/references/color-providers.md
skills/logo-land/references/color-workflow.md
skills/logo-land/references/delivery-checks.md
skills/logo-land/references/ip-mascot.md
skills/logo-land/references/logo-directions.md
skills/logo-land/references/project-files.md
skills/logo-land/references/typography.md
```

## Exact old section anchors

Keep these root fragments at the related compact section when headings are renamed. Heading-derived IDs below use the current visible headings; there are no duplicate headings in this inventory.

| Existing file | Fragment IDs |
|---|---|
| `README.md` | `#get-started`, `#use-the-repository-directly`, `#install-as-a-codex-plugin`, `#use-natural-language`, `#six-app-icon-directions`, `#choose-colors-in-four-ways`, `#pair-a-symbol-with-exact-lettering`, `#eight-logo-types`, `#ten-real-samples`, `#transparent-background-logos`, `#revisions-and-delivery`, `#image-generation-and-the-file-helper`, `#releases-and-versioning`, `#research-and-verification` |
| `README.ko.md` | `#시작하기`, `#저장소에서-바로-사용`, `#codex-플러그인으로-설치`, `#대화로-사용하기`, `#앱-아이콘-방향-여섯-가지`, `#네-가지-방식으로-색상-정하기`, `#심볼과-정확한-글자-조합하기`, `#로고-유형-8가지`, `#샘플-10개`, `#투명-배경-로고`, `#수정과-전달-파일`, `#이미지-생성과-파일-보조-도구의-차이`, `#릴리스와-버전-관리`, `#조사와-제작-근거` |

Also preserve `docs/README.md#logo-land-research-and-implementation`, `docs/README.md#earlier-research-and-releases`, and `docs/brand/README.md#historical-identity` beside the replacement archive/legacy links. Existing HTML galleries keep their existing fragment IDs by remaining unchanged.

## Final verification and cleanup

- Final full-baseline comparison before removal: 328 of 329 files unchanged; only the separately owned `skills/logo-land/SKILL.md` changed concurrently. Both root READMEs, docs/brand index, gallery engines, manifests, downloads and images remained at the recorded baseline. No concurrent edit was reverted.
- Authored reports: eight local Markdown links resolve; final-newline, trailing-whitespace and fenced-block checks pass. The paths recommended for later creation remain clearly marked proposals. No production tests or rendered GUI verification were claimed.
- Server identity rechecked with `ps -p 89713 -o pid=,command=` immediately before `kill 89713`; it was the exact task server bound to 8795. Session `68725` terminated with exit 143 after SIGTERM. No other process was stopped.
- The command safety review rejected `rm -rf -- /tmp/ll-readme-ia` because forced removal commands are not permitted. Cleanup used a safer exact allowlist of the 22 known filenames, first checking the complete directory membership and each regular-file type, then unlinking those files and removing the empty directory; no recursive force deletion occurred.
- At `2026-09-12T18:06:36Z`, `test ! -e /tmp/ll-readme-ia` exited 0 and `lsof -nP -iTCP:8795 -sTCP:LISTEN` returned no listener (exit 1). All temporary captures/script/logs and the owned HTTP process were removed. Only the two assigned Markdown reports remain as this task's deliverables.

The research scope is complete. Root owns the final information-architecture contract and subsequent documentation implementation, with five pending quality originals and the sixteen-entry gallery supplied by their separate owners.
