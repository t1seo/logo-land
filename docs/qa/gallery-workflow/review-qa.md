# T5 independent hands-on QA

판정: **PASS**. 미해결 제품 결함은 발견되지 않았습니다. 실제 CLI와 HTTP 검증을 직접 수행했으며, 전체 Python 테스트와 Chrome 동작은 현재 소스에 연결된 기존 증거를 명시적으로 재사용했습니다. Task `task_93f5096417e5`, dispatch `ctx_f72e51fb7048`.
Scope: read-only review against `06b94c41922973fc98392fadde25fff9aa498f6e` on `feat/logo-land-gallery-workflow`, including untracked feature files. Own only this report and `review-qa.json`. This is the QA perspective of the coordinator's five independent reviews; no nested review team, source edits, installations, image calls, browser launch, commit or branch change.

## Execution ledger

1. Complete: read T1–T5 and evidence, record scenarios, pin current source/input hashes.
2. Complete: restore portable snapshots and execute independent actual CLI scenarios.
3. Complete: serve actual CLI output, download originals/prompts, inspect existing Chrome evidence.
4. Complete: approved late release-guide correction rechecked, evidence retained, owned resources removed and final verdict recorded.

## Resource registration before creation

Exclusive temporary root `/tmp/ll-060-review-qa/` must be absent before creation; record device/inode. Registered contents: `qa.rb`, `http.rb`, `finish.rb`, `cleanup.rb`, `workspace/` (restored sessions and selection JSON), `legacy/` (isolated legacy-null fixture), `gallery/`, refusal/hostile output directories, `downloads/`, `logs/`, and JSON inventories/receipts. No file outside this root may be used as a disposable fixture. Every subprocess argv/PID/status and script hash is captured in the retained JSON; no tmux or extra Orca terminal/session is created.

Server: `127.0.0.1:8798`, directory `/tmp/ll-060-review-qa`, max lifetime 120 seconds under owned Ruby supervisor; check port is free first, record exact Python server argv/PID, terminate/reap and recheck absence. Exact required surface: `curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8798/gallery/index.html`. CLI commands bounded to 30 seconds; focused Node regression bounded to 30 seconds. Remove only owned inventoried files after retaining hashes/results, then empty directories; verify all registered subprocesses, temp root and port absent. Existing Chrome remains untouched.

## Scenarios recorded before app execution

Each row is an execution task: steps → expected result. New execution and reused evidence will be distinguished in final results. P0 first, then P1/P2.

| ID | Priority | Steps → expected result |
|---|---|---|
| Q01 | P0 | Hash current 73 source, 41 tests, 183 public files against final bindings → exact maps and aggregates match. |
| Q02 | P0 | Compare T3 maps with final maps and supplements → exactly one changed source, one added Node test and three changed public files; unrelated hashes equal. |
| Q03 | P0 | Run actual helper `--help` → exit 0 with compare-gallery and existing commands. |
| Q04 | P0 | Restore six snapshot `state` wrappers and run real `show` → correct revisions, eight artifact identities and original prompt bytes. |
| Q05 | P0 | Build mixed COMMON/v1 + Leaflet/v1 using current revisions → two distinct portable identities and original downloads. |
| Q06 | P0 | Compare all eight saved candidates with final selection → parents/revisions match, no approval or selection writes. |
| Q07 | P0 | Request gallery twice at existing output → refusal and existing output unchanged. |
| Q08 | P0 | Duplicate same session/artifact in selection → exit nonzero, no published directory. |
| Q09 | P0 | Select Relay revision 1 against revision 2 → stale refusal with current revision, no output. |
| Q10 | P0 | Supply malformed JSON, negative revision and wrong revision type → explicit errors, no output/state change. |
| Q11 | P0 | Supply absent artifact/session → clear refusal and no misleading success. |
| Q12 | P0 | Put closing textarea/script/img-event and shell-like strings in notes → inert escaped text, single authored script, no sentinel. |
| Q13 | P0 | Attempt export before selection and after isolated selection without review → export gate refuses, no package. |
| Q14 | P0 | Restore a legacy parent with null lockup, later set brief default, build child prompt → unknown parent layout remains unknown. |
| Q15 | P0 | Use exact required HTTP command against independently built gallery → HTTP 200, exact index hash and source identities. |
| Q16 | P0 | Download linked brand/icon originals and prompts → four HTTP 200 responses, exact PNG/prompt hashes. |
| Q17 | P0 | Rehash source, inputs, approvals and foreign worktree files → no unauthorized changes. |
| Q18 | P1 | Inspect rendered card/filter markup and source JSON → kind/style filters, stable IDs and precise resume identifiers. |
| Q19 | P1 | Run six actual-template Node lifecycle regressions → restored kind/style/context, reset and counts agree. |
| Q20 | P1 | Inspect existing T4 final Back/reload/child-context screenshots and bound hashes → resolved behavior matches current template/index. |
| Q21 | P1 | Inspect final README desktop/narrow screenshots and current HTML groups → six originals remain in 3+3 groups, links valid. |
| Q22 | P1 | Independently resume all snapshots via repeat show/read → original and exact prompt bytes unchanged. |
| Q23 | P1 | Reuse hash-bound interruption/publication regressions → twice-cancel then retry, rollback and foreign-inode protection covered. |
| Q24 | P1 | Inspect installation follow-up source/cache map and helper evidence → refreshed template/source matches current 0.6.0 payload. |
| Q25 | P2 | Inspect UI/metadata and retained observations → candidates unapproved, previews illustrative, source unreleased, attribution and historical failures preserved. |

Reflection additions (recorded before execution):

| ID | Priority | Steps → expected result |
|---|---|---|
| R01 | P0 | Precreate foreign sentinel inside output destination → helper refuses and sentinel bytes preserved. |
| R02 | P1 | Wrong/unknown extra selection keys and parent identities → strict rejection instead of silent interpretation. |
| R03 | P1 | Repeat bounded HTTP reads and cancel partial transfer → later complete reads preserve source/gallery bytes. |
| R04 | P1 | Compare every public original/prompt with snapshots and sample manifest → all eight unchanged, child-parent relation retained. |
| R05 | P0 | Inventory and clean every owned script/file/PID/port → only reports remain; no owned server or fixture retained. |

위 25개 시나리오와 5개 추가 시나리오는 앱 실행 전에 기록했습니다. 당시 문서 해시는 JSON의 `scenario_plan_sha256`에 있습니다. Native-call cancellation/paid retries are outside this read-only review and use directly source-bound prior evidence where applicable.

## 실행 결과

30개 시나리오: **P0 19/19, P1 10/10, P2 1/1 PASS**. 아래 `실행`은 이번 검토의 직접 관찰, `재사용`은 출처와 해시를 확인한 기존 증거입니다. 모든 literal argv, PID, 종료 상태, stdout/stderr 및 본문 해시는 [review-qa.json](review-qa.json)에 보존했습니다.

| ID | 결과 | 실제 관찰 / 증거 |
|---|---|---|
| Q01 | PASS · 실행 | 독립 파일 목록 73/41/183개에 누락·추가 없음; 모든 파일/집계 해시 일치. |
| Q02 | PASS · 실행 | 최초 T3 대비 template 1개, README 2개와 index 1개 변경; Node 1개 추가. 이후 승인된 releases.md 변경도 별도로 검증; 40개 Python 테스트 포함 나머지 전부 일치. |
| Q03 | PASS · 실행 | 지정한 `uv run python … --help` exit 0; compare-gallery/show/prompt/export 확인. |
| Q04 | PASS · 실행 | 6개 snapshot.state 복원 후 show; 8개 원본과 저장된 prompt 일치, 모든 선택·review null. |
| Q05 | PASS · 실행 | COMMON/v1/revision1/brand와 Leaflet/v1/revision1/app_icon, count 2; 별도 파일과 링크. |
| Q06 | PASS · 실행 | 8개 비교의 18개 산출물이 현재 공개 갤러리와 완전히 동일; Relay/Sprig 부모 관계 보존. |
| Q07 | PASS · 실행 | 이미 있는 gallery 출력은 exit 1 conflict; 기존 6개 파일 그대로. |
| Q08 | PASS · 실행 | 중복 pair는 `invalid_selection: Choose distinct (session, artifact) pairs`, exit 1; 출력 없음. |
| Q09 | PASS · 실행 | `stale_revision: Session relay: expected 1; current 2`, exit 1; 출력 없음. |
| Q10 | PASS · 실행 | 잘린 JSON, -1 revision, 문자열 revision 모두 exit 1; 상태·출력 불변. |
| Q11 | PASS · 실행 | 없는 artifact는 not_found, 없는 session은 invalid_file; exit 1과 빈 stdout. |
| Q12 | PASS · 실행 + 재사용 | 실제 hostile selection은 escaped text와 단일 authored script, sentinel 없음; T4 31번 스크린샷도 inert notes. |
| Q13 | PASS · 실행 | 미선택 export는 not_selected, 별도 복사본에서 선택 후 export는 review_required; package 없음. |
| Q14 | PASS · 실행 | 실제 COMMON 원본의 격리된 상태 복사본에서 parent.lockup=null + 나중 brief=stacked; edit는 null, 새 generation prompt만 stacked. |
| Q15 | PASS · 실행 | 지정 curl은 HTTP/1.0 200 OK, 17,359-byte index; 정확한 본문 해시 일치. |
| Q16 | PASS · 실행 | 실제 HTML 링크 4개에서 brand/icon PNG와 exact prompt 다운로드; 모두 200과 원본 해시 일치. |
| Q17 | PASS · 실행 | 최초 951개 보호 파일 불변; 최종에는 승인된 releases.md 1개만 변경, 나머지 950개와 복원 source 14개 불변. 최종 73/41/183 map 일치. |
| Q18 | PASS · 실행 | kind/style 및 context/surround controls, 두 카드의 전체 source/revision 표시, 별도 copy/download ID 확인. |
| Q19 | PASS · 실행 | `node --test tests/comparison_browser_restoration.test.mjs`: 6 passed, 0 failed, 52.523291 ms. |
| Q20 | PASS · 재사용 + 직접 열람 | 45번은 Brand/Web header/Dark와 COMMON 1/8; 52번은 abstract/Favicon/Dark와 Relay v1/v2 2/8; 46번 reload 원본 표시. |
| Q21 | PASS · 실행 + 직접 열람 | 양쪽 README HTML [3,3], credits/links 유지; T4 32/33 desktop와 36/39 narrow 스크린샷 확인. |
| Q22 | PASS · 실행 | 6세션×3회 추가 show, Relay prompt 3회 완전 동일; 정확한 canonical parent 경로와 메모 보존. |
| Q23 | PASS · 재사용 | current hash-bound 622 baseline 및 58 follow-up 내 PNG/prompt/manifest/index 단계별 twice-cancel/retry와 foreign inode 보호. |
| Q24 | PASS · 재사용 + 실행 | installation follow-up의 73개 공통 source 해시와 추가 THIRD_PARTY_NOTICES 일치; 74개 payload/cache map 동일, template 갱신 확인. |
| Q25 | PASS · 실행 + 재사용 | 미승인 후보/illustrative 경고, 0.6.0 개발판 및 v0.3.1 기존 공개판, IP credit 유지; Leaflet 추가색·Relay drift·Sprig 미달 메모 보존. |
| R01 | PASS · 실행 | foreign/KEEP가 있는 목적지 거절; sentinel 원문·해시 불변. |
| R02 | PASS · 실행 | 알 수 없는 parent 필드는 extra_forbidden, ../common 경로는 pattern 거절; exit 1, 출력 없음. |
| R03 | PASS · 실행 | rate-limited PNG 전송 2회 의도적 50ms 취소(exit 28), 각 직후 index GET 200/완전 동일; 원본 불변. |
| R04 | PASS · 실행 | 8개 공개 PNG/prompt를 snapshot 및 18-file manifest와 대조; 전부 일치, 원본 부모 관계 보존. |
| R05 | PASS · 최종 receipt | 아래 cleanup receipt에서 각 파일·디렉터리·프로세스·포트 및 tool session 종료 확인. |

## 소스와 기존 검증의 연결

| 현재 그룹 | 파일 수 | SHA-256 aggregate |
|---|---:|---|
| Source payload | 73 | `039501853cade59c4d05f448c85e8d50b71888d7d16e6e45e29b9bcaa6f7dbc7` |
| Tests, Python + Node | 41 | `834097dae4a4160f74ffc69488be681869769c1937a79b63de53e7de0206392c` |
| Public docs/assets, final approved guide | 183 | `d6f164db0e3fa470aff3798db251cef299f43792e89fda61b3b09abbd5d8f409` |

[final-bindings.json](final-bindings.json)을 독립 git tracked/untracked 목록과 대조했습니다. 집계 규칙은 정렬된 `sha256 + two spaces + relative path + LF`입니다. T3 이후 변경은 `comparison-gallery.template.html`, README EN/KO, 공개 comparison/index.html 및 아래 승인된 releases.md입니다. 새 Node 테스트는 changes_since_t3의 기존 파일 변경 목록과 별도로 확인했습니다. 최초 HTTP/CLI 시점의 public aggregate `0cf9433aa0004f0a274e77c7e628683cb33795151a7664b221a6eec025c67abe`는 역사적 바인딩으로 JSON에 그대로 남겼습니다.

[integration.json](integration.json)의 **622 passed**, Ruff/format, basedpyright 0 diagnostics, lock 성공을 재사용했습니다. 바뀐 template와 새 Node 테스트는 [browser-restoration.json](browser-restoration.json)의 해시 및 **58 focused Python PASS**에 연결되고, 이번에 Node **6 cases**를 직접 실행했습니다. 전체 테스트를 반복하지 않았으며, 이 문서 작업에 새 build/LSP 결과를 주장하지 않습니다. [README 수정 증거](readme-layout-fix.md), [설치 후속 증거](installation-followup.json), [Chrome 증거](chrome.md)도 현재 바이트와 연결됩니다. 설치 항목은 source 73개에 unchanged THIRD_PARTY_NOTICES를 더한 74개이며 새 설치는 수행하지 않았습니다.

직접 열람한 주요 소스는 새 comparison 모듈 4개, template 전체, intent.py, 실제 entrypoint, storage/prompts/workflow/delivery, comparison-workflow, lockup continuity와 Node/publication/CLI/markup 테스트입니다. baseline diff뿐 아니라 새 untracked 기능 파일도 포함했습니다.

## 실제 CLI와 HTTP

```sh
uv run python skills/logo-land/scripts/logo_project.py --help
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-review-qa compare-gallery --selection-file /tmp/ll-060-review-qa/workspace/mixed.json --output gallery
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8798/gallery/index.html
node --test tests/comparison_browser_restoration.test.mjs
```

실제 helper 결과는 `{"path":"gallery","index_path":"gallery/index.html","count":2}`, exit 0입니다. 복원 session은 temp root의 `.logo-generator/`, selection 입력은 `workspace/` 아래에 두었습니다. HTTP 본문 SHA-256은 `2d8cf5298f12c0baa64d65790d2d9348dcc4dbcda9844febf6a2dd2c819dd4ea`이며, 아래 URL은 HTML의 실제 download 링크에서 추출했습니다.

| `/gallery/` 아래 다운로드 | 정체성 | SHA-256 |
|---|---|---|
| images/001.png | common/v1/r1 · brand · 1774×887 | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` |
| prompts/001.txt | common/v1/r1 exact prompt | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` |
| images/002.png | leaflet/v1/r1 · app_icon · 1254×1254 | `256b1ee1e25d9d8160ec0751db1453ae31990cecb5c2cd68570410c668cb6b4e` |
| prompts/002.txt | leaflet/v1/r1 exact prompt | `0cad98ad36526c630cf05aa5fdde33d14e87a5545d1302f4be6ba4628e14faf5` |

취소/재개 외 모든 HTTP 요청은 200이며 다운로드 4개 모두 PNG/prompt body 해시를 비교했습니다. 모든 실제 CLI/refusal argv와 JSON 입력은 evidence의 commands 및 cleanup inventory에 있으며, 혼합 selection은 gallery_manifest.source에 그대로 있습니다. API/image 호출이나 fake native output은 없습니다. 격리된 legacy 복사본에서 metadata 경계만 변형했고 실제 이미지를 새 결과로 import하지 않았습니다.

## 9개 적대적 범주

| 범주 | 결과와 범위 |
|---|---|
| Malformed input | 실제 JSON/type/negative/extra/traversal/absent 항목 거절; 출력 없음. |
| Prompt injection | hostile notes를 argv/JSON 데이터로만 전달; escaped HTML, exact quoted prompt, sentinel 없음. 네이티브 모델 면역성 주장은 없음. |
| Cancel/resume | 모든 세션 3회 추가 show, 정확한 parent/prompt; 실제 HTTP 취소 2회 후 정상 재개. 유료 native 호출 파괴적 취소는 N/A. |
| Stale state | 실제 revision 1 대 current 2 거절; 후속 brief default가 parent null을 채우지 않음. |
| Dirty worktree | 951개 보호 파일과 73/41/183 map 불변; existing output 및 foreign sentinel 보호. |
| Hung commands | CLI/Node 30초, curl connect 3초/total 20초와 outer 25초; 서버 lifetime 120초 및 finally TERM/reap. 예기치 않은 timeout 없음. |
| Flaky tests | 이번 Node 6건 한 번 통과; 전체 suite 재실행 없음. 아래 collector 오류와 첫 결과는 숨기지 않고 보존. |
| Misleading success | 반환 count만으로 통과시키지 않고 실제 HTML identities, 18개 output, 4개 HTTP 원본/prompt 및 상태 해시 확인. |
| Repeated interruptions | 두 전송 취소와 정상 GET 재개, 반복 show/prompt; publication 단계 취소는 source-bound 이전 테스트 재사용. |

## QA 도구 오류와 한계

제품 failure는 없었습니다. 첫 baseline collector는 새 Node 파일을 기존 파일 변경 목록과 혼동해 앱 실행 전에 중단했습니다. 첫 HTTP는 실제 200이고 해시가 일치했으나 Ruby UTF-8/ASCII-8BIT 문자열 비교가 false여서 collector가 중단했습니다. 동일 로컬 바이트의 text/binary 비교 false → binary/binary true 토글로 원인을 확인하고 stdout binmode만 수정해 HTTP 구간을 다시 실행했습니다. 첫 서버 PID와 응답은 보존했고 종료·reap 후 새 소유 서버로 실행했습니다. 설치 freeze 비교도 74개와 core 73개의 범위 차이를 그대로 비교해 중단했으며, 추가 THIRD_PARTY_NOTICES의 바이트까지 확인해 정정했습니다. 정적 검사 재실행은 이 진단에 한정되고 CLI 전체나 native 작업을 반복하지 않았습니다.

이전 read-only 탐색에서 Ruby 2.6의 Hash#except 미지원과 존재하지 않는 추정 파일명 2개가 나온 사실도 JSON에 남겼습니다. 모든 실패 표시에는 collector 오류 분류와 실제 진단을 붙였으며 제품 오류로 바꾸거나 기록을 삭제하지 않았습니다.

Chrome은 새로 실행하지 않았습니다. 기존 T4 스크린샷 8개를 원본으로 열람하고 해시를 검증했습니다. 좁은 화면 증거는 Chrome 300% zoom의 effective CSS 폭이며 실제 모바일 기기 검증은 아닙니다. 실제 폰트·정밀 HEX·모델/seed·플랫폼 package/승인을 보장하지 않습니다. T6 merge/delivery는 coordinator의 남은 작업이며 검토 실패가 아닙니다.

## 승인된 마지막 문서 변경

첫 cleanup preflight는 `docs/releases.md` 외부 변경을 감지하고 **파일을 하나도 삭제하기 전에** exit 1로 멈췄습니다. Coordinator의 `msg_571b6ee176d5`, `msg_1de8cd9f564d`, `msg_57737524b653`에서 context reviewer의 승인된 0.5.0→0.6.0 안내 수정임을 확인했습니다. 전체 문서와 정확한 diff를 읽고 현재 버전·현재 계획 링크·local-cache 예시만 바뀐 점, 공개 0.3.1 및 실패한 0.4.0 기록이 보존된 점을 확인했습니다.

Guide SHA-256은 `e3f6aa8d31b7356bb3440e71c8dbda5720bff50a4cd5546bcdbffa006d354f35`, 갱신된 final-bindings.json SHA-256은 `df6c741906d3df829f387d9e6c1a6c2a753e2c6e219d154504f636f15a221337`입니다. source73/test41은 그대로이고 public183의 단 한 파일 변경만 반영되었습니다. 새 map 전체와 집계 해시, 수정된 계획 링크의 존재를 직접 확인한 후 cleanup을 재개했습니다. CLI·Node·전체 suite 재실행은 없었습니다. 최초 map, 이전/이후 guide 해시, diff와 cleanup 중단 사실은 JSON `authorized_late_delta`에 남겼습니다.

## Cleanup receipt

PASS: owned root device/inode 16777230/35041829 확인 후 68개 파일 각각의 inode·해시를 재확인하여 unlink하고, 34개 빈 디렉터리를 제거했습니다. `/tmp/ll-060-review-qa`는 존재하지 않습니다. 모든 스크립트 원문, 입력 JSON, 파일별 SHA-256과 literal subprocess argv는 `review-qa.json`에 보존했습니다.

서버 PID 30310 / 31369 모두 SIGTERM 후 reap되었고 port 8798은 비어 있습니다. 등록 PID 71개 중 cleanup driver 39449 외 전부 부재를 확인했으며, driver 종료 확인은 아래 최종 receipt로 기록합니다. Tool exec session 16350도 exit 0으로 종료되었습니다. 새 Chrome/Orca/tmux session은 만들지 않았고 기존 Chrome 탭은 건드리지 않았습니다.

삭제 파일 집계 SHA-256: `eb0bc97240eb3bb352b629c17fc9831e6c88f07543a56c49b61fc66256c48a5e`. 승인된 releases.md 변경을 반영한 최종 Source/test/public map과 951개 보호 파일, 14개 복원 source 및 모든 native 원본/prompt/approval은 최종 확인까지 불변입니다.

**최종 cleanup PASS:** 등록한 71개 PID 모두 부재(마지막 cleanup driver 39449 포함), 임시 root 부재, port 8798 free, 갱신된 73/41/183 map 전체 일치를 확인했습니다. 최종 retained artifact는 이 보고서와 review-qa.json뿐입니다.
