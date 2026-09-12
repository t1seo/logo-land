# Hands-on execution QA

**PASS** for the assigned hands-on QA scope, completed 2026-09-12. Confidence is high for the exercised public CLI, persistence, delivery and relocation behavior; moderate for general conversational behavior, because tool unavailability was controlled and no new GUI agent or generation was launched. No blocking findings remain in this review. Owns this report and `/tmp/logo-review-qa.WDcBwx` only; production code and root `morrow-live` session are read-only.

## Plan and scenario brainstorm, recorded before execution

1. Completed: read full plugin skill and all four references, inspect CLI and existing real generated files.
2. Completed: execute public CLI subprocess scenarios with stdout/stderr/exit evidence in a separate workspace.
3. Completed: installed-cache and ZIP relocation passed, existing full tests passed once, reserved-output fix independently passed, rebuilt final package and new installed cache matched and passed direct CLI checks.

Initial 25 scenarios:

| ID | Priority | Scenario and expected observable behavior |
|---|---|---|
| S01 | P1 | CLI help and empty list work in an independent workspace. |
| S02 | P0 | Init complete brief at revision 0; user text preserved. |
| S03 | P1 | Duplicate init fails without replacing prior state. |
| S04 | P0 | Prompt returns text but creates no PNG or revision. |
| S05 | P0 | Import saved real A-v1; bytes/hash/prompt preserved. |
| S06 | P0 | Import separate real B-v1; distinct IDs preserved. |
| S07 | P0 | Stale revision fails with no mutation. |
| S08 | P0 | Duplicate artifact fails without overwriting bytes. |
| S09 | P0 | Unknown parent fails without an orphan image. |
| S10 | P0 | Edit prompt resolves exact selected parent path without mutation. |
| S11 | P0 | Import real saved A-v2 with actual A-v1 lineage. |
| S12 | P0 | Export without selection fails. |
| S13 | P0 | Select A-v2 then export without review fails. |
| S14 | P0 | Explicit false review is saved and blocks export. |
| S15 | P0 | Explicit inspected review unlocks real PNG export. |
| S16 | P0 | PNG bytes, ZIP members, manifest, guide all match selected artifact. |
| S17 | P0 | Fresh-process show resumes selection, parent lineage, hashes and export. |
| S18 | P0 | Existing output destination rejects overwrite; new output preserves earlier delivery. |
| S19 | P1 | Malformed/unknown-field brief rejects with no session. |
| S20 | P0 | Non-PNG, missing file, empty prompt imports reject without mutation. |
| S21 | P0 | Malformed/unsupported saved JSON fails safely in copied session only. |
| S22 | P0 | Changed/missing saved PNG blocks resume in copied session only. |
| S23 | P0 | Opaque brief with transparent artifact cannot export despite passing review fixture. |
| S24 | P0 | Explicit transparent-to-opaque background variant exports selected requirement. |
| S25 | P0 | Missing-image-tool skill dry-run preserves brief/prior assets and records simulated failure; no fake image. |

Augmented after reading boundaries (7 additional scenarios):

| ID | Priority | Scenario and expected observable behavior |
|---|---|---|
| S26 | P0 | Copy plugin runtime to another directory and run documented `uv run --project` from unrelated CWD. |
| S27 | P1 | Copy a populated workspace; fresh process uses relocated parent path and no original dependency. |
| S28 | P0 | Path traversal/absolute destination, symlink source and session ID rejected. |
| S29 | P1 | Manually staged test lock fails fast and is not removed by helper. |
| S30 | P1 | Disabled-tool edit skill dry-run preserves selected parent and records simulated failure. |
| S31 | P1 | Background default remains original brief; explicit opposite variant mismatch fails. |
| S32 | P2 | Missing/null legacy background reads with fallback and no state rewrite. |

Follow-up S33 (P1) was added after the independent code reviewer reproduced an internal export destination leaving a lock behind: verify the separately implemented reserved-output fix rejects `.logo-generator` destinations before writes, preserves state and all storage paths, and still permits similarly named ordinary output folders.

The disabled/missing tool scenarios simulate availability only. This worker will not call generation, fabricate a tool error, alter image pixels, or claim a new generated result. Saved real images are reused; negative schema/assessment fixtures are explicitly QA fixtures.

## Executed evidence

Environment: macOS, Python project configured for 3.12+, uv 0.9.16. The normal subprocess prefix was:

```sh
uv run --no-sync --project <workspace> \
  python <workspace>/skills/logo-generator/scripts/logo_project.py \
  --workspace /tmp/logo-review-qa.WDcBwx/workspace
```

`run-main.sh`, `run-boundaries.sh`, and `run-installed.sh` in the temporary evidence directory invoked public commands as separate processes. Each invocation has `logs/<ID>.command` with shell-escaped complete arguments, `logs/<ID>.stdout`, `logs/<ID>.stderr`, and an expected/actual exit row in `exits.tsv`. These are real CLI runs, not Typer CliRunner calls or mocked helper calls. Every fresh `show` and `prompt` is a new interpreter process.

| Scenario | Expected exit | Actual exit | Observed evidence |
|---|---|---|---|
| S01 | 0/0 | 0/0 | Help lists commands; new workspace `list` returns `[]`. |
| S02 | 0 | 0 | `main` revision 0, exact `Morrow Studio`, concept count 2, no artifacts. |
| S03 | 1 | 1 | Duplicate init returns JSON `File exists`; `cmp` confirms original state unchanged. |
| S04 | 0 | 0 | `mode=generation`, parent null, revision 0; state bytes unchanged. |
| S05 | 0 | 0 | Saved real A-v1 imported at revision 1; direct `cmp` with supplied PNG passes. |
| S06 | 0 | 0 | B-v1 imported at revision 2; a-v1 and b-v1 retain distinct IDs and hashes. |
| S07 | 1 | 1 | `stale_revision: Expected revision 1; current revision is 2`; state unchanged. |
| S08 | 1 | 1 | `conflict: Artifact a-v1 already exists`; state unchanged. |
| S09 | 1 | 1 | `not_found` for nonexistent parent; no orphan PNG exists. |
| S10 | 0 | 0 | `mode=edit`, parent a-v1, exact verified workspace a-v1 path; state unchanged. |
| S11 | 0 | 0 | Saved real A-v2 imported at revision 3 with `parent_id=a-v1`; prior A/B remain. |
| S12 | 1 | 1 | `not_selected`; no package produced. |
| S13 | 0/1 | 0/1 | Selection advances to revision 4; unreviewed export returns `review_required`. |
| S14 | 0/1 | 0/1 | Explicit QA false `small_size_ok` is saved at revision 5; export remains blocked and state bytes stay unchanged. |
| S15 | 0/0 | 0/0 | Review based on reopened real A-v1/A-v2 and saved size-comparison screenshot advances to revision 6; export succeeds at revision 7. |
| S16 | 0/0/0 | 0/0/0 | Delivered PNG matches A-v2; `unzip -t` passes all 3 members; manifest identifies a-v2, a-v1 parent, raster, 1254 pixels, opaque request and no transparency. |
| S17 | 0 | 0 | Fresh `show` returns revision 7, a-v2 selected, original lineage and export; hashes revalidated. |
| S18 | 1/0 | 1/0 | Existing output returns `conflict` with state unchanged; new `delivery-v2` succeeds at revision 8 and PNG matches earlier delivery. |
| S19 | 1/1 | 1/1 | Incomplete JSON returns `json_invalid`; unknown brief field returns `extra_forbidden`. |
| S20 | 1/1/1 | 1/1/1 | JPEG renamed PNG rejected as `invalid_png`; absent input rejected as `invalid_file`; empty prompt rejected as `string_too_short`; state unchanged. |
| S21 | 1/1 | 1/1 | A copied session with invalid JSON and then schema 99 rejects with validation errors. |
| S22 | 1/1 | 1/1 | Appending bytes to copied saved PNG causes `hash_mismatch`; moving it away causes `invalid_file`. |
| S23 | 0/0/1 | 0/0/1 | Real transparent A-v1 with original opaque request and labeled all-true QA review fixture fails `background_mismatch`; state and destination preserved. |
| S24 | 0 throughout | 0 throughout | Transparent-intent replay imports real A-v1 then real opaque A-v2 with actual a-v1 parent and `--background opaque`; export uses opaque override despite initial transparent brief. Edit prompt reports parent background opaque. Later selecting transparent A-v1 exports actual transparency, with byte-identical PNG. |
| S25 | 0 throughout | 0 throughout | Missing-tool dry-run and actual independent installed-skill exercise save brief/prompts/failure only; exact Hangul and count 2 survive; zero artifacts and exports. See transcript below. |
| S26 | 0 throughout | 0 throughout | Copied runtime, actual installed cache, and extracted release ZIP each run via documented `uv run --project` from unrelated CWD; no `.logo-generator` data in plugin folders. |
| S27 | 0 throughout | 0 throughout | Relocated workspace resumes; edit prompt resolves parent beneath `/private/tmp/logo-review-qa.WDcBwx/relocated workspace/`, not the original workspace. |
| S28 | 1/1/1/1 | 1/1/1/1 | Traversal and absolute export return `unsafe_path`; symlink input returns `invalid_file`; traversal session ID fails schema; original state unchanged. |
| S29 | 1 | 1 | Test-owned existing lock returns `locked`, remains present, and state stays unchanged; QA removes only the lock it created. |
| S30 | 0 throughout | 0 throughout | Disabled edit dry-run and installed-skill execution resolve real a-v2, save simulated failed attempts, preserve 3 images, a-v2 selection, 2 delivered packages and PNG bytes. |
| S31 | 1/2 for rejection; 0 for default probe | 1/2; 0 | Opaque A-v2 with omitted override under transparent brief cannot export (`background_mismatch`); `--background checkerboard` is a Typer usage error, exit 2. Explicitly labeled metadata-only reuse also confirms that an opaque-overridden parent defaults to the original transparent brief when override is omitted. |
| S32 | 0 throughout | 0 throughout | Copied legacy state with missing and then null backgrounds resumes; prompt fallback is opaque; both states remain byte-identical after reads. |
| S33 | 1/1 for reserved paths; 0 for ordinary export/checks | 1/1; 0 | Both `.logo-generator/locks/main.lock/package` and `.LOGO-GENERATOR/sessions/new` return `reserved_output`; state and full managed path list remain identical and no lock remains. `.logo-generator-backup/final` export succeeds, preserves PNG bytes, and fresh resume reaches revision 14. |

After final package verification, **149 command/assertion invocations** had matching expected and actual exits. Command groups include checks as well as CLI actions; this number is not presented as 149 independent scenarios. The scenario count is **33** (25 initial, 7 boundary additions, 1 independently reported fix recheck).

## Independent installed-skill execution: controlled tool unavailability

The independent QA worker read the entire installed `skills/logo-generator/SKILL.md` at the actual personal cache supplied by the coordinator:

```text
<codex-home>/plugins/cache/personal/logo-generator/0.2.0
```

Controlled condition: this host really exposes `image_gen__imagegen`, but the QA scenario deliberately excludes permission to invoke it. No host setting was changed and no real outage or error response is alleged. The skill logic was executed by this separate worker, using installed files and actual subprocesses. This is more than recording a fixture failure, but it does not establish behavior of a different fresh GUI agent or a real unavailable server.

S25 input, complete Korean request written to `inputs/korean-request.txt` before execution:

> 고요 스튜디오는 동네 소상공인을 위한 친환경 포장 디자인 회사입니다. 로고 글자는 정확히 '고요 스튜디오'로 해 주세요. 30~40대 독립 매장 운영자가 대상이고 차분하고 간결한 심볼과 한글 조합형으로 부탁드립니다. 짙은 초록 #174C3C와 흰색 불투명 배경을 쓰고, 웹사이트와 명함용 시안 두 개를 만들어 주세요. 슬로건이나 추가 문구는 넣지 말아 주세요.

Skill decisions executed: extract supplied fields without another questionnaire; preserve exact text and count; resolve helper relative to installed skill; save in separate user workspace; build separate geometric and organic prompts; stop at the known tool boundary; record a clearly labeled controlled failure, with no import, fake PNG, paid API, or network image fallback. Public commands S25e–S25m all returned exit 0. Final `goyo` state: revision 1, 0 artifacts, 1 explicitly simulated failure, 0 exports. `test ! -e` confirmed both artifacts and output directories absent. Prompt commands remain revision 0 until the failure record is written.

Exact scenario response produced after execution:

> 현재 이 실행에서는 이미지 생성 도구를 사용할 수 없어 로고 이미지를 만들지는 못했습니다. ‘고요 스튜디오’의 정확한 표기와 요청하신 색상·배경·시안 수를 저장하고, 기하학 심볼과 잎 모티프 두 방향의 프롬프트를 준비했습니다. 저장 위치는 `/tmp/logo-review-qa.WDcBwx/installed-skill-workspace`이며, 이미지 도구를 사용할 수 있는 실행에서 `goyo` 작업을 이어가실 수 있습니다.

S30 input for existing project:

> main 작업의 a-v2를 이어서 수정해 주세요. 글자와 배치는 유지하고 잉크만 검정으로 바꿔 주세요.

Skill decisions executed: installed helper `show` verifies the existing session; installed `prompt --parent a-v2 --changes ...` resolves exact a-v2; the previously reopened a-v2 is the edit target; no tool invocation under controlled disabled availability; `failure --parent a-v2` records that limitation. Installed commands S30d–S30h all returned exit 0. Final state: revision 13, selected a-v2, 3 unchanged artifacts, 2 prior exports, 2 labeled simulated failures (one original local dry-run and one installed-skill run). Byte comparison with saved real A-v2 passes.

Exact scenario response produced after execution:

> 저장된 a-v2와 원본 파일을 확인했습니다. 현재 이 실행에서는 이미지 편집 도구를 사용할 수 없어 검정색 수정본은 만들지 못했습니다. 기존 a-v2와 두 전달 패키지는 그대로 보존했고, 요청하신 수정 내용과 진행하지 못한 이유를 main 작업에 기록했습니다.

These two responses are recorded QA transcript outputs, not messages sent to an external user/account and not claims of generation. No credentials or APIs were used.

## Actual host-call provenance audit

The coordinator authorized a narrow read of the root rollout for only three image-generation call/result pairs. This worker inspected the matching `custom_tool_call` and `custom_tool_call_output` records and extracted only those pairs into temporary evidence. No unrelated authentication records were included in this report.

| Saved artifact | Actual tool input | Call ID | Returned image filename | Returned PNG SHA-256 |
|---|---|---|---|---|
| a-v1 | `image_gen__imagegen({prompt})`; reads saved a-v1 prompt; both reference mechanisms omitted | `call_FhUV7kJPMeunOrnBmw6F5zEq` | `exec-51782ab7-41d1-4d88-afcd-c9c14224731f.png` | `55a790a078cff75fdc201da383b8006c42107fc7372d4fa6b7d6cc5e14bfe851` |
| b-v1 | `image_gen__imagegen({prompt:p.output})`; reads saved b-v1 prompt; both references omitted | `call_pnhKpfLtek1acXvw2gO2j4do` | `exec-925811fa-0102-45e5-87e2-b7c02713b567.png` | `aab27b586f7b1de90601fc73d97b03f232f46b1a81ca83ec6466c638fba472cf` |
| a-v2 | `image_gen__imagegen({prompt:p.output, referenced_image_paths:[<repo>/docs/qa/live/images/a-v1.png]})` | `call_ZsTAhCjElCYtGX6mnUqg0Z89` | `exec-75fbfe64-e021-4174-8b4c-24e7cff9c8bc.png` | `666eb20feaf67ee3bc4a1c879f5c551a55998bf2b257d5e52c0b142e599ab519` |

The hashes above were independently calculated by base64-decoding the actual returned `input_image.image_url` in those results directly into `shasum -a 256`. They match saved QA files, imported workspace files and (for a-v2) delivered PNG. Thus these are the exact returned native images, and A-v2 has an actual parent-image tool reference, not only a claimed JSON lineage.

The currently exposed tool schema accepts `prompt`, `referenced_image_paths`, and `num_last_images_to_include`. All three recorded calls match that schema; none injects API-only model, size, quality, output, or background arguments. Two separate concept calls and one real referenced edit agree with `native-image.md` and the saved live log. Tool availability during this worker's controlled dry-runs is clearly distinguished from these historical actual calls.

## Visual and file delivery inspection

Opened actual saved A-v1, A-v2 and the coordinator's saved Chrome size-comparison JPEG through the local image viewer. This worker did not control a browser. Exact `Morrow Studio` lettering, large margins and the M structure are visible. The saved comparison shows identifiable mark and legible wordmark near 256 CSS pixels; the whole lockup at 48 pixels has the documented small-text limitation. A-v2 has slight texture/tonal variation and interior curve changes, so exact flat HEX, pixel preservation and editable vector claims are not supported. This is consistent with the qualified fictional demonstration review, not certification that every requested pixel constraint succeeded.

The gate-negative all-true reviews used only in S23/S31 are explicitly named `QA gate-isolation fixture`. They isolate automatic background checking and do not stand in for visual approval. Background replay sessions reuse real PNGs under controlled QA intent; they do not represent new generations or a user changing their order.

The final a-v2 PNG is 1254×1254 with no transparent pixels. `unzip -t` passes; extracting each ZIP member and comparing against the adjacent PNG, manifest and guide yields identical bytes. Source PNG, extracted PNG and delivered PNG all hash to `666eb20feaf67ee3bc4a1c879f5c551a55998bf2b257d5e52c0b142e599ab519`. The guide separates historical green palette from the actual selected navy-edit prompt and explicitly labels raster/vector/font/CMYK/legal boundaries.

## Tests, source preservation and limits

`uv run --no-sync pytest -q` ran once in this worker and returned exit 0: **84 passed in 58.48s**. After the separate reserved-output fix, the specifically affected new regression file was run once: `uv run --no-sync pytest tests/test_reserved_output.py -q`, exit 0, **12 passed in 8.02s**. Raw stdout/stderr/exit are under the temporary evidence directory. No production Python was edited and no full-suite loops were run. The full-suite result is the pre-fix checkpoint; the 12-case focused result and S33 public CLI execution cover the later change.

All root `morrow-live` files retained their starting SHA-256 values; `cmp root-before.sha256 root-after.sha256` returned exit 0. Root session revision remains 7; session JSON SHA-256 is `43a38d8e69378d40ed2ef4a9b471cda137dbd34821f1d2667f9c1e65523e901d`. Root PNG hashes match the provenance table. All malformed, deleted, modified, symlink and lock cases occurred in this worker's temporary folders only.

Boundaries: no new image generation, real missing-server failure, desktop browser manipulation, paid export, trademark/vector/font certification, Windows/Linux runtime, offline-first dependency install, or automatic discovery in a new Codex GUI thread was exercised. Installed helper and extracted package execution passed; install itself belongs to the coordinator's installation record. CLI usage errors use Typer stderr/exit 2 rather than the helper's JSON error envelope. Normal data/filesystem errors exercised here use JSON stderr/exit 1.

## Final rebuilt package and installation verification

The coordinator rebuilt and reinstalled after the reserved-output correction. The final manifest version is `0.2.0+codex.20260912125753`; actual installed cache is the same personal cache parent shown above, with that version directory replacing `0.2.0`. Earlier installed-skill transcripts intentionally retain the version actually used then; their persisted workspace was resumed successfully by the final installed version.

`dist/logo-generator-0.2.0.zip` SHA-256: `1ccf995e106217dc76c28f4247d162da27569de6f55d4a63fe3069a6df949775`.

Final commands F01–F20, recorded by `run-final-package.sh`, all matched expected exits. Extraction into a new temporary directory succeeded; recursive comparison excluding interpreter caches found the entire skills tree identical across source, extracted package and installed cache. Plugin manifests matched byte-for-byte, as did the checked project/lock files. The source, extracted and installed `delivery.py` all hash to `4037d445e4dfc2d8e2ce661a82bc92b446755d817b86346a105a5b48791d2326`.

From unrelated CWD using documented `uv run --project`, the final installed helper resumed both the Korean no-image `goyo` session and the existing real-image `main` session. An installed reserved-path export returned exit 1 and `reserved_output` without state change or lock residue. The newly extracted final ZIP then exported `main` to fresh `final-package-smoke`, returning exit 0; PNG byte comparison and `unzip -t` passed. Another fresh installed process resumed revision 15, selected a-v2, 3 original images and 4 preserved delivery directories. Both plugin locations remain free of `.logo-generator` session data. Root `morrow-live` remained revision 7, selected a-v2, with all four starting file hashes unchanged.

Only this report is authored in the repository. Temporary command logs, transcripts, copied inputs and isolated workspaces are retained at `/tmp/logo-review-qa.WDcBwx` for coordinator inspection; no instrumentation or root-session changes were introduced. Full base64 tool outputs were discarded after independent hash verification, retaining only the three relevant sanitized call records and inputs. The separately discovered reserved-output issue is fixed and independently verified; no further work remains in this dispatch.
