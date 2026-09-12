# Chrome + Codex Computer Use 추가 조사

사용자가 기존 Google 로그인 상태를 활용하기 위해 Chrome을 지정했고, 이번 작업 동안 Computer Use의 Chrome 앱 접근을 명시적으로 허용했습니다. 실제 `@oai/sky`의 앱 상태 읽기·접근성 요소 클릭·값 설정·키 입력으로 조작했습니다. Orca 내장 브라우저 캡처와 구분해 파일명에 `chrome`을 붙였습니다. native 화면 파일은 반환된 원래 JPEG이며 PNG로 확장자만 바꾸지 않았습니다.

계정 선택·개인 이메일·결제 상세 화면은 대표 스크린샷으로 저장하지 않습니다. 텍스트 스냅샷에 이메일이 있으면 지웠습니다. 결제는 실행하지 않았습니다.

## Design.com

- Chrome의 기존 계정 세션에서는 Download가 가입 화면 대신 저장된 draft와 Checkout으로 이어졌습니다. [연간 요금 화면](screenshots/design-chrome-01-checkout.jpeg).
- 해당 계정·시점의 연간 결제 월 환산 표시는 Starter $5, Value $6, Premium $7였고 기본 선택 Value의 연간 합계는 US$72였습니다. Monthly로 전환하면 $15/$24/$29, Value 합계 US$24/월이 표시됐습니다. 프로모션과 시점에 종속된 실측이며 일반 고정 가격이 아닙니다.
- 결제 화면에 표시된 Edit Design 링크로 [저장된 편집기](screenshots/design-chrome-02-saved-editor.jpeg)에 돌아갔습니다.
- ‘배경을 흰색, 아이콘을 짙은 초록으로 바꾸고 Morrow Studio 문구 유지’를 AI 패널에 입력·전송했습니다. [실제 수정 결과](screenshots/design-chrome-03-ai-edited.jpeg)는 요청을 수행했다는 응답과 캔버스를 보여줍니다. 응답은 원래 대문자 표기 MORROW STUDIO가 유지됐다고 설명했습니다. 모델의 자기 보고와 별도로 캔버스 확인이 필요합니다.
- [Preview](screenshots/design-chrome-04-preview.jpeg)는 여러 적용 예를 보여주며 Keep Editing과 Proceed To Download로 분기합니다.
- 유료 로고 파일은 구매하지 않았으므로 ZIP 실물이나 SVG 구조는 미검증입니다.

## Fiverr Logo Maker

Chrome의 기존 로그인 세션에서 Orca의 결과 목록 URL을 열어 같은 Morrow Studio 후보를 이어 봤습니다. 로고를 클릭하면 별도 탭에서 [변형 선택](screenshots/fiverr-chrome-01-variations.jpeg)이 열리고, Customize This Design 또는 Buy & Download로 나뉩니다.

[편집기](screenshots/fiverr-chrome-02-editor.jpeg)는 Suggested, Colors, Name, Slogan, Shape, Background, Layouts, My Drafts를 제공합니다. Reset, Undo, Redo, Make a Copy, Auto-align, Preview도 표시됩니다. 편집한 연구용 초안이 My Drafts에 잡히는 것을 관찰했습니다.

[Name의 실제 제어](screenshots/fiverr-chrome-03-typography.jpeg)는 문구, 폰트·굵기, 크기, 자간, Curve, 색, 가로·세로 위치입니다. 구형 공식 도움말만으로 확인하지 못했던 자간·곡선 기능을 현행 앱에서 확인했습니다.

한글은 글꼴에 따라 결과가 달랐습니다. Changa Light 200에서 `모로 스튜디오` 입력은 받았지만 [캔버스에는 빈 사각형](screenshots/fiverr-chrome-04-korean-test.jpeg)이 표시됐습니다. Font 검색에서 [Noto Sans KR](screenshots/fiverr-chrome-05-korean-font.jpeg)을 찾고 적용하자 [한글 문구가 정상 표시](screenshots/fiverr-chrome-06-korean-rendered.jpeg)됐습니다. 이는 해당 글꼴·해당 문구의 화면 렌더링 확인이며, 모든 한글 폰트나 유료 SVG 출력 검증을 의미하지 않습니다.

[Shape](screenshots/fiverr-chrome-07-shape-controls.jpeg)는 Show Shape를 켜면 도형 종류, 채움색, 너비·높이, 가로·세로 위치, Corner Radius가 나타납니다. 스위치는 접근성 트리에 조작 가능한 요소로 노출되지 않아 실제 스크린샷의 위치를 확인해 클릭했습니다. [Layouts](screenshots/fiverr-chrome-08-layouts.jpeg), [전체 팔레트](screenshots/fiverr-chrome-09-palettes.jpeg), [배경색](screenshots/fiverr-chrome-10-background.jpeg) 패널도 확인했습니다. 각 항목의 모든 값을 변경한 것은 아닙니다.

Buy & Download는 즉시 결제가 아니라 [패키지 선택](screenshots/fiverr-chrome-11-packages.jpeg)을 열었습니다. Essential US$30, Professional US$60, Unlimited US$90를 실측했습니다. PNG·투명 배경, 상위 상품의 SVG·웹/앱 파일·소셜 키트·가이드·Zoom 배경 및 수정 횟수 차이가 표시됐습니다. Buy now는 누르지 않았고 유료 파일을 받은 것으로 기록하지 않습니다.

## Tailor Brands

Google 계정 선택과 기본 프로필·이메일 동의를 거쳐 로그인했습니다. 기존 계정의 Logos에서 Create new를 골라 별도 `Morrow Studio` 시안을 생성했습니다. 기존 주 로고의 편집·교체 버튼은 사용하지 않았습니다. 계정의 기존 사업명이나 로고 목록 화면은 조사 캡처에 넣지 않았습니다.

[사업 설명](screenshots/tailor-chrome-02-brief.jpeg)을 입력하고 Initial Based를 선택했습니다. 이 경로는 별도 아이콘 검색 없이 [서체 느낌 세 개](screenshots/tailor-chrome-03-initial-styles.jpeg)를 고르게 했고, 로그인 후에는 실제 [이니셜 후보와 목업](screenshots/tailor-chrome-04-generated-initials.jpeg)이 나왔습니다. 공개 조사에서 막혔던 결과·편집 단계까지 확인한 것입니다.

[편집기](screenshots/tailor-chrome-05-editor.jpeg)의 Type은 Styles·Fonts·Text와 Name·Initial을 제공합니다. Text에서 이니셜 `M`을 `MS`로 입력하고 Save를 눌러 [실제 캔버스 수정](screenshots/tailor-chrome-06-initials-edited.jpeg)을 확인했습니다. 문구의 대소문자 선택과 태그라인 입력도 있습니다. [Shapes](screenshots/tailor-chrome-07-shapes.jpeg), [주색·보조색·추천 팔레트](screenshots/tailor-chrome-08-color.jpeg), [배치 대안](screenshots/tailor-chrome-09-layout.jpeg)을 열었습니다. Undo, Save, Saved, New Logo와 명함·웹·상품·소셜 적용 예도 표시됩니다. 모든 팔레트·서체 조합을 생성한 것은 아닙니다.

[Sample](screenshots/tailor-chrome-10-sample.jpeg)은 조사용 로고 페이지·QR과 무료 다운로드를 제공합니다. Download a sample을 실제 눌러 받은 [샘플](samples/tailor-morrow-sample.jpg)은 **200×200 RGB PNG**였습니다. 사이트의 원래 다운로드 파일명은 `LogoSample_ByTailorBrands.jpg`였지만 `file`과 `sips` 모두 PNG로 판별했습니다. 픽셀 변환 없이 사본을 보관했으며, 확장자만 보고 형식을 판단하면 안 된다는 사례입니다. 이 경쟁사 샘플은 연구 자료이며 플러그인 패키지에는 포함하지 않습니다.

Finish는 [디자인 검토](screenshots/tailor-chrome-11-review.jpeg) 후 완료 화면으로 이동합니다. 신규 시안의 Download 안내까지 이어서 확인했습니다. 유료 구독·결제는 실행하지 않았습니다.

Tailor의 Download는 계정의 브랜드 요금표로 이동했습니다. 연간 결제의 월 환산 금액은 Basic $3.99, Standard $5.99, Premium $12.99이며, Standard부터 Vector EPS가 표시됐습니다. 1 Month/1 Year/2 Years 선택이 있습니다. 이 화면에는 계정의 기존 주 로고가 함께 표시되어 연구 스크린샷으로 저장하지 않았습니다. 신규 시안을 기존 주 로고로 교체한 것은 아니며, 상품 Select·결제는 누르지 않았습니다.

## Looka

Orca에서 만든 연구용 draft URL을 Chrome에서 열면 [로고·브랜드 적용 예](screenshots/looka-chrome-01-draft-preview.jpeg)는 보였지만 동일한 편집 세션은 이어지지 않았습니다. 메뉴의 Log in → Google로 기본 프로필·이메일 동의를 진행했습니다. Looka는 [같은 이메일의 기존 계정이 있으므로 이메일·비밀번호로 로그인하라](screenshots/looka-chrome-02-account-boundary.jpeg)는 오류를 반환했습니다. 개인 이메일과 비밀번호는 화면에 입력·저장하지 않았습니다.

따라서 Chrome의 계정 편집·유료 다운로드는 미확인입니다. 로고 생성·Name·Layout 편집은 앞선 실제 Orca 사용 기록에 근거하며, 로그인 성공이나 Chrome 편집 완료로 바꾸어 서술하지 않습니다. 비밀번호 재설정이나 다른 계정 생성은 실행하지 않았습니다.

## Brandmark

Chrome에서 Google 로그인 후 일반 폼 생성과 별개인 [Icon Designer](screenshots/brandmark-chrome-01-icon-designer.jpeg)에 진입했습니다. 문장 입력·Auto Prompt 스위치·스타일 선택이 있습니다. [스타일](screenshots/brandmark-chrome-02-icon-styles.jpeg)은 Auto, Minimal, Sticker, Illustration, Line Art, 3D/Geometric, Cartoon입니다.

Minimal과 Auto Prompt를 유지한 채 ‘친환경 스튜디오의 녹색 새싹을 기하학 M 형태로, 흰 배경, 문구 없음’ [프롬프트](screenshots/brandmark-chrome-03-icon-prompt.jpeg)를 입력하고 Generate를 실제 실행했습니다. [생성 결과](screenshots/brandmark-chrome-04-generated-icon.jpeg)에는 후보와 확장된 설명이 나타났습니다. Refine은 추가 문구 창 없이 바로 처리에 들어가 [새 후보](screenshots/brandmark-chrome-05-refined-icon.jpeg)를 만들었습니다. 생성된 잎 아이콘은 화면상 Y에 가까운 실루엣도 포함하므로, ‘M 모양’ 요구를 완벽히 충족했다고 평가하지 않습니다.

[Paint](screenshots/brandmark-chrome-06-paint.jpeg)는 Edit Image 화면을 열며 브러시 크기 다섯 단계, 팔레트·사용자 색, 이미지 스포이트, Brush·Eraser, Undo·Redo, Clear, Save를 제공합니다. 도구를 확인하고 닫았으며 실제 브러시 스트로크 저장은 실행하지 않았습니다. 결과 도구에는 Variants와 Save Icon도 있습니다.

Variants도 실제 실행해 [변형 후보](screenshots/brandmark-chrome-07-icon-variants.jpeg)가 추가되는 것을 확인했습니다. Refine/Variants 모두 기존 결과 기록을 화면에 유지했습니다. 이 아이콘 생성 경로의 실측은 일반 Generate logos 폼과 구별합니다.

Save Icon을 누른 뒤 Saved logos에 [조사용 아이콘 카드](screenshots/brandmark-chrome-08-saved-icon.jpeg)가 생겼습니다. 카드를 다시 열어 [아이콘과 적용 예 미리보기](screenshots/brandmark-chrome-09-saved-preview.jpeg)를 확인했습니다. 이는 저장·재열기 확인이며 벡터 로고 편집기로 자동 연결됐다는 뜻은 아닙니다. 목록에는 구버전 저장 로고는 `app.brandmark.io/v3`에서 계속 지원한다는 안내도 표시됐습니다. 이 후속 조사에서 결제나 유료 벡터 다운로드는 하지 않았습니다.
