"""Portable read-only color-gallery public API."""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass
from html import escape
from pathlib import Path
from string import Template
from tempfile import TemporaryDirectory

from logo_helper.color_gallery_cards import render_palette_cards
from logo_helper.color_gallery_data import intent_markup, lockup_markup, report_markup
from logo_helper.models import Artifact, ArtifactId, ProjectError, Session
from logo_helper.storage import Store, read_source, safe_path, write_new

__all__ = ["GalleryResult", "render_color_gallery", "render_palette_cards"]


@dataclass(frozen=True, slots=True)
class GalleryResult:
    """Workspace-relative published paths and the explicit ordered artifact IDs."""

    path: str
    index_path: str
    artifact_ids: tuple[ArtifactId, ...]


def artifact_card(state: Session, artifact: Artifact) -> str:
    report = next(
        (item for item in reversed(state.color_reports) if item.artifact_id == artifact.id), None
    )
    identifier = escape(artifact.id)
    return (
        f'<article class="artifact-card" id="artifact-{identifier}">'
        f'<div class="card-heading"><h2>{identifier}</h2><span>{artifact.image.width} x '
        f'{artifact.image.height} px</span></div><div class="surface">'
        f'<img src="images/{identifier}.png" alt="{escape(state.brief.brand_name)} · '
        f'{identifier}" width="{artifact.image.width}" height="{artifact.image.height}">'
        '</div><div class="card-body"><p class="provenance">Parent artifact: '
        f"{escape(artifact.parent_id or 'None')} · PNG original bytes</p>"
        f"{intent_markup(state, artifact)}{report_markup(report)}{lockup_markup(artifact)}"
        f'<a class="download" href="images/{identifier}.png" download>Download {identifier}.png'
        "</a></div></article>"
    )


def render_color_gallery(
    store: Store,
    state: Session,
    artifact_ids: tuple[ArtifactId, ...],
    output_relative: str,
) -> GalleryResult:
    """Stage explicit original PNGs and publish exclusively without saving session state."""
    if not artifact_ids or len(set(artifact_ids)) != len(artifact_ids):
        raise ProjectError("invalid_selection", "Choose one or more distinct artifact IDs")
    artifacts = tuple(state.artifact(identifier) for identifier in artifact_ids)
    destination = safe_path(store.root, output_relative)
    relative = destination.relative_to(store.root)
    if relative.parts[0].casefold() in {".logo-generator", ".git"}:
        raise ProjectError("reserved_output", "Gallery cannot occupy reserved project storage")
    if destination.exists():
        raise ProjectError("conflict", "Gallery destination already exists")
    template_path = Path(__file__).resolve().parents[2] / "assets/color-gallery.template.html"
    markup = Template(template_path.read_text(encoding="utf-8")).substitute(
        brand=escape(state.brief.brand_name),
        session=escape(state.id),
        revision=state.revision,
        count=len(artifacts),
        cards="".join(artifact_card(state, artifact) for artifact in artifacts),
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".logo-gallery-", dir=destination.parent) as temporary:
        staging = Path(temporary)
        (staging / "images").mkdir()
        for artifact in artifacts:
            data = read_source(safe_path(store.session_dir(state.id), artifact.path))
            if hashlib.sha256(data).hexdigest() != artifact.sha256:
                raise ProjectError("hash_mismatch", f"Artifact {artifact.id} changed during render")
            write_new(staging / "images" / f"{artifact.id}.png", data)
        write_new(staging / "index.html", markup.encode("utf-8"))
        _ = safe_path(store.root, output_relative)
        _publish_gallery(staging, destination)
    return GalleryResult(relative.as_posix(), f"{relative.as_posix()}/index.html", artifact_ids)


def _publish_gallery(staging: Path, destination: Path) -> None:
    try:
        destination.mkdir()
    except FileExistsError as error:
        raise ProjectError("conflict", "Gallery destination already exists") from error
    published: list[Path] = []
    images = destination / "images"
    images_created = False
    try:
        images.mkdir()
        images_created = True
        for source in (*sorted((staging / "images").iterdir()), staging / "index.html"):
            target = destination / source.relative_to(staging)
            os.link(source, target)
            published.append(target)
    except OSError:
        for path in published:
            path.unlink()
        if images_created:
            images.rmdir()
        destination.rmdir()
        raise
