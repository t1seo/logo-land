# Installation verification

## Current development installation after final corrections

Verified on **2026-09-13 KST**. The repository source, Python project and lock remain **`0.4.0`**. The refreshed personal installation is **`0.4.0+codex.20260912161802`**, incorporating the legacy metadata export correction and matching Dark-preview surface. Version 0.4.0 is unreleased; the published release remains 0.3.1 because required native sample gates are unmet.

The final payload contains **55 files**. All 54 non-manifest files match the source; the manifest differs only by the official local cachebuster. The actual installed helper completed **29 CLI invocations: 27 successes and two expected strict-export refusals**. Original PNG/ZIP integrity, schema-1 metadata compatibility, advisory uncertainty and the generated `#171717` Dark preview were checked.

See the [final installed-cache report](color-workflow/installation-040-final.md) for exact commands, hashes, validation and scope. Existing native originals were reused; this is not new image generation, cold-cache offline installation or a fresh GUI-thread invocation. Start a **new Codex conversation** with **`$logo-land`** to load the refreshed skill.

## Earlier v0.4.0 installation checkpoint

The following record predates the final compatibility correction and cache refresh above. Its original commands and version remain historical evidence.

Verified on **2026-09-13 KST**. The repository source manifest, Python project and locked helper package are **`0.4.0`**. The personal installation is **`0.4.0+codex.20260912153655`**, using the official `plugin-creator` cachebuster helper. The suffix refreshes the local Codex cache; it is not a release version. Version 0.4.0 remains unreleased because required native sample checks did not pass; the latest published release is 0.3.1.

| Location | Plugin manifest version | Python project / locked helper version |
| --- | --- | --- |
| Repository working tree | `0.4.0` | `0.4.0` / `0.4.0` |
| Personal source: `~/plugins/logo-land` | `0.4.0+codex.20260912153655` | `0.4.0` / `0.4.0` |
| Installed cache: `<codex-home>/plugins/cache/personal/logo-land/0.4.0+codex.20260912153655` | `0.4.0+codex.20260912153655` | `0.4.0` / `0.4.0` |

`<codex-home>` denotes the active Orca Codex account's home. Its `plugins` directory resolves to the user's shared `~/.codex/plugins` directory. Public records use these aliases instead of private account paths.

The personal source had no differences from its previous 21-file installed cache or repository `HEAD`, apart from the expected manifest cachebuster. After checking for personal edits, the release payload was synchronized, the official validator passed for both personal source and installed cache, and `codex plugin add logo-land@personal --json` returned the version and cache path above. Both installed trees contain the same **55 packaged files**; all **54 non-manifest files** match the repository byte-for-byte. The manifest differs from the public version only by its cachebuster. The payload includes the new color, reference, lockup, gallery and export helpers and `THIRD_PARTY_NOTICES.md`, with no runtime caches, project outputs or private files.

The helper was then executed **from that installed cache**, with the working directory and session data in a separate `output/install-040-workspace/`. All 15 CLI calls succeeded: session initialization, palette proposal/save, prompt/lockup binding, real-original import, color analysis, gallery creation, visual review, selection, export, and a separate reference extraction/proposal/save/prompt check. The exact NORTHLINE brief, palette, lockup, final native prompt and existing native PNG were preserved. The stored Chrome large/128 px review supplied visual evidence; the original and both saved 128 px light/dark screenshots were reopened during this installation check.

The exported **schema-2 manifest** records the selected palette, lockup and recomputed color report. ZIP integrity passed, its only entries are `logo.png`, `manifest.json`, and `brand-guide.md`, and the archived PNG is byte-identical to the actual native original:

```text
SHA-256 3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534
```

The color report is `pass` under **advisory** palette intent; this is not an exact-pixel or strict-color certification. NORTHLINE is intentionally opaque, and `transparency_verified` is false. Full commands, hashes, observations and limitations are in the [v0.4.0 installed-helper evidence](color-workflow/installation-040.md).

`codex plugin list --json` still exits 1 because the unrelated configured `astral-codex` marketplace lacks a supported manifest. That configuration was not changed. This run did not perform fresh native generation, a cold-cache offline installation, a new GUI-thread skill invocation, commit, push or release. The public plugin files and original NORTHLINE session remained unchanged.

Start a **new Codex thread** and invoke **`$logo-land`** to pick up the refreshed skill. For example: `$logo-land Help me create a logo that fits my brand.`

## Historical records: Logo Land v0.3.1

Verified on **2026-09-12**. The release version is **`0.3.1`**. The local installation uses **`0.3.1+codex.20260912140549`**, generated by the official `plugin-creator` cachebuster helper. The `+codex.<timestamp>` suffix identifies this local Codex cache refresh; it is not a separate release version and does not belong in the repository's release manifest or Python package version.

| Location | Plugin manifest version | Python project / locked helper version |
| --- | --- | --- |
| Repository, tracked release files | `0.3.1` | `0.3.1` / `0.3.1` |
| Local source: `~/plugins/logo-land` | `0.3.1+codex.20260912140549` | `0.3.1` / `0.3.1` |
| Installed cache: `<codex-home>/plugins/cache/personal/logo-land/0.3.1+codex.20260912140549` | `0.3.1+codex.20260912140549` | `0.3.1` / `0.3.1` |

`<codex-home>` denotes the active Orca Codex account's home directory. The repository checks above refer to the working-tree contents of Git-tracked files; this installation check does not establish that a commit, tag, or release asset has been published.

### Installation and verification evidence

The installation step validated the `personal` marketplace with the official helper, synchronized the release files to `~/plugins/logo-land`, generated the local cachebuster, and successfully ran:

```sh
codex plugin add logo-land@personal --json
```

The subsequent read-only verification confirmed:

- `.codex-plugin/plugin.json`, `pyproject.toml`, and `uv.lock` are Git-tracked repository files. Their release versions are `0.3.1`; the lockfile check targets the `logo-land-helper` package entry.
- The repository, local source, and installed cache have identical English interface text and all four `interface.defaultPrompt` entries. These cover brand creation, color-only refinement, saved-project resume/export, and transparent-background creation or removal. The first prompt is `$logo-land Help me create a logo that fits my brand.`
- Both installed trees contain exactly the same 21 packaged files tracked under `.codex-plugin/`, `assets/`, `skills/`, `pyproject.toml`, and `uv.lock`, with no missing or extra files. All 20 non-manifest files are byte-for-byte identical to the repository. The manifest objects match after removing only the exact `+codex.20260912140549` suffix from their version fields; the source and cache manifests are also byte-for-byte identical to each other.
- The official `plugin-creator/scripts/validate_plugin.py` validator exited successfully for both `~/plugins/logo-land` and the installed cache shown above.

This follow-up changed only this installation record. Plugin sources and caches were inspected read-only; configuration and other marketplace entries were left untouched. No reinstall or publication was performed during verification.

### Pick up the updated plugin

Start a **new Codex thread** and invoke **`$logo-land`** so the updated skills and tools can be loaded. For example: `$logo-land Help me create a logo that fits my brand.` The official `plugin-creator` update guide recommends a new thread after reinstalling.

This record verifies installation files and manifest validity. It does not claim that the refreshed plugin was selected in a new GUI thread or that a new image-generation session was run. Fresh-clone installation instructions are in the [English README](../../README.md) and [Korean README](../../README.ko.md).

## Historical records: Logo Land v0.3.0

The following records describe earlier installations and their checks, not the current v0.4.0 installation. Historical cache paths are retained as evidence and are not current download links.

투명 배경 요청 지침과 시작 문구를 추가한 당시 설치 버전은 `0.3.0+codex.20260912135514`였습니다. 당시 `codex plugin add logo-land@personal --json`, manifest 검사와 스킬 검사가 모두 통과했습니다. [투명 PNG 샘플과 검증](../transparency/README.md)을 참고해 주세요.

이름을 `logo-land`로 변경한 당시에는 전용 로고를 포함해 `codex plugin add logo-land@personal --json`이 성공했으며 버전은 `0.3.0+codex.20260912133131`이었습니다. 당시 소스는 `~/plugins/logo-land`, 캐시는 `<codex-home>/plugins/cache/personal/logo-land/0.3.0+codex.20260912133131`이었습니다. manifest·스킬 검사 및 이 캐시에서 브랜드 세션 revision 4 재개 조회가 통과했습니다.

이름 변경 당시 이전 `logo-generator@personal`과 임시 `logo-kit@personal` 설치본은 CLI로 제거했습니다. 개인 marketplace의 다른 항목은 변경하지 않았습니다.

## Historical records: before the rename (v0.2.0)

아래 ZIP과 캐시 경로는 최초 구현 당시의 검증 기록이며 현재 배포 다운로드 링크가 아닙니다. 개인 홈 경로는 배포용 문서에서 별칭으로 표시했습니다.

2026-09-12에 `dist/logo-generator-0.2.0.zip`을 만들고 `unzip -t`로 모든 항목을 검사했습니다. ZIP은 플러그인 manifest, 스킬·참조·예제·helper, pyproject, uv.lock, 짧은 사용 안내를 포함합니다. 연구 자료, 브라우저 계정 정보, 실제 사용자 세션, 테스트 캐시와 가상환경은 포함하지 않습니다.

개인 marketplace는 공식 plugin-creator scaffold로 `~/.agents/plugins/marketplace.json`에 생성했습니다. 이 환경의 CLI는 개인 marketplace의 `./plugins/logo-generator`를 `~/plugins/logo-generator`로 해석했습니다. 소스를 그 위치에 배치한 뒤 다음 명령이 성공했습니다.

```sh
codex plugin add logo-generator@personal --json
```

첫 설치는 `version: 0.2.0`으로 성공했습니다. 마지막 예약 출력 경로 수정 후 공식 cachebuster helper로 버전을 갱신하여 재설치했습니다. 당시 반환 값은 `pluginId: logo-generator@personal`, `version: 0.2.0+codex.20260912125753`, `authPolicy: ON_INSTALL`이었습니다. 당시 설치 캐시는 Orca Codex 계정 홈의 `plugins/cache/personal/logo-generator/0.2.0+codex.20260912125753`이며, 소스 위치는 `<plugin-sources>/logo-generator`였습니다. 당시 플러그인·스킬 검사와 ZIP 무결성 검사도 통과했습니다.

`codex plugin list --json`은 기존의 별도 `astral-codex` marketplace에 지원되는 manifest가 없다는 오류로 실패했습니다. 이 오류는 개인 플러그인 추가 명령의 성공과 별개이며, 관련 없는 marketplace 설정은 변경하지 않았습니다. 전체 목록 조회가 정상이라고 주장하지 않습니다.

이름 변경 전에는 새 Codex 대화에서 `$logo-generator`로 시작하도록 안내했습니다. 당시 세션에서 설치 명령과 파일 검증은 실행했지만, 사용자의 새 GUI 대화에서 스킬 선택까지 대신 실행한 것은 아닙니다. 당시 독립 실행 QA의 패키지 이동·캐시 실행 결과는 [QA 검토](review-qa.md)에 기록합니다.
