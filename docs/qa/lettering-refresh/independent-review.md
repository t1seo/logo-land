# 레터링 업데이트 독립 검토

**판정: PASS — 검토 범위에서 수정이 필요한 회귀를 발견하지 못했습니다.**

2026-09-14, 기준 커밋 `a472e50`과 현재 공유 작업 트리를 비교했습니다.
Orca 작업은 `task_52bf919cc2c1`, Dispatch는 `ctx_36bc90fbac3a`입니다.
소스·README·이미지·릴리스 파일은 수정하지 않았으며, 저장소 안에는 이 보고서만 작성했습니다.
실행 자료는 `/tmp/logopia-independent-20260914-52bf919c/`에 남겼습니다.

아직 게시되지 않은 v0.7.0 링크는 아래의 **통합·게시 확인 사항**으로 분리했습니다.
이 PASS는 구현·현재 파일·문서의 검토 결과이며, 원격 게시 완료를 뜻하지 않습니다.

## 검토한 구현과 안내

[core-report.md](core-report.md), [docs-report.md](docs-report.md),
현재 [verification.md](verification.md)를 읽고 실제 변경 내용과 대조했습니다.
핵심 변경은 [prompts.py](../../../skills/logo-land/scripts/logo_helper/prompts.py)와
[logo_prompts.py](../../../skills/logo-land/scripts/logo_helper/logo_prompts.py)입니다.

- [SKILL.md](../../../skills/logo-land/SKILL.md), [레터링 안내](../../../skills/logo-land/references/lettering.md),
  [타이포그래피 안내](../../../skills/logo-land/references/typography.md), 로고 유형 및 전달 점검 안내가
  `wordmark`·`lettermark`·`monogram`·`combination`을 같은 의미로 설명합니다.
  글자 적층을 별도 심볼 배치로 오인하거나 브랜드명에서 임의 이니셜을 만들도록 지시하지 않습니다.
- 새 로고에만 유형별 제작 지침을 적용합니다. 수정에서는 실제 부모 이미지, 최신 요청,
  부모의 변경된 글자·배치·팔레트가 우선하며 초기 브리프를 역사적 문맥으로 표시합니다.
- 앱 아이콘 분기는 일반 레터링 지침을 덧붙이기 전에 반환합니다. 기존 여덟 로고 유형,
  여섯 아이콘 프리셋, 세션 형식과 의존성을 유지합니다.
- 자연어의 유형 선택은 스킬을 읽는 에이전트의 역할이라고 명시합니다. Python이 자연어를
  자동 분류하거나 실제 생성 이미지의 철자를 보증한다고 과장하지 않습니다.
- 일색 실루엣 평가는 추가 단색 납품물이 아닙니다. 실제 이미지의 철자·한글·색상·투명도는
  직접 확인하며, 폰트 파일·벡터·플랫폼 아이콘 패키지로 설명하지 않습니다.

## 실제 CLI 동작: 9개 시나리오 PASS

현재 `.venv/bin/python`으로 실제 `skills/logo-land/scripts/logo_project.py`를
별도 임시 작업 공간에서 실행했습니다. 총 **88회 CLI 호출**이며, 자체 작성한 좁은 범위의
검증으로 안내된 주요 동작을 확인했습니다. 가져온 PNG는 기존의 명시적인 합성 테스트
파일입니다. 아래 결과는 프롬프트·저장·상속 검증이며 새 이미지 생성 품질을 주장하지 않습니다.

| 시나리오 | 실제 입력과 확인 결과 |
|---|---|
| 글자만 있는 워드마크 | 긴 브랜드 문맥과 별도로 `exact_text="Luma Lab"`을 사용했습니다. 글자 구성 지침과 별도 아이콘 금지가 포함되고, `lockup=null`이 prompt/import에서 유지되었습니다. |
| 전체 브랜드명이 아닌 기하학 이니셜 | `brand_name="North Ridge Solutions"`, `exact_text="NR"`, `logo_type="lettermark"`, N 위·R 아래라는 concept를 사용했습니다. 렌더링 문자열은 NR이며, 읽을 수 있는 독립 글자 지침을 받고 심볼 배치가 생기지 않았습니다. |
| 한글과 정확한 문자열 | 앞뒤·연속 공백, `너울  Lab`, 따옴표, `A`+결합 악센트, 줄바꿈, 분해된 `한`, 구두점 및 별도 슬로건을 전달했습니다. 저장된 exact_text/slogan 및 최종 prompt가 문자 단위로 일치했습니다. 브랜드 레터링에 아이콘의 8코드포인트 제한이 적용되지 않았습니다. |
| 변경된 부모 글자와 오래된 이름 | 최초 `OLD COMPANY` → v2에서 `너울  Lab`으로 교체 → v3에서 속공간만 넓히는 연속 수정입니다. 반환된 실제 부모는 v2이며, 이전 이름은 역사적 문맥으로만 남았습니다. 새 생성 지침은 없고, 기존 이미지와 이력은 유지되었습니다. |
| 명시적인 심볼+문자 배치 | 초기 wordmark 브리프에 stacked/start/center lockup을 명시했습니다. 조합형 지침이 우선하고, 다음 수정은 이를 상속했습니다. 이후 horizontal/end로 명시 변경했을 때에도 prompt/import의 배치가 일치했습니다. |
| 기존 앱 아이콘 경로 | 여섯 프리셋 각각의 생성·수정, 총 12개 결과를 `git archive a472e50 skills/logo-land/scripts`로 가져온 실제 기준 CLI와 비교했습니다. prompt 문자열이 완전히 일치하고 반환 JSON 값도 동일하며, 일반 레터링 지침이 섞이지 않았습니다. |
| 엄격한 팔레트 보존 | 다색·입체·그라데이션 스타일 문맥과 충돌하는 `#123456` 단일 locked/required/allowed 색상, `max_colors=1`, `allow_gradients=false`를 사용했습니다. 구조화된 제한과 digest가 유지되며, 활성 팔레트를 바꿔도 부모 수정은 원래 팔레트를 상속했습니다. 실제 color-analyze도 합성 이미지의 색상 차이를 `mismatch`로 기록했습니다. |
| 오래된 세션 | 저장된 schema-1 및 schema-2 fixture에서 show/list/prompt가 원본 JSON을 다시 쓰지 않았습니다. 첫 import는 schema-1에만 원본 그대로의 백업을 만들며 schema-2로 이행하고, 옛 prompt·PNG·알 수 없는 부모 lockup/palette/icon 의도를 유지했습니다. |
| 오래된 revision 거절 | 이미 진행된 세션에 revision 0으로 import했습니다. 요청이 거절되고 세션 바이트는 그대로였습니다. |

첫 부모 경로 검사에서는 macOS의 `/tmp` → `/private/tmp` 정규화를 고려하지 않아
검증 코드의 비교가 실패했습니다. 비교를 `Path.resolve()`로 수정하고 해당 시나리오만
7회 호출로 다시 확인하여 통과했습니다. 이는 제품 결함이 아니며 최초 실행 기록도 보존했습니다.

실행 자료:

- `probe.py`: 검증 코드입니다. 재실행할 때마다 새 임시 작업 공간을 만듭니다.
- `commands.json`, `followup-commands.json`: 모든 CLI 인수·stdout·stderr·종료 코드입니다.
- `final-probe-results.json`: 해당 경로 검사를 바로잡은 최종 9개 결과입니다.

```sh
.venv/bin/python /tmp/logopia-independent-20260914-52bf919c/probe.py
.venv/bin/python /tmp/logopia-independent-20260914-52bf919c/asset_check.py
.venv/bin/python /tmp/logopia-independent-20260914-52bf919c/docs_check.py
uv lock --check
git diff --check
```

독립 검토에서 `uv lock --check`와 `git diff --check`도 통과했습니다.
642개 전체 테스트, Ruff, basedpyright와 스킬 검사는 구현 담당자의
[실행 기록](core-report.md)을 검토했으며, 이 리뷰가 같은 전체 검사를 다시 실행한 것은 아닙니다.

## 이미지·출처·배포 메타데이터: PASS

[manifest.json](../../showcase/2026-09/manifest.json)의 identity 1개와 showcase 16개를
[catalog.json](../../showcase/2026-09/catalog.json), 실제 PNG, 선택된 receipt, 최종 prompt,
import 기록 및 현재 로컬 세션의 원본과 대조했습니다. 모두 식별자·부모·정확한 문자열·해시가
일치합니다. 실제 PNG 형식·크기·투명 픽셀 여부도 manifest/receipt와 일치합니다.

16개 현재 이미지 경로는 다음과 같습니다. 아래 파일은 모두 불투명 PNG이며,
NOVA NOTES만 1536×1024, 나머지는 1254×1254입니다.

| 이미지 경로 (`docs/showcase/2026-09/` 기준) | 연결된 artifact |
|---|---|
| [images/01-luma.png](../../showcase/2026-09/images/01-luma.png) | a-v2 ← a-v1 |
| [images/02-loop-lab.png](../../showcase/2026-09/images/02-loop-lab.png) | a-v1 |
| [images/03-goyo.png](../../showcase/2026-09/images/03-goyo.png) | a-v1 |
| [images/04-bread-bloom.png](../../showcase/2026-09/images/04-bread-bloom.png) | a-v1 |
| [images/05-kite.png](../../showcase/2026-09/images/05-kite.png) | a-v1 |
| [images/06-miso.png](../../showcase/2026-09/images/06-miso.png) | a-v1 |
| [images/07-northline.png](../../showcase/2026-09/images/07-northline.png) | a-v1 |
| [images/08-mulgyeol.png](../../showcase/2026-09/images/08-mulgyeol.png) | a-v2 ← a-v1 |
| [images/09-fern.png](../../showcase/2026-09/images/09-fern.png) | a-v1 |
| [images/10-nova-notes.png](../../showcase/2026-09/images/10-nova-notes.png) | a-v1 |
| [images/11-reading-owl.png](../../showcase/2026-09/images/11-reading-owl.png) | a-v1 |
| [images/12-weather.png](../../showcase/2026-09/images/12-weather.png) | a-v1 |
| [images/13-flow.png](../../showcase/2026-09/images/13-flow.png) | a-v1 |
| [images/14-notes.png](../../showcase/2026-09/images/14-notes.png) | a-v1 |
| [images/15-cloud.png](../../showcase/2026-09/images/15-cloud.png) | a-v1 |
| [images/16-sprout.png](../../showcase/2026-09/images/16-sprout.png) | a-v1 |

19개 receipt가 초기 생성 17회·수정 2회를 기록하고, 선택하지 않은 LUMA/물결의 초기 PNG와
prompt도 해시가 맞는 상태로 남아 있습니다. tool은 `image_gen__imagegen`, model은
`unreported`로 기록되었습니다. 이 검토는 저장된 출처 기록과 원본을 대조했으며 생성 호출을
재실행하거나 별도의 모델 신원을 증명하지 않았습니다.

[보드](../../../assets/logo-land-showcase.png)는 2400×3182입니다.
[HTML](../../showcase/2026-09/index.html)의 img 16개가 정확히 현재 manifest의 showcase
집합과 일치합니다. 보드·브랜드 마스터·현재 물결 원본을 직접 열었고, 담당자가 기록한
[240px/64px 화면](actual-size.png)과 [한국어 모바일 README](readme-ko-mobile.png)도 확인했습니다.
LOGO/LAND, LUMA, NL, 고요, 물결, 틈을 구분할 수 있었으며, 물결의 수정본에는 ㅜ의 아래획이
보입니다. 모바일 보드는 전체 개요로 쓰이며, 개별 파일과 큰 보드로 이어지는 링크가 있습니다.
새 브라우저 세션의 최종 점검은 요청대로 코디네이터가 담당했습니다.

브랜드 마스터의 SHA-256은
`3b8c127df99e54b76eb6588204f9b2efdfbb908ad649f6a9891118f9d9a38994`입니다.
README 자산, showcase의 identity, 전달 PNG 및 ZIP 안의 PNG가 같은 바이트입니다.
ZIP 무결성, manifest와 brand-guide의 외부 파일/ZIP 내부 바이트도 일치합니다.
브랜드 export는 `color_policy: unverified`이며 이를 엄격한 팔레트 통과로 오인하지 않습니다.

`.codex-plugin/plugin.json`, `pyproject.toml`, `uv.lock`의 버전은 모두 **0.7.0**입니다.
플러그인 이름과 호출은 `logo-land`/`$logo-land`, repository는 `t1seo/logopia`,
brandColor는 `#17352B`, 로고 경로는 `./assets/logo-land-wordmark.png`로 일치합니다.
의존성 변경은 없습니다.

## 문서 링크와 최종 통합 상태

현재 README·문서·스킬 안내 23개에서 **817개 링크/이미지 참조**를 파싱했습니다.
로컬 누락 파일, 잘못된 Markdown fragment, 중복 anchor, 기존 heading/명시 anchor 손실이
모두 **0개**였습니다. Markdown 및 HTML 링크를 함께 읽고 front matter는 제목에서 제외했습니다.
두 README는 각각 로컬 이미지 2개, 배지 3개와 대체 텍스트를 갖춥니다.

기록된 외부 URL 10개도 실제 HTTP로 확인했습니다. 9개는 200이며, 이전 저장소 이름을 쓰는
[폰트 조사 링크](https://github.com/t1seo/logo-land/blob/main/docs/research/font-tools.md)는
현재 [logopia 경로](https://github.com/t1seo/logopia/blob/main/docs/research/font-tools.md)로
정상 이동했습니다. 이전 색상 실험의 실패·미확정 기록은 역사적 자료로 남아 있습니다.

코디네이터의 `msg_9d6242da415e`에 따라 브랜드 페이지의 ZIP/guide 추가와 360px hero를
최종 상태로 검토했습니다. docs 담당자의 과거 해시가 달라진 것은 알려진 통합 변경이며,
현재 파일의 링크와 패키지는 이 리뷰에서 재확인했습니다. `verification.md`도 이미 존재합니다.
현재 검토한 브랜드 페이지의 SHA-256은 다음과 같습니다.

- `docs/brand/README.md`: `aaa05aaf6e23491a3cfe7490e342b4cbe069d78cdd56d8c9dc204d0e25e2919a`
- `docs/brand/README.ko.md`: `9f74eb468df9fdf840d2b590e62e99a9646c9b74cf868735476987f413264796`

### 통합·게시 확인 사항 — 구현 회귀와 구분합니다

2026-09-14 **07:57 UTC / 16:57 KST** 검사 당시
[v0.7.0 릴리스 URL](https://github.com/t1seo/logopia/releases/tag/v0.7.0)은 **HTTP 404**였습니다.
코디네이터가 아직 게시를 진행하기 전이므로 예정된 릴리스 링크의 통합 상태로 분류합니다.
게시 후 해당 URL, tag와 최종 커밋의 일치, 릴리스 첨부 파일을 확인해 주세요.
현재 README의 Release 배지는 정적 이미지이므로 배지 이미지의 HTTP 200만으로
릴리스가 게시되었다고 판정하지 않아야 합니다.

현재 manifest·16개 다운로드·브랜드 ZIP/guide·버전 메타데이터의 추가 수정은 필요하지 않습니다.
이후 코디네이터가 변경한 파일은 최종 해시/링크 확인 대상입니다.
리뷰어는 commit, push, tag, release, 배포 또는 설치를 수행하지 않았습니다.
