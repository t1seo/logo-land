<p align="center">
  <a href="https://github.com/t1seo/logo-land/releases/tag/v0.3.1"><img src="https://img.shields.io/badge/Release-v0.3.1-191917?style=flat-square&amp;labelColor=f6f3ec" alt="v0.3.1 릴리스"></a>
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/Development-v0.5.0-a64b32?style=flat-square&amp;labelColor=f6f3ec" alt="미출시 개발 버전 0.5.0"></a>
  <img src="https://img.shields.io/badge/Codex-Plugin-191917?style=flat-square&amp;labelColor=f6f3ec" alt="Codex 플러그인">
  <img src="https://img.shields.io/badge/Python-3.12%2B-191917?style=flat-square&amp;labelColor=f6f3ec" alt="Python 3.12 이상">
  <img src="https://img.shields.io/badge/Output-PNG-a64b32?style=flat-square&amp;labelColor=f6f3ec" alt="PNG 출력">
  <a href="docs/README.md"><img src="https://img.shields.io/badge/Docs-English-191917?style=flat-square&amp;labelColor=f6f3ec" alt="English documentation"></a>
  <a href="docs/README.ko.md"><img src="https://img.shields.io/badge/Docs-%ED%95%9C%EA%B5%AD%EC%96%B4-191917?style=flat-square&amp;labelColor=f6f3ec" alt="한국어 문서"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="docs/README.ko.md">문서</a> · <a href="docs/samples/README.ko.md">샘플</a>
</p>

# Logo Land (로고랜드)

<p align="center"><img src="assets/logo-land-studio.png" alt="Logo Land 열린 프레임 심볼과 LOGO LAND 워드마크" width="320"></p>

**Codex와 대화하며 로고와 앱 아이콘 아트워크를 만드실 수 있습니다.**

<a id="시작하기"></a><a id="저장소에서-바로-사용"></a><a id="이미지-생성과-파일-보조-도구의-차이"></a>

## 설치

Codex 내장 이미지 생성·편집 도구, Python 3.12 이상과 uv가 필요합니다. 플러그인 설치만으로 없는 이미지 도구가 활성화되지는 않습니다.

```sh
git clone https://github.com/t1seo/logo-land.git
cd logo-land
uv sync --locked
codex
```

이 저장소의 Codex 대화에서 [skills/logo-land/SKILL.md](skills/logo-land/SKILL.md)를 읽도록 요청한 뒤 아래 예제를 사용해 주세요.

<a id="codex-플러그인으로-설치"></a>

다른 프로젝트에서 `$logo-land`를 사용하시려면 [전체 플러그인 설치 안내](docs/installation.ko.md)를 따라 주세요.

<a id="릴리스와-버전-관리"></a>

현재 저장소는 **v0.5.0 개발 소스**이며, 정식 릴리스는 [v0.3.1](https://github.com/t1seo/logo-land/releases/tag/v0.3.1)입니다.

<a id="대화로-사용하기"></a>

## 이렇게 요청해 보세요

> $logo-land 명상 스튜디오 고요의 차분한 로고 시안 두 개를 만들어 주세요. 단순한 심볼과 정확한 한글 고요를 조합해 주세요.

> $logo-land 독서 앱에 어울리는 IP 캐릭터를 제품과 관련된 세 방향으로 정하고 독립 시안 여섯 개를 만들어 주세요. 색은 알아서 골라 주세요.

> 두 번째 로고를 사용해 주세요. 글자와 형태는 유지하고 주 색상을 남색으로 바꾼 뒤 배경을 투명하게 만들어 주세요.

<a id="앱-아이콘-방향-여섯-가지"></a><a id="네-가지-방식으로-색상-정하기"></a><a id="심볼과-정확한-글자-조합하기"></a><a id="로고-유형-8가지"></a><a id="수정과-전달-파일"></a>

## 만들 수 있는 것

- **로고 유형 8가지:** 워드마크, 레터마크, 모노그램, 심볼, 추상형, 조합형, 엠블럼, 마스코트.
- **앱 아이콘 스타일 6가지:** IP 캐릭터, 픽토그램, 추상형, 모노그램, 소프트 3D, 픽셀 아트.
- **색상과 글자:** 팔레트를 고르고 정확한 브랜드명을 요청하며, 심볼을 글자 옆이나 위에 배치하실 수 있습니다.
- **수정과 재개:** 선택한 이미지를 수정하고 저장한 프로젝트를 이어서 작업하며, 검수한 로고를 PNG·ZIP·간단한 브랜드 안내로 내보내실 수 있습니다.

결과는 래스터 PNG이며 편집 가능한 벡터와 폰트 파일은 포함되지 않습니다. 폰트명은 시각적 참고입니다. 앱 아이콘 아트워크는 별도의 플랫폼별 준비가 필요합니다.

<a id="샘플-10개"></a><a id="투명-배경-로고"></a>

## 샘플

각 분류에서 개별 샘플 페이지의 원본 이미지와 제공되는 파일을 확인하실 수 있습니다.

- [브랜드 로고](docs/samples/README.ko.md) · 로고 유형 8가지로 만든 브랜드 10개
- [색상과 타이포그래피](docs/colors/README.ko.md) · 프로젝트 7개의 사례 8개
- [앱 아이콘](docs/app-icons/README.ko.md) · IP 시안 6개와 원본·수정 방향 비교 5쌍
- [투명 배경 로고](docs/samples/transparency.ko.md) · GROVE PNG 예제와 배경 사용 안내
- [Logo Land 로고](docs/brand/README.ko.md) · 현재 로고와 보존된 이전 로고

<a id="조사와-제작-근거"></a>

## 출처

IP 캐릭터 지침은 [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill)을 바탕으로 각색했습니다. [고정된 원본과 각색 안내](skills/logo-land/references/ip-mascot.md), [MIT 라이선스 고지](skills/logo-land/assets/ip-as-logo.LICENSE), [제3자 출처 고지](THIRD_PARTY_NOTICES.md)를 확인해 주세요.

[문서](docs/README.ko.md) · [변경 이력](CHANGELOG.md) · [도움 요청](https://github.com/t1seo/logo-land/issues)
