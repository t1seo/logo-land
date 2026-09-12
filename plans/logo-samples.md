# Logo Land 샘플·브랜딩·README 실행 계획

사용자 최종 선택: **Logo Land**, 저장소·플러그인·스킬 ID `logo-land`. 마지막 이름 요청이 이전 후보를 대체합니다. README 도식은 사용자가 승인한 아이보리·검정 스타일의 diagram-design을 적용합니다. 브랜드 로고는 별도로 사용자가 요청한 LEGOLAND 패러디 방향으로 native imagegen에서 생성합니다.

## 실행 범위

- [x] 설치된 플러그인으로 10개 가상 브랜드의 독립 세션과 프롬프트 작성.
- [x] native 이미지 생성 10회, 반환 원본별 연결, PNG 가져오기.
- [x] 8유형과 한글 두 종을 큰 화면 및 실제 Chrome 240 CSS px에서 검수하고 각각 PNG·ZIP·가이드 내보내기.
- [x] 로컬 HTML 갤러리의 유형 필터·상세 요청·실제 프롬프트·검수 기록·다운로드 구현.
- [x] 최초 갤러리의 다섯 독립 검토와 403개 DOM 단언 통과.
- [x] 이름을 `logo-land`로 변경하고 새 설치본 생성. 기존 `.logo-generator/` 세션·출력 경로는 호환성을 위해 유지.
- [x] 자체 스킬로 Logo Land 전용 브랜드 로고 생성·검수·등록.
- [x] 영어 README.md와 한국어 README.ko.md, 언어 전환·사실에 기반한 배지·각 언어 도식·샘플 이미지 완성.
- [x] 최종 Chrome의 필터·상세·키보드·다운로드와 반응형 레이아웃 확인.
- [x] 이름 변경 후 테스트·정적 검사·로컬 링크 및 PNG·ZIP 해시 검증.
- [x] GitHub 저장소를 `t1seo/logo-land`로 변경하고 `main` 커밋·푸시 및 원격 SHA 확인.
- [x] 최종 샘플 HTML을 Chrome에 열어 두기.

## 고정된 자료 계약

`docs/samples/catalog.json`의 실제 브랜드는 LUMA, LOOP LAB, 고요, BREAD & BLOOM, KITE, MISO, NORTHLINE, 물결, FERN, NOVA NOTES입니다. 각 브랜드는 별도 native 호출 1회로 생성했습니다. 워드마크와 조합형은 각각 2개, 나머지 6유형은 각 1개입니다.

샘플당 `items/<id>/brief.json`, `prompt.txt`, `import.json`, `review.json`, `delivery/logo.png`, `delivery/manifest.json`, `delivery/brand-guide.md`, `delivery/logo-package.zip`를 보존합니다. 생성 당시의 `$logo-generator` 요청을 사후 조작하지 않습니다. 새 사용 안내에는 `$logo-land`를 표시합니다.

배경은 요청한 색상의 **불투명 단색**입니다. 10종 모두 1254×1254 PNG, 실제 투명 픽셀 0개입니다. 작은 크기 검수는 브랜드 소개용 240 CSS px이며 파비콘 적합성을 뜻하지 않습니다. 이미지 파일을 CSS/SVG로 대신 만들거나 원본을 덮어쓰지 않습니다.

## QA 기준

- 갤러리 파일을 `file://`로 열었을 때 실제 이미지가 표시되고 유형별 수가 위 계약과 일치합니다.
- 상세에서 요청·프롬프트가 카탈로그와 일치하며 PNG·ZIP·가이드가 실제 로컬 파일을 가리킵니다.
- Escape로 상세를 닫고 원래 카드에 초점이 돌아갑니다. 모바일에서도 상세·필터·다운로드를 사용할 수 있습니다.
- README 두 언어의 기능·설치·제약·샘플 내용이 대응하고, 각 로컬 이미지·링크가 새 복제본에 포함됩니다.
- diagram-design self_check·geometry 및 실제 렌더링에서 글자와 화살표가 잘리지 않습니다.
- `uv run --locked pytest -q`, Ruff, basedpyright가 통과합니다. 역사적인 검사와 현재 검사를 구분합니다.
- 스테이징 범위를 직접 검토하고, 개인 인증 자료·임시 디버깅 자료·가상환경은 포함하지 않습니다.
- 일반 `main` 푸시 후 로컬 HEAD와 원격 refs/heads/main이 일치합니다. 강제 푸시는 사용하지 않습니다.

초기 Metis 제안 중 검색·검색 초기화·추가 크기 보기 UI는 사용자 요구가 아니므로 채택하지 않았습니다. 실제 계약은 유형 필터와 상세 보기이며 작은 크기는 별도 Chrome 검수로 확인합니다. 독립 브랜드 생성, 문서, 갤러리 작업은 Orca Run `run_561a522272ae`에서 조정합니다.
