# Personal installation follow-up: browser restoration

**PASS, including cleanup.** One official refresh installed `0.6.0+codex.20260913005849`. The actual returned-cache helper reproduces the frozen source output, and its COMMON/Drip comparison passed CLI and HTTP download verification. Source stays pure `0.6.0`. A new Codex thread is required to load the refreshed skill; this worker does not claim current-thread reload.

Task `task_457cdb1c8d36`, dispatch `ctx_0904a67e1a1a`. Full normalized command arguments, actual stdout/stderr, timeout/exit/PID receipts, source bindings and complete file maps are retained in [installation-followup.json](installation-followup.json). Raw response hashes bind private captures; only local path prefixes are normalized. Previous [installation.md](installation.md) and [installation.json](installation.json) remain byte-identical historical evidence.

## Completed execution ledger

1. Matched every one of the 74 T3 final personal/cache hashes, including the exact file sets, against previous `0.6.0+codex.20260913004309`. Discovered the actual old cache by read-only manifest enumeration under the real Codex homes, then deduplicated resolved paths.
2. Received root `SOURCE READY: Chrome regression passed`, message `msg_90d31b9e7163`, after browser-owner closure `msg_f1148b50391f`. Reverified the frozen source and old installed bytes before copying or installing.
3. Copied only `skills/logo-land/assets/comparison-gallery.template.html`, preserved `THIRD_PARTY_NOTICES.md`, applied the official default cachebuster once and ran `codex plugin add logo-land@personal --json` once.
4. Validated source/personal/cache through the official plugin-creator validator and three `uv lock --check` calls. Executed the actual returned helper, retained CLI/HTTP and preservation evidence, then removed and verified all owned temporary resources.

## Installation and source binding

| Check | Actual result |
|---|---|
| Previous installation | `0.6.0+codex.20260913004309`; all 74 personal and cache hashes equal T3 |
| Source changes since T3 | Exactly one payload file: comparison HTML template |
| New official version | `0.6.0+codex.20260913005849`; one add, exit 0, 0.141 seconds |
| Personal/cache | 74 files, complete byte equality; aggregate `28a6d9bfe442fc17f5a39b421a3e2c0a349832f5ea998dee0068e0dbab6694c0` |
| Source equality | All 73 non-manifest files match; manifest content differs only by the official single timestamp suffix |
| Frozen template | `2e9760669f0aa2d9d34267fce0241452f43de435c9c4985bce80be70afb309a3` |
| Installed all-eight output | All 18 files equal the current source-helper/public output; index `66e8ac8fd728f85a683ee041437a2a0fbe56a2f4b89902fb9eefc4c1d29610c6` |
| COMMON/Drip index | `ef8d9bde7e5f0e95c8801391e60e10638add86ddab135cd1fbe209c734508ec6` |
| Marketplace | Existing `personal` → local `./plugins/logo-land`; unchanged SHA `422580558aa3790de35022394fc5b29eb3e15af1bea4e419bd615c95169598e6` |

The prior cache was verified again immediately before official add. The official command removed it after successful replacement; this worker did not delete any cache. The new helper path came directly from `installedPath` in that command's actual JSON response, with returned and resolved paths captured. No cache path was inferred from a version label.

The installed template is byte-identical to the frozen template. Its single script is byte-identical to the generated COMMON/Drip script and includes `window.addEventListener("pageshow", update);`. Independently, using the saved eight-item selection through the installed helper regenerated all 18 public comparison files exactly. These checks bind this installation to the source worker's actual regression: 2 passing PIN cases, 4 failing restoration cases before the edit, then all 6 passing after it and 58 targeted cases passing. Exact source evidence is preserved and linked in [browser-restoration.json](browser-restoration.json).

## Actual installed CLI and HTTP surface

Restored the six real native sessions byte-for-byte from the read-only private workspace. Fresh installed `show` calls matched all six states exactly: COMMON, Drip, Leaflet and Teum revision 1; Relay and Sprig revision 2. All 14 copied state/PNG files and all 37 protected source PNG/prompt/state files remained unchanged. Every selection and review stayed null.

The primary installed CLI returned `{"path":"gallery","index_path":"gallery/index.html","count":2}`. Its manifest identifies **common / v1 / COMMON / brand** and **drip / v1 / Drip / app_icon** separately. No state or artifact was regenerated. COMMON's 1774 × 887 original and Drip's 1254 × 1254 original retain their exact native PNG and prompt bytes.

The literal installed argv is retained in JSON; the private cache prefix is normalized here:

```sh
uv run <cache:0.6.0+codex.20260913005849>/skills/logo-land/scripts/logo_project.py --workspace <temporary-root>/workspace compare-gallery --selection-file <temporary-root>/inputs/selection.json --output gallery
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8801/gallery/index.html
```

The actual curl response was **HTTP/1.0 200 OK** and its body exactly equalled the generated index. Four additional HTTP downloads returned 200 and matched both the manifest and originals:

| Download | Exact SHA-256 |
|---|---|
| COMMON PNG | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` |
| COMMON prompt | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` |
| Drip PNG | `8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f` |
| Drip prompt | `67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d` |

The Chrome owner separately observed fresh reload → Brand + Web header + Dark → COMMON Original PNG → toolbar Back restoring the correct controls, identity and 1-of-8 result. This report attributes that observation to root's explicit SOURCE READY message. This worker's HTTP/CLI checks do not substitute for Chrome observation.

## Nine adversarial classes

| Class | Observed result or limit |
|---|---|
| Malformed/boundary | Actual truncated JSON, duplicate source, stale revision and old child revision refused; no destination. Existing destination bytes preserved; stale import produced no artifact. |
| Hostile notes | Closing script, event-handler markup, command substitution and backticks remain escaped data; only one authored script and no sentinel file. |
| Cancel/resume | Previous cache verified through the official replacement boundary. Two rounds of fresh show/prompt preserve saved bytes. Deliberate installation cancellation is N/A. |
| Stale/dirty state | Full old 74-file maps checked first and again before writes, root freeze honored, only expected template copied, shared unowned work preserved. |
| Hung commands | Helper/validator 30s, official add 120s, curl 20s; server lifetime 300s plus explicit termination/reap. No timeout or surviving registered process group. |
| Flaky results | One official add and one cachebuster; no blind retry, image call or native budget mutation. Disposable collector corrections disclosed below. |
| Misleading success | Actual returned cache/version/bytes, count 2, distinct v1 identities, 18-file regeneration and exact HTTP download hashes checked independently. |
| Repeated interruptions | One durable task/dispatch and receipt; repeated fresh reads do not reset state. No actual interruption; destructive install interruption is N/A. |
| Real surface/native cost | Actual cache CLI and HTTP executed; independent Chrome closure attributed explicitly. All unselected/unapproved values preserved, no new native image call. |

## Resource ownership and final cleanup

Registered before creation: `/tmp/ll-060-install-followup`; `admin.rb`, `refresh.rb`, `smoke.rb`, `finish.rb`; evidence, input, workspace and download descendants; the server command and `127.0.0.1:8801`. Each child argv/timeout was logged before spawn and its PID immediately afterward. Server PID **17657** was bounded to 300 seconds, explicitly terminated with SIGTERM and reaped. Both the initial bind probe and final `lsof`/bind checks confirm port availability.

Cleanup preserved the complete 99-file temporary inventory in JSON, verified each file's hash immediately before deletion, and removed only those files followed by empty owned directories. The temporary root's device/inode was rechecked before deletion. `/tmp/ll-060-install-followup` is absent, all registered PIDs including cleanup driver **18932** are absent, and no owned child group or port listener remains. Final source, personal/cache, original/session, marketplace and historical evidence checks passed.

Retained intentionally: the personal runtime payload, official returned cache and this report pair. No production code, tests, README, metadata, `.omo`, marketplace/configuration or dependency edits were made. No new mirror test or broad source pytest repeat was added. The known unrelated astral marketplace manifest failure from T3 was not re-probed.

Disposable harness corrections: two initial read-only marketplace path probes returned ENOENT because the personal marketplace's home-relative source path was incorrectly resolved against its manifest directory; the final check followed the official scaffold's home/plugins default. The temporary smoke script also had a bracket typo caught by Ruby parsing before execution; after correction, `ruby -c` passed and smoke ran once. These issues caused no payload write, installation retry or native operation. System Ruby 2.6-compatible collections were used throughout.
