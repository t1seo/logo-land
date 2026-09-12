# Eleven native app icon originals

PASS: eleven exact candidate IDs, six presets and six IP candidates are preserved in [Small canvas, big character.](../../app-icons/index.html). All PNGs are 1254 × 1254; their bytes, prompts, intent and native receipt identities agree across source, session, catalog, published files and HTTP downloads. These checks establish provenance and byte integrity, not artistic approval, strict-color conformance, approved export or platform acceptance.

[Machine-readable lineage](native-samples.json) · [Sample plan](sample-plan.json) · [Gallery manifest](../../app-icons/manifest.json)

## Source and import lineage

All eleven native tasks completed successfully before catalog imports began. Each candidate had exactly one native call with prompt only, no previous-candidate reference and no artistic retry. The tool is recorded exactly per source receipt; model and standalone call identifiers were unreported. Basenames below identify the actual returned files, not a claimed request ID. All exact basenames resolved uniquely under the native output root and their files were rehashed; absolute locators are retained privately in ignored `output/app-icons-catalog/native-locators.json`.

The catalog was initialized through the actual helper in the repository workspace with session `icon-collection` and brand name `Small canvas, big character.`. Eleven normal imports used the exact native prompt, explicit matching `app_icon`, `--background opaque` and current catalog revisions 0–10. The source generation revision remains 0 for every candidate; each source session is revision 1. Catalog revision 11 was published once through `icon-gallery` into the previously absent `docs/app-icons` directory, without selection, review, export or session mutation. Catalog copies are not new generations.

| ID / native receipt | Native returned basename | Original SHA-256 | Bytes | Native / catalog import revision |
|---|---|---|---:|---|
| [ip-a1](native/ip-a1.json) | `exec-444bd22d-69ea-4e81-98f4-1dc7ebd416fd.png` | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` | 1060303 | 0 / 0 → 1 |
| [ip-a2](native/ip-a2.json) | `exec-69f1932c-a98e-4c6c-b9c5-3c64bf120ae1.png` | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` | 1049136 | 0 / 1 → 2 |
| [ip-b1](native/ip-b1.json) | `exec-46b22cd1-2320-47a0-b4d1-f9a813e87f71.png` | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` | 1083251 | 0 / 2 → 3 |
| [ip-b2](native/ip-b2.json) | `exec-6c5ded23-7e8a-44cd-8e78-70a59a8c6aa6.png` | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` | 1039677 | 0 / 3 → 4 |
| [ip-c1](native/ip-c1.json) | `exec-fcd63f18-bfca-4dca-bb67-b27effbd7ab7.png` | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` | 1096895 | 0 / 4 → 5 |
| [ip-c2](native/ip-c2.json) | `exec-d0d7d47e-9949-48a5-acb8-3d7c9ff2451e.png` | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` | 1089169 | 0 / 5 → 6 |
| [pictogram](native/pictogram.json) | `exec-4e4775d9-cddf-442d-8f5a-3af6c2e329ae.png` | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` | 928736 | 0 / 6 → 7 |
| [abstract](native/abstract.json) | `exec-305eb971-5233-4957-a723-75a26bc6bf7a.png` | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` | 961065 | 0 / 7 → 8 |
| [monogram](native/monogram.json) | `exec-b849c41f-2ed6-4d2c-8a56-2637857a1cb9.png` | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` | 832716 | 0 / 8 → 9 |
| [soft-3d](native/soft-3d.json) | `exec-0877f8d4-36ca-4f37-845d-e9063d2b0fd4.png` | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` | 1526612 | 0 / 9 → 10 |
| [pixel-art](native/pixel-art.json) | `exec-0402d8c4-45f5-43f8-9755-0b0c1bf928f2.png` | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` | 946180 | 0 / 10 → 11 |

Every row is PNG, 1254 × 1254, with requested background `opaque`. Source/native/session/catalog/published/HTTP hashes are all identical. Exact source sessions, receipt hashes, native-result hashes, source and catalog paths, full prompts, prompt hashes and frozen icon intent are recorded per row in the JSON. The Korean monogram requests exactly `모`. The first six IP candidates represent owl, capybara and puppy reading companions with left/right requested placements. Extra objects, highlights, shading and other artistic variation remain unchanged.

## Executed verification

- **PASS** — receipt and source state unchanged since PIN.
- **PASS** — fresh-process saved catalog resume twice.
- **PASS** — duplicate gallery IDs.
- **PASS** — existing destination.
- **PASS** — duplicate artifact import.
- **PASS** — stale import revision.
- **PASS** — stale source hash.
- **PASS** — hostile text data.
- **PASS** — malformed intent JSON.
- **PASS** — truncated receipt rejected in memory.
- **PASS** — actual schema and full PNG decoder.
- **PASS** — HTTP original and exact prompt downloads.
- **PASS** — dirty worktree and old galleries preserved.
- **not_applicable** — cancel/repeated interruption: No native calls or actual interruptions in this task; same receipt IDs verified and fresh-process catalog resumes executed without regeneration.
- **PASS** — hung commands/flaky artistic retries: Every helper command bounded to 30 seconds; curl connect 2 seconds and total 10 seconds; no native call or artistic retry.
- **PASS** — misleading success: Gallery contains all 11 originals; selected_id is null, every review is null, exports empty; no strict conformance or platform approval claim.

Parsed 183 source-workspace JSON records and all eleven public receipts. Actual helper `show` loaded and validated every source session; actual `GalleryManifest` and `Session` models validated the published manifest and catalog, and the helper fully decoded all eleven PNGs. Two new helper processes resumed the saved catalog at revision 11 without mutation. All six `icon-presets` entries matched the catalog coverage.

Negative probes required nonzero errors for duplicate IDs, duplicate import, existing destination and stale revision; the live catalog and published tree remained byte-identical. The stale-source probe altered only a disposable copied session's expected SHA and received `hash_mismatch` with no destination left behind. Hostile subject/brand text was escaped in HTML, hostile prompt text remained exact UTF-8 in its download, no executable script element appeared in the CSS-only page and no shell marker was created. Malformed intent and truncated receipt JSON were rejected. No product source change or artificial source test was required for this operational publication task.

The audit harness initially needed normalization for ip-c1's direct intent shape. Two preliminary hostile-text checks assumed one script element; inspecting the actual CSS-only template corrected the expectation to zero. These were probe assumptions, not native generation failures or product fixes; all owned temporary resources were removed each time. Final actual QA passed. Full bounded command outputs and preliminary evidence remain in `output/app-icons-catalog/`.

## HTTP checks

An owned local server on 127.0.0.1:8781 served the actual published directory. The HTML, manifest, eleven original PNGs and eleven prompt files all returned HTTP 200 and exact source bytes (24 responses). Each request used:

```sh
curl -i --fail --silent --show-error --connect-timeout 2 --max-time 10 http://127.0.0.1:8781/index.html
```

The recorded commands appended an owned temporary output path so binary response bodies could be compared without terminal rendering. The same flags were used for every original and prompt URL below.

| Response path | HTTP | Body bytes | Body SHA-256 | Source bytes |
|---|---:|---:|---|---|
| `index.html` | 200 | 21510 | `e87c1e9d3a78b6404d5560d8e778e8ef812618e7f13d1e7ed7a1d3b18e74a1bd` | exact match |
| `manifest.json` | 200 | 6655 | `fe6b2183a34beadf3932f00a63999ba17015792f15f87511b14a0ed9d9801dc9` | exact match |
| `images/ip-a1.png` | 200 | 1060303 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` | exact match |
| `prompts/ip-a1.txt` | 200 | 1377 | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` | exact match |
| `images/ip-a2.png` | 200 | 1049136 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` | exact match |
| `prompts/ip-a2.txt` | 200 | 1393 | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` | exact match |
| `images/ip-b1.png` | 200 | 1083251 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` | exact match |
| `prompts/ip-b1.txt` | 200 | 1391 | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` | exact match |
| `images/ip-b2.png` | 200 | 1039677 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` | exact match |
| `prompts/ip-b2.txt` | 200 | 1394 | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` | exact match |
| `images/ip-c1.png` | 200 | 1096895 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` | exact match |
| `prompts/ip-c1.txt` | 200 | 1388 | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` | exact match |
| `images/ip-c2.png` | 200 | 1089169 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` | exact match |
| `prompts/ip-c2.txt` | 200 | 1403 | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` | exact match |
| `images/pictogram.png` | 200 | 928736 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` | exact match |
| `prompts/pictogram.txt` | 200 | 1056 | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` | exact match |
| `images/abstract.png` | 200 | 961065 | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` | exact match |
| `prompts/abstract.txt` | 200 | 1097 | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` | exact match |
| `images/monogram.png` | 200 | 832716 | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` | exact match |
| `prompts/monogram.txt` | 200 | 1060 | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` | exact match |
| `images/soft-3d.png` | 200 | 1526612 | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` | exact match |
| `prompts/soft-3d.txt` | 200 | 1091 | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` | exact match |
| `images/pixel-art.png` | 200 | 946180 | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` | exact match |
| `prompts/pixel-art.txt` | 200 | 1110 | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` | exact match |

### Captured response headers

<details><summary>index.html</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:51 GMT
Content-type: text/html
Content-Length: 21510
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>manifest.json</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:51 GMT
Content-type: application/json
Content-Length: 6655
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/ip-a1.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:51 GMT
Content-type: image/png
Content-Length: 1060303
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/ip-a1.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:51 GMT
Content-type: text/plain
Content-Length: 1377
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/ip-a2.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:51 GMT
Content-type: image/png
Content-Length: 1049136
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/ip-a2.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:51 GMT
Content-type: text/plain
Content-Length: 1393
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/ip-b1.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 1083251
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/ip-b1.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1391
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/ip-b2.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 1039677
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/ip-b2.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1394
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/ip-c1.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 1096895
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/ip-c1.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1388
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/ip-c2.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 1089169
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/ip-c2.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1403
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/pictogram.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 928736
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/pictogram.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1056
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/abstract.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 961065
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/abstract.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1097
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/monogram.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 832716
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/monogram.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1060
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/soft-3d.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 1526612
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/soft-3d.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1091
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>images/pixel-art.png</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: image/png
Content-Length: 946180
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

<details><summary>prompts/pixel-art.txt</summary>

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:27:52 GMT
Content-type: text/plain
Content-Length: 1110
Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT
```

</details>

## Preservation, cleanup and scope

The shared worktree was dirty before this task. All 236 existing sample/color gallery files retained their pinned hashes. Edits were limited to assigned documentation, the new gallery, aggregate reports and ignored catalog workspace; other contributors' changes were preserved. Earlier color failure records and release gates remain unchanged. Source version is 0.5.0 development/unreleased, the old 0.4.0 draft remains unpublished and public release is 0.3.1.

Server port, log, temporary download paths and resource owner were registered before spawn; owned PID 22327 was then recorded and terminated with SIGTERM. All temporary responses, probe sessions and server logs were removed from the owned temporary directory. The server log is retained as evidence in ignored `qa-results.json`. `lsof` found no 8781 listener and a fresh bind/release succeeded. Native originals, source sessions and the persistent catalog were retained.

Chrome interaction and browser-download QA remains separately owned by the coordinator's Chrome task. No commit, release, new native call, ranking or approval was performed here.

Documentation checks passed: 275 local links resolve, both READMEs use the same six original PNG previews linked to the full gallery, EN/KO sample/size/version claims match, earlier README color/logo sections and the historical 0.4.0/0.3.1 changelog text are unchanged, and authored-file whitespace checks exit 0.
