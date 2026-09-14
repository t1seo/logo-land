from __future__ import annotations

import errno
import os
import stat
from hashlib import sha256
from typing import TYPE_CHECKING, Literal, assert_never
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import pytest
from logopia_studio.gallery import publish_gallery
from logopia_studio.helper_models import HelperManifest
from logopia_studio.models import StudioError, Workflow
from tests.hermes.test_gallery_delivery_fixture import make_delivered, package_delivery

if TYPE_CHECKING:
    from pathlib import Path


def refresh_hashes(workspace: Path, state: Workflow) -> Workflow:
    assert state.delivery is not None
    delivery = state.delivery.model_copy(
        update={
            "zip_sha256": sha256((workspace / state.delivery.zip_path).read_bytes()).hexdigest(),
            "manifest_sha256": sha256(
                (workspace / state.delivery.path / "manifest.json").read_bytes()
            ).hexdigest(),
        }
    )
    return state.model_copy(update={"delivery": delivery})


@pytest.mark.parametrize(
    "name", ["logo-package.zip", "manifest.json", "brand-guide.md", "logo.png"]
)
@pytest.mark.parametrize("damage", ["missing", "changed"])
def test_missing_or_changed_delivery_fails_without_publication(
    tmp_path: Path, name: str, damage: Literal["missing", "changed"]
) -> None:
    state = make_delivered(tmp_path)
    assert state.delivery is not None
    path = tmp_path / state.delivery.path / name
    match damage:
        case "missing":
            path.unlink()
        case "changed":
            _ = path.write_bytes(b"changed delivery")
        case _:
            assert_never(damage)
    with pytest.raises(StudioError, match="gallery_delivery"):
        _ = publish_gallery(tmp_path, state, tmp_path / "publication")
    assert not (tmp_path / "publication").exists()


@pytest.mark.parametrize("name", ["logo-package.zip", "manifest.json"])
def test_malformed_delivery_with_matching_saved_digest_is_rejected(
    tmp_path: Path, name: str
) -> None:
    state = make_delivered(tmp_path)
    assert state.delivery is not None
    directory = tmp_path / state.delivery.path
    _ = (directory / name).write_bytes(b"malformed fixture")
    state = refresh_hashes(tmp_path, state)
    with pytest.raises(StudioError, match="gallery_delivery"):
        _ = publish_gallery(tmp_path, state, tmp_path / "publication")


@pytest.mark.parametrize("damage", ["foreign", "prompt", "brief", "review", "selected"])
def test_saved_package_cannot_borrow_foreign_or_stale_identity(
    tmp_path: Path, damage: Literal["foreign", "prompt", "brief", "review", "selected"]
) -> None:
    state = make_delivered(tmp_path)
    assert state.delivery is not None
    manifest = HelperManifest.model_validate_json(
        (tmp_path / state.delivery.path / "manifest.json").read_bytes()
    )
    match damage:
        case "foreign":
            manifest = manifest.model_copy(update={"session_id": "another-workflow"})
        case "prompt":
            source = manifest.source.model_copy(update={"prompt": "Another exact prompt"})
            manifest = manifest.model_copy(update={"source": source})
        case "brief":
            manifest = manifest.model_copy(
                update={"brief": manifest.brief.model_copy(update={"exact_text": "Other name"})}
            )
        case "review":
            selected = state.candidates[1].model_copy(update={"critiques": ()})
            state = state.model_copy(
                update={"candidates": (state.candidates[0], selected, *state.candidates[2:])}
            )
        case "selected":
            state = state.model_copy(update={"selected_id": "candidate-1"})
        case _:
            assert_never(damage)
    if damage != "selected":
        state = package_delivery(tmp_path, state, manifest)
    with pytest.raises(StudioError, match="gallery_delivery"):
        _ = publish_gallery(tmp_path, state, tmp_path / "publication")


@pytest.mark.parametrize("damage", ["extra", "duplicate", "oversize", "unsafe_path", "symlink"])
def test_bounded_package_and_contained_paths(
    tmp_path: Path, damage: Literal["extra", "duplicate", "oversize", "unsafe_path", "symlink"]
) -> None:
    state = make_delivered(tmp_path)
    assert state.delivery is not None
    directory = tmp_path / state.delivery.path
    match damage:
        case "extra":
            with ZipFile(directory / "logo-package.zip", "a", compression=ZIP_DEFLATED) as archive:
                archive.writestr("../foreign.txt", "must never extract")
        case "duplicate":
            with (
                pytest.warns(UserWarning, match="Duplicate name"),
                ZipFile(directory / "logo-package.zip", "a") as archive,
            ):
                archive.writestr("logo.png", (directory / "logo.png").read_bytes())
        case "oversize":
            with (directory / "brand-guide.md").open("wb") as stream:
                _ = stream.truncate(1024 * 1024 + 1)
        case "unsafe_path":
            delivery = state.delivery.model_copy(update={"zip_path": "../foreign.zip"})
            state = state.model_copy(update={"delivery": delivery})
        case "symlink":
            guide = directory / "brand-guide.md"
            guide.unlink()
            guide.symlink_to(directory / "manifest.json")
        case _:
            assert_never(damage)
    if damage in {"extra", "duplicate"}:
        state = refresh_hashes(tmp_path, state)
    with pytest.raises(StudioError, match="gallery_delivery"):
        _ = publish_gallery(tmp_path, state, tmp_path / "publication")
    assert not (tmp_path / "foreign.txt").exists()


@pytest.mark.parametrize("damage", ["no_receipt", "not_delivered"])
def test_delivery_state_cannot_imply_unverified_approval(tmp_path: Path, damage: str) -> None:
    state = make_delivered(tmp_path)
    state = state.model_copy(
        update={"delivery": None} if damage == "no_receipt" else {"phase": "awaiting_choice"}
    )
    with pytest.raises(StudioError, match="gallery_delivery"):
        _ = publish_gallery(tmp_path, state, tmp_path / "publication")


def test_delivered_write_interruption_preserves_foreign_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    state = make_delivered(tmp_path)
    output = tmp_path / "publication"

    def interrupt_delivery(_descriptor: int) -> None:
        if (output / "delivery/logo-package.zip").exists():
            _ = (output / "foreign.txt").write_text("keep this foreign draft")
            raise OSError(errno.ENOSPC, "fixture delivery interruption")

    monkeypatch.setattr(os, "fsync", interrupt_delivery)
    with pytest.raises(StudioError, match="gallery_output"):
        _ = publish_gallery(tmp_path, state, output)
    assert list(output.iterdir()) == [output / "foreign.txt"]
    assert (output / "foreign.txt").read_text() == "keep this foreign draft"
    with pytest.raises(StudioError, match="gallery_output"):
        _ = publish_gallery(tmp_path, state, output)


def test_package_cannot_describe_a_selected_png_as_a_symlink(tmp_path: Path) -> None:
    state = make_delivered(tmp_path)
    assert state.delivery is not None
    directory = tmp_path / state.delivery.path
    with ZipFile(directory / "logo-package.zip", "w") as archive:
        for name in ("logo.png", "manifest.json", "brand-guide.md"):
            info = ZipInfo(name)
            info.create_system = 3
            info.external_attr = (stat.S_IFLNK | 0o777) << 16
            archive.writestr(info, (directory / name).read_bytes())
    state = refresh_hashes(tmp_path, state)
    with pytest.raises(StudioError, match="gallery_delivery"):
        _ = publish_gallery(tmp_path, state, tmp_path / "publication")
