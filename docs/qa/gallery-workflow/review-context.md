# T5 independent context review

**PASS · CTX-1 해결, 최종 해시 확인 및 정리 완료.** 비교 CLI·원본 다운로드·출처 보존이 통과했습니다. 연결된 릴리스 안내의 버전 모순 한 건을 발견한 뒤, 조정자의 동일 작업 범위 확장에 따라 해당 문서만 수정하고 실패/성공 검사 및 HTTP 검증을 마쳤습니다. T6 병합 대기는 실패 사유가 아닙니다.

검토 기준: `feat/logo-land-gallery-workflow`, HEAD/base `06b94c41922973fc98392fadde25fff9aa498f6e`. 추적되지 않은 신규 파일도 포함했습니다. 전체 명령 argv, 출력·상태·해시, 입력, 파일 목록과 자원 기록은 [review-context.json](review-context.json)에 있습니다.

## 발견 사항

**CTX-1 · MAJOR · 해결됨 · `docs/releases.md:5,33`의 최초 상태.** 5행은 현재 소스를 `0.5.0`이라고 설명하고, 33행은 저장소 manifest·Python 프로젝트·lockfile을 `0.5.0`으로 유지하라고 지시합니다. 실제 세 메타데이터와 양쪽 설치 안내는 `0.6.0`입니다. `docs/installation.md`와 `.ko.md`가 이 릴리스 안내로 연결하므로 현재 개발/설치 버전의 설명이 서로 충돌합니다.

```sh
sed -n '1,40p' docs/releases.md
cat .codex-plugin/plugin.json
```

실제 출력: `Current source is **0.5.0, unreleased**`, `Keep the repository manifest, pyproject.toml and uv.lock at clean 0.5.0`와 manifest `"version": "0.6.0"`. 원래 문서 해시: `9db0a035add342fb63cf351303f09f67b163f79c68fec128cc9fd9471244c5e8`. 현재 소스·캐시 예제를 0.6.0으로 고치고, 0.5.0 이력·정식 0.3.1·미게시 0.4.0 사실은 보존해야 합니다. 조정자에게 `msg_b79d9a06e7c6`으로 전달했습니다. 해당 메시지의 “30행”은 “33행”으로 정정합니다.

## 문서·출처·이력

- 최초 변경 공개 Markdown **25개 전체**와 이후 수정한 릴리스 안내를 읽었습니다. 양쪽 README·문서 색인·카테고리·설치·전체 갤러리, 신규 샘플/상태 안내, SKILL과 변경된 사용 지침을 포함합니다. 정확한 목록은 JSON `modified_public_docs`입니다. 관련 helper 전체 파일, T1–T5 계획, T3 통합, T4 Chrome·restoration·README 보완, 원래/갱신 설치 기록도 확인했습니다.
- 영어 기본 소개와 한국어 대응 내용이 일치합니다. README는 짧은 설치·요청·기능·출처 흐름이며 긴 조사/개발 진행 본문을 추가하지 않았습니다. 샘플 단락은 양쪽 모두 **3+3**입니다.
- 양쪽 전체 갤러리에 **54개 PNG 경로 / 53개 고유 해시**가 동일 순서로 있습니다. 모든 썸네일의 href와 src가 같으며 밤결의 복제 부모만 동일 해시입니다. 변경 공개 문서의 실제 로컬 파일 링크는 모두 존재합니다. 앵커와 실제 Chrome 클릭은 T3/T4의 해시 연결 검증을 재사용했습니다.
- 공개 receipt 8개를 이미지·프롬프트·부모 입력 해시와 대조했습니다. **6회 초기 + 2회 자식**, 6개 세션, 7개 아이콘(1254×1254)과 COMMON(1774×887)이며 실제 helper `show`로 복원한 상태의 선택/검수는 모두 null입니다. `planned → running → returned → imported`, 네이티브 도구, 모델 미보고가 일치합니다.
- Leaflet 추가 색, Relay의 넓어진 틈과 기하 변화, Sprig의 불명확한 왼쪽 굽힘과 32px 개선 미입증을 양쪽 문서가 보존합니다. 생성 담당자의 관찰을 독립적인 품질 벤치마크로 바꾸지 않았습니다. 갤러리/메모는 승인, CSS 미리보기는 플랫폼 패키지, 래스터 글자는 폰트 조판으로 표현하지 않습니다.
- 기준 커밋의 역사적 파일 **331개**를 git blob과 비교하여 변화가 없음을 확인했습니다. 이전 IP 원본/프롬프트, 색상 실패·미확정 기록과 출처를 포함합니다. 기존 네이티브 동시 실행 수 지침 이탈도 native-samples.md에 공개되어 있고 삭제되지 않았습니다.
- IP 안내는 s1dashu의 [`acb834c717bcd0a487c49732d08397ba280d690b`](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/SKILL.md)를 명시합니다. `gh api`로 가져온 동일 커밋 LICENSE와 번들 MIT 고지가 바이트 단위로 일치합니다: `b8f39925b1c36ca531c5e663aeb7ba427f94a526495785b4d1b2797fae8f2546`.
- 실제 `gh repo view`, 전체 issue/PR 조회(각 0건), release API와 git log/blame을 확인했습니다. [`v0.3.1`](https://github.com/t1seo/logo-land/releases/tag/v0.3.1)은 2026-09-12T14:12:52Z 게시됐고, v0.4.0은 `draft:true`, `published_at:null`입니다. 0.6.0은 미출시 소스입니다. git 이력 `fd1d89c`의 영어 기본/버전 정렬, `b391ca8` 색상 기능, `6d946e6` 아이콘 업데이트와 호환 경로 보존이 이어집니다.
- 설치 지침은 소스 체크아웃, 로컬 marketplace, 설치 캐시와 새 대화 필요성을 구분합니다. 갱신 설치 `0.6.0+codex.20260913005849` 증거의 소스 74개(고지 포함)가 현재와 일치합니다. 설치를 재실행하거나 현재 대화의 스킬 갱신을 주장하지 않았습니다. 예전 설치의 별도 astral marketplace 오류도 기록에 남아 있습니다.
- Slack/Notion/email: **N/A**, 요청 범위 밖이며 접근하지 않았습니다.

## 해시와 기존 검증 재사용

독립적인 디렉터리 열거로 final-bindings 파일 집합까지 대조했습니다. 아래 집합은 실제 CLI 전에 고정했고 실행 후에도 같습니다.

| 집합 | 개수 | SHA-256 집계 |
|---|---:|---|
| 소스 payload | 73 | `039501853cade59c4d05f448c85e8d50b71888d7d16e6e45e29b9bcaa6f7dbc7` |
| Python + Node 테스트 | 41 | `834097dae4a4160f74ffc69488be681869769c1937a79b63de53e7de0206392c` |
| 공개 파일 | 183 | `0cf9433aa0004f0a274e77c7e628683cb33795151a7664b221a6eec025c67abe` |

T3 대비 변경은 소스의 HTML 템플릿 1개와 공개 파일의 양쪽 README·생성 index 3개뿐입니다. 기존 Python 테스트 40개는 같고 Node `.mjs` 회귀 1개가 추가됐습니다. **622개 Python 통합 테스트**는 기존 실행을 재사용했습니다. T4의 `node --test tests/comparison_browser_restoration.test.mjs` **6개**와 별도 Python **58개** 통과는 현재 템플릿·테스트·index에 연결됩니다. README 3+3 수정과 Chrome Back 복구는 해당 보완 기록에 연결했습니다. 과거 T3 index와 현재 index가 같아야 한다고 요구하지 않았고 전체 테스트를 반복하지 않았습니다.

## 새 실제 실행

공개 스냅샷의 `state`를 새 세션 JSON으로 복원하고, 8개 원본을 지정 경로에 복사했습니다. helper `--help`와 실제 `show` 6개를 실행한 뒤 COMMON/Drip 두 후보를 선택 입력으로 지정했습니다.

```sh
uv run python skills/logo-land/scripts/logo_project.py --help
uv run python skills/logo-land/scripts/logo_project.py --workspace /tmp/ll-060-review-context compare-gallery --selection-file /tmp/ll-060-review-context/inputs/selection.json --output gallery
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8799/gallery/index.html
```

CLI exit 0, 실제 JSON `{"path":"gallery","index_path":"gallery/index.html","count":2}`. HTTP/1.0 **200 OK**, curl exit 0, 본문 해시 `5cf64653c02172b697239f1cfc34a50a99c9a7da4e670cfbdaf338b87b93bed7`. 실제 원본 링크 4개를 내려받아 manifest·원본과 대조했습니다.

| 원본 정체성 | PNG SHA-256 | 프롬프트 SHA-256 |
|---|---|---|
| common / v1 / revision 1 / brand | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` |
| drip / v1 / revision 1 / app_icon | `8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f` | `67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d` |

**CLI/HTTP binary PASS**입니다. 최초 문서 verdict FAIL은 CTX-1 수정으로 해결됐으며, 갱신된 최종 파일 집합까지 확인하여 문서 관점도 PASS입니다.

| 필수 adversarial class | 실제 관찰 / 재사용 |
|---|---|
| Malformed | 실제 잘린 JSON exit 1, 중복 `(session,artifact)` exit 1; 목적지 없음. |
| Prompt injection | `</script>`, img/onerror, 승인 지시, `$()`·백틱을 rationale에 입력. 실제 gallery exit 0, 전체 escaped 문자열, 저작 스크립트 1개, sentinel 없음, 승인 변화 없음. 네이티브 모델 면역 주장 없음. |
| Cancel/resume | 실제 read-only prompt 프로세스에 SIGINT 두 번; 모두 Python import 중 exit 130. 각 중단 후 새 show 성공, 15개 fixture/보호 파일의 바이트 동일. |
| Stale | 현재 common revision 1에 revision 0 입력: exit 1, `stale_revision`, 목적지 없음. |
| Dirty worktree | 시작 상태와 추적/미추적 파일 해시 고정. 이미 있는 gallery 출력은 conflict exit 1로 거부하고 모든 기존 파일·foreign marker 보존. |
| Hung commands | helper/GitHub 30초, curl connect 3초/total 20초, server 120초 상한. 시간 초과 없음, owned server 종료·회수. |
| Flaky tests | 전체/집중 suite는 해시 연결 기록 재사용. 숨은 재시도 없음. 초기 git blame의 두 경로 문법 오류(exit 129)는 경로별 조회로 수정하여 모두 공개. |
| Misleading success | 실제 JSON·HTML 정체성·원본/프롬프트 해시·null 승인을 확인. CTX-1 최초 모순을 FAIL로 보존하고, 별도 실제 실패/수정/성공/HTTP 기록으로 해결함. |
| Repeated interruptions | 두 번의 SIGINT/새 show, 예정된 HTTP 본문 3회 읽기 모두 바이트 보존. publication 단계 반복 중단은 T1/T3/T4의 현재 소스에 연결된 기존 증거 재사용. 유료 네이티브 중단/재생성은 N/A. |

Chrome·설치·네이티브 작업을 새로 실행하지 않았습니다. 이번 수정은 Markdown 안내와 보고서뿐이므로 새 build/LSP 결과는 N/A이며, 기존 성공 기록을 새 실행처럼 표현하지 않았습니다.

## 자원 정리

생성 전 `/tmp/ll-060-review-context`, `audit.rb`·`smoke.rb`·`finish.rb`, fixture/입력/gallery/download/log 하위 경로와 `127.0.0.1:8799`를 등록했습니다. 실제 서버 PID **29046**는 SIGTERM 후 회수됐고 포트 재바인딩이 성공했습니다. helper·GitHub 등 자식 PID/argv/종료 상태는 JSON에 있습니다. Ruby driver의 OS PID는 보존하지 못했으며, 도구 세션 **76866 / 16281 / 99953**의 exit 0 완료 기록을 대신 남겼습니다.

범위 확장 후 `fix-guide.rb`, `releases.before.md`, `releases.md`, guide-server 로그도 생성 전에 등록했습니다. 임시 파일별 inode·해시 목록을 보존한 뒤 소유한 파일과 빈 디렉터리만 삭제하고, 등록된 프로세스/포트/임시 루트 부재를 최종 확인했습니다. 삭제 완료 영수증은 아래와 JSON cleanup에 기록했습니다. 최종 gallery 페이지·서버·브라우저는 보존하지 않습니다. 조정자가 관리하는 Chrome과 다른 작업자의 자원은 건드리지 않았습니다.

## CTX-1 수정 및 재검증

권한: 조정자 `msg_9226efb8c231`. 현재 소스 소개·해당 계획 링크·로컬 캐시 예제만 0.6.0으로 맞췄습니다. 기존 공개 릴리스/미게시 초안, 실패 근거, 릴리스 절차는 바뀌지 않았습니다. 최초 해시와 전체 본문을 JSON에 보존했습니다.

현재 버전 assertion은 수정 전 exit 1(`FAIL: current source must be 0.6.0`), 같은 argv로 수정 후 exit 0입니다. 예상 세 치환으로 전체 파일이 정확히 재현되며 로컬 링크와 `git diff --check`도 통과했습니다.

```sh
curl -i --fail --connect-timeout 3 --max-time 20 http://127.0.0.1:8799/releases.md
```

실제 HTTP/1.0 200 OK, exit 0, 저장소 최종 문서와 응답이 완전히 같습니다. 최종 SHA-256: `e3f6aa8d31b7356bb3440e71c8dbda5720bff50a4cd5546bcdbffa006d354f35`. 새 이미지/설치/테스트 반복 없이 검증했습니다. SOURCE READY는 `msg_3de5d2aeec75`로 전달했으며 조정자가 공개 파일 해시 집합을 갱신합니다.

## 최종 확인과 완료 영수증

조정자 `msg_37c96024aeda`의 갱신 목록 SHA `df6c741906d3df829f387d9e6c1a6c2a753e2c6e219d154504f636f15a221337`를 실제 파일과 대조했습니다. 소스 73개와 테스트 41개는 검토 시작과 동일하고, 공개 183개 중 `docs/releases.md`만 위 승인 수정으로 달라졌습니다. 최종 공개 집계는 `d6f164db0e3fa470aff3798db251cef299f43792e89fda61b3b09abbd5d8f409`입니다. 위 `0cf9433...` 집계는 이번 수정 전 T4 상태이며 이력이므로 보존합니다. 모든 현재 파일과 집계가 새 final-bindings에 일치합니다.

**정리 PASS:** 임시 파일 44개를 inode·해시 확인 후 개별 삭제하고 빈 하위 디렉터리 23개와 루트를 제거했습니다. 등록 자식 PID 45개 및 cleanup driver PID 38297의 부재를 확인했습니다. 두 서버를 각각 회수했고 8799 재바인딩이 성공했습니다. 도구 세션 76866·16281·99953은 종료됐습니다. 임시 루트·갤러리·스크립트·다운로드·로그·서버는 남지 않았으며, 증거는 이 보고서/JSON에 보존했습니다.

미해결 검토 사항은 없습니다. 전달 변경 파일은 `docs/releases.md`와 이 보고서 쌍뿐입니다. 다른 리뷰·병합·공개 여부는 조정자가 관리합니다.
