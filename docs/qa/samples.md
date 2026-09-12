# Logo Land 샘플·브랜드 검증

검증일: 2026-09-12. [실행 계획](../../plans/logo-samples.md), [샘플 갤러리](../samples/index.html), [브랜드 제작 과정](../brand/README.md).

## 실제 이미지 생성과 전달

설치된 자체 플러그인으로 각 브리프와 프롬프트를 준비한 뒤 Codex 내장 이미지 도구를 **샘플 10회, 브랜드 1회** 호출했습니다. 각 반환 파일을 따로 가져와 선택·육안 검수·내보내기를 진행했습니다. 가상 브랜드의 샘플 방향은 사용자가 위임한 시연 범위에서 정했으며 사용자가 각 디자인을 승인했다고 기록하지 않았습니다.

샘플 10개는 8유형을 포함합니다. 워드마크와 조합형은 각각 2개이고 나머지는 1개씩입니다. 모든 샘플은 1254 × 1254 불투명 PNG이며 투명 픽셀은 0개입니다. 전용 LOGO LAND 로고는 1774 × 887 불투명 PNG입니다. 큰 원본과 실제 Chrome에서 샘플은 240 CSS px, 브랜드는 400 / 240 CSS px로 확인했습니다. 파비콘 크기·인쇄 검수는 포함하지 않았습니다.

각 세션의 초기화, 프롬프트, 가져오기, 선택, 검수, 내보내기 JSON을 `docs/samples/items/`와 `docs/brand/`에 보존했습니다. `generation.json`은 실제 native 도구의 반환 파일명과 해시를 연결합니다. 샘플 생성 플러그인은 `0.2.0+codex.20260912125753`, 브랜드 생성 플러그인은 `0.3.0+codex.20260912132222`입니다. 당시의 요청과 버전은 이름 변경 뒤에도 보존했습니다. `generatedAt`은 생성 파일을 등록한 시각이며 이미지 도구의 실행 시작 시각이 아닙니다.

Orca 독립 감사는 11개 PNG의 해시, ZIP CRC, ZIP 내부 PNG·manifest·가이드의 원본 바이트 일치, catalog/data.js 일치와 14개 문서·구현 계약을 확인했습니다. 발견된 옛 스킬 링크 3개를 수정했습니다. 배포용 과거 QA 사본의 개인 홈·계정 경로는 `<workspace>`, `<codex-home>`, `<plugin-sources>`로 표기했으며 원래 사본은 Git 제외 폴더에 보존했습니다. 이미지·ZIP·생성 프롬프트 자체는 변경하지 않았습니다.

수정 후 동일한 독립 감사 명령 5종을 다시 실행했습니다. [기계 검사 결과](samples/artifact-audit.json)에 11개 패키지·14개 계약·로컬 참조 770개·명백한 credential 패턴 검사 PASS를 보존했습니다. 개인 홈 경로 적중은 0개입니다. 과거 QA의 임시 경로는 실행 증거로 남겼습니다.

## Chrome Computer Use

외부 Google Chrome을 Codex Computer Use의 native Sky 연결로 조작했습니다. jsdom 검사를 실제 브라우저 검사로 서술하지 않았습니다.

| 시나리오 | 실제 결과 |
|---|---|
| `file://` 갤러리 | 실제 PNG 카드 10개, 최종 Logo Land 이름과 `$logo-land` 안내 표시 |
| 필터 9개 | 전체 10 / 워드마크 2 / 조합형 2 / 나머지 6유형 각 1개 |
| 고요 상세 | 큰 PNG, 원래 요청, 실제 프롬프트 펼치기, 검수 기록·크기·해시·등록 시각 표시 |
| 키보드 | Escape로 닫고 고요 카드에 초점 복귀, Enter로 다시 열기 확인 |
| ZIP 클릭 | Chrome 다운로드 완료. 받은 ZIP SHA-256이 원본과 일치 |
| 390 × 844 장치 모드 | 단일 열 목록, 줄바꿈되는 필터, LUMA 상세 세로 배치·스크롤·다운로드 버튼 확인 |
| README 도식 | 영어·한국어 HTML의 실제 렌더링에서 텍스트·화살표·여백 확인 |

다운로드한 고요 ZIP의 SHA-256: `328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7`.

역방향 Shift+Tab에서는 Chrome 접근성 트리에 초점이 보고되지 않아 완전한 초점 순환을 검증했다고 주장하지 않습니다. DevTools에 `file:` 고유 origin 관련 메시지 1건이 있었으며 원인은 확정하지 않았습니다. 위 이미지·필터·상세·다운로드 시나리오는 실제로 동작했습니다. 브라우저의 보안 설정은 변경하지 않았습니다.

[축소 샘플](samples/small-size-chrome.jpeg) · [브랜드 축소](samples/brand-small-size.jpeg) · [ZIP 다운로드](samples/gallery-download.jpeg) · [모바일 목록](samples/gallery-mobile.jpeg) · [모바일 상세](samples/gallery-mobile-detail.jpeg) · [모바일 다운로드](samples/gallery-mobile-downloads.jpeg) · [영문 흐름도](samples/workflow-en.jpeg) · [한국어 흐름도](samples/workflow-ko.jpeg)

## 자동 검사와 설치

- 최종 `logo-land` 경로로 변경 후 `uv run --locked pytest -q`: **96 passed in 38.39s**.
- Ruff: 통과. basedpyright: 오류 0개, 경고 0개.
- 플러그인 manifest 검증과 skill quick_validate: 통과. 스킬 검사 도구의 PyYAML은 `uv run --with pyyaml`로 임시 제공했습니다.
- diagram-design의 두 HTML self_check·geometry·XML·SVG 일치 검사: [기록](../diagrams/validation.md).
- 최초 UI의 다섯 독립 검토, 403개 DOM 단언과 중간 이름 변경 후 73개 단언: [범위별 기록](samples/gallery-review.md).
- 전용 로고를 포함한 최종 설치 `logo-land@personal`, 버전 `0.3.0+codex.20260912133131` 성공. 해당 캐시의 helper로 브랜드 세션 revision 4를 다시 읽었습니다.

스테이징 후 공백 검사에서는 보존된 전달 가이드의 빈 문구 뒤 공백과 연구 Markdown의 의도적인 줄바꿈 공백만 보고됐습니다. ZIP·가이드의 바이트 일치를 유지하기 위해 해당 원본은 바꾸지 않았으며, 두 종류의 문서를 제외한 `git diff --cached --check`는 통과했습니다.

최종 설치본의 신규 GUI 대화 자동 발견과 Windows/Linux 실행은 확인하지 않았습니다. 새 대화에서 `$logo-land`로 시작하실 수 있습니다.

## 저장소 반영과 화면 표시

GitHub 저장소를 `t1seo/logo-land`로 변경했으며 기존 비공개 설정과 기본 브랜치 `main`을 유지했습니다. 구현·샘플·문서를 담은 `04e10ac0970e9b2911d3af6e18e2eb4f67a249b7`을 일반 `main` 푸시로 반영한 뒤 `git ls-remote origin refs/heads/main`과 로컬 HEAD의 일치를 확인했습니다.

푸시 후 최종 샘플 HTML을 Chrome에 열었습니다. 마지막 표시 단계에서는 Computer Use의 주소 타이핑 누락과 다른 탭으로 바뀌는 상황이 있어 macOS `open -a 'Google Chrome' docs/samples/index.html`로 파일을 열었으며, 이어서 Computer Use가 `Logo Land (로고랜드) — 로고 샘플 아카이브` 창 제목을 반환했습니다. 이 마지막 조회에는 스크린샷이 제공되지 않았으므로 앞서 완료한 Chrome 화면 검수와 구분합니다.
