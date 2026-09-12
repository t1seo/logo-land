# 예약 저장 영역 출력 충돌 수정

2026-09-12, **PASS**. 독립 검토에서 발견한 `export --output .logo-generator/locks/demo.lock/...`의 상태 commit 후 잠금 해제 실패를 수정했습니다. 전체 테스트 96개가 통과했으며, 실제 CLI에서 예약 출력 거부 후 같은 세션의 일반 내보내기도 성공했습니다.

## 변경과 원인

기존 내보내기는 workspace 안에 있는 경로라면 잠금 디렉터리 하위도 허용했습니다. 여기에 전달 파일을 쓴 후 상태를 저장하면 `Store.locked()`의 `lock.rmdir()`가 `Directory not empty`로 실패했습니다. 명령은 실패했지만 revision은 증가하고 잠금은 남는 상태였습니다.

`skills/logo-generator/scripts/logo_helper/delivery.py:72`의 `_export_destination()`이 기존 `safe_path()` 검사를 수행한 뒤, 정규화된 workspace 상대 경로의 첫 디렉터리가 `.logo-generator`인지 검사합니다. 예약 영역 자체와 모든 하위를 `ProjectError("reserved_output", ...)`로 거부합니다. 대소문자를 구별하지 않는 파일시스템의 이름 충돌을 피하도록 첫 디렉터리를 `casefold()`로 비교하며, 중복 `/`도 기존 경로 정규화 후 검사합니다. `.logo-generator-backup/` 같은 별도 이름은 허용합니다.

`delivery.py:85`에서 이 검사를 **잠금 획득 전** 수행하므로 예약 출력 요청은 lock 폴더를 만들거나 상태·전달 파일을 쓰기 전에 종료합니다. 기존 경로 검사, 배타적 출력 생성, 검토·배경 조건, commit·롤백 흐름은 계속 적용됩니다. 검증 책임을 전용 함수로 분리하여 기존 export 함수의 Ruff 복잡도 한도를 유지했습니다. 린트·타입 검사 억제를 추가하지 않았습니다.

## 실패 재현과 회귀 검사

새 `tests/test_reserved_output.py`를 구현 변경 전에 작성하여 실제 CLI subprocess로 실행했습니다.

```text
수정 전: 10 failed, 2 passed in 24.45s
수정 후 대상 검사: 12 passed in 16.91s
최종 전체 검사: 96 passed in 43.79s
```

수정 전 `.logo-generator/locks/demo.lock/package`는 실제 `[Errno 66] Directory not empty`로 실패했고, 다른 예약 영역은 기존 conflict 오류나 잘못된 성공을 반환했습니다. 빈 workspace에서는 경로 검사보다 먼저 managed lock 디렉터리를 만들고 `invalid_file`로 종료했습니다. 일반 출력 대조군 2개는 수정 전부터 통과하여 문제를 예약 영역 경계로 한정했습니다.

새 회귀 검사 12개는 다음을 확인합니다.

- 예약 영역 루트, lock 폴더, 현재·다른 세션 lock 하위, 현재·새 세션 폴더, artifacts 하위, 중복 슬래시, 대문자 별칭을 거부합니다.
- 거부 시 종료 코드 1과 `reserved_output`을 반환하며, 상태 JSON 바이트와 전체 workspace 경로 목록이 그대로이고 잔여 lock이 없습니다.
- 아직 세션이 없는 빈 workspace에서도 예약 출력 요청이 어떠한 저장 영역도 만들지 않습니다.
- 일반 `exports/final-v2`와 `.logo-generator-backup/final-v2`는 원본 PNG를 보존하고 revision 4 및 export 기록을 저장합니다.

## 최종 검사

```sh
PYTHONDONTWRITEBYTECODE=1 uv run --no-sync pytest -q -p no:cacheprovider \
  --basetemp /tmp/logo-reserved-output.3WFIu1/full
uv run --no-sync ruff check --no-cache skills/logo-generator/scripts tests
uv run --no-sync ruff format --check --no-cache skills/logo-generator/scripts tests
PYTHONDONTWRITEBYTECODE=1 uv run --no-sync basedpyright
```

| 검사 | 결과 |
| --- | --- |
| 전체 pytest, 최종 구조로 1회 실행 | 96 passed in 43.79s |
| Ruff | All checks passed! |
| 포맷 검사 | 19 files already formatted |
| basedpyright | 0 errors, 0 warnings, 0 notes |
| Programming 스킬 no-excuse 검사, 변경 Python 2개 | no violations in 2 file(s) |
| 주석·빈 줄 제외 행 수 | delivery.py 132행, 새 테스트 47행 |

최종 전체 검사 중 변경한 것은 오류 메시지 인자의 줄바꿈뿐이며 실행 의미는 동일합니다. 별도 의존성이나 빌드 단계는 추가하지 않았습니다.

## 실제 CLI 사용 확인

새 테스트의 합성 PNG 세션을 별도 임시 workspace로 복사했습니다. tmux가 없어 도구의 실제 PTY에서 CLI를 직접 실행했습니다. 시작 상태는 `demo`, revision 3, 선택 시안 `v1`이며 합성 검토 fixture임을 유지했습니다.

```text
export --session demo --revision 3 --output .logo-generator/locks/demo.lock/final
→ exit 1
→ {"error": "reserved_output: Export destination cannot be inside reserved .logo-generator storage"}
cmp 이전 session.json 현재 session.json → 일치
잠금 및 예약 출력 경로 검사 → 없음

같은 workspace에서:
export --session demo --revision 3 --output exports/final
→ exit 0, revision 4
cmp artifacts/v1.png exports/final/logo.png → 일치
unzip -t exports/final/logo-package.zip
→ logo.png, manifest.json, brand-guide.md 모두 OK
→ No errors detected in compressed data
```

## 소유권·한계·인계

수정한 저장소 파일은 `delivery.py`, `tests/test_reserved_output.py`, 이 보고서 3개뿐입니다. 기존 독립 검토 보고서 `docs/qa/review-code.md`는 수정하지 않았습니다. 새 테스트의 Given/When/Then 주석은 자동 comment-checker의 BDD 허용 항목에 해당합니다.

상태 및 시안 4개 파일의 작업 전후 SHA-256이 모두 일치했습니다. `morrow-live/session.json`은 `43a38d8e69378d40ed2ef4a9b471cda137dbd34821f1d2667f9c1e65523e901d`를 유지합니다. 임시 재현 파일·저널·테스트 workspace는 `/tmp/logo-reserved-output.3WFIu1/` 아래에만 만들고 결과 기록 후 제거했습니다. 저장소의 다른 변경이나 계정·Chrome·설치·패키징을 건드리지 않았고 커밋·하위 에이전트 실행도 하지 않았습니다.

이 검증은 macOS에서 수행한 helper 파일 처리 검증입니다. Windows/Linux 실제 실행이나 새 로고 생성 품질을 검증한 것으로 해석하지 않습니다. 이번 수정의 미해결 차단 문제는 없으며, 최종 독립 QA·보안 검토와 패키지 반영은 코디네이터가 담당합니다.
