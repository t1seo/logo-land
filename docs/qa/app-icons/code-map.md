# 앱 아이콘 통합 코드 지도 및 검증 보고서

작성일: 2026-09-13 KST. 담당 작업: `icons_code_map`, `task_5715d03dd068`, dispatch `ctx_dbb7631c8fc7`.

이 보고서는 읽기 전용 코드·테스트 탐색 결과와 구현 권고를 구분합니다. 실제 변경한 파일은 이 보고서뿐이며, 이미지 생성·프로덕션 수정·테스트 실행·릴리스 상태 변경·하위 작업자 생성은 하지 않았습니다.

## 결론

앱 아이콘은 기존 `LogoType`에 추가할 로고 조형 종류가 아니라 별도의 **용도 의도**로 모델링하는 편이 안전합니다. `mascot`은 IP 캐릭터와 앱 아이콘 양쪽에 사용할 수 있고, 앱 아이콘에는 심볼·모노그램·추상 형태도 필요합니다. 기존 원본 PNG 저장, 부모 계보, 실제 프롬프트, 선택·검토·내보내기 흐름을 재사용하되 의도의 해석과 승인 조건을 추가하는 것이 핵심입니다.

가장 주의할 경계는 다음 네 가지입니다.

1. `build_prompt()`는 항상 로고와 브리프의 정확한 문구·슬로건을 요구합니다. 아이콘 분기를 마지막 문장 하나로 덧붙이면 기존 문구·락업 지시와 충돌합니다.
2. `import_image()`의 배경 기본값은 **원래 브리프**이며 부모 배경이 아닙니다. 이 동작은 기존 테스트로 고정되어 있습니다. 아이콘 상속을 추가하면서 배경 동작을 함께 바꾸면 안 됩니다.
3. 원본 보존과 승인 내보내기는 이미 다른 경계입니다. 사각형이 아니거나 색상 제약을 못 맞춘 정상 PNG도 창작 샘플로 보존하고, 승인 내보내기에서 실패 사유를 제시해야 합니다.
4. `docs/samples/gallery.js`는 `status === "exported"`일 때만 이미지·다운로드를 공개합니다. 한 번 생성한 창작 샘플을 보여주기 위해 이 상태를 허위로 설정해서는 안 됩니다.

## 1. 실제 기준 상태

| 항목 | 실제 확인 결과 |
| --- | --- |
| 작업 디렉터리 | `/Users/cillian/Documents/Github/Projects/logo-generator` |
| HEAD | `ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5` |
| `pyproject.toml` | `logo-land-helper`, 버전 `0.4.0`, Python `>=3.12` |
| 최초 `git status --short` | 출력 없음, 깨끗한 작업 트리였습니다. |
| 중간 동시 변경 | `.omo/drafts/logo-land-app-icons.md`가 다른 작업에 의해 untracked로 나타났습니다. 읽거나 수정하지 않았습니다. |
| 기존 테스트 수 | `docs/qa/color-workflow/final-tests.txt:6`에 `315 passed in 112.19s (0:01:52)`가 기록되어 있습니다. 이번 작업에서 재실행하거나 수집한 수치가 아닙니다. |
| 기존 미완료 상태 | `docs/qa/color-workflow/release.md:34`에 T8, 전체 검증 승인, T9 미완료가 명시되어 있습니다. |
| 기존 승인 공백 | `release-state.json`의 `whole_goal_complete=false`, `public_release_ready=false`; 승인된 제한색·흰색 투명 native 출력이 남아 있습니다. |

릴리스 관련 내용은 **저장된 감사 기록**을 확인한 것이며 GitHub의 현재 릴리스 상태를 새로 조사한 것은 아닙니다. 이 작업은 해당 기록·계획 체크박스·버전·태그·배포 상태를 변경하지 않았습니다.

## 2. 모델과 저장 경계

아래 경로에서 `H/`는 `skills/logo-land/scripts/logo_helper/`를 뜻합니다.

| 파일·심볼 | 현재 역할과 앱 아이콘 접점 |
| --- | --- |
| `H/model_base.py:36` `FrozenModel` | `frozen=True`, `extra="forbid"`, `strict=True`입니다. 임의 키, 문자열 boolean, 타입 강제를 허용하지 않는 새 의도 모델의 기반입니다. |
| `H/model_base.py` `LogoType`, `Text`, `schema_integer` | 로고 종류 8개에 이미 `mascot`이 있습니다. `Text`는 공백만인 값을 거부하고 최대 20,000자입니다. 버전은 JSON 정수여야 하므로 `true`, `1.0`, `"1"`을 거부합니다. |
| `H/brief_models.py:11` `Brief` | 정확한 문구 최대 2,000자, `logo_type`, 자유 텍스트 스타일·팔레트·용도, 선택적 `lockup`, 배경, 시안 수를 보관합니다. 앱 아이콘 의도는 없습니다. `exact_text=""`는 현재 허용됩니다. |
| `H/lockup_models.py:8` `LockupIntent` | horizontal/stacked, symbol start/end, text alignment, typography style, 선택적 font reference입니다. 마지막 두 값은 외형 요청이며 실제 폰트 사용 증명이 아닙니다. |
| `H/artifact_models.py:53` `Artifact` | 원본 경로·SHA-256·실측 PNG 정보·최종 프롬프트·부모 ID·배경·팔레트 ID·락업을 저장합니다. 이미지 의도와 승인 검토는 구분되어 있습니다. |
| `H/artifact_models.py:13` `VisualReview` | reviewer/notes와 다섯 boolean의 명시적 검토입니다. `passed`는 다섯 값 모두 true일 때만 true이며 사용자 선택이나 플랫폼 적합성 증명은 아닙니다. |
| `H/artifact_models.py:75` `FailedAttempt` | 실제 실패의 프롬프트·이유·부모·시각만 기록합니다. 도구 시도 횟수, one-pass 정책, 의도 스냅샷은 없습니다. |
| `H/session_models.py:25` `Session` | 스키마 v2, revision, 브리프, 순서가 있는 아티팩트·팔레트 계보, 선택, 실패, 내보내기, 참조·색상 보고서를 보관합니다. |
| `H/session_models.py:44` 이후 validators | 부모가 앞에 있어야 하며 중복·누락·부정 경로·잘못된 선택을 거부합니다. 팔레트·참조 해시·보고서의 artifact/hash/palette/digest 결합도 검사합니다. |
| `H/models.py` | 분리된 엄격 모델의 public import facade입니다. 새 의도를 여러 모듈에 흩어진 dict로 전달하지 말고 여기에 명시적으로 노출할 수 있습니다. |

### 기존 버전과 마이그레이션

`H/legacy_state.py:117`의 `LegacySession`은 v1 전용이며 `LegacyBrief`, `LegacyArtifact`, review/failure/export 모델도 별도로 고정되어 있습니다. `parse_stored_session()`은 `LegacySession | Session`을 검증하고, `parse_session()`은 검증된 v1을 메모리에서만 v2로 바꿉니다. 기존 v1에 `lockup`을 끼워 넣어도 거부합니다.

`H/storage.py:129`의 `Store.load()`는 매번 실제 PNG 해시·디코딩 정보와 참조 해시를 재검증합니다. `show`, `list`, `prompt`는 마이그레이션 파일을 쓰지 않습니다. `Store.save():161`은 저장 모델을 다시 파싱하고, 기존 아티팩트의 review/reviewed_at을 제외한 필드와 팔레트·참조·색상 보고서 prefix를 비교해 변경을 거부합니다. v1 첫 쓰기에는 원래 바이트 그대로 `session.v1.backup.json`을 생성하며 다른 내용의 백업은 덮어쓰지 않습니다.

**권고:** 새 저장 계약은 v3로 명시하고 v1/v2 읽기 호환성을 유지하는 안을 우선 검토해 주세요. v2에 nullable 필드만 추가하면 새 helper가 옛 v2를 읽는 것은 쉽지만, `extra="forbid"`인 기존 0.4.0 helper는 새 필드가 null이어도 거부합니다. 따라서 이를 양방향 호환이라고 설명할 수 없습니다. v3는 이 단절을 버전으로 드러내는 선택이며, 이 보고서가 제품 버전이나 릴리스 변경을 수행한 것은 아닙니다.

- 기존 v1 파서의 허용 필드를 넓히지 않고, 기존 v2 brief/artifact/review/session 계약도 별도 고정 모델로 보관하는 방식이 안전합니다. 새 `Brief`나 `Artifact`를 v2 파서에서 재사용하면 새 필드가 과거 스키마로 유입됩니다.
- v1/v2를 현재 모델로 읽을 때 새 의도·아이콘 검토·생성 시도 증거는 `None`으로 유지합니다. `use_cases`, 프롬프트의 “icon”, 사각형 크기, 얼굴 모양을 보고 앱 아이콘이라고 추정하지 않습니다.
- 읽기와 프롬프트 작성은 원래 세션 바이트를 보존하고, 첫 성공한 쓰기에서만 해당 버전 백업과 v3 상태를 기록하는 기존 원칙을 확장합니다. 기존 v1 백업이 있는 v2에는 그 백업도 그대로 남겨야 합니다.
- 새 의도 스냅샷은 기존 아티팩트의 immutable 비교에 포함합니다. 검토 필드만 갱신할 수 있으며 과거 이미지에 앱 아이콘 의도를 소급 부여하지 않습니다.
- 새 내보내기 manifest도 새 계약임을 명시해야 합니다. 기존 PNG/manifest/ZIP 파일을 재작성하거나 재해석하지 않습니다.

## 3. 권장 의도 계약과 상속

다음은 **제안**이며 현재 구현되어 있지 않습니다.

| 계약 | 권장 내용 |
| --- | --- |
| `AssetIntent` | `kind`를 discriminator로 하는 `LogoIntent | AppIconIntent`, 저장 필드는 `AssetIntent | None`으로 둡니다. `None`은 과거/미기록 상태이고 `LogoIntent(kind="logo")`는 명시적 로고 전환입니다. |
| `AppIconIntent` | `kind="app_icon"`, `form=mascot|symbol|monogram|abstract|object`, `canvas="square"`, `corner_treatment=unmasked|rounded_artwork`, `composition=centered|lower_corner` 등을 엄격한 Literal로 표현합니다. 스타일·재질·분위기는 기존 스타일/컨셉을 사용하여 모든 아이콘을 같은 캐릭터 스타일로 제한하지 않습니다. |
| 아이콘 문구 | `lettering`을 `mode="none"` 또는 `mode="exact", text=<제한된 비공백 문자열>`인 판별 union으로 둡니다. `monogram`에는 exact 문구가 필요합니다. 아이콘 문구는 기존 브리프 문구와 독립적이며 역사적 브리프를 수정하지 않습니다. |
| 모서리 의미 | `unmasked`는 사각 원본의 바깥 모서리를 OS 모양으로 미리 자르지 않는다는 요청입니다. `rounded_artwork`는 요청한 시각 요소이며 플랫폼 마스크 인증이 아닙니다. 둥근 캐릭터 몸체와 출력 캔버스 마스크를 같은 필드로 취급하지 않습니다. |
| 배경·색상 | 색을 새 의도 객체에 중복 저장하지 않습니다. 기존 `requested_background`, `PaletteVersion`, `ColorConstraints`를 계속 사용합니다. 앱 아이콘이라는 이유로 투명도 요구나 엄격 팔레트를 조용히 바꾸지 않습니다. |
| 저장 위치 | 브리프에 신규 루트 기본값, Artifact에 해석이 완료된 immutable snapshot, PromptResult에 같은 해석 결과를 둡니다. 별도 전역 active-icon 상태나 임의 문자열 사전은 필요하지 않습니다. |

`H/intent.py:20`의 `resolve_intent()`를 프롬프트와 import의 공통 해석 지점으로 유지해 주세요. 새 의도는 전체 객체를 교체하는 방식으로 해석하면 부분 dict 병합의 모호함을 피할 수 있습니다.

| 상황 | 제안하는 새 asset intent 우선순위 |
| --- | --- |
| 부모 없는 생성 | 명시적 override → 브리프 asset intent → `None` |
| 부모 있는 편집 | 명시적 override → 부모의 기록된 asset intent **그대로** |
| 과거 부모의 intent가 `None` | `None`을 유지합니다. 브리프의 새 기본값으로 소급 추정하지 않습니다. |
| 아이콘 부모를 로고로 전환 | 명시적 `{"kind":"logo"}`가 있어야 합니다. null/누락은 상속 의미로 남깁니다. |
| 재선택·내보내기 | 선택된 Artifact의 snapshot만 사용합니다. 최신 브리프나 나중에 가져온 형제 의도를 가져오지 않습니다. |

현재 팔레트는 명시 override → 부모 palette ID(없으면 그대로 unknown) 또는 루트 active palette 순서입니다. 현재 락업은 명시 override → 부모 락업 → 브리프 락업이며, 부모의 null은 브리프로 fallback합니다. 이 차이를 새 의도와 혼동하지 않아야 합니다.

아이콘으로 명시 전환할 때 과거 브리프/부모의 **상속된** 조합형 락업과 전체 브랜드 문구는 역사적 설명으로만 남기고 아이콘 생성 지시에서 제외하는 안을 권고합니다. 아이콘 override와 **명시적인** `--lockup-file`을 동시에 주면 `intent_conflict`로 거부해야 합니다. 아이콘 문구는 `lettering`이 유일한 생성 기준입니다. 모노그램인데 문구가 없거나, 금지색/허용색/그라디언트 정책이 충돌하는 요청도 도구 호출 전에 거부해야 합니다.

## 4. CLI·프롬프트·import 접점

실제 실행한 help의 전체 진입점은 다음과 같습니다.

```text
reference-add, palette-propose, palette-add, color-analyze, color-gallery,
init, list, show, prompt, import, select, review, export, failure
```

| 표면 | 실제 확인한 옵션 / 제안 |
| --- | --- |
| `logo_project.py:84` `prompt_command` | `--session --concept --parent --changes --palette --lockup-file`; `--background`나 아이콘 옵션은 없습니다. `--intent-file`을 구조화 JSON 경계로 추가하고 동일한 파서를 import에서도 쓰는 안을 권고합니다. |
| `logo_project.py:108` `import_command` | `--session --artifact --image --prompt-file --revision --parent --palette --lockup-file --background opaque\|transparent`; 실제 최종 프롬프트 파일과 실제 이미지 경로를 읽습니다. |
| `logo_project.py` `review` | `--session --artifact --review-file --revision`; 기존 boolean을 임의로 true로 채우면 안 됩니다. |
| `logo_project.py` `export` | `--session --revision --output`; 선택된 검토 완료 PNG만 패키징합니다. 샘플용 우회 flag를 추가하지 않는 편이 안전합니다. |
| `color-gallery` | `--session --artifacts --output`; 명시된 아티팩트의 원본 사본을 갤러리로 발행하며 상태를 저장하지 않습니다. |
| `H/cli_options.py:26` `parse_lockup` | bounded regular file → strict JSON 모델이라는 `parse_asset_intent` 구현 패턴으로 재사용할 수 있습니다. |
| `logo_project.py:204` `main` | `ProjectError`, Pydantic validation, OS, Unicode 오류를 stderr JSON과 exit 1로 번역합니다. Typer 인자 오류는 exit 2입니다. 새 코드도 이 경계를 사용해야 합니다. |

### 프롬프트

`H/prompts.py:36`의 `build_prompt()`는 편집에 parent와 nonempty changes가 모두 있는지 검사합니다. 부모의 실제 경로·의도 배경을 반환하며 최신 변경을 우선하고, structured palette를 역사적 팔레트보다 권위 있는 지시로 붙입니다. `PromptResult`는 revision, parent, palette ID/digest, lockup을 반환하지만 실제 도구 호출이나 결과와 암호학적으로 결합되어 있지는 않습니다.

아이콘용 본문을 별도 `icon_prompts.py` 같은 작은 모듈에 두고 **공통 본문 생성 전에** 분기하는 안을 권고합니다. 원본 사각 PNG, 한 개의 독립 결과, 구체적 형태·문구 정책·모서리·구성, 작은 크기 식별성, 요청한 색상/배경을 기술할 수 있습니다. 앱 스크린샷, 기기 프레임, 연락처 시트, 꾸며낸 벡터나 플랫폼 패키지를 생성 산출물로 요구해서는 안 됩니다. mascot 로고의 기존 경로는 유지해야 합니다.

자유 입력 `concept`, `changes`, 브랜드 설명, 참조 provider 응답은 데이터입니다. `changes`를 권위 있다고 부르는 현재 문장이 구조화 정책까지 무력화하지 않도록 요청 데이터를 명확하게 구획하고, 정책은 마지막에 명시하며, 의미 충돌은 모델/해석 경계에서 검사하는 편이 안전합니다. 프롬프트 문장만으로 prompt injection이나 픽셀 적합성이 해결되었다고 주장할 수는 없습니다.

### 원본 import와 도구 지연

`H/workflow.py:54`의 `import_image()`는 파일을 읽고 PNG를 완전히 디코딩한 후 lock/revision을 확인합니다. 의도를 해석하고 Artifact를 만들며, 팔레트가 있으면 최초 색상 보고서를 만든 다음 원본 바이트를 exclusive write하고 상태를 저장합니다. 상태 저장 오류에는 이번에 만든 PNG만 되돌립니다. `H/import_reports.py:20`의 `initial_report()`는 예상된 분석 실패를 unverified 보고서로 남겨 정상 PNG import를 보존합니다.

아이콘 의도도 이 snapshot 생성에 포함하되 **의도상 정사각형인데 실제 이미지가 직사각형이라는 이유로 import 자체를 거부하지 않는** 편이 요구에 맞습니다. 실제 폭·높이·알파·프롬프트를 남기고 부적합 결과를 창작 샘플로 검토할 수 있어야 합니다. PNG 형식·해시·경로 검증은 기존처럼 필수입니다.

도구 실행 전 저장한 PromptResult의 revision과 의도 JSON을 import에도 그대로 전달해야 합니다. generation 중 다른 mutation이 생기면 기존 `stale_revision`이 import를 막습니다. 단순히 새 revision으로 재시도하여 최신 의도를 원본 결과에 붙이면 안 됩니다. 원래 결과와 정확한 프롬프트를 보존한 뒤 부모·팔레트·락업·asset intent의 일치 여부를 확인해야 합니다. 현재 CLI는 최종 프롬프트 내용과 구조화 옵션이 일치하는지 스스로 증명하지 않으므로, 이를 자동 보장한다고 문서화해서는 안 됩니다.

## 5. 창작 샘플, 엄격 검증, 승인 내보내기

현재 `H/delivery.py:107`의 `export()`는 순서대로 selection, 모든 명시적 visual review, 요청/실측 배경 일치, 새 목적지, 원본 hash, fresh color evidence를 검사합니다. `H/color_delivery.py:112`의 `export_colors()`는 저장된 pass를 그대로 신뢰하지 않고 원본을 다시 측정합니다. strict에는 선행 determinate 보고서와 새 적합 측정이 필요하고, advisory/unknown은 한계를 manifest에 남깁니다. ROI가 있으면 그 범위를 유지하므로 전체 이미지 적합성이라고 부르면 안 됩니다.

| 단계 | 권고하는 의미 |
| --- | --- |
| 한 번 생성한 창작 샘플 | 실제 시도 한 번의 원본 PNG·정확한 최종 prompt·시도 결과를 보존합니다. 실패도 실패로 남기고 자동 수정이나 재생성으로 one-pass 통계를 숨기지 않습니다. |
| 구조화 적합성 | 형식/크기/배경/색상은 실제 데이터로 확인하고, 글자·모서리·구성·식별성은 명시적 시각 검토가 필요합니다. 미검증·불일치·판정 불가를 구분합니다. |
| 승인/선택 | 기존 selected ID와 사용자 선택 또는 위임의 근거를 사용합니다. `VisualReview.passed`는 사용자 승인으로 자동 승격되지 않습니다. |
| 내보내기 완료 | 실제 `export` transaction이 성공한 아티팩트와 manifest/ZIP의 존재·해시를 근거로 표시합니다. 샘플 상태가 이 단계를 건너뛰지 않습니다. |

새 generation 증거를 추가한다면 `None | NativeAttempt`로 두고 `policy=one_pass|iterative`, 명시적 시도 ID/순서, host call 식별자(실제로 제공될 때만)를 보관하는 정도부터 시작할 수 있습니다. 과거 결과에 `attempt_count=1`을 기본으로 채우면 안 됩니다. 현재 `Artifact`와 `FailedAttempt`만으로 native 호출 횟수를 정확히 계산할 수 없으며, helper 자체가 도구를 호출하지 않으므로 one-pass 여부의 근거는 host 기록이어야 합니다.

아이콘에만 필요한 `AppIconReview`를 v3 `VisualReview`의 optional typed 필드로 추가해 미기록 상태를 유지하고, export의 아이콘 분기에서 실제 square 여부와 이 검토의 문구·모서리/마스크·small-size 결과를 요구하는 안을 권고합니다. 기존 로고 검토 JSON의 의미는 유지합니다. 새 검토 값을 별도 mutable artifact 필드로 흩뿌리기보다 기존 review 안에 두면 `Store.save()`의 review 갱신 예외를 확장할 필요가 줄어듭니다.

`H/export_bundle.py:19`의 `publish_bundle()`은 `logo.png`, `manifest.json`, `brand-guide.md`, 이를 담은 `logo-package.zip`을 staging 후 exclusive하게 발행합니다. PNG는 재인코딩하지 않습니다. 파일명은 첫 통합에서 그대로 유지해 소비자 호환성을 줄이고, manifest에 선택된 asset intent·실제 크기·검토 범위를 추가하는 편이 작습니다. guide의 역사적 전체 문구와 선택된 아이콘 문구를 구분해야 합니다. `manifest.source.prompt`에는 원문이 보존되지만 guide의 blockquote는 표현용이므로 원문 파일 대용으로 취급하지 않습니다.

플랫폼 지정 픽셀 크기, adaptive icon foreground/background, Xcode asset catalog, ICO/ICNS, SVG/EPS/AI 등은 실제 생성·검증 없이는 포함되었다고 주장할 수 없습니다. 여기서는 **native PNG artwork**만 다룹니다. 플랫폼 규격 적합성을 제품 기능으로 추가하려면 그때 해당 공식 규격을 별도 확인해야 하며 이번 코드 탐색은 그 인증을 하지 않았습니다.

## 6. 갤러리 접점

`H/color_gallery.py:30`의 `artifact_card()`는 원본 다운로드·팔레트 의도·저장된 측정·락업을 표시합니다. `render_color_gallery():49`는 명시적 ID만 복사하고 해시를 확인하며 기존 목적지·예약 저장소를 거부합니다. `H/color_gallery_data.py`는 HTML escape를 적용하고 “stored measurement only”, legacy/unknown과 unverified를 구분합니다. full prompt, 절대 로컬 경로, 비선택 참조를 공개하지 않는 것은 기존 테스트와 `references/project-files.md:210`에 명시된 계약입니다.

최소 추가는 asset intent/실제 이미지 facts/검토 상태를 이 갤러리에 보여주는 것입니다. 내부 session의 정확한 prompt 보존과 공용 갤러리의 prompt 공개는 다른 결정입니다. 기존 color gallery에 전체 prompt를 자동 노출하면 privacy 회귀가 됩니다. 사용자 요청으로 작성하는 공개 창작 샘플은 별도 명시적 sample data/파일에 정확한 prompt를 포함하고, 새 raw PNG 링크와 승인 export 링크를 구분하는 편이 안전합니다.

`docs/samples/gallery.js:17`의 `exported()`, `:25`의 `localPath()`, `:27`의 `renderDownloads()`, `:50`의 `openSample()`, `:107`의 `makeCard()`가 정적 샘플의 접점입니다. 현 경로 검증은 `items/<id>/delivery/<file>`만 허용합니다. native 샘플 보관 경로를 추가하려면 필요한 local 패턴만 열고 임의 URL/경로는 계속 거부해야 합니다. `data.js`는 `window.LOGO_SAMPLES`라는 수동 데이터이며 엄격한 Python schema와 자동 동기화되지 않습니다.

제안하는 표시 모델은 생성 결과(`pending/failed/generated`), 검증(`unverified/mismatch/indeterminate/pass`), 선택/승인, 내보내기(`없음/실제 경로`)를 각각 사실에 근거해 분리하는 것입니다. 원본 미리보기와 PNG 다운로드는 generated 여부·실제 파일 로딩으로, ZIP/가이드는 실제 export 증거로 활성화합니다. HTML은 `textContent`/escape를 유지하고, 시각 미리보기용 CSS rounded mask와 실제 원본 모서리 검사 화면도 구분해야 합니다.

## 7. 소유권 경계와 모듈 크기

`wc -l`로 실제 물리 줄 수를 확인했습니다. Python production 파일은 모두 250줄 이하입니다. `logo_project.py` 214, `storage.py` 207, `color_analysis.py` 205, `legacy_state.py` 181, `color_models.py` 167, `delivery.py` 166, `workflow.py` 161, `session_models.py` 135, `prompts.py` 113, `color_gallery.py` 109, `color_gallery_data.py` 100입니다. 이 수치는 주석·공백을 포함한 줄 수이며 pure LOC 측정은 아닙니다.

| 후속 소유자 경계 | 담당 파일 / 의존성 |
| --- | --- |
| 모델·호환성 담당 | 새 `asset_intent_models.py`, 새 frozen v2 모델, `brief_models.py`, `artifact_models.py`, `session_models.py`, `legacy_state.py`, `models.py`, `storage.py`; schema/상속/필드 이름을 먼저 고정하고 전용 모델·마이그레이션 테스트를 소유합니다. |
| CLI·프롬프트·import 담당 | `intent.py`, `cli_options.py`, `logo_project.py`, `prompts.py`, 새 `icon_prompts.py`, `workflow.py`; 모델 계약 이후 시작하며 저장 모델 파일을 동시에 수정하지 않습니다. |
| 승인 내보내기 담당 | `delivery.py`, 새 `icon_delivery.py` 또는 검토 helper, `color_guide.py`와 필요한 `export_bundle.py`; 기존 엄격 색상 알고리즘·임계값을 변경하지 않습니다. |
| 갤러리 담당 | `color_gallery*.py`, 해당 template, 선택된 공개 샘플용 HTML/JS/data; approval/export 상태를 직접 만들어내지 않으며 모델·export 계약 이후 통합합니다. |
| 사용 흐름 문서 담당 | `skills/logo-land/SKILL.md`, `references/project-files.md`, 필요하면 별도 app-icon 참고 문서; one-pass와 strict 후속 작업, 최종 prompt 보관 규칙을 명시합니다. 기존 릴리스 문서는 담당하지 않습니다. |

`storage.py`와 진입 스크립트는 확장 여유가 작으므로 버전 백업/파서와 icon CLI 등록 등을 작은 모듈로 나눌 수 있습니다. 현재 큰 테스트 파일은 `test_palette_engine.py` 296, `test_color_reports.py` 291, `test_color_gallery.py` 290, `test_color_analysis.py` 277, `test_color_models.py` 268줄입니다. 새 아이콘 테스트는 별도 작은 파일로 두고 관련 없는 기존 테스트를 재구성하지 않는 편이 안전합니다. 이 보고서에서 위 소유자들을 생성하거나 작업을 배정하지 않았습니다.

## 8. 정확한 기존 회귀 테스트 위치

아래는 소스에서 이름과 검증 내용을 확인한 테스트입니다. **이번 작업에서 실행하지 않았습니다.**

| 주제 | 기존 테스트 |
| --- | --- |
| 배경 역사/상속 | `tests/test_background_compatibility.py::test_import_defaults_to_original_brief_when_parent_requested_another_background`; `::test_legacy_session_when_background_intent_is_missing_or_null`; `::test_import_rejects_when_background_option_is_invalid` |
| 배경 편집·재선택 | `tests/test_background_variants.py::test_prompt_when_parent_background_differs_from_original`; `::test_export_when_child_requests_opposite_background`; `::test_export_rejects_when_child_pixels_mismatch_explicit_background`; `::test_export_when_original_is_selected_after_opposite_child_import` |
| 락업·문구 | `tests/test_color_models.py::test_lockup_roundtrip_preserves_exact_text_and_requested_font`; `tests/test_palette_workflow.py::test_lockup_when_parent_has_explicit_override` |
| 팔레트 prompt/import 결합 | `tests/test_palette_workflow.py::test_palette_when_parent_differs_from_active`; `::test_import_when_palette_or_revision_is_invalid`; `tests/test_cli_workflow.py::test_prompt_when_edit_changes_color` |
| strict 모델 | `tests/test_color_models.py::test_constraints_reject_coercion_and_unknown_fields`; `::test_constraint_conflicts_have_stable_code`; `::test_report_binding_and_measurement_tampering_is_rejected` |
| 실제 색상 측정 | `tests/test_color_analysis.py::test_known_black_ivory_passes_and_bytes_stay_identical`; `::test_restricted_99_percent_boundary`; `::test_required_presence_boundaries`; `::test_roi_limits_scope_and_legacy_intent_stays_unverified`; `::test_transparent_hidden_red_cannot_fail_white_lettering` |
| v1 무기록 읽기·백업 | `tests/test_palette_compatibility.py::test_legacy_reads_do_not_write_and_first_select_migrates`; `::test_failed_migration_reuses_verified_backup`; `::test_mismatched_backup_is_never_overwritten`; `::test_strict_legacy_and_future_version_rejection`; `::test_legacy_version_requires_a_json_integer` |
| 과거 계보·불변성 | `tests/test_palette_compatibility.py::test_legacy_migration_preserves_edited_lineage_selection_and_exports`; `::test_existing_artifact_cannot_gain_retroactive_palette_intent`; `::test_new_init_writes_v2_and_review_can_be_first_migration` |
| 재선택 export truth | `tests/test_delivery_guide.py::test_old_selected_parent_exports_its_palette_and_lockup`; `::test_guide_records_selected_edit_request_when_palette_has_changed`; `::test_legacy_export_stays_color_unverified`; `::test_export_preserves_explicit_roi_and_discloses_scope` |
| 승인·신선한 strict 증거 | `tests/test_cli_workflow.py::test_export_when_visual_review_failed`; `tests/test_color_reports.py::test_strict_export_requires_existing_analysis`; `::test_export_recomputes_forged_report_metrics`; `::test_strict_export_requires_determinate_evidence`; `::test_export_appends_fresh_report_with_original_zip_bytes`; `::test_advisory_mismatch_exports_with_explicit_warning` |
| 메타데이터 실패/정직한 한계 | `tests/test_color_export_compatibility.py::test_non_strict_export_preserves_png_with_unassessable_metadata`; `::test_strict_export_cannot_promote_unassessable_metadata_to_pass`; `::test_metadata_fallback_does_not_bypass_original_integrity`; `::test_color_export_does_not_swallow_integrity_or_programming_errors` |
| 갤러리/공개 제한 | `tests/test_color_gallery.py::test_explicit_artifacts_are_portable_byteidentical_and_readonly`; `::test_candidate_cards_escape_text_and_hide_private_evidence`; `::test_reports_keep_status_intent_measurement_and_font_truth`; `::test_brand_xss_is_inert`; `::test_unbound_report_pass_is_never_color_verification`; `tests/test_color_cli_integration.py::test_gallery_when_read_only` |
| 실패·트랜잭션 | `tests/test_transactions.py::test_import_rolls_back_when_state_commit_fails`; `::test_export_rolls_back_when_state_commit_fails`; `::test_cli_update_refuses_when_another_writer_holds_lock`; `tests/test_color_workflow_transactions.py::test_import_when_analysis_fails`; `tests/test_color_reports.py::test_color_report_rolls_back_when_publish_fails` |
| 경로·재개 | `tests/test_resume_and_portability.py::test_import_preserves_orphan_file_when_untracked_path_exists`; `::test_resume_rejects_when_stored_state_is_tampered`; `::test_cli_runs_when_only_skill_scripts_are_copied`; `tests/test_reserved_output.py::test_export_rejects_reserved_output_before_creating_storage`; `tests/test_cli_safety.py::test_resume_when_artifact_hash_changed` |

## 9. 후속으로 추가할 테스트와 적대적 시나리오

다음 node 이름·시나리오는 **새 제안**입니다. 이 파일들은 아직 없고 테스트를 통과했다고 주장하지 않습니다.

| 제안 파일·테스트 | 구체적 검증 |
| --- | --- |
| `test_app_icon_models.py::test_rejects_malformed_asset_intent` | 알 수 없는 kind/form, 문자열 boolean, 여분 키, null 내부 필수 필드, 빈 exact 문구, monogram+no-text를 JSON 경계에서 거부하고 상태를 바꾸지 않습니다. |
| `test_app_icon_models.py::test_logo_type_remains_independent` | logo+mascot과 app_icon+mascot/symbol/abstract/monogram/object가 구분되며 과거 mascot이 자동 아이콘이 되지 않습니다. |
| `test_app_icon_compatibility.py::test_v1_v2_reads_are_byte_preserving` | 실제 고정 v1/v2 fixture를 fresh process에서 show/list/prompt하고 원본 state/PNG hash 불변과 새 필드 None을 확인합니다. 현재 모델 dump에서 필드를 빼 만든 fixture에만 의존하지 않습니다. |
| `test_app_icon_compatibility.py::test_first_write_backs_up_each_legacy_schema` | select/review/import/export 각각 첫 mutation, v1/v2별 백업·실패 후 재사용·백업 충돌 거부를 확인합니다. unknown version, bool/float/string version, v1/v2에 끼운 새 필드를 거부합니다. |
| `test_app_icon_compatibility.py::test_existing_artifact_intent_is_immutable` | 과거 Artifact에 icon intent를 추가하거나 기존 icon snapshot을 변경한 save가 실패하고, review 갱신만 성공합니다. |
| `test_app_icon_workflow.py::test_prompt_import_share_parent_intent` | 부모 없는 기본값, 명시 override, 다른 brief의 아이콘 부모, None인 과거 부모, 명시 logo 전환을 표로 검증합니다. prompt 반환 의도와 import snapshot이 같아야 합니다. |
| `test_app_icon_workflow.py::test_icon_transition_handles_historical_lockup` | 조합형 로고 부모→no-text icon에서 과거 브랜드/락업은 역사만 남고 active text 지시에서 빠집니다. 명시 icon+명시 lockup은 안정적 `intent_conflict`로 거부합니다. |
| `test_app_icon_prompts.py::test_free_text_cannot_rewrite_structured_intent` | concept/changes에 `ignore prior instructions`, 가짜 JSON key, 줄바꿈, backticks/`$(...)`, `</script>`를 넣습니다. 요청 데이터로만 남고 모델 상태·의도·명령 실행·HTML DOM을 바꾸지 않아야 합니다. native 모델의 의미적 불복종 방지까지 증명하는 테스트는 아닙니다. |
| `test_app_icon_prompts.py::test_no_text_and_exact_lettering_branches` | no-text 아이콘에 기존 `copy verbatim` 브랜드/슬로건 지시가 없고, exact 한글/모노그램은 공백·Unicode를 그대로 유지하며 로고 프롬프트는 회귀하지 않습니다. |
| `test_app_icon_workflow.py::test_stale_generation_import_preserves_original` | prompt revision을 저장하고 중간 palette mutation 후 원본을 import합니다. stale 오류, PNG orphan 없음, state 불변을 확인하고, 원본 파일·prompt는 남겨 재개할 수 있어야 합니다. |
| `test_app_icon_delivery.py::test_nonconforming_native_sample_is_preserved` | 정상 직사각 PNG, 요청과 다른 알파/색상 각각 import 성공·원본 바이트 보존을 확인하고, approved export는 각각 구체적 이유로 거부해야 합니다. |
| `test_app_icon_delivery.py::test_selected_parent_exports_its_own_intent` | 다른 아이콘/로고/팔레트 형제를 추가한 뒤 이전 부모를 선택합니다. manifest/guide/ZIP는 선택된 부모의 문구·의도·원본 bytes만 담아야 합니다. |
| `test_app_icon_delivery.py::test_icon_export_requires_scoped_review` | 누락된 아이콘 검토, false small-size/lettering/corner 검토, 위조 stored color pass는 승인 export를 허용하지 않습니다. pass여도 raster만 포함하고 플랫폼/벡터 번들은 없습니다. |
| `test_app_icon_gallery.py::test_generated_sample_is_not_exported` | generated/unverified 샘플은 원본+정확한 공개 prompt를 볼 수 있지만 ZIP·approved 배지는 없고, 실패 샘플은 이미지가 있는 것처럼 표시되지 않습니다. |
| `test_app_icon_gallery.py::test_private_color_gallery_keeps_prompt_private` | 기존 color gallery는 새 intent를 inert text로만 표시하고 full prompt/절대경로/참조 provider 응답은 계속 제외합니다. |
| `test_app_icon_transactions.py::test_import_export_migration_failure_cleanup` | fsync/save/publish 실패, 중복 ID, 이미 존재하는 orphan/destination에 대해 기존 파일을 보존하고 이번 작업의 staging만 회수합니다. |
| `test_app_icon_prompts.py::test_final_prompt_size_is_checked_before_generation` | aggregate prompt 20,000자 경계와 넘는 입력을 검증합니다. exact final prompt가 Artifact 한도를 넘는데 host 호출 후에야 실패하는 상황을 사전 차단해야 합니다. |

### 이번 작업에서 실제 실행한 것과 하지 않은 것

| 시나리오 | 이번 결과 / 한계 |
| --- | --- |
| HTTP 원문 확인 | **PASS**, 아래 명령·상태·바이트·해시 증거를 참조해 주세요. |
| CLI 실제 표면 | **PASS**, top-level 및 prompt/import/export/review/color-gallery help를 로컬 설치된 interpreter로 실행했습니다. |
| dirty worktree | **실제 관찰**, 최초 clean → 다른 작업의 untracked draft 등장. 변경을 되돌리거나 자신의 결과로 취급하지 않았습니다. |
| malformed intent / conflicting icon-text-corner-colors | **정적 평가 및 테스트 제안만 수행**, 새 계약이 아직 구현되지 않아 runtime 적합성 판정은 N/A입니다. 기존 color conflict/strict 모델 테스트는 위에 매핑했습니다. |
| prompt injection | **정적 평가만 수행**, shell에 사용자 prompt를 실행하는 코드는 확인되지 않았고 JS는 textContent를 씁니다. native 모델 호출은 금지되어 있어 모델 공격 실험은 N/A입니다. |
| stale revision / old v1-v2 / resume | **정적 평가만 수행**, 실제 사용자 session mutation은 금지되어 있어 임시 세션 실행을 하지 않았습니다. 관련 기존/제안 테스트를 명시했습니다. |
| interruption / kill | **N/A**, 읽기 전용 역할에서 writer를 만들거나 강제 중단하지 않았습니다. 기존 예외 rollback과 강제 종료 복구는 동등하지 않습니다. |
| 장시간 명령 | **분석만 수행**, 전체 suite/native 호출을 하지 않았습니다. curl은 connect 10초/전체 30초 제한을 사용했고 실제 호출은 1초 미만에 끝났습니다. |
| browser visual QA | **N/A**, UI 변경/새 갤러리 생성이 없는 코드 지도 작업이며 실제 브라우저나 이미지 QA를 수행하지 않았습니다. |
| LSP/build/전체 suite | **N/A**, Markdown 보고서만 작성했습니다. 315 tests는 과거 기록이며 이번 검증으로 재인증하지 않습니다. |

중단 위험은 `mkdir` lock과 파일 copy/atomic state 사이에 있습니다. 일반 예외는 정리되지만 SIGKILL은 `finally`를 보장하지 않아 lock/orphan이 남을 수 있습니다. 다음 실행이 lock을 훔치거나 원본을 덮어쓰지 않는 현재 동작을 유지하고, 후속 QA에서 별도 임시 workspace에 실제 중단·재개 시나리오를 추가해야 합니다. native 호출 동안 session lock을 잡아 두면 다른 작업과 heartbeat를 막으므로 prompt→host call→revision 확인 import 경계를 유지하는 편이 안전합니다.

긴 입력은 현재 `PromptResult.prompt`, concept/changes, slogan의 전체 합산 크기가 제한되지 않는다는 점이 중요합니다. import 때 `Artifact.prompt`의 20,000자 제한이 적용되므로 사전 검사 위치가 필요합니다. `read_source()`는 64 MiB, PNG는 40,000,000 pixels를 제한하며, 모든 `Store.load()`가 저장된 PNG를 다시 읽고 디코딩하므로 대량 세션은 느려질 수 있습니다. JSON/프롬프트 파일을 사용하면 shell 인자 길이와 quoting 위험을 줄일 수 있지만 입력 크기·처리 시간 검증을 대체하지는 않습니다.

## 10. 실제 명령 및 HTTP QA 증거

다음 로컬 명령은 실제 실행했으며 전부 exit 0이었습니다. `-B`와 `PYTHONDONTWRITEBYTECODE=1`을 사용하여 Python bytecode를 생성하지 않았습니다. 네이티브 이미지 생성·세션 mutation 명령은 실행하지 않았습니다.

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B skills/logo-land/scripts/logo_project.py --help
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B skills/logo-land/scripts/logo_project.py prompt --help
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B skills/logo-land/scripts/logo_project.py import --help
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B skills/logo-land/scripts/logo_project.py export --help
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B skills/logo-land/scripts/logo_project.py review --help
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B skills/logo-land/scripts/logo_project.py color-gallery --help
```

필수 HTTP 명령은 다음과 같았습니다. 출력은 임시 `response.txt`에 받아 header/body를 분리하고 `git show <commit>:pyproject.toml`의 바이트와 `cmp`로 비교했습니다.

```sh
curl -i --fail --silent --show-error --connect-timeout 10 --max-time 30 https://raw.githubusercontent.com/t1seo/logo-land/ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5/pyproject.toml
```

```text
HTTP status: HTTP/2 200
curl exit: 0
response Date: Sat, 12 Sep 2026 16:46:15 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 1526
body bytes: 1526
committed pyproject bytes: 1526
cmp exit: 0
body SHA-256:      3873f84390ebb17f3b3faaeb1483525f15f099da405e79b4d40569d7d4c3814d
committed SHA-256: 3873f84390ebb17f3b3faaeb1483525f15f099da405e79b4d40569d7d4c3814d
worktree SHA-256:  3873f84390ebb17f3b3faaeb1483525f15f099da405e79b4d40569d7d4c3814d
PASS: HTTP 200 and byte-identical committed pyproject.toml.
```

검증 대상은 [커밋에 고정된 pyproject.toml](https://raw.githubusercontent.com/t1seo/logo-land/ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5/pyproject.toml)입니다. HTTP 성공은 이 파일 접근과 바이트 일치의 증거이며 native 이미지 품질이나 전체 구현 검증의 증거가 아닙니다.

### 임시 리소스 등록·정리

| 리소스 | 생성·사용·최종 상태 |
| --- | --- |
| `/tmp/logo-land-icons-http.Vodgq8` | stdout에 `QA_REGISTER`로 생성 시 등록했습니다. |
| 위 디렉터리의 `response.txt` | curl header+body 원문, 검증 후 삭제했습니다. |
| 위 디렉터리의 `body.toml` | header를 제거한 비교용 body, 검증 후 삭제했습니다. |
| 위 디렉터리의 `committed.toml` | `git show ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5:pyproject.toml`, 검증 후 삭제했습니다. |
| 디렉터리 최종 상태 | EXIT trap이 위 세 파일만 `rm`하고 빈 디렉터리를 `rmdir`했습니다. `QA_CLEANUP=/tmp/logo-land-icons-http.Vodgq8 removed`가 출력되었습니다. |

첫 HTTP wrapper 호출은 cleanup의 `rm -f` 형태를 허용하지 않는 자동 실행 검토에서 **실행 전 거부**되었습니다. 해당 호출은 파일을 만들거나 HTTP 요청을 실행하지 않았습니다. 새로 생성한 세 파일을 이름으로 지정하는 일반 `rm`과 빈 디렉터리 `rmdir`로 바꾼 안전한 명령이 성공했으므로 사용자 승인이나 추가 리소스 정리는 필요하지 않았습니다.

## 11. 종료 검증과 남은 작업

보고서 생성 후 `git diff --check --no-index /dev/null docs/qa/app-icons/code-map.md`가 exit 0이었으며, 실제 심볼 위치를 확인했습니다. 8절의 기존 테스트 참조 58개는 파일에서 해당 함수 정의가 존재하는지 별도로 검사해 모두 확인했습니다. `test ! -e /tmp/logo-land-icons-http.Vodgq8`가 성공했고 `git diff --name-only`에는 기존 tracked 파일 변경이 없었습니다. HEAD도 그대로이며 아래 릴리스 증거 네 파일의 SHA-256이 기준값과 모두 일치했습니다.

종료 검사에서 다른 작업의 `.omo/drafts/logo-land-app-icons.md`, `docs/research/app-icon-sources.json`, `docs/research/app-icon-tools.md`, `plans/logo-land-app-icons.md`, `docs/qa/app-icons/metis.md`도 관찰했습니다. 해당 파일은 이 작업의 산출물이 아니며 수정하거나 정리하지 않았습니다. `docs/qa/app-icons/` 아래 이 작업의 소유 결과물은 `code-map.md` 하나입니다.

```text
release-state.json 54bd651c3dbb1f312f20b845a358bf399be334f0e3aebec5bd7c911bcfd9fbe0
release.md        15ab403bf1985d1b492e4fddae84ce238f397f6b00d299765a6a1f54e138bb4f
review-summary.md 397021409aa996b5325a3afd0d56c0ef42ddc8f1357780fceaf25d938e497d8b
final-tests.txt   70bb4a04b2a79410570fe219e3522ef3a6ae06c9de524a066806915a02091b1d
```

코드 지도 작업의 결과물은 이 보고서입니다. 후속 구현·native one-pass 생성·새 회귀 테스트·실제 갤러리/승인 export QA는 아직 수행하지 않았으며, 이전 T8/VERIFY/T9 승인 공백도 그대로 남아 있습니다.
