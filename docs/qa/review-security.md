# 독립 보안 검토

검토일: 2026-09-12 · 담당: 보안 전담 검토자 · 범위: 로컬 CLI, 저장소 경계, 배포 입력, 연구 자료 노출, 의존성

**판정: PASS. 확인된 CRITICAL/HIGH 차단 사항은 없습니다.** 최종 내부 출력 경로 패치와 재생성된 배포 ZIP까지 독립 확인했습니다. 아래 LOW 사항은 로컬 사용자 권한으로 실행되는 도구라는 위협 모델에서 비차단 개선 사항입니다. 악의적인 사용자가 작업 폴더를 동시에 교체하는 환경이나 외부 요청을 받는 서버로서의 안전성을 보증하는 판정은 아닙니다.

## 발견 사항

### S1 · LOW · 검증 오류가 거부한 입력값을 stderr에 포함합니다

- 위치: `skills/logo-generator/scripts/logo_project.py:194`, `skills/logo-generator/scripts/logo_helper/models.py:40`.
- `ValidationError`를 `str(error)`로 출력하므로 잘못 추가된 필드의 값이 오류 메시지에 포함됩니다. 임시 brief에 `password`라는 알 수 없는 필드와 합성 시험값을 넣어 CLI를 실행했으며, 입력은 거부됐지만 그 합성값이 stderr에 포함되는 것을 확인했습니다.
- 실제 자격 증명이 노출된 사례를 발견한 것은 아닙니다. 사용자가 개인 정보를 실수로 JSON에 넣고 터미널 기록이나 오류를 공유할 때 추가 노출이 생길 수 있습니다.
- 권고: Pydantic의 입력값 비표시 설정 또는 값이 제외된 구조화 오류를 사용하십시오. 필드명·오류 종류·수정 방법은 유지할 수 있습니다.

### S2 · LOW · 배포 스크립트의 전이 의존성은 별도로 잠겨 있지 않습니다

- 위치: `skills/logo-generator/scripts/logo_project.py:2`, `uv.lock`, `skills/logo-generator/references/project-files.md`.
- PEP 723에는 Pydantic, Pillow, Typer, Rich의 직접 버전이 정확히 고정되어 있지만 `logo_project.py.lock`은 없습니다. 문서의 `uv run --project … logo_project.py …` 실행을 오프라인으로 재현했으며, uv가 프로젝트 가상환경 대신 별도 스크립트 환경을 사용했습니다.
- 프로젝트 `uv.lock`의 해시가 해당 실행 경로의 모든 전이 의존성을 고정한다고 볼 수 없습니다. 문서는 검토 도중 이 차이를 설명하도록 보완되었으며, 잘못된 동작 안내라는 지적은 남기지 않습니다. 새 환경에서 전이 버전이 달라질 수 있다는 공급망·재현성 개선 여지만 남습니다.
- 완화: 문서에 프로젝트 lock을 실제 사용하는 `uv run --locked --project … python …/logo_project.py …` 대안이 추가된 것을 확인했습니다. 기본 스크립트 실행 경로도 재현 가능하게 만들려면 스크립트 전용 lock을 배포하는 방법이 남습니다. uv의 [인라인 메타데이터 설명](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies)과 [스크립트 의존성 잠금 설명](https://docs.astral.sh/uv/guides/scripts/#locking-dependencies)에 근거합니다.

### S3 · INFO · PNG 거부 판정 전에 다른 포맷 파서를 거칠 수 있습니다

- 위치: `skills/logo-generator/scripts/logo_helper/images.py:24`, `skills/logo-generator/scripts/logo_helper/images.py:30`.
- `Image.open`에 `formats=["PNG"]` 제한이 없습니다. 합성 JPEG 뒤에 PNG의 IEND 바이트를 붙인 입력을 검사했을 때 JPEG 파서 진입 후 `invalid_png`로 정상 거부되는 것을 확인했습니다. PNG로 잘못 수용되거나 코드 실행이 일어난 것은 아닙니다.
- 포맷 제한을 두 호출에 적용하면 필요 없는 파서 노출을 줄일 수 있습니다. 현재 고정 버전의 취약점 재현이나 출시 차단 사유로 분류하지 않았습니다.

## 경계와 실제 동작 검증

다음 기존 테스트를 직접 실행했으며 **59개가 통과했습니다**.

```sh
uv run --no-sync pytest -q tests/test_boundaries.py tests/test_cli_safety.py tests/test_transactions.py tests/test_resume_and_portability.py
```

별도 임시 작업 폴더에서 실제 CLI 프로세스를 실행한 **19개 독립 검사도 통과했습니다**. 합성 로고·합성 brief만 사용했고 임시 세션은 정리했습니다. 원래 `morrow-live` 세션은 변경하지 않았습니다.

| 영역 | 확인 내용과 근거 |
|---|---|
| 입력 파싱 | Pydantic의 strict/extra-forbid, 식별자 정규식, 스키마 버전, 부모 순서·중복 ID·선택 참조 검사를 확인했습니다. 잘못된 입력은 원래 상태를 보존했습니다. |
| 경로 이탈 | `../`, 절대 경로, Windows 구분자·드라이브 형태와 관리 영역의 symlink를 차단했습니다. 실제 CLI의 session ID와 export 경로 이탈도 거부됐습니다. |
| 입력 파일 | symlink leaf, FIFO 등 비정규 파일, 64 MiB 초과 파일을 거부했습니다. FIFO 검사는 블로킹 없이 끝났습니다. 명시적으로 지정한 일반 소스 파일을 workspace 밖에서 읽는 것은 정상 기능입니다. |
| 충돌·상태 보존 | `xb` 생성, 기존 디렉터리 거부, revision 비교, mkdir 잠금이 기존 파일·세션·내보내기를 보존했습니다. 저장 실패 시 import/export 롤백과 잠금 해제를 기존 테스트로 확인했습니다. |
| 쉘 주입 | 런타임 소스에 shell/subprocess/eval/exec 호출이 없습니다. 명령 치환·백틱 형태의 합성 문자열을 JSON에 넣고 init/prompt를 실행했지만 명령은 실행되지 않았습니다. 문서는 임의 텍스트를 파일로 전달하도록 안내합니다. |
| 이미지 제한 | 바이트 제한 64 MiB, 픽셀 제한 4천만, 완전한 PNG/IEND 검사, 실제 decode, APNG·빈 이미지·완전 투명 이미지 거부가 있습니다. 4천만 초과 헤더를 실제 CLI에서 거부했습니다. |
| 해시·원본 | 재개 시 모든 artifact의 SHA-256·디코딩 사실을 재검사하며 export에서 선택 원본의 해시를 다시 확인합니다. 변경된 이미지로 show가 실패했고 정상 PNG와 전달 PNG의 해시가 같았습니다. |
| 검수 게이트 | 선택과 명시적인 육안 검수가 없으면 export가 실패했습니다. 픽셀의 실제 투명도와 요청한 배경을 비교하며, 단순 RGBA 채널 존재를 투명으로 간주하지 않습니다. |
| ZIP | 고정된 파일명만 쓰고 압축 해제 기능은 없습니다. 로고 전달 ZIP의 엔트리는 `logo.png`, `manifest.json`, `brand-guide.md` 3개이며 경로 이탈 이름이 없습니다. |
| 네트워크 | 헬퍼는 이미지 API나 외부 HTTP 요청을 호출하지 않습니다. 최초 환경 준비의 uv 패키지 취득과 호스트 내장 이미지 호출은 별도 경계입니다. |

## 자료·배포 점검

- 소스·문서·JSON/JSONL·스냅샷·HTML·설정·lock을 포함한 **218개 텍스트 파일**을 값 비노출 방식으로 스캔했습니다. 개인 이메일, API 키, 비밀 키, JWT로 확인된 항목은 없었습니다. `.venv`, git 내부, 캐시, 실제 사용자 세션은 배포 입력과 구분했습니다.
- Looka 진입 스냅샷의 이메일 2건은 해당 서비스의 공개 문의 주소로 분류했습니다. 원문은 이 보고서에 복사하지 않았습니다.
- `docs/research/snapshots/design-01-entry.json:5`, `captures.jsonl:4`, `gallery.html:1`의 Design.com `/s/maker` URL에는 8자리 **`code`** 쿼리가 남아 있습니다. 공개 진입 코드일 가능성이 있어 인증 토큰으로 단정하지 않았습니다. 값은 출력하지 않았으며 불필요한 쿼리의 제거를 코디네이터에게 제안했습니다. 초기 메시지의 `token` 명칭은 `code`로 정정했습니다.
- 첫 로컬 Vision OCR은 연구 스크린샷과 실제 QA 이미지 136개, 실패 0개였습니다. 추가 자료를 포함한 전체 재검사는 **144개, 실패 0개**로 12:53:36 UTC에 완료됐습니다. 그 뒤 추가된 Looka Chrome 2개와 Brandmark Chrome 3개도 별도 검사했으며 **5개 모두 실패·민감 패턴 검출이 없었습니다**. 이메일·API 키 형태·계정 선택 화면·민감 쿼리 패턴을 검사했고 OCR 원문은 저장하거나 출력하지 않았습니다. 이후 새로 추가되는 자료에는 이 판정을 자동 적용하지 않습니다.
- 이미지 메타데이터 138개를 검사했습니다. JPEG의 EXIF 후보는 내부 태그까지 확인했으며 대표 샘플의 태그는 이미지 폭·높이였습니다. GPS·소유자·작성자·사용자 설명 태그는 검출되지 않았습니다. 개별 PNG에 임의 metadata를 넣는 사용자를 막거나 입력 이미지 metadata를 제거하는 기능은 없고, 원본 바이트 보존이 명시된 동작입니다.
- 최종 `dist/logo-generator-0.2.0.zip`은 **29개 엔트리 / 일반 파일 20개 / 비압축 127,872바이트**였습니다. 연구 자료, 사용자 세션, `.env`, 캐시, symlink, 이탈 경로, 자격 증명 패턴이 없습니다. 최종 패치가 들어간 런타임 파일은 검토 소스와 같았으며 패키지 README만 저장소 README와 달랐습니다. 검토한 ZIP의 SHA-256은 `1ccf995e106217dc76c28f4247d162da27569de6f55d4a63fe3069a6df949775`입니다.

## 의존성 확인과 한계

`uv.lock`의 외부 패키지 21개는 PyPI 인덱스를 가리키며, 배포 파일 URL 호스트는 `files.pythonhosted.org`였습니다. 기록된 모든 sdist/wheel에 SHA-256이 있습니다. VCS 브랜치 의존성이나 자격 증명이 포함된 인덱스 URL은 발견하지 못했습니다. 개발용 basedpyright·Node 바이너리 등은 lock에 있으나 런타임 스크립트의 직접 의존성은 아닙니다.

| 패키지 | 확인 버전 | 공식 근거와 결론 |
|---|---|---|
| Pillow | 12.3.0 | [공식 12.3.0 보안 수정 기록](https://pillow.readthedocs.io/en/stable/releasenotes/12.3.0.html#security)을 확인했습니다. 예를 들어 [GHSA-62p4-gmf7-7g93](https://github.com/python-pillow/Pillow/security/advisories/GHSA-62p4-gmf7-7g93)은 12.2.0 이하가 영향 범위이고 12.3.0 이상이 수정 범위로 명시됩니다. 이는 해당 advisory에 대한 판단입니다. |
| Pydantic / pydantic-core | 2.13.5 / 2.46.5 | [유지보수자의 advisory 목록](https://github.com/pydantic/pydantic/security/advisories)을 확인했습니다. 목록에는 과거 v1 계열 datetime 무한 루프 공지가 있습니다. 목록 조회만으로 현재 배포의 모든 취약점 부재를 보증하지 않습니다. |
| Typer | 0.27.2 | [유지보수자의 보안 페이지](https://github.com/fastapi/typer/security)를 확인했습니다. 공개 advisory가 없다는 페이지 상태는 전체 CVE 부재 증명이 아닙니다. |
| Rich | 14.3.4 | [유지보수자의 advisory 목록](https://github.com/Textualize/rich/security/advisories)을 확인했습니다. Rich의 전이 의존성과 번들 라이브러리까지 전수 취약점 검사를 수행한 것은 아닙니다. |

소스 수준 경로·CLI 검사에 대한 신뢰도는 높고, 민감 자료·의존성 전체에 대한 신뢰도는 중간입니다. OCR은 작은 글씨·비정형 개인정보·잘못 인식한 문자열을 놓칠 수 있고, 정규식 스캔은 인코딩된 비밀이나 의미상 민감한 일반 문장을 전부 판별하지 못합니다. 패키지 공급자 서명·wheel 내부 바이너리·시스템 Python/uv·호스트 이미지 런타임의 취약점은 이번 범위 밖입니다. **“CVE가 없다”는 결론은 내리지 않습니다.**

## 신뢰 모델과 최종 확인

- 경로 검사는 일반적인 정적 symlink와 잘못된 입력을 막습니다. `resolve`/검사 이후 파일을 열거나 쓰는 단계는 descriptor 기반 `openat` 격리가 아니므로 악의적인 동시 디렉터리 교체까지 보장하지 않습니다. 잠금은 협조하는 writer 사이의 제어입니다.
- SHA-256은 저장한 원본의 변경을 감지합니다. 같은 권한의 사용자가 이미지와 JSON의 해시·review를 함께 변경하는 경우를 인증하거나, PNG가 실제 호스트 imagegen에서 나왔음을 암호학적으로 증명하지는 않습니다. 실제 tool 결과 선택과 육안 검수는 호스트 작업 흐름의 책임으로 문서화되어 있습니다.
- 단일 입력과 픽셀 수는 제한되지만 세션의 이미지 총수·JSON 배열 총수·누적 디스크 사용·누적 decode 시간에는 별도 상한이 없습니다. 외부의 자동 요청을 받는 서비스로 사용하려면 추가 격리와 자원 제한이 필요합니다.
- 보안 검토자는 구현·Chrome·원래 사용자 상태를 수정하지 않았으며 외부 서비스에 메시지·결제·게시·변경 요청을 수행하지 않았습니다. 작성 파일은 이 보고서뿐입니다.
- 재현 요약은 `/tmp/logo-security-audit.SA8ZiF/cli-probes.txt`, 값이 제거된 자료 스캔은 같은 폴더의 `text-scan-final.json`, `image-scan-final.txt`에 있습니다. 해당 임시 파일은 현재 로컬 검토 보조 자료이며 배포 ZIP에는 포함되지 않습니다.

최종 패치 재검증은 통과했습니다. `delivery.py:72`의 `_export_destination`은 잠금을 잡기 전에 내부 저장 영역을 판정하고, `.casefold()`로 대소문자를 정규화해 `.logo-generator`와 그 하위 경로를 거부합니다. 실제 CLI로 다음 7개 사례를 확인했습니다.

- `.logo-generator`, `.logo-generator/locks/audit.lock/new`, `.LOGO-GENERATOR/locks/audit.lock/new`, `.logo-generator/sessions/injected`, `.LoGo-GeNeRaToR/nested`: 모두 거부되고 원래 파일·디렉터리 내용과 구조가 보존됐으며 잠금이 남지 않았습니다.
- `.logo-generator-lookalike/export`, `.assets/export`: 정상 내보내기가 성공했으며 잠금이 남지 않았습니다.

최종 변경 뒤 `tests/test_reserved_output.py`와 `tests/test_cli_safety.py`를 실행한 **29개 테스트**도 통과했습니다. 변경된 `delivery.py`와 새 회귀 테스트의 Ruff 및 basedpyright는 오류·경고가 없습니다. 독립 7개 검사 로그는 `/tmp/logo-security-audit.SA8ZiF/reserved-output.txt`, 최종 ZIP 검사 결과는 같은 폴더의 `package-final.json`에 있습니다. 검증한 `delivery.py` SHA-256은 `4037d445e4dfc2d8e2ce661a82bc92b446755d817b86346a105a5b48791d2326`입니다. 실제 실행 환경은 macOS/Python 3.12이며 Windows에서의 실동작까지 검증한 것은 아닙니다.
