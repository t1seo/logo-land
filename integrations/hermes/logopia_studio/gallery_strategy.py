"""Render concise strategy excerpts while retaining every escaped source field."""

from __future__ import annotations

import re
from html import escape
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Strategy


def _short(text: str, limit: int = 105) -> str:
    first = re.split(r"(?<=[.!?。])\s+|\n", text.strip(), maxsplit=1)[0]
    if len(first) > limit:
        first = first[:limit].rsplit(" ", maxsplit=1)[0].rstrip(" ,:;") + "…"
    return escape(first)


def strategy_panel(strategy: Strategy | None) -> str:
    if strategy is None:
        return '<p class="muted">아직 저장된 디자인 전략이 없습니다.</p>'
    full = "".join(
        f"<div><dt>{title}</dt><dd>{escape(value)}</dd></div>"
        for title, value in (
            ("포지셔닝", strategy.positioning),
            ("사용자의 필요", strategy.audience_need),
            ("브랜드의 약속", strategy.brand_promise),
            ("구성 원칙", strategy.distinctive_principle),
            ("글자", strategy.typography),
            ("색", strategy.color_roles),
            ("전략의 가정", "\n".join(strategy.assumptions)),
        )
    )
    return "".join(
        (
            '<div class="strategy-grid"><div><p class="eyebrow">POSITIONING</p>',
            f"<h2>{_short(strategy.positioning, 85)}</h2>",
            f"<p>{_short(strategy.brand_promise)}</p></div>",
            '<div class="strategy-notes"><p><span>구성 원칙</span>',
            f"<span>{_short(strategy.distinctive_principle)}</span></p>",
            f"<p><span>색과 글자</span><span>{_short(strategy.color_roles, 65)} · ",
            f"{_short(strategy.typography, 65)}</span></p></div></div>",
            '<details id="strategy-details"><summary>전체 전략과 가정 보기</summary>',
            f"<dl>{full}</dl><p>저장된 디자인 제안이며 시장 조사 결과가 아닙니다.</p></details>",
        )
    )
