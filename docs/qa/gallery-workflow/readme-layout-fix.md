# README sample paragraph layout fix

Task `task_26c0467ebc01`, dispatch `ctx_0f2fc172e41a`; shared branch `feat/logo-land-gallery-workflow`.

## Scope and progress

Only `README.md`, `README.ko.md`, and this report are owned. Preserve all other workers' changes. This is a paragraph-only layout correction; no production code, assets, installations, commits, pushes, or new tests.

- Complete: inspect both current READMEs and the actual baseline Chrome screenshot.
- Complete: pin baseline bytes and insert one paragraph boundary after sample 3 in each language.
- Complete: static invariants, local targets, bounded read-only HTTP requests, and final hashes.
- Complete: preserve evidence, stop/reap the owned server, and remove all 12 owned temporary files plus the empty temporary directory.

## Resources registered before creation

- Temporary root `/tmp/ll-060-readme-fix`: initially absent; exclusive creation required. Owned contents are `README.md.before`, `README.ko.md.before`, `baseline.json`, `static.json`, `http.json`, `README.md.diff`, `README.ko.md.diff`, `serve.rb`, `http.rb`, `server.log`, `server.pid`, and `server-exit.txt`. No other temporary directory or persistent script is permitted.
- Read-only repository server `127.0.0.1:8800`: initial `lsof -nP -iTCP:8800 -sTCP:LISTEN` found no listener. Register server-child PID before it executes `python3 -m http.server`; the Ruby supervisor must release that child only after recording its PID. Maximum lifetime 300 seconds; stop and reap only the owned child. No browser or GUI control.
- HTTP captures remain in memory until written to the registered `http.json`; each literal `curl -i --fail --connect-timeout 3 --max-time 20` has a 20-second bound. Temp cleanup must verify directory ownership and remove only the enumerated files, then the empty directory.
- Actual desktop/narrow GFM rendering belongs to browser owner `ctx_a04104359e84`; this worker's static/HTTP results are not a visual PASS.

## Baseline

Inspected [actual Chrome screenshot](chrome/09-readme-en-desktop.jpg), SHA-256 `d347a5d9d5cfe4a96b070a1a6cdb3a0b25a4c2ab47f75aa93851b616de546954`: Goyo, COMMON, MISO, reading owl, and weather appear in the first row; Relay appears alone below. Each source sample has width `160`, and the original six share one paragraph.

- `README.md`: `d260d80f97af11458355e75d34368966479b40c096929065cc4c9fee8e1a4aa9`.
- `README.ko.md`: `d03c6a92ec0b181e0c54e5eb64440d5152355323a13af13c1a9b1551d381737f`.
- Published release `v0.3.1`; development source `v0.6.0`.
- IP credit links remain `https://github.com/s1dashu/ip-as-logo-skill`, `skills/logo-land/references/ip-mascot.md`, `skills/logo-land/assets/ip-as-logo.LICENSE`, and `THIRD_PARTY_NOTICES.md` in both languages.

Server PID **7163** registered while its forked child was blocked on a pipe, before server execution; supervisor PID **7155**, lifetime bound 300 seconds. Command: `/usr/bin/python3 -m http.server 8800 --bind 127.0.0.1 --directory /Users/cillian/Documents/Github/Projects/logo-generator`. Temp directory device `16777230`, inode `35033544`.

## Exact change and invariants

Both languages gained only `</p>`, a blank line, and `<p>` after MISO. Reversing that insertion reproduces the entire pinned baseline byte-for-byte. All other text, English default, Korean badges, ordered six href/src/width/alt tuples, one-click gallery links, anchors, version statements and IP credits are unchanged. Ordered sample tuples and original PNG hashes are recorded below.

Each document has sample paragraph counts `[3, 3]`; all 18 unique local file targets in each language exist. The checker refused nonexistent `docs/samples/items/__ll060_missing__/delivery/logo.png` without creating that path. `git diff --check -- README.md README.ko.md docs/qa/gallery-workflow/readme-layout-fix.md` exited 0. Inline anchors remain eligible to wrap within each paragraph; actual narrow-screen overflow behavior is reserved for the browser owner.

Immediately after the edit, all 69 source payload files, all six PNGs and the foreign tracked diff matched the baseline. During final evidence collection, concurrent changes to other workers' source files were detected and preserved. This worker made no source payload edits; a whole-workspace source freeze is no longer claimed. Current concurrent source differences are recorded below. The original foreign tracked diff SHA-256 is `180ffeaaaa025261cc96e773283e01b6f2ff3a74961374df9dda44ab3a5089fd`; final observed SHA-256 is `180ffeaaaa025261cc96e773283e01b6f2ff3a74961374df9dda44ab3a5089fd`. Public README hashes changed as expected and need inclusion in integration's final documentation snapshot.

```json
[
  {
    "path": "skills/logo-land/assets/comparison-gallery.template.html",
    "before": "6dc83dcf23970c27c544b21806544a488cdef34338dd965d9e4a9bcbbc929849",
    "after": "2e9760669f0aa2d9d34267fce0241452f43de435c9c4985bce80be70afb309a3"
  }
]
```

### README.md

```diff
--- /tmp/ll-060-readme-fix/README.md.before	2026-09-13 09:52:49
+++ README.md	2026-09-13 09:53:05
@@ -28,6 +28,9 @@
   <a href="docs/samples/items/03-goyo/delivery/logo.png"><img src="docs/samples/items/03-goyo/delivery/logo.png" width="160" alt="고요 · Korean combination logo"></a>
   <a href="docs/gallery-workflow/images/common-v1.png"><img src="docs/gallery-workflow/images/common-v1.png" width="160" alt="COMMON · shared-workspace logo"></a>
   <a href="docs/samples/items/06-miso/delivery/logo.png"><img src="docs/samples/items/06-miso/delivery/logo.png" width="160" alt="MISO · mascot"></a>
+</p>
+
+<p>
   <a href="docs/app-icons/images/ip-a1.png"><img src="docs/app-icons/images/ip-a1.png" width="160" alt="Reading owl · IP character"></a>
   <a href="docs/app-icons-quality-v1/images/pictogram-quality-v1.png"><img src="docs/app-icons-quality-v1/images/pictogram-quality-v1.png" width="160" alt="Weather · revised pictogram"></a>
   <a href="docs/gallery-workflow/images/relay-v2.png"><img src="docs/gallery-workflow/images/relay-v2.png" width="160" alt="Relay · abstract refinement with a wider opening"></a>
```

Final SHA-256: `eb1d9d2c75ec36cdc148bf546c35e9cf21b7ac4e8f302dcab58f98f161440c31`.

### README.ko.md

```diff
--- /tmp/ll-060-readme-fix/README.ko.md.before	2026-09-13 09:52:49
+++ README.ko.md	2026-09-13 09:53:05
@@ -28,6 +28,9 @@
   <a href="docs/samples/items/03-goyo/delivery/logo.png"><img src="docs/samples/items/03-goyo/delivery/logo.png" width="160" alt="고요 · 한글 조합형 로고"></a>
   <a href="docs/gallery-workflow/images/common-v1.png"><img src="docs/gallery-workflow/images/common-v1.png" width="160" alt="COMMON · 공유 작업 공간 로고"></a>
   <a href="docs/samples/items/06-miso/delivery/logo.png"><img src="docs/samples/items/06-miso/delivery/logo.png" width="160" alt="MISO · 마스코트"></a>
+</p>
+
+<p>
   <a href="docs/app-icons/images/ip-a1.png"><img src="docs/app-icons/images/ip-a1.png" width="160" alt="독서 부엉이 · IP 캐릭터"></a>
   <a href="docs/app-icons-quality-v1/images/pictogram-quality-v1.png"><img src="docs/app-icons-quality-v1/images/pictogram-quality-v1.png" width="160" alt="날씨 · 수정 픽토그램"></a>
   <a href="docs/gallery-workflow/images/relay-v2.png"><img src="docs/gallery-workflow/images/relay-v2.png" width="160" alt="Relay · 가운데 틈을 넓힌 추상형 수정"></a>
```

Final SHA-256: `c3d10b3183b21e7466b1b83b4882a4922d629a921a3dc13f480d6833d6b13875`.

### Pinned sample identities and original PNG bytes

```json
{
  "samples": {
    "README.md": [
      [
        "docs/samples/items/03-goyo/delivery/logo.png",
        "docs/samples/items/03-goyo/delivery/logo.png",
        "160",
        "고요 · Korean combination logo"
      ],
      [
        "docs/gallery-workflow/images/common-v1.png",
        "docs/gallery-workflow/images/common-v1.png",
        "160",
        "COMMON · shared-workspace logo"
      ],
      [
        "docs/samples/items/06-miso/delivery/logo.png",
        "docs/samples/items/06-miso/delivery/logo.png",
        "160",
        "MISO · mascot"
      ],
      [
        "docs/app-icons/images/ip-a1.png",
        "docs/app-icons/images/ip-a1.png",
        "160",
        "Reading owl · IP character"
      ],
      [
        "docs/app-icons-quality-v1/images/pictogram-quality-v1.png",
        "docs/app-icons-quality-v1/images/pictogram-quality-v1.png",
        "160",
        "Weather · revised pictogram"
      ],
      [
        "docs/gallery-workflow/images/relay-v2.png",
        "docs/gallery-workflow/images/relay-v2.png",
        "160",
        "Relay · abstract refinement with a wider opening"
      ]
    ],
    "README.ko.md": [
      [
        "docs/samples/items/03-goyo/delivery/logo.png",
        "docs/samples/items/03-goyo/delivery/logo.png",
        "160",
        "고요 · 한글 조합형 로고"
      ],
      [
        "docs/gallery-workflow/images/common-v1.png",
        "docs/gallery-workflow/images/common-v1.png",
        "160",
        "COMMON · 공유 작업 공간 로고"
      ],
      [
        "docs/samples/items/06-miso/delivery/logo.png",
        "docs/samples/items/06-miso/delivery/logo.png",
        "160",
        "MISO · 마스코트"
      ],
      [
        "docs/app-icons/images/ip-a1.png",
        "docs/app-icons/images/ip-a1.png",
        "160",
        "독서 부엉이 · IP 캐릭터"
      ],
      [
        "docs/app-icons-quality-v1/images/pictogram-quality-v1.png",
        "docs/app-icons-quality-v1/images/pictogram-quality-v1.png",
        "160",
        "날씨 · 수정 픽토그램"
      ],
      [
        "docs/gallery-workflow/images/relay-v2.png",
        "docs/gallery-workflow/images/relay-v2.png",
        "160",
        "Relay · 가운데 틈을 넓힌 추상형 수정"
      ]
    ]
  },
  "pngs": {
    "docs/samples/items/03-goyo/delivery/logo.png": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
    "docs/gallery-workflow/images/common-v1.png": "9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b",
    "docs/samples/items/06-miso/delivery/logo.png": "10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649",
    "docs/app-icons/images/ip-a1.png": "7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b",
    "docs/app-icons-quality-v1/images/pictogram-quality-v1.png": "b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a",
    "docs/gallery-workflow/images/relay-v2.png": "a4066faa64d1f58024d1a44afb011694a1808b628b988ac71a0986e90069491d"
  }
}
```

## Actual HTTP surface evidence

Executed the literal commands below against the registered repository server. At `2026-09-13T00:54:04Z`, all **12 requests** returned `HTTP/1.0 200 OK` and curl exit 0. Each body equalled the local file before and after its request, and each PNG matched its pre-edit hash and image/png content type. The first eight requests fetch both READMEs followed by all six originals; each README was then fetched twice more, retaining identical bytes and `[3, 3]` counts. Maximum request duration: **0.012258s**.

Raw Markdown is served as application/octet-stream by the standard-library server; these checks establish transport and byte identity, not GFM rendering. Captured commands, headers, body lengths, hashes and paragraph counts follow.

```json
[
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/README.md",
    "exit": 0,
    "seconds": 0.012258,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: application/octet-stream",
      "Content-Length: 5336",
      "Last-Modified: Sun, 13 Sep 2026 00:53:05 GMT"
    ],
    "bytes": 5336,
    "sha256": "eb1d9d2c75ec36cdc148bf546c35e9cf21b7ac4e8f302dcab58f98f161440c31",
    "paragraphs": [
      3,
      3
    ]
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/README.ko.md",
    "exit": 0,
    "seconds": 0.00882,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: application/octet-stream",
      "Content-Length: 5984",
      "Last-Modified: Sun, 13 Sep 2026 00:53:05 GMT"
    ],
    "bytes": 5984,
    "sha256": "c3d10b3183b21e7466b1b83b4882a4922d629a921a3dc13f480d6833d6b13875",
    "paragraphs": [
      3,
      3
    ]
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/docs/samples/items/03-goyo/delivery/logo.png",
    "exit": 0,
    "seconds": 0.010535,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: image/png",
      "Content-Length: 898170",
      "Last-Modified: Sat, 12 Sep 2026 13:16:00 GMT"
    ],
    "bytes": 898170,
    "sha256": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
    "paragraphs": null
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/docs/gallery-workflow/images/common-v1.png",
    "exit": 0,
    "seconds": 0.010554,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: image/png",
      "Content-Length: 850531",
      "Last-Modified: Sun, 13 Sep 2026 00:29:23 GMT"
    ],
    "bytes": 850531,
    "sha256": "9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b",
    "paragraphs": null
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/docs/samples/items/06-miso/delivery/logo.png",
    "exit": 0,
    "seconds": 0.010994,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: image/png",
      "Content-Length: 1026254",
      "Last-Modified: Sat, 12 Sep 2026 13:16:05 GMT"
    ],
    "bytes": 1026254,
    "sha256": "10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649",
    "paragraphs": null
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/docs/app-icons/images/ip-a1.png",
    "exit": 0,
    "seconds": 0.011641,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: image/png",
      "Content-Length: 1060303",
      "Last-Modified: Sat, 12 Sep 2026 17:24:59 GMT"
    ],
    "bytes": 1060303,
    "sha256": "7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b",
    "paragraphs": null
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/docs/app-icons-quality-v1/images/pictogram-quality-v1.png",
    "exit": 0,
    "seconds": 0.010885,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: image/png",
      "Content-Length: 924939",
      "Last-Modified: Sat, 12 Sep 2026 18:25:12 GMT"
    ],
    "bytes": 924939,
    "sha256": "b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a",
    "paragraphs": null
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/docs/gallery-workflow/images/relay-v2.png",
    "exit": 0,
    "seconds": 0.010579,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: image/png",
      "Content-Length: 898003",
      "Last-Modified: Sun, 13 Sep 2026 00:31:34 GMT"
    ],
    "bytes": 898003,
    "sha256": "a4066faa64d1f58024d1a44afb011694a1808b628b988ac71a0986e90069491d",
    "paragraphs": null
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/README.md",
    "exit": 0,
    "seconds": 0.009308,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: application/octet-stream",
      "Content-Length: 5336",
      "Last-Modified: Sun, 13 Sep 2026 00:53:05 GMT"
    ],
    "bytes": 5336,
    "sha256": "eb1d9d2c75ec36cdc148bf546c35e9cf21b7ac4e8f302dcab58f98f161440c31",
    "paragraphs": [
      3,
      3
    ]
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/README.ko.md",
    "exit": 0,
    "seconds": 0.009026,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: application/octet-stream",
      "Content-Length: 5984",
      "Last-Modified: Sun, 13 Sep 2026 00:53:05 GMT"
    ],
    "bytes": 5984,
    "sha256": "c3d10b3183b21e7466b1b83b4882a4922d629a921a3dc13f480d6833d6b13875",
    "paragraphs": [
      3,
      3
    ]
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/README.md",
    "exit": 0,
    "seconds": 0.008733,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: application/octet-stream",
      "Content-Length: 5336",
      "Last-Modified: Sun, 13 Sep 2026 00:53:05 GMT"
    ],
    "bytes": 5336,
    "sha256": "eb1d9d2c75ec36cdc148bf546c35e9cf21b7ac4e8f302dcab58f98f161440c31",
    "paragraphs": [
      3,
      3
    ]
  },
  {
    "command": "curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8800/README.ko.md",
    "exit": 0,
    "seconds": 0.009146,
    "headers": [
      "HTTP/1.0 200 OK",
      "Server: SimpleHTTP/0.6 Python/3.9.6",
      "Date: Sun, 13 Sep 2026 00:54:04 GMT",
      "Content-type: application/octet-stream",
      "Content-Length: 5984",
      "Last-Modified: Sun, 13 Sep 2026 00:53:05 GMT"
    ],
    "bytes": 5984,
    "sha256": "c3d10b3183b21e7466b1b83b4882a4922d629a921a3dc13f480d6833d6b13875",
    "paragraphs": [
      3,
      3
    ]
  }
]
```

## Nine required classes

| Class | Evidence and result |
| --- | --- |
| 1. Malformed local target | Nonexistent sample target refused; all 18 actual local target files in each README exist. No missing path created. |
| 2. Injection | Exact ordered comparison of every HTML href/src/width/alt attribute passed; inverse-insertion comparison preserves trusted markup and escaping. No user-data execution introduced. |
| 3. Cancel/resume | Three GETs per language preserved exact bytes and navigation targets. GETs do not mutate README state; generation/install cancellation is outside this change. Browser navigation remains browser-owned. |
| 4. Stale state | Both baseline README hashes checked immediately before editing. Static, repeated served responses and final files match the LAYOUT READY hashes. Concurrent foreign source changes were detected and retained. |
| 5. Dirty workspace | This task wrote only two owned README files and this report. Six PNGs remain unchanged. Initially 69 source payload files and the foreign tracked diff were unchanged; later observed concurrent source differences are recorded above and were not reverted. |
| 6. Hung operation | Each curl used connect timeout 3 seconds and total timeout 20 seconds; server supervisor bound was 300 seconds. All requests completed. Server PID 7163 was terminated/reaped, supervisor 7155 exited 0, both PIDs are absent and port 8800 is free. |
| 7. Flaky behavior | No failing HTTP request or blind HTTP rerun. Repeated GETs were planned stability checks. LAYOUT READY initially rejected conflicting payload flags; the corrected invocation delivered once as msg_6dcd1fc64671. A final collector correctly stopped on a concurrent foreign source change; the diagnostic used unavailable Ruby filter_map once, then switched to Ruby-compatible map/compact. Neither incident changed source or README data. |
| 8. Misleading results | Baseline Chrome screenshot shows 5+1. Static/HTTP checks establish source paragraphs and bytes only. Final Chrome desktop/narrow visual acceptance remains root/browser owner ctx_a04104359e84. |
| 9. Repeated interruptions | Three independent GETs per language returned the same hashes, 3+3 groups and links; no request left partial repository output. Actual Chrome reload/back/forward interactions remain browser QA. |

Native generation, schema mutations, installation, full test suites, code diagnostics and builds are N/A for this reversible Markdown-only change. No tests or dependency operations were added or run. This task exercised its assigned HTTP surface and did not control Chrome.

## Handoff and cleanup

LAYOUT READY was delivered with both hashes before HTTP QA. Server receipt: `reaped pid=7163 status=#<Process::Status: pid 7163 SIGTERM (signal 15)>`; supervisor tool session 1218 exited 0. `lsof -nP -iTCP:8800 -sTCP:LISTEN` exited 1 with no output, and kill(0) confirmed PIDs 7163 and 7155 absent. Temporary cleanup follows after preserving this evidence.

**Own static/HTTP scope: PASS. Chrome visual gate: pending root/browser owner.**

### Owned temporary cleanup inventory

Directory ownership matched device 16777230 / inode 35033544. Exactly 12 registered files were present; all evidence had been preserved above. The following pre-removal hashes identify the owned files:

```json
{
  "README.ko.md.before": "d03c6a92ec0b181e0c54e5eb64440d5152355323a13af13c1a9b1551d381737f",
  "README.ko.md.diff": "5d66ab86437e3db042d51cf472833b5e9b3809b614adaaf538ab05af2a257c6e",
  "README.md.before": "d260d80f97af11458355e75d34368966479b40c096929065cc4c9fee8e1a4aa9",
  "README.md.diff": "36c3882ace17d264bb6f17023ff4e18826d44425791dda9d4740bb7cd87ecba4",
  "baseline.json": "7e0ba1a79308013a4d64f8d9238a4bdb33cfcb4658643352ac66d52cafaae83c",
  "http.json": "bd3880b29c82ba9edf30f0485abee9cb37fedec52b5fbdf62125cf40d7813607",
  "http.rb": "55514ba1ac41e45c3592538d3a75fa51ec2c5107129dd60e5d70b90982dad3e6",
  "serve.rb": "5d6c7789bc8dd858758571a341a0c6081f8dcb8116258c47e8d04b40ec70074b",
  "server-exit.txt": "2ad2a9f0679c7c16141e6f0c7324a7de087578f6b4932d3a09d04ec232366e99",
  "server.log": "9304598a74a7157364fc8621c6e21df5f964932c7695ce5a508728bda209251a",
  "server.pid": "87cab300736ea36b207fd620be7f7b77550cf7f9d1c5d9e7f206a074e1d012a4",
  "static.json": "d2a19573cce04436a2a1cf164eb2ec615fd9a9ee993075f83026de692ce9b7e5"
}
```

Cleanup PASS: `/tmp/ll-060-readme-fix` is absent after removal of only the twelve inventoried files and its empty directory. Final inverse-insertion checks and all six PNG hashes passed immediately before cleanup. Both README final hashes remain those in LAYOUT READY; browser desktop/narrow visual acceptance is still assigned to root/browser owner.
