"""Display review state using the core's original/parent/view evidence checks."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .checks import review_input, unmet_criteria, verify_critiques
from .models import StudioError

if TYPE_CHECKING:
    from pathlib import Path

    from .models import Candidate, Workflow


def _review_label(workspace: Path, state: Workflow, candidate: Candidate) -> str:
    if not candidate.critiques:
        return "생성됨 · 미검토"
    if {item.role for item in candidate.critiques} != {"design", "production"}:
        return "검토 중 · 기록 일부만 있음"
    try:
        verify_critiques(review_input(workspace, state, candidate), candidate.critiques)
    except StudioError:
        return "검토 조건 불일치 · 다시 검토 필요"
    if unmet_criteria(state, candidate):
        if any(
            item.status == "needs_revision"
            for report in candidate.critiques
            for item in report.criteria
        ):
            return "검토됨 · 수정 필요"
        return "검토됨 · 확인할 항목 있음"
    return f"검토됨 · {state.brief.display_width}px 조건 통과"


def review_labels(workspace: Path, state: Workflow) -> tuple[str, ...]:
    root = workspace.resolve()
    return tuple(_review_label(root, state, candidate) for candidate in state.candidates)
