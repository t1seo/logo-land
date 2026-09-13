# T5 독립 목표·제약 리뷰

**최종 PASS, 정리 완료입니다.** 확인된 제품 결함이나 미충족 첫 마일스톤 요구사항은 없습니다. 신뢰도는 높음이며, 이미지 제작·설치·Chrome 동작은 아래 명시한 기존 실행 증거를 현재 파일에 연결해 판정했습니다.

Task `task_07f0145a6133`, dispatch `ctx_17f869370ad6`. 작업 디렉터리 `/Users/cillian/Documents/Github/Projects/logo-generator`, 브랜치 `feat/logo-land-gallery-workflow`, 비교 기준 `06b94c41922973fc98392fadde25fff9aa498f6e`입니다. 추적되지 않은 신규 기능 파일도 포함했습니다. 코드·문서·자산·설정은 읽기 전용으로 검토했고, 이 보고서와 [기계 판독 증거](review-goal.json)만 소유합니다. T6 커밋·푸시·main 병합은 조정자의 후속 작업이며 T5 실패 사유가 아닙니다.

## 완료한 범위

| 승인 요구사항 | 판정과 근거 |
|---|---|
| 여러 세션의 브랜드/아이콘 혼합 비교 | 달성. 여섯 공개 스냅샷의 `state`를 독립 workspace에 복원하고 실제 `show`로 검증했습니다. 실제 `compare-gallery`는 동일한 `v1` ID를 세션별로 구분하고, 여덟 원본 및 두 child 계보를 모두 발행했습니다. |
| 현재 리비전·명시적 원본·바이트 보존 | 달성. [비교 모델](../../../skills/logo-land/scripts/logo_helper/comparison_models.py), [발행 경로](../../../skills/logo-land/scripts/logo_helper/comparison_gallery.py), storage/publisher 전체를 검토했습니다. Relay/Sprig의 v1도 현재 revision 2를 사용합니다. 독립 발행 18개 파일이 최종 공개 파일과 모두 동일합니다. |
| 이유·유지·변경·관찰을 수정으로 연결 | 달성. [전체 워크플로](../../../skills/logo-land/references/comparison-workflow.md), SKILL 및 관련 지침과 카드/프롬프트 경로를 검토했습니다. 실제 Relay/v2 `prompt` 두 번에 네 메모, revision 2, 정확한 parent 경로가 유지됐고 상태는 불변입니다. |
| narrow legacy-null 수정 | 달성. [intent.py](../../../skills/logo-land/scripts/logo_helper/intent.py)의 두 줄 변경은 부모가 없을 때만 brief를 사용합니다. 실제 집중 검사 10개가 fresh/non-null/override/null/모순 입력/재개를 통과했습니다. 기존 fixture 변경은 잘못 상속된 마지막 lockup 문단 제거이며 배경·원본 프롬프트 검사는 유지됐습니다. |
| 사용 장면과 작은 크기 비교 | 달성. template/cards 전체에서 artwork/home/header/favicon, 16/32/64/128, light/dark, 필터·reset·복사·다운로드를 확인했습니다. 실제 Node 6개가 현재 template의 복원 동작을 통과합니다. 실제 Chrome 조작은 [T4](chrome.md)의 해시가 일치하는 증거를 재사용합니다. |
| 영문 기본·한국어 README, 즉시 샘플·한 번의 전체 갤러리 이동 | 달성. 두 README 전체 및 수정된 문서·설치 안내·갤러리를 검토했습니다. 각 README에 3+3 원본 링크가 있고, EN/KO 통합 페이지 모두 동일한 54개 원본 경로/53개 고유 PNG 해시를 직접 표시합니다. GitHub용 Markdown과 로컬 HTML을 구분합니다. |
| 네이티브 결과 여덟 개 | 달성. 여섯 initial + Relay/Sprig child 두 개이며 전부 보존됐습니다. 각 공개 receipt/prompt/state/manifest/PNG 해시·크기·계보·메모가 연결됩니다. 실제 호출의 근거는 [native](native-samples.md)와 [T3](integration.json)를 재사용하며 신규 이미지 호출은 하지 않았습니다. |
| 원본/후보/승인 구분 및 관찰의 정직성 | 달성. 여섯 세션의 선택과 모든 review가 null로 유지됐습니다. 갤러리 이후 COMMON export는 `not_selected`로 거절됐습니다. 선택된 미검수 후보의 `review_required`는 해시가 일치하는 기존 테스트·설치 증거에 연결됩니다. Leaflet 추가 색상, Relay 형태 변화, Sprig 미실현 굽힘과 과거 실패·미확정 결과가 남아 있습니다. |
| 개발 0.6.0과 개인 설치 | 달성. manifest/project/lock 버전은 0.6.0이고 CHANGELOG는 Unreleased입니다. pyproject/uv.lock은 기준 소스와 helper 버전 외 동일합니다. [최종 설치](installation-followup.json)의 personal/cache 74개 map이 서로 같고 73개 비manifest 파일은 현재 소스와 같습니다. 실제 설치와 cache CLI/HTTP는 담당자의 실행 증거를 재사용합니다. |
| 범위·출처·기존 기능 보존 | 달성. 실제 폰트 조판·벡터·플랫폼 패키지는 계속 후속 범위이며 새 의존성이 없습니다. IP 고정 출처·MIT 고지 및 기존 IP 프롬프트/원본을 보존합니다. 모델·seed·정확한 이미지 크기·폰트 재현·플랫폼 승인 보장을 추가하지 않았습니다. |

계획 T1–T5, integration/installation/Chrome 및 보완 기록, 신규 네 모듈과 template, CLI/intent 변경 및 관련 storage/session/prompt/publisher, 변경 테스트, 사용 지침·README·갤러리·native 바인딩을 검토했습니다. 통합본을 읽고 실행한 결과이며 `git diff`만으로 신규 파일을 누락하지 않았습니다.

## 현재 소스와 기존 검사 연결

[final-bindings.json](final-bindings.json)의 파일별 SHA-256와 정렬된 `<sha>  <path>\n` 집계값을 독립 계산했습니다. 실행 전후 소스·테스트·native 바인딩은 유지됐습니다. 마지막에 조정자가 알린 릴리스 안내 문서 보완을 아래 최종 공개 map에 반영했습니다.

| 그룹 | 개수 | 현재 aggregate SHA-256 |
|---|---:|---|
| 설치 소스 | 73 | `039501853cade59c4d05f448c85e8d50b71888d7d16e6e45e29b9bcaa6f7dbc7` |
| 테스트 | 41 | `834097dae4a4160f74ffc69488be681869769c1937a79b63de53e7de0206392c` |
| 공개 문서·갤러리 파일 | 183 | `d6f164db0e3fa470aff3798db251cef299f43792e89fda61b3b09abbd5d8f409` |

T3 이후 차이는 소스 template 1개, 공개 README 두 개·generated index·릴리스 안내의 총 4개입니다. 초기 T4 공개 aggregate `0cf9433aa0004f0a274e77c7e628683cb33795151a7664b221a6eec025c67abe`는 역사적 바인딩으로 남깁니다. T3의 Python 테스트 40개는 전부 동일하고 Node `.mjs` 1개만 추가됐습니다. 기존 622개 Python 검사·Ruff/format/basedpyright/lock 성공은 [T3](integration.md), template/index의 이후 보완은 [복원 수정](browser-restoration.md)의 Node 6개·Python 집중 58개, README 변경은 [3+3 보완](readme-layout-fix.md)에 각각 연결했습니다. 역사적 template/README 해시가 현재와 다른 것을 실패로 취급하지 않았습니다. 전체 suite는 재실행하지 않았습니다.

새 실행은 `node --test tests/comparison_browser_restoration.test.mjs` **6 PASS**, `uv run pytest -q tests/test_lockup_continuity.py` **10 PASS / 5.64초**입니다. `git diff --check`도 통과했습니다. 독립 리뷰가 새 LSP 검사나 별도 빌드를 실행했다고 주장하지 않습니다.

## 독립 실제 시나리오

모든 CLI는 실제 helper argv이며 dry-run이 없습니다. 성공·의도된 거절을 포함한 36개 명령과 두 SIGINT 명령의 literal argv, stdout/stderr, 종료값·해시·PID가 JSON에 있습니다.

| 시나리오 | 실제 결과 |
|---|---|
| 대표 1: COMMON brand + Drip icon의 같은 v1 | 혼합 갤러리에 각각 `common/v1/r1`, `drip/v1/r1`로 존재합니다. 실제 링크의 PNG/프롬프트 HTTP 네 건이 200이며 원본 해시와 같습니다. |
| 대표 2: 여섯 세션의 전체 여덟 후보 | 실제 CLI count 8, 공개 18개 파일과 바이트 단위 일치, brand 1/icon 7 및 child 계보 둘이 유지됩니다. |
| 대표 3: Relay/v2 선택 맥락 재개 | `show → prompt` 두 회에서 revision 2, parent v2, 실제 canonical 경로, 네 판단 메모가 유지됩니다. 네이티브 편집을 했다고 주장하지 않습니다. |
| 경계: 잘린 JSON `{"title":` | exit 1, `json_invalid`, 결과 폴더 없음. |
| 경계: 동일 session/artifact 중복 | exit 1, `invalid_selection`, 결과 폴더 없음. |
| 경계: Relay r1을 현재 r2에 사용 | exit 1, `stale_revision: Session relay: expected 1; current 2`, 결과 폴더 없음. |
| 경계: revision=true | exit 1, `int_type`, 결과 폴더 없음. |
| 경계: 공백 title | exit 1, `string_pattern_mismatch`, 결과 폴더 없음. |
| 경계: artifact=missing | exit 1, `not_found`, 결과 폴더 없음. |
| 경계: preserve 2,001자 | exit 1, `string_too_long`, 결과 폴더 없음. |
| 경계: reserved/absolute 출력 | 각각 exit 1, `reserved_output`/`unsafe_path`. |
| 기존 foreign-gallery | exit 1, 기존 `foreign.txt` 해시 동일. |
| 악성 형태의 notes/title | closing textarea/script, img/onerror, shell substitution, 승인 지시가 들어간 JSON을 실제 CLI로 발행했습니다. authored script 1개, 입력 markup은 escaped data, manifest 메모 유지, sentinel 없음. 모델 수준 면역성은 검증하지 않았습니다. |
| 승인 우회 | 비교 후 COMMON export exit 1, `not_selected`; 상태·원본 불변. |
| 두 번 읽기 중단 후 재개 | 실제 `show` 시작 50ms 뒤 각 process group에 SIGINT, 두 번 모두 exit 130/KeyboardInterrupt였습니다. 이어진 실제 show가 기존 Relay state와 같고, 14개 fixture 파일 해시가 같습니다. 임의 쓰기 중단 시점까지 검증한 것은 아닙니다. |
| 반복 HTTP GET | index 최초 및 두 추가 GET 모두 200, 동일 본문 SHA-256입니다. |

## 정확한 수동 QA 채널

```sh
uv run python skills/logo-land/scripts/logo_project.py --help
uv run python /Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-review-goal compare-gallery --selection-file /tmp/ll-060-review-goal/inputs/selection.json --output gallery
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8795/gallery/index.html
```

실제 CLI 결과는 `{"path":"gallery","index_path":"gallery/index.html","count":8}`, exit 0입니다. curl은 **HTTP/1.0 200 OK**, 42,459 bytes이며 index SHA-256은 `66e8ac8fd728f85a683ee041437a2a0fbe56a2f4b89902fb9eefc4c1d29610c6`입니다. 본문은 실제 발행 파일과 같습니다.

같은 본문에 있는 `href`를 확인한 후 실제 `/gallery/images/002.png`, `/gallery/prompts/002.txt`(Drip), `/gallery/images/008.png`, `/gallery/prompts/008.txt`(COMMON)를 `curl --fail --connect-timeout 3 --max-time 20 --output <owned-file> --write-out '%{http_code}' <linked-URL>`로 내려받았습니다. 모두 200입니다.

| 원본 | PNG SHA-256 | prompt SHA-256 |
|---|---|---|
| Drip | `8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f` | `67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d` |
| COMMON | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` |

**수동 채널 binary PASS:** 실제 CLI/HTTP 200·정확한 source identity·PNG/prompt 본문 해시·원본/승인 불변 조건이 모두 만족됩니다. 서버 시작 성공만으로 판정하지 않았습니다.

## 아홉 가지 적대적 상황

| 종류 | 실행·재사용 범위 |
|---|---|
| Malformed input | 위 실제 7개 input 거절과 안전하지 않은 output 두 개를 확인했습니다. 최대 60개/4 MiB 및 추가 경계는 바인딩된 기존 검사 재사용입니다. |
| Prompt injection | 실제 notes/title escaping·단일 script·sentinel 부재와 네 메모 전달을 확인했습니다. native 공격 호출은 N/A입니다. |
| Cancel/resume | 두 실제 SIGINT와 성공 재개, 두 show/prompt 및 세 HTTP GET의 바이트 보존을 확인했습니다. |
| Stale state | 현재 리비전 불일치 실제 거절, 전체 소스 pre/post hash; staging 중 변경은 기존 publication 검사 재사용입니다. |
| Dirty worktree | 처음부터 dirty branch에서 foreign 출력을 보호했습니다. 보호 파일 1,513개 중 1,511개는 동일하고, 릴리스 안내와 최종 바인딩 JSON 두 개만 조정자가 알린대로 변경됐습니다. 다른 리뷰 파일은 별도 소유로 제외했습니다. |
| Hung commands | CLI/Node/집중 pytest 30초, curl total 20초/outer 25초, 취소 wait 10초, 서버 300초 한도입니다. timeout은 없었습니다. |
| Flaky tests | 집중 Node/Python 각 한 번, 전체 suite 추가 실행 없음. 아래 검증기 오류를 숨기지 않고 저장했으며 성공한 CLI 발행을 반복하지 않았습니다. |
| Misleading success | count/manifest/18개 파일/실제 HTTP/원본 해시/승인 상태를 교차 확인했습니다. QA 성공과 이미지 미감·정식 출시를 구분했습니다. |
| Repeated interruptions | 실제 SIGINT 두 회 후 동일 state를 확인했습니다. 네 발행 단계의 twice-cancel/rollback/retry는 현재 Python 소스·테스트에 바인딩된 T3/T4 결과 재사용입니다. 유료 이미지·설치 중단은 이 읽기 전용 리뷰에서 N/A입니다. |

## 자원 등록·검증기 한계

실행 전에 이 보고서에 `/tmp/ll-060-review-goal`, scripts `review.rb`/`finish.rb`, `.logo-generator`, inputs/gallery/hostile-gallery/foreign-gallery/downloads/server.log와 포트 **8795**를 등록했습니다. 임시 루트는 배타적으로 생성했고 device/inode는 **16777230/35041665**입니다. 각 실행 argv를 먼저 저장하고 PID를 시작 직후 기록했습니다. 서버 PID **31308**은 SIGTERM으로 종료·회수됐고 포트 재바인딩이 통과했습니다. 브라우저는 만들지 않았습니다.

Ruby 검증기에서 제품과 무관한 오류를 공개합니다. 두 `ruby -c` 실패는 닫는 괄호 누락으로 실제 시나리오 전에 수정했습니다. 첫 실행은 한글 prompt의 binary/UTF-8 문자열 비교 차이, 다음 실행은 macOS `/tmp`/`/private/tmp` 문자열 비교 때문에 멈췄습니다. 바이트와 canonical 경로로 확인해 제품 문제와 구별했고, 원래 출력·실패를 JSON에 유지한 채 성공한 명령을 재실행하지 않고 이어갔습니다. 소스·테스트나 예상 결과를 고친 것은 아닙니다.

집중 pytest는 기본 framework 경로 `.../T/pytest-of-cillian/pytest-107`을 만들었습니다. 실행 시각 및 정확한 10개 테스트 디렉터리로 소유를 확인해 별도 정리 목록에 포함했습니다. 기존 pytest-105/106 또는 다른 프로세스·작업 자원은 정리 대상이 아닙니다.

새 이미지, API, 설치, commit/checkout/push를 실행하지 않았습니다. 실제 Chrome 클릭·viewport는 [기존 최종 T4](chrome.md), 실제 personal 설치는 [기존 최종 설치](installation-followup.md)를 재사용했습니다. 설치 기록의 알려진 별도 astral marketplace 조회 오류는 본 리뷰에서 다시 실행하지 않았으며 성공한 personal 설치와 구분됩니다. 공개 릴리스 표시는 주어진 기존 v0.3.1 기준을 유지했는지 검토했고, 새 외부 릴리스 조회나 게시를 하지 않았습니다.

## 마지막 보완 확인과 정리 영수증

정리 후 마지막 해시 검사는 동시 변경된 `docs/releases.md`와 `final-bindings.json`을 정확히 감지하고 멈췄습니다. 조정자의 `msg_20f1623704a7`/`msg_c9671dd73587`을 읽고, [릴리스 안내](../../releases.md) 전체와 두 문단의 narrow diff를 다시 검토했습니다. current source/cache 예시만 0.6.0으로 정정됐고 v0.3.1 공개 상태·0.4.0 실패 이력은 보존됐습니다. 갱신 map의 소스 73·테스트 41·공개 파일 183개 및 위 aggregate를 전부 다시 확인했으며, 다른 1,511개 보호 파일은 동일합니다. 현재 `final-bindings.json` SHA-256은 `df6c741906d3df829f387d9e6c1a6c2a753e2c6e219d154504f636f15a221337`입니다.

등록 임시 루트와 pytest-107의 **일반 파일 125개, symlink 8개, 디렉터리 95개**를 소유·inode·해시 검사 후 정리했습니다. pytest의 공유 `pytest-current`는 이번 실행이 만든 정확한 inode/생성 시각/107 대상일 때만 제거했습니다. 기존 테스트 디렉터리는 보존됐습니다. 모든 파일의 제거 전 inventory와 최종 두 Ruby 스크립트는 JSON 증거에 남아 있습니다.

서버 31308 및 드라이버 28632/29974/31056/35077, 모든 CLI/취소 자식 등 **등록 PID 43개와 cleanup driver 38718**의 부재를 확인했습니다. 서버는 종료·회수됐고 포트 8795는 재바인딩 가능하며 두 임시 루트 모두 없습니다. 도구 세션 61419/47414는 공개한 검증기 오류로 종료됐고, 44845/45082는 exit 0으로 종료됐습니다. 원래 Orca 작업 터미널은 조정자가 해제하도록 그대로 두었습니다. 이 리뷰가 만든 브라우저나 최종 제공 페이지는 남아 있지 않습니다.

실행 계획은 자료·바인딩 검토, 독립 CLI/HTTP 시나리오, 증거·정리 확인 모두 완료입니다. 남은 작업은 조정자의 나머지 T5 종합 및 승인된 T6 전달입니다. 확인된 제품 결함은 없으며 최종 판정은 **PASS**입니다.
