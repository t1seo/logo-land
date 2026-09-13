# T5 independent security review

**PASS · Severity NONE · 보안 취약점 재현 없음.** Task `task_5a83ad532fc4`, dispatch `ctx_122c5e3f3843`.

Read-only security ownership on `feat/logo-land-gallery-workflow`, baseline `06b94c41922973fc98392fadde25fff9aa498f6e`; only this report and `review-security.json` may be retained.

Resource registration before creation: exclusive `/tmp/ll-060-review-security/`, `review.rb`, `finish.rb`, `workspace/` fixture descendants, `inputs/`, `downloads/`, generated `gallery/` and adversarial destinations, subprocess logs and registration records; bounded static server on `127.0.0.1:8797`. The fixture workspace is the temporary root so the required publication is exactly `/tmp/ll-060-review-security/gallery/index.html`. All subprocess argv, PID, timeout and status will be captured, with no installation or native/image calls. The server will use the existing interpreter and receive a 300-second lifetime bound plus explicit termination/reap. Cleanup will verify the root device/inode, inventory files/symlinks, remove only owned descendants, and confirm root/PID/port absence.

Execution ledger: complete source/evidence review → complete frozen hash binding → complete actual CLI/HTTP/adversarial checks → complete cleanup → PASS. T6 merge is outside this review.

## 검토 범위와 현재 소스 연결

입력 모델, CLI, 카드 직렬화, 템플릿 전체, `storage.py`, `app_icon_publish.py`, `images.py`, `delivery.py`, `intent.py`, 실행 helper를 모두 읽었습니다. 계획 T1–T5와 비교·연속성·통합·Chrome·설치 및 복원/README 후속 증거, 공개 스냅샷·입력·프롬프트·원본·출처 문서를 확인했습니다. Git diff에 없는 새 비교 모듈과 Node 테스트도 포함했습니다. 상세 argv, 실제 stdout/stderr·종료 상태·해시, 입력, 파일별 해시, 임시 자원 목록은 [review-security.json](review-security.json)에 있습니다.

`final-bindings.json`의 모든 파일을 실행 전후 독립 계산했습니다. 소스와 Python/Node 테스트의 파일 집합도 별도로 열거하여 일치함을 확인했습니다.

| 현재 파일 집합 | 수 | SHA-256 aggregate |
|---|---:|---|
| 설치 소스 | 73 | `039501853cade59c4d05f448c85e8d50b71888d7d16e6e45e29b9bcaa6f7dbc7` |
| Python + Node 테스트 | 41 | `834097dae4a4160f74ffc69488be681869769c1937a79b63de53e7de0206392c` |
| 최종 공개 문서·갤러리 | 183 | `d6f164db0e3fa470aff3798db251cef299f43792e89fda61b3b09abbd5d8f409` |

독립 CLI 실행 당시 T3 이후 기존 소스 변경은 비교 템플릿 1개, 공개 변경은 README 두 개와 생성 index 1개뿐이었고 당시 public aggregate는 `0cf9433aa0004f0a274e77c7e628683cb33795151a7664b221a6eec025c67abe`였습니다. 기존 40 Python 테스트는 동일하며 Node `.mjs` 1개가 추가되었습니다. 현재 템플릿 `2e9760669f0aa2d9d34267fce0241452f43de435c9c4985bce80be70afb309a3`와 Node 테스트 `dba7111715f09b11af3f68b33a03f079451db72fc8a98345fe67200e759d4a3e`는 복원 후속 기록과 일치합니다. README는 3+3 배치 후속 해시와 일치합니다.

정리 후 최종 점검은 `hash changed current_public_docs_snapshot`으로 승인된 후속 문서 변경을 감지했습니다. 조정자의 `msg_7a7310608de5`에 따라 `docs/releases.md` 전체와 정확한 diff를 읽었습니다. 현재 source/cache 예시만 0.6.0으로 갱신되고 published 0.3.1·미공개 0.4.0 실패 기록·별도 게시 승인은 유지됩니다. 이전 297개 파일 중 이 문서 하나만 추가 변경되었으며 SHA는 `e3f6aa8d31b7356bb3440e71c8dbda5720bff50a4cd5546bcdbffa006d354f35`입니다. 새 `final-bindings.json` SHA `df6c741906d3df829f387d9e6c1a6c2a753e2c6e219d154504f636f15a221337`와 모든 73/41/183 파일 및 aggregate를 다시 독립 확인했습니다. 위 표는 이 최종 binding이며, JSON은 CLI 당시와 최종 두 기록을 모두 보존합니다. 실행 코드·테스트·원본은 변하지 않아 CLI나 전체 suite를 반복하지 않았습니다.

기존 증거 재사용을 새 실행과 구분합니다. [T3](integration.json)의 622개 pytest 및 Ruff/format/basedpyright/lock PASS, [복원 후속](browser-restoration.json)의 58개 Python 및 `node --test tests/comparison_browser_restoration.test.mjs` 6개 PASS를 재사용했으며 전체 테스트를 다시 실행하지 않았습니다. [설치 후속](installation-followup.json)의 현재 캐시/개인 payload는 모든 비-manifest 소스 해시가 현재 소스와 일치하며 기록된 설치 버전은 `0.6.0+codex.20260913005849`입니다. 이 검토에서 설치하거나 캐시를 다시 실행하지 않았습니다. 기준 커밋 대비 의존성/lock 변경은 자체 프로젝트 버전뿐이며 타사 22개 패키지 기록은 동일합니다.

## 실제 CLI 및 HTTP

공개 스냅샷의 `state`와 연결된 원본을 전용 임시 루트에 복원했습니다. 6개 세션을 실제 `show`로 각각 두 번 확인했고 모든 상태가 스냅샷과 같습니다. 아래 명령은 실제 실행한 최종 argv입니다.

```sh
uv run python skills/logo-land/scripts/logo_project.py --help
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-review-security compare-gallery --selection-file /tmp/ll-060-review-security/inputs/valid.json --output gallery
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8797/gallery/index.html
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8797/gallery/images/008.png
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8797/gallery/prompts/008.txt
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8797/gallery/images/002.png
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8797/gallery/prompts/002.txt
```

Helper 종료 0, `{"path":"gallery","index_path":"gallery/index.html","count":8}`. 생성 18개 파일이 현재 공개 갤러리와 바이트 단위로 같습니다. HTTP는 종료 0, **HTTP/1.0 200 OK**, HTML 42,459바이트, 본문 SHA-256 `66e8ac8fd728f85a683ee041437a2a0fbe56a2f4b89902fb9eefc4c1d29610c6`입니다. 실제 HTML의 다운로드 링크에서 받은 파일은 각각 200이며 아래 원본·manifest 해시와 같습니다.

| 실제 식별자 | PNG SHA-256 | 정확한 prompt SHA-256 |
|---|---|---|
| common / v1 / r1 / brand | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` |
| drip / v1 / r1 / app_icon | `8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f` | `67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d` |

나머지 6개를 포함한 8개 원본·프롬프트도 공개 receipt, sample manifest, 복원 상태 및 생성 manifest와 독립 대조했습니다. private native 원본과 실제 호출의 관계는 소스에 연결된 T2/T3 기록을 재사용했습니다. 이 검토에서 native/API 호출은 0회입니다.

## 구체적 보안 시나리오와 9개 클래스

| 클래스 | 실제 결과 / 재사용 범위 |
|---|---|
| 1. Malformed input | 잘린 JSON, 중복 source, boolean revision, 추가 `approve` 키, `../common` session, 2,001자 note, 4 MiB+1 JSON 모두 종료 1·stdout 없음. 새 gallery/index 또는 staging 잔재 없음. title/1–60개 범위는 현재 해시에 연결된 기존 input/limit 테스트로 보완했습니다. |
| 2. Prompt injection / XSS | 모든 note에 `</textarea></title><script>…</script><img src=x onerror=…>`, 명령 치환·backtick 및 승인 강요 문장을 전달했습니다. 제목에도 닫는 태그를 넣었습니다. 출력은 종료 0이지만 text가 이스케이프되고 authored script는 1개이며 injected img/sentinel/승인 변경이 없습니다. 후속 지침도 note를 신뢰할 명령이나 승인으로 취급하지 않습니다. |
| 3. Cancel/resume | 6세션 × 2회 실제 show가 상태를 보존했습니다. 이미지/prompt/manifest/index 각각에서 두 번 취소 후 성공 재개하는 기존 `test_cancel_repeat_then_retry_removes_partial_publication` 4개 경우는 현재 해시와 T3/T4 PASS에 연결하여 재사용했습니다. |
| 4. Stale state | 실제 current revision 대신 0을 넣으면 `stale_revision`, 종료 1, 목적지 없음. staging 중 revision advance와 PNG tamper는 기존 `test_revision_advance_during_staging_fails_before_publish`, `test_source_tampering_during_copy_fails_without_publication` 증거를 재사용했습니다. 갤러리는 저장 스냅샷이며 모든 가능한 동시 파일 교체를 원자적으로 막는다고 주장하지 않습니다. |
| 5. Dirty workspace / path | `../escape`, 절대 경로, 내부 `..`, backslash, drive colon, `.git`, 대소문자 혼합 reserved 저장소, `.`를 실제 CLI로 거부했습니다. selection leaf·원본·상태·목적지·목적지 부모 symlink도 거부했습니다. 기존 출력은 conflict로 보존되며 foreign 디렉터리의 sentinel 바이트도 동일합니다. 취소 중 foreign inode 교체 보호는 기존 `test_foreign_replacement_survives_when_publication_is_cancelled` PASS를 재사용했습니다. |
| 6. Hung commands | helper 30초, curl 연결 3초/전체 20초/부모 25초, 서버 300초로 제한했습니다. 기록된 49개 명령의 최대 소요 시간은 0.714초 미만이며 timeout은 없습니다. 두 서버 모두 SIGTERM 후 reap했습니다. |
| 7. Flaky tests / tooling | 새 테스트 실패나 전체 suite 재시도 없음. 임시 collector의 문자열 인코딩 비교 오류를 아래에 원인·실패 그대로 보존했습니다. 제품 CLI를 재실행하지 않고 HTTP 후속만 진행했습니다. |
| 8. Misleading success | 종료 0만으로 통과시키지 않고 8개 식별자, 생성 18개 파일, HTTP 본문 및 원본/prompt 해시를 확인했습니다. 실제 export는 unselected에서 `not_selected`; 별도 선택 상태 fixture에서도 review 없음으로 `review_required`를 반환하고 아무 export도 만들지 않았습니다. 비교 fixture의 원본·선택·검토 상태는 불변입니다. |
| 9. Repeated interruptions | 계획한 반복 show/HTTP GET은 바이트와 식별자를 보존했습니다. 반복 publication 취소는 위의 해시 연결된 기존 증거 재사용입니다. 유료 native 작업 강제 중단, 설치 취소, 외부 공격은 이번 읽기 전용 검토에 해당하지 않아 N/A입니다. |

입력은 Pydantic strict/unknown-key 거부 및 길이 제한을 사용합니다. 일반 파일 읽기는 64 MiB, PNG 디코딩은 4천만 픽셀로 제한되며 정적 완전 PNG만 수용합니다. 경로는 정규화/containment 및 symlink 검사를 거치고 원본 해시·디코딩 사실을 다시 확인합니다. publisher는 배타적으로 파일을 연결하고 index를 마지막에 쓰며 rollback 시 device/inode가 같은 파일만 지웁니다. 템플릿의 JS는 고정 코드이고 동적 문자열이 JS/URL로 삽입되지 않습니다. CSP는 기본·연결·base·form을 차단하고 로컬 이미지 및 authored inline CSS/JS를 허용합니다. PNG 내부 C2PA 문자열이나 저장 prompt를 HTML로 실행하는 경로는 없습니다.

## 공개 자료와 출처 점검

자격 증명/개인키/토큰 패턴은 새 public/QA 텍스트 및 바이너리의 ASCII 범위에서 발견되지 않았습니다. 다만 QA의 실제 명령·스택·Chrome 파일 URL에는 **로컬 계정 경로가 보존되어 있습니다**. 이 메타데이터 노출은 조정자에게 `msg_da5bacb1469a`로 고지했습니다. 사용자 콘텐츠나 비밀 토큰으로 분류하지 않았으며, 보고서가 개인정보를 전혀 포함하지 않는다고 주장하지 않습니다. Downloads 및 최종 gallery 스크린샷을 직접 확인했고 해당 다운로드 화면은 이 작업의 네 항목으로 제한되어 있습니다. 모든 스크린샷에 대한 OCR 검사는 수행하지 않았습니다.

7개 native PNG 및 동일한 comparison 복사본에서 발견된 이메일 문자열은 `caBX` C2PA 서명 안의 **Trufo CA 연락처**이며, 주변 필드에 CA Division / Claim Signing CA / OpenAI Media Service가 기록되어 있습니다. 8개 전체는 `caBX`를 포함하고 원본 해시는 그대로입니다. 서명 메타데이터를 제거하거나 이를 새 모델 선택/보증 주장으로 사용하지 않았습니다. 인증서 신뢰 체인 검증은 수행하지 않았습니다.

IP 원저자 s1dashu 및 MIT 고지는 기준 커밋과 동일합니다. 네이티브 6 initial + 2 child와 모든 혼재·실패·불충분 관찰을 유지하고, gallery가 승인·실제 플랫폼 패키지·폰트 조판·모델/seed/정밀 보장으로 표시되지 않음을 확인했습니다. 소스 `0.6.0`은 unreleased이며 기존 공개 릴리스를 재게시하지 않았습니다.

## 도구 실패 기록과 정리 영수증

첫 HTTP 자체는 200 및 정확한 SHA였으나 Ruby `UTF-8`와 `ASCII-8BIT` 문자열을 그대로 비교하여 collector가 `FAIL: HTTP index exact 200`으로 종료했습니다. 잘림/잘못된 페이지 가설은 동일한 Content-Length와 public/generated/HTTP SHA로 배제했습니다. 같은 파일로 `UTF8 == binary → false`, `UTF8.b == binary → true`, 원래 비교 복귀 → false를 확인한 뒤 후속 collector에서 바이트 비교로 고쳤습니다. 첫 실패·stderr·서버 종료와 후속 200·4다운로드·반복 GET을 모두 JSON에 보존했습니다. 생산 소스나 테스트는 바꾸지 않았습니다. 추가 읽기 전용 receipt 요약에서는 array를 object로 취급한 일회성 TypeError가 있었고 파일/CLI 동작에 영향이 없었습니다.

등록 임시 루트 device/inode `16777230 / 35041746`을 제거 직전에 재확인했습니다. **73개 일반 파일, 2개 symlink, 32개 디렉터리(루트 포함)**를 항목별 inode/해시 또는 링크 대상 검증 후 제거했습니다. 전체 목록은 JSON에 있으며 foreign 파일은 제거하지 않았습니다.

- 서버 **29648**, 후속 서버 **32566**: 각각 SIGTERM(15) 후 reap; 현재 PID 없음.
- collector exec session **65859**: 종료 1인 초기 수집기 실패로 정착; **52743**: 후속 종료 0으로 정착. 두 스크립트 실행 프로세스가 없는 것을 `ps`로 재확인했습니다.
- 49개 명령 자식 PID와 등록 setup PID는 모두 종료됨을 확인했습니다. 정리 driver PID **36178**의 종료 확인은 최종 JSON에 기록됩니다.
- `lsof -nP -iTCP:8797 -sTCP:LISTEN`: 종료 1, 출력 없음; 동일 주소 bind 성공. `/tmp/ll-060-review-security` 없음.
- 원본·상태·입력, 73/41/183 해시 및 기존 후속 QA 해시 모두 일치합니다. source/docs/assets/config 변경 없이 이 보고서와 JSON만 남겼습니다. 브라우저·설치·사용자 최종 열린 갤러리는 조작하지 않았습니다.

**최종 보안 판정 PASS.** 실제 CLI/HTTP와 보안 거부·보존 동작은 확인됐으며, 재사용 증거와 미실행 범위는 위에 구분했습니다. 조정자의 T6 통합/전달은 별도 작업입니다.
