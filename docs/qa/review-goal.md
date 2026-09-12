# 목표·제약 독립 검토

검토일: 2026-09-12. Orca Task `task_cb289d03f916`, Dispatch `ctx_e1e11736009b`입니다. 이 작업자는 이 문서와 `/tmp/logo-goal-qa.4MrplD/`만 작성합니다. 구현과 원래 `morrow-live` 세션은 읽기 전용으로 취급했습니다.

**판정: PASS.** 핵심 로고 제작·파일 전달 및 검토 시점에 완료된 수용 기준에서 차단 결함은 발견하지 않았습니다. 계획 4번의 독립 스킬 도구 부재 시나리오는 설치 캐시를 사용한 S25/S30의 실제 명령·종료 코드·상태 기록으로 확인했습니다. 코디네이터가 진행 중인 Chrome 추가 조사·색인 마무리는 아래 R03의 PARTIAL로 남기며, 이 판정이 그 작업까지 완료됐다는 뜻은 아닙니다.

## 기준과 증거 수준

사용자 요구는 조정자가 제공한 `/tmp/logo-review-context.txt`, [확정 계획](../../plans/logo-generator.md), [요구사항 초안](../../.omo/drafts/logo-generator.md)에서 교차 확인했습니다. 원래 사용자 대화 전체를 직접 열람했다고 주장하지 않습니다. [설계 검토](../planning/gap-analysis.md), [제품 스킬](../../skills/logo-land/SKILL.md), 네 개 참조 문서, manifest, README, 공식 기능 조사·비교표·실사용 보고서·실제 이미지 QA를 읽었습니다. 현행 호스트의 이미지 도구 스키마와 버전 일치 Orca orchestration 가이드도 대조했습니다.

ACHIEVED는 해당 기준의 구현 또는 실행 증거가 있다는 뜻입니다. PARTIAL은 범위를 구분해야 하거나 예정된 검증이 남았다는 뜻이며, MISSED는 필요한 구현·자료가 없다는 뜻입니다. 스킬의 지침, 다른 작업자의 실행 기록, 이 검토자의 직접 실행을 구분합니다. 경쟁사 유료 파일 구매, 다섯 서비스의 전체 유료 기능 실행, 별도 웹 앱 구현은 사용자 요구에 추가하지 않습니다.

## 요구사항별 판정

| ID | 요구사항·수용 기준 | 상태 | 구체적 근거와 범위 |
|---|---|---|---|
| R01 | Looka·Brandmark·Tailor Brands·Fiverr Logo Maker·Design.com의 제작 방법·유형·기능 조사 | ACHIEVED | [공식 조사](../research/official-features.md)에 다섯 서비스별 생성 진입, 입력, 편집, 유형, 파일·계정·유료 경계가 있습니다. [출처 목록](../research/sources.json)은 실제 67건이며 본문 확인 61건, 본문 미추출 3건, 404 색인 2건, 열기 오류 색인 1건을 구분합니다. |
| R02 | 실제 브라우저 조작과 단계별 스크린샷을 docs에 저장 | ACHIEVED | [캡처 원장](../research/captures.jsonl)의 중간 스냅샷 131건을 집계했고 중복 slug가 없으며 모든 screenshot·snapshot 대상 파일이 존재했습니다. 다섯 서비스의 대표 실제 이미지를 직접 열었습니다. 추가 캡처에 따라 총수는 증가할 수 있습니다. |
| R03 | 사용자 지정 Chrome + Codex Computer Use로 후속 조사 | PARTIAL | [Chrome 추가 조사](../research/chrome-followup.md)에 Design.com AI 수정·상품 선택, Fiverr 편집·한글 확인이 있습니다. Tailor의 후속 생성 캡처도 추가되는 중이며 Looka·Brandmark 후속 경계와 최종 문서화는 코디네이터 진행 범위입니다. |
| R04 | 주요 제작 분기와 조사 한계를 정직하게 구분 | ACHIEVED | Brandmark 새 앱·v3·템플릿·빈 캔버스·로그인 필요 아이콘 생성, Tailor 세 유형과 아이콘 검색/도형 분기, Design.com 무료 카탈로그와 AI 편집, Fiverr 디자이너 매칭을 구분했습니다. 파일명보다 실제 화면을 우선하며 유료 출력·미실행 제어를 성공으로 서술하지 않습니다. |
| R05 | 조사 결과를 플러그인 설계에 반영 | ACHIEVED | [비교표](../research/comparison.md)가 단계적 브리프, 유형/스타일 구분, 개별 시안, 선택안 수정, 정확한 문구, 배경·크기 검수로 연결합니다. 경쟁사 화면·템플릿을 생성 로고 에셋으로 복사하지 않습니다. |
| R06 | 구현 전에 계획과 책임 경계를 수립 | ACHIEVED | [계획](../../plans/logo-generator.md)의 의존성·소유권·QA와 [갭 분석](../planning/gap-analysis.md)이 존재합니다. 진행 체크박스 갱신은 코디네이터의 마지막 문서 정리 항목입니다. |
| R07 | 대화형 Codex 플러그인을 실제 구현 | ACHIEVED | `.codex-plugin/plugin.json` v0.2.0, 스킬 frontmatter, `agents/openai.yaml`, 예제 브리프, 독립 helper가 있습니다. README에서 호출·재개·사용 요건을 설명합니다. 설치 후 자동 발견까지 이 항목이 증명하지는 않습니다. |
| R08 | 대화에서 브리프를 수집하고 불필요한 반복 질문을 피함 | ACHIEVED | 스킬은 기존 입력 재사용, 중요한 누락만 질문, 명시적 생성·수정 요청을 권한으로 해석합니다. 완성 브리프·가이드·참조·탐색·수정 경로를 구분합니다. 모든 대화 표현을 실행 평가한 것은 아닙니다. |
| R09 | 실제 로고는 native imagegen으로 생성 | ACHIEVED | [실제 QA](live/README.md), A/B 별도 PNG와 최종 프롬프트, 부모 참조 수정본이 있습니다. helper 도움말도 이미지 API를 호출하지 않는다고 표시합니다. 이 작업자는 이미 생성된 파일을 재사용했으며 새 이미지 호출을 했다고 주장하지 않습니다. |
| R10 | 로고 유형·스타일·요청 시안 수 지원 | ACHIEVED | [유형 계약](../../skills/logo-land/references/logo-directions.md)에 8가지 유형과 별도 스타일 축이 있습니다. 기본 3개는 사용자 지정 수로 대체하며 실제 QA는 2개입니다. helper 보고서는 24개 요청 보존 회귀 검사를 기록합니다. 8유형 모두의 실제 시각 품질을 검증했다는 뜻은 아닙니다. |
| R11 | 개별 시안 비교·선택·정확한 참조 수정·원본 보존 | ACHIEVED | A-v1/B-v1은 별도 이미지이며 A-v2의 parent는 A-v1입니다. [원본 비교 화면](live/chrome-visual-qa.jpeg)을 직접 열었고, 임시 세션에서 동일한 실제 이미지의 가져오기·선택·부모 관계를 재확인했습니다. |
| R12 | 저장된 작업의 재개·이력·실패 보존 | ACHIEVED | [최종 재개 기록](live/resume-final.json)은 revision 7과 A-v2 선택을 보존합니다. 별도 CLI 프로세스에서 제 임시 세션도 재개했고, 실패 기록 추가 후 원본 3개·부모·선택·기존 export가 유지됐습니다. 설치된 플러그인의 새 대화 발견은 별도 범위입니다. |
| R13 | 실제 PNG 검사·시각 검수·최종 파일 전달 | ACHIEVED | 최종 PNG는 1254×1254이고 alpha 255입니다. 선택 PNG의 실제 SHA-256 및 ZIP 세 항목을 직접 재확인했습니다. 큰 원본·256px/48px 비교 화면에서 정확한 Morrow Studio 문구, 여백, 작은 크기 한계를 확인했습니다. |
| R14 | 버전별 배경 변형과 최신 요청 우선 | ACHIEVED | [배경 변형 QA](background-variants.md)는 opaque↔transparent 양방향, 기본값, legacy null/missing, 선택 버전별 export를 검증합니다. [실행 계약](../../skills/logo-land/references/project-files.md)은 기본값이 부모가 아닌 초기 브리프임을 명시합니다. |
| R15 | 자동 검사와 독립 실사용 검증 | ACHIEVED | helper·배경 변형 보고서의 84개 테스트 checkpoint와 Ruff·basedpyright·lock 증거가 있으며 독립 QA도 전체 84개를 다시 통과했습니다. 이 작업자는 별도의 CLI 정상 흐름과 8개 오류를 직접 실행했습니다. 후속 예약 출력 경로 수정 뒤의 최종 검사 수는 코디네이터가 갱신하며, 전체 테스트를 이 검토자가 재실행했다고 주장하지 않습니다. |
| R16 | 도구가 없는 환경에서 독립 스킬 실행 | ACHIEVED | 독립 QA 작업자의 설치 캐시 기반 S25/S30 실행 스크립트·exit 원장·상태 결과를 직접 대조했습니다. 완성 한글 요청은 이미지 없는 브리프로 보존됐고 기존 수정은 선택 A-v2·원본 3개·전달 2개를 유지했습니다. capability를 의도적으로 제외한 통제 시나리오이며 실제 호스트 장애 재현이나 신규 생성 성공을 주장하지 않습니다. |
| R17 | 설치 가능한 패키지와 최종 안내 | ACHIEVED | [설치 기록](installation.md)에 `codex plugin add logo-generator@personal --json` 성공과 캐시 위치가 있습니다. `dist/logo-generator-0.2.0.zip`의 29개 항목에 연구·세션·가상환경이 없고 `unzip -t`도 직접 통과했습니다. 새 GUI 대화에서 스킬 자동 발견은 미검증으로 명시합니다. |

## 제약 검토

| 제약 | 판정·근거 |
|---|---|
| Orca orchestration 사용 | ACHIEVED. 이 작업은 유효한 Task/Dispatch로 실행하며, `orca status --json`에서 연결된 1.4.198 런타임을 확인했습니다. 조정자에게 CLI status·heartbeat·escalation으로만 전달했습니다. |
| 존댓말과 한국어 설명 | ACHIEVED. 사용자용 README·주요 문서는 한국어 존댓말이며, 이 검토도 동일하게 작성했습니다. 내부 스킬의 영어 지침은 사용자 대화의 말투를 대체하지 않습니다. |
| 허용된 Chrome·Google 로그인 범위 | ACHIEVED인 권한 경계입니다. 사용자 승인 자체는 기록되어 있고, 이 작업자는 브라우저·계정을 조작하지 않았습니다. 모든 사이트 회원가입 성공을 별도 의무로 만들지 않습니다. |
| 구매·게시·커밋 없음 | 관찰한 기록과 작업 범위에서 위반이 없습니다. 가격 선택과 결제를 구분하며, 이 작업자는 어떤 계정·게시·git mutation도 실행하지 않았습니다. 전체 외부 계정의 모든 행동을 독립 감사한 것은 아닙니다. |
| native imagegen과 helper의 역할 분리 | ACHIEVED. live 도구 인자는 prompt와 두 참조 방식이며, 코드가 아니라 호스트가 이미지를 생성하도록 계약되어 있습니다. 별도 API 키 요구나 숨은 fallback 계약이 없습니다. |
| 정확한 참조와 원본 보존 | ACHIEVED. 로컬 이미지 사전 열람, 두 참조 방식의 상호 배타, 누락 이미지 재요청, 안정적인 parent/ID, 신규 버전 보존이 문서에 있습니다. 혼합 첨부·5개 초과는 계약 검토 범위이며 실제 호출 QA 범위는 아닙니다. |
| 설치 캐시에 사용자 데이터 저장 금지 | ACHIEVED. 제 임시 한글·공백 workspace에만 세션과 전달 파일이 생겼습니다. root의 `morrow-live`는 변하지 않았습니다. |
| 벡터·폰트·권리 과장 금지 | ACHIEVED. 래스터 PNG와 편집 가능한 SVG/EPS/AI·폰트·상표/독점권을 구분합니다. 실제 무료 PNG를 경쟁사 유료 벡터 다운로드 증거로 취급하지 않습니다. |
| 시각 검수 자동 승인 금지 | ACHIEVED. 실제 최종 검수에 구체적인 관찰과 48px·곡률·미세 색조 한계가 있습니다. 제가 임시 세션에 등록한 검수도 실제 PNG와 비교 화면을 본 후 작성했습니다. |
| 공유 작업 보존·소유권 | ACHIEVED. 본 보고서와 임시 QA 파일만 작성했습니다. 다른 리뷰어의 문서·구현·브라우저·원본 세션을 변경하지 않았으며 하위 작업자도 실행하지 않았습니다. |

## 직접 확인한 대표 워크플로

공통 실행은 `uv run --no-sync --project <repo> python <repo>/skills/logo-generator/scripts/logo_project.py --workspace '/tmp/logo-goal-qa.4MrplD/workspace 한글' ...`입니다. workspace는 계약대로 먼저 존재해야 합니다. 처음 미존재 폴더로 init을 시도했을 때 ENOENT가 반환됐고, 해당 임시 폴더를 만든 뒤 실행했습니다.

| 흐름 | 실행·결과 | 증거 |
|---|---|---|
| W1. 완성 브리프에서 개별 시안·참조 수정·전달 | init 0 → A-v1 import 1 → B-v1 import 2 → A-v1 선택 3 → 실제 A-v2를 A-v1 부모로 import 4 → A-v2 선택 5 → 실제 시각 검수 6 → export 7. 정상 종료했습니다. | 임시 `run-workflows.zsh`, 단계별 JSON, `export.json`; 실제 생성 자체는 [live QA](live/README.md)의 증거입니다. |
| W2. 기존 작업 재개 후 다음 수정 준비 | 별도 show에서 revision 7·선택 A-v2·원본 세 개가 복구됐습니다. `prompt --parent a-v2 --changes ...`가 해당 workspace의 정확한 부모 경로와 최신 요청을 반환했습니다. prompt는 새 이미지를 만들지 않았습니다. | 임시 `resume.json`, `prompt.json` |
| W3. 생성 도구 실패를 기록하고 정상 작업 보존 | 명시적으로 모의 실패라고 표시한 `failure --parent a-v2` 후 revision 8, failures 1, artifacts 3, selected A-v2, exports 1을 새 프로세스에서 확인했습니다. 이것은 CLI 실패 보존 검증이며 실제 도구 오류나 독립 스킬 실행을 가장하지 않습니다. | 임시 `failure.json`, `resume-after-failure.json` |
| W4. 원본 PNG·ZIP 사용 | 전달 PNG를 원래 A-v2와 cmp로 비교하여 동일 바이트를 확인했습니다. `unzip -t`의 logo.png, manifest.json, brand-guide.md가 모두 OK였습니다. | 임시 전달 폴더와 기존 [전달 ZIP](live/delivery/logo-package.zip) |

## 직접 확인한 경계 사례

다음 7개는 현재 revision 8인 임시 세션에 CLI 명령으로 실행했습니다. `run-edges.zsh`와 각 `.err`가 임시 작업 폴더에 있습니다. 여섯 변경 요청 전후 session.json이 `cmp`로 동일했고, 파일 변조 검사 후 임시 원본을 복구하자 show가 다시 성공했습니다.

| 사례 | 실제 결과 |
|---|---|
| E1. 없는 시안 선택 | `not_found: Artifact 'nonexistent' does not exist` |
| E2. 오래된 revision으로 선택 | `stale_revision: Expected revision 7; current revision is 8` |
| E3. 같은 artifact ID 재가져오기 | `conflict: Artifact a-v1 already exists` |
| E4. 없는 부모를 지정한 수정본 | `not_found: Artifact 'nonexistent' does not exist`; 신규 child가 등록되지 않았습니다. |
| E5. workspace 밖으로 export | `unsafe_path: Paths must remain relative to the workspace` |
| E6. 기존 전달 경로 덮어쓰기 | `conflict: Export destination already exists` |
| E7. 저장된 이미지가 다른 실제 PNG로 바뀜 | `hash_mismatch: Artifact a-v2 changed; restore its original file`; 임시 사본 복구 후 재개가 성공했습니다. |
| E8. 시각 검수가 없는 최종 export | 별도 `unreviewed` 세션의 revision 2에서 `review_required: All explicit visual review checks must pass`; stderr에 JSON 오류가 기록되고 state와 출력 경로가 보존됐습니다. |

E8은 별도 `run-review-gate.zsh`와 `unreviewed-export.err`에 기록했습니다. 기존 `live/export-before-review.json`은 stdout을 받은 빈 파일이라 오류 JSON 근거로 사용하지 않습니다. 기존 실행 설명은 [live QA](live/README.md)에 있으며, 이번 별도 실행에서는 stderr까지 직접 확인했습니다.

추가 문서 증거로 배경 불일치·투명↔불투명은 [배경 변형 QA](background-variants.md), 위장·절단 PNG·APNG·모든 픽셀 투명·상태 손상·잠금·rollback은 [helper QA](helper-tests.md)에 있습니다. 이 추가 사례를 제가 직접 재실행한 8개에 합산하지 않습니다.

## 이미지·연구 근거에 대한 독립 관찰

- Looka 편집기 화면에는 실제 로고 캔버스, Name/Slogan/Symbol/Container와 배치·팔레트·다운로드가 표시됩니다. 메뉴 존재가 모든 값을 변경했다는 증거는 아닙니다.
- Brandmark 새 앱 화면에서 잎 아이콘과 Morrow Studio가 나란히 배치됐습니다. HEX 시도 실패와 견본 클릭 성공이 별도로 기록되어 있습니다.
- Tailor 공개 결과에는 가입 오버레이가 있으므로 뒤에 보이는 후보·Customize를 편집 완료로 판정할 수 없습니다. 이후 Chrome 보완은 별도 자료로 누적되고 있습니다.
- Fiverr Chrome 화면에서 Noto Sans KR와 `모로 스튜디오`의 실제 캔버스 렌더링을 확인했습니다. 이것은 해당 문구·폰트의 성공이며 전체 한글·SVG 검증으로 확대할 수 없습니다.
- Design.com Chrome 화면에는 AI 수정 응답과 짙은 녹색 아이콘·MORROW STUDIO가 있습니다. 응답의 흰 배경 주장은 편집기 화면 관찰 수준이며 실제 유료 PNG alpha 확인을 의미하지 않습니다.
- 실제 A-v2는 정확한 Morrow Studio 문구와 M 형상을 보여 줍니다. 원본과 다른 내부 곡률·미세한 질감이 있으므로 픽셀 단위 보존, 완전한 단색 도형 또는 벡터 품질을 보증할 수 없습니다. 기존 QA도 이 한계를 명시합니다.

확인한 원래 최종 PNG와 전달 PNG의 SHA-256은 모두 `666eb20feaf67ee3bc4a1c879f5c551a55998bf2b257d5e52c0b142e599ab519`입니다. root 세션 JSON은 기존 기록과 같은 `43a38d8e69378d40ed2ef4a9b471cda137dbd34821f1d2667f9c1e65523e901d`를 유지했습니다.

## 조정자에게 전달한 보완 항목

1. **해결: 계획 4번의 독립 스킬 도구 부재 증거.** 최초에는 helper failure fixture만 확인되어 보완 요청을 보냈습니다. 이후 설치 캐시를 사용한 S25/S30 실제 기록을 직접 읽어 브리프·부모·이전 출력 보존과 가짜 이미지 없음이 확인됐습니다. 초기 Orca 전달은 `msg_7eecb04a169f`, `msg_01ec79fe2c78`, `msg_eff82ff12af3`이며, 최종 판정에서는 열린 blocker로 남기지 않습니다.
2. **예정된 전달 작업:** Chrome 잔여 결과를 조사 문서에 연결하고, 진행표·계획 체크박스·최종 검사 수를 마지막 상태에 맞춰 주세요. 패키지의 연구·사용자 세션·캐시 제외와 개인 등록은 이후 증거로 확인했습니다. 설치되는 파일을 추가 변경하시면 최종 패키지·설치 사본에도 반영해 주세요. 이는 이미 조정자가 수행 중인 단계이며 새 구현 결함은 아닙니다.

## 알려진 비차단 사항

- [설치 기록](installation.md)에 따르면 전체 `codex plugin list --json`은 기존 별도 astral-codex marketplace 오류로 실패합니다. 개인 플러그인 추가 성공과 구분되며, 관련 없는 설정을 바꾸라는 요구를 추가하지 않습니다. GUI 새 대화 발견도 미검증입니다.
- [코드 검토](review-code.md)는 사용자가 `.logo-generator/locks/<session>.lock/` 내부를 export 경로로 명시했을 때 저장 후 잠금 해제 오류가 발생하는 MINOR 사례를 재현했습니다. 제 8개 경계 사례에는 이 예약 영역 충돌이 포함되지 않으므로 이를 제 테스트가 방지한다고 주장하지 않습니다. 기본 출력·일반 workspace 상대 출력에서는 관측되지 않은 문제이며 구체적인 보완은 코드 검토의 담당 조정자에게 전달되어 있습니다.

## 독립 스킬 부재 시나리오의 확정 근거

다른 QA 작업자가 소유한 `/tmp/logo-review-qa.WDcBwx/run-installed.sh`, `exits.tsv`, `inputs/korean-request.txt`, `logs/S25j.stdout`, `logs/S30d.stdout`, `logs/S30f.stdout`을 읽었습니다. 제가 이 명령들을 다시 실행하거나 해당 workspace를 수정하지 않았습니다.

- 새 생성 S25e–S25m의 expected/actual exit가 전부 0입니다. 명시적 한국어 완성 요청을 설치 스킬 흐름으로 파싱하고 두 콘셉트 프롬프트를 보존했습니다. `goyo`의 exact text는 `고요 스튜디오`, concept count 2, revision 1, artifacts 0, exports 0, failures 1입니다. failure 이유는 실제 도구 실패가 아닌 capability 제외 QA임을 명시합니다. 이미지 폴더·출력 폴더 없음도 실제 shell 검사가 통과했습니다.
- 기존 수정 S30d–S30h의 expected/actual exit도 전부 0입니다. 부모 경로는 해당 workspace의 `a-v2.png`이며, 한글 수정 요구를 반영한 프롬프트 뒤에 모의 도구 부재만 기록했습니다. revision 13, selected A-v2, artifacts 3, exports 2, 마지막 failure parent A-v2가 유지됐고 원본 cmp도 통과했습니다.
- 설치 캐시와 실제 배포 ZIP을 서로 다른 위치에서 사용한 S26d–S26i도 전부 exit 0입니다. 원래 사용자 workspace를 읽고 재배치된 workspace의 부모 경로를 반환했으며 설치 캐시·패키지 안에 사용자 `.logo-generator`가 생기지 않았습니다.

이는 독립 검토자가 설치된 스킬 절차를 제한된 capability 조건으로 실행한 증거입니다. 도구를 실제로 제거한 새로운 GUI 세션이나 이미지 서버 장애 주입 실험은 아닙니다. [실사용 QA 보고서](review-qa.md)의 `Independent installed-skill execution` 절에 실제 한국어 응답 두 개도 기록되었으며, 생성하지 못한 사실과 보존한 내용을 정확히 설명함을 확인했습니다.

같은 QA 보고서의 `Actual host-call provenance audit`는 별도 허가받은 원래 도구 호출 세 쌍을 확인하여, A/B의 참조 없는 독립 호출과 A-v1을 참조한 A-v2 편집 호출을 구분합니다. 실제 반환 base64의 해시가 저장된 PNG와 일치한다는 독립 검증이 추가되었습니다. 이 작업자는 해당 보고서를 확인했으며 원래 rollout 전체를 직접 읽거나 인증 정보를 열람하지 않았습니다.

검증 신뢰도는 핵심 파일·세션 동작과 원본 보존에 높음, 실제 native 생성 출처와 연구 조작 이력에는 제공된 1차 캡처·프롬프트·조정자 실행 기록에 근거한 높음입니다. 전 제품 유형·임의 참조 조합·모든 호스트·운영체제에 대한 일반화는 하지 않습니다.
