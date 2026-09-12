# 실제 Codex 이미지 생성·수정 QA

2026-09-12, 가상 브랜드 Morrow Studio로 내장 `image_gen` 도구를 실제 호출했습니다. 아래는 합성 테스트 fixture가 아니라 반환된 실제 PNG입니다. 테스트 담당자가 A안을 선정했으며 사용자 브랜드 승인으로 해석하지 않습니다.

| 단계 | 실제 결과 | 증거 |
|---|---|---|
| A 생성 | 기하학 M + Morrow Studio 조합형, 1254×1254 | [A-v1](images/a-v1.png), [실제 프롬프트](prompts/a-v1.txt) |
| B 생성 | 잎 모티프 + 세리프 문구의 별도 시안, 1254×1254 | [B-v1](images/b-v1.png), [실제 프롬프트](prompts/b-v1.txt) |
| 비교·선택 | 세션에 a-v1, b-v1을 별도로 가져온 뒤 a-v1 선택 | [선택 결과](select-a.json) |
| 부모 참조 수정 | 실제 a-v1 PNG를 `referenced_image_paths`로 전달. 남색·불투명 흰 배경으로 수정 | [A-v2](images/a-v2.png), [최종 편집 프롬프트](prompts/a-v2.txt), [가져오기](import-a2.json) |
| 불완전 검수 차단 | 시각 검토를 등록하지 않은 export가 종료 코드 1, `review_required` 반환 | 아래 실행 기록 |
| 투명도 확인 | A/B 원본에는 투명 영역이 존재했고 A-v2는 전체 alpha=255 | 아래 실제 디코딩 표 |

## 실제 파일 검사

| ID | 크기 | alpha 최소/최대 | 투명 픽셀 수 | 보이는 픽셀 수 |
|---|---|---|---|---|
| a-v1 | 1254×1254 | 0 / 255 | 1,569,371 | 251,254 |
| b-v1 | 1254×1254 | 0 / 255 | 1,571,270 | 200,929 |
| a-v2 | 1254×1254 | 255 / 255 | 0 | 1,572,516 |

투명 픽셀은 alpha<255, 보이는 픽셀은 alpha>0으로 정의해 반투명 픽셀은 양쪽 수에 포함됩니다. 첫 두 이미지가 흰 배경 요청을 충족하지 못한 실제 사례를 바탕으로, 양방향 배경 불일치 차단 회귀 검사를 추가했습니다.

```text
init morrow-live → revision 0
import a-v1 → revision 1
import b-v1 → revision 2
select a-v1 → revision 3
export --revision 3 → exit 1 / review_required (상태 보존)
import a-v2 --parent a-v1 → revision 4
```

실제 생성 결과의 원본 파일을 확인해 저장소에 복사했습니다. 공용 생성 폴더에서 가장 최근 파일을 추측해 선택하지 않았습니다. 프롬프트 작성과 세션 관리는 helper, 그림 생성·수정은 내장 이미지 도구가 수행했습니다. 이미지 픽셀을 Python이나 다른 렌더러로 수정하지 않았습니다.

## 시각적 한계

A-v2에서 브랜드명 표기와 M의 전체 구조, 위 심볼·아래 문구 배치는 유지됐습니다. 오른쪽 내부 곡률과 미세 색조는 원본과 다릅니다. 요청한 HEX와 모든 픽셀이 일치하는 벡터 출력이나 픽셀 단위 보존을 주장하지 않습니다. 작은 파비콘에는 조합형 전체를 축소하기보다 별도 심볼 변형이 필요합니다.

[브라우저 비교 화면](preview.html)은 원본 PNG를 CSS로 표시합니다. 최종 내보내기 및 독립 검토 기록은 검수 후 아래에 추가합니다.

## 최종 검수·내보내기·재개

Chrome을 Codex Computer Use로 조작해 [비교 페이지의 실제 화면](chrome-visual-qa.jpeg)을 확인했습니다. 256px의 심볼·문구 가독성은 통과했고 48px의 한계를 명시했습니다. 검수 내용을 [review-a2.json](review-a2.json)에 작성한 뒤 최종 선택·검토·내보내기를 진행했습니다.

```text
select a-v2 --revision 4 → revision 5
review a-v2 --revision 5 → revision 6
export --revision 6 → revision 7
별도 프로세스 show morrow-live → revision 7, a-v2 선택, 모든 원본 해시 재확인
```

[최종 PNG](delivery/logo.png), [ZIP](delivery/logo-package.zip), [브랜드 안내](delivery/brand-guide.md), [manifest](delivery/manifest.json)를 생성했습니다. 최종 PNG는 1254×1254, 완전 불투명입니다. [내보내기 응답](export-final.json)과 [별도 프로세스 재개](resume-final.json)를 보존했습니다. 수정 전 A/B와 수정본 A-v2는 모두 원래 바이트로 남아 있습니다.

`unzip -t`로 최종 ZIP의 세 항목 무결성을 확인했습니다. 생성 PNG·세션 사본·전달 PNG의 SHA-256은 모두 `666eb20feaf67ee3bc4a1c879f5c551a55998bf2b257d5e52c0b142e599ab519`로 일치했습니다.
