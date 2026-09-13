# Comparison gallery implementation evidence

Dispatch: `task_5b734efaf55f` / `ctx_58d0a06b54af`. Branch: `feat/logo-land-gallery-workflow`. Base: `06b94c41922973fc98392fadde25fff9aa498f6e`.

## Execution ledger

- [x] PIN old icon-gallery output/source bytes with two artifact IDs.
- [x] RED mixed-session v1/v1 compare-gallery unknown command.
- [x] GREEN implementation, adversarial regressions, required checks.
- [x] Actual CLI and bounded HTTP download/hash QA.
- [x] Cleanup receipt and coordinator handoff.

## Resource registration (before creation)

- DONE `/tmp/ll-060-compare`: exclusively create for CLI/HTTP QA; remove only this owned directory after preserving evidence here.
- DONE `127.0.0.1:8790`: check unoccupied before starting owned server; register actual PID; terminate only that PID after download QA.
- Pytest temporary directories are created/managed by pytest. Automated tests start no external servers.

## Scope

No generation, installs, commits, source-session writes or approval mutation in this command. Browser visual/interaction QA is root-owned T4. Code checks do not establish artwork quality.

## Active resource receipt

- `/tmp/ll-060-compare` created exclusively: device `16777230`, inode `34983239`.
- Owned server PID `38972`, tool exec session `22597`, bound only to `127.0.0.1:8790`, maximum lifetime 300 seconds; teardown completed below. Port was unoccupied before launch.

## Actual HTTP receipt

The CLI returned `{"path":"gallery","index_path":"gallery/index.html","count":2}`.

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sun, 13 Sep 2026 00:21:12 GMT
Content-type: text/html
Content-Length: 15409
Last-Modified: Sun, 13 Sep 2026 00:20:53 GMT
```

Downloaded HTML bytes exactly matched the on-disk index. Parsed article identities: `(brand, v1, revision 1)` and `(icon, v1, revision 1)`, with kinds `brand` and `app_icon`.

| Source | PNG dimensions | Downloaded PNG SHA-256 | Exact prompt SHA-256 |
|---|---|---|---|
| brand / v1 | 1774 × 887 | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` | `aade1fdadd545f9d551382156db17ff43010a6fa10ce293e105cdf5ce5857c21` |
| icon / v1 | 1254 × 1254 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |

All five requests returned 200. PNG/prompt download hashes matched both the source files and the gallery manifest. Source JSON and original artifact checks after publication:

```text
8f262d3816aa83d234f07833721b9e8880e90c48a8499984a2b6fab0da974fe8  /tmp/ll-060-compare/.logo-generator/sessions/brand/session.json
cee9be43fc3c6dbb60110c26af449ca6698f6b2f1521f022ce31b062c22f7308  /tmp/ll-060-compare/.logo-generator/sessions/icon/session.json
f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343  /tmp/ll-060-compare/.logo-generator/sessions/brand/artifacts/v1.png
f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42  /tmp/ll-060-compare/.logo-generator/sessions/icon/artifacts/v1.png

```

HTTP HTML SHA-256: `e282e9958b53abffb9138bf57d86d9f2ad7866be1c84edff1a0fd488769a812d`.

## PIN → RED → GREEN

Before any production changes:

1. Added `tests/test_comparison_baseline.py`, then ran `uv run pytest -q tests/test_comparison_baseline.py`: **1 passed in 0.96s**. The actual old `icon-gallery` CLI received explicit `v2,v1`; original PNG bytes, exact CRLF prompt bytes and every saved source file matched before/after. Both candidates were unreviewed.
2. Added `tests/test_comparison_cli.py` with two real mixed brand/icon sessions, each containing `v1`, then ran `uv run pytest -q tests/test_comparison_cli.py`: **1 failed in 0.43s**, with the intended actual subprocess exit **2** and error `No such command 'compare-gallery'. Did you mean 'color-gallery', 'icon-gallery'?`.
3. Added comparison input/provenance models, escaped cards, renderer, template and two-line CLI registration. Ran `uv run pytest -q tests/test_comparison_baseline.py tests/test_comparison_cli.py`: **2 passed in 1.01s**.
4. Added edge regressions. The focused command progressed from **69 passed in 4.55s**, through **80 passed in 4.73s** and **80 passed in 6.31s**, to **82 passed in 15.31s** after maximum-size and selection-symlink cases. These are observed executions, not dry runs.
5. Initial strict checks found **37 Ruff issues** (format/line length, raw regex markers, one test-complexity warning, control-code constant) and **9 basedpyright errors** (implicit string concatenation, unnecessary match binding, private-import references in tests, ignored `Path.replace` result). Corrected the owned files; subsequent Ruff check passed and basedpyright reported **0 errors, 0 warnings, 0 notes**.

## Implementation contract

```sh
uv run python skills/logo-land/scripts/logo_project.py --workspace <existing-workspace> compare-gallery --selection-file <selection.json> --output <relative-directory>
```

Input fields exactly match the approved plan. Title is required and bounded to 200 characters; the four optional decision texts default to empty and are bounded to 2,000 characters each. The CLI rejects selection documents above 4 MiB after the existing bounded regular-file reader. Unknown fields, coercible revisions, invalid IDs, duplicate `(session, artifact)` pairs, empty selections and more than 60 candidates are rejected. Accepted count and maximum text boundaries are exercised through the CLI's 20-second timeout.

Each manifest artifact has `source` containing the explicit session/revision/artifact and all four decision texts; immutable parent ID, brand, kind/style, icon/lockup intent, decoded `image` facts, `sha256`, `prompt_sha256`, `image_file` and `prompt_file` accompany it. Files are assigned by ordered selection position: `images/001.png`, `prompts/001.txt`, etc. Both saved revision and decoded image/hash are checked before publication; revision/source integrity is rechecked after staging. `Store.load`, safe paths and the existing inode-aware exclusive publisher are reused.

No selection, approval, prompt or session write occurs. All creative candidates remain comparable regardless of review, while `export` still rejects an unreviewed selected candidate. Contexts and sizes are CSS previews; PNG bytes are not resized or re-encoded. The template has no remote dependencies and no fetch, shell, eval or user text embedded in JavaScript. Local notes remain selectable when clipboard permission/API access is unavailable. Control characters below U+0020 except whitespace are displayed as visible escaped notation; the manifest preserves their exact JSON data.

The Python modules own separate responsibilities: selection/provenance contracts, CLI boundary, snapshot publication and escaped markup. All are below 250 code lines. Untrusted selection data is parsed once by strict frozen Pydantic models; no `Any`, casts or type-ignore escapes were introduced. Existing app-icon renderer/template and original sample bytes remain untouched.

## Adversarial observables (nine classes)

| Class | Actual probe | Observable result |
|---|---|---|
| 1. Malformed/boundary input | CLI `{`, array/null/empty objects, unknown root/item fields, boolean/string/negative revision, blank title; model 0/61 items and 201/2001-character texts; duplicate pair across revisions | Exit 1 or strict boundary error; no destination/index; exact source bytes preserved |
| 2. Injection and hostile data | Closing textarea, img/onerror/script tags, remote URL, `javascript:`, quotes, ampersand, `$cards`, shell-looking substitution, NUL/ESC, CRLF and Korean text in notes/brand | HTML parser sees only the one authored script, no event attributes, no injected download/src URL; manifest retains exact notes; no `nope` file is created |
| 3. Cancellation/retry | KeyboardInterrupt before image, prompt, manifest and index link; two cancellations per phase followed by real retry | Every cancellation removes owned partial destination/staging; retry completes with two candidates; no source mutation |
| 4. Stale/missing/tampered state | Wrong initial revision, revision advance during staging, missing session/artifact, missing PNG, tampered bytes, wrong decoded dimensions, SVG bytes in saved PNG location | Explicit stale/not-found/file/hash/metadata errors; no published index; concurrent newer revision survives |
| 5. Paths/dirty state/foreign ownership | Traversal/absolute/backslash/drive/reserved outputs, dirty output, output/parent/source/state/selection symlinks, foreign inode replacing already-linked image during cancellation | Paths fail; existing foreign files and replacement inode survive rollback; incomplete gallery never has an index/manifest |
| 6. Large/resource/time budget | 4 MiB + 1 selection; 60 actual candidates with maximal title and all four maximal notes through actual CLI | Oversized file fails explicitly; all 60 allowed sources publish under the harness's 20-second timeout with unchanged PNG/prompt hashes |
| 7. Determinism/repeat | Same saved selection rendered to two fresh destinations; attempted reuse of first destination; repeated focused suite executions | Every relative output file byte matches between fresh destinations; existing output conflicts; repeated suites pass |
| 8. Misleading success/gate bypass | Inspect absence of index at interrupted publication phases; selected-but-unreviewed candidate compared then exported | No success result or completion index for partial work; export continues to require review |
| 9. Real surface/provenance/cleanup | Actual CLI init/import/compare, exact required HTTP command plus four downloads, source and download SHA checks, owned PID/temp teardown | 200 for all five requests; two distinct v1 identities and exact original/prompt bytes; all source checks OK; server and temporary directory removed |

N/A: image generation retries, paid APIs, installation and commits are outside this command/worker scope. Chrome rendering, full control interaction, file:// browser behavior and artistic quality are explicitly assigned to root-owned T4; parser/HTTP/code tests are not claimed as visual QA.

## Actual CLI/HTTP commands

The two meaningful fixture PNGs were existing native sample originals: `docs/brand/delivery/logo.png` with `docs/brand/prompt.txt`, and `docs/app-icons/images/pictogram.png` with `docs/app-icons/prompts/pictogram.txt`. No image was generated or altered for this verification. Brand brief used `Logo Land`, `LOGO LAND`, combination/opaque; icon brief used `Weather`, empty lettering, opaque and pictogram intent describing sun/cloud. Both sessions were newly initialized and imported without review.

```sh
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-compare init --session brand --brief /tmp/ll-060-compare/brand.json
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-compare import --session brand --artifact v1 --revision 0 --image docs/brand/delivery/logo.png --prompt-file docs/brand/prompt.txt
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-compare init --session icon --brief /tmp/ll-060-compare/icon.json
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-compare import --session icon --artifact v1 --revision 0 --image docs/app-icons/images/pictogram.png --prompt-file docs/app-icons/prompts/pictogram.txt
shasum -a 256 /tmp/ll-060-compare/.logo-generator/sessions/*/session.json /tmp/ll-060-compare/.logo-generator/sessions/*/artifacts/v1.png > /tmp/ll-060-compare/sources-before.sha256
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-compare compare-gallery --selection-file /tmp/ll-060-compare/selection.json --output gallery
curl -i --fail --max-time 20 http://127.0.0.1:8790/gallery/index.html > /tmp/ll-060-compare/http-index.txt
curl --fail --max-time 20 -D /tmp/ll-060-compare/image-001.headers http://127.0.0.1:8790/gallery/images/001.png -o /tmp/ll-060-compare/image-001.png
curl --fail --max-time 20 -D /tmp/ll-060-compare/image-002.headers http://127.0.0.1:8790/gallery/images/002.png -o /tmp/ll-060-compare/image-002.png
curl --fail --max-time 20 -D /tmp/ll-060-compare/prompt-001.headers http://127.0.0.1:8790/gallery/prompts/001.txt -o /tmp/ll-060-compare/prompt-001.txt
curl --fail --max-time 20 -D /tmp/ll-060-compare/prompt-002.headers http://127.0.0.1:8790/gallery/prompts/002.txt -o /tmp/ll-060-compare/prompt-002.txt
shasum -a 256 -c /tmp/ll-060-compare/sources-before.sha256
```

Owned server was launched with the current virtualenv Python as `python -m http.server 8790 --bind 127.0.0.1 --directory /tmp/ll-060-compare`, inside a `subprocess.Popen` context with `wait(timeout=300)` and timeout-triggered terminate/wait. Its real access log recorded GETs for index, both PNGs and both prompts with status 200 at `13/Sep/2026 09:21:12` local time.

## Cleanup receipt

- Server PID `38972` terminated using `kill -TERM 38972`; owning exec session `22597` subsequently returned exit 0 with all five access-log entries.
- `lsof -tiTCP:8790 -sTCP:LISTEN` returned no listener after termination.
- Temporary directory device/inode matched `(16777230, 34983239)` before deletion; only `/tmp/ll-060-compare` was removed, then nonexistence asserted.
- Output: `Cleanup PASS: owned temp inode removed; localhost8790 has no listener; PID38972 exited.`
- No retained server, browser tab or QA directory is owned by this worker. Test fixture files remain under pytest's standard retention-managed temporary root, not user workspace data.

## Final verification

- `uv run pytest -q tests/test_comparison_*.py tests/test_app_icon_gallery.py --durations=3`: **82 passed in 24.74s**. Slowest: old CLI PIN 3.55s; maximum-60-candidate CLI test 2.93s; selected-but-unreviewed export gate 1.78s. The ordinary required command without durations previously passed all 82 in 15.31s. Parallel workspace load affected elapsed time; no failed or timed-out cases were observed.
- `uv run ruff check skills/logo-land/scripts/logo_helper/comparison_*.py skills/logo-land/scripts/logo_project.py tests/test_comparison_*.py`: **All checks passed**.
- `uv run ruff format --check skills/logo-land/scripts/logo_helper/comparison_*.py skills/logo-land/scripts/logo_project.py tests/test_comparison_*.py`: **13 files already formatted**.
- `uv run basedpyright`: **0 errors, 0 warnings, 0 notes** across the shared workspace at final verification. Earlier findings were owned transient implementation errors, now resolved; no unrelated failures remain in this run.
- `git diff --exit-code 06b94c41922973fc98392fadde25fff9aa498f6e -- skills/logo-land/scripts/logo_helper/app_icon_gallery.py skills/logo-land/scripts/logo_helper/app_icon_publish.py skills/logo-land/assets/app-icon-gallery.template.html docs/brand/delivery/logo.png docs/brand/prompt.txt docs/app-icons/images/pictogram.png docs/app-icons/prompts/pictogram.txt`: **exit 0**, no diff. This establishes unchanged old renderer/publisher/template and the actual source originals/prompts used in HTTP QA.
- Pure nonblank/noncomment line counts: comparison cards 90, CLI 23, gallery 85, models 56; minimal registration file 184; test modules 24–119. No owned module exceeds 250.

Final owned implementation/automated/HTTP gates: **PASS**. The remaining integration, native gallery and Chrome/T4 work belongs to the coordinator's other tasks. No artwork-quality claim is made.
