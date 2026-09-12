from __future__ import annotations

from datetime import UTC, datetime
from hashlib import sha256
from importlib.util import find_spec
from typing import TYPE_CHECKING, Literal, assert_never

import pytest
from PIL import Image

from logo_helper import app_icon_gallery, app_icon_publish
from logo_helper.app_icon_gallery import GalleryManifest, render_app_icon_gallery
from logo_helper.app_icon_models import AppIconIntent
from logo_helper.images import inspect_png
from logo_helper.models import Artifact, ArtifactId, Brief, ProjectError, Session, SessionId
from logo_helper.storage import Store

if TYPE_CHECKING:
    from pathlib import Path

    from tests.conftest import Harness


def test_icon_gallery_has_a_dedicated_public_api() -> None:
    # Given: the color gallery must keep its independent behavior.
    # When: a caller looks up the dedicated icon gallery module.
    specification = find_spec("logo_helper.app_icon_gallery")
    # Then: icon artwork has its own public renderer.
    assert specification is not None


@pytest.fixture
def icon_state(harness: Harness) -> Session:
    with Image.new("RGBA", (96, 64), (150, 185, 170, 255)) as image:
        image.putpixel((0, 0), (10, 25, 90, 80))
        image.putpixel((48, 32), (241, 191, 60, 255))
        image.save(harness.png)
    data = harness.png.read_bytes()
    now = datetime.now(UTC)
    brief = Brief(brand_name="Fixture", exact_text="", industry="test", audience="QA")
    intent = AppIconIntent(preset="ip_mascot", subject="Owl", placement="lower_left")
    first = Artifact(
        id=ArtifactId("v1"),
        path="artifacts/v1.png",
        sha256=sha256(data).hexdigest(),
        image=inspect_png(data),
        prompt='Exact prompt\r\n<script>alert("prompt")</script>\n한글\n',
        created_at=now,
        requested_background="opaque",
        app_icon=intent,
    )
    second = first.model_copy(
        update={
            "id": ArtifactId("v2"),
            "path": "artifacts/v2.png",
            "app_icon": AppIconIntent(
                preset="monogram", subject="Notes", placement="center", text="메모"
            ),
        }
    )
    legacy = first.model_copy(
        update={"id": ArtifactId("v3"), "path": "artifacts/v3.png", "app_icon": None}
    )
    state = Session(
        id=SessionId("demo"),
        created_at=now,
        updated_at=now,
        brief=brief,
        artifacts=(first, second, legacy),
    )
    store = Store.at(harness.workspace)
    folder = store.session_dir(state.id)
    (folder / "artifacts").mkdir(parents=True)
    for artifact in state.artifacts:
        _ = (folder / artifact.path).write_bytes(data)
    store.save(state)
    return state


def test_originals_prompts_and_intent_are_available_without_review(
    harness: Harness,
    icon_state: Session,
) -> None:
    # Given: unreviewed artwork includes non-square dimensions and artistic alpha variance.
    before = harness.state_path.read_bytes()
    ids = (ArtifactId("v2"), ArtifactId("v1"))
    # When: explicit artwork is published in the requested order.
    result = render_app_icon_gallery(Store.at(harness.workspace), icon_state, ids, "icons")
    folder = harness.workspace / result.path
    manifest = GalleryManifest.model_validate_json((folder / "manifest.json").read_bytes())
    # Then: exact bytes, exact UTF-8 prompt and artifact-specific intent remain paired.
    assert result.index_path == "icons/index.html"
    assert tuple(item.artifact_id for item in manifest.artifacts) == ids
    for item in manifest.artifacts:
        artifact = icon_state.artifact(item.artifact_id)
        assert (folder / item.image_file).read_bytes() == harness.png.read_bytes()
        assert (folder / item.prompt_file).read_bytes() == artifact.prompt.encode("utf-8")
        assert item.sha256 == artifact.sha256
        assert item.prompt_sha256 == sha256(artifact.prompt.encode("utf-8")).hexdigest()
        assert (item.width, item.height) == (96, 64)
        assert item.app_icon == artifact.app_icon
    assert harness.state_path.read_bytes() == before
    assert icon_state.selected_id is None
    assert icon_state.artifacts[0].review is None


def test_metadata_is_inert_and_controls_are_portable(harness: Harness, icon_state: Session) -> None:
    # Given: display metadata attempts HTML, attribute and template injection.
    payload = '<img src=x onerror="alert(1)"><script>bad()</script>$cards'
    intent = AppIconIntent(preset="pictogram", subject=payload, placement="center")
    artifact = icon_state.artifacts[0].model_copy(update={"app_icon": intent})
    state = icon_state.model_copy(
        update={
            "artifacts": (artifact,),
            "brief": icon_state.brief.model_copy(update={"brand_name": payload}),
        }
    )
    # When: the page is rendered without embedding prompt content in HTML.
    result = render_app_icon_gallery(Store.at(harness.workspace), state, (artifact.id,), "icons")
    markup = (harness.workspace / result.index_path).read_text()
    # Then: all controls and downloads work locally and untrusted markup is escaped.
    assert "&lt;img src=x" in markup
    assert "&quot;alert(1)&quot;" in markup
    assert all(
        value not in markup
        for value in ("<script", 'onerror="alert', "fetch(", "http://", "https://", artifact.prompt)
    )
    assert all(
        f'id="{value}"' in markup
        for value in (
            "mask-square",
            "mask-rounded",
            "mask-circle",
            "size-32",
            "size-64",
            "size-128",
            "surface-light",
            "surface-dark",
            "preset-all",
            "preset-monogram",
        )
    )
    assert 'type="reset"' in markup
    assert "object-fit: contain" in markup
    assert 'href="images/v1.png"' in markup
    assert 'href="prompts/v1.txt"' in markup
    assert "illustrative" in markup
    assert "viewport" in markup
    assert all(value not in markup for value in ("data-status=", "PASS", "approved", "ranking"))


@pytest.mark.parametrize(
    ("ids", "code"),
    [
        ((), "invalid_selection"),
        (("v1", "v1"), "invalid_selection"),
        (("v3",), "not_app_icon"),
        (("missing",), "not_found"),
    ],
)
def test_invalid_selections_fail_without_publication(
    harness: Harness,
    icon_state: Session,
    ids: tuple[str, ...],
    code: str,
) -> None:
    before = harness.state_path.read_bytes()
    with pytest.raises(ProjectError, match=code):
        _ = render_app_icon_gallery(
            Store.at(harness.workspace),
            icon_state,
            tuple(ArtifactId(item) for item in ids),
            "icons",
        )
    assert not (harness.workspace / "icons").exists()
    assert harness.state_path.read_bytes() == before


@pytest.mark.parametrize(
    "output",
    [
        "",
        ".",
        "../escape",
        "/escape",
        "a/../escape",
        "a\\b",
        "C:x",
        ".git/icons",
        ".LoGo-GeNeRaToR/icons",
    ],
)
def test_reserved_and_escaping_paths_fail(
    harness: Harness, icon_state: Session, output: str
) -> None:
    with pytest.raises(ProjectError, match=r"unsafe_path|reserved_output"):
        _ = render_app_icon_gallery(
            Store.at(harness.workspace), icon_state, (ArtifactId("v1"),), output
        )


@pytest.mark.parametrize(
    "case",
    ["existing", "symlink", "parent_symlink", "missing", "tampered", "source_symlink", "facts"],
)
def test_filesystem_failures_leave_no_partial_gallery(
    harness: Harness,
    icon_state: Session,
    case: Literal[
        "existing", "symlink", "parent_symlink", "missing", "tampered", "source_symlink", "facts"
    ],
    tmp_path: Path,
) -> None:
    output = harness.workspace / "icons"
    source = harness.state_path.parent / "artifacts/v1.png"
    state = icon_state
    match case:
        case "existing":
            output.mkdir()
            _ = (output / "keep").write_text("foreign")
        case "symlink" | "parent_symlink":
            output.symlink_to(tmp_path, target_is_directory=True)
        case "missing":
            source.unlink()
        case "tampered":
            _ = source.write_bytes(b"changed")
        case "source_symlink":
            source.unlink()
            source.symlink_to(harness.png)
        case "facts":
            artifact = state.artifacts[0]
            state = state.model_copy(
                update={
                    "artifacts": (
                        artifact.model_copy(
                            update={"image": artifact.image.model_copy(update={"width": 999})}
                        ),
                    )
                }
            )
        case _:
            assert_never(case)
    with pytest.raises(
        ProjectError, match=r"conflict|unsafe_path|invalid_file|hash_mismatch|invalid_state"
    ):
        _ = render_app_icon_gallery(
            Store.at(harness.workspace),
            state,
            (ArtifactId("v1"),),
            "icons/nested" if case == "parent_symlink" else "icons",
        )
    assert not list(harness.workspace.glob(".app-icon-gallery-*"))
    if case == "existing":
        assert (output / "keep").read_text() == "foreign"
    elif not output.is_symlink():
        assert not output.exists()


def test_concurrent_state_advance_preserves_explicit_snapshot(
    harness: Harness,
    icon_state: Session,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    store = Store.at(harness.workspace)
    newer = icon_state.model_copy(update={"revision": 1, "selected_id": ArtifactId("v2")})
    original = app_icon_publish.publish_gallery

    def advance_before_publish(staging: Path, destination: Path) -> None:
        store.save(newer)
        original(staging, destination)

    monkeypatch.setattr(app_icon_gallery, "publish_gallery", advance_before_publish)
    result = render_app_icon_gallery(store, icon_state, (ArtifactId("v1"),), "icons")
    manifest = GalleryManifest.model_validate_json(
        (harness.workspace / result.path / "manifest.json").read_bytes()
    )
    assert manifest.revision == icon_state.revision
    assert manifest.artifacts[0].artifact_id == ArtifactId("v1")
    assert store.load(icon_state.id) == newer
