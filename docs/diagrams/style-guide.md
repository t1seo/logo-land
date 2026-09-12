# Logo Land 다이어그램 스타일

이 파일은 이 프로젝트의 다이어그램에만 적용합니다. 사용자가 승인한 아이보리·블랙 스킨이며, 설치된 스킬이나 공유 프로필은 수정하지 않습니다.

## 출처와 구성

- [diagram-design](https://github.com/cathrynlavery/diagram-design/tree/8d8b2993ee2256ee7dfc0eeb3b5713aba3b60792), MIT, skill version 2.6.
- 적용 지침: `SKILL.md`, `references/style-guide.md`, `references/semantic-patterns.md`, `references/type-data-flow.md`, `references/output-spec.md`, `references/export.md`, `assets/template.html`.
- 의미 패턴: **Unstructured input → structured artifact**. 짧은 요청에서 정확한 표기와 업종을 추출하고, 미정인 색상은 질문 대상으로 남깁니다.
- 유형: 가로 데이터 흐름. 사용자와 Codex의 대화 → 내장 이미지 생성·수정 → Codex의 육안 검수와 로컬 파일 도구의 검사·전달입니다.
- 크기: `doc-wide`, `viewBox="0 0 1280 720"`, 정적 HTML과 README용 SVG.
- 영문 원본: `workflow-en.html`, 한국어 원본: `workflow.html`. 각 언어의 README가 해당 SVG를 사용하며, 두 버전의 구조·역할·검수 범위는 같습니다.
- 입력과 브리프를 첫 단계 안의 두 노드로 표시합니다. 총 4개 노드, 4개 연결선, 1개 연결선 라벨입니다.
- 고정 프레임과 한글 가독성을 위해 예제의 작은 역할 행·숫자 칩 대신 단계별 역할 제목과 큰 노드를 사용합니다. 우측 검수 노드에서 중앙 이미지 도구로 돌아가는 점선은 선택안 수정입니다.
- 파일 보조 명령별 내부 단계와 8개 로고 유형은 README와 참조 문서에 둡니다.

## 색상

| 역할 | 값 | 용도 |
|---|---|---|
| paper | `#f6f3ec` | 페이지·SVG 배경, 라벨 마스크 |
| paper-2 | `#eeeadf` | 대화 입력 배경 |
| ink | `#191917` | 본문, 선, 검수 노드 |
| muted | `#5f5b52` | 보조 글자, 일반 연결선 |
| soft | `#69655b` | 부가 설명 |
| rule | `#d6d0c4` | 구분선 |
| rule-solid | `#aaa396` | 경계선 |
| accent | `#a64b32` | 이미지 생성 단계와 그 입력 연결선 |
| accent-tint | `#f0e3da` | 이미지 생성 노드 배경 |
| link | `#5f5b52` | 외부 연결용 예약 마커 |

색만으로 상태를 전달하지 않습니다. 단계명, 도구 역할, 실선·점선과 범례로 의미를 함께 표시합니다. 그림자, 그라디언트, 배경 패턴은 사용하지 않습니다.

## 서체와 배치

- 제목: `'Instrument Serif', 'Noto Serif KR', 'AppleMyungjo', 'Batang', serif`.
- 한글·사람이 읽는 이름: `'Geist', 'Noto Sans KR', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif`.
- 기술 식별자: `'Geist Mono', ui-monospace, monospace`.
- 외부 폰트 요청은 넣지 않습니다. 파일을 독립적으로 열거나 GitHub README의 이미지로 표시할 수 있도록 로컬 폴백을 사용합니다. 환경에 따라 글꼴 모양은 달라집니다.
- 제목 40px, 노드 제목 24–28px, 설명 20px, 역할·범례 16px. 한글은 12px 미만으로 줄이지 않습니다.
- 좌표·크기·글자 크기는 4px 격자, 외곽 여백은 최소 40px입니다.
- 연결선은 수평·수직 또는 반경 8px의 직각 곡선입니다. 연결선을 먼저 그리고 노드를 나중에 그립니다.
- 연결선 라벨은 불투명 paper 마스크를 두고 선과 8px 간격을 유지합니다.

## 내보내기

각 언어의 HTML이 원본입니다. 첫 번째 SVG 블록을 추출하고 XML 선언을 붙여 `workflow.svg`와 `workflow-en.svg`를 만듭니다. SVG 내부에 필요한 스타일을 포함하며 외부 참조, 스크립트, `foreignObject`, 외부 폰트는 없습니다. README는 해당 언어의 SVG를 이미지로 참조합니다. SVG는 문서의 흐름도이며 플러그인이 생성하는 로고의 출력 형식을 뜻하지 않습니다.

README의 제품 로고는 별도 생성된 `assets/logo.png`를 사용합니다. README의 네 가지 배지는 Codex 플러그인, Python 3.12 이상, PNG 출력, 영문·한국어 문서라는 사실만 표시하며 CI 결과나 라이선스를 나타내지 않습니다.
