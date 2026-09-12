# 로고 프로젝트 helper 구현·검증

검증일: 2026-09-12. 범위: `plans/logo-generator.md` 작업 3. 작업자는 `skills/logo-generator/scripts/`, `pyproject.toml`, `uv.lock`, `tests/`, 이 문서만 작성했습니다. 스킬 본문, 참조 문서, 예제 자산, README, manifest 및 실제 이미지 생성 QA는 코디네이터 소유입니다.

## 구현 결과

- Python 3.12 이상의 typed CLI이며 Pydantic v2가 외부 JSON을 파싱합니다. 알 수 없는 JSON 키와 잘못된 타입은 거부하고, 정확한 로고 문구는 그대로 보존합니다.
- 세션 생성, 명시적 세션 목록·재개, 생성·수정 프롬프트, PNG 가져오기, 시안 선택, 명시적 시각 검토, 최종 패키지 내보내기, 호스트 호출 실패 기록을 제공합니다.
- 실제 PNG 원본 바이트를 복사하며 이미지 API 호출, 이미지 생성, 결과 픽셀 편집·변환은 하지 않습니다. Pillow의 RGBA 변환은 알파 통계 검사에만 사용합니다.
- 가져온 시안에는 안정적인 ID, 부모 ID, 최종 사용 프롬프트, SHA-256, 실제 크기·형식·알파 통계와 시각 검토 기록이 있습니다. 모든 재개·변경·내보내기에서 저장된 이미지의 해시와 디코딩 결과를 확인합니다.
- 선택한 이미지와 모든 시각 검토가 통과해야 내보낼 수 있습니다. 투명 배경 요청은 실제 투명 픽셀이 있어야 하며, 불투명 배경 요청은 모든 픽셀이 불투명해야 합니다. 배경이 다르면 all-true 시각 검토도 통과하지 못합니다. 출력은 `logo.png`, `manifest.json`, `brand-guide.md`, `logo-package.zip`입니다. ZIP에는 앞의 세 파일이 들어가며 PNG 원본과 ZIP 내부 파일의 바이트 일치를 검사했습니다.
- 수정 프롬프트는 요청한 변경이 과거 브리프의 충돌하는 필드보다 우선함을 명시합니다. 브랜드 안내에서 원래 문구·스타일·팔레트는 `Initial brief`로 구분하고 `Selected version request`에는 선택한 시안의 실제 프롬프트를 수록하여 최신 수정 요청이 기준임을 표시합니다.

## 실행 계약

```sh
uv run --project /path/to/plugin /path/to/plugin/skills/logo-generator/scripts/logo_project.py --workspace /path/to/workspace list
```

workspace는 이미 존재하는 사용자 작업 폴더입니다. 모든 경로와 인자는 개별 argv 또는 올바르게 인용한 문자열로 전달합니다. 아래 예제는 위 공통 실행 접두사를 생략했습니다.

```text
init --session demo --brief /path/to/brief.json
show --session demo
prompt --session demo --concept "Geometric symbol"
import --session demo --artifact v1 --image /actual/tool-result.png --prompt-file /path/to/actual-prompt.txt --revision 0
prompt --session demo --parent v1 --changes "Change green to navy"
import --session demo --artifact v2 --parent v1 --image /actual/edit-result.png --prompt-file /path/to/edit-prompt.txt --revision 1
select --session demo --artifact v2 --revision 2
review --session demo --artifact v2 --review-file /path/to/review.json --revision 3
export --session demo --revision 4
failure --session demo --prompt-file /path/to/failed-prompt.txt --reason "Actual host error" --revision 5 --parent v2
```

`init`은 revision 0입니다. `import`, `select`, `review`, `export`, `failure`는 현재 revision을 필수로 받아 성공할 때만 1 증가시킵니다. `list`, `show`, `prompt`는 읽기 전용입니다. `prompt` 출력의 `prompt`는 제안 문자열이며 `parent_image_path`는 검증한 실제 부모 PNG 경로입니다. 도구에 전달하기 전에 수정했다면 수정된 최종 프롬프트를 `--prompt-file`로 가져와야 합니다.

상태는 `.logo-generator/sessions/<id>/session.json`, 원본 사본은 같은 세션의 `artifacts/<artifact-id>.png`입니다. 출력 기본값은 `output/logo-generator/<session-id>/`이며 `export --output`으로 새로운 workspace 상대 경로를 지정할 수 있습니다. 이미 있는 출력 폴더는 비어 있어도 덮어쓰지 않습니다.

정상 명령 stdout은 JSON입니다. 알려진 파일·스키마·도메인 오류는 stderr JSON과 종료 코드 1을 반환하고, 잘못된 CLI 인자는 Typer의 종료 코드 2를 반환합니다. `--help`는 사람이 읽는 도움말입니다.

### 브리프 JSON

| 키 | JSON 타입 | 기본값·제약 |
|---|---|---|
| `brand_name` | string | 필수, 공백만 불가 |
| `exact_text` | string | 필수, 최대 2,000자; 문구 없는 심볼은 빈 문자열 |
| `industry`, `audience` | string | 필수, 공백만 불가 |
| `slogan` | string | `""` |
| `logo_type` | string enum | `combination`; wordmark, lettermark, monogram, symbol, abstract, combination, emblem, mascot |
| `styles`, `palette`, `forbidden`, `use_cases`, `assumptions` | array of strings | `[]`; 항목은 공백만 불가 |
| `background` | string enum | `opaque`; opaque 또는 transparent |
| `concept_count` | integer | `3`; 1 이상, 요청한 수를 그대로 보존 |

공백만 불가인 텍스트 필드는 최대 20,000자입니다. 문자열이나 숫자에서 불리언으로 자동 변환하지 않으며, 브리프의 문자열과 배열도 지정 타입으로만 받습니다.

### 시각 검토 JSON

```json
{
  "reviewer": "실제로 이미지를 확인한 검토자",
  "notes": "문구, 여백, 작은 크기 식별성, 수정 보존 조건과 배경을 확인한 내용",
  "text_correct": true,
  "composition_ok": true,
  "small_size_ok": true,
  "preservation_ok": true,
  "background_checked": true
}
```

모든 필드가 필수입니다. 문자열 두 개는 공백만으로 채울 수 없으며, 나머지는 JSON boolean이어야 합니다. 실패한 검토도 저장되지만 내보내기는 거부됩니다. 자동 검사로 실제 디자인 품질이나 검토자의 진실성을 증명할 수는 없습니다.

## 검증 기록

환경: macOS, CPython 3.12.12, uv 0.9.16. 잠근 주요 버전: Pydantic 2.13.5, Pillow 12.3.0, Typer 0.27.2, Rich 14.3.4, pytest 9.1.1, Ruff 0.16.7, basedpyright 1.40.1. 루트 `uv.lock`에 프로젝트 환경을 잠갔고 진입 스크립트의 PEP 723에도 검증한 직접 의존성 버전을 지정했습니다. 스크립트 직접 실행 시 uv는 PEP 723 환경을 사용합니다. 루트 lock 환경을 그대로 사용하려면 `uv run --project /path/to/plugin python /path/to/skill/scripts/logo_project.py ...`로 실행할 수 있습니다.

### Red → green 증거

| 단계 | 실제 명령·관측 |
|---|---|
| 최초 red | `uv run --python 3.12 pytest -q tests/test_cli_workflow.py tests/test_cli_safety.py`: **24 failed in 0.70s**. 실행 가능한 초기 placeholder가 `logo project commands are not implemented`로 종료해 테스트가 실패했습니다. 테스트 수집·import 오류는 아니었습니다. |
| 기본 green | `uv run pytest -q --tb=short`: **24 passed in 12.42s**. 별도 프로세스에서 전체 저장·재개·내보내기 흐름을 실행했습니다. |
| 보존 경계 red | `uv run pytest -q tests/test_transactions.py tests/test_boundaries.py --tb=short`: **6 failed, 19 passed in 1.19s**. export 상태 commit 실패 시 신규 폴더 잔존, fsync 실패 시 부분 파일 잔존, Windows drive 경로, 공백 브리프를 발견했습니다. |
| 보존 경계 green | 같은 두 파일: **25 passed in 1.53s**. 기존 데이터 보존을 유지하면서 신규 파일만 정리하도록 수정했습니다. |
| PNG 절단 red | `test_inspect_rejects_when_png_end_is_truncated`: **2 failed, 2 passed in 0.05s**. Pillow가 마지막 1바이트·4바이트 누락을 허용하는 사례를 재현했습니다. 완전한 IEND 종료 청크 검사 후 회귀 검사가 통과합니다. |
| 시안 수 red | `test_brief_accepts_explicit_concept_count_above_default`: **1 failed in 0.15s**. 임의 상한 20을 제거하여 명시적으로 요청한 24개를 보존합니다. |
| 전체 통합 확인 | 상한 변경 전: **64 passed in 28.94s**. 최종 실행 결과는 아래 최종 검사에 기록합니다. |
| 시안 수 green | 상한 변경 포함 전체: **65 passed in 32.05s**. |
| 실제 QA 피드백 red | 불투명 요청에 투명 파일 내보내기 및 초기 팔레트가 최종 팔레트로 오해될 안내: **2 failed in 1.28s**. 코디네이터의 실제 이미지 QA 관측을 독립 합성 fixture로 재현했습니다. |
| 실제 QA 피드백 green | 두 회귀 검사와 수정 프롬프트 우선권 검사: **3 passed in 1.69s**. |

구현 중 발견한 Typer 호환성도 실제 runtime으로 확인했습니다. PEP 695 타입 별칭은 `Type not yet supported: SessionOption`을 발생시켰고 직접 `Annotated` 별칭은 정상 동작했습니다. 또한 callback에서는 `PosixPath`로 변환되지만 context에는 `{'workspace': '.'}` 문자열이 남는 것을 관측하여 Pydantic 경계에서 경로를 파싱했습니다. 이 조사에는 source breakpoint, 환경 변수 변경, 임시 debugger 파일, listener를 남기지 않았습니다.

### 검증 시나리오

- 정상: 한국어 브리프·공백 경로, 여러 세션 목록, 부모 연결된 수정본 재개, 최종 PNG/manifest/ZIP 일치, 요청한 불투명 배경, 실패한 호스트 호출 기록.
- 이미지: RGB, 불투명 RGBA, 실제 부분 투명 RGBA, 팔레트 투명 PNG, 완전 투명, 위장 JPEG, 빈 파일, 중간·끝 절단 PNG, APNG 거부.
- 상태: malformed JSON, 미지원 버전, 필수 필드 누락, 부모 자체 참조, 중복 ID, 잘못된 세션 ID, 경로·크기 변조, 삭제된 이미지, 변경된 해시.
- 보존: 오래된 revision, 미등록 기존 파일과 이름 충돌, 기존 시안 덮어쓰기, 기존 export 폴더 충돌, fsync 실패, 상태 commit 실패 시 rollback.
- 경로: 상대 traversal, 절대 경로, Windows drive·역슬래시, 세션 루트·시안 폴더·출력 부모 symlink.
- 잠금: 한 프로세스가 실제 lock을 잡은 상태에서 별도 CLI 프로세스가 변경을 시도하면 `locked` 오류로 거부하며, 예외 이후 잠금을 다시 얻을 수 있습니다.
- 이식성: scripts 폴더만 공백이 있는 다른 위치로 복사한 뒤 `uv run --offline --project <plugin-root> <copied-scripts>/logo_project.py ... init`을 새 subprocess에서 실행했습니다. 복사본은 개발자 홈 경로나 원본 스킬 import 경로를 필요로 하지 않습니다.

## 최종 검사

```sh
uv run pytest -q --tb=short
uv run ruff check skills/logo-generator/scripts tests
uv run ruff format --check skills/logo-generator/scripts tests
uv run basedpyright
uv lock --check
```

Ruff: `All checks passed!`; basedpyright: `0 errors, 0 warnings, 0 notes`; lock 검증: 종료 코드 0. 모든 Python 파일은 주석·빈 줄을 제외해 250행 미만입니다. 타입 검사 `all` 및 Ruff `ALL`을 사용하며, `Any`, `object`, `cast`, type-ignore를 도입하지 않았습니다. 아래 최종 인계 결과에 최종 파일 수와 실행 결과를 기록합니다.

Ruff 예외는 formatter와 충돌하는 규칙, 이름으로 충분한 간단한 공개 함수의 docstring, typed exception의 첫 인자인 오류 코드에 대한 EM101, Pydantic runtime annotation import, 고정 argv subprocess 테스트에 한정됩니다. CLI는 선언형 인자가 많아 인자 수 상한을 7로 설정했습니다.

## 보장 범위와 인계

최종 전체 테스트는 **67 passed in 17.62s**이며, 마지막 전달 안내·배경 검사에 대한 targeted 재검증은 **3 passed in 2.04s**입니다. 최종 Ruff는 `All checks passed!`, formatter는 `16 files already formatted`, basedpyright는 `0 errors, 0 warnings, 0 notes`, `uv lock --check`는 종료 코드 0입니다. no-excuse 감사는 `no violations in 16 file(s)`입니다. 주석·빈 줄을 제외한 최대 파일 크기는 `logo_project.py`의 151행이며 250행을 초과하는 파일은 없습니다.

파일 크기는 64 MiB, 이미지 크기는 4천만 픽셀까지 허용하며 static PNG만 받습니다. 정상 명령에 대한 변경은 session별 mkdir lock과 revision으로 직렬화합니다. JSON은 같은 디렉터리에서 파일을 flush/fsync한 후 원자적으로 교체합니다. 디스크 오류는 이전 상태를 유지하며 이번 명령이 만든 신규 파일만 정리합니다. 외부 프로세스의 파일 변조는 이후 해시 검사로 감지합니다.

강제 프로세스 종료·전원 차단은 다중 파일 트랜잭션으로 보장하지 않습니다. 남은 lock은 자동으로 빼앗지 않으므로 실행 중인 writer가 없음을 확인한 후에만 해당 lock을 복구해야 합니다. crash로 생긴 미등록 이미지나 전달 폴더도 자동 덮어쓰기·삭제하지 않습니다. 관리 디렉터리는 symlink를 거부하며 사용자가 명시한 workspace 자체는 운영체제 경로 별칭을 resolve한 신뢰 루트로 사용합니다. macOS에서 실제 실행했고 Windows/Linux 실행 자체는 이번 작업에서 검증하지 않았습니다.

테스트 PNG는 pytest 임시 폴더에서 Pillow로 만든 **명시적 합성 fixture**입니다. 이 테스트 결과를 실제 로고 생성·편집·시각 품질의 증거로 사용하지 않습니다. 실제 호스트 이미지 생성·편집과 통합 시각 QA, 계획 6번의 독립 다섯 관점 검토는 코디네이터가 담당합니다. 추가 하위 에이전트 금지 지시에 따라 이 작업자는 다른 에이전트를 실행하지 않았습니다. 계정·marketplace 변경, API 호출, git commit도 수행하지 않았습니다.
