from __future__ import annotations

import json
from typing import TYPE_CHECKING

from PIL import Image, ImageDraw

from logo_helper import workflow
from logo_helper.app_icon_models import AppIconIntent
from logo_helper.models import ArtifactId, Brief, SessionId
from logo_helper.storage import Store

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


def prepare_sources(harness: Harness) -> Path:
    store = Store.at(harness.workspace)
    for identifier, dimensions, color in (
        ("brand", (120, 48), "#f6f1e6"),
        ("icon", (96, 96), "#30352f"),
    ):
        with Image.new("RGBA", dimensions, color) as image:
            draw = ImageDraw.Draw(image)
            draw.rectangle((12, 12, 36, 36), fill="#b85840")
            draw.ellipse((44, 12, 68, 36), fill="#e2af66")
            image.save(harness.png)
        intent = (
            AppIconIntent(preset="pictogram", subject="Open book", placement="center")
            if identifier == "icon"
            else None
        )
        _ = workflow.create(
            store,
            SessionId(identifier),
            Brief(brand_name=identifier, exact_text="", industry="books", audience="readers"),
        )
        _ = workflow.import_image(
            store,
            SessionId(identifier),
            0,
            artifact_id=ArtifactId("v1"),
            image=harness.png,
            prompt=f"Exact {identifier} prompt\r\nKeep book shape. 한글\n",
            app_icon=intent,
            parent_id=None,
        )
    selection = harness.workspace / "selection.json"
    _ = selection.write_text(
        json.dumps(
            {
                "title": "Reading directions",
                "items": [
                    {"session": "brand", "revision": 1, "artifact": "v1"},
                    {"session": "icon", "revision": 1, "artifact": "v1"},
                ],
            }
        ),
        encoding="utf-8",
    )
    return selection


def source_bytes(workspace: Path) -> dict[str, bytes]:
    root = workspace / ".logo-generator"
    return {
        str(path.relative_to(root)): path.read_bytes() for path in root.rglob("*") if path.is_file()
    }
