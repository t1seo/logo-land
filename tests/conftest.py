from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Final

import pytest
from PIL import Image
from pydantic import BaseModel, ConfigDict

SCRIPT: Final = Path(__file__).resolve().parents[1] / "skills/logo-land/scripts/logo_project.py"


class ArtifactView(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    id: str
    parent_id: str | None
    sha256: str
    path: str


class SessionView(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)
    revision: int
    selected_id: str | None = None
    artifacts: tuple[ArtifactView, ...] = ()


@dataclass(frozen=True, slots=True)
class Harness:
    workspace: Path
    brief: Path
    png: Path
    prompt: Path
    review: Path

    def run(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--workspace", str(self.workspace), *args],
            capture_output=True,
            text=True,
            check=False,
            timeout=20,
        )

    def ok(self, *args: str) -> str:
        result = self.run(*args)
        assert result.returncode == 0, result.stderr + result.stdout
        return result.stdout

    def init(self) -> None:
        _ = self.ok("init", "--session", "demo", "--brief", str(self.brief))

    def import_image(self, revision: int = 0, artifact: str = "v1", *extra: str) -> str:
        return self.ok(
            "import",
            "--session",
            "demo",
            "--artifact",
            artifact,
            "--image",
            str(self.png),
            "--prompt-file",
            str(self.prompt),
            "--revision",
            str(revision),
            *extra,
        )

    def prepare_export(self) -> None:
        self.init()
        _ = self.import_image()
        _ = self.ok("select", "--session", "demo", "--artifact", "v1", "--revision", "1")
        _ = self.ok(
            "review",
            "--session",
            "demo",
            "--artifact",
            "v1",
            "--revision",
            "2",
            "--review-file",
            str(self.review),
        )

    @property
    def state_path(self) -> Path:
        return self.workspace / ".logo-generator/sessions/demo/session.json"


@pytest.fixture
def harness(tmp_path: Path) -> Harness:
    workspace = tmp_path / "작업 공간"
    workspace.mkdir()
    brief = tmp_path / "brief.json"
    _ = brief.write_text(
        json.dumps(
            {
                "brand_name": "모로 스튜디오",
                "exact_text": "Morrow Studio",
                "industry": "design",
                "audience": "small businesses",
                "background": "transparent",
                "palette": ["green"],
                "styles": ["minimal"],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    png = tmp_path / "synthetic-fixture.png"
    with Image.new("RGBA", (16, 16), (0, 120, 50, 255)) as image:
        image.putpixel((0, 0), (0, 0, 0, 0))
        image.save(png)
    prompt = tmp_path / "prompt.txt"
    _ = prompt.write_text("Create Morrow Studio in green. Fixture only.", encoding="utf-8")
    review = tmp_path / "review.json"
    _ = review.write_text(
        json.dumps(
            {
                "reviewer": "automated fixture test",
                "notes": "Synthetic test; not image generation QA.",
                "text_correct": True,
                "composition_ok": True,
                "small_size_ok": True,
                "preservation_ok": True,
                "background_checked": True,
            }
        ),
        encoding="utf-8",
    )
    return Harness(workspace, brief, png, prompt, review)
