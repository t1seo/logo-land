# T6 conversational color and lockup evidence

Date: 2026-09-13 (Asia/Seoul). Owner: T6 skill/docs worker.

Scope: skill instructions and references only. This record separates manual instruction walkthroughs, executable helper evidence, and native image QA. No native image call, live Leonardo call, font installation, or visual approval is claimed here; T8 owns native-image evidence.

## Baseline before editing

Base inspected: `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`.

```text
uv run --locked pytest tests/test_cli_workflow.py tests/test_background_variants.py tests/test_resume_and_portability.py
27 passed in 29.20s

uv run --with pyyaml '$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py' skills/logo-land
Skill is valid!
```

## Red: behavior gaps reproduced by reading the original skill

These are manual decision tests against the original instructions, not failed automated tests or generated conversations. Existing `combination` support, native-only edits, exact Hangul checks, and no redundant generation approval were already present and are preserved.

| Given / when | Required observable decision | Original result |
|---|---|---|
| Photo + keep `#247A52` + at most two colors + choose for me | One composed constraint set, explicit reference source, assistant selection, then authorized generation | No structured constraint/source routing or recorded selection guidance: red. |
| Leonardo is unavailable | Local suggestion with an honest unavailable record | No optional-provider fallback/evidence procedure: red. |
| Locked green lies outside the allowed black/ivory set | Stop before native calls with a conflict | No conflict check: red. |
| A navy child of a green logo receives a geometry-only edit while active palette is green | Preserve the navy parent palette and its structured lockup | Parent-image preservation existed; palette/lockup version precedence was unspecified: red. |
| Exact `달빛 빵집` and `오늘도, 따뜻하게!` with horizontal → stacked variant | Preserve both strings; change only requested layout; keep typeface appearance distinct from a font-file claim | Exact text guidance existed; structured layout/typography handoff was unspecified: red. |
| Initial strict mismatch plus two unsuccessful native repairs | Retain all candidates, report unresolved, do not promise compliant export | No bounded color-repair/export policy: red. |

No wording-matching tests were added for documentation. The green walkthroughs below inspect decisions; executable parser/CLI checks are recorded separately when available.

## Green: manual instruction walkthroughs

Each scenario was walked through against the updated skill and its routed references. Transcript lines below are authored examples of the required response, not messages from a live end user or an independently executed model. Fixture observations are declared inputs, not measurements made in this task.

### combinedconstraints: reference + exact anchor + count + delegated selection

Given a complete brief for a transparent combination mark, one requested concept, and a scenario reference extraction containing sand `#EADFC5` among its candidates. That extraction value is a fixture input, not a claimed photo measurement.

User: “Use this photo, keep #247A52, at most two colors, choose for me.”

Decision trace: use the supplied reference for extraction, not as the edit parent; compose `locked_hex=["#247A52"]`, `allowed_hex=null`, `max_colors=2`, `required_hex=[]`, `allow_gradients=false`; select green for symbol/lettering and the fixture's sand for one visible accent; record `source=reference`, the actual extraction evidence when executed, `selected_by=assistant`, and rationale. Shared green roles do not introduce duplicate swatches. The transparent exterior is excluded from the count.

Assistant example: “기준 녹색 #247A52는 유지하고, 사진에서 추출한 후보 중 모래색을 작은 포인트로 선택하겠습니다. 두 색으로 한 가지 조합형 로고를 만들겠습니다.” This statement is appropriate only after real extraction returns the stated color; otherwise the assistant must say extraction is unavailable and avoid the claim.

Then build one palette-bound prompt and proceed to the already-authorized native call, with no extra palette approval and no palette×concept multiplication. Outcome: manual decision check passes; actual extraction/generation is reserved for integrated QA.

### absentMCP: unavailable optional Leonardo

Given no Leonardo tools exposed and an automatic warm-color brief with choice delegated.

Decision trace: record unavailable provider status; use assistant or local-harmony source truthfully; keep palette constraints; choose one candidate and proceed if generation is authorized. No `npx`, MCP configuration write, account connection or fake external call occurs.

Assistant example: “이 환경에는 Leonardo 도구가 연결되어 있지 않아, 여기서 제안한 테라코타·짙은 갈색·크림 조합으로 진행하겠습니다.” If the local engine also fails, explain the calculation gap instead of claiming a local measured result.

Outcome: passes by instruction walkthrough; no live Leonardo evidence claimed.

### conflictingconstraints: locked color outside allowed set

Given `locked_hex=["#247A52"]`, `allowed_hex=["#000000","#F4EBDD"]`, `max_colors=2`.

When the candidate is prepared, stop with a constraint conflict before any native call. Assistant example: “고정하신 녹색이 허용된 검정·아이보리 목록에 없습니다. 녹색을 허용 색에 포함할지, 녹색 고정을 해제할지 정해 주시겠습니까?” The response does not silently choose either change.

Outcome: manual decision check passes. Also reject three distinct locked colors under a two-color cap and reject gradients plus a count/allowed-set restriction.

### inheritedpalette and inheritedlockup: parent wins over active/brief intent

Given a green horizontal `a-v1`, a navy stacked `a-v2` descended from it, and active green for future generations. Both artifacts have their own palette/lockup intent. Exact text is `달빛 빵집`; slogan is `오늘도, 따뜻하게!`.

User: “두 번째 로고의 심볼과 글자 간격만 조금 넓혀 주세요.”

Decision trace: resolve the displayed second choice to `a-v2`; inspect/use that exact image; create `a-v3` with parent `a-v2`, inherited navy and stacked layout/typography, unchanged source strings, and a spacing-only edit. Do not reset to green or horizontal. Explicitly retain a transparent import override if applicable; background omission has its own legacy behavior. Reselecting `a-v1` resolves green/horizontal, not the newest palette or lockup.

Outcome: passes by instruction walkthrough; no raster preservation claim is made.

### exactHangul: horizontal → stacked, preserving brand and slogan

Given `logo_type=combination`, `exact_text="달빛 빵집"`, `slogan="오늘도, 따뜻하게!"`, horizontal/start/start lockup and rounded sans-serif appearance.

User: “심볼을 글자 위로 옮겨 주세요. 글자와 색은 그대로요.”

Decision trace: derive a stacked/start layout from the selected parent; retain the text block's requested alignment unless the user changes it; preserve appearance, palette, both source strings and background. Use separate artifact ID/final prompt. The exact brand space, slogan comma and exclamation mark remain in the prompt. Do not substitute `달빛빵집`, `Moonlight Bakery` or pseudo-Hangul.

Assistant example: “심볼을 글자 위로 옮기고, ‘달빛 빵집’과 ‘오늘도, 따뜻하게!’의 문구·글자 모양·색상은 유지하겠습니다.” After generation, compare both strings visually; plausible-looking or incorrect lettering cannot pass exact-text review.

Outcome: instruction-level preservation passes; visual Hangul verification belongs to T8.

### logotypedistinction: wordmark, combination and icon-only

Given “Create a wordmark reading 달빛 빵집,” do not add a moon icon. Given “달 심볼과 달빛 빵집 이름이 함께 있는 로고,” keep `combination` with both symbol and exact name. Given an explicitly requested icon-only derivative, omit lettering deliberately and retain true variant provenance; do not present it as fulfilling the original required-text combination deliverable.

Outcome: passes; existing combination support is enhanced, not represented as entirely new.

### invalidprovider: reject a near anchor and extra color

Given an external candidate with `#257A52` instead of locked `#247A52`, or three distinct colors under `max_colors=2`.

Decision trace: normalize through the local candidate boundary, reject the lock-breaking/count-breaking suggestion with its reason, record the real provider response separately, and choose a valid local/assistant fallback with its true source. `#247A5280`, CSS color functions and `passed=true` are not valid substitutes for palette input or local measurement.

Outcome: manual decision check passes; T2's actual invalid-provider fixtures are the executable source of truth.

### repairlimit: two unsuccessful edits preserve the failed candidates

Given initial strict mismatch `a-v1`, then mismatched repairs `a-v2` and `a-v3` for the same user request.

Decision trace: exactly two additional native repair attempts are permitted. Keep all three originals/prompts/reports, stop further automatic repairs, and explain unresolved fidelity. A visual review cannot bypass strict export, and an advisory palette must not replace the strict intent silently.

Assistant example: “두 차례 보정 후에도 지정 색상 조건을 충족하지 못했습니다. 세 후보와 검증 기록을 보존했으며, 조건을 충족한 최종본으로 내보내지는 않겠습니다.”

Outcome: passes by instruction walkthrough; these are hypothetical failures, not actual native attempts in this task.

### countscope and uncertainty: white is visible artwork

Given transparent white lettering, preserve visible white in palette/count/measurement and exclude only the transparent exterior. Given an opaque ivory background under max two, reserve a color slot for ivory and do not add unrequested white. Given unsupported ICC or insufficient core samples, report indeterminate evidence and no strict pass; an ROI narrows the claim and is not automatic segmentation.

Outcome: passes. A color histogram never proves that green belongs to the symbol or that Hangul is correct; those remain visual checks.

### comparefirst and fontclaim: respect the requested stage

Given “Show three color choices first,” present three palette choices without invoking image generation. Given a named-font appearance request, record a visual reference and describe the desired letterforms; never claim a font binary was used or licensed by inspecting raster appearance. No font download, separate typesetting engine or automatic font-service setup is authorized by these requests.

Outcome: passes.

## Attribution and scope checklist

- Adobe Leonardo skill/MCP documentation and Apache-2.0 license were read at pinned commit `eb6481da40df27654ac8efa42038007f6fad2431`; the MCP README was fetched from its raw pinned URL after the browser fetch timed out.
- Color Expert original skill/README and CC BY 4.0 license were read at `6514810aaab15cdd0e4202af52a6afed27ed314d`. The README credits compiler `@meodai` and distinguishes separately authored reference content.
- `THIRD_PARTY_NOTICES.md` links authors, primary pinned sources, license copies and the exact adaptation scope. The six HEX directions are original examples, not copied collections.
- No upstream reference collections, font binaries, MCP configuration, Python image edits, READMEs, manifests or git/release operations were added by T6.
- W3C's primary contrast explanation was checked for the logo/brand-name-text exception; the guide still asks for visual readability checks and avoids certification claims.
- Incorporated the font worker's `docs/research/font-tools.md`, including Korean/Latin family distinctions, Gowun Dodum's single weight, and the corrected Black Han Sans script conflict. No independent broad font search was performed. The typography guide links the report's primary pinned license/script evidence and treats every name as an appearance reference.

## Executed parser and CLI checks

T1's published `docs/qa/color-workflow/contracts.md` was read along with the actual `ColorConstraints`, `PaletteContent`, `SourceEvidence` and `LockupIntent` models. The two JSON blocks were extracted directly from the new references and passed to their respective Pydantic `model_validate_json` boundaries in a one-shot `PYTHONPATH=skills/logo-land/scripts uv run --locked python` invocation. Its output was:

```text
combinedconstraints: accepted by ColorConstraints; strict=true
lockup: accepted by LockupIntent; visual font reference null
conflictingconstraints: constraint_conflict
```

All six palette table rows were parsed into typed `Swatch`/`PaletteContent` values, rather than tested by matching document wording. Output:

```text
Warm bakery: accepted; 3 distinct colors
Quiet technology: accepted; 3 distinct colors
Botanical: accepted; 3 distinct colors
Playful studio: accepted; 3 distinct colors
Editorial craft: accepted; 3 distinct colors
Black and ivory: accepted; 2 distinct colors
All six illustrative palette directions accepted by PaletteContent
```

`uv run --locked pytest tests/test_color_models.py` reported **30 passed in 0.11s**. These are the state worker's tests executed read-only, not newly authored T6 tests.

T2's actual `PaletteRequest` / `propose_palettes` / `validate_candidate` implementation and invalid-provider fixtures were then reviewed. `uv run --locked pytest tests/test_palette_engine.py` reported **29 passed in 0.13s**, covering missing/ambiguous sources, invalid HEX, normalized duplicates, broken locks/counts, combined reference/lock/count requests and missing calculation engine. No T2 files were edited.

Actual CLI smoke: `uv run --locked python skills/logo-land/scripts/logo_project.py --help` returned exit 0. A `TemporaryDirectory` workspace then ran the real Python CLI as subprocesses with argv lists:

```text
init --session t6-hangul --brief <temporary-workspace>/brief.json
prompt --session t6-hangul --concept "Moon symbol left of the exact Korean name; rounded sans-serif appearance"

init: exit=0; temporary session=t6-hangul
prompt: exit=0; mode=generation; revision=0; read-only=true
preserved exact_text: 달빛 빵집
preserved slogan: 오늘도, 따뜻하게!
temporary workspace removed; no image call, image edit or font installation
```

The brief used `logo_type=combination`, transparent background and one concept. `PromptResult.model_validate_json` accepted the result, both literal strings were present, and the saved session bytes were unchanged by `prompt`. This verifies CLI text preservation, not rendered Hangul or the new structured inheritance behavior; T4's contract/integration checks cover the latter.

The exposed tool inventory was searched for Leonardo by tool name/description and returned no matches. No Leonardo call was made or invented.

An actual `PaletteRequest` with locked `#247A52`, `max_colors=2` and a source-evidence note about the absent tool was then sent to `propose_palettes`. It returned these local candidates:

| Recipe | Returned colors | Source / selection |
|---|---|---|
| Monochromatic | `#247A52`, `#02140A` | `local_harmony` / `assistant` |
| Analogous | `#247A52`, `#56742E` | `local_harmony` / `assistant` |
| Complementary | `#247A52`, `#8E4F7C` | `local_harmony` / `assistant` |

Every returned candidate retained the exact anchor and two-color limit, and provider/tool/response fields remained null. This is actual local fallback evidence, not a Leonardo or image-generation claim.

The T4 owner supplied the document CLI contract in message `msg_deaf6a03ba13`: `reference-add`, `palette-propose`, `palette-add`, `color-analyze`, `color-gallery`, `--palette` and `--lockup-file` on prompt/import, with import revision matching the prompt response. Only after receipt were the short combined-mode CLI examples added. Request/source binding and candidate-versus-envelope handling were checked against that contract and T2's typed request model. The new command examples have not been executed by T6; T4/T8 own their integrated runtime checks and any final signature adjustment. The CLI evidence above exercises the existing init/prompt surface only.

## Documentation validation and cleanup

After the guidance changes, the same installed skill-creator `quick_validate.py` returned `Skill is valid!`. The final relative-link/encoding/whitespace check resolved **20 local reference links across all seven owned Markdown documents**, with valid UTF-8 and no trailing whitespace. `git diff --check` also passed for the tracked skill/direction changes. The skill entry remained 64 lines, with detailed mode guidance routed to references.

Only the seven T6-owned Markdown files were edited. No Python source, tests, manifests or README files were changed; Python-specific Ruff/basedpyright/LSP and module-size gates are not applicable to this documentation diff. The subprocess workspace was removed through `TemporaryDirectory`; no scripts, font binaries, image files, servers or helper sessions remain from T6. Shared dependency caches and other workers' changes were left intact.

Adversarial classes covered here: conflicting/combined constraints, unavailable or invalid optional providers, version/selection confusion, exact Unicode and punctuation, logo-type mislabeling, unsupported font/glyph claims, alpha/white/count scope, uncertain measurements, unbounded repair loops, and external attribution/license confusion. Native image quality and actual export conformance are explicitly outside this worker's evidence.
