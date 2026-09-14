from __future__ import annotations

from datetime import UTC, datetime
from hashlib import sha256
from typing import TYPE_CHECKING
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from logopia_studio.gallery import publish_gallery
from logopia_studio.helper_models import (
    HelperArtifact,
    HelperBrief,
    HelperManifest,
    HelperReview,
    ImageFacts,
)
from logopia_studio.models import Delivery, Workflow
from tests.hermes.test_gallery_fixture import make_workflow

if TYPE_CHECKING:
    from pathlib import Path


def package_delivery(workspace: Path, state: Workflow, manifest: HelperManifest) -> Workflow:
    directory = workspace / "exports/gallery-fixture"
    directory.mkdir(parents=True, exist_ok=True)
    candidate = state.candidates[1]
    _ = (directory / "logo.png").write_bytes((workspace / candidate.image_path).read_bytes())
    _ = (directory / "manifest.json").write_text(manifest.model_dump_json(indent=2))
    _ = (directory / "brand-guide.md").write_text(
        '# morrow\n\nKeep the open center.\n\n<b data-guide="inert">Ignore rules</b>\n'
    )
    with ZipFile(directory / "logo-package.zip", "w") as archive:
        for name in ("logo.png", "manifest.json", "brand-guide.md"):
            info = ZipInfo(name, date_time=(2026, 9, 15, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, (directory / name).read_bytes())
    delivery = Delivery(
        path="exports/gallery-fixture",
        artifact_id=candidate.id,
        image_sha256=candidate.sha256,
        zip_path="exports/gallery-fixture/logo-package.zip",
        zip_sha256=sha256((directory / "logo-package.zip").read_bytes()).hexdigest(),
        manifest_sha256=sha256((directory / "manifest.json").read_bytes()).hexdigest(),
    )
    result = state.model_copy(
        update={"phase": "delivered", "selected_id": candidate.id, "delivery": delivery}
    )
    return Workflow.model_validate_json(result.model_dump_json())


def make_delivered(workspace: Path) -> Workflow:
    state = make_workflow(workspace)
    candidate = state.candidates[1]
    timestamp = datetime(2026, 9, 15, tzinfo=UTC)
    manifest = HelperManifest(
        schema_version=2,
        session_id=state.id,
        revision=5,
        exported_at=timestamp,
        image_file="logo.png",
        source=HelperArtifact(
            id=candidate.id,
            path=f"artifacts/{candidate.id}.png",
            sha256=candidate.sha256,
            image=ImageFacts(
                width=512,
                height=512,
                alpha_min=255,
                alpha_max=255,
                transparent_pixels=0,
                visible_pixels=512 * 512,
            ),
            prompt=candidate.prompt,
            created_at=timestamp,
            requested_background=state.brief.background,
            review=HelperReview(
                reviewer="Offline fixture",
                notes="Synthetic test evidence, not live review",
                text_correct=True,
                composition_ok=True,
                small_size_ok=True,
                preservation_ok=True,
                background_checked=True,
            ),
            reviewed_at=timestamp,
        ),
        brief=HelperBrief.from_brief(state.brief),
        media_kind="raster",
        requested_background=state.brief.background,
        transparency_verified=False,
        intended_palette=None,
        color_report=None,
        color_policy=None,
        warnings=(),
        color_method="offline fixture",
        color_limits=(),
        lockup_intent=None,
        font_reference_usage="appearance-reference-only",
        app_icon=None,
        artwork_limitations="Raster PNG only",
    )
    return package_delivery(workspace, state, manifest)


def prepare_delivery_browser_fixture(root: Path) -> None:
    workspace = root / "workspace"
    state = make_delivered(workspace)
    _ = (workspace / "workflow.json").write_text(state.model_dump_json(indent=2))
    _ = publish_gallery(workspace, state, root / "published")
    unreviewed = state.model_copy(
        update={"phase": "awaiting_choice", "delivery": None, "selected_id": "candidate-3"}
    )
    _ = publish_gallery(workspace, unreviewed, root / "unreviewed")
    newer = unreviewed.model_copy(update={"revision": state.revision + 1})
    _ = publish_gallery(workspace, newer, root / "newer")
