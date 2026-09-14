# OFFCUT · Hermes 제작 사례

[English](README.md) · [한국어](README.ko.md) · [Hermes로 만들기](../hermes.ko.md)

[오프라인 예제 페이지](index.html)를 브라우저에서 열면 가상의 가구 스튜디오를 위한 세 방향과 정확한 부모 이미지 기반 수정을 비교하실 수 있습니다. 흰 원본 캔버스, 통과하지 못한 리뷰, 코디네이터의 사례 선택을 그대로 보여 드립니다.

| 방향 | 원본 | 실제 리뷰 지적 |
| --- | --- | --- |
| Useful Remainder | [c1 PNG](originals/c1.png) | 디자인 리뷰가 더 정교한 글자 간격을 요청했습니다. |
| Repair Joint | [c2 PNG](originals/c2.png) | 배경 처리와 과도한 여백 개선을 요청했습니다. |
| Modular Shift | [c3 PNG](originals/c3.png) | 결합 형태, 글자 간격과 작은 음각 틈의 개선을 요청했습니다. |

![OFFCUT Useful Remainder 원본](originals/c1.png)

코디네이터는 **c1**을 사례의 수정 대상으로 선택했습니다. 정확한 자식 [e1 PNG](originals/e1.png)은 FF/FC/UT 간격을 개선했지만, 두 모델 리뷰 모두 보존 대상인 심볼과 글자 사이의 틈이 줄었다고 지적했습니다. 따라서 **수정 필요** 결과로 남아 있습니다.

두 번째 수정은 **e1**을 정확한 부모 이미지로 사용했습니다. [e2 PNG](originals/e2.png)는 개선된 글자 간격을 유지하면서 심볼과 글자 사이의 틈을 복원했고, 두 새 리뷰에서 다섯 항목 모두 통과했습니다. 코디네이터는 **e2**를 선택했으며 네이티브 워크플로는 **revision 47**에서 전달을 마쳤습니다.

![OFFCUT 최종 e2 원본](originals/e2.png)

[검증된 패키지 다운로드](delivery/logo-package.zip) · [브랜드 가이드 읽기](delivery/brand-guide.md) · [내보내기 매니페스트](delivery/manifest.json)

ZIP에는 e2 원본 PNG, 매니페스트와 가이드가 담겨 있습니다. ZIP SHA256: `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04`. 연결된 PNG는 모두 기준 원본과 바이트가 같으며, 페이지를 위해 배경·여백·그림을 편집하지 않았습니다.

[공개용으로 추린 사례 기록](example.json)에는 허용된 브리프, 부모 관계, 정확한 피드백, 모델 정보와 검토 항목만 담았습니다. 리뷰는 별도의 모델 호출 결과이며 사람의 인증이 아닙니다. 이 정적 페이지에서 워크플로를 재개하지는 않습니다.
