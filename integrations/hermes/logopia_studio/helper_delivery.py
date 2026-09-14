"""Review/select/export through the helper and verify committed package bytes."""

from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING
from zipfile import BadZipFile, ZipFile

from pydantic import ValidationError

from .checks import candidate_by_id, unmet_criteria
from .helper_models import HelperManifest, HelperReview
from .models import Delivery, StudioError
from .store_files import read_file, safe_path

if TYPE_CHECKING:
    from .helper import HelperBridge
    from .models import Job, Workflow


def verified_delivery(bridge: HelperBridge, state: Workflow, output: str) -> Delivery:
    if state.selected_id is None:
        raise StudioError("selection_required", "Select an exact candidate")
    session = bridge.show(state)
    records = tuple(item for item in session.exports if item.path == output)
    if len(records) != 1 or records[0].artifact_id != state.selected_id:
        raise StudioError(
            "outcome_unknown", "No exact helper ExportRecord at the reserved destination"
        )
    candidate = candidate_by_id(state, state.selected_id)
    destination = safe_path(bridge.root, output)
    png = read_file(safe_path(destination, "logo.png"))
    manifest_data = read_file(safe_path(destination, "manifest.json"))
    zip_data = read_file(safe_path(destination, "logo-package.zip"))
    guide_data = read_file(safe_path(destination, "brand-guide.md"))
    try:
        manifest = HelperManifest.model_validate_json(manifest_data)
    except ValidationError as error:
        raise StudioError("invalid_delivery", str(error)) from error
    if (
        manifest.source != bridge.artifact(session, state.selected_id)
        or manifest.source.sha256 != candidate.sha256
        or manifest.session_id != state.id
        or manifest.brief != session.brief
        or manifest.exported_at != records[0].created_at
        or manifest.requested_background != state.brief.background
        or hashlib.sha256(png).hexdigest() != candidate.sha256
    ):
        raise StudioError("invalid_delivery", "Manifest/original differs from the committed export")
    try:
        with ZipFile(safe_path(destination, "logo-package.zip")) as archive:
            names = {"logo.png", "manifest.json", "brand-guide.md"}
            if set(archive.namelist()) != names or len(archive.namelist()) != len(names):
                raise StudioError("invalid_delivery", "Unexpected ZIP payload")
            for name, data in (
                ("logo.png", png),
                ("manifest.json", manifest_data),
                ("brand-guide.md", guide_data),
            ):
                info = archive.getinfo(name)
                if info.file_size != len(data) or archive.read(name) != data:
                    raise StudioError(
                        "invalid_delivery", "ZIP payload differs from published files"
                    )
    except BadZipFile as error:
        raise StudioError("invalid_delivery", str(error)) from error
    return Delivery(
        path=output,
        artifact_id=candidate.id,
        image_sha256=candidate.sha256,
        zip_path=f"{output}/logo-package.zip",
        zip_sha256=hashlib.sha256(zip_data).hexdigest(),
        manifest_sha256=hashlib.sha256(manifest_data).hexdigest(),
    )


def export_job(bridge: HelperBridge, state: Workflow, job: Job) -> Delivery:
    if state.selected_id is None or job.output_path is None:
        raise StudioError("invalid_job", "Delivery lacks selection or reserved output")
    candidate = candidate_by_id(state, state.selected_id)
    unmet = unmet_criteria(state, candidate)
    if unmet:
        raise StudioError("review_required", "; ".join(unmet))
    session = bridge.show(state)
    if any(item.path == job.output_path for item in session.exports):
        return verified_delivery(bridge, state, job.output_path)
    expected_review = HelperReview(
        reviewer="Logopia independent design and production image critiques",
        notes="Both bound roles explicitly passed all required criteria; no human certification.",
        text_correct=True,
        composition_ok=True,
        small_size_ok=True,
        preservation_ok=True,
        background_checked=True,
    )
    artifact = bridge.artifact(session, candidate.id)
    if artifact.review != expected_review:
        path = bridge.request_file(
            state.id, f"{job.id}-review.json", expected_review.model_dump_json()
        )
        session = bridge.invoke(
            "review",
            "--session",
            state.id,
            "--artifact",
            candidate.id,
            "--revision",
            str(session.revision),
            "--review-file",
            str(path),
        )
    if session.selected_id != candidate.id:
        session = bridge.invoke(
            "select",
            "--session",
            state.id,
            "--artifact",
            candidate.id,
            "--revision",
            str(session.revision),
        )
    _ = bridge.invoke(
        "export",
        "--session",
        state.id,
        "--revision",
        str(session.revision),
        "--output",
        job.output_path,
    )
    return verified_delivery(bridge, state, job.output_path)
