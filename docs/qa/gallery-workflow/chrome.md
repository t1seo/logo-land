# Actual Google Chrome gallery QA

**PASS.** Both observed product issues were fixed by their owners and rechecked in real Chrome: README samples now form 3+3 rows, and Back restores filters, visible cards, count, preview context and surround together. The final comparison is open in the named owned window with one tab, 8 candidates and default controls.

Date: 2026-09-13 KST. Task task_5444b0bc7a55 / dispatch ctx_a04104359e84. Branch feat/logo-land-gallery-workflow. Browser-only ownership: this report and chrome/ screenshots; no production, artwork, installation or commit edits.

Read plan T4 and [comparison](comparison.md), [continuity](continuity.md), [documentation](docs.md), [native samples](native-samples.md), [T3 integration](integration.md), and the earlier app-icon Chrome reports. Applied the official Computer Use SKILL.md at /Users/cillian/.codex/.tmp/bundled-marketplaces/openai-bundled/plugins/computer-use/skills/computer-use/SKILL.md and Orca orchestration guidance.

## Actual surface and scenario results

All GUI used tools.mcp__node_repl__js and documented @oai/sky. The exact first call was sky.get_app_state({app:"com.google.Chrome"}) after globalThis.sky=(await import("@oai/sky")).sky. A fresh address field 124 received file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/gallery-workflow/comparison/index.html with sky.set_value, followed by Return and fresh state. Every later indexed action was grounded in a newly fetched accessibility tree; literal calls are retained below.

README EN/KO and docs/gallery EN/KO were rendered by actual POST https://api.github.com/markdown with mode=gfm and context=t1seo/logo-land. The owned localhost wrappers use local GitHub-like CSS, preserve source image sizes, resolve Markdown links to rendered pages and PNG links to exact files. They are labeled **GFM-rendered local previews**, not live GitHub. Desktop was Chrome 100%; narrow was actual Chrome 300% zoom, exercising a narrower effective CSS layout, not mobile-device emulation or a measured physical mobile viewport.

| Scenario | Observed result and evidence |
|---|---|
| README first visit, EN default and separate KO | PASS: centered top badges, language navigation, same six clickable originals including COMMON/Relay. Final 3+3 rows: [EN](chrome/32-readme-en-final-desktop.jpg), [KO](chrome/33-readme-ko-final-desktop.jpg). |
| Narrow README | PASS: badges wrap, prose and sample rows fit, no page-level horizontal overflow or clipped lettering observed. [KO top](chrome/35-readme-ko-narrow-top.jpg), [samples](chrome/36-readme-ko-narrow-samples.jpg), [installation](chrome/37-readme-ko-narrow-install.jpg); [EN top](chrome/38-readme-en-narrow-top.jpg), [samples](chrome/39-readme-en-narrow-samples.jpg), [installation](chrome/40-readme-en-narrow-install.jpg). |
| One-click image and gallery journey | PASS: clicked all six README thumbnails to the exact PNG image documents (10-original-1 through 6); each Back returned to rendered README. EN/KO gallery links each opened rendered Markdown in one click. All eight new gallery originals were separately clicked and their image-document URLs/dimensions observed. |
| Unified gallery | PASS: 54 linked PNG paths / 53 unique SHA-256 values, including six initials and two edits; byte inventory below. Readable [EN desktop](chrome/11-gallery-en-top.jpg), [KO desktop](chrome/13-gallery-ko-top.jpg), [EN narrow](chrome/17-gallery-en-narrow-top.jpg), [KO narrow](chrome/15-gallery-ko-narrow-top.jpg). Refinements remain qualified as mixed; [Sprig/COMMON](chrome/12-gallery-en-refinements.jpg). |
| Archive/status/credit continuity | PASS: [brands](chrome/47-gallery-brands-anchor-fixed.jpg), [icons](chrome/48-gallery-icons-anchor-fixed.jpg), [failed/indeterminate color history](chrome/49-gallery-color-statuses.jpg), [current/archive identity](chrome/50-gallery-identity.jpg); IP source/MIT notices readable in [EN](chrome/41-readme-en-credits.jpg) and [KO](chrome/34-readme-ko-credits.jpg). |
| Comparison controls | PASS: brand 1, app artwork 7, abstract 2, soft 3D 2; brand+soft3D 0 and clear empty message; Reset returns 8 and Artwork/Light/All kinds/All styles. Evidence 02, 19, 20, 23, [empty](chrome/29-combined-empty.jpg), [reset](chrome/30-reset-eight-defaults.jpg). |
| Contexts and sizes | PASS: artwork, [app home light](chrome/24-app-home-light.jpg)/[dark](chrome/25-app-home-dark.jpg), [web header dark](chrome/26-web-header-dark.jpg), [favicon dark](chrome/27-favicon-dark.jpg), visible 16/32/64/128px displays on [light](chrome/21-filtered-child-copy.jpg) and [dark](chrome/28-sizes-dark.jpg). These are CSS placements, not platform files. |
| Source and decision copy | PASS: expand then Copy reports success for Leaflet and filtered Relay v2. Paste into an empty owned editable localhost probe contained the exact source, PNG hash and four notes: [Leaflet](chrome/08-owned-copy-probe.jpg), [filtered child](chrome/22-filtered-child-copy-probe.jpg). No pre-existing clipboard content was read; fallback was not entered. |
| Real downloads | PASS: actual Chrome HTTP-link downloads of COMMON and Relay v2 PNG/prompt match source bytes and hashes, four files total. [Filtered download history](chrome/51-owned-downloads.jpg). On file URLs Chrome opens originals directly despite download attributes; this distinct behavior is recorded, not described as a file download. |
| Repeated navigation and identity | PASS after fix: Brand/Web header/Dark → COMMON PNG → Back restored 1 candidate and all controls; exact prompt → Back also restored them. Another child cycle preserved abstract/Favicon/Dark, card numbers 03/04 and relay v1/v2 revision 2. Reload legitimately resets defaults and retains all source identities. [Brand restoration](chrome/45-fixed-back-restoration-top.jpg), [child restoration](chrome/52-fixed-child-back-context.jpg). |
| Offline local page | PASS within scope: file page reloaded after owned HTTP server was closed, rendering all 8 candidates/default controls. Template has no remote asset dependency. [Final retained gallery](chrome/53-final-file-gallery.jpg). No network-disconnection/OS-setting change was performed. |

## Failures found, fixes and QA-tool corrections

1. **Resolved product failure:** Back initially restored Kind=Brand logo while showing all 8 cards. [First top evidence](chrome/06-back-filter-mismatch-top.jpg); screenshot 05 shows the accompanying expanded Leaflet card. Sent msg_6b7ca8d42c11. Source owner added pageshow synchronization; current index SHA-256 is 66e8ac8fd728f85a683ee041437a2a0fbe56a2f4b89902fb9eefc4c1d29610c6. Fresh Reload and actual Back passed; see [owner regression evidence](browser-restoration.md).
2. **Resolved layout finding:** both READMEs initially wrapped six 160px samples 5+1, leaving Relay alone ([EN](chrome/09-readme-en-desktop.jpg), [KO](chrome/14-readme-ko-desktop-initial.jpg)). Sent msg_02dc3d067706; the document owner split paragraphs after sample three. Final GitHub API rerender and both widths pass.
3. **Owned preview corrections:** GitHub API prefixes raw anchor IDs with user-content; initial local category clicks changed the URL but stayed at top (42/43). Normalized that prefix only in the four temporary wrappers; real category clicks then reached their headings (47/48/49/50). Production Markdown was not changed by this worker.
4. **Tool observations:** one scroll without coordinates was rejected before execution; re-grounded and used screenshot-derived coordinates. Two immediate probe lookups preceded completed localhost rendering; a subsequent fresh state exposed the editable field. Initial hostile setup used a missing private path and exited before source copy; restored a real portable Relay snapshot instead. Chrome ignored the downloads URL query as an input value, so the actual search field was set and the retained screenshot replaced with only our four entries. No unrelated download entry was opened, removed or retained in the final screenshot.

## Integrity and reused automated evidence

T3 recorded 622 passing tests, Ruff/format success, 0 basedpyright diagnostics and lock consistency. All 40 T3 Python test hashes still match. Of 73 installable source files, only the owner-fixed comparison template differs; its final hash is 2e9760669f0aa2d9d34267fce0241452f43de435c9c4985bce80be70afb309a3. The [fix receipt](browser-restoration.md) supplies 6 Node regressions and 58 targeted passing Python cases. This browser worker did not repeat the broad suite, make Python edits or invent build/LSP results.

Before GUI, 326 source/public/private-working files were hashed; final comparison found exactly four authorized concurrent changes: both READMEs, comparison template and generated index. All remaining 322 files, including native originals, exact prompts, six saved sessions, revisions, selection and approval state, match. All eight displayed comparison PNG/prompt hashes independently match their manifest. The historical snapshot warning remained visible. T2/T3 source-bound stale refusal is reused: stale_revision: Session relay: expected 1; current 2, exit 1, no output ([receipt](../../gallery-workflow/receipts/adversarial-checks.json)).

Final README SHA-256: EN eb1d9d2c75ec36cdc148bf546c35e9cf21b7ac4e8f302dcab58f98f161440c31; KO c3d10b3183b21e7466b1b83b4882a4922d629a921a3dc13f480d6833d6b13875.

## Nine adversarial classes

| Class | Actual evidence or bounded N/A |
|---|---|
| Malformed | Reused T2/T3 actual strict-selection CLI refusals: negative revision and missing artifact exit 1 without output, with source bytes unchanged; receipt linked above. No need to corrupt a real original. |
| Injection | Real helper generated a one-candidate page from a copied real Relay snapshot with literal closing-textarea/script/img-onerror strings and a local missing-image name. Chrome displayed escaped inert text, normal Relay art and no alert/foreign image; [evidence](chrome/31-hostile-note-inert.jpg). HTML contained one authored script and no injected img. No remote attack URL/native call. |
| Cancel/resume | Repeated original/prompt → Back and Reload exercised navigation/resumption; saved source bytes stayed unchanged. Cancelling a paid native job is N/A. |
| Stale | Historical warning/current IDs observed; source-bound CLI refusal reused above. Restoration bug recorded before its source-owner fix and retested against refreshed bytes. |
| Dirty/foreign ownership | Named additional window, exclusive temp root, exact new download inodes; unrelated window/tabs/download files/history preserved. |
| Hung | GitHub HTTP and actual helper subprocesses had 20-second bounds; short Sky calls/fresh state, no hung GUI call. In-process loopback server explicitly closed; no foreign PID killed. |
| Flaky | First failures retained or described before correction; no blind retry or native regeneration. Fresh state preceded every next action; automated failures were source-owner regressions, not suppressed. |
| Misleading success | Accessibility labels, inspected raw screenshots, actual image-document URLs, real downloads and exact hashes agree. HTTP alone was not accepted as visual PASS. |
| Repeated interruptions | Repeated tab changes, original/back/prompt/back/reload/filter/reset and two source-copy/paste cycles preserved identities and original state. Forced process destruction is N/A. |

## Resource registration and cleanup

The report registered resources before creation: new named window Gallery QA ctx_a04104359e84, primary gallery tab, temporary preview/probe tabs, /tmp/ll060-chrome-ctx_a04104359e84, localhost 8794, screenshot folder, and absent matching Downloads filenames. Exclusive root device/inode: 16777230/35031304. The HTTP server ran in the existing Computer Use node kernel PID 94939; only its server object was closed, and the kernel/Chrome app were preserved.

Completed: Chrome 100% zoom restored, temporary preview/probe/download-history tabs closed; exact four downloaded copies rehashed, inode-checked and removed with filesystem operations. Server.close completed with listening=false; lsof on port 8794 returned no listener. All temporary scripts, API responses, wrappers, copied Relay fixture and generated hostile page were removed after their evidence was recorded; the verified final receipt is appended below.

No artwork/export approval, strict HEX, actual font composition, vector, OS/platform package or universal small-size-readiness claim is made.

**Intentional retention:** exactly one user-viewing tab remains in Gallery QA ctx_a04104359e84 at file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/gallery-workflow/comparison/index.html, Artwork / Light / All kinds / All styles, 8 candidates, page top, zoom 100%. The pre-existing New Tab window was not changed or closed. This retained gallery needs no server.

<details><summary>GitHub Markdown API request receipts</summary>

Initial and final four requests all returned HTTP 200. Bodies were rendered in actual Chrome as described above.

~~~json
{
  "initial": [
    {
      "doc": "README.md",
      "status": 200,
      "sourceBytes": 5326,
      "responseBytes": 9939,
      "date": "Sun, 13 Sep 2026 00:49:16 GMT",
      "requestId": "8E98:6B16C:76923C:AFF706:6AA5F30C"
    },
    {
      "doc": "README.ko.md",
      "status": 200,
      "sourceBytes": 5974,
      "responseBytes": 10629,
      "date": "Sun, 13 Sep 2026 00:49:16 GMT",
      "requestId": "8E98:6B16C:769260:AFF737:6AA5F30C"
    },
    {
      "doc": "docs/gallery.md",
      "status": 200,
      "sourceBytes": 17847,
      "responseBytes": 22534,
      "date": "Sun, 13 Sep 2026 00:49:17 GMT",
      "requestId": "8E98:6B16C:769278:AFF759:6AA5F30C"
    },
    {
      "doc": "docs/gallery.ko.md",
      "status": 200,
      "sourceBytes": 19138,
      "responseBytes": 23825,
      "date": "Sun, 13 Sep 2026 00:49:17 GMT",
      "requestId": "8E98:6B16C:76929E:AFF785:6AA5F30D"
    }
  ],
  "final": [
    {
      "doc": "README.md",
      "status": 200,
      "sourceBytes": 5336,
      "responseBytes": 9959,
      "date": "Sun, 13 Sep 2026 00:54:35 GMT",
      "requestId": "925E:6B16C:76DD4C:B06B44:6AA5F44B"
    },
    {
      "doc": "README.ko.md",
      "status": 200,
      "sourceBytes": 5984,
      "responseBytes": 10649,
      "date": "Sun, 13 Sep 2026 00:54:36 GMT",
      "requestId": "925E:6B16C:76DD5E:B06B66:6AA5F44B"
    },
    {
      "doc": "docs/gallery.md",
      "status": 200,
      "sourceBytes": 17847,
      "responseBytes": 22534,
      "date": "Sun, 13 Sep 2026 00:54:36 GMT",
      "requestId": "925E:6B16C:76DD73:B06BB3:6AA5F44C"
    },
    {
      "doc": "docs/gallery.ko.md",
      "status": 200,
      "sourceBytes": 19138,
      "responseBytes": 23825,
      "date": "Sun, 13 Sep 2026 00:54:37 GMT",
      "requestId": "925E:6B16C:76DD98:B06BDC:6AA5F44C"
    }
  ]
}
~~~

</details>

<details><summary>Actual helper hostile-note receipt</summary>

~~~json
{
  "argv": [
    "run",
    "--locked",
    "python",
    "/Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/scripts/logo_project.py",
    "--workspace",
    "/tmp/ll060-chrome-ctx_a04104359e84/workspace",
    "compare-gallery",
    "--selection-file",
    "/tmp/ll060-chrome-ctx_a04104359e84/hostile-selection.json",
    "--output",
    "hostile-gallery"
  ],
  "stdout": "{\n  \"path\": \"hostile-gallery\",\n  \"index_path\": \"hostile-gallery/index.html\",\n  \"count\": 1\n}\n",
  "stderr": "",
  "htmlSha256": "605581f527a98934d2138ffbd53d250c1f0890ee00b542a160c3f2aca96fb1b8",
  "sourceStateUnchanged": true,
  "literal": "</textarea><script>alert(\"QA-INERT\")</script><img src=\"qa-inert-missing.png\" onerror=\"alert('QA-INERT')\">"
}
~~~

</details>

<details><summary>Actual downloaded bytes and original bindings</summary>

| File | Bytes | SHA-256 | Source |
|---|---:|---|---|
| 008.png | 850531 | 9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b | docs/gallery-workflow/comparison/images/008.png |
| 008.txt | 1697 | 1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a | docs/gallery-workflow/comparison/prompts/008.txt |
| 004.png | 898003 | a4066faa64d1f58024d1a44afb011694a1808b628b988ac71a0986e90069491d | docs/gallery-workflow/comparison/images/004.png |
| 004.txt | 2837 | 7c970c80e2167fb7677c82a3ffb360e17ad6569a28b341d881952fabbcd87cef | docs/gallery-workflow/comparison/prompts/004.txt |

</details>

<details><summary>All eight comparison source hashes</summary>

| Source | Revision | PNG SHA-256 | Exact prompt SHA-256 |
|---|---:|---|---|
| leaflet/v1 | 1 | 256b1ee1e25d9d8160ec0751db1453ae31990cecb5c2cd68570410c668cb6b4e | 0cad98ad36526c630cf05aa5fdde33d14e87a5545d1302f4be6ba4628e14faf5 |
| drip/v1 | 1 | 8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f | 67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d |
| relay/v1 | 2 | 6588c675013483c18bcc5fad4986c60e0ec21a78ef7c7591d055e2bb2b620b58 | 68f8163701caf21ec0e3c06b43128ff5f4fbc6c67183d5a8649a13e58f7ea813 |
| relay/v2 | 2 | a4066faa64d1f58024d1a44afb011694a1808b628b988ac71a0986e90069491d | 7c970c80e2167fb7677c82a3ffb360e17ad6569a28b341d881952fabbcd87cef |
| teum/v1 | 1 | a97780b67a304853d1b8795d6d3af8efdc4658d36703ed1cdabfa8710b73bf7e | 8312812f546902472a7eb0d98311e3e6c1b29fe58ba8a6d55cb826c61e03721c |
| sprig/v1 | 2 | 956577408a1a8986dd87cf430e44451739d93285352c5ebe5305d19ae216e222 | 9965898ff25f67a25e10e8002c7037852b7b6b99d0ca4b5a66513edd24c85094 |
| sprig/v2 | 2 | ed16c756532ef268880f4a1d281d87323bef707cecfe3c41b41397bef74e65ac | b83d6deeea4f252a27962f1171618ce72e58e7e807c0e6e9c6ba7b2652e6f22a |
| common/v1 | 1 | 9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b | 1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a |

</details>

<details><summary>54 unified-gallery displayed PNG paths and hashes</summary>

| Relative path | SHA-256 |
|---|---|
| docs/gallery-workflow/images/leaflet-v1.png | 256b1ee1e25d9d8160ec0751db1453ae31990cecb5c2cd68570410c668cb6b4e |
| docs/gallery-workflow/images/drip-v1.png | 8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f |
| docs/gallery-workflow/images/relay-v1.png | 6588c675013483c18bcc5fad4986c60e0ec21a78ef7c7591d055e2bb2b620b58 |
| docs/gallery-workflow/images/relay-v2.png | a4066faa64d1f58024d1a44afb011694a1808b628b988ac71a0986e90069491d |
| docs/gallery-workflow/images/teum-v1.png | a97780b67a304853d1b8795d6d3af8efdc4658d36703ed1cdabfa8710b73bf7e |
| docs/gallery-workflow/images/sprig-v1.png | 956577408a1a8986dd87cf430e44451739d93285352c5ebe5305d19ae216e222 |
| docs/gallery-workflow/images/sprig-v2.png | ed16c756532ef268880f4a1d281d87323bef707cecfe3c41b41397bef74e65ac |
| docs/gallery-workflow/images/common-v1.png | 9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b |
| docs/samples/items/01-luma/delivery/logo.png | 29c891de028f14cc8b8a715f105b2dd8b383fa647f691521bd0de25428f561ef |
| docs/samples/items/02-loop-lab/delivery/logo.png | c03e72b2362ed7071f52f441520a73fa9a92be697efa551ae14b3cb43da8aab4 |
| docs/samples/items/03-goyo/delivery/logo.png | 4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174 |
| docs/samples/items/04-bread-bloom/delivery/logo.png | 420ac19545143efbc4681b27b68fd074656da803869c746bd9c1eeb5678c9b8c |
| docs/samples/items/05-kite/delivery/logo.png | dffb886a7a72196a42df21e36afe23cfb6e07bd25bad35c69c44f4de5c0232a7 |
| docs/samples/items/06-miso/delivery/logo.png | 10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649 |
| docs/samples/items/07-northline/delivery/logo.png | 4eb27ce806aab3a32f58337c8b1fd00f6257f1abe970f98f12edfac6be423c06 |
| docs/samples/items/08-mulgyeol/delivery/logo.png | da97616502733dcef4b6b082d7746149793a22a576f3ad179a4da641d7ed66cf |
| docs/samples/items/09-fern/delivery/logo.png | db9066ee56c2789324aa7c53e5ba68b9e6c003ba3fe98578ea8b0e6196181e27 |
| docs/samples/items/10-nova-notes/delivery/logo.png | 0e26b2354a22faba2128d205c377abe09e590c82f895e2716fe51e0877715553 |
| docs/app-icons/images/ip-a1.png | 7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b |
| docs/app-icons/images/ip-a2.png | 74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd |
| docs/app-icons/images/ip-b1.png | 1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a |
| docs/app-icons/images/ip-b2.png | c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069 |
| docs/app-icons/images/ip-c1.png | 93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28 |
| docs/app-icons/images/ip-c2.png | 64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916 |
| docs/app-icons/images/pictogram.png | f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42 |
| docs/app-icons-quality-v1/images/pictogram-quality-v1.png | b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a |
| docs/app-icons/images/abstract.png | 7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4 |
| docs/app-icons-quality-v1/images/abstract-quality-v1.png | 93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b |
| docs/app-icons/images/monogram.png | 964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b |
| docs/app-icons-quality-v1/images/monogram-quality-v1.png | e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f |
| docs/app-icons/images/soft-3d.png | da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63 |
| docs/app-icons-quality-v1/images/soft-3d-quality-v1.png | ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2 |
| docs/app-icons/images/pixel-art.png | 87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5 |
| docs/app-icons-quality-v1/images/pixel-art-quality-v1.png | 29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328 |
| docs/colors/projects/sunroom/images/a-v1.png | e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb |
| docs/colors/projects/northline/images/a-v1.png | 3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534 |
| docs/colors/projects/grove/images/a-v1.png | 768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06 |
| docs/colors/projects/grove/images/a-v2.png | c60c605176b39f2b26f5299a2c99906dc5cc3e93e4716691e1e2b3154af33809 |
| docs/colors/projects/grove/images/a-v3.png | e0e0ba746f10f1ab0df53b6a2bda9c6d1f27d621efef68c4142d080407d0bc74 |
| docs/colors/projects/grove/images/a-v4.png | db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7 |
| docs/colors/projects/bamgyeol/images/a-v1.png | 083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941 |
| docs/colors/projects/bamgyeol/images/a-v2.png | 27e010082310501ac2ca6060aa8835ff3e75cd727bb971fb76f08b153884815b |
| docs/colors/projects/bamgyeol/images/a-v3.png | 0df1d666d480aae721f6ccab6fa7ff9d2388b015946e8e051381c86e9766c6f3 |
| docs/colors/projects/tide/images/a-v1.png | 2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d |
| docs/colors/projects/fieldnote/images/a-v1.png | 049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870 |
| docs/colors/projects/fieldnote/images/a-v2.png | 7dacc55d6f90f10f7206729f3f0d7cffc75b36ff6191e7430d8e01e2b76c40cb |
| docs/colors/projects/fieldnote/images/a-v3.png | 05398268ac42aa8d0da04976a9c6367df1bb186e1b3fe46e927db3e494ee65e2 |
| docs/colors/projects/white-bamgyeol/images/parent-v1.png | 083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941 |
| docs/colors/projects/white-bamgyeol/images/white-v1.png | 764557003be078c7e83fca85b7b40d43977edefa9ef46caf49f5279c403a3151 |
| docs/colors/projects/white-bamgyeol/images/white-v2.png | fda77d0af6c53c4d0d28099ca6568cbb7e877ac6045ea9ca6898bf77884a29a5 |
| docs/colors/projects/white-bamgyeol/images/white-v3.png | 0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd |
| assets/logo-land-studio.png | 11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3 |
| assets/logo.png | f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343 |
| assets/logo-transparent.png | ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7 |

</details>

<details><summary>Literal actual indexed Sky calls with fresh bound labels</summary>

Each listed numeric index came from a fresh full accessibility tree immediately before the action. Calls are evidence of completed GUI actions, not instructions to replay stale indexes. Keyboard navigation/zoom, screenshot-grounded scrolling and fresh get_app_state calls also occurred between these actions.

~~~js
sky.click({app:"com.google.Chrome",element_index:360}) // Window menu
sky.click({app:"com.google.Chrome",element_index:38}) // Name Window
sky.click({app:"com.google.Chrome",element_index:11}) // Name window OK
sky.click({app:"com.google.Chrome",element_index:42}) // 42 pop up button Kind, Value: All kinds
sky.click({app:"com.google.Chrome",element_index:2}) // 2 Brand logo, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:85}) // 85 link Description: Original PNG common / v1 · revision 1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/gallery-workflow/comparison/images/008.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:83}) // 83 disclosure triangle Source and decision text
sky.click({app:"com.google.Chrome",element_index:87}) // 87 button Copy source + notes
sky.set_value({app:"com.google.Chrome",element_index:10,value:"http://127.0.0.1:8794/probe"}); sky.press_key({app:"com.google.Chrome",key:"Return"})
sky.click({app:"com.google.Chrome",element_index:29}) // 29 text entry area (settable) Owned pasted notes
sky.set_value({app:"com.google.Chrome",element_index:10,value:"http://127.0.0.1:8794/render/README.md"}); sky.press_key({app:"com.google.Chrome",key:"Return"})
sky.click({app:"com.google.Chrome",element_index:51}) // 51 link Description: 고요 · Korean combination logo, Value: 127.0.0.1:8794/repo/docs/samples/items/03-goyo/delivery/logo.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:52}) // 52 link Description: COMMON · shared-workspace logo, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/common-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:53}) // 53 link Description: MISO · mascot, Value: 127.0.0.1:8794/repo/docs/samples/items/06-miso/delivery/logo.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:54}) // 54 link Description: Reading owl · IP character, Value: 127.0.0.1:8794/repo/docs/app-icons/images/ip-a1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:55}) // 55 link Description: Weather · revised pictogram, Value: 127.0.0.1:8794/repo/docs/app-icons-quality-v1/images/pictogram-quality-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:56}) // 56 link Description: Relay · abstract refinement with a wider opening, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/relay-v2.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:48}) // 48 link Description: See every original in one visual gallery →, Value: 127.0.0.1:8794/render/docs/gallery.md
sky.click({app:"com.google.Chrome",element_index:33}) // 33 link Description: 한국어, Value: 127.0.0.1:8794/render/docs/gallery.ko.md
sky.click({app:"com.google.Chrome",element_index:37}) // 37 link Description: Logo Land, Value: 127.0.0.1:8794/render/README.ko.md
sky.click({app:"com.google.Chrome",element_index:48}) // 48 link Description: 전체 원본을 한 페이지에서 보기 →, Value: 127.0.0.1:8794/render/docs/gallery.ko.md
sky.click({app:"com.google.Chrome",element_index:32}) // 32 link Description: English, Value: 127.0.0.1:8794/render/docs/gallery.md
sky.set_value({app:"com.google.Chrome",element_index:10,value:"http://127.0.0.1:8794/repo/docs/gallery-workflow/comparison/index.html"}); sky.press_key({app:"com.google.Chrome",key:"Return"})
sky.click({app:"com.google.Chrome",element_index:42}) // 42 pop up button Kind, Value: All kinds
sky.click({app:"com.google.Chrome",element_index:2}) // 2 Brand logo, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:85}) // 85 link Description: Original PNG common / v1 · revision 1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/comparison/images/008.png
sky.click({app:"com.google.Chrome",element_index:87}) // 87 link Description: Exact prompt common / v1 · revision 1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/comparison/prompts/008.txt
sky.click({app:"com.google.Chrome",element_index:43}) // 43 pop up button Kind, Value: Brand logo
sky.click({app:"com.google.Chrome",element_index:3}) // 3 App artwork, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:47}) // 47 pop up button Style, Value: All styles
sky.click({app:"com.google.Chrome",element_index:2}) // 2 abstract, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:122}) // 122 link Description: Original PNG relay / v2 · revision 2, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/comparison/images/004.png
sky.click({app:"com.google.Chrome",element_index:123}) // 123 link Description: Exact prompt relay / v2 · revision 2, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/comparison/prompts/004.txt
sky.click({app:"com.google.Chrome",element_index:120}) // 120 disclosure triangle Source and decision text
sky.click({app:"com.google.Chrome",element_index:124}) // 124 button Copy source + notes
sky.set_value({app:"com.google.Chrome",element_index:10,value:"http://127.0.0.1:8794/probe"}); sky.press_key({app:"com.google.Chrome",key:"Return"})
sky.click({app:"com.google.Chrome",element_index:30}) // 30 text entry area (settable) Owned pasted notes
sky.click({app:"com.google.Chrome",element_index:47}) // 47 pop up button Style, Value: abstract
sky.click({app:"com.google.Chrome",element_index:7}) // 7 soft 3d, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:35}) // 35 pop up button Preview, Value: Artwork
sky.click({app:"com.google.Chrome",element_index:2}) // 2 App home, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:39}) // 39 pop up button Surround, Value: Light
sky.click({app:"com.google.Chrome",element_index:2}) // 2 Dark, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:35}) // 35 pop up button Preview, Value: App home
sky.click({app:"com.google.Chrome",element_index:3}) // 3 Web header, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:35}) // 35 pop up button Preview, Value: Web header
sky.click({app:"com.google.Chrome",element_index:4}) // 4 Favicon / tab, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:43}) // 43 pop up button Kind, Value: App artwork
sky.click({app:"com.google.Chrome",element_index:2}) // 2 Brand logo, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:49}) // 49 button Reset comparison
sky.set_value({app:"com.google.Chrome",element_index:10,value:"file:///tmp/ll060-chrome-ctx_a04104359e84/workspace/hostile-gallery/index.html"}); sky.press_key({app:"com.google.Chrome",key:"Return"})
sky.click({app:"com.google.Chrome",element_index:84}) // 84 disclosure triangle Source and decision text
sky.set_value({app:"com.google.Chrome",element_index:10,value:"http://127.0.0.1:8794/render/README.md"}); sky.press_key({app:"com.google.Chrome",key:"Return"})
sky.click({app:"com.google.Chrome",element_index:40}) // 40 link Description: 한국어, Value: 127.0.0.1:8794/render/README.ko.md
sky.click({app:"com.google.Chrome",element_index:39}) // 39 link Description: English, Value: 127.0.0.1:8794/render/README.md
sky.click({app:"com.google.Chrome",element_index:49}) // 49 link Description: See every original in one visual gallery →, Value: 127.0.0.1:8794/render/docs/gallery.md
sky.click({app:"com.google.Chrome",element_index:42}) // 42 link Description: 10 brands, Value: 127.0.0.1:8794/render/docs/gallery.md#brands
sky.click({app:"com.google.Chrome",element_index:44}) // 44 link Description: 16 app icons, Value: 127.0.0.1:8794/render/docs/gallery.md#app-icons
sky.click({app:"com.google.Chrome",element_index:189}) // 189 tab (settable, boolean) Description: Logo Land / six directions, two refinements · Logo Land comparison - Memory usage - 89.5 MB, Value: off
sky.click({app:"com.google.Chrome",element_index:6}) // 6 button Reload
sky.click({app:"com.google.Chrome",element_index:49}) // 49 button Reset comparison
sky.click({app:"com.google.Chrome",element_index:43}) // 43 pop up button Kind, Value: All kinds
sky.click({app:"com.google.Chrome",element_index:2}) // 2 Brand logo, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:35}) // 35 pop up button Preview, Value: Artwork
sky.click({app:"com.google.Chrome",element_index:3}) // 3 Web header, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:39}) // 39 pop up button Surround, Value: Light
sky.click({app:"com.google.Chrome",element_index:2}) // 2 Dark, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:88}) // 88 link Description: Original PNG common / v1 · revision 1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/gallery-workflow/comparison/images/008.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:89}) // 89 link Description: Exact prompt common / v1 · revision 1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/gallery-workflow/comparison/prompts/008.txt
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:6}) // 6 button Reload
sky.click({app:"com.google.Chrome",element_index:347}) // 347 tab (settable, boolean) Description: GFM local QA — docs/gallery.md - Memory usage - 337 MB, Value: off
sky.click({app:"com.google.Chrome",element_index:6}) // 6 button Reload
sky.click({app:"com.google.Chrome",element_index:42}) // 42 link Description: 10 brands, Value: 127.0.0.1:8794/render/docs/gallery.md#brands
sky.click({app:"com.google.Chrome",element_index:44}) // 44 link Description: 16 app icons, Value: 127.0.0.1:8794/render/docs/gallery.md#app-icons
sky.click({app:"com.google.Chrome",element_index:33}) // 33 link Description: Sprig · gentle plant care · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/sprig-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:34}) // 34 link Description: Sprig · gentle plant care · v2, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/sprig-v2.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:42}) // 42 link Description: COMMON · shared workspace · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/common-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:56}) // 56 link Description: Leaflet · reading fox · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/leaflet-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:62}) // 62 link Description: Drip · water reminder · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/drip-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:68}) // 68 link Description: Relay · quiet handoff · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/relay-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:69}) // 69 link Description: Relay · quiet handoff · v2, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/relay-v2.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:77}) // 77 link Description: 틈 · notes · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/teum-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:83}) // 83 link Description: Sprig · gentle plant care · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/sprig-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:84}) // 84 link Description: Sprig · gentle plant care · v2, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/sprig-v2.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:92}) // 92 link Description: COMMON · shared workspace · v1, Value: 127.0.0.1:8794/repo/docs/gallery-workflow/images/common-v1.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:46}) // 46 link Description: 8 color cases, Value: 127.0.0.1:8794/render/docs/gallery.md#colors
sky.click({app:"com.google.Chrome",element_index:48}) // 48 link Description: Identity and archive, Value: 127.0.0.1:8794/render/docs/gallery.md#identity
sky.set_value({app:"com.google.Chrome",element_index:10,value:"chrome://downloads/?q=127.0.0.1%3A8794"}); sky.press_key({app:"com.google.Chrome",key:"Return"})
sky.click({app:"com.google.Chrome",element_index:113}) // 113 tab (settable, boolean) Description: Logo Land / six directions, two refinements · Logo Land comparison - Memory usage - 111 MB, Value: off
sky.click({app:"com.google.Chrome",element_index:47}) // 47 pop up button Style, Value: All styles
sky.click({app:"com.google.Chrome",element_index:2}) // 2 abstract, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:35}) // 35 pop up button Preview, Value: Artwork
sky.click({app:"com.google.Chrome",element_index:4}) // 4 Favicon / tab, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:39}) // 39 pop up button Surround, Value: Light
sky.click({app:"com.google.Chrome",element_index:2}) // 2 Dark, ID: menuItemSelected:
sky.click({app:"com.google.Chrome",element_index:126}) // 126 link Description: Original PNG relay / v2 · revision 2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/gallery-workflow/comparison/images/004.png
sky.click({app:"com.google.Chrome",element_index:4}) // 4 button Back
sky.click({app:"com.google.Chrome",element_index:135}) // 135 tab (settable, boolean) Description: Download History - Memory usage - 330 MB, Value: off
sky.click({app:"com.google.Chrome",element_index:49}) // 49 button Reset comparison
sky.click({app:"com.google.Chrome",element_index:6}) // 6 button Reload
~~~

</details>

<details><summary>Raw screenshot inventory</summary>

All retained screenshots were copied byte-for-byte from screenshot.url using node:fs/promises and fileURLToPath, emitted and visually inspected. No crop, resize, recompression or pixel edit was applied. Screenshots 42/43 document the corrected local-wrapper anchor issue; 05/06 and 09/14 preserve initial product findings. The final 51 image contains only owned downloads.

| Screenshot | Bytes | SHA-256 |
|---|---:|---|
| [01-comparison-initial.jpg](chrome/01-comparison-initial.jpg) | 114937 | 618e660c5303070eb2e8b12505a2ca5ee52aa0cdad6dab315029c7bda9bb18e5 |
| [02-brand-filter.jpg](chrome/02-brand-filter.jpg) | 101333 | b07747cd7ac7a0da6b3348ea891011e056760e198d48493fffc6ad66d94e0727 |
| [03-file-png-opens-original.jpg](chrome/03-file-png-opens-original.jpg) | 87712 | 71267942e177675b61f89375575bf61534ada5fd2fc19709b5b8923a325a12ee |
| [05-first-back-filter-mismatch.jpg](chrome/05-first-back-filter-mismatch.jpg) | 169170 | 83a67f9fbcc323e82b44091e9c1fa5ddb57d2b72bb9b000034558eea7256b136 |
| [06-back-filter-mismatch-top.jpg](chrome/06-back-filter-mismatch-top.jpg) | 115838 | 0b7811baef520825ec01f3a15a32ff1a7d22df7d49654a2ae6a10ad5a2f6eb4b |
| [07-copy-outcome.jpg](chrome/07-copy-outcome.jpg) | 148292 | 80b7383c4f43ca66ab659766becbf6e372f80ebf64f2491f5df8045f86116c7f |
| [08-owned-copy-probe.jpg](chrome/08-owned-copy-probe.jpg) | 91757 | 5d893f43aea7b70ac98c7b710a7c10df5d4d7d6331fdde061a27d8aa123b1087 |
| [09-readme-en-desktop.jpg](chrome/09-readme-en-desktop.jpg) | 103157 | d347a5d9d5cfe4a96b070a1a6cdb3a0b25a4c2ab47f75aa93851b616de546954 |
| [10-original-1.jpg](chrome/10-original-1.jpg) | 71327 | 314bb60e79dca07862ca7bae6f1b8d130120dff379e93a12cecfa7c59d020088 |
| [10-original-2.jpg](chrome/10-original-2.jpg) | 86561 | ef4336595a8ccf08c6fbd9c1fc847f091a94db74dd8a40e790d1e8005d753875 |
| [10-original-3.jpg](chrome/10-original-3.jpg) | 91616 | 8003f92162ed4a1b0b1159088d375254b4fbf68b12545ee4515d8a05c6e9b8d1 |
| [10-original-4.jpg](chrome/10-original-4.jpg) | 83409 | fbf4e5d2127d986ffd083244b1104b510becc5a768c52533db84e493a3257074 |
| [10-original-5.jpg](chrome/10-original-5.jpg) | 64872 | 8f38f40167b2e33d11e3218d3d181ca9fdeee90aae3ef67dd5d03ecc87aa94ee |
| [10-original-6.jpg](chrome/10-original-6.jpg) | 67190 | 54b62009f7569b27813daf8c1e898a310f23e894b0eeceecbb13c1689333191d |
| [11-gallery-en-top.jpg](chrome/11-gallery-en-top.jpg) | 123127 | 44280de270b176c1f5f0b328c6970e62e622495261a2496cd3a0a4472c607159 |
| [12-gallery-en-refinements.jpg](chrome/12-gallery-en-refinements.jpg) | 104406 | e7ed4452b02eea5ba61f5f5581b111d00473c3a0d9456eef64163b7129ba8698 |
| [13-gallery-ko-top.jpg](chrome/13-gallery-ko-top.jpg) | 114401 | a03d3f7b6603f575ecf62c66430b4deec5511b39744f3a3e1ce8e122c0a31608 |
| [14-readme-ko-desktop-initial.jpg](chrome/14-readme-ko-desktop-initial.jpg) | 101982 | 5dbdb63ea6ed7a36785b8c27d54d875c3d3defa25b26a0cae99bbc55e64cca57 |
| [15-gallery-ko-narrow-top.jpg](chrome/15-gallery-ko-narrow-top.jpg) | 155106 | 5a88a053ab880efd875aa29547660e4d81eb7445223ce77a5789ce527ca33209 |
| [16-gallery-ko-narrow-content.jpg](chrome/16-gallery-ko-narrow-content.jpg) | 103628 | 97415ed100d0bedc6cc5cdd19e47fec1bc5d2550aba82a665cd08478cb5db9b6 |
| [17-gallery-en-narrow-top.jpg](chrome/17-gallery-en-narrow-top.jpg) | 152319 | 45cd7839619ae1f7c537f07635d4cceca6d020efd954012c836e848b8ceed551 |
| [18-gallery-en-narrow-content.jpg](chrome/18-gallery-en-narrow-content.jpg) | 73484 | 44409edaa359eacc1b1dd165996edca95af16281299e350a418d34b3a6541358 |
| [19-app-artwork-seven.jpg](chrome/19-app-artwork-seven.jpg) | 115558 | 3f55ecd72ebbd77d05def054b50bb7f9ff22444b948cd3f31199d13c726fd7d2 |
| [20-abstract-two.jpg](chrome/20-abstract-two.jpg) | 105041 | 11ce78870cb49e517925570dabc6fb745fbe74afde9561e88f6443340fdb5b9f |
| [21-filtered-child-copy.jpg](chrome/21-filtered-child-copy.jpg) | 167903 | 65ec92f9bc3d68ee63aeb7b265859fc67fe2c3c77a7779e27157036737b7211b |
| [22-filtered-child-copy-probe.jpg](chrome/22-filtered-child-copy-probe.jpg) | 118255 | b8c3c4bb1381cac696e2617aecc983c127876f7fbbe2b5486edfc456a2427597 |
| [23-soft3d-two.jpg](chrome/23-soft3d-two.jpg) | 104063 | 7aa4402699457c18582a4812997a9fb77e9e7425eb98406df3c608ec4bf3ac6f |
| [24-app-home-light.jpg](chrome/24-app-home-light.jpg) | 101530 | a33b07d05937560d5d205f6c47f574f37f9682b5fb510527e59827910f74bacd |
| [25-app-home-dark.jpg](chrome/25-app-home-dark.jpg) | 106261 | da94bd0547b9f80a7d5ee14fdbc4e3339cf79119b273962469386f7926adf34f |
| [26-web-header-dark.jpg](chrome/26-web-header-dark.jpg) | 106465 | 2e9b0f36e254dc22dcaa8383d02bca2b97c45bdb86b72aaff1e9603aef699d03 |
| [27-favicon-dark.jpg](chrome/27-favicon-dark.jpg) | 106171 | d062e1a2f121e93f20c7fd631365513ed003d458a5c7090e751d28b431f52c62 |
| [28-sizes-dark.jpg](chrome/28-sizes-dark.jpg) | 149041 | a65175bf94ba22ae3cf64d3145bc606df823d5dcb4a4260e48a6eaf581724bed |
| [29-combined-empty.jpg](chrome/29-combined-empty.jpg) | 95842 | 60e030e48b8aa1887241f311b1036d0ae8195a7bc1c6b88db0c3c619f016445e |
| [30-reset-eight-defaults.jpg](chrome/30-reset-eight-defaults.jpg) | 114478 | 802a375ac88d6ec3d5637c6ddbf8b721a4d8229f9435a10118f1bebe8116423a |
| [31-hostile-note-inert.jpg](chrome/31-hostile-note-inert.jpg) | 157321 | 8bdbfa1ec606ba48b2dfb9f966e75f2c0315a76b18f2301c54321db59ab806ec |
| [32-readme-en-final-desktop.jpg](chrome/32-readme-en-final-desktop.jpg) | 103097 | ea83905e94cb7681f4ede8916fc5f8383b85e68f94b135b7a4d7189319b9c09e |
| [33-readme-ko-final-desktop.jpg](chrome/33-readme-ko-final-desktop.jpg) | 103211 | 7942b811ef764a4722712dd49db7239a5eef38019eb1ed3b10c69df1afb297a0 |
| [34-readme-ko-credits.jpg](chrome/34-readme-ko-credits.jpg) | 131596 | 0e399d6bd53ce8b00230b7022a352b4bb69062f5bcfc384750237fe349d3c850 |
| [35-readme-ko-narrow-top.jpg](chrome/35-readme-ko-narrow-top.jpg) | 120546 | 59bccd974c30f56a4b4100c4213285ed84e0604c06458b102b2cbcaf311fe55a |
| [36-readme-ko-narrow-samples.jpg](chrome/36-readme-ko-narrow-samples.jpg) | 119733 | 619f2aa9986bbf357e8535a3f7237f13668a2b6184dc82b0b7148005be6353c1 |
| [37-readme-ko-narrow-install.jpg](chrome/37-readme-ko-narrow-install.jpg) | 128201 | 9298bdf64d8726ae43e369737b60e12671572b58d448415ed7b3a8cc5cae1d02 |
| [38-readme-en-narrow-top.jpg](chrome/38-readme-en-narrow-top.jpg) | 112540 | fcd96379b4e8a98ffddd311e2765cdb25a0c22d9f70c75b06cf1d2e25e37edef |
| [39-readme-en-narrow-samples.jpg](chrome/39-readme-en-narrow-samples.jpg) | 123644 | 7a3c235c8c417c8a8ff591cdeced820a269c13b9782ac48a31772edc264d2f77 |
| [40-readme-en-narrow-install.jpg](chrome/40-readme-en-narrow-install.jpg) | 132233 | c837e89d192d4317b575fa6a9d2f27990d87c3bb6b68587138efcef67aa7d9c1 |
| [41-readme-en-credits.jpg](chrome/41-readme-en-credits.jpg) | 142595 | baef450ae7d7620c4eee804fc949da8b159fb3fb9887797d83debc1776fee6a9 |
| [42-gallery-brands.jpg](chrome/42-gallery-brands.jpg) | 123715 | a65a1033f71c30ec2a10360d39877676737a531ece3fe294d9f314290bccf411 |
| [43-gallery-icons.jpg](chrome/43-gallery-icons.jpg) | 123897 | 080f8072a03c7ae6727b1be1c81ec08a755c2df0e906363d0dea43c3508897f0 |
| [44-fixed-back-restoration.jpg](chrome/44-fixed-back-restoration.jpg) | 104895 | a2874750b4b4c0a0f562b7b770a61f3c8829b3c0e7aede8012d3ce3fcacbdde6 |
| [45-fixed-back-restoration-top.jpg](chrome/45-fixed-back-restoration-top.jpg) | 104553 | 92fcce84d83a35b963fe3acd365e16de24d60ecb835e8b24647f09f92175360f |
| [46-fixed-reload-controls.jpg](chrome/46-fixed-reload-controls.jpg) | 168696 | c577cca9291e197abc5bf39a98afc63084921f37766685c8751592c440a442f5 |
| [47-gallery-brands-anchor-fixed.jpg](chrome/47-gallery-brands-anchor-fixed.jpg) | 68641 | 492c01936d3d4fb0e248da19e8542d87cce5f2f0a42c440b72d36924bdfd089b |
| [48-gallery-icons-anchor-fixed.jpg](chrome/48-gallery-icons-anchor-fixed.jpg) | 104167 | f8e2bd6f40b08ebb5d5d07259d92ddf752aae020a75bc07c76b50812f4d8547f |
| [49-gallery-color-statuses.jpg](chrome/49-gallery-color-statuses.jpg) | 114858 | aa2d79a25d4750eddde0b724289bd1b505e20c8afdacfa6f6470eb90fd4e6684 |
| [50-gallery-identity.jpg](chrome/50-gallery-identity.jpg) | 140914 | ba5bd05283d312145c14778df831a99bc7f9930a90d6688101072c923e5dafd4 |
| [51-owned-downloads.jpg](chrome/51-owned-downloads.jpg) | 65182 | 0bb6769813a817b1e4d5c3914cfef9121984333415903c702e738fc771b67acd |
| [52-fixed-child-back-context.jpg](chrome/52-fixed-child-back-context.jpg) | 108072 | 16057c3fb466dec53821c979165aa91421457cdb4311cd6857ab3996e7620139 |
| [53-final-file-gallery.jpg](chrome/53-final-file-gallery.jpg) | 115421 | 27aa48caabeced997d52a42c19ab885d175b54f31c097b8215aff62d1a7d5f42 |

</details>

Final cleanup receipt: owned temporary root identity was rechecked as device/inode 16777230/35031304, then removed; nonexistence verified. All four new Downloads filenames are absent. Port 8794 has no listener. Final file-gallery screenshot was taken after server shutdown; exactly one requested gallery tab is intentionally retained. No outstanding product finding or owned temporary resource remains.
