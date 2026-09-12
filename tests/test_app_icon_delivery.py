from __future__ import annotations

import os
from hashlib import sha256
from typing import TYPE_CHECKING, Literal, assert_never
from zipfile import ZipFile

import pytest
from PIL import Image

from logo_helper import app_icon_publish
from logo_helper.app_icon_guide import ARTWORK_LIMITATIONS
from logo_helper.app_icon_models import AppIconIntent
from logo_helper.delivery import Manifest
from logo_helper.images import inspect_png
from logo_helper.models import ArtifactId, Brief, ProjectError, Session, SessionId
from logo_helper.storage import Store
from tests.test_color_reports import prepare_color

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


def test_export_manifest_supports_selected_icon_snapshot() -> None:
    # Given: version-two exports retain all existing gates.
    # When: the additive manifest contract is inspected.
    fields = Manifest.model_fields
    # Then: the selected icon intent and artwork limitation are explicit.
    assert "app_icon" in fields
    assert "artwork_limitations" in fields


def _prepare(harness: Harness, *, strict: bool = False) -> Session:
    brief = Brief.model_validate_json(harness.brief.read_bytes())
    _ = harness.brief.write_text(
        brief.model_copy(update={"background": "opaque"}).model_dump_json()
    )
    with Image.new("RGB", (32, 32), (0, 120, 50)) as image:
        image.save(harness.png)
    if strict:
        state = prepare_color(harness)
    else:
        harness.prepare_export()
        state = Store.at(harness.workspace).load(SessionId("demo"))
    intent = AppIconIntent(preset="monogram", subject="Notes", placement="center", text="메모")
    artifact = state.artifacts[0].model_copy(update={"app_icon": intent})
    state = state.model_copy(update={"artifacts": (artifact,)})
    _ = harness.state_path.write_text(state.model_dump_json())
    return state


def test_export_pairs_selected_icon_snapshot_with_exact_zip_bytes(harness: Harness) -> None:
    # Given: the selected parent's intent differs from the newer child and current brief.
    state = _prepare(harness)
    parent = state.artifacts[0]
    newer = AppIconIntent(preset="pictogram", subject="Weather", placement="lower_right")
    child = parent.model_copy(
        update={
            "id": ArtifactId("v2"),
            "path": "artifacts/v2.png",
            "parent_id": parent.id,
            "app_icon": newer,
        }
    )
    _ = (harness.state_path.parent / child.path).write_bytes(harness.png.read_bytes())
    state = state.model_copy(
        update={
            "artifacts": (parent, child),
            "brief": state.brief.model_copy(update={"app_icon": newer, "exact_text": ""}),
        }
    )
    Store.at(harness.workspace).save(state)
    # When: the reviewed parent is exported through the actual CLI.
    _ = harness.ok("export", "--session", "demo", "--revision", str(state.revision))
    folder = harness.workspace / "output/logo-generator/demo"
    manifest = Manifest.model_validate_json((folder / "manifest.json").read_bytes())
    guide = (folder / "brand-guide.md").read_text()
    # Then: the selected immutable intent and platform limits match all ZIP payloads.
    assert manifest.schema_version == 2
    assert manifest.app_icon == parent.app_icon
    assert manifest.source.id == parent.id
    assert manifest.artwork_limitations == ARTWORK_LIMITATIONS
    assert "메모" in guide
    assert "monogram" in guide
    assert "Weather" not in guide
    assert ARTWORK_LIMITATIONS in guide
    assert (folder / "logo.png").read_bytes() == harness.png.read_bytes()
    with ZipFile(folder / "logo-package.zip") as archive:
        assert set(archive.namelist()) == {"logo.png", "manifest.json", "brand-guide.md"}
        assert all(
            archive.read(name) == (folder / name).read_bytes() for name in archive.namelist()
        )


@pytest.mark.parametrize(
    "gate",
    ["selection", "review", "background", "hash", "strict_missing", "strict_forged", "stale"],
)
def test_icon_metadata_never_bypasses_existing_export_gates(
    harness: Harness,
    gate: Literal[
        "selection", "review", "background", "hash", "strict_missing", "strict_forged", "stale"
    ],
) -> None:
    state = _prepare(harness, strict=gate.startswith("strict"))
    artifact = state.artifacts[0]
    source = harness.state_path.parent / artifact.path
    revision = state.revision
    match gate:
        case "selection":
            state = state.model_copy(update={"selected_id": None})
            expected = "not_selected"
        case "review":
            state = state.model_copy(
                update={"artifacts": (artifact.model_copy(update={"review": None}),)}
            )
            expected = "review_required"
        case "background":
            with Image.new("RGBA", (32, 32), (0, 120, 50, 128)) as image:
                image.save(source)
            data = source.read_bytes()
            state = state.model_copy(
                update={
                    "artifacts": (
                        artifact.model_copy(
                            update={"sha256": sha256(data).hexdigest(), "image": inspect_png(data)}
                        ),
                    )
                }
            )
            expected = "background_mismatch"
        case "hash":
            _ = source.write_bytes(b"tampered")
            expected = "hash_mismatch"
        case "strict_missing":
            state = state.model_copy(update={"color_reports": ()})
            expected = "color_review_required"
        case "strict_forged":
            with Image.new("RGB", (32, 32), (255, 0, 0)) as image:
                image.save(source)
            digest = sha256(source.read_bytes()).hexdigest()
            state = state.model_copy(
                update={
                    "artifacts": (artifact.model_copy(update={"sha256": digest}),),
                    "color_reports": tuple(
                        report.model_copy(
                            update={"artifact_sha256": digest, "status": "pass", "reasons": ()}
                        )
                        for report in state.color_reports
                    ),
                }
            )
            expected = "color_mismatch"
        case "stale":
            revision -= 1
            expected = "stale_revision"
        case _:
            assert_never(gate)
    _ = harness.state_path.write_text(state.model_dump_json())
    before = harness.state_path.read_bytes()
    result = harness.run("export", "--session", "demo", "--revision", str(revision))
    assert result.returncode != 0
    assert expected in result.stderr
    assert harness.state_path.read_bytes() == before
    assert not (harness.workspace / "output").exists()


@pytest.mark.parametrize("failure", ["disk", "cancel", "foreign"])
def test_publication_failure_rolls_back_owned_files_and_can_resume(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: Literal["disk", "cancel", "foreign"],
) -> None:
    staging = tmp_path / "staging"
    destination = tmp_path / "published"
    for name in ("images", "prompts"):
        (staging / name).mkdir(parents=True)
        _ = (staging / name / "v1").write_bytes(b"fixture")
    for name in ("manifest.json", "index.html"):
        _ = (staging / name).write_bytes(b"fixture")
    original_link = os.link
    expected = KeyboardInterrupt if failure == "cancel" else OSError

    def interrupt(source: Path, target: Path) -> None:
        if target.name == "index.html":
            if failure == "foreign":
                _ = (destination / "keep").write_bytes(b"foreign")
            if failure == "cancel":
                raise KeyboardInterrupt
            message = "injected publication failure"
            raise OSError(message)
        original_link(source, target)

    monkeypatch.setattr(os, "link", interrupt)
    for _ in range(2):
        with pytest.raises(expected):
            app_icon_publish.publish_gallery(staging, destination)
        assert not (destination / "index.html").exists()
        assert not (destination / "images").exists()
        if failure == "foreign":
            assert (destination / "keep").read_bytes() == b"foreign"
            break
        assert not destination.exists()
    if failure != "foreign":
        monkeypatch.setattr(os, "link", original_link)
        app_icon_publish.publish_gallery(staging, destination)
        assert (destination / "index.html").read_bytes() == b"fixture"


def test_destination_created_after_staging_is_not_overwritten(tmp_path: Path) -> None:
    destination = tmp_path / "published"
    destination.mkdir()
    _ = (destination / "keep").write_bytes(b"foreign")
    with pytest.raises(ProjectError, match="conflict"):
        app_icon_publish.publish_gallery(tmp_path / "staging", destination)
    assert (destination / "keep").read_bytes() == b"foreign"
