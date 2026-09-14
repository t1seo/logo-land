"""Verify saved delivery provenance and bounded ZIP members without extraction."""

from __future__ import annotations

import stat
import zlib
from hashlib import sha256
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, Final
from zipfile import ZIP_DEFLATED, ZIP_STORED, BadZipFile, ZipFile

from pydantic import ValidationError

from .checks import candidate_by_id, review_input, unmet_criteria, verify_critiques
from .gallery_files import GalleryFile
from .helper_models import HelperBrief, HelperManifest
from .models import StudioError
from .store_files import MAX_FILE_BYTES, read_file, safe_path

if TYPE_CHECKING:
    from .models import Candidate, Delivery, Workflow

TEXT_LIMIT: Final = 1024 * 1024


def _read_payload(directory: Path, name: str, limit: int) -> bytes:
    path = safe_path(directory, name)
    if not path.is_file() or path.stat().st_size > limit:
        raise StudioError("gallery_delivery", f"Delivery file missing or too large: {name}")
    data = read_file(path)
    if len(data) > limit:
        raise StudioError("gallery_delivery", f"Delivery file exceeds its bound: {name}")
    return data


def _verify_manifest(manifest: HelperManifest, state: Workflow, candidate: Candidate) -> None:
    source = manifest.source
    if (
        manifest.session_id != state.id
        or manifest.brief != HelperBrief.from_brief(state.brief)
        or manifest.requested_background != state.brief.background
        or source.id != candidate.id
        or source.path != f"artifacts/{candidate.id}.png"
        or source.sha256 != candidate.sha256
        or source.parent_id != candidate.parent_id
        or source.prompt != candidate.prompt
        or source.requested_background != state.brief.background
        or (source.image.width, source.image.height) != (candidate.width, candidate.height)
    ):
        raise StudioError("gallery_delivery", "Delivery manifest differs from this snapshot")
    review = source.review
    if (
        review is None
        or source.reviewed_at is None
        or not all(
            (
                review.text_correct,
                review.composition_ok,
                review.small_size_ok,
                review.preservation_ok,
                review.background_checked,
            )
        )
    ):
        raise StudioError("gallery_delivery", "Delivery manifest lacks its passing review")


def _verify_archive(package: bytes, members: tuple[GalleryFile, ...]) -> None:
    with ZipFile(BytesIO(package)) as archive:
        expected = {item.path.name for item in members}
        if set(archive.namelist()) != expected or len(archive.infolist()) != len(expected):
            raise StudioError("gallery_delivery", "Unexpected or duplicate delivery ZIP members")
        for item in members:
            info = archive.getinfo(item.path.name)
            if (
                info.file_size != len(item.data)
                or info.flag_bits & 1
                or info.compress_type not in {ZIP_STORED, ZIP_DEFLATED}
                or info.is_dir()
                or stat.S_IFMT(info.external_attr >> 16) not in {0, stat.S_IFREG}
            ):
                raise StudioError("gallery_delivery", "Unsupported or oversized delivery member")
            with archive.open(info) as stream:
                actual = stream.read(len(item.data) + 1)
            if actual != item.data:
                raise StudioError("gallery_delivery", "ZIP member differs from saved delivery")


def _verified_files(root: Path, state: Workflow, delivery: Delivery) -> tuple[GalleryFile, ...]:
    if state.phase != "delivered" or state.selected_id != delivery.artifact_id:
        raise StudioError("gallery_delivery", "Delivery is not bound to the selected snapshot")
    candidate = candidate_by_id(state, delivery.artifact_id)
    if delivery.image_sha256 != candidate.sha256:
        raise StudioError("gallery_delivery", "Delivery original differs from selected candidate")
    verify_critiques(review_input(root, state, candidate), candidate.critiques)
    if unmet_criteria(state, candidate):
        raise StudioError("gallery_delivery", "Selected delivery has unmet review criteria")
    directory = safe_path(root, delivery.path)
    if delivery.zip_path != f"{delivery.path}/logo-package.zip":
        raise StudioError("gallery_delivery", "ZIP path differs from its saved delivery folder")
    package = _read_payload(directory, "logo-package.zip", MAX_FILE_BYTES)
    manifest_data = _read_payload(directory, "manifest.json", TEXT_LIMIT)
    png = _read_payload(directory, "logo.png", MAX_FILE_BYTES)
    guide = _read_payload(directory, "brand-guide.md", TEXT_LIMIT)
    if (
        sha256(package).hexdigest() != delivery.zip_sha256
        or sha256(manifest_data).hexdigest() != delivery.manifest_sha256
        or sha256(png).hexdigest() != candidate.sha256
    ):
        raise StudioError("gallery_delivery", "Saved delivery bytes are missing or changed")
    _verify_manifest(HelperManifest.model_validate_json(manifest_data), state, candidate)
    _ = guide.decode("utf-8")
    members = (
        GalleryFile(Path("delivery/logo.png"), png),
        GalleryFile(Path("delivery/manifest.json"), manifest_data),
        GalleryFile(Path("delivery/brand-guide.md"), guide),
    )
    _verify_archive(package, members)
    return (*members, GalleryFile(Path("delivery/logo-package.zip"), package))


def delivery_files(workspace: Path, state: Workflow) -> tuple[GalleryFile, ...]:
    """Return verified copies, or fail before publication if delivery evidence changed."""
    if state.delivery is None:
        if state.phase == "delivered":
            raise StudioError("gallery_delivery", "Delivered snapshot has no saved receipt")
        return ()
    try:
        return _verified_files(workspace.resolve(), state, state.delivery)
    except (
        OSError,
        StudioError,
        ValidationError,
        BadZipFile,
        EOFError,
        UnicodeDecodeError,
        zlib.error,
    ) as error:
        raise StudioError("gallery_delivery", f"Delivery unavailable: {error}") from error
