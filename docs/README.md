# Logo Land 조사·제작 자료

[English README](../README.md) · [한국어 README](../README.ko.md) · [Logo Land 전용 로고](brand/README.md) · [실제 샘플 10개 갤러리](samples/index.html)

추가 제작한 샘플과 브랜드 변경 검수는 [샘플·브랜드 검증 기록](qa/samples.md)에 정리했습니다. 아래는 최초 조사·구현 기록입니다.

2026-09-12에 다섯 서비스를 조사하고, Codex 내장 이미지 생성으로 대화형 플러그인을 구현했습니다. 브랜드 예제는 가상의 `Morrow Studio`입니다. 캡처 151개, 공식 출처 URL 67개, 최종 테스트 96개와 다섯 독립 검토를 정리했습니다.

| 자료 | 내용 |
|---|---|
| [다섯 서비스 비교와 제품 반영](research/comparison.md) | 제작 방식·유형·차이와 플러그인으로 가져온 흐름 |
| [공식 기능 조사](research/official-features.md) | 다섯 사이트의 입력 방식, 로고 유형, 편집, 다운로드·상품 범위와 출처 |
| [Looka·Fiverr·Design 직접 사용](research/looka-fiverr-design-walkthrough.md) | 실제로 클릭·입력·생성한 흐름과 스크린샷 |
| [Brandmark·Tailor 직접 사용](research/brandmark-tailor-walkthrough.md) | 직접 확인한 제작 단계와 확인 한계 |
| [Chrome 로그인 후 추가 조사](research/chrome-followup.md) | Codex Computer Use로 확인한 편집·한글·상품 선택 |
| [스크린샷 갤러리](research/gallery.html) | 서비스별 화면을 한 페이지에서 탐색 |
| [원시 캡처 목록](research/captures.jsonl) | URL·시각·PNG/JPEG·접근성 스냅샷 대응 관계 |
| [출처 목록](research/sources.json) | 공식 URL과 확인 상태 |
| [제작 계획](../plans/logo-generator.md) | 요구사항, 설계, 구현·검증 범위 |
| [설계 검토](planning/gap-analysis.md) | 이미지 도구·상태·참조·출력의 주요 판단 |
| [자동 검사](qa/helper-tests.md) | 정상 흐름과 실패·복구·동시성 검사 |
| [배경 변형 검사](qa/background-variants.md) | 버전별 투명·불투명 배경과 기존 작업 재개 검사 |
| [최종 검증 종합](qa/final.md) | 96개 테스트, 독립 검토, 패키지·설치 및 자료 검증 |
| [설치 기록](qa/installation.md) | 개인 플러그인 설치 위치, ZIP과 새 대화 사용법 |
| [실제 이미지 도구 테스트](qa/live/README.md) | 개별 시안 생성, 선택안 수정, 파일 검증·전달 |
| [이미지 비교 화면](qa/live/preview.html) | 원본과 수정본, 크기·배경별 확인 |

직접 실행한 기능과 공식 문서로만 확인한 기능은 각 보고서에서 구분합니다. 로그인·결제가 필요한 모든 기능을 실행했다는 의미는 아닙니다. 가격과 상품 구성은 조사 시점·지역·노출 조건에 따라 달라질 수 있습니다.

스크린샷은 제작 흐름의 연구 자료입니다. 사이트 디자인·로고 템플릿을 플러그인 에셋으로 재배포하지 않습니다. 플러그인이 실제 생성하는 로고와 경쟁 사이트의 예시 화면은 별개의 자료입니다.
