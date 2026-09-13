# T5 독립 코드 검토

**PASS · 확인된 제품 결함 없음 · 신뢰도 높음.** 기준 `06b94c41922973fc98392fadde25fff9aa498f6e`, 브랜치 `feat/logo-land-gallery-workflow`를 검토했습니다. 추적되지 않은 신규 파일도 포함했습니다. 원본·구현·테스트는 수정하지 않았으며, T6 병합 대기는 이 검토의 실패가 아닙니다.

Task `task_22720923e882` / dispatch `ctx_2d9c12278f97`. 실제 argv, 종료 코드, stdout/stderr와 해시, 입력, 전체 임시 검증 스크립트, 보존·정리 목록은 [review-code.json](review-code.json)에 있습니다.

## 코드와 기존 증거 검토

신규 비교 모듈 네 개, 전체 HTML 템플릿, CLI 등록과 `intent.py`, 인접 모델·저장소·PNG 검사·기존 갤러리·게시·프롬프트·import/export 구현을 모두 읽었습니다. 신규 Python 테스트 여덟 파일, 연속성 테스트, 변경된 호환성 테스트/프롬프트 fixture, Node 회귀 테스트와 공용 테스트 helper도 전체 확인했습니다. 계획 T1–T5 및 비교·연속성·통합·설치·Chrome·후속 수정 기록을 대조했습니다.

- **게시·롤백:** [comparison_gallery.py](../../../skills/logo-land/scripts/logo_helper/comparison_gallery.py)는 명시적 현재 리비전을 확인하고, 저장된 PNG 해시·실제 디코딩 정보를 복사 시 다시 확인합니다. staging 완료 후 `Store.expect`로 재검증합니다. 기존 [app_icon_publish.py](../../../skills/logo-land/scripts/logo_helper/app_icon_publish.py)는 배타적으로 출력 경로를 만들고 index를 마지막으로 링크하며, 롤백 시 inode가 일치하는 자체 파일만 정리합니다. 전체 디렉터리 rename 방식의 원자성을 주장하는 구현은 아닙니다.
- **입력·식별·오류:** strict frozen Pydantic 계약으로 강제 형변환·추가 필드를 거부합니다. 선택 파일 4 MiB, 후보 1–60개, 제목 200자와 메모별 2,000자 제한이 있으며, 기존 파일 reader도 64 MiB로 제한됩니다. `(session, artifact)` 중복을 거부하고 리비전을 별도로 검사하므로 서로 다른 세션의 `v1`이 충돌하지 않습니다. 알려진 입력·파일 오류는 실제 CLI에서 비영 종료와 오류 JSON으로 전달됩니다.
- **연속성·승인:** 부모가 있으면 부모의 `null` lockup을 유지하고, 부모가 없을 때만 brief에서 상속합니다. 프롬프트와 import가 같은 resolver를 사용합니다. 비교는 선택·검토·승인을 설정하지 않으며 기존 export gate를 유지합니다.
- **안전한 표시·유지보수:** 사용자 문자열은 HTML에서 escape되고 URL은 내부 순번으로 생성됩니다. 사용자 데이터는 JavaScript에 삽입되지 않습니다. 역할이 모델/CLI/게시/카드로 분리되어 있고 신규 모듈은 각각 56/23/85/90 비공백·비주석 줄입니다. 타입 우회나 신규 의존성은 없습니다.
- **테스트 의미:** 단순 성공 코드뿐 아니라 실제 CLI, 원본/프롬프트 바이트, 상태 보존, 선택 후 미검토 export 거부, 게시 단계별 취소·외부 inode 보존·중간 리비전/PNG 변경을 확인합니다. 바뀐 레거시 fixture는 재현된 잘못된 brief 상속 문단만 제거하며 기존 배경·프롬프트 검증을 유지합니다. Node 테스트는 실제 템플릿 스크립트를 실행하고, 실제 Chrome 검증은 별도 소유자 기록으로 구분됩니다.

## 현재 소스 해시 연결

[final-bindings.json](final-bindings.json)의 파일 목록을 독립적으로 다시 열거하고 모든 파일 해시와 정렬 집계값을 검증했습니다. CLI 전후 및 정리 직후 보호 파일 **303개**, 임시 원본/상태 **16개**가 일치했습니다. 공개 8개 원본과 프롬프트·스냅샷도 포함됩니다. 이후 coordinator가 알린 `docs/releases.md` 수정만 발생했으며, 아래 최종 값은 해당 변경을 포함합니다.

| 그룹 | 파일 수 | SHA-256 |
|---|---:|---|
| 소스 | 73 | `039501853cade59c4d05f448c85e8d50b71888d7d16e6e45e29b9bcaa6f7dbc7` |
| 테스트 | 41 | `834097dae4a4160f74ffc69488be681869769c1937a79b63de53e7de0206392c` |
| 공개 문서·신규 자료 | 183 | `d6f164db0e3fa470aff3798db251cef299f43792e89fda61b3b09abbd5d8f409` |

T3 이후 기존 파일 변경은 템플릿 1개와 README 두 개/공개 index/출시 가이드 4개입니다. 기존 Python 테스트 40개는 같고 Node 테스트 1개가 추가되었습니다. README 두 언어의 이미지 문단은 각각 `[3, 3]`입니다. CLI QA 당시 공개 집계 `0cf9433aa0004f0a274e77c7e628683cb33795151a7664b221a6eec025c67abe`는 T4 시점의 역사적 값으로 보존합니다.

최종 점검은 출시 가이드 변경을 해시 불일치로 정확히 감지했습니다. coordinator 알림 `msg_f041e2611be0`과 갱신 완료 `msg_8978a7517c74`를 받고 전체 diff를 확인했습니다. 현재 소스/개인 캐시 예시를 0.6.0으로 고치고 계획 링크를 갱신한 좁은 변경이며, 공개 0.3.1과 실패한 미출시 0.4.0 기록은 유지됩니다. 최종 가이드 SHA는 `e3f6aa8d31b7356bb3440e71c8dbda5720bff50a4cd5546bcdbffa006d354f35`, 최종 바인딩 파일 SHA는 `df6c741906d3df829f387d9e6c1a6c2a753e2c6e219d154504f636f15a221337`입니다. 나머지 302개 보호 파일은 그대로이며 소스/테스트 재실행 사유는 없습니다.

**기존 실행 재사용이며 이번 재실행은 아닙니다:** [integration.json](integration.json)의 622개 통과, Ruff/format 성공, basedpyright 0 diagnostics, lock 검증을 그대로 연결했습니다. 템플릿 변경은 [browser-restoration.json](browser-restoration.json)의 `node --test tests/comparison_browser_restoration.test.mjs` **6개 통과**와 별도 Python **58개 통과**에 연결됩니다. 새 결함이 없어 전체/집중 테스트를 중복 실행하지 않았습니다. [installation-followup.json](installation-followup.json)의 최종 템플릿 및 18개 공개 파일 해시도 현재 파일과 일치합니다. 해당 설치와 Chrome 결과는 소유자 증거 재사용이며, 이번 검토에서 설치나 브라우저 조작을 수행하지 않았습니다.

## 실제 CLI·HTTP 시나리오

공개 스냅샷의 `state`를 풀어 여섯 세션과 기존 레거시 fixture를 소유 임시 경로에 복원했습니다. 직접 원본·프롬프트 해시를 검증한 뒤 실제 helper로 게시했습니다. 모든 호출은 argv 배열로 실행했습니다. 환경 `PYTHONDONTWRITEBYTECODE=1`, `UV_NO_SYNC=1`, `UV_OFFLINE=1`로 설치·bytecode 쓰기를 방지했습니다.

실제 작업 디렉터리는 저장소 루트이며 주요 명령은 다음과 같습니다.

```sh
uv run python skills/logo-land/scripts/logo_project.py --help
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-review-code compare-gallery --selection-file /tmp/ll-060-review-code/inputs/selection.json --output gallery
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8796/gallery/index.html
```

비교 명령은 exit 0, `{"path":"gallery","index_path":"gallery/index.html","count":2}`를 반환했습니다. HTTP는 **200 OK**, 본문 **17,146 bytes**, SHA-256 `76f82b41a5a848bc90433eb193f669e42f60ed3f4c45e4e1263ea24debd49edc`이며 생성 파일과 동일합니다. HTML의 실제 다운로드 링크 네 개를 추출해 같은 curl 인자로 요청했습니다.

| 실제 링크 | 원본·manifest·HTTP 공통 SHA-256 |
|---|---|
| `/gallery/images/001.png` · COMMON | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` |
| `/gallery/prompts/001.txt` · COMMON | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` |
| `/gallery/images/002.png` · Drip | `8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f` |
| `/gallery/prompts/002.txt` · Drip | `67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d` |

| 독립 시나리오 | 실제 결과 |
|---|---|
| COMMON/Drip의 동일 `v1` | 서로 다른 session/artifact/revision, brand/app_icon 구분, 두 원본 보존 |
| 공개 최종 선택 8개 재생성 | 생성 파일 18개 전부 현재 공개 비교와 동일 |
| `{` 잘못된 JSON | exit 1, `Invalid JSON`, 출력 경로 없음 |
| boolean revision | exit 1, integer 검증 거부, 출력 없음 |
| relay/v1의 revision 1 | exit 1, `stale_revision: Session relay: expected 1; current 2` |
| 동일 후보 중복 | exit 1, `invalid_selection`, 출력 없음 |
| 4 MiB + 1 입력 | exit 1, `Selection JSON exceeds the 4 MiB limit` |
| 기존 foreign 출력 | exit 1 conflict, sentinel 원본 바이트 보존 |
| hostile 메모 | script/img/onerror/셸 형태 문자열 escape, authored script 1개, marker 없음, JSON 메모 그대로 |
| 레거시 show/prompt 2회 | brief nonnull/parent null 유지, 실제 정규화된 부모 경로와 메모 보존 |
| 비교 후 export | exit 1 `not_selected`, 승인·세션 변경과 export 출력 없음 |
| 실제 링크 다운로드·반복 GET | 총 7회 HTTP 200, 바이트 일치, 상태·리비전·승인 불변 |

## 아홉 가지 적대적 조건

| 조건 | 근거 |
|---|---|
| malformed input | 위 실제 JSON/타입/중복/용량 거부 |
| prompt injection | 위 실제 hostile 메모와 literal argv, 실행 marker 부재 |
| cancel/resume | 새 show/prompt·GET 반복; 게시 취소는 기존 소스 연결 테스트 재사용 |
| stale state | 새 relay 리비전 거부; staging 도중 변경 검사는 기존 테스트 재사용 |
| dirty worktree | CLI QA의 303개 보호 파일 동일, 이후 허가된 가이드 변경 하나만 탐지·재검증; 외부 sentinel 보존 및 inode 교체 롤백 재사용 |
| hung commands | CLI 30초, curl 연결 3초/전체 20초/외부 25초, 서버 300초 제한; timeout 없음 |
| flaky tests | 새 테스트 실행/실패 은폐 없음; 아래 임시 harness 중단 두 건 공개 |
| misleading success | 실제 count/식별자/HTTP 본문/원본 해시/18개 파일/상태 보존을 함께 검증 |
| repeated interruptions | 이미지·프롬프트·manifest·index의 두 번 취소 후 재시도 테스트 재사용; 새 반복 읽기와 reload 바이트 보존 |

새로운 강제 중단/동시 OS 공격 실험은 하지 않았습니다. 단계별 publication fault 증거는 동일 소스와 테스트에 연결된 T3/T4 실행을 재사용합니다. 유료 네이티브 호출 중단은 N/A입니다. 이번 검토에는 이미지/API 호출이 없습니다.

임시 harness 첫 시도는 Ruby의 ASCII-8BIT/UTF-8 비교에서 멈췄습니다. 실제 SHA-256은 같아 바이트 비교로 교정했습니다. 이후 부모 경로를 `/tmp`로 예상한 검사가 실제 정상 경로 `/private/tmp`에서 멈춰 realpath로 교정하고 남은 읽기/HTTP 단계만 이어갔습니다. 두 중단의 실제 기록을 JSON에 보존했으며 제품 오류나 숨긴 재시도로 처리하지 않았습니다.

## 리소스 정리와 범위

생성 전 등록 메시지 `msg_78d14bdf2433`: `/tmp/ll-060-review-code`, 하위 fixture/input/log/검증 스크립트와 `127.0.0.1:8796`. root identity는 device **16777230**, inode **35041861**입니다. 임시 Ruby 스크립트 세 개와 파일별 inode/해시 목록을 JSON에 보존한 다음 **58개 자체 파일**과 빈 하위 디렉터리만 삭제했습니다. 임시 root가 없고, 서버 PID **30923**은 SIGTERM 후 reap되었으며 포트 재바인드가 성공했습니다. 기존 등록 PID 39개와 최종 정리 driver **34669**의 종료도 확인했습니다. 새 tmux·브라우저·Orca 하위 세션은 만들지 않았고 이 worker 터미널의 해제는 coordinator 소유입니다.

`git diff --check`는 exit 0입니다. 미해결 제품 결함은 없습니다. 설치 기록의 기존 무관한 astral marketplace-list 실패는 보존했으며 다시 조사하지 않았습니다. 원본 8개, IP 출처, 역사적 실패·불충분 판정과 미승인 상태를 유지합니다. source 0.6.0은 unreleased이며 CSS 예시는 플랫폼 패키지·정확한 폰트/모델/seed 보장이 아닙니다. 남은 통합 검토와 커밋·배포 판단은 coordinator 범위입니다.
