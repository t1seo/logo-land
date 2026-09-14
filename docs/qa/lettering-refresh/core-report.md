# Lettering-first 로고 지원: 구현 및 검증 기록

기존 여덟 가지 로고 유형과 저장 형식을 유지하면서, 글자 중심 로고의 제작 지침과
유형별 Python 프롬프트를 보강했습니다. 새 프리셋·필드·외부 생성 API는 추가하지
않았으며, 이 작업에서는 실제 로고 이미지를 생성하거나 수정하지 않았습니다.

## 변경 내용

- `skills/logo-land/references/lettering.md`를 추가했습니다. 한국어·영어 요청을
  워드마크, 구분해서 읽는 레터마크, 획을 통합하는 모노그램, 심볼 결합 로고로
  연결하며, 통통한 다색 입체 글자·앞으로 기울어진 스포츠 글자·기하학적 적층
  이니셜을 실제 획·속공간·자간·연결부 결정으로 구체화합니다.
- `skills/logo-land/SKILL.md`와 `references/logo-directions.md`, `typography.md`,
  `delivery-checks.md`에 해당 안내를 연결했습니다. 정확한 글자·대소문자·공백·한글,
  작은 크기와 단색 실루엣의 점검을 설명하며, 실제 단색 결과물의 검증과 구분합니다.
- `scripts/logo_helper/logo_prompts.py`는 기존 `LogoType` 여덟 값을 분기합니다.
  워드마크에는 별도 심볼을 붙이지 않으며, 입체·스포츠 처리는 사용자가 해당 스타일을
  요청했을 때만 적용하도록 안내합니다. `styles`와 `concept`는 그대로 전달합니다.
- `scripts/logo_helper/prompts.py`는 새 생성에서만 유형별 제작 지침을 적용합니다.
  수정 작업의 초기 유형·문자열·스타일은 이력으로 표시하고, 선택한 부모 이미지와
  최신 수정 요청을 우선합니다. 실제로 저장된 심볼/문자 배치가 있으면 초기
  `wordmark` 라벨로 되돌리지 않습니다. 앱 아이콘의 전용 분기는 유지했습니다.
- `tests/test_lettering_prompts.py`에 20개 검증 사례를 추가했습니다. 기존
  `tests/test_app_icon_compatibility.py`의 일반 로고 문구 전체 스냅샷 비교는
  세션·원본 바이트·리비전·실제 적용 의도를 확인하는 검사로 바꾸었습니다.
  과거 저장 프롬프트나 문서의 스냅샷 파일은 변경하지 않았습니다.

## 검증 결과

| 명령 | 결과 |
|---|---|
| `uv run pytest -q tests/test_lettering_prompts.py tests/test_cli_workflow.py tests/test_app_icon_prompts.py tests/test_app_icon_compatibility.py tests/test_lockup_continuity.py tests/test_palette_workflow.py tests/test_background_variants.py` | **65 passed**, 50.50초 |
| `uv run pytest -q` | **642 passed**, 383.85초 |
| `uv run ruff check skills/logo-land/scripts tests` | **All checks passed!** |
| `uv run basedpyright` | **0 errors, 0 warnings, 0 notes** |
| `uv run ruff format --check skills/logo-land/scripts/logo_helper/prompts.py skills/logo-land/scripts/logo_helper/logo_prompts.py tests/test_lettering_prompts.py tests/test_app_icon_compatibility.py` | 4개 파일 형식 검사 통과 |
| `uv run --with pyyaml python /Users/cillian/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/logo-land` | **Skill is valid!** |
| `git diff --check` | 통과 |
| 변경한 스킬 Markdown 5개 파일의 로컬 링크 점검 | 30개 대상 모두 존재합니다. |

처음 점검할 때 엄격한 문자열 결합 타입 검사와 테스트용 팔레트의 잘못된
`source="user"` 값을 발견하여 수정했습니다. 생성 출처는 기존 허용 값인
`assistant`, 선택 주체는 `user`로 분리했습니다. 스킬 검사기에 필요한 PyYAML은
일회성 `uv run --with` 환경으로 제공했으며 프로젝트 의존성은 변경하지 않았습니다.

주요 회귀 검사는 다음 내용을 확인합니다.

- 따옴표, 연속/앞뒤 공백, 줄바꿈, 대소문자, 한글과 분해된 Unicode 문자열이
  브리프 → CLI 프롬프트 → 실제 import 기록에서 그대로 유지됩니다.
- 적층 레터마크에는 심볼/문자 배치가 생기지 않으며, 레터마크와 모노그램은
  서로 다른 구성 지침을 받습니다.
- 다색 입체 스타일과 단색 제한이 함께 있으면 구조화된 팔레트의 HEX, 개수,
  그라데이션 제한을 보존합니다. 단색 점검 지침은 추가 이미지 생성을 요청하지 않습니다.
- 수정 프롬프트가 초기 `OLD NAME`을 새 필수 문구로 되돌리지 않으며, 부모의
  변경된 글자·자간·연결부를 유지하고 실제 부모 경로를 반환합니다.
- 초기 워드마크 브리프보다 명시된/상속된 심볼 결합 배치를 우선하며, 프롬프트와
  import의 배치 의도가 일치합니다. 부모의 팔레트·배경·알 수 없는 옛 배치도
  기존 회귀 검사로 확인합니다.
- 앱 아이콘 전용 결과는 기존 생성 함수와 일치하며, 일반 로고의 새 지침이
  섞이지 않습니다. 기존 앱 아이콘 스냅샷 검사도 통과했습니다.

## 실제 대화에 사용할 점검 입력

아래 문장은 자연어 라우팅과 실제 이미지 품질을 추가 확인하기 위한 입력 예시입니다.
본 작업의 자동 검사가 이미지 생성 품질을 검증했다는 뜻은 아닙니다.
자동 테스트에서 쓰는 작은 PNG는 이력·파일 동작 검사용 합성 자료입니다.

| 입력 예시 | 기대되는 처리와 확인 사항 |
|---|---|
| “어린이 만들기 브랜드 `momi`의 글자 로고를 만들어 주세요. 전부 소문자이고, 말랑하고 통통한 입체 글자를 여러 색으로 표현해 주세요. 별도 캐릭터 없이 세 방향을 보고 싶어요.” | `wordmark`, exact `momi`; 서로 다른 획·속공간·리듬으로 세 개념을 구성하고 글자만 남깁니다. |
| “Create one lettering-only logo for `RIVET`, a training brand: strong forward slant, compact spacing, angular open counters, black only, transparent background.” | `wordmark`, exact `RIVET`; 경사와 절단면으로 속도감을 표현하며 추가 속도 심볼이나 회색 음영을 넣지 않습니다. |
| “`NR` 두 글자를 N 위, R 아래로 쌓은 미니멀 기하학 로고를 만들어 주세요. 두 글자는 따로 읽혀야 해요.” | `lettermark`, exact `NR`, `lockup=null`; 같은 모듈과 광학적 행 간격을 사용하고 모노그램으로 합치지 않습니다. |
| “Interlock the exact initials `AV` with one shared stroke, while keeping both characters identifiable.” | `monogram`, exact `AV`; 공유 획을 설계하되 글자 누락·대체가 없는지 확인합니다. |
| “브랜드 표기는 `너울  Lab`입니다. 가운데 공백 두 개와 대소문자를 유지해서 둥근 한글·영문 글자 로고를 만들어 주세요.” | `wordmark`; 문자열을 그대로 저장하고, 한글 음절 구조와 두 단어 사이 간격을 실제 이미지에서 확인합니다. |
| “두 번째 시안의 새 이름 `너울  Lab`, 색과 연결된 획은 유지하고, 닫힌 속공간만 조금 넓혀 주세요.” | 선택한 실제 부모를 대상으로 수정합니다. 최초 브리프의 이전 이름·유형·팔레트를 복원하지 않습니다. |
| “A leaf symbol above the exact name `Neri Studio`, with the text centered.” | `combination`과 stacked/start/center 배치입니다. 적층 레터마크로 잘못 분류하지 않습니다. |

## 남은 한계와 담당 범위

자연어 요청의 해석은 스킬을 읽는 에이전트가 수행합니다. Python helper가 한국어·영어를
자동 분류하거나 정확한 글자·단색 재현·폰트 사용을 증명하지는 않습니다. 실제 결과의
문자 정확도, 작은 크기의 식별성, 레퍼런스와 구별되는 독창성은 네이티브 생성 후
이미지를 직접 열어 확인해야 합니다. 이미지 샘플·브랜드 자산·배포 메타데이터와
README 문서는 다른 담당자가 작업 중이며, 해당 변경은 수정하거나 되돌리지 않았습니다.
이 작업에서는 commit/push를 실행하지 않았습니다.
