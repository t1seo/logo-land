# 독립 코드 품질 검토

**판정: PASS.** 검토 범위에서 릴리스를 차단할 CRITICAL/MAJOR 결함은 확인하지 못했습니다. 사용자 지정 출력 경로의 이례적인 내부 저장 영역 충돌을 MINOR 1건으로 기록합니다. 신뢰도는 현재 macOS CLI 동작에 대해 높으며, 실행하지 않은 운영체제·파일시스템에 대해서는 제한적입니다.

검토일: 2026-09-12. 담당: 독립 코드 품질 리뷰 작업자. 구현 파일을 수정하지 않았으며, 이 보고서만 저장소에 추가했습니다.

## 발견 사항

### MINOR: 내부 잠금 영역을 출력 폴더로 지정하면 정상 commit 뒤 잠금 해제가 실패합니다

- 위치: `skills/logo-generator/scripts/logo_helper/delivery.py:93`, `delivery.py:121`, `delivery.py:128`, `skills/logo-generator/scripts/logo_helper/storage.py:126`.
- `safe_path`는 workspace 밖 이동과 symlink를 차단하지만 관리용 `.logo-generator/locks/` 하위 출력은 허용합니다. 내보내기가 현재 세션의 lock 디렉터리 안에 파일을 만든 다음 상태를 저장하면, context manager의 `lock.rmdir()`가 비어 있지 않은 디렉터리 오류로 종료합니다.
- 결과: CLI는 종료 코드 1을 반환하지만 export와 revision은 이미 저장되어 있습니다. 후속 변경 명령은 `locked`로 거부됩니다. 자동으로 잠금을 지우지 않는 정책 때문에 수동 복구가 필요합니다.
- 심각도 근거: 내부 잠금의 정확한 경로를 사용자 지정 출력으로 명시해야 발생합니다. 기본 출력과 일반 `exports/final-v2`는 정상 동작하며 기존 시안·이전 전달본 바이트 손실은 관측하지 않았습니다. 정상 사용자 흐름의 차단 결함으로 확대하지 않았습니다.
- 개선 방향: 출력 대상에서 helper의 관리용 저장 루트를 예약 영역으로 제외하거나, 최소한 lock 영역을 파일 생성 전에 거부하는 작은 경계 검사를 고려하실 수 있습니다. 이번 읽기 전용 검토에서는 구현을 변경하지 않았습니다.

실제 재현은 pytest가 만든 합성 PNG 세션을 두 개의 독립 임시 workspace에 복사한 뒤 CLI로 실행했습니다. 두 복사본의 시작 revision은 5였습니다. 아래 명령은 기존 프로젝트 환경에서 사용하며, `WORKSPACE`에는 해당 임시 복사본을 넣었습니다.

```sh
uv run --no-sync python skills/logo-generator/scripts/logo_project.py \
  --workspace WORKSPACE export --session demo --revision 5 \
  --output exports/final-v2
# 정상 대조군: exit 0

uv run --no-sync python skills/logo-generator/scripts/logo_project.py \
  --workspace WORKSPACE export --session demo --revision 5 \
  --output .logo-generator/locks/demo.lock/final-v2
# 경계 사례: exit 1, [Errno 66] Directory not empty: .../demo.lock

uv run --no-sync python skills/logo-generator/scripts/logo_project.py \
  --workspace WORKSPACE show --session demo
# 경계 사례의 저장 상태: revision 6

uv run --no-sync python skills/logo-generator/scripts/logo_project.py \
  --workspace WORKSPACE select --session demo --artifact v2 --revision 6
# 경계 사례의 후속 변경: exit 1, locked: Session locked; inspect running writers ...
```

## 검토 범위와 확인한 계약

untracked 파일도 포함하여 다음 전체 내용을 읽었습니다.

- 런타임 8개: `logo_project.py`, `logo_helper/{__init__,models,storage,images,prompts,workflow,delivery}.py`.
- `tests/`의 모든 Python 파일: fixture, CLI 동작·안전성, 경계, 트랜잭션, 재개·이식성, 전달 안내, 배경 변형·구버전 호환성.
- `skills/logo-generator/SKILL.md`, 모든 `references/*.md`, `pyproject.toml`, plugin manifest, helper 및 배경 변경 QA 기록과 실제 이미지 QA 기록.

| 검토 축 | 코드 근거와 판단 |
| --- | --- |
| 타입과 입력 경계 | `models.py:37`의 frozen/strict/extra-forbid Pydantic 모델, `logo_project.py:50`·`:147`의 JSON 경계가 실제 CLI에 연결됩니다. 문자열 boolean으로 검토 통과를 만들 수 없습니다. 현재 변경 경로의 `model_copy` 값도 선언된 모델과 일치합니다. |
| 상태 정합성 | `models.py:152`는 중복 ID, 부모 순서·순환, 선택·실패·export의 없는 참조, 관리 경로 불일치를 거부합니다. `storage.py:128`은 모든 저장 PNG의 해시와 디코딩된 메타데이터를 다시 비교합니다. |
| 오류 전파 | `logo_project.py:190`이 도메인·검증·파일·UTF-8 오류를 JSON stderr와 비정상 종료로 전달합니다. 호스트 이미지 실패는 `workflow.py:120`에서 실제 artifact 없이 별도로 남깁니다. CLI 사용법 오류는 Typer의 일반 종료 코드 2 경로입니다. |
| 변경 충돌 | `storage.py:110`의 세션별 mkdir lock과 `storage.py:147`의 revision 비교가 모든 정상 변경에 적용됩니다. 실제 별도 CLI 프로세스가 잠금을 점유한 writer와 충돌할 때 거부되는 회귀 검사를 실행했습니다. |
| 저장·롤백 | `storage.py:66`은 배타적 파일 생성 및 fsync 실패 정리, `storage.py:81`은 같은 디렉터리의 상태 교체를 수행합니다. `workflow.py:84`·`delivery.py:123`의 commit 실패 롤백과 기존 파일 보존 검사를 실행했습니다. 강제 종료·전원 차단의 다중 파일 원자성은 기존 문서에서 명시적으로 보장하지 않습니다. |
| 리소스 | `storage.py:20`·`:55`는 입력 읽기를 64 MiB로 제한합니다. `images.py:13`·`:17`은 4천만 픽셀, static PNG, 완전한 IEND와 실제 가시 픽셀을 검사합니다. 전체 세션 수·시안 수에 따른 누적 재검사 비용에는 별도 상한이 없지만, 문서화한 대화형 로고 흐름에서 차단 문제를 관측하지 않았습니다. |
| 배경 의미 | `workflow.py:77`은 생략 시 최초 brief 배경을 저장하며 부모 값을 자동 상속하지 않습니다. 이는 현재 스킬·참조 문서의 명시적 계약과 일치합니다. 구버전 missing/null 필드는 최초 brief로 해석하고 read-only 재개 시 다시 저장하지 않습니다. |
| 수정 프롬프트 | `prompts.py:55`는 명시적 부모 파일, 부모 배경, 최신 변경의 우선권과 나머지 부모 특성 보존을 제공합니다. helper는 제안 프롬프트만 만들며 실제 호출·최종 프롬프트 저장·시각 검수는 스킬의 책임으로 구분됩니다. |
| 전달 내용 | `delivery.py:79`는 선택한 시안의 모든 검토 통과와 해당 시안의 배경 요구를 확인합니다. `delivery.py:97`의 원본 바이트 재해시, manifest·ZIP의 원본 보존과 과거 brief/선택 요청 구분을 확인했습니다. PNG를 벡터·폰트·법적 권리로 오인시키는 구현 주장은 없습니다. |
| 유지보수성 | 상태 모델, 파일 경계, PNG 검사, 프롬프트, 변경 동작, 전달, CLI 역할이 분리되어 있습니다. 모든 런타임 파일은 전체 행 수부터 200행 이하이며 현재 타입·린트 억제로 결함을 숨기는 패턴은 발견하지 못했습니다. |

## 이 검토에서 직접 실행한 검증

모든 상태 변경과 합성 PNG 재현은 `/tmp/logo-review-code.vEOhvv/` 아래에서만 수행했습니다. bytecode 생성은 명령별 `PYTHONDONTWRITEBYTECODE=1`, pytest cache는 `-p no:cacheprovider`로 비활성화했습니다.

```sh
PYTHONDONTWRITEBYTECODE=1 uv run --no-sync pytest -q -p no:cacheprovider \
  --basetemp /tmp/logo-review-code.vEOhvv/pytest \
  tests/test_transactions.py \
  tests/test_background_variants.py \
  tests/test_background_compatibility.py \
  tests/test_cli_workflow.py::test_export_when_selected_image_is_explicitly_reviewed \
  tests/test_boundaries.py::test_inspect_rejects_when_png_is_animated \
  tests/test_cli_safety.py::test_import_when_request_is_unsafe
```

- 위 대상 테스트: **28 passed in 31.60s**.
- `uv run --no-sync basedpyright`: **0 errors, 0 warnings, 0 notes**.
- `uv run --no-sync ruff check --no-cache skills/logo-generator/scripts tests`: **All checks passed!**.
- `uv run --no-sync ruff format --check --no-cache skills/logo-generator/scripts tests`: **18 files already formatted**.
- 실제 CLI의 정상 사용자 지정 출력과 내부 잠금 경로 충돌을 별도로 대조 재현했습니다.

기존 QA의 전체 84개 통과 기록은 읽었으나 이번 작업자가 전체 테스트를 다시 실행한 것으로 주장하지 않습니다. 스킬이 지정한 실제 이미지 생성·수정, Chrome 시각 확인, 설치·패키징은 코디네이터 및 다른 독립 검토 범위입니다. 이번 검토에서 이미지 도구·계정·브라우저를 조작하지 않았고 `morrow-live` 세션을 변경하지 않았습니다. Windows/Linux 실행, 비표준 파일시스템의 hard-link 지원, 악의적인 외부 프로세스의 실시간 파일 교체, 강제 종료·전원 손실 시나리오는 재현하지 않았습니다.

임시 QA 자료는 핵심 관측을 위에 기록한 뒤 제거했습니다. 구현 수정이나 추가 하위 에이전트 실행 없이 독립 검토를 완료했습니다.
