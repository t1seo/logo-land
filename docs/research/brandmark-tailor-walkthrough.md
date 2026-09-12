# Brandmark·Tailor Brands 실제 브라우저 조사

조사일은 2026-09-12이며, 캡처 시간은 UTC 12:11:11–12:24:12 / 한국시간 21:11:11–21:24:12입니다. Brandmark 새 앱과 v3에서는 비로그인 생성·편집까지 진행했습니다. Tailor Brands에서는 세 가지 로고 유형의 공개 온보딩을 살펴보고, 아이콘 유형으로 생성한 뒤 결과 공개 전 가입 화면까지 확인했습니다.

테스트 브랜드는 **Morrow Studio**, 업종은 지속가능한 디자인 스튜디오, 선호는 미니멀한 포레스트 그린입니다. 계정 생성, 개인 인증 정보 입력, 구매, CAPTCHA 우회는 하지 않았습니다. 아래의 ‘직접 확인’은 실제 클릭·입력·화면 확인을 뜻하며, 공개 제품 설명과 구분했습니다.

이 문서는 Orca 내장 브라우저에서 수행한 공개·비로그인 조사 범위입니다. 코디네이터의 UTC 12:27:04 지시에 따라 현재 증거를 확정했습니다. 이후 개인 Google 세션이 있는 외부 Chrome을 통한 추가 조사는 코디네이터가 담당하며 이 문서의 검증 범위에 포함하지 않습니다.

## 조사 방법과 증거

Orca 내장 브라우저만 사용하고 모든 명령에 정확한 페이지 ID를 지정했습니다. 스냅샷 확인 → 화면 조작 → 새 스냅샷 확인 순서로 진행했습니다. PNG는 `orca screenshot --page <id> --json`의 base64 결과를 디코딩한 실제 화면입니다. 각 PNG에 대응하는 JSON 접근성 스냅샷과 정확한 URL·ISO 시각을 저장했습니다. 전체 증거는 아래 76개 캡처 목록과 [공유 캡처 원장](captures.jsonl)에 있습니다.

| 대상 | 페이지 ID | 조사한 진입점 |
|---|---|---|
| Brandmark 새 앱·v3 | `89e997f6-caba-4c18-9fc9-10936ec59cef` | [새 앱](https://chat.brandmark.io/), [홈페이지](https://brandmark.io/), [v3](https://app.brandmark.io/v3/) |
| Tailor 제작 마법사 | `0e9ddc38-caab-4ff3-94e0-d8e7fc3d1b43` | 전달받은 Morrow Studio 제작 세션 |
| Tailor 공개 설명·가격 링크 | `df8c8e30-42cb-45dc-a562-bf569f1af20a` | [Logo Maker](https://www.tailorbrands.com/logo-maker), [Pricing](https://www.tailorbrands.com/product-pricing) |

Brandmark 홈페이지의 v3 링크 조작 중 새 앱 탭이 추가로 열렸습니다. 실제 v3 검증은 링크 대상인 `https://app.brandmark.io/v3/`를 소유 페이지에 직접 열어 진행했습니다. 다른 조사자의 사이트·페이지는 조작하지 않았습니다.

## 한눈에 보는 실제 접근 범위

| 항목 | Brandmark 새 앱 | Brandmark v3 | Tailor Brands |
|---|---|---|---|
| 공개 생성 진입 | 자동 생성, 템플릿, 빈 캔버스; Icon Designer는 로그인 요구 | 이름·키워드·색상 스타일 마법사 | Icon Based, Name Based, Initial Based |
| 생성 결과 | 비로그인 캐러셀·그리드 확인 | 비로그인 캐러셀 확인 | 생성 후 가입 오버레이; 정상 결과 탐색은 진행하지 못했습니다 |
| 실제 편집 | 텍스트·폰트·배치·아이콘·색상 변경 확인 | 이름·배치·배경·색상 패널 확인 | 가입 경계로 편집기 미접근 |
| 저장 | Save에서 로그인 요구 | 별도 저장 시험 없음 | 미접근 |
| 가격·내보내기 | 공개 패키지 가격 확인; 실제 파일 다운로드 없음 | 공개 패키지 가격 확인; 실제 파일 다운로드 없음 | 공개 가격 링크는 LLC 서비스; 로고 금액 미확인 |
| 대화형 생성 | 호스트명은 `chat`이지만 접근한 생성 흐름은 3단계 폼입니다 | 폼 기반입니다 | 단계별 폼과 시각적 선택입니다 |

## Brandmark 새 앱

### 생성 모드와 온보딩

[시작 화면](screenshots/brandmark-extra-01-modes.png)은 Generate, Templates, Icon Designer 세 카드를 제공합니다. 사이드바에는 Generate logos, New Logo, Icon Designer, Logo Templates, My Account가 있습니다.

자동 생성은 `/generate`에서 브랜드명·선택적 슬로건 → 키워드 → 색상 스타일 순서입니다. Morrow Studio를 입력하고 슬로건은 비웠으며, 키워드는 `sustainable design studio, forest, minimal`을 사용했습니다. 색상은 Organic을 선택했습니다. Simple, Vibrant, Organic, High Contrast, Dark, Soft Pastel과 단색 견본도 보였습니다. [입력](screenshots/brandmark-extra-03-keywords.png), [색상 선택](screenshots/brandmark-extra-05-organic-selected.png)

계정 없이 결과가 나왔습니다. [캐러셀](screenshots/brandmark-extra-07-results.png)과 [그리드](screenshots/brandmark-extra-08-grid.png)를 전환할 수 있었고, Gen AI·Text 표식과 워드마크, 글자에 잎·집 형태를 결합한 디자인, 나무 형태 등을 확인했습니다. Organic을 골랐지만 첫 결과는 파란 아이콘이었습니다. 따라서 이 세션에서는 색상 스타일이 정확한 포레스트 그린을 보장하지 않았습니다. 카드에는 Purchase, Edit, Variants, Save가 있으며, 그리드 카드 클릭은 큰 로고·목업 상세 화면을 열었습니다.

### 편집기에서 실제로 수행한 조작

[편집기](screenshots/brandmark-extra-10-editor.png)는 캔버스 왼쪽의 Quick Edit 패널에 Title, Slogan, Icon, Layout, Background를 배치합니다. 아래에는 Save, File, 실행 취소·다시 실행, Snap, 줌이 있습니다.

| 조작 | 실제 결과·관찰 | 증거 |
|---|---|---|
| 로고 제목을 Morrow Studio로 교체 | 캔버스의 제목을 수정했습니다. 최초 제목의 일부 글자는 접근성 스냅샷에서 사설 유니코드 글리프로 노출됐지만 화면에는 로고 글자로 보였습니다 | [편집 화면](screenshots/brandmark-extra-13-color-picker.png) |
| 폰트 변경 | Cypher에서 Brandmark Montserrat 300 옵션을 선택했고 Font: Montserrat 및 캔버스 변화가 확인됐습니다 | [변경 후](screenshots/brandmark-extra-12-font-changed.png) |
| 폰트 탐색 | 검색, Cyrillic·Chinese·Japanese·Korean, 굵기, Sans/Modern·Serif/Classic·Script·Brush 필터가 보였습니다; 각 언어 렌더링은 시험하지 않았습니다 | [폰트 선택기](screenshots/brandmark-extra-11-font-picker.png) |
| 배치 변경 | 다섯 가지 도식 중 아이콘 위 배치를 아이콘 왼쪽 배치로 바꿨습니다 | [변경 후](screenshots/brandmark-extra-15-layout-changed.png) |
| 아이콘 교체 | Search Icons에서 leaf 검색 → 결과의 첫 잎 아이콘 선택 → 기존 아이콘이 잎으로 바뀌었습니다 | [검색 결과](screenshots/brandmark-extra-19-leaf-results-loaded.png), [교체 후](screenshots/brandmark-extra-20-icon-replaced.png) |
| 색상 변경 | Solid/Gradient, HEX, 색상 면, 팔레트, Randomize, 견본을 확인했습니다. `#1B4332` 및 `1B4332` 입력 후 Enter·Tab 시도는 화면의 파란색을 바꾸지 못했습니다. 이후 초록 견본을 클릭하자 아이콘이 `#00e676`으로 바뀌었습니다 | [HEX 시도](screenshots/brandmark-extra-22-color-attempt.png), [견본 적용](screenshots/brandmark-extra-23-green-swatch.png) |
| 세부 위치·문자 제어 확인 | 크기, 자간, 행간, 정렬, Top/Left 숫자 입력과 아이콘 표시·크기·위치 제어가 보였습니다. 모든 숫자 입력을 각각 변경한 것은 아닙니다 | [문자](snapshots/brandmark-extra-13-color-picker.json), [아이콘](snapshots/brandmark-extra-16-icon-controls.json) |
| File 메뉴 열기 | Add Text, Add Shape, Add Template, Add Icon, Import Image, 잠금 제어, Generate Icon이 보였습니다. 이 메뉴는 요소 추가 중심이었습니다 | [메뉴](screenshots/brandmark-extra-24-file-menu.png) |

HEX 입력이 반영되지 않은 원인은 조사하지 않았습니다. 포레스트 그린 적용 성공으로 기록하지 않으며, 초록 견본 적용 성공과 구분합니다. 아이콘 검색도 최초에는 No results found가 보였지만 후속 스냅샷에서 결과가 로드됐습니다.

### 변형·템플릿·빈 캔버스·아이콘 생성

Variants를 열어 Color, Icon, Font 탭을 확인했습니다. [Color 변형](screenshots/brandmark-extra-29-variants-loaded.png)은 아홉 가지 미리보기를 표시했고, 어두운 초록 계열도 포함했습니다. Icon·Font 탭의 실제 변형 생성은 검증하지 않았습니다.

Logo Templates는 `/templates`에서 검색과 All, Modern, Natural, Industrial, Vintage, Abstract 분류를 제공합니다. Natural을 선택했을 때 템플릿 13개와 목록 끝 안내가 보였습니다. 첫 Use Template은 녹색 농업 심볼과 Cornora / HARVESTING IDEAS 문구가 있는 [편집 캔버스](screenshots/brandmark-extra-34-template-editor.png)를 열었습니다. 닫을 때 Save changes? 확인창의 Save·Discard·Close가 보였고, 이 조사에서 연 템플릿은 Discard로 닫았습니다. New Logo는 `/design`의 [빈 캔버스](screenshots/brandmark-extra-36-new-logo.png)를 열었습니다.

사이드바 Icon Designer를 선택하면 `/account`의 [로그인 화면](screenshots/brandmark-extra-31-icon-designer.png)이 나왔습니다. 따라서 독립 아이콘 프롬프트나 다회 대화는 테스트하지 못했습니다. `chat.brandmark.io`라는 주소만으로 대화식 로고 생성 UX가 검증됐다고 해석하면 안 됩니다.

### 저장·가격·파일 경계

Save는 [Login to Save Your Logo](screenshots/brandmark-extra-25-save-gate.png) 창을 띄우며 Google 또는 이메일 로그인을 요구했습니다. 결과 카드의 Purchase는 계정 없이 패키지 가격을 보여줬습니다. 패키지별 최종 Purchase 버튼은 누르지 않았습니다.

| 새 앱 표시 패키지 | 조사 시점 표시 가격 | 화면에 표시된 핵심 구성 |
|---|---|---|
| Basic | $35, 일회성 | PNG 로고 |
| Designer | $65, 일회성 Launch Promo; $95 취소선 | 벡터 디자인 파일, 사람의 디자인 지원, 무제한 디자인 변경, 브랜드 가이드, 명함·웹·소셜·발표 자료, 목업, SVG/Lottie, QR |
| Enterprise | $195, 일회성 | Designer 구성, 비AI 원본 디자인 10개, 우선 디자인 지원, 폰트 다운로드 |

가격 증거는 [공개 패키지 화면](screenshots/brandmark-extra-27-purchase-login.png)입니다. 파일명에 `login`이 들어가지만 실제 화면은 로그인창이 아닌 가격표입니다. 홈페이지의 SVG·PNG·PDF 내보내기는 [공개 설명](snapshots/brandmark-extra-37-marketing-entry.json)이며, 이 세션에서 다운로드된 산출물은 없습니다.

## Brandmark v3

홈페이지에서 새 생성 앱과 별도로 연결된 [v3](https://app.brandmark.io/v3/)는 직접 열었을 때 정상 동작했습니다. 브랜드명·슬로건 → 키워드 → 동일한 여섯 색상 스타일 → 생성 흐름입니다. 일반 텍스트로 입력한 키워드는 바로 확정되지 않았고, 추천 leaf를 눌러 태그를 만든 후 다음 단계로 진행했습니다. **v3에서 실제로 확정된 키워드는 leaf**였으므로 새 앱과 완전히 동일한 입력을 사용한 결과 비교는 아닙니다. Organic 색상 스타일은 동일하게 선택했습니다. [키워드](screenshots/brandmark-extra-41-v3-colors.png), [색상](screenshots/brandmark-extra-42-v3-color-style.png)

비로그인 [결과 캐러셀](screenshots/brandmark-extra-44-v3-results.png)에 Morrow Studio 워드마크와 Purchase, Save, Edit, Ideas가 표시됐습니다. reCAPTCHA 배지는 있었으나 도전 과제는 나오지 않았고, 우회 없이 생성됐습니다.

편집기는 새 앱의 왼쪽 패널 대신 [화면 아래 패널](screenshots/brandmark-extra-45-v3-editor.png)을 사용합니다. Name, Slogan, Icon, Background, Layout 탭이 있으며, 이름 크기·자간·굵기·행간·폰트·위치를 확인했습니다. [Layout](screenshots/brandmark-extra-46-v3-layout.png)의 다섯 도식과 [Background](screenshots/brandmark-extra-47-v3-background.png)의 컨테이너·크기·위치·배경색, [색상 선택기](screenshots/brandmark-extra-48-v3-color-picker.png)의 Color·Gradient·Saved와 HEX 입력을 열어 확인했습니다. v3에서는 새 앱과 같은 수준으로 아이콘·폰트·HEX 변경 성공까지 재시험하지 않았습니다.

| v3 패키지 | 조사 시점 표시 가격 | 새 앱과 비교 시 주의점 |
|---|---|---|
| Basic | $25, 일회성 | 새 앱 Basic $35와 다릅니다 |
| Designer | $65, 일회성 | 소스 파일, 브랜드 가이드, 명함·소셜·발표·레터헤드·목업, 무제한 디자인 변경이 표시됩니다 |
| Enterprise | $175, 일회성 | 최대 10개 디자이너 원본 컨셉; 새 앱 $195와 다릅니다 |

[v3 가격표](screenshots/brandmark-extra-49-v3-purchase.png)까지 확인했고 결제는 진행하지 않았습니다. 새 앱 가격과 v3 가격을 하나의 현행 가격으로 합치면 안 됩니다.

## Tailor Brands

### 공개 온보딩과 세 가지 유형

전달받은 제작 세션은 브랜드명 Morrow Studio 입력 이후였습니다. 첫 화면은 How did you discover? 유입 경로 질문으로, AI(예: ChatGPT)를 포함한 여러 선택지와 Skip이 있었습니다. Skip 후 제공 형태에서 Services, 업종 검색에서 Design Studio를 선택했습니다. [업종·설명](screenshots/tailor-extra-05-brief.png)에 다음 문장을 입력했습니다.

> Morrow Studio is a sustainable design studio. We want a minimal forest green logo for thoughtful, environmentally conscious clients.

| 공개 분기 | 실제로 진행한 내용 | 증거 |
|---|---|---|
| Icon Based | Geometric Shape 또는 Search For Icon 선택으로 이어졌습니다 | [분기](screenshots/tailor-extra-07-icon-type-selected.png) |
| Geometric Shape | 추상 도형 20개, 최대 5개 선택 안내, 다섯 슬롯, Skip을 확인했습니다. 도형은 선택하지 않고 검색 분기로 이동했습니다 | [도형](screenshots/tailor-extra-08-geometric.png) |
| Search For Icon | 카테고리 제안, 검색·Reset·Load more를 확인했습니다. leaf를 검색해 첫 잎 아이콘을 선택했습니다 | [검색 결과](screenshots/tailor-extra-10-leaf-results.png), [선택](screenshots/tailor-extra-11-leaf-selected.png) |
| Name Based | 생성 후 공개 마법사로 돌아가 유형을 바꿨습니다. 아이콘 선택 없이 스타일 단계로 바로 이어졌습니다 | [Name 단계](screenshots/tailor-extra-23-name-mode.png) |
| Initial Based | 같은 방식으로 유형을 바꿔 아이콘 단계 없이 스타일로 이어짐을 확인했습니다 | [Initial 단계](screenshots/tailor-extra-22-initial-mode.png) |

스타일은 이름·폰트가 다른 이미지 카드 15개 중 **세 개를 선택해야** Next가 활성화됐습니다. 최종 선택은 Thin, Rounded, Classy였습니다. Childish를 잠시 선택했다가 해제했고 최종 3/3 상태를 확인했습니다. 카드 이름은 접근성 스냅샷에서 충분히 설명되지 않아 실제 PNG의 글자를 읽었습니다. [스타일 목록](screenshots/tailor-extra-12-font-styles.png), [최종 선택](screenshots/tailor-extra-13-styles-selected.png)

Icon Based의 잎 아이콘 경로만 최종 생성했습니다. Name Based·Initial Based는 공개 분기 진입을 확인했으며 각각 별도 결과 세트를 생성하지 않았습니다. 이 흐름에서는 독립 색상 선택 단계를 만나지 않았고, 포레스트 그린 선호는 설명 문장으로만 전달됐습니다.

### 생성 진행과 가입 경계

생성 화면은 로고 디자인, 명함, 소셜 게시물 등의 진행 메시지와 백분율을 표시했습니다. 1% 캡처부터 결과 가입창 캡처까지 약 4분 20초가 걸렸습니다. 이는 한 세션의 관측 시간이며 일반적인 처리 속도 측정은 아닙니다. 전체 시간·URL은 아래 증거 목록에 있습니다.

최종 URL은 `https://studio.tailorbrands.com/business/131807094/wizard/logos/766286290?selectedBrandVersionId=9448612715`였습니다. [가입 화면](screenshots/tailor-extra-21-results-boundary.png)은 로고 선택지를 보려면 무료 가입하라는 안내와 Facebook, Google, 이메일, 비밀번호, I Agree, Already Registered?를 표시했습니다. 닫기 버튼은 보이지 않았습니다.

배경에는 어두워진 로고 목록과 명함·웹사이트·상품·소셜 목업이 보였고, 접근성 스냅샷에는 Customize, Love it!, See More가 존재했습니다. 가입 오버레이 뒤의 버튼 존재를 **사용 가능한 편집기 접근 성공으로 계산하지 않았습니다**. 가입하지 않았으므로 결과 정상 탐색, 색상·폰트·아이콘·배치 편집, 저장, 실제 다운로드, 로고 구매 가격은 확인하지 못했습니다.

브라우저의 뒤로 가기와 공개 마법사 상단 Logo type·About 탐색으로 이전 입력 단계에 돌아갔습니다. About에는 업종과 설명이 유지됐습니다. 가입 경계를 우회하지 않았습니다.

### 공개 설명과 가격 링크의 한계

[공개 Logo Maker 페이지](https://www.tailorbrands.com/logo-maker)의 [전체 스냅샷](snapshots/tailor-extra-25-public-features.json)은 워드마크·모노그램·아이콘, 폰트·아이콘·색상 편집, EPS·SVG·PNG 제공을 설명합니다. FAQ는 저해상도 다운로드는 무료이고 고해상도 벡터는 유료라고 안내합니다. **이는 제품 설명이며 이 조사에서 수행한 다운로드·편집 결과가 아닙니다.**

공개 사이트의 Pricing 링크는 [product-pricing](https://www.tailorbrands.com/product-pricing)으로 이어졌지만, 실제 [화면](screenshots/tailor-extra-27-public-pricing.png)은 LLC 설립 가격 안내였습니다. 해당 서비스 금액을 로고 가격으로 보고하지 않습니다. 제작 탭에서 공개 홈페이지로 이동할 때 ERR_ABORTED가 발생해 별도의 소유 탭을 만들었으며, 탭 생성·가격 페이지 이동 명령의 일시적인 runtime_unavailable은 후속 페이지 목록과 스냅샷으로 정상 로드를 확인했습니다.

## 대화형 로고 플러그인에 적용할 관찰 기반 제안

아래는 직접 관찰한 UX에서 도출한 설계 제안이며, 경쟁사가 제공한다고 검증한 기능 목록은 아닙니다.

1. 브랜드명·업종·설명·로고 유형·색상·스타일을 대화에서 모아 짧은 확인 요약으로 보여주는 구성이 적합합니다. Tailor의 유형별 분기는 아이콘형에만 심볼 질문을 추가하는 방식의 근거가 됩니다.
2. ‘자연적인 느낌’과 정확한 색상값을 따로 보관할 필요가 있습니다. Brandmark의 Organic 결과가 파란색이었으므로 포레스트 그린 같은 명시적 제약은 생성 후 미리보기에서 다시 확인해야 합니다.
3. 결과에는 여러 후보와 확대 보기, 글자·아이콘·색·배치 수정 진입점을 함께 제공하는 편이 좋겠습니다. Brandmark에서는 캐러셀·그리드·변형 비교와 직접 편집을 연결할 수 있었습니다.
4. 대화로 ‘아이콘을 왼쪽으로’, ‘잎 모양으로’, ‘더 가는 글꼴로’ 요청하더라도 변경 전후 미리보기와 되돌리기가 필요합니다. 이번 조사에서는 해당 조작을 시각적으로 확인할 수 있었지만 HEX 입력은 성공하지 않아 확인 절차의 가치가 드러났습니다.
5. 가입·결제 시점을 생성 시작 전에 안내하는 편이 좋겠습니다. Tailor는 생성 대기 이후 결과를 가입창으로 가렸고, Brandmark는 생성·편집 후 저장에서 로그인을 요구했습니다.
6. 생성 중에는 진행 상태와 완료 후 다음 행동을 명확히 보여주는 편이 좋겠습니다. 단일 세션에서 Tailor의 대기가 약 4분 20초였으므로 고정적인 짧은 소요 시간 약속을 그대로 차용하기 어렵습니다.
7. 내보내기 형식·해상도·비용은 실제 파일 생성 성공과 분리해 기록해야 합니다. 이번 조사에서도 공개 설명, 패키지 구성, 다운로드 성공은 서로 다른 증거 수준입니다.

## 캡처 품질과 해석 주의점

총 76개 PNG와 76개 JSON 스냅샷입니다. Brandmark 49쌍, Tailor 27쌍을 저장했습니다. 핵심 모드·결과·편집·가격·가입·유형 화면은 이미지 뷰어로 실제 열어 확인했습니다. 스냅샷을 먼저 저장하고 PNG를 바로 뒤에 찍으므로 비동기 전환 중의 텍스트와 화면이 조금 다를 수 있습니다. 특히 Brandmark 아이콘 교체 캡처 20은 스냅샷에 직전 대화상자가 남아 있고 PNG에는 교체된 잎이 보입니다.

최종 파일 검증에서 PNG 76개의 시그니처·크기(2798×1818 또는 2798×1746), JSON 76개의 성공 상태·URL 일치, 중복 없는 캡처 이름, 본문 로컬 링크 197개의 존재를 확인했습니다. PNG 총용량은 19,231,343바이트입니다. 코드 변경이 없는 조사 산출물이므로 애플리케이션 빌드·테스트는 수행하지 않았습니다.

일부 파일명은 캡처 당시 예상 상태를 담고 있습니다. `brandmark-extra-26-purchase-gate`는 편집기이고, `27-purchase-login`이 실제 가격표입니다. `30-font-variants`는 변형창을 닫은 캐러셀로 폰트 변형 검증이 아닙니다. `38-v3-entry`는 아직 홈페이지이며 실제 v3는 39부터입니다. `41-v3-colors`는 키워드 단계이고 실제 색상은 42입니다. Tailor 14–20은 생성 진행 상태이며 실제 가입 경계는 21입니다. **다음 표의 동작·결과 설명과 실제 파일 내용이 판정 기준입니다.**

## 전체 캡처 원장

시각은 캡처 저장 완료 기준 UTC이며 한국시간은 9시간을 더하시면 됩니다. URL은 각 스냅샷이 반환한 정확한 페이지 주소입니다.

| 캡처·증거 파일 | UTC 시각 | 정확한 URL | 동작·결과 |
|---|---|---|---|
| brandmark-extra-01-modes<br>[PNG](screenshots/brandmark-extra-01-modes.png) · [스냅샷](snapshots/brandmark-extra-01-modes.json) | 2026-09-12T12:11:11.643Z | <https://chat.brandmark.io/> | 새 앱 시작 화면: Generate, Templates, Icon Designer와 사이드바를 확인했습니다. |
| tailor-extra-01-discovery<br>[PNG](screenshots/tailor-extra-01-discovery.png) · [스냅샷](snapshots/tailor-extra-01-discovery.json) | 2026-09-12T12:11:12.964Z | <https://studio.tailorbrands.com/business/131807094/wizard/channel> | 전달받은 제작 세션에서 유입 경로 질문과 Skip을 확인했습니다. |
| brandmark-extra-02-generate-entry<br>[PNG](screenshots/brandmark-extra-02-generate-entry.png) · [스냅샷](snapshots/brandmark-extra-02-generate-entry.json) | 2026-09-12T12:11:19.316Z | <https://chat.brandmark.io/generate> | Generate를 열어 브랜드명·선택적 슬로건 입력을 확인했습니다. |
| tailor-extra-02-business-name<br>[PNG](screenshots/tailor-extra-02-business-name.png) · [스냅샷](snapshots/tailor-extra-02-business-name.json) | 2026-09-12T12:11:21.509Z | <https://studio.tailorbrands.com/business/131807094/wizard/intro> | Skip 후 상품·서비스 등 제공 형태를 묻는 화면입니다; 브랜드명 입력 화면이 아닙니다. |
| tailor-extra-03-services<br>[PNG](screenshots/tailor-extra-03-services.png) · [스냅샷](snapshots/tailor-extra-03-services.json) | 2026-09-12T12:11:31.848Z | <https://studio.tailorbrands.com/business/131807094/wizard/intro> | Services를 선택했습니다. |
| brandmark-extra-03-keywords<br>[PNG](screenshots/brandmark-extra-03-keywords.png) · [스냅샷](snapshots/brandmark-extra-03-keywords.json) | 2026-09-12T12:11:42.679Z | <https://chat.brandmark.io/generate> | Morrow Studio 입력 후 지속가능한 스튜디오·forest·minimal 키워드 단계로 진행했습니다. |
| tailor-extra-04-industry<br>[PNG](screenshots/tailor-extra-04-industry.png) · [스냅샷](snapshots/tailor-extra-04-industry.json) | 2026-09-12T12:11:45.208Z | <https://studio.tailorbrands.com/business/131807094/wizard/profile> | 업종 Design 검색 결과에서 Design Studio를 선택했습니다. |
| brandmark-extra-04-color-style<br>[PNG](screenshots/brandmark-extra-04-color-style.png) · [스냅샷](snapshots/brandmark-extra-04-color-style.json) | 2026-09-12T12:12:06.155Z | <https://chat.brandmark.io/generate> | 키워드 입력 후 여섯 색상 스타일과 단색 견본을 확인했습니다. |
| brandmark-extra-05-organic-selected<br>[PNG](screenshots/brandmark-extra-05-organic-selected.png) · [스냅샷](snapshots/brandmark-extra-05-organic-selected.json) | 2026-09-12T12:12:17.778Z | <https://chat.brandmark.io/generate> | Organic 색상 스타일을 선택했습니다. |
| tailor-extra-05-brief<br>[PNG](screenshots/tailor-extra-05-brief.png) · [스냅샷](snapshots/tailor-extra-05-brief.json) | 2026-09-12T12:12:30.413Z | <https://studio.tailorbrands.com/business/131807094/wizard/profile> | 지속가능한 스튜디오·미니멀 포레스트 그린 로고 설명을 입력했습니다. |
| brandmark-extra-06-generating<br>[PNG](screenshots/brandmark-extra-06-generating.png) · [스냅샷](snapshots/brandmark-extra-06-generating.json) | 2026-09-12T12:12:32.141Z | <https://chat.brandmark.io/generate> | 생성을 실행해 완료 전환 화면을 확인했습니다. |
| brandmark-extra-07-results<br>[PNG](screenshots/brandmark-extra-07-results.png) · [스냅샷](snapshots/brandmark-extra-07-results.json) | 2026-09-12T12:12:53.176Z | <https://chat.brandmark.io/generate> | 비로그인 결과 캐러셀과 Purchase·Edit·Variants·Save를 확인했습니다. |
| brandmark-extra-08-grid<br>[PNG](screenshots/brandmark-extra-08-grid.png) · [스냅샷](snapshots/brandmark-extra-08-grid.json) | 2026-09-12T12:13:00.327Z | <https://chat.brandmark.io/generate> | Grid View를 눌러 여러 로고 후보를 비교했습니다. |
| tailor-extra-06-logo-types<br>[PNG](screenshots/tailor-extra-06-logo-types.png) · [스냅샷](snapshots/tailor-extra-06-logo-types.json) | 2026-09-12T12:13:04.078Z | <https://studio.tailorbrands.com/business/131807094/wizard/design-type?profileStepId=766286286> | Icon Based·Name Based·Initial Based 유형을 확인했습니다. |
| tailor-extra-07-icon-type-selected<br>[PNG](screenshots/tailor-extra-07-icon-type-selected.png) · [스냅샷](snapshots/tailor-extra-07-icon-type-selected.json) | 2026-09-12T12:13:12.206Z | <https://studio.tailorbrands.com/business/131807094/wizard/icon?id=766286287> | Icon Based 선택 후 Geometric Shape·Search For Icon 분기를 확인했습니다. |
| tailor-extra-08-geometric<br>[PNG](screenshots/tailor-extra-08-geometric.png) · [스냅샷](snapshots/tailor-extra-08-geometric.json) | 2026-09-12T12:13:21.301Z | <https://studio.tailorbrands.com/business/131807094/wizard/icon/abstract?id=766286287> | Geometric Shape의 추상 도형 20개·최대 5개 선택·Skip을 확인했습니다. |
| brandmark-extra-09-card-detail<br>[PNG](screenshots/brandmark-extra-09-card-detail.png) · [스냅샷](snapshots/brandmark-extra-09-card-detail.json) | 2026-09-12T12:13:23.281Z | <https://chat.brandmark.io/generate> | 그리드 카드를 눌러 확대 로고·목업 상세를 열었습니다. |
| tailor-extra-09-icon-search<br>[PNG](screenshots/tailor-extra-09-icon-search.png) · [스냅샷](snapshots/tailor-extra-09-icon-search.json) | 2026-09-12T12:13:35.726Z | <https://studio.tailorbrands.com/business/131807094/wizard/icon/search?id=766286287> | 검색 분기로 이동해 카테고리·검색창·Reset·Load more를 확인했습니다. |
| brandmark-extra-10-editor<br>[PNG](screenshots/brandmark-extra-10-editor.png) · [스냅샷](snapshots/brandmark-extra-10-editor.json) | 2026-09-12T12:13:59.051Z | <https://chat.brandmark.io/generate> | Edit로 캔버스와 Quick Edit 패널을 열었습니다. |
| tailor-extra-10-leaf-results<br>[PNG](screenshots/tailor-extra-10-leaf-results.png) · [스냅샷](snapshots/tailor-extra-10-leaf-results.json) | 2026-09-12T12:14:01.089Z | <https://studio.tailorbrands.com/business/131807094/wizard/icon/search?id=766286287> | leaf 검색으로 잎 아이콘 결과를 확인했습니다. |
| brandmark-extra-11-font-picker<br>[PNG](screenshots/brandmark-extra-11-font-picker.png) · [스냅샷](snapshots/brandmark-extra-11-font-picker.json) | 2026-09-12T12:14:13.720Z | <https://chat.brandmark.io/generate> | Title의 폰트 선택기에서 검색·언어·굵기·스타일 필터를 확인했습니다. |
| tailor-extra-11-leaf-selected<br>[PNG](screenshots/tailor-extra-11-leaf-selected.png) · [스냅샷](snapshots/tailor-extra-11-leaf-selected.json) | 2026-09-12T12:14:15.222Z | <https://studio.tailorbrands.com/business/131807094/wizard/icon/search?id=766286287> | 첫 잎 아이콘을 선택했습니다. |
| brandmark-extra-12-font-changed<br>[PNG](screenshots/brandmark-extra-12-font-changed.png) · [스냅샷](snapshots/brandmark-extra-12-font-changed.json) | 2026-09-12T12:14:26.361Z | <https://chat.brandmark.io/generate> | Montserrat 300 옵션을 선택해 폰트 표시와 캔버스 변화를 확인했습니다. |
| brandmark-extra-13-color-picker<br>[PNG](screenshots/brandmark-extra-13-color-picker.png) · [스냅샷](snapshots/brandmark-extra-13-color-picker.json) | 2026-09-12T12:14:47.101Z | <https://chat.brandmark.io/generate> | 제목을 Morrow Studio로 바꾸고 제목 색상 선택기를 열었습니다. |
| tailor-extra-12-font-styles<br>[PNG](screenshots/tailor-extra-12-font-styles.png) · [스냅샷](snapshots/tailor-extra-12-font-styles.json) | 2026-09-12T12:14:54.140Z | <https://studio.tailorbrands.com/business/131807094/wizard/questions?id=766286287> | 스타일 이미지 카드 15개와 세 개 선택 요구를 확인했습니다. |
| brandmark-extra-14-layout<br>[PNG](screenshots/brandmark-extra-14-layout.png) · [스냅샷](snapshots/brandmark-extra-14-layout.json) | 2026-09-12T12:15:25.819Z | <https://chat.brandmark.io/generate> | Layout을 열어 다섯 가지 배치 도식을 확인했습니다. |
| tailor-extra-13-styles-selected<br>[PNG](screenshots/tailor-extra-13-styles-selected.png) · [스냅샷](snapshots/tailor-extra-13-styles-selected.json) | 2026-09-12T12:15:42.275Z | <https://studio.tailorbrands.com/business/131807094/wizard/questions?id=766286287> | Thin·Rounded·Classy를 선택해 3/3 및 Next 활성화를 확인했습니다. |
| brandmark-extra-15-layout-changed<br>[PNG](screenshots/brandmark-extra-15-layout-changed.png) · [스냅샷](snapshots/brandmark-extra-15-layout-changed.json) | 2026-09-12T12:15:45.636Z | <https://chat.brandmark.io/generate> | 아이콘 왼쪽 배치를 선택해 화면 변화를 확인했습니다. |
| tailor-extra-14-result-gate<br>[PNG](screenshots/tailor-extra-14-result-gate.png) · [스냅샷](snapshots/tailor-extra-14-result-gate.json) | 2026-09-12T12:15:47.334Z | <https://studio.tailorbrands.com/business/131807094/wizard/generate?prevId=766286289> | 생성을 시작했습니다; 결과 경계가 아니라 1% 진행 화면입니다. |
| brandmark-extra-16-icon-controls<br>[PNG](screenshots/brandmark-extra-16-icon-controls.png) · [스냅샷](snapshots/brandmark-extra-16-icon-controls.json) | 2026-09-12T12:15:57.376Z | <https://chat.brandmark.io/generate> | Icon 패널의 검색·생성·표시·크기·색·위치 제어를 확인했습니다. |
| tailor-extra-15-after-generation<br>[PNG](screenshots/tailor-extra-15-after-generation.png) · [스냅샷](snapshots/tailor-extra-15-after-generation.json) | 2026-09-12T12:15:58.888Z | <https://studio.tailorbrands.com/business/131807094/wizard/generate?prevId=766286289> | 생성 진행 4% 화면입니다. |
| brandmark-extra-17-search-icons<br>[PNG](screenshots/brandmark-extra-17-search-icons.png) · [스냅샷](snapshots/brandmark-extra-17-search-icons.json) | 2026-09-12T12:16:09.751Z | <https://chat.brandmark.io/generate> | Search Icons 대화상자를 열었습니다. |
| brandmark-extra-18-leaf-icons<br>[PNG](screenshots/brandmark-extra-18-leaf-icons.png) · [스냅샷](snapshots/brandmark-extra-18-leaf-icons.json) | 2026-09-12T12:16:19.528Z | <https://chat.brandmark.io/generate> | leaf 검색 직후 No results found 상태를 기록했습니다; 후속 캡처에서 로드됐습니다. |
| brandmark-extra-19-leaf-results-loaded<br>[PNG](screenshots/brandmark-extra-19-leaf-results-loaded.png) · [스냅샷](snapshots/brandmark-extra-19-leaf-results-loaded.json) | 2026-09-12T12:16:37.054Z | <https://chat.brandmark.io/generate> | 비동기 로드 후 잎 아이콘 결과가 표시됐습니다. |
| brandmark-extra-20-icon-replaced<br>[PNG](screenshots/brandmark-extra-20-icon-replaced.png) · [스냅샷](snapshots/brandmark-extra-20-icon-replaced.json) | 2026-09-12T12:16:39.898Z | <https://chat.brandmark.io/generate> | 첫 잎 아이콘을 선택했습니다; PNG에는 교체 결과, 스냅샷에는 직전 대화상자가 남아 있습니다. |
| tailor-extra-16-generation-progress<br>[PNG](screenshots/tailor-extra-16-generation-progress.png) · [스냅샷](snapshots/tailor-extra-16-generation-progress.json) | 2026-09-12T12:16:41.509Z | <https://studio.tailorbrands.com/business/131807094/wizard/generate?prevId=766286289> | 생성 진행 29% 화면입니다. |
| brandmark-extra-21-icon-color<br>[PNG](screenshots/brandmark-extra-21-icon-color.png) · [스냅샷](snapshots/brandmark-extra-21-icon-color.json) | 2026-09-12T12:16:55.663Z | <https://chat.brandmark.io/generate> | 아이콘 색상 선택기를 열었습니다. |
| brandmark-extra-22-color-attempt<br>[PNG](screenshots/brandmark-extra-22-color-attempt.png) · [스냅샷](snapshots/brandmark-extra-22-color-attempt.json) | 2026-09-12T12:17:07.094Z | <https://chat.brandmark.io/generate> | 포레스트 그린 HEX 입력을 시도했지만 캔버스는 파란색으로 남았습니다. |
| brandmark-extra-23-green-swatch<br>[PNG](screenshots/brandmark-extra-23-green-swatch.png) · [스냅샷](snapshots/brandmark-extra-23-green-swatch.json) | 2026-09-12T12:17:20.237Z | <https://chat.brandmark.io/generate> | 초록 견본을 클릭해 아이콘 색상 #00e676 적용을 확인했습니다. |
| brandmark-extra-24-file-menu<br>[PNG](screenshots/brandmark-extra-24-file-menu.png) · [스냅샷](snapshots/brandmark-extra-24-file-menu.json) | 2026-09-12T12:17:24.243Z | <https://chat.brandmark.io/generate> | File 메뉴의 텍스트·도형·템플릿·아이콘 추가 및 이미지 가져오기를 확인했습니다. |
| brandmark-extra-25-save-gate<br>[PNG](screenshots/brandmark-extra-25-save-gate.png) · [스냅샷](snapshots/brandmark-extra-25-save-gate.json) | 2026-09-12T12:17:35.199Z | <https://chat.brandmark.io/generate> | Save를 눌러 Login to Save Your Logo 창을 확인했습니다. |
| brandmark-extra-26-purchase-gate<br>[PNG](screenshots/brandmark-extra-26-purchase-gate.png) · [스냅샷](snapshots/brandmark-extra-26-purchase-gate.json) | 2026-09-12T12:17:49.440Z | <https://chat.brandmark.io/generate> | 로그인창을 닫은 편집기 상태입니다; 파일명과 달리 가격 경계 화면이 아닙니다. |
| tailor-extra-17-result-access<br>[PNG](screenshots/tailor-extra-17-result-access.png) · [스냅샷](snapshots/tailor-extra-17-result-access.json) | 2026-09-12T12:17:58.659Z | <https://studio.tailorbrands.com/business/131807094/wizard/generate?prevId=766286289> | 생성 진행 71% 화면입니다. |
| brandmark-extra-27-purchase-login<br>[PNG](screenshots/brandmark-extra-27-purchase-login.png) · [스냅샷](snapshots/brandmark-extra-27-purchase-login.json) | 2026-09-12T12:18:06.347Z | <https://chat.brandmark.io/generate> | 결과 카드 Purchase에서 공개 Basic $35·Designer $65 프로모션·Enterprise $195 가격표를 열었습니다. |
| brandmark-extra-28-variants<br>[PNG](screenshots/brandmark-extra-28-variants.png) · [스냅샷](snapshots/brandmark-extra-28-variants.json) | 2026-09-12T12:18:26.542Z | <https://chat.brandmark.io/generate> | Variants 대화상자를 열었으며 미리보기는 아직 로딩 중입니다. |
| brandmark-extra-29-variants-loaded<br>[PNG](screenshots/brandmark-extra-29-variants-loaded.png) · [스냅샷](snapshots/brandmark-extra-29-variants-loaded.json) | 2026-09-12T12:18:33.235Z | <https://chat.brandmark.io/generate> | Color 변형 아홉 개와 Color·Icon·Font 탭을 확인했습니다. |
| brandmark-extra-30-font-variants<br>[PNG](screenshots/brandmark-extra-30-font-variants.png) · [스냅샷](snapshots/brandmark-extra-30-font-variants.json) | 2026-09-12T12:18:35.498Z | <https://chat.brandmark.io/generate> | 변형창이 닫힌 캐러셀입니다; 파일명과 달리 Font 변형을 시험한 증거가 아닙니다. |
| tailor-extra-18-generation-complete<br>[PNG](screenshots/tailor-extra-18-generation-complete.png) · [스냅샷](snapshots/tailor-extra-18-generation-complete.json) | 2026-09-12T12:18:37.304Z | <https://studio.tailorbrands.com/business/131807094/wizard/generate?prevId=766286289> | 생성 진행 86% 화면입니다; 완료된 결과가 아닙니다. |
| brandmark-extra-31-icon-designer<br>[PNG](screenshots/brandmark-extra-31-icon-designer.png) · [스냅샷](snapshots/brandmark-extra-31-icon-designer.json) | 2026-09-12T12:18:47.456Z | <https://chat.brandmark.io/account> | Icon Designer 선택 후 계정 로그인 화면이 나왔습니다. |
| brandmark-extra-32-templates<br>[PNG](screenshots/brandmark-extra-32-templates.png) · [스냅샷](snapshots/brandmark-extra-32-templates.json) | 2026-09-12T12:18:56.717Z | <https://chat.brandmark.io/templates> | Logo Templates에서 검색과 여섯 분류를 확인했습니다. |
| tailor-extra-19-result-or-gate<br>[PNG](screenshots/tailor-extra-19-result-or-gate.png) · [스냅샷](snapshots/tailor-extra-19-result-or-gate.json) | 2026-09-12T12:18:58.581Z | <https://studio.tailorbrands.com/business/131807094/wizard/generate?prevId=766286289> | 생성 진행 92% 화면입니다. |
| brandmark-extra-33-natural-templates<br>[PNG](screenshots/brandmark-extra-33-natural-templates.png) · [스냅샷](snapshots/brandmark-extra-33-natural-templates.json) | 2026-09-12T12:19:06.483Z | <https://chat.brandmark.io/templates> | Natural을 선택해 템플릿 13개와 목록 끝 안내를 확인했습니다. |
| brandmark-extra-34-template-editor<br>[PNG](screenshots/brandmark-extra-34-template-editor.png) · [스냅샷](snapshots/brandmark-extra-34-template-editor.json) | 2026-09-12T12:19:14.154Z | <https://chat.brandmark.io/templates> | 첫 Use Template을 눌러 Cornora 템플릿 편집기를 열었습니다. |
| brandmark-extra-35-template-close-guard<br>[PNG](screenshots/brandmark-extra-35-template-close-guard.png) · [스냅샷](snapshots/brandmark-extra-35-template-close-guard.json) | 2026-09-12T12:19:31.766Z | <https://chat.brandmark.io/templates> | 템플릿 닫기에서 Save changes? 창의 Save·Discard·Close를 확인했습니다. |
| brandmark-extra-36-new-logo<br>[PNG](screenshots/brandmark-extra-36-new-logo.png) · [스냅샷](snapshots/brandmark-extra-36-new-logo.json) | 2026-09-12T12:19:40.495Z | <https://chat.brandmark.io/design> | Discard 후 New Logo에서 빈 캔버스를 열었습니다. |
| tailor-extra-20-after-99-percent<br>[PNG](screenshots/tailor-extra-20-after-99-percent.png) · [스냅샷](snapshots/tailor-extra-20-after-99-percent.json) | 2026-09-12T12:19:44.645Z | <https://studio.tailorbrands.com/business/131807094/wizard/generate?prevId=766286289> | 생성 진행 100% 전환 화면입니다. |
| brandmark-extra-37-marketing-entry<br>[PNG](screenshots/brandmark-extra-37-marketing-entry.png) · [스냅샷](snapshots/brandmark-extra-37-marketing-entry.json) | 2026-09-12T12:19:53.443Z | <https://brandmark.io/> | Brandmark 홈페이지와 새 앱·v3 진입 링크를 조사했습니다. |
| brandmark-extra-38-v3-entry<br>[PNG](screenshots/brandmark-extra-38-v3-entry.png) · [스냅샷](snapshots/brandmark-extra-38-v3-entry.json) | 2026-09-12T12:20:03.388Z | <https://brandmark.io/> | v3 링크 클릭 뒤 원래 페이지는 아직 홈페이지였습니다; 실제 v3 화면은 39입니다. |
| tailor-extra-21-results-boundary<br>[PNG](screenshots/tailor-extra-21-results-boundary.png) · [스냅샷](snapshots/tailor-extra-21-results-boundary.json) | 2026-09-12T12:20:06.119Z | <https://studio.tailorbrands.com/business/131807094/wizard/logos/766286290?selectedBrandVersionId=9448612715> | 결과 URL에서 로고 옵션 공개 전 필수 가입 오버레이를 확인했습니다; 가입하지 않았습니다. |
| brandmark-extra-39-v3-direct<br>[PNG](screenshots/brandmark-extra-39-v3-direct.png) · [스냅샷](snapshots/brandmark-extra-39-v3-direct.json) | 2026-09-12T12:20:26.526Z | <https://app.brandmark.io/v3/> | 명시된 v3 주소를 직접 열어 기존 앱의 이름·슬로건 입력 화면을 확인했습니다. |
| brandmark-extra-40-v3-keywords<br>[PNG](screenshots/brandmark-extra-40-v3-keywords.png) · [스냅샷](snapshots/brandmark-extra-40-v3-keywords.json) | 2026-09-12T12:20:40.784Z | <https://app.brandmark.io/v3/> | v3에서 Morrow Studio 입력 후 키워드 입력·추천 태그를 확인했습니다. |
| brandmark-extra-41-v3-colors<br>[PNG](screenshots/brandmark-extra-41-v3-colors.png) · [스냅샷](snapshots/brandmark-extra-41-v3-colors.json) | 2026-09-12T12:20:53.919Z | <https://app.brandmark.io/v3/> | 키워드 일반 텍스트만 입력된 상태입니다; 실제 색상 화면은 42입니다. |
| tailor-extra-22-initial-mode<br>[PNG](screenshots/tailor-extra-22-initial-mode.png) · [스냅샷](snapshots/tailor-extra-22-initial-mode.json) | 2026-09-12T12:20:57.432Z | <https://studio.tailorbrands.com/business/131807094/wizard/questions?id=766286287> | 공개 마법사로 돌아가 Initial Based 선택 후 아이콘 없이 스타일 단계로 이어짐을 확인했습니다. |
| tailor-extra-23-name-mode<br>[PNG](screenshots/tailor-extra-23-name-mode.png) · [스냅샷](snapshots/tailor-extra-23-name-mode.json) | 2026-09-12T12:21:19.306Z | <https://studio.tailorbrands.com/business/131807094/wizard/questions?id=766286287> | Name Based 선택 후 아이콘 없이 스타일 단계로 이어짐을 확인했습니다. |
| tailor-extra-24-about-return<br>[PNG](screenshots/tailor-extra-24-about-return.png) · [스냅샷](snapshots/tailor-extra-24-about-return.json) | 2026-09-12T12:21:30.467Z | <https://studio.tailorbrands.com/business/131807094/wizard/profile?id=766286286> | About으로 돌아가 업종과 설명이 유지됨을 확인했습니다. |
| brandmark-extra-42-v3-color-style<br>[PNG](screenshots/brandmark-extra-42-v3-color-style.png) · [스냅샷](snapshots/brandmark-extra-42-v3-color-style.json) | 2026-09-12T12:21:39.636Z | <https://app.brandmark.io/v3/> | 추천 leaf를 확정한 뒤 색상 스타일 단계로 진행했습니다. |
| brandmark-extra-43-v3-generation<br>[PNG](screenshots/brandmark-extra-43-v3-generation.png) · [스냅샷](snapshots/brandmark-extra-43-v3-generation.json) | 2026-09-12T12:21:53.290Z | <https://app.brandmark.io/v3/> | Organic 선택 후 v3 생성을 실행했습니다. |
| brandmark-extra-44-v3-results<br>[PNG](screenshots/brandmark-extra-44-v3-results.png) · [스냅샷](snapshots/brandmark-extra-44-v3-results.json) | 2026-09-12T12:22:02.181Z | <https://app.brandmark.io/v3/> | v3 결과 캐러셀과 Morrow Studio 워드마크를 확인했습니다. |
| brandmark-extra-45-v3-editor<br>[PNG](screenshots/brandmark-extra-45-v3-editor.png) · [스냅샷](snapshots/brandmark-extra-45-v3-editor.json) | 2026-09-12T12:22:11.080Z | <https://app.brandmark.io/v3/> | Edit를 눌러 하단 패널형 v3 편집기를 열었습니다. |
| brandmark-extra-46-v3-layout<br>[PNG](screenshots/brandmark-extra-46-v3-layout.png) · [스냅샷](snapshots/brandmark-extra-46-v3-layout.json) | 2026-09-12T12:22:20.478Z | <https://app.brandmark.io/v3/> | v3 Layout의 다섯 배치 도식을 확인했습니다. |
| brandmark-extra-47-v3-background<br>[PNG](screenshots/brandmark-extra-47-v3-background.png) · [스냅샷](snapshots/brandmark-extra-47-v3-background.json) | 2026-09-12T12:22:40.800Z | <https://app.brandmark.io/v3/> | v3 Background의 컨테이너·크기·위치·배경색 제어를 확인했습니다. |
| brandmark-extra-48-v3-color-picker<br>[PNG](screenshots/brandmark-extra-48-v3-color-picker.png) · [스냅샷](snapshots/brandmark-extra-48-v3-color-picker.json) | 2026-09-12T12:22:55.988Z | <https://app.brandmark.io/v3/> | v3 색상 선택기의 Color·Gradient·Saved와 HEX 입력을 확인했습니다. |
| brandmark-extra-49-v3-purchase<br>[PNG](screenshots/brandmark-extra-49-v3-purchase.png) · [스냅샷](snapshots/brandmark-extra-49-v3-purchase.json) | 2026-09-12T12:23:17.304Z | <https://app.brandmark.io/v3/> | v3 Purchase에서 Basic $25·Designer $65·Enterprise $175 공개 가격표를 확인했습니다. |
| tailor-extra-25-public-features<br>[PNG](screenshots/tailor-extra-25-public-features.png) · [스냅샷](snapshots/tailor-extra-25-public-features.json) | 2026-09-12T12:23:25.784Z | <https://www.tailorbrands.com/logo-maker> | 공개 Logo Maker 페이지의 기능·FAQ 전체 스냅샷을 저장했습니다; PNG는 페이지 상단입니다. |
| tailor-extra-26-feature-section<br>[PNG](screenshots/tailor-extra-26-feature-section.png) · [스냅샷](snapshots/tailor-extra-26-feature-section.json) | 2026-09-12T12:23:40.758Z | <https://www.tailorbrands.com/logo-maker> | 공개 페이지를 스크롤했습니다; PNG는 생성 유도 문구와 예시 로고 구간입니다. |
| tailor-extra-27-public-pricing<br>[PNG](screenshots/tailor-extra-27-public-pricing.png) · [스냅샷](snapshots/tailor-extra-27-public-pricing.json) | 2026-09-12T12:24:12.442Z | <https://www.tailorbrands.com/product-pricing> | 공개 Pricing 링크의 목적지가 LLC 가격 페이지임을 확인했습니다; 로고 가격이 아닙니다. |
