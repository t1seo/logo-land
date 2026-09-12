# 패키지와 개인 설치 검증

## 현재 설치: Logo Land

투명 배경 요청 지침과 시작 문구를 추가한 최신 설치 버전은 `0.3.0+codex.20260912135514`입니다. `codex plugin add logo-land@personal --json`, manifest 검사와 스킬 검사가 모두 통과했습니다. [투명 PNG 샘플과 검증](../transparency/README.md)을 참고해 주세요.

최종 이름은 `logo-land`입니다. 전용 로고를 포함해 `codex plugin add logo-land@personal --json`이 성공했으며 버전은 `0.3.0+codex.20260912133131`입니다. 소스는 `~/plugins/logo-land`, 캐시는 `<codex-home>/plugins/cache/personal/logo-land/0.3.0+codex.20260912133131`입니다. manifest·스킬 검사 및 이 캐시에서 브랜드 세션 revision 4 재개 조회가 통과했습니다.

이전 `logo-generator@personal`과 임시 `logo-kit@personal` 설치본은 CLI로 제거했습니다. 개인 marketplace의 다른 항목은 변경하지 않았습니다. 새 Codex 대화에서는 **`$logo-land`**로 시작하시면 됩니다. 저장소를 새로 내려받아 설치하는 방법은 [English README](../../README.md)와 [한국어 README](../../README.ko.md)에 있습니다.

## 이름 변경 전 기록

아래 ZIP과 캐시 경로는 최초 구현 당시의 검증 기록이며 현재 배포 다운로드 링크가 아닙니다. 개인 홈 경로는 배포용 문서에서 별칭으로 표시했습니다.

2026-09-12에 `dist/logo-generator-0.2.0.zip`을 만들고 `unzip -t`로 모든 항목을 검사했습니다. ZIP은 플러그인 manifest, 스킬·참조·예제·helper, pyproject, uv.lock, 짧은 사용 안내를 포함합니다. 연구 자료, 브라우저 계정 정보, 실제 사용자 세션, 테스트 캐시와 가상환경은 포함하지 않습니다.

개인 marketplace는 공식 plugin-creator scaffold로 `~/.agents/plugins/marketplace.json`에 생성했습니다. 이 환경의 CLI는 개인 marketplace의 `./plugins/logo-generator`를 `~/plugins/logo-generator`로 해석했습니다. 소스를 그 위치에 배치한 뒤 다음 명령이 성공했습니다.

```sh
codex plugin add logo-generator@personal --json
```

첫 설치는 `version: 0.2.0`으로 성공했습니다. 마지막 예약 출력 경로 수정 후 공식 cachebuster helper로 버전을 갱신하여 재설치했습니다. 최종 반환 값은 `pluginId: logo-generator@personal`, `version: 0.2.0+codex.20260912125753`, `authPolicy: ON_INSTALL`입니다. 설치 캐시는 현재 Orca Codex 계정 홈의 `plugins/cache/personal/logo-generator/0.2.0+codex.20260912125753`이며, 소스 위치는 `<plugin-sources>/logo-generator`입니다. 최종 플러그인·스킬 검사와 ZIP 무결성 검사도 통과했습니다.

`codex plugin list --json`은 기존의 별도 `astral-codex` marketplace에 지원되는 manifest가 없다는 오류로 실패했습니다. 이 오류는 개인 플러그인 추가 명령의 성공과 별개이며, 관련 없는 marketplace 설정은 변경하지 않았습니다. 전체 목록 조회가 정상이라고 주장하지 않습니다.

새 Codex 대화에서 `$logo-generator`로 시작하면 됩니다. 이번 세션에서 설치 명령과 파일 검증은 실행했지만, 사용자의 새 GUI 대화에서 스킬 선택까지 대신 실행한 것은 아닙니다. 독립 실행 QA의 패키지 이동·캐시 실행 결과는 [QA 검토](review-qa.md)에 기록합니다.
