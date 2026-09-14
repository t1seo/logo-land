"""Render offline downloads from already verified publication payloads."""

from __future__ import annotations

from base64 import b64encode
from html import escape
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .gallery_files import GalleryFile
    from .models import Workflow


def package_panel(state: Workflow, files: tuple[GalleryFile, ...]) -> str:
    if state.delivery is None:
        return ""
    payload = {item.path.name: item.data for item in files if item.path.parent.name == "delivery"}
    package = b64encode(payload["logo-package.zip"]).decode("ascii")
    guide = b64encode(payload["brand-guide.md"]).decode("ascii")
    binding = f"{state.id} · r{state.revision} · {state.delivery.artifact_id}"
    return "".join(
        (
            '<section id="delivery" class="delivery-panel" aria-labelledby="delivery-title">',
            '<div><p class="eyebrow">YOURS TO TAKE</p>',
            '<h2 id="delivery-title">선택한 방향을, 이제 사용할 시간.</h2>',
            '<p class="delivery-description">',
            "선택 원본 PNG와 브랜드 가이드, 출처 기록을 담았습니다.</p>",
            f'<p id="delivery-binding" class="delivery-binding">{escape(binding)}</p></div>',
            '<div class="delivery-actions">',
            '<a id="download-package" class="package-button" ',
            f'href="data:application/zip;base64,{package}" ',
            'download="logo-package.zip">로고 패키지 받기 <span>ZIP ↓</span></a>',
            f'<a id="download-guide" href="data:text/markdown;base64,{guide}" ',
            'download="brand-guide.md">브랜드 가이드 받기 ↗</a>',
            '<span class="delivery-size">원본 · 가이드 · 매니페스트</span></div>',
            '<details class="delivery-record"><summary>전달 파일과 검증 기록 보기</summary>',
            "<p>이 게시본을 만들 때 저장된 파일과 해시를 확인했습니다. ",
            "최신 Hermes 상태는 별도로 확인해 주세요.</p>",
            '<p><a href="delivery/logo.png">선택 원본 열기</a> · ',
            '<a href="delivery/brand-guide.md">가이드 파일 열기</a> · ',
            '<a href="delivery/manifest.json">매니페스트 열기</a> · ',
            '<a href="delivery/logo-package.zip">패키지 파일 열기</a></p>',
            f"<p>패키지 SHA-256 <code>{state.delivery.zip_sha256}</code></p>",
            f"<p>원본 SHA-256 <code>{state.delivery.image_sha256}</code></p></details></section>",
        )
    )
