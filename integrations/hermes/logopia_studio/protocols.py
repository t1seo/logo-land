"""Finite native host calls; engine reservations happen before each invocation."""

from pathlib import Path
from typing import Protocol

from .models import Critique, GeneratedImage, PlanResult, ReviewInput, StudioBrief


class DesignHost(Protocol):
    """Transport boundary with no Hermes dependency or filesystem lock ownership."""

    def plan(self, brief: StudioBrief) -> PlanResult: ...

    def generate(self, prompt: str, parent: Path | None, background: str) -> GeneratedImage: ...

    def critique(self, request: ReviewInput) -> tuple[Critique, ...]: ...
