# Transparent PNG · 투명 배경 로고

[미리보기](index.html) · [투명 PNG](../../assets/logo-transparent.png) · [ZIP](delivery/logo-package.zip) · [브랜드 가이드](delivery/brand-guide.md)

Logo Land의 투명 배경 요청 지침을 명확히 하고, 기존 Logo Land 로고를 실제 Codex 내장 이미지 도구로 편집한 예제입니다. 원래 불투명 로고와 전달 패키지는 그대로 보존했습니다.

## 사용 방법

새 로고는 “투명 배경 PNG로 만들어 주세요”라고 요청하시면 됩니다. 스킬은 브리프를 `background: transparent`로 저장하고 실제 투명 배경 생성을 요청합니다. 기존 로고는 정확한 원본을 참조해 배경만 제거하고, 새 버전을 `--parent <id> --background transparent`로 등록합니다.

> $logo-land 고요라는 브랜드의 로고를 투명 배경 PNG로 만들어 주세요.

> 이 로고의 배경만 제거해 주세요. 글자·색상·형태는 유지해 주세요.

투명해 보이는 흰 배경이나 체크무늬 그림을 투명 PNG로 취급하지 않습니다. 실제 알파 픽셀과 육안 검수가 모두 충족돼야 내보낼 수 있습니다. 흰 글자 등 의도된 전경은 남기며 배경 제거에 맞지 않는 생성 결과는 내장 이미지 도구로 수정합니다.

## 실제 생성·검수 결과

| 확인 항목 | 결과 |
|---|---|
| 실제 이미지 도구 | `image_gen__imagegen` 1회, 기존 로고를 정확한 파일 참조로 편집 |
| 원본 / 새 버전 | `logo-land-brand`의 `a-v1` → `a-v2` |
| 선택 버전 배경 | `transparent`; 처음 브리프의 `opaque`는 역사적 의도로 보존 |
| 파일 | 1774 × 887, RGBA PNG |
| 완전히 투명한 픽셀 | 916,043개, alpha 0 |
| 부분 투명한 픽셀 | 653,675개, alpha 1–254 |
| 완전히 불투명한 픽셀 | 3,820개, alpha 255 |
| 네 모서리 | 모두 alpha 0 |
| 육안 검수 | 밝은 바탕·슬레이트색 바탕·CSS 체크무늬·240 CSS px 표시를 Chrome Computer Use로 확인 |
| 내보내기 | revision 8, 투명도 검사 통과 후 PNG·ZIP·가이드 생성 |
| SHA-256 | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |

기존 LOGO LAND 철자, 빨간 블록, 노란 햇살, 깃발, 흰 LOGO 글자와 배치를 유지했고 배경판이 제거됐습니다. 어두운 바탕에서는 원래 검정 LAND의 대비가 약합니다. 밝은 바탕 사용을 권장하며, 어두운 바탕용 흰 글자 버전은 별도로 요청하실 수 있습니다. 픽셀 단위로 완전히 동일한 원형 보존을 보장하는 편집은 아닙니다.

[실제 프롬프트](prompt.txt) · [생성 출처와 알파 기록](generation.json) · [육안 검수](review.json) · [Chrome 화면](chrome-preview.jpeg) · [내보내기 manifest](delivery/manifest.json)

## 코드와 문서 검증

기존 helper의 투명도 검사·버전별 배경 기록·내보내기 기능은 이미 구현돼 있어 Python 코드는 변경하지 않았습니다. 스킬의 발견 조건, 투명 생성·배경 제거 지침, 플러그인의 시작 요청과 두 언어 README의 사용 예제를 보완했습니다.

`uv run --locked pytest -q tests/test_background_variants.py tests/test_background_compatibility.py`: **17 passed in 11.46s**. 투명↔불투명 변경, 요구사항과 실제 픽셀 불일치 거부, 원본 재선택, 이후 수정과 기존 세션 호환 시나리오를 재검증했습니다. 이전 전체 테스트 96개를 이번에 다시 실행했다고 주장하지 않습니다.

README의 빈 두 컬럼 샘플 표는 **브랜드 / 로고 유형 / 생성 결과**, **Brand / Logo type / Generated logo**의 세 컬럼으로 수정했습니다. 각 언어에서 기존 10개 샘플과 PNG 링크를 유지했습니다.

Markdown을 HTML로 렌더링해 두 언어의 모든 표 머리글이 비어 있지 않은지, 샘플 표에 10행·이미지 10개가 유지되는지 검사했습니다. Chrome에서도 [한국어 표](readme-ko-table.jpeg)와 [영어 표](readme-en-table.jpeg)를 확인했습니다. 이 화면은 로컬 Markdown 렌더링 결과입니다. 전체 문서의 로컬 참조 검사도 통과했습니다. 생성 PNG·전달 PNG·ZIP 내부 파일이 일치하고 원래 불투명 PNG의 해시가 변하지 않은 것도 확인했습니다.

업데이트된 개인 플러그인 `0.3.0+codex.20260912135514`의 설치, manifest 검사, 스킬 검사가 통과했습니다. 새 Codex 대화에서 `$logo-land`로 요청하시면 새 투명 배경 지침을 사용합니다.

프롬프트 응답 사본의 개인 작업 폴더는 `<workspace>`로 표기했습니다. PNG·ZIP·실제 생성 프롬프트의 바이트는 수정하지 않았습니다.
