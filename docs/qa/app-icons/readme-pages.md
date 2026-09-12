# Existing sample pages: D1-A verification

Task `task_615f1548b42e`, dispatch `ctx_06f4bafd6edb`, observed 2026-09-12 18:15:25 UTC. Scope: 42 public Markdown pages (21 full EN/KO pairs) plus this report. Implemented the final D1-A contract in `plans/logo-land-app-icons.md` and the complete `docs/research/readme-structure.md` mapping. No generation, image editing, installation, commit, browser or child-agent work was performed.

## Outcome and execution checklist

- Complete: baseline and existing download validation before public-page edits.
- Complete: ten individual brand pages, seven color project pages, two category indexes, generic transparency and current brand, each in English and Korean.
- Complete: owned-page local paths, download bytes, language parity and anchor checks, including the disposable broken-download sentinel.
- Complete: bounded HTTP requests, exact response bytes, Korean UTF-8 and reload check.
- Complete: stale hash recheck and owned server termination; temporary-directory removal is recorded below after transcription.

The worktree was already dirty at HEAD `ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5`. Only the existing `docs/brand/README.md` was rewritten; the other 41 public pages were absent before this task. Existing original images, prompts, HTML/JS/CSS, manifest/session/history records and deliveries were preserved. The prior current-brand page had 40 lines, 4397 bytes and SHA-256 `2a2ce0f0d4c11b81df9430711318202768bdb2e4a7e764540ff06430a8f45083`; its `historical-identity` heading anchor is retained explicitly in both final brand pages.

## Before/after page map and EN/KO matrix

Counts below are editorial measurements: physical lines and whitespace-delimited words including Markdown, not functional tests or a language-quality score. Every pair has equal normalized navigation/image/download targets and fully localized prose, request, headings and alt text. Brand names and existing original filenames remain unchanged. Old English-only brand guides and historical records are linked as existing artifacts rather than duplicated translations.

| English page | Korean counterpart | Before | EN lines / words | KO lines / words | Pair |
|---|---|---|---|---|---|
| `docs/brand/README.md` | `docs/brand/README.ko.md` | Existing EN, no KO | 20 / 104 | 20 / 96 | PASS |
| `docs/colors/README.md` | `docs/colors/README.ko.md` | Neither page existed | 20 / 183 | 20 / 176 | PASS |
| `docs/colors/projects/bamgyeol/README.md` | `docs/colors/projects/bamgyeol/README.ko.md` | Neither page existed | 19 / 85 | 19 / 80 | PASS |
| `docs/colors/projects/fieldnote/README.md` | `docs/colors/projects/fieldnote/README.ko.md` | Neither page existed | 19 / 83 | 19 / 74 | PASS |
| `docs/colors/projects/grove/README.md` | `docs/colors/projects/grove/README.ko.md` | Neither page existed | 31 / 128 | 31 / 127 | PASS |
| `docs/colors/projects/northline/README.md` | `docs/colors/projects/northline/README.ko.md` | Neither page existed | 19 / 95 | 19 / 83 | PASS |
| `docs/colors/projects/sunroom/README.md` | `docs/colors/projects/sunroom/README.ko.md` | Neither page existed | 19 / 88 | 19 / 76 | PASS |
| `docs/colors/projects/tide/README.md` | `docs/colors/projects/tide/README.ko.md` | Neither page existed | 19 / 96 | 19 / 84 | PASS |
| `docs/colors/projects/white-bamgyeol/README.md` | `docs/colors/projects/white-bamgyeol/README.ko.md` | Neither page existed | 19 / 82 | 19 / 73 | PASS |
| `docs/samples/README.md` | `docs/samples/README.ko.md` | Neither page existed | 22 / 115 | 22 / 114 | PASS |
| `docs/samples/items/01-luma/README.md` | `docs/samples/items/01-luma/README.ko.md` | Neither page existed | 19 / 82 | 19 / 74 | PASS |
| `docs/samples/items/02-loop-lab/README.md` | `docs/samples/items/02-loop-lab/README.ko.md` | Neither page existed | 19 / 81 | 19 / 73 | PASS |
| `docs/samples/items/03-goyo/README.md` | `docs/samples/items/03-goyo/README.ko.md` | Neither page existed | 19 / 89 | 19 / 76 | PASS |
| `docs/samples/items/04-bread-bloom/README.md` | `docs/samples/items/04-bread-bloom/README.ko.md` | Neither page existed | 19 / 87 | 19 / 81 | PASS |
| `docs/samples/items/05-kite/README.md` | `docs/samples/items/05-kite/README.ko.md` | Neither page existed | 19 / 81 | 19 / 76 | PASS |
| `docs/samples/items/06-miso/README.md` | `docs/samples/items/06-miso/README.ko.md` | Neither page existed | 19 / 84 | 19 / 80 | PASS |
| `docs/samples/items/07-northline/README.md` | `docs/samples/items/07-northline/README.ko.md` | Neither page existed | 19 / 93 | 19 / 82 | PASS |
| `docs/samples/items/08-mulgyeol/README.md` | `docs/samples/items/08-mulgyeol/README.ko.md` | Neither page existed | 19 / 84 | 19 / 78 | PASS |
| `docs/samples/items/09-fern/README.md` | `docs/samples/items/09-fern/README.ko.md` | Neither page existed | 19 / 80 | 19 / 76 | PASS |
| `docs/samples/items/10-nova-notes/README.md` | `docs/samples/items/10-nova-notes/README.ko.md` | Neither page existed | 19 / 84 | 19 / 83 | PASS |
| `docs/samples/transparency.md` | `docs/samples/transparency.ko.md` | Neither page existed | 19 / 98 | 19 / 89 | PASS |

Previous entrances remain `docs/samples/index.html`, `docs/colors/index.html`, their existing project HTML, and the historical `docs/transparency/README.md`. New category tables expose all ten existing sample IDs and all eight color cases across seven projects. GROVE original and warmer sections share the same page; the original alone has ZIP/guide links. The earlier NORTHLINE `NL` page and later full-name NORTHLINE page link to each other with explicit distinction.

## Local paths, downloads and anchors

Final owned public-page scan: **42 pages, 412 link/image references, 21 EN/KO pairs, 47 distinct public download targets, zero unexpected failures**. The original catalog and `data.js` parse to identical JSON; all 18 showcased sample/color PNG hashes matched recorded metadata before edits. All 54 baseline file targets existed with nonzero bytes. Fourteen existing ZIPs were opened before edits and their `logo.png` and `brand-guide.md` entries matched the sibling files byte for byte; final ZIP CRC checks also passed. All three color delivery PNGs match their showcase assets, and the current brand hero matches its delivery PNG exactly. PNG signatures and actual IHDR dimensions were read from the unchanged bytes; guide UTF-8 was checked. The original brand page's 24 outgoing links still resolve.

This is an owned-page check, not an all-repository link claim. The only allowed pending destination is root-owned `docs/README.ko.md`, with these exact four incoming links at the final check:

| Source | Authored target | Missing destination / owner |
|---|---|---|
| `docs/brand/README.ko.md` | `../README.ko.md` | `docs/README.ko.md` / D1-C |
| `docs/colors/README.ko.md` | `../README.ko.md` | `docs/README.ko.md` / D1-C |
| `docs/samples/README.ko.md` | `../README.ko.md` | `docs/README.ko.md` / D1-C |
| `docs/samples/transparency.ko.md` | `../README.ko.md` | `docs/README.ko.md` / D1-C |

D1-C was notified through Orca status `msg_4b23c2c35ec4`; it owns creating that destination and root verification. All other page targets exist. Final Chrome navigation and representative Markdown rendering belong to the separately dispatched Chrome owner; this worker did not claim hosted GitHub or browser-render evidence.

| Anchor family | English | Korean | Evidence |
|---|---|---|---|
| Brand historical identity | `docs/brand/README.md#historical-identity` | `docs/brand/README.ko.md#historical-identity` | Explicit anchor present; legacy target exists |
| GROVE original | `docs/colors/projects/grove/README.md#original` | `docs/colors/projects/grove/README.ko.md#original` | Explicit anchor; original PNG and original package only |
| GROVE warmer | `docs/colors/projects/grove/README.md#warmer` | `docs/colors/projects/grove/README.ko.md#warmer` | Explicit anchor; warmer PNG only; failure stated |
| Original color histories | `index.html#artifact-a-v1` in sunroom, northline, bamgyeol, tide, fieldnote; white-bamgyeol uses `#artifact-white-v3` | Same unchanged HTML targets | IDs checked in actual existing HTML; GROVE links complete local history |

## Actual HTTP evidence

Owned server: PID `14511`, exec session `86834`, port `8802`, bound only to `127.0.0.1`, serving this repository. Temporary root and port were registered before creation; PID/command were recorded in the owned temporary root before fetching. Each request used `curl -i --fail --silent --show-error --connect-timeout 2 --max-time 10`. Exact required first request:

```sh
curl -i --fail --silent --show-error --connect-timeout 2 --max-time 10 http://127.0.0.1:8802/docs/samples/items/03-goyo/README.md -o /tmp/ll-readme-pages/goyo.http
```

For each response, the header/body separator was parsed, `200 OK` required and body compared directly to the final file. The Korean body decoded as valid UTF-8 and contained the actual `명상 스튜디오` text. Two independent GETs of the English page produced identical bodies.

| Capture | Requested repository path | HTTP | Body bytes | Body SHA-256 |
|---|---|---|---|---|
| `goyo.http` | `docs/samples/items/03-goyo/README.md` | 200 | 737 | `eb2fc0833a115c9bc217ece47c9e1d714fabe2eed2fae6ad64c158f4f5fb7fe3` |
| `goyo-ko.http` | `docs/samples/items/03-goyo/README.ko.md` | 200 | 841 | `bd0601f9342d2e8d03cf359705f795e763935cc7f8b6405402ad70ee973b2806` |
| `goyo-png.http` | `docs/samples/items/03-goyo/delivery/logo.png` | 200 | 898170 | `4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174` |
| `grove-png.http` | `docs/colors/assets/03-grove.png` | 200 | 653299 | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `grove-zip.http` | `docs/colors/deliveries/grove/logo-package.zip` | 200 | 644827 | `61fed8500b5b562fa28e34a65d79bfd585c59132adc298a7af5a0e8413784d12` |
| `goyo-reload.http` | `docs/samples/items/03-goyo/README.md` | 200 | 737 | `eb2fc0833a115c9bc217ece47c9e1d714fabe2eed2fae6ad64c158f4f5fb7fe3` |

Captured response headers, transcribed before removing temporary response files:

`goyo.http`

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:12:59 GMT
Content-type: application/octet-stream
Content-Length: 737
Last-Modified: Sat, 12 Sep 2026 18:11:29 GMT
```

`goyo-ko.http`

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:12:59 GMT
Content-type: application/octet-stream
Content-Length: 841
Last-Modified: Sat, 12 Sep 2026 18:11:29 GMT
```

`goyo-png.http`

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:12:59 GMT
Content-type: image/png
Content-Length: 898170
Last-Modified: Sat, 12 Sep 2026 13:16:00 GMT
```

`grove-png.http`

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:12:59 GMT
Content-type: image/png
Content-Length: 653299
Last-Modified: Sat, 12 Sep 2026 15:41:45 GMT
```

`grove-zip.http`

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:12:59 GMT
Content-type: application/zip
Content-Length: 644827
Last-Modified: Sat, 12 Sep 2026 15:39:50 GMT
```

`goyo-reload.http`

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:12:59 GMT
Content-type: application/octet-stream
Content-Length: 737
Last-Modified: Sat, 12 Sep 2026 18:11:29 GMT
```

## Factual result and nine-class checks

| Class | Actual observation or precise non-applicability |
|---|---|
| Missing/broken download | Disposable `/tmp/ll-readme-pages/missing-download.md` linked `never-delivered.zip`; the same path checker reported one `missing file`, as expected; no repository original was moved or removed. |
| Untrusted prompt text | Saved user/native prompt strings were parsed and hashed as data; no stored instruction was executed. A disposable Markdown blockquote containing literal shell substitution and an instruction-like phrase remained byte-identical; no sentinel file appeared. Public requests are blockquoted examples; original prompt files retain their old command names and exact bytes. |
| Resume/reload | Second independent HTTP GET of final Goyo EN returned the same body hash. Static pages have no application/session state to resume; no fake app-state case was asserted. |
| Stale source | Baseline hashes for 60 source/guidance/assets files were re-read after authoring and HTTP QA: 0 changes; all 320 protected original files also matched. Final integration remains the root owner's responsibility if concurrent source work later changes them. |
| Dirty ownership | Baseline already included root/source/skill/app-icon work from others; only the assigned 42 public Markdown paths and this report were written in the repository. No reset, checkout, restore, install, commit or unrelated edit. Baseline dirty inventory is retained below. |
| Bounded HTTP | Six GETs with two-second connection and ten-second total limits each returned 200 and exact final bytes; no unbounded retry or wait. Owned server was stopped by its recorded PID after rechecking its exact command. |
| No rerolls | Zero native generation/edit calls and zero pixel transformations; 320 original files preserved, including every unsuccessful historical color attempt. |
| Misleading success | SUNROOM retains small-subtitle review failure; warmer GROVE explicitly retains opaque checkerboard failure and has no ZIP; 밤결, FIELD NOTE and white 밤결 remain indeterminate with no approved package. Original GROVE distinguishes green-anchor pass from strict two-color certification. Current brand is opaque; historical transparency links retain their old-identity label. No broad license claim or phantom ZIP. |
| Repeated steering / originals | Final D1 requirements were re-read during verification; all checks addressed the same sample IDs and seven projects. Successive hash checks and HTTP reload left original assets intact. No claim of a new runtime steering mechanism applies to static Markdown. |

No production source test was created or run for these Markdown changes. LSP/typecheck/build are not applicable to authored Markdown; local paths, anchors, actual downloads, UTF-8, whitespace and HTTP bytes are the matching checks. The temporary Ruby checker initially used an unavailable `filter_map` on system Ruby 2.6, was changed to `map` plus `compact`, and then passed; this was a temporary verification-script compatibility correction, not a product failure. An unnecessary temporary-script memo comment was removed after hook feedback before public pages were generated.

## Download inventory

SHA-256 and byte counts below are the actual final local files; original download integrity was checked before edits and again after authoring. Each ZIP also passed complete archive CRC testing.

| Download | Bytes | Dimensions / archive | SHA-256 |
|---|---|---|---|
| `assets/logo-land-studio.png` | 835901 | 1774 × 887 | `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3` |
| `docs/brand/2026-identity/delivery/brand-guide.md` | 9428 | UTF-8 guide | `c6a2a2c5d8f7f8b635598f6fc7d8bd856927a192a22591c3911ccd365475445b` |
| `docs/brand/2026-identity/delivery/logo-package.zip` | 832310 | CRC PASS; PNG/guide exact | `080e4f9592b31a1819b28ec050b96ec95666a32b7bb65760e67cf2992d14bd94` |
| `docs/colors/assets/01-sunroom.png` | 915115 | 1774 × 887 | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/assets/02-northline.png` | 882512 | 1254 × 1254 | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/assets/03-grove.png` | 653299 | 1942 × 809 | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/assets/04-grove-warm.png` | 1589312 | 1946 × 808 | `db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7` |
| `docs/colors/assets/05-bamgyeol.png` | 334046 | 1254 × 1254 | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/assets/06-tide.png` | 891144 | 1774 × 887 | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/assets/07-fieldnote.png` | 999504 | 1536 × 1024 | `049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870` |
| `docs/colors/assets/08-bamgyeol-white.png` | 373191 | 1254 × 1254 | `0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd` |
| `docs/colors/deliveries/grove/brand-guide.md` | 8025 | UTF-8 guide | `8346e72d6e0394fe08b7d299a61d57332d2a468f25624d9a5c4e5af7a797d5c5` |
| `docs/colors/deliveries/grove/logo-package.zip` | 644827 | CRC PASS; PNG/guide exact | `61fed8500b5b562fa28e34a65d79bfd585c59132adc298a7af5a0e8413784d12` |
| `docs/colors/deliveries/northline/brand-guide.md` | 8010 | UTF-8 guide | `cf0f466fc251c941e3002d91036b7a300677b9db16a130f34356af254c0f649b` |
| `docs/colors/deliveries/northline/logo-package.zip` | 877838 | CRC PASS; PNG/guide exact | `aae2b39736136b671db4114d88e65f10c44997151fae37a197c390e62c41a472` |
| `docs/colors/deliveries/tide/brand-guide.md` | 9043 | UTF-8 guide | `7f80155f0ec68e027ead683d15f273497b8e0c74e46ab0e7930fcc2c482301ea` |
| `docs/colors/deliveries/tide/logo-package.zip` | 887270 | CRC PASS; PNG/guide exact | `b76d0cda7f231e10948cf48a261827d2622bb1b52253e4cd032a34b75ed23a61` |
| `docs/samples/items/01-luma/delivery/brand-guide.md` | 2890 | UTF-8 guide | `0c17b2af701728d8181156538df5520f0d773368fd83f8457a2774c24af0fc11` |
| `docs/samples/items/01-luma/delivery/logo-package.zip` | 819738 | CRC PASS; PNG/guide exact | `737551e69c8a5da9682b2114f3019e4f61f7f78def0e58d00ff83398d5a94b71` |
| `docs/samples/items/01-luma/delivery/logo.png` | 828471 | 1254 × 1254 | `29c891de028f14cc8b8a715f105b2dd8b383fa647f691521bd0de25428f561ef` |
| `docs/samples/items/02-loop-lab/delivery/brand-guide.md` | 2795 | UTF-8 guide | `a3ce1670f7461ada41a2c25af5c01e2b1100cf897625b900b88788dd07aa71a9` |
| `docs/samples/items/02-loop-lab/delivery/logo-package.zip` | 884552 | CRC PASS; PNG/guide exact | `d5018f24dbe40ba47b3ad91c71d7336090bc5168dcba715ab6e5f1c7fdf808bc` |
| `docs/samples/items/02-loop-lab/delivery/logo.png` | 893181 | 1254 × 1254 | `c03e72b2362ed7071f52f441520a73fa9a92be697efa551ae14b3cb43da8aab4` |
| `docs/samples/items/03-goyo/delivery/brand-guide.md` | 2942 | UTF-8 guide | `c5c7d11ef37522399d997fc71c768c971a8db7998e78d7d909ba01f3b88de2ce` |
| `docs/samples/items/03-goyo/delivery/logo-package.zip` | 889585 | CRC PASS; PNG/guide exact | `328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7` |
| `docs/samples/items/03-goyo/delivery/logo.png` | 898170 | 1254 × 1254 | `4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174` |
| `docs/samples/items/04-bread-bloom/delivery/brand-guide.md` | 2907 | UTF-8 guide | `45a299a04c17e4d970a60d6f5738cd7bd7a56b9dd9c77266d651d8d7b42124db` |
| `docs/samples/items/04-bread-bloom/delivery/logo-package.zip` | 1048579 | CRC PASS; PNG/guide exact | `45e1804099316f69e00f95908c7846b890db714661fd20ceb2ad4c9889d7e44d` |
| `docs/samples/items/04-bread-bloom/delivery/logo.png` | 1057106 | 1254 × 1254 | `420ac19545143efbc4681b27b68fd074656da803869c746bd9c1eeb5678c9b8c` |
| `docs/samples/items/05-kite/delivery/brand-guide.md` | 2955 | UTF-8 guide | `0fc4110c24574ce8a99ec60da291ed3fb03c68e648ce461e8c4245ff3ac67d06` |
| `docs/samples/items/05-kite/delivery/logo-package.zip` | 651225 | CRC PASS; PNG/guide exact | `146b54b76b88e127ae4613dbb03722e579845bc2b00577913433ce2e9bb75a1c` |
| `docs/samples/items/05-kite/delivery/logo.png` | 659904 | 1254 × 1254 | `dffb886a7a72196a42df21e36afe23cfb6e07bd25bad35c69c44f4de5c0232a7` |
| `docs/samples/items/06-miso/delivery/brand-guide.md` | 2905 | UTF-8 guide | `5bb3028039e259502187bc2dec43dd156aaee675bdc2b83ef034cd968011c640` |
| `docs/samples/items/06-miso/delivery/logo-package.zip` | 1016808 | CRC PASS; PNG/guide exact | `e263545af230e5db2da6e79017f3058b4336a5b7693c600bf749c18f6176eeba` |
| `docs/samples/items/06-miso/delivery/logo.png` | 1026254 | 1254 × 1254 | `10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649` |
| `docs/samples/items/07-northline/delivery/brand-guide.md` | 2942 | UTF-8 guide | `8b22fa7003e480d1205f474f479b6b1acf14dc2902d5886aa6cd46e45d74c59a` |
| `docs/samples/items/07-northline/delivery/logo-package.zip` | 787731 | CRC PASS; PNG/guide exact | `1d2a5555cb0922268acf8a99b6b060a9678d5ad64b93e84d4a4532c0b0dc620a` |
| `docs/samples/items/07-northline/delivery/logo.png` | 797205 | 1254 × 1254 | `4eb27ce806aab3a32f58337c8b1fd00f6257f1abe970f98f12edfac6be423c06` |
| `docs/samples/items/08-mulgyeol/delivery/brand-guide.md` | 2969 | UTF-8 guide | `ed352474099206976d522c9912b5b5808a1edc7f5694cfd976668a681f70d2b3` |
| `docs/samples/items/08-mulgyeol/delivery/logo-package.zip` | 860202 | CRC PASS; PNG/guide exact | `da783385149d57ef84d3678b51d7f975bba4fa2f8e4370fb7021d79b9250485d` |
| `docs/samples/items/08-mulgyeol/delivery/logo.png` | 869641 | 1254 × 1254 | `da97616502733dcef4b6b082d7746149793a22a576f3ad179a4da641d7ed66cf` |
| `docs/samples/items/09-fern/delivery/brand-guide.md` | 2970 | UTF-8 guide | `96684e2feb162efbc861c5ecaedd06a18ebdeade3aa5b996e36db3a031f7ee5a` |
| `docs/samples/items/09-fern/delivery/logo-package.zip` | 977074 | CRC PASS; PNG/guide exact | `22251e63f3cab0143931e9c5c63641c61b1ddb6f65b9dd44bfdd8970f61b21b3` |
| `docs/samples/items/09-fern/delivery/logo.png` | 985597 | 1254 × 1254 | `db9066ee56c2789324aa7c53e5ba68b9e6c003ba3fe98578ea8b0e6196181e27` |
| `docs/samples/items/10-nova-notes/delivery/brand-guide.md` | 2934 | UTF-8 guide | `55e0a9308d077919151784f08c6859ec0cfdedb230e6d2ea5bd94f8168c1eba5` |
| `docs/samples/items/10-nova-notes/delivery/logo-package.zip` | 950584 | CRC PASS; PNG/guide exact | `39c1363deb0a2bcb6070e6b07ab1309824a5eb958f81981dda9fe7f088e6bfe7` |
| `docs/samples/items/10-nova-notes/delivery/logo.png` | 959993 | 1254 × 1254 | `0e26b2354a22faba2128d205c377abe09e590c82f895e2716fe51e0877715553` |

## Protected original hash ledger

Baseline captured 2026-09-12 18:08:43 UTC; rechecked 2026-09-12 18:15:04 UTC. All 320 entries retain these exact bytes/hashes. This includes old HTML/JS/CSS, saved prompts, session/manifest/report records, original PNG/ZIP files, historical parody identity/transparency paths and all original eleven app-icon assets.

<details>
<summary>All protected originals: baseline SHA-256 equals final SHA-256</summary>

| Path | Bytes | Unchanged SHA-256 |
|---|---|---|
| `assets/logo-land-studio.png` | 835901 | `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3` |
| `assets/logo-transparent.png` | 696379 | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |
| `assets/logo.png` | 973470 | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| `docs/app-icons/images/abstract.png` | 961065 | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| `docs/app-icons/images/ip-a1.png` | 1060303 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| `docs/app-icons/images/ip-a2.png` | 1049136 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| `docs/app-icons/images/ip-b1.png` | 1083251 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| `docs/app-icons/images/ip-b2.png` | 1039677 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| `docs/app-icons/images/ip-c1.png` | 1096895 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| `docs/app-icons/images/ip-c2.png` | 1089169 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| `docs/app-icons/images/monogram.png` | 832716 | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| `docs/app-icons/images/pictogram.png` | 928736 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| `docs/app-icons/images/pixel-art.png` | 946180 | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| `docs/app-icons/images/soft-3d.png` | 1526612 | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| `docs/app-icons/index.html` | 21510 | `e87c1e9d3a78b6404d5560d8e778e8ef812618e7f13d1e7ed7a1d3b18e74a1bd` |
| `docs/app-icons/manifest.json` | 6655 | `fe6b2183a34beadf3932f00a63999ba17015792f15f87511b14a0ed9d9801dc9` |
| `docs/app-icons/prompts/abstract.txt` | 1097 | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| `docs/app-icons/prompts/ip-a1.txt` | 1377 | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| `docs/app-icons/prompts/ip-a2.txt` | 1393 | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| `docs/app-icons/prompts/ip-b1.txt` | 1391 | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| `docs/app-icons/prompts/ip-b2.txt` | 1394 | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| `docs/app-icons/prompts/ip-c1.txt` | 1388 | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| `docs/app-icons/prompts/ip-c2.txt` | 1403 | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| `docs/app-icons/prompts/monogram.txt` | 1060 | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| `docs/app-icons/prompts/pictogram.txt` | 1056 | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| `docs/app-icons/prompts/pixel-art.txt` | 1110 | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| `docs/app-icons/prompts/soft-3d.txt` | 1091 | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
| `docs/brand/2026-identity/adversarial.json` | 3660 | `2818de7f1829400a81ccf32a8cd592d5555784be589ac46b3322a95351ca0e54` |
| `docs/brand/2026-identity/baseline.json` | 55532 | `253c3091b9938d96edc2d82cf6f036f61f5fe069a3e6b97715d86d8a8e7952ff` |
| `docs/brand/2026-identity/brief.json` | 1526 | `872d428a6c6b9d748c055c98d725b442bda51ae6602bc163ddb8e6a6de0c11ac` |
| `docs/brand/2026-identity/cleanup.json` | 487 | `ffbe1af387549e7ca27ff8cb89d6f2b10c64e887b5145f425091517c601150ae` |
| `docs/brand/2026-identity/color-report.json` | 4428 | `1a12e119e384ead68ed5ddac5038fd0ae6c3cd68c5c283da1deba1199dff0eca` |
| `docs/brand/2026-identity/commands.json` | 147153 | `08e372d703396e72597fbce9b4192668059f106a516b8e778c3652c7fdfa0cdf` |
| `docs/brand/2026-identity/delivery-checks.json` | 596 | `bfb870d989fc55e59ca5b5c5796fb1c24f1585f7430a5d9463172a55945b282f` |
| `docs/brand/2026-identity/delivery/brand-guide.md` | 9428 | `c6a2a2c5d8f7f8b635598f6fc7d8bd856927a192a22591c3911ccd365475445b` |
| `docs/brand/2026-identity/delivery/logo-package.zip` | 832310 | `080e4f9592b31a1819b28ec050b96ec95666a32b7bb65760e67cf2992d14bd94` |
| `docs/brand/2026-identity/delivery/logo.png` | 835901 | `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3` |
| `docs/brand/2026-identity/delivery/manifest.json` | 15480 | `1d309c2b538f3c3d021a4d899b888d3c4f9a71f03694d4ae0e7a92b07e902c54` |
| `docs/brand/2026-identity/helper-provenance.json` | 7832 | `e000a6c861bd3f294548ce8692b443ce86e5187e5e5354a1fa5fe5b0d7965774` |
| `docs/brand/2026-identity/http-fixed.json` | 795 | `500328e07e381d2ba8d783bfbd899a2247010bbd8bc335fa3cfe357d4f9529c9` |
| `docs/brand/2026-identity/icon-preservation.json` | 2593 | `39c0d10c06f47abf12918fb3df354ef54ab759f534dfffb495ae5e0f74b37320` |
| `docs/brand/2026-identity/legacy-readme.original.txt` | 1606 | `ba7cb085770037fc8a3e5af65f3ba5f0717a8430b972eaf547f160a082ce70d6` |
| `docs/brand/2026-identity/lockup.json` | 294 | `d525c3fa94f0e85e7799a45fe781684411a2d08ba899d8c2a31a36ca66683b25` |
| `docs/brand/2026-identity/native-receipt.json` | 2155 | `6d506fe3375188309945c730bdeecb00652da61825d98e1a485d3038f74d4629` |
| `docs/brand/2026-identity/palette.json` | 828 | `c754a7e38b317a6a9d033b8667360fb331578eb199131a93b3d091cb48d1e305` |
| `docs/brand/2026-identity/preview.html` | 4507 | `bf1da531206931ffa45241bc3562b631bd305de2a20c48145dab84b783b475b7` |
| `docs/brand/2026-identity/prompt-response.json` | 4552 | `7b8d0f820619ab6f01f2c18a6cfb8f7c9cd54fa1fe74d299b148e4b4b3b53ef0` |
| `docs/brand/2026-identity/prompt.txt` | 3826 | `b9ddaf051eb98c1d65e43a4f2e71a315991266826135b66084edc7e4f1403da7` |
| `docs/brand/2026-identity/quality-checks.json` | 1001 | `c3e1a4ea206d675051907b0a5bec00edcfa8c55191a100c2714ba2de474c0d85` |
| `docs/brand/2026-identity/review.json` | 1031 | `7460811317708fee7cf3fee9aade1ee7898e8ee5822f148061f1d450ecfb74fe` |
| `docs/brand/2026-identity/session.json` | 19820 | `9a9b54bb49e743969c6988accc02ecb0558d4fb325ce10b12d8641c7db390e28` |
| `docs/brand/2026-identity/verification.json` | 1160 | `82cd4d9151475bdaffb6b6f116ca994782d436d630b26c74345907b7cfddf43f` |
| `docs/brand/brief.json` | 877 | `aa0b625ab6c11286586df92513301e1e20380508bc28d6ddc62e8e9453c2a5b6` |
| `docs/brand/delivery/brand-guide.md` | 4312 | `185b72f4752d572a793da2487d4911e2f1d3e1513bbc1493e3831be2ebc3ec65` |
| `docs/brand/delivery/logo-package.zip` | 965327 | `16ccea597e80fbfcaacfab0dfd79126d279a4996fb15c7ee682a5030492afab2` |
| `docs/brand/delivery/logo.png` | 973470 | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| `docs/brand/delivery/manifest.json` | 5751 | `7c0bd506f81ad8ca18b97d5f3ef6742da8f32faaa5ff61fd618948194a49bf9d` |
| `docs/brand/export.json` | 5924 | `7c776629054db26c33456e8e61b1140b9a9d7e37116948935cca4685fcad309b` |
| `docs/brand/generation.json` | 433 | `4d3425f8b10e971441e15d9cc8147f363a19a34ecab1597425a7e7629a904cce` |
| `docs/brand/import.json` | 4943 | `84788dcb9b0912c571654eabbcf8ee866eb16fc0383f627223dc588e43c75c0f` |
| `docs/brand/init.json` | 1312 | `af4d032602589095937de6d58448d10b97f470077770fc7e37e28ef5897ddf96` |
| `docs/brand/legacy.md` | 1978 | `8e7f3fa70a6b84e69e2822ff8a4fff8c7354ab0d813f7f7fc4a12f9bad5f488b` |
| `docs/brand/prompt-response.json` | 2206 | `4717bf5a1247d08835f273f60fe644854379e9671e8412de5b826f22edd770cb` |
| `docs/brand/prompt.txt` | 3068 | `aade1fdadd545f9d551382156db17ff43010a6fa10ce293e105cdf5ce5857c21` |
| `docs/brand/review-response.json` | 5793 | `883d1712b59e963701e2cbe17f3104ffc9609e9ebe150880dd9b3a088f1cb69f` |
| `docs/brand/review.json` | 780 | `4a2b2cbc5731c8f255703b4efae17401bf569c3a0207477a14f7bdcb7b401a30` |
| `docs/brand/select.json` | 4945 | `1235aa5090ca8f0c54ab10210122a5c82b5d656695d812daeb26c41d9d791e1e` |
| `docs/colors/assets/01-sunroom.png` | 915115 | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/assets/02-northline.png` | 882512 | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/assets/03-grove.png` | 653299 | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/assets/04-grove-warm.png` | 1589312 | `db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7` |
| `docs/colors/assets/05-bamgyeol.png` | 334046 | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/assets/06-tide.png` | 891144 | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/assets/07-fieldnote.png` | 999504 | `049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870` |
| `docs/colors/assets/08-bamgyeol-white.png` | 373191 | `0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd` |
| `docs/colors/deliveries/grove/brand-guide.md` | 8025 | `8346e72d6e0394fe08b7d299a61d57332d2a468f25624d9a5c4e5af7a797d5c5` |
| `docs/colors/deliveries/grove/logo-package.zip` | 644827 | `61fed8500b5b562fa28e34a65d79bfd585c59132adc298a7af5a0e8413784d12` |
| `docs/colors/deliveries/grove/logo.png` | 653299 | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/deliveries/grove/manifest.json` | 13070 | `7b9e94c1ccc29ab27a4499f1ffbdcefe33f1181892b08ca228eab8477a26628c` |
| `docs/colors/deliveries/northline/brand-guide.md` | 8010 | `cf0f466fc251c941e3002d91036b7a300677b9db16a130f34356af254c0f649b` |
| `docs/colors/deliveries/northline/logo-package.zip` | 877838 | `aae2b39736136b671db4114d88e65f10c44997151fae37a197c390e62c41a472` |
| `docs/colors/deliveries/northline/logo.png` | 882512 | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/deliveries/northline/manifest.json` | 12789 | `3ab7713a789411dcb78b67f6b3b76fa2df7ffe870dec3d9917b0dc7076b06695` |
| `docs/colors/deliveries/tide/brand-guide.md` | 9043 | `7f80155f0ec68e027ead683d15f273497b8e0c74e46ab0e7930fcc2c482301ea` |
| `docs/colors/deliveries/tide/logo-package.zip` | 887270 | `b76d0cda7f231e10948cf48a261827d2622bb1b52253e4cd032a34b75ed23a61` |
| `docs/colors/deliveries/tide/logo.png` | 891144 | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/deliveries/tide/manifest.json` | 14756 | `7465b62610871bd41b065c2bd8150ddecfe143b07ec9d16fcf5bc9ab2d0693bb` |
| `docs/colors/index.html` | 38564 | `5a0118f37c31c6d30837f2e68bcb931d82f24873a8a547709f4edb6e7f3749f8` |
| `docs/colors/manifest.json` | 99088 | `e13b772bd2fa4b810777bab3cec7ba145d4d227f1b47843b1d3ae7bce6d6dfea` |
| `docs/colors/projects/bamgyeol/images/a-v1.png` | 334046 | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/projects/bamgyeol/images/a-v2.png` | 1958592 | `27e010082310501ac2ca6060aa8835ff3e75cd727bb971fb76f08b153884815b` |
| `docs/colors/projects/bamgyeol/images/a-v3.png` | 1854918 | `0df1d666d480aae721f6ccab6fa7ff9d2388b015946e8e051381c86e9766c6f3` |
| `docs/colors/projects/bamgyeol/index.html` | 17699 | `314fe40653b2b7dfce0c43a0029fda6611a324bbfa9ca38d6ae4294484c63d6f` |
| `docs/colors/projects/bamgyeol/prompts/a-v1.txt` | 3062 | `3950599ae9b733fe0111291a1a0de6cf4d95f1b30a83dff75407673172d570c9` |
| `docs/colors/projects/bamgyeol/prompts/a-v2.txt` | 3600 | `d27ffe104061d0322cbeb644c8609af05c9dc6c211eed2c4082fc99efe10f5f8` |
| `docs/colors/projects/bamgyeol/prompts/a-v3.txt` | 465 | `fc168fe3993b19ca0ad02f9d51ef74d646fcde1bd0472636d8b5be313cec1363` |
| `docs/colors/projects/bamgyeol/reports.html` | 16634 | `145ec5b6add0ca7f5b6fdd0ba7dfcaf77fe2f31761c7a50929af3ca228139a58` |
| `docs/colors/projects/bamgyeol/reports/report-0da294e689214a569d637c32a14c1026.json` | 4356 | `cbf2a0160af65977d1d2c6349527ab02834b4397922e75b0288b0b5c9ee7d15a` |
| `docs/colors/projects/bamgyeol/reports/report-81d1d2403f124e45b5894589ce129d7a.json` | 4176 | `59d3e2cb7dcd1ecc1c0fed63b393e895b233d05245d1827bea581c208b65495d` |
| `docs/colors/projects/bamgyeol/reports/report-82dcdf50196a4d55ac78ff0b522326d0.json` | 4175 | `476a4ccaa84f364753c98bb190034f23b0024a9896c72e3c5bf75be0fc290c19` |
| `docs/colors/projects/bamgyeol/session.json` | 39080 | `74c6ae2611906caac2f5b1b90b71978450bebc529abae693f54e56158754e204` |
| `docs/colors/projects/fieldnote/images/a-v1.png` | 999504 | `049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870` |
| `docs/colors/projects/fieldnote/images/a-v2.png` | 2222167 | `7dacc55d6f90f10f7206729f3f0d7cffc75b36ff6191e7430d8e01e2b76c40cb` |
| `docs/colors/projects/fieldnote/images/a-v3.png` | 1993871 | `05398268ac42aa8d0da04976a9c6367df1bb186e1b3fe46e927db3e494ee65e2` |
| `docs/colors/projects/fieldnote/index.html` | 18430 | `5df45b7a017f114261ab893711adc479989e40e956290dd62d087d5f5686255a` |
| `docs/colors/projects/fieldnote/prompts/a-v1.txt` | 4009 | `0476d6b1666e0a408299f508e7a26965fb85308637e79fd83cae9b2416e3ef85` |
| `docs/colors/projects/fieldnote/prompts/a-v2.txt` | 590 | `42b5af799eac55dfae849e71c1b2f25679699892003a9036b6fadeeeb1c8529e` |
| `docs/colors/projects/fieldnote/prompts/a-v3.txt` | 405 | `cdd10ac6b9ec0cf5f5d4c7ccca28583b1f5c16e31af55a90f66dc95e4c06c0cd` |
| `docs/colors/projects/fieldnote/references/grove-colors.png` | 653299 | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/projects/fieldnote/reports.html` | 17355 | `a85ad18990324a98b26a9b2d46e2748737a832483338d35383d1fab192205d39` |
| `docs/colors/projects/fieldnote/reports/report-5aaf0c21d2244f3f8aa3e402f916ed39.json` | 4474 | `a00694207891b48291e23f821bd54029932538a22c0f7c4018042a6cfa963f55` |
| `docs/colors/projects/fieldnote/reports/report-ae8056de0d3e44b0a222bdb23fbcc579.json` | 4198 | `668fe2e8535312162951e3ed5640b6d55081fbf5a0eb81e90387bf2a6be7edb1` |
| `docs/colors/projects/fieldnote/reports/report-bfb5fbc88c274283876c782e82632a4b.json` | 4194 | `e9e6caaf863980c3daa08f0f429191d70ac47bc0de601f5362c5f9d89954e1f3` |
| `docs/colors/projects/fieldnote/session.json` | 40821 | `5c6b0002c63b1919f23eafe2a0d284f6855336778a076e2eb152e50a8f776eaf` |
| `docs/colors/projects/grove/images/a-v1.png` | 653299 | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/projects/grove/images/a-v2.png` | 1993868 | `c60c605176b39f2b26f5299a2c99906dc5cc3e93e4716691e1e2b3154af33809` |
| `docs/colors/projects/grove/images/a-v3.png` | 1331289 | `e0e0ba746f10f1ab0df53b6a2bda9c6d1f27d621efef68c4142d080407d0bc74` |
| `docs/colors/projects/grove/images/a-v4.png` | 1589312 | `db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7` |
| `docs/colors/projects/grove/index.html` | 21048 | `0d060eaf03bbc641704601bb4d626087f5c77c27a6b65ac232459998ba441dbc` |
| `docs/colors/projects/grove/prompts/a-v1.txt` | 3031 | `16ce1b74bfe18c4b1564376355765be80329fc733fefeaa39d3337be2004c722` |
| `docs/colors/projects/grove/prompts/a-v2.txt` | 3433 | `1b3f53e4ccd609f1eee40d3ee9a5485b8b90bac8c6516ec5ceac4e81b35b4564` |
| `docs/colors/projects/grove/prompts/a-v3.txt` | 513 | `b8e33e4d395ff32c015a05392f3d733f6a7b07bf520949b988fce05d7126476d` |
| `docs/colors/projects/grove/prompts/a-v4.txt` | 469 | `4df5087d869710d451b4662764fcbd3f73db92131d861ccc215df40c3a30ef96` |
| `docs/colors/projects/grove/reports.html` | 19094 | `881f9ebeac0ff24f0c734302cfe63c48dd5e4be31e740cc91341a02a5b8421af` |
| `docs/colors/projects/grove/reports/export-a8e90d0c7eb74bcfb8bbd6fcbd570a4b.json` | 4411 | `ebb0918c86070fc5d0d2ca3bd0c436e44a7cc8dfb7b9efe50390e82567620f57` |
| `docs/colors/projects/grove/reports/report-83b2e7e69e1d441595feae69b9b970ad.json` | 4411 | `43ec6582ef5e10e8a5c68065bc36816a5927530fca599f4cfd1ad25623a56cd2` |
| `docs/colors/projects/grove/reports/report-8ad54d5b46074ef999c7083e550f6b12.json` | 4106 | `7855bed8c3145b7d2b05829b4b9e43967a28323cad3e9d526fcdc31c8137edbd` |
| `docs/colors/projects/grove/reports/report-9b0d511b5f634a83979e706ceb3330d1.json` | 4100 | `2fb9ca6fbb57648971fe0b68d68264f48fb0847e5713301dea9ab1a9e7e22815` |
| `docs/colors/projects/grove/reports/report-d0483f48d4d24defa8b77f2acf4a46f9.json` | 4103 | `8d4030cd86d6ccb1556b8042cb4f4822b0f1b2e41e98e2538239d809e17bb181` |
| `docs/colors/projects/grove/session.json` | 57661 | `21f14affaaeaa5fe671f5bfb1b8030374e2ff7b03892fbc7f2c77b45a9f12107` |
| `docs/colors/projects/northline/images/a-v1.png` | 882512 | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/projects/northline/index.html` | 10828 | `6f3f30f48540e1e852a1916cb97d9f85180f4325d1861f512f567d966ab6bf21` |
| `docs/colors/projects/northline/prompts/a-v1.txt` | 2920 | `73c985fe0e290bf98cd758676a570283d0bf5695c99827d1a28f757c4ce00119` |
| `docs/colors/projects/northline/reports.html` | 12304 | `2f37c3bc29338e172023ac70f2e49e5fc06a1c2c656754f1750d26f09579366e` |
| `docs/colors/projects/northline/reports/export-ebcbc02f93344a18ba4568016d68980e.json` | 4117 | `487d044505a949578bab79ecc8500951ff44ecd7ba1962e694fa374df6f50f16` |
| `docs/colors/projects/northline/reports/report-a45574ad29184f6bab909f5fb77336fe.json` | 4117 | `132bc58664a084311017bda331f7971febab378f9c535aa8562359a712004d87` |
| `docs/colors/projects/northline/session.json` | 19911 | `f9d6a877729fe009ae0d8d61636b9de7f9ff1ef3c68371b356999e6ed99edcc4` |
| `docs/colors/projects/sunroom/images/a-v1.png` | 915115 | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/projects/sunroom/index.html` | 11009 | `5ffcb381fd8765188069138a121c6a98115d8225f6d11d786f596136f05a1fb4` |
| `docs/colors/projects/sunroom/prompts/a-v1.txt` | 2781 | `a2b435a2be56f59df8f60305a44e6e1068cedef8346305d3499523ad7253dd60` |
| `docs/colors/projects/sunroom/reports.html` | 12447 | `b3a0887359cc6916940dff000eacfee9633870dd129183478c3d2dc571cb99ff` |
| `docs/colors/projects/sunroom/reports/report-4f44a0b5c1b044659f014370325adac7.json` | 4299 | `6e1a9c52bf505d645eac36559dda73909b4921ab70471cfdd832b25f4a22e314` |
| `docs/colors/projects/sunroom/session.json` | 15486 | `c701d822d727dffa0c1fcc4fb6d49b1b3195fecceb699d85c8755ff33623a104` |
| `docs/colors/projects/tide/images/a-v1.png` | 891144 | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/projects/tide/index.html` | 10989 | `bc1e9efbcd6e9673775871d438eef41843f5f34b837956968cff22f185c0ee4f` |
| `docs/colors/projects/tide/prompts/a-v1.txt` | 3823 | `0228783b3948e6db29bf7f443a7e41998b86df46f801489635433eb7781b520f` |
| `docs/colors/projects/tide/references/sunroom-colors.png` | 915115 | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/projects/tide/reports.html` | 12604 | `4f450b77c1b294aa7724cb70513818c0e123e4bfd5f445e2d7a0fee5c3227ac0` |
| `docs/colors/projects/tide/reports/export-a93930d610d74e948324475c62b57ae1.json` | 4117 | `e0a35d9eab54e30fcbfdd33d279787dd09036488a8ed2e9a9114f5dfe62e654b` |
| `docs/colors/projects/tide/reports/report-fd7670cbe1c547a593d960a3c93715e6.json` | 4117 | `130e87eb165acd22f075dad0b9cfd1400c0d7625b209d7fd6a628b60a9982692` |
| `docs/colors/projects/tide/session.json` | 21135 | `4c03b9c94d5de5722d80d7ae5388bf1371ac45a09f4e11f0535d32fb12ffba94` |
| `docs/colors/projects/white-bamgyeol/images/parent-v1.png` | 334046 | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/projects/white-bamgyeol/images/white-v1.png` | 327144 | `764557003be078c7e83fca85b7b40d43977edefa9ef46caf49f5279c403a3151` |
| `docs/colors/projects/white-bamgyeol/images/white-v2.png` | 375026 | `fda77d0af6c53c4d0d28099ca6568cbb7e877ac6045ea9ca6898bf77884a29a5` |
| `docs/colors/projects/white-bamgyeol/images/white-v3.png` | 373191 | `0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd` |
| `docs/colors/projects/white-bamgyeol/index.html` | 20692 | `f2a941d9fc8556e5b07663f4068dc1ba316e1c2678afba81acef04f4ffa4086a` |
| `docs/colors/projects/white-bamgyeol/prompts/parent-v1.txt` | 3062 | `3950599ae9b733fe0111291a1a0de6cf4d95f1b30a83dff75407673172d570c9` |
| `docs/colors/projects/white-bamgyeol/prompts/white-v1.txt` | 476 | `52b4c11e7166abbe10380c59db4e44f85ec450c25c10a93c465cbaed396dfb94` |
| `docs/colors/projects/white-bamgyeol/prompts/white-v2.txt` | 345 | `4d3a947680ba451faafc3a59def385e56e6e7f1eaf30ab961882ce6d46009f3b` |
| `docs/colors/projects/white-bamgyeol/prompts/white-v3.txt` | 343 | `ef590fa42488fa88e7f093970338a7acebefab44ee09b9e9afe1c3dd25b0fc3f` |
| `docs/colors/projects/white-bamgyeol/reports.html` | 18881 | `7aa545491cc60911510c207b0ba56b460c6071937fbe2e1f4bb66f42f05a0485` |
| `docs/colors/projects/white-bamgyeol/reports/report-588011cab723462bacb99a957b4dc678.json` | 4218 | `1bacd7f1aa60f6380074f5b2072f953ec222f905b7edb14c2363ba7ae1539d1d` |
| `docs/colors/projects/white-bamgyeol/reports/report-6c1d44e25b714060af0d602866ac2d4c.json` | 4361 | `3e39d7c0936295a06bf05ceab2ca8da6dd4aa53205a75f1d32c80c6f6d05ba36` |
| `docs/colors/projects/white-bamgyeol/reports/report-9bc44eedf2dc4aebbc1e6e4396098860.json` | 4221 | `069a7a799eb860e2d80e410254df422b0b9981da5c59f2253d8cf5c96dd7cf57` |
| `docs/colors/projects/white-bamgyeol/reports/report-fd183d105dd74c1db560ea63ffffb1bb.json` | 4158 | `332e859ef21d174776149a089ed8b73f0c36da719f3e1a75907e2daab9e52b09` |
| `docs/colors/projects/white-bamgyeol/session.json` | 52458 | `7accd7c91aa6f56fa48862adc99982b2801c40a1e26b298a668e1453da62cee6` |
| `docs/colors/verification.json` | 8323 | `a0edc2ce3fc0f83bdddbada15d7c4097644f25c562be1849180a1c7ea887b670` |
| `docs/samples/catalog.json` | 37514 | `6cd286ea659c998a1563b6f4a0b56b078234dfe946054c9ccea3252b2df5f55d` |
| `docs/samples/data.js` | 37537 | `6312b89775426b4039baac26ed6b3454532a5c38f3375c920e943a1dab30fe76` |
| `docs/samples/gallery.css` | 17000 | `8a05900f4295d6fa1602a5edf690373150555d9b118935c9a363426b604288aa` |
| `docs/samples/gallery.js` | 9273 | `812e7a2f78b6d786b0b9af66e32a3185e057a6d291361f37e80a0424f044ab24` |
| `docs/samples/generation.json` | 4487 | `4868f3fc5839bf28a3f19df4328eeb1b2dab89914ea0aee166dbf2c07dee3a74` |
| `docs/samples/index.html` | 8697 | `6195d260a64c0a2c14ca6a86caf3d89ad0c41cc90c93e4718818dea73b6c2e70` |
| `docs/samples/items/01-luma/brief.json` | 842 | `bfc221cb27908da79323f28eb48191f17f4d7e76a2b8b854b3976d0f505a3136` |
| `docs/samples/items/01-luma/delivery/brand-guide.md` | 2890 | `0c17b2af701728d8181156538df5520f0d773368fd83f8457a2774c24af0fc11` |
| `docs/samples/items/01-luma/delivery/logo-package.zip` | 819738 | `737551e69c8a5da9682b2114f3019e4f61f7f78def0e58d00ff83398d5a94b71` |
| `docs/samples/items/01-luma/delivery/logo.png` | 828471 | `29c891de028f14cc8b8a715f105b2dd8b383fa647f691521bd0de25428f561ef` |
| `docs/samples/items/01-luma/delivery/manifest.json` | 4220 | `cab00ce0951e6b856c2ab1397dcf8f3b800883404684d89ae48a8e901acd2a9d` |
| `docs/samples/items/01-luma/export.json` | 4409 | `e3f3fb6361e5ab6d7e26c45903c3dd52bb9d5c056fdf76fd3f8c2b27d9ec65de` |
| `docs/samples/items/01-luma/import.json` | 3440 | `7c7cc3bf683eb2f56cad6a329ac6b01a2a064859f590ac4662b17a0bd47719a2` |
| `docs/samples/items/01-luma/init.json` | 1174 | `5b2734532cc99f0ac52bd1bf433c129607328555a131636f3f99a2b8c0560d8b` |
| `docs/samples/items/01-luma/prompt-response.json` | 1307 | `6854dd49ba6fcf546206cc4b43fa96fcd175b66126a3286f6478b012b7c8d5f3` |
| `docs/samples/items/01-luma/prompt.txt` | 1702 | `42e7a37eb050d8b9a51232b66d4f3187b4e44470abe8c35fb4366838c495ec54` |
| `docs/samples/items/01-luma/review-response.json` | 4262 | `93eeca215736ff3e9ed03693f89ad233b60f143abd7c71eeac18e2f3c9521a23` |
| `docs/samples/items/01-luma/review.json` | 752 | `2dd5ae1c3ddf1498b973f85d908bd546228d59eae0f0ff9e49ae920f41756fd9` |
| `docs/samples/items/01-luma/select.json` | 3442 | `325f8ebb6d28c3c1eeea85263f2dbf16b2358fc2d724e60da3571aacdbf98ffe` |
| `docs/samples/items/02-loop-lab/brief.json` | 820 | `a0f1f1d3ede551adff9d891b68d88f0981ff2c09a9b75fba83545a7551bcf119` |
| `docs/samples/items/02-loop-lab/delivery/brand-guide.md` | 2795 | `a3ce1670f7461ada41a2c25af5c01e2b1100cf897625b900b88788dd07aa71a9` |
| `docs/samples/items/02-loop-lab/delivery/logo-package.zip` | 884552 | `d5018f24dbe40ba47b3ad91c71d7336090bc5168dcba715ab6e5f1c7fdf808bc` |
| `docs/samples/items/02-loop-lab/delivery/logo.png` | 893181 | `c03e72b2362ed7071f52f441520a73fa9a92be697efa551ae14b3cb43da8aab4` |
| `docs/samples/items/02-loop-lab/delivery/manifest.json` | 4142 | `7c1ea612a9976316154bfeba46dda8f7bc30f55c68d47effe9f8990d6927c672` |
| `docs/samples/items/02-loop-lab/export.json` | 4335 | `7b2a2e4f43c0c1174b8ac7c80efbcca35b21a8b61f6dd18239b47180e3ffaefc` |
| `docs/samples/items/02-loop-lab/import.json` | 3364 | `90502dcb7a454b02fb07a1b6758f123e0bbdc56dfe084b534b1227b229bcde5f` |
| `docs/samples/items/02-loop-lab/init.json` | 1156 | `5e5b5f1a955e35c45a5649d344a4137f9143893d2db1fb4b20a9a0b1e5a1b593` |
| `docs/samples/items/02-loop-lab/prompt-response.json` | 1271 | `c78f3f5163e872aff79ec36835a4a80dae932b674d130520bf1ff28c77cb03c9` |
| `docs/samples/items/02-loop-lab/prompt.txt` | 1644 | `4ff03315be3301c0f8d800ad1e0184e35cd11abec36cfb17308a209ac90322cf` |
| `docs/samples/items/02-loop-lab/review-response.json` | 4184 | `48b9cbe998c53fd10708b08abc7e70799bafd117cd914bf6803d1923cf0db22e` |
| `docs/samples/items/02-loop-lab/review.json` | 750 | `e7dd98c1064334c5741d074cf2b1f0125ba087b5104b781ac83147680242738d` |
| `docs/samples/items/02-loop-lab/select.json` | 3366 | `dcde8374b255789519305ddece04eb090ded597525e7e7a742046c112041622a` |
| `docs/samples/items/03-goyo/brief.json` | 824 | `28742b89cc5ee66f4b1a5ff8ed7b5477c57989b614330caa7d4069417a7d9543` |
| `docs/samples/items/03-goyo/delivery/brand-guide.md` | 2942 | `c5c7d11ef37522399d997fc71c768c971a8db7998e78d7d909ba01f3b88de2ce` |
| `docs/samples/items/03-goyo/delivery/logo-package.zip` | 889585 | `328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7` |
| `docs/samples/items/03-goyo/delivery/logo.png` | 898170 | `4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174` |
| `docs/samples/items/03-goyo/delivery/manifest.json` | 4257 | `3a80a87104f9cd5c28aca2f892abfb7dda8a3c1fdc87c36519b4cb82fb26f8f2` |
| `docs/samples/items/03-goyo/export.json` | 4446 | `f009a669284d6b6914d28cffb7e3799fff306355d93e4b2cb3cd255c6f08ef97` |
| `docs/samples/items/03-goyo/import.json` | 3498 | `8224342203e53679501faf7e8e4a251651ad71108f75910ef423f4fbdd5f04e2` |
| `docs/samples/items/03-goyo/init.json` | 1156 | `58929251dee4718c48645c8573fc8e391304c1df34cd9b9ace6eba7329f11fbd` |
| `docs/samples/items/03-goyo/prompt-response.json` | 1336 | `4187c86f96d94c16b06ef64ee016681c0b89d8af1d27ebe3268a354e72d59990` |
| `docs/samples/items/03-goyo/prompt.txt` | 1778 | `8b8dcfc8d3c6d51d7ed18e17cc13cf9b890fabd96fbe28d853e288375a9feefe` |
| `docs/samples/items/03-goyo/review-response.json` | 4299 | `7b0d03b4b87e378f39ec8b4b420190574f7af5ea254f32ccb9b637bf717f77bd` |
| `docs/samples/items/03-goyo/review.json` | 731 | `485968ee6daa42ccd92e383f4d4efb73498e272dafc1230a66ea8bac38073aea` |
| `docs/samples/items/03-goyo/select.json` | 3500 | `f75ecb44a59e33cdea8c474aa5400e4c3fbad1cf22852e6597cde1ba124aedbf` |
| `docs/samples/items/04-bread-bloom/brief.json` | 823 | `f7e9f0bdc3820b1895cd5e1a72b9e4d5515853bf686709fbcc02124144e9699c` |
| `docs/samples/items/04-bread-bloom/delivery/brand-guide.md` | 2907 | `45a299a04c17e4d970a60d6f5738cd7bd7a56b9dd9c77266d651d8d7b42124db` |
| `docs/samples/items/04-bread-bloom/delivery/logo-package.zip` | 1048579 | `45e1804099316f69e00f95908c7846b890db714661fd20ceb2ad4c9889d7e44d` |
| `docs/samples/items/04-bread-bloom/delivery/logo.png` | 1057106 | `420ac19545143efbc4681b27b68fd074656da803869c746bd9c1eeb5678c9b8c` |
| `docs/samples/items/04-bread-bloom/delivery/manifest.json` | 4216 | `5703533eae24d50b619f3d1bbacbebd9a5fc42d4a1fdc9f9759a413efbf22228` |
| `docs/samples/items/04-bread-bloom/export.json` | 4412 | `48372dda9b64049c64002359930f7f521373dc636f20e4079a7c4ac3b93139f6` |
| `docs/samples/items/04-bread-bloom/import.json` | 3453 | `a381ab9c6215a0f7934d6f496d682eadbc718179f39f104f4f60452437c0f886` |
| `docs/samples/items/04-bread-bloom/init.json` | 1162 | `d66a1105120aa019e7179a5e62b9996b099808454ee45b16a055881c235db5d5` |
| `docs/samples/items/04-bread-bloom/prompt-response.json` | 1317 | `ebb2e8a4a2b904f3a9548fda60af1eaab04cf4bf1ec5e41f736a0d5d53c5ac40` |
| `docs/samples/items/04-bread-bloom/prompt.txt` | 1727 | `d0b751283e8e01baef338a8ed8e1617f556d3f577c7a385e4622d7c5fab025f0` |
| `docs/samples/items/04-bread-bloom/review-response.json` | 4258 | `7e01df6f958e7eb21183e9bd2e7d1a1960af85e883634aa496cf369df0c02cd7` |
| `docs/samples/items/04-bread-bloom/review.json` | 735 | `b14f58869c80b420869bd3758b6e03d0f3e8f34b5c45fb1f2c850c599e779515` |
| `docs/samples/items/04-bread-bloom/select.json` | 3455 | `2deb7608d495cfee464797bd027c1721ffcb026a3fcb8d56eed220bf9544080c` |
| `docs/samples/items/05-kite/brief.json` | 794 | `901dc890643041dfaae6e74de06c34ab67e9aa512b430a0888fe9691573c4dbf` |
| `docs/samples/items/05-kite/delivery/brand-guide.md` | 2955 | `0fc4110c24574ce8a99ec60da291ed3fb03c68e648ce461e8c4245ff3ac67d06` |
| `docs/samples/items/05-kite/delivery/logo-package.zip` | 651225 | `146b54b76b88e127ae4613dbb03722e579845bc2b00577913433ce2e9bb75a1c` |
| `docs/samples/items/05-kite/delivery/logo.png` | 659904 | `dffb886a7a72196a42df21e36afe23cfb6e07bd25bad35c69c44f4de5c0232a7` |
| `docs/samples/items/05-kite/delivery/manifest.json` | 4217 | `31569fc1c084b69a3bcc8867395af8e156a58816b9c159beaad6a9e33b452fcf` |
| `docs/samples/items/05-kite/export.json` | 4406 | `cf5acd251728f04eff7cd1b211cfcd73f4d489c058f73d6f0025f4b827b4ac83` |
| `docs/samples/items/05-kite/import.json` | 3486 | `6ce674a0cd12808ef5ef81986ecf9a26e084e400b602d6c683ccda849b75794e` |
| `docs/samples/items/05-kite/init.json` | 1126 | `8e41faf41c4aa0e7eb42e440a619d2f0a20c6d08b36ecf4cd69e99ebffa743cd` |
| `docs/samples/items/05-kite/prompt-response.json` | 1330 | `8550068f053bb70be94e51f047784d1289053154e80bbd1f6307c4b92e9679df` |
| `docs/samples/items/05-kite/prompt.txt` | 1796 | `a79432dfeb4931e2d4c95c3fb5ce2241709519571633fd794b58f6ffa724ecf7` |
| `docs/samples/items/05-kite/review-response.json` | 4259 | `e511a88e0d810f3bff87d056bcf6efab682b5c93ffbe2e85bf9bd0cd8c37ae15` |
| `docs/samples/items/05-kite/review.json` | 703 | `fa4899f794f2ffaccc38300afe5726b5456eda79024027173c1fe0389bde23df` |
| `docs/samples/items/05-kite/select.json` | 3488 | `a5c9e64b6d5ada2cf9077a0955c43b99194a39bbc172ce422c47fb3e66561a09` |
| `docs/samples/items/06-miso/brief.json` | 807 | `5bbee46b313006e949f7c51642b8b6b90b062ec561af2a1221b4c3b12a8d30e6` |
| `docs/samples/items/06-miso/delivery/brand-guide.md` | 2905 | `5bb3028039e259502187bc2dec43dd156aaee675bdc2b83ef034cd968011c640` |
| `docs/samples/items/06-miso/delivery/logo-package.zip` | 1016808 | `e263545af230e5db2da6e79017f3058b4336a5b7693c600bf749c18f6176eeba` |
| `docs/samples/items/06-miso/delivery/logo.png` | 1026254 | `10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649` |
| `docs/samples/items/06-miso/delivery/manifest.json` | 4166 | `017544e508286c64481b9d90493c669f309f0809aec02092d4d20373fc48de88` |
| `docs/samples/items/06-miso/export.json` | 4355 | `38133df4745a37a55a6df8572146b24729b9844f9b5bf2d2d6e59f2e3d8af50e` |
| `docs/samples/items/06-miso/import.json` | 3440 | `b7350c61fbbf20d69942f33f5e76aacd41535bec190b0940dd26a724ecdb31b7` |
| `docs/samples/items/06-miso/init.json` | 1139 | `4830e443d052e1faa8ab4cf39b063524c3452dbc10ae95dd6563197791c5f421` |
| `docs/samples/items/06-miso/prompt-response.json` | 1307 | `070b64e1a91ab561d05a8e8ccbeed7197df74c037cb2449476fd910e3b0709e9` |
| `docs/samples/items/06-miso/prompt.txt` | 1737 | `5ff42b47c41dab0af06411b9d1fcd5e008e571ba5423004ae4fbe16dde6e144a` |
| `docs/samples/items/06-miso/review-response.json` | 4208 | `47b657f45d2bb59d836d68a5c6a1b878dceb1db4a75d463f5310049bd48120c3` |
| `docs/samples/items/06-miso/review.json` | 698 | `d6ecc93bb4a1c708f91aa2a2bdfc78cc51c791eb2ee8cc6b981a4173ceb0b525` |
| `docs/samples/items/06-miso/select.json` | 3442 | `b853cd53d923406a3f88471dbe5c1bef4a1a98646defd5e48a7203ac7772d02d` |
| `docs/samples/items/07-northline/brief.json` | 811 | `87b0024364f1a56364219627c9d89e86bdaaf3a8c4cc0e5fe8095caa08dc72fa` |
| `docs/samples/items/07-northline/delivery/brand-guide.md` | 2942 | `8b22fa7003e480d1205f474f479b6b1acf14dc2902d5886aa6cd46e45d74c59a` |
| `docs/samples/items/07-northline/delivery/logo-package.zip` | 787731 | `1d2a5555cb0922268acf8a99b6b060a9678d5ad64b93e84d4a4532c0b0dc620a` |
| `docs/samples/items/07-northline/delivery/logo.png` | 797205 | `4eb27ce806aab3a32f58337c8b1fd00f6257f1abe970f98f12edfac6be423c06` |
| `docs/samples/items/07-northline/delivery/manifest.json` | 4200 | `9c70b3e2c9464ddab72821f76908a7bef7d9fe6e7bf3b7b186ee65f6aaf70a4d` |
| `docs/samples/items/07-northline/export.json` | 4394 | `b36decc4c94917dcf88cc4f60ba017e70cc9bd852fb5a5544f9854e30c0e545e` |
| `docs/samples/items/07-northline/import.json` | 3499 | `53b17978e2b3967bd7f6d126c58ebd19159f8516184d4b12e9e792671d8efdae` |
| `docs/samples/items/07-northline/init.json` | 1148 | `6965eae56b79adedfae70157f9c16d7a21cb0c2ea3091bae4e2bc72d2283d2ab` |
| `docs/samples/items/07-northline/prompt-response.json` | 1339 | `ddcbce4b3a783cde4d833d1d67fdabdad5110b675c1e0313f398545428ff9172` |
| `docs/samples/items/07-northline/prompt.txt` | 1787 | `c6d059d8cb95faed5246bef05fe921ac212075d5f9ffcce12e79d1596b3d8ead` |
| `docs/samples/items/07-northline/review-response.json` | 4242 | `9923a3a8e23bab405f5256521264ef016f45916a0515b2a72d5ec958c07d70a9` |
| `docs/samples/items/07-northline/review.json` | 673 | `48ebf8d8fc0a49235e93deb8682c8009585d6dfb777a4fbc246a992ecba8114f` |
| `docs/samples/items/07-northline/select.json` | 3501 | `3ed49da83a98131e8f5a77528e773399fa1833f19b69d06c595595316e2e4e95` |
| `docs/samples/items/08-mulgyeol/brief.json` | 815 | `dda2b2802c795e8b45986d3d85d13ec88a8e647b5a1bdb6a8207c9e23de21bd1` |
| `docs/samples/items/08-mulgyeol/delivery/brand-guide.md` | 2969 | `ed352474099206976d522c9912b5b5808a1edc7f5694cfd976668a681f70d2b3` |
| `docs/samples/items/08-mulgyeol/delivery/logo-package.zip` | 860202 | `da783385149d57ef84d3678b51d7f975bba4fa2f8e4370fb7021d79b9250485d` |
| `docs/samples/items/08-mulgyeol/delivery/logo.png` | 869641 | `da97616502733dcef4b6b082d7746149793a22a576f3ad179a4da641d7ed66cf` |
| `docs/samples/items/08-mulgyeol/delivery/manifest.json` | 4259 | `c723f500cacadfdf2bffbea6eb01847fcd308108c503497fa1eb218295762089` |
| `docs/samples/items/08-mulgyeol/export.json` | 4452 | `567c13ecf2aff41395cb60628e5c8f5a9bed0fd965579bad5cc6950af593c5c3` |
| `docs/samples/items/08-mulgyeol/import.json` | 3514 | `63d2212ea4338c9984a8ca0f7844b3da6e85bc5ea8b1702dd466a46bd4fbc33a` |
| `docs/samples/items/08-mulgyeol/init.json` | 1151 | `321246e299de00657930b6d8de659caa724f70a44b283ba73630c5f6fd20975c` |
| `docs/samples/items/08-mulgyeol/prompt-response.json` | 1346 | `b728ecd31f81302024829ef8283cb6fae85159cd0591478951248a5c4265e89c` |
| `docs/samples/items/08-mulgyeol/prompt.txt` | 1799 | `abfc5d06669b358f7d24ca2d03beaf1b37fad1bfbec3079554bf235007c00c7e` |
| `docs/samples/items/08-mulgyeol/review-response.json` | 4301 | `129539e7b0e38405cfdbebaf0424c78c9661fa7f2a82796d2178761ee7d9eebe` |
| `docs/samples/items/08-mulgyeol/review.json` | 717 | `4deb57b145c47b3392bc90611dccd21212d05bc31490bcf2653a0e9ee3e08dd4` |
| `docs/samples/items/08-mulgyeol/select.json` | 3516 | `5d29053c17f926c18d05c91229f0140057e834155b27cd4a85ebc01c498c05c5` |
| `docs/samples/items/09-fern/brief.json` | 818 | `a26c1f1f36001df6607aa7877af4babcfbc568ac90a4784388e4afd4d4de8387` |
| `docs/samples/items/09-fern/delivery/brand-guide.md` | 2970 | `96684e2feb162efbc861c5ecaedd06a18ebdeade3aa5b996e36db3a031f7ee5a` |
| `docs/samples/items/09-fern/delivery/logo-package.zip` | 977074 | `22251e63f3cab0143931e9c5c63641c61b1ddb6f65b9dd44bfdd8970f61b21b3` |
| `docs/samples/items/09-fern/delivery/logo.png` | 985597 | `db9066ee56c2789324aa7c53e5ba68b9e6c003ba3fe98578ea8b0e6196181e27` |
| `docs/samples/items/09-fern/delivery/manifest.json` | 4248 | `3bad9944a59f736691647ee2f073376fc6d1b32cfd556e7b9d55228ba7423c06` |
| `docs/samples/items/09-fern/export.json` | 4437 | `13c2608d559f48d332c16ff87c4e5bb9091c29b79d4f1bca01db31ff26702a5f` |
| `docs/samples/items/09-fern/import.json` | 3518 | `5d8f671f9a973666f4bd44f4a883ad4022e39f5990e4c8ff247e45069f0fa21b` |
| `docs/samples/items/09-fern/init.json` | 1150 | `a1156d43abfebab5ec378384758d9b863fc96c5fca4a4b20a9ac27ebe0e565e6` |
| `docs/samples/items/09-fern/prompt-response.json` | 1346 | `b900586cc2e70307d11d1b51d5e6cf892010e2e4dc69a7a19ce0ca507d857668` |
| `docs/samples/items/09-fern/prompt.txt` | 1804 | `7e6012a8106d624db3d0271cdc621bfb2630bbb2926c30ef28601c3355e8a200` |
| `docs/samples/items/09-fern/review-response.json` | 4290 | `d9f5ced3d2f0e60e43d434622071a981ec24c68f305a08908d90e01d2bb2d6e2` |
| `docs/samples/items/09-fern/review.json` | 702 | `416b0b2679e5ccdd07b66fb9b2c71cc443415bb1ce53b46bf753303e052549c7` |
| `docs/samples/items/09-fern/select.json` | 3520 | `457e10d003b56073f8a8d3637f9139e214c2bdbaf3a077d84edb87344d459ff7` |
| `docs/samples/items/10-nova-notes/brief.json` | 828 | `2b05add8c82e5cf2e2e3dc3104914a17d5f3b31dd38a880e5f7b19e635ebe258` |
| `docs/samples/items/10-nova-notes/delivery/brand-guide.md` | 2934 | `55e0a9308d077919151784f08c6859ec0cfdedb230e6d2ea5bd94f8168c1eba5` |
| `docs/samples/items/10-nova-notes/delivery/logo-package.zip` | 950584 | `39c1363deb0a2bcb6070e6b07ab1309824a5eb958f81981dda9fe7f088e6bfe7` |
| `docs/samples/items/10-nova-notes/delivery/logo.png` | 959993 | `0e26b2354a22faba2128d205c377abe09e590c82f895e2716fe51e0877715553` |
| `docs/samples/items/10-nova-notes/delivery/manifest.json` | 4299 | `7476a85865e158a2f1c76775e365f53e84268228f9cc3fcec01d1e8f40dabba2` |
| `docs/samples/items/10-nova-notes/export.json` | 4494 | `0d1085e34d31e09e3b49245880fc615ac9c1d98bb853e3e9e7bc0b486c71819b` |
| `docs/samples/items/10-nova-notes/import.json` | 3490 | `05d91d3112119a1e3a2dc0b8305b6253ac5ef57d186b8a2074ceef166aecc56d` |
| `docs/samples/items/10-nova-notes/init.json` | 1166 | `f7166d475c25ec1f38db8dbdaf9b74e4f25941b82e6b48d0a075a9616ba34596` |
| `docs/samples/items/10-nova-notes/prompt-response.json` | 1335 | `f11db98370297420d13f525db1749d27ce598742045dff585b91c7c0392ad79e` |
| `docs/samples/items/10-nova-notes/prompt.txt` | 1760 | `6d64eb9c274a8da147890b7620f29c87d41c9f5881854e642a47b9b0cb100609` |
| `docs/samples/items/10-nova-notes/review-response.json` | 4341 | `a6b2d5cfee0a41c150123fbad9631e59a8db51654ece2647f0c755488f14af7b` |
| `docs/samples/items/10-nova-notes/review.json` | 781 | `176dbf2a192d6e5d8eade34353365d7f9fb8c951bf760f8f0949cf788a505892` |
| `docs/samples/items/10-nova-notes/select.json` | 3492 | `cfecad7c34d81c01d3099926ce8334dbfce5d89f1287e209cde5e67ac6f1ef40` |
| `docs/transparency/README.md` | 4752 | `cc897e9c43499a9d1cddd64ed6fdb1b24b9fb5bc0f47c40aa12349f6f99d5e5f` |
| `docs/transparency/chrome-preview.jpeg` | 151858 | `6064f8ba83fab7c58682c2c02a5ffff40f4f2ca7ed6714218757d5b8271d9521` |
| `docs/transparency/delivery/brand-guide.md` | 3694 | `a40e81bb002467e5a4578f12cd09baa00e4d8c3b7c91262563a64cf58cf9f3f0` |
| `docs/transparency/delivery/logo-package.zip` | 684581 | `6378dbb7d5f2c6b461ecfca6732df1143142eba8b1e616dc7b34d09b36eab1cf` |
| `docs/transparency/delivery/logo.png` | 696379 | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |
| `docs/transparency/delivery/manifest.json` | 5260 | `6086c41366f5383c9bd7cce1c85db55d390a596a16faca2b4e115dc2fca2f7a5` |
| `docs/transparency/export.json` | 10042 | `9946396e46fb32744743796141d34776921c8cedf829472a0583d24cfa2b4897` |
| `docs/transparency/generation.json` | 823 | `724d3a82294a6c438919e97c7cdef6ff4a9bd45945b91ea6ec44846b439fa8a0` |
| `docs/transparency/import.json` | 8931 | `31527033fc4bab0f0e7f52486c2ce5a2d7d6b277cd4d2554c67dd429a25b0daf` |
| `docs/transparency/index.html` | 3280 | `f2f207307b2ba1c6c0998e43c21d4d507aee6fbda8838ba5c7bfd4582f4750b0` |
| `docs/transparency/prompt-response.json` | 2312 | `fea6b6ca5db2199d05e1227f7ab6c424178909de03629c977267d4d0d987b6ff` |
| `docs/transparency/prompt.txt` | 2435 | `f2c98f8fdffd799f0abf5f05b38717f72e1034d52d3f2673ac90a37cf533c302` |
| `docs/transparency/readme-en-table.jpeg` | 102640 | `17eae1e3a45f96407d103d21a3f5d9f33df33658d4c8afecc52c453714b50340` |
| `docs/transparency/readme-ko-table.jpeg` | 99615 | `f9e0b1174454be873b14668410af1dfce0314fcf7d63a6c6861df889d8c31952` |
| `docs/transparency/review-response.json` | 9906 | `1a00bc2b4f867619167c3ba5dd9d19f82d43a3cbd5202be7e2fb965e78995dab` |
| `docs/transparency/review.json` | 907 | `23f201656d4216298a3910a4bd9d8744d3255e1045673eeabd934f9b2f21958f` |
| `docs/transparency/select.json` | 8931 | `2e1997002d04bf29f8e14acf31f2373b0043e92aff6bd7ca65c9c657a1eb4959` |

</details>

<details>
<summary>Source baseline and stale-source recheck</summary>

| Path | Baseline SHA-256 | Final |
|---|---|---|
| `skills/logo-land/SKILL.md` | `e6021663acc3c056d47b0a5ccae3727f7d7a9e32affe5acee95d1f33b299a4f5` | Same |
| `skills/logo-land/agents/openai.yaml` | `26e73fa8f7fa5c8296639b69e2eab5feaf014b2ad73f54581278c2230a659a74` | Same |
| `skills/logo-land/assets/app-icon-gallery.template.html` | `960c682d45807c8a7f1a0dfb5f031f6a17f3fb6d4ca0c84501514375bd8cb9dd` | Same |
| `skills/logo-land/assets/app-icon.example.json` | `2477e1384ba781a44a0116f4a86c71a85cdea3e4030ae6c388e28c1779685fbc` | Same |
| `skills/logo-land/assets/brief.example.json` | `2841dbbba9e3d94759c1a1b5ccc2885b8a94a87e7ede81f0786d0b7d31155342` | Same |
| `skills/logo-land/assets/color-gallery.template.html` | `65c0745614f866f670a94068503552c9982ef48c1a6697f05943ac999cea6773` | Same |
| `skills/logo-land/assets/ip-as-logo.LICENSE` | `b8f39925b1c36ca531c5e663aeb7ba427f94a526495785b4d1b2797fae8f2546` | Same |
| `skills/logo-land/references/app-icons.md` | `be380997cd484b56dfcbdf2bedd0c63f7542274b7a32858eb993ec97eec82421` | Same |
| `skills/logo-land/references/color-providers.md` | `285199155af770b052e1d7aa2ec92bb687320d1f5aebe6008eadc3ca0e61af8f` | Same |
| `skills/logo-land/references/color-workflow.md` | `3f2f3d941fc5f72f64b0900059477e3f1fb2748b2bcdd4fdea24c1361f897b06` | Same |
| `skills/logo-land/references/delivery-checks.md` | `2f6aad601457654886dc6edb8065e4a91ef8719a3c2982becfc62a217ad604d8` | Same |
| `skills/logo-land/references/ip-mascot.md` | `08f93b78555246ea3b71a11d4879a53790808df4cab400bd5ed84b6d409e4850` | Same |
| `skills/logo-land/references/logo-directions.md` | `06eaf7c2e48bc93743f2dd76915105687bacc5a25a810932d5514bcf771049bc` | Same |
| `skills/logo-land/references/native-image.md` | `34056909420a4db68be7d00b09a18aabd450221529f814d73b7642369f096c3f` | Same |
| `skills/logo-land/references/project-files.md` | `f3f635a78005d3059885f6c55b69d3e07cd1e7fc92026a38be66555b155fcb42` | Same |
| `skills/logo-land/references/typography.md` | `137a3f88cb1287e31650d327399b66061e0ab6a5da8f246a48f005433ca8b56d` | Same |
| `skills/logo-land/scripts/logo_helper/__init__.py` | `23c8d2ce225a99efe9832a41c20b46d139f5b31049dd641a04e13ff83b84f4d0` | Same |
| `skills/logo-land/scripts/logo_helper/app_icon_cli.py` | `e09075977adfd8c0b98202242ab3759fb1145227df987aeaac33c31896d35ada` | Same |
| `skills/logo-land/scripts/logo_helper/app_icon_gallery.py` | `71a2a7873af195cdeefe312f6d0462552fd1bb8856c117b5a20349649371e43f` | Same |
| `skills/logo-land/scripts/logo_helper/app_icon_guide.py` | `c063bf22bbcfa82c982caa2c066db2b069b34f8d633ba3f6afdb1e9d4fd17012` | Same |
| `skills/logo-land/scripts/logo_helper/app_icon_models.py` | `21ba823e490677f5e70ce9d05c782b1fa12884f405c4ba4601fd052bb1209c2d` | Same |
| `skills/logo-land/scripts/logo_helper/app_icon_presets.py` | `0b7a5a4e01363a7f1bc1513a1c4bdba423d906edf722b322dab3253abfd849ae` | Same |
| `skills/logo-land/scripts/logo_helper/app_icon_prompts.py` | `d59ff54a2c77a368390be832bda5643af92dbab75d1a6431838687397e847080` | Same |
| `skills/logo-land/scripts/logo_helper/app_icon_publish.py` | `fb4dea5c484a4c617e898626d324a1aed5335e7b853299f45827d15d8a652ae5` | Same |
| `skills/logo-land/scripts/logo_helper/artifact_models.py` | `f35d32f2da234e92dd5144d48eb62fbddfac3039dd079b4d0a5d35eccd3231f0` | Same |
| `skills/logo-land/scripts/logo_helper/brief_models.py` | `caea33b207c181391fde6d9bc4fc7826335a8d2eb47f7124b51e5fbb18d16b12` | Same |
| `skills/logo-land/scripts/logo_helper/cli_options.py` | `e3f697458b482079c27b446cbb56aef4c6cf38ce3cd49ca94f1600ab76f4c8d3` | Same |
| `skills/logo-land/scripts/logo_helper/color_analysis.py` | `cfcef1c51c0f7a4067b7e9317df5b6f4acdb5312036e37516c9aab16f2d0ba30` | Same |
| `skills/logo-land/scripts/logo_helper/color_cli.py` | `d731f309d0dc877eb9f0ec71bf733c2461cda8757f9f15ac38fe7d0d7b9e3809` | Same |
| `skills/logo-land/scripts/logo_helper/color_delivery.py` | `7e7f0a4745def5b15ad08699dc57b113eca97eeeaa9b2aefaba35ef138d98f55` | Same |
| `skills/logo-land/scripts/logo_helper/color_gallery.py` | `05076788df31137f3ca6576a58346533130f2dd710779e35eb9311370ae6b56d` | Same |
| `skills/logo-land/scripts/logo_helper/color_gallery_cards.py` | `253ba8f0a439a4bb8129d2cb43463d5897df2d42cc9528ee627f8c709d669a53` | Same |
| `skills/logo-land/scripts/logo_helper/color_gallery_data.py` | `81dbf0876dc5cdc6e21493e80098489f54bc8e39dcb13bd3e61a38c5b998a030` | Same |
| `skills/logo-land/scripts/logo_helper/color_guide.py` | `34cdb38dddc6b398376fe5b492eef1799052b0b82a47bb48f3f4b801ea6f424a` | Same |
| `skills/logo-land/scripts/logo_helper/color_math.py` | `aa677d064632e48a9d108ba5d0b818c57f589ba1bcb61406261d8502cdc86288` | Same |
| `skills/logo-land/scripts/logo_helper/color_models.py` | `d3b4093611e2aa2d095c6c4f9027e65c794ef8b836c89d4a24c554f4a720f547` | Same |
| `skills/logo-land/scripts/logo_helper/color_profiles.py` | `055a299c1bd6738add1b44ad8977ffb48b9a3310bb9387665daa6efe04ca34df` | Same |
| `skills/logo-land/scripts/logo_helper/color_reports.py` | `95cf4f2605c8ca248a489d4e53fafee9f18b663d6effd38f3b5e5d080dd5596d` | Same |
| `skills/logo-land/scripts/logo_helper/color_sampling.py` | `71946e9eda8b329b5cafffc0163161abd2b17ddab3c92184bc5d4ba99ad94330` | Same |
| `skills/logo-land/scripts/logo_helper/color_workflow.py` | `7ef6e5c33c7f56d2320a643f5cd99428555b9eb4fa24fe65857b96147379cc42` | Same |
| `skills/logo-land/scripts/logo_helper/delivery.py` | `ed3713421b316e43568641451f41fc5a71332608acc8b8b2bf6c1db6f4469859` | Same |
| `skills/logo-land/scripts/logo_helper/export_bundle.py` | `33de44fb7677569d65c7b883c6d5b098c998e19bd9f731a6138ee9c09a1de612` | Same |
| `skills/logo-land/scripts/logo_helper/images.py` | `bd3d03ce8ab8fc7c6767da8fe8269e688ee63f16e14f04bf21d0e9d631a15f0a` | Same |
| `skills/logo-land/scripts/logo_helper/import_reports.py` | `69ffb9f6a9dbe5ac149fb9113f36ff63067cbad244c8c3a48af919e30223691c` | Same |
| `skills/logo-land/scripts/logo_helper/intent.py` | `244d7f1f4b0b07fa733c968ad130b84f9084719059f562385d55891e749b47fa` | Same |
| `skills/logo-land/scripts/logo_helper/legacy_state.py` | `09119091b50d9a4b8d9e4782636a8cddbd93b0d0fd197c774c129d2bc8ac3c5d` | Same |
| `skills/logo-land/scripts/logo_helper/lockup_models.py` | `0c0fb574ca59d4e6bb72ef26df4dcc36e013e354901840f4bf7cb30291c035cc` | Same |
| `skills/logo-land/scripts/logo_helper/model_base.py` | `0051b0fc239944f0143da201848f98d8c414c9d2d520f5de4f4718c88756c49e` | Same |
| `skills/logo-land/scripts/logo_helper/models.py` | `dc28d55027542510328ebdf80a820ed3456e6f6cfbd00cae102395026a0079ca` | Same |
| `skills/logo-land/scripts/logo_helper/palette_proposals.py` | `6968ca4356be8197ffdd68500ea2f53c72dff935c743e57305bb7ae4e10aca4b` | Same |
| `skills/logo-land/scripts/logo_helper/palettes.py` | `6c60dffcca290bd390e1259600cdd91e190589995af6c42152ba42f719d77e08` | Same |
| `skills/logo-land/scripts/logo_helper/prompts.py` | `340974db2816c5f0deecc766cfcabd8036d8e59e2608be5f1688657b57967a1b` | Same |
| `skills/logo-land/scripts/logo_helper/reference_decode.py` | `b55055f40a5fee8a01943acd082bfe8b7a521b61bb1773f36a208f5e5f9c453f` | Same |
| `skills/logo-land/scripts/logo_helper/reference_evidence.py` | `ab80fa6b9a19f77b525566c9f4b8129720dee403daea9994155e0888e2d0d1f4` | Same |
| `skills/logo-land/scripts/logo_helper/reference_models.py` | `87da637a01602f5dd0655ff6e8bfefae9ca2c609513dcbfe43a9f5e07553064e` | Same |
| `skills/logo-land/scripts/logo_helper/references.py` | `a02f6d9bf3775820bc4d394d539186c64da7ce96cb00a359e34e266acec4d3b7` | Same |
| `skills/logo-land/scripts/logo_helper/session_models.py` | `3d5917431dd8c8f7f43c2acc91dd845682b0d8483e1de835ba5794eda3dcdaea` | Same |
| `skills/logo-land/scripts/logo_helper/storage.py` | `e0a9bd8c18458beeda1a0ad9479afbec68ac6c4690b42f795dc3cdbd813b42a6` | Same |
| `skills/logo-land/scripts/logo_helper/workflow.py` | `a82d1cd1c02a16b4c202c1a01d08a6a5e44f18491d297bc01857c663dbbbd6d6` | Same |
| `skills/logo-land/scripts/logo_project.py` | `1bc33dbe2f06accd050aa069315d4b7bed0470a95bed10e18b5090b98eddd5fa` | Same |

</details>

<details>
<summary>Pre-existing dirty worktree inventory</summary>

```text
 M .codex-plugin/plugin.json
 M CHANGELOG.md
 M README.ko.md
 M README.md
 M THIRD_PARTY_NOTICES.md
 M docs/README.md
 M docs/brand/README.md
 M docs/releases.md
 M pyproject.toml
 M skills/logo-land/SKILL.md
 M skills/logo-land/references/native-image.md
 M skills/logo-land/references/project-files.md
 M skills/logo-land/scripts/logo_helper/artifact_models.py
 M skills/logo-land/scripts/logo_helper/brief_models.py
 M skills/logo-land/scripts/logo_helper/cli_options.py
 M skills/logo-land/scripts/logo_helper/delivery.py
 M skills/logo-land/scripts/logo_helper/intent.py
 M skills/logo-land/scripts/logo_helper/models.py
 M skills/logo-land/scripts/logo_helper/prompts.py
 M skills/logo-land/scripts/logo_helper/workflow.py
 M skills/logo-land/scripts/logo_project.py
 M uv.lock
?? assets/logo-land-studio.png
?? docs/app-icons/
?? docs/brand/2026-identity/
?? docs/brand/legacy.md
?? docs/qa/app-icons/
?? docs/research/app-icon-quality-sources.json
?? docs/research/app-icon-quality.md
?? docs/research/app-icon-sources.json
?? docs/research/app-icon-tools.md
?? docs/research/readme-structure.md
?? plans/logo-land-app-icons.md
?? skills/logo-land/assets/app-icon-gallery.template.html
?? skills/logo-land/assets/app-icon.example.json
?? skills/logo-land/assets/ip-as-logo.LICENSE
?? skills/logo-land/references/app-icons.md
?? skills/logo-land/references/ip-mascot.md
?? skills/logo-land/scripts/logo_helper/app_icon_cli.py
?? skills/logo-land/scripts/logo_helper/app_icon_gallery.py
?? skills/logo-land/scripts/logo_helper/app_icon_guide.py
?? skills/logo-land/scripts/logo_helper/app_icon_models.py
?? skills/logo-land/scripts/logo_helper/app_icon_presets.py
?? skills/logo-land/scripts/logo_helper/app_icon_prompts.py
?? skills/logo-land/scripts/logo_helper/app_icon_publish.py
?? tests/test_app_icon_compatibility.py
?? tests/test_app_icon_delivery.py
?? tests/test_app_icon_gallery.py
?? tests/test_app_icon_models.py
?? tests/test_app_icon_prompts.py
?? tests/test_app_icon_quality.py
?? tests/test_app_icon_workflow.py
?? tests/test_app_icon_workflow_invariants.py
?? tests/test_app_icon_workflow_palette.py
```

</details>

## Cleanup and handoff

Server PID `14511` received TERM at 2026-09-12 18:13:35 UTC; its exec session exited 143 as expected, and `lsof -nP -iTCP:8802 -sTCP:LISTEN` returned no listener. No other process was stopped. Exact temporary inventory registered under `/tmp/ll-readme-pages` and transcribed before deletion:

- `/tmp/ll-readme-pages/baseline.json`
- `/tmp/ll-readme-pages/download-baseline.json`
- `/tmp/ll-readme-pages/goyo-ko.http`
- `/tmp/ll-readme-pages/goyo-png.http`
- `/tmp/ll-readme-pages/goyo-reload.http`
- `/tmp/ll-readme-pages/goyo.http`
- `/tmp/ll-readme-pages/grove-png.http`
- `/tmp/ll-readme-pages/grove-zip.http`
- `/tmp/ll-readme-pages/http-evidence.json`
- `/tmp/ll-readme-pages/missing-download.md`
- `/tmp/ll-readme-pages/owned-pages.json`
- `/tmp/ll-readme-pages/quoted-input.md`
- `/tmp/ll-readme-pages/server.json`
- `/tmp/ll-readme-pages/validation.json`
- `/tmp/ll-readme-pages/verify-pages.rb`
- `/tmp/ll-readme-pages/write-pages.rb`
- `/tmp/ll-readme-pages/write-report.rb`

Public Markdown pages and this QA report are persistent deliverables. The root owner must create `docs/README.ko.md` and perform its final combined links/Chrome checks. No original image, prompt, package, historical HTML or source file requires restoration. Temporary cleanup completed after transcription.

Cleanup verified 2026-09-12 18:15:25 UTC: removed the exact owned temporary root and its 17 registered files; the directory is absent and port 8802 has no listener. Final owned checks passed for 43 Markdown files (UTF-8, final newline, whitespace, and tracked diff whitespace), with the four documented D1-C links still pending.
