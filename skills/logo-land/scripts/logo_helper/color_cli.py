"""Additive flat color commands using the same session and error boundaries."""

from pathlib import Path
from typing import Annotated

import typer
from pydantic import TypeAdapter

from logo_helper import color_workflow
from logo_helper.cli_options import (
    ArtifactOption,
    RevisionOption,
    RoiOption,
    SessionOption,
    parse_roi,
    store_from,
)
from logo_helper.color_gallery import GalleryResult, render_color_gallery
from logo_helper.models import ArtifactId, PaletteContent, PaletteId, ReferenceId, SessionId
from logo_helper.palette_proposals import propose
from logo_helper.storage import read_source


def reference_add(
    ctx: typer.Context,
    session: SessionOption,
    revision: RevisionOption,
    reference: Annotated[str, typer.Option("--reference")],
    image: Annotated[Path, typer.Option("--image")],
    roi_file: RoiOption = None,
) -> None:
    """Copy a static PNG/JPEG and record immutable reference provenance."""
    state = color_workflow.add_reference(
        store_from(ctx),
        SessionId(session),
        revision,
        reference_id=ReferenceId(reference),
        image=image,
        roi=parse_roi(roi_file),
    )
    typer.echo(state.model_dump_json(indent=2))


def palette_propose(
    ctx: typer.Context,
    session: SessionOption,
    request_file: Annotated[Path, typer.Option("--request-file")],
    reference: Annotated[str | None, typer.Option("--reference")] = None,
) -> None:
    """Return validated palette candidates and revision without saving state."""
    store = store_from(ctx)
    result = propose(
        store,
        store.load(SessionId(session)),
        read_source(request_file),
        ReferenceId(reference) if reference is not None else None,
    )
    typer.echo(result.model_dump_json(indent=2))


def palette_add(
    ctx: typer.Context,
    session: SessionOption,
    revision: RevisionOption,
    palette: Annotated[str, typer.Option("--palette")],
    palette_file: Annotated[Path, typer.Option("--palette-file")],
    parent_palette: Annotated[str | None, typer.Option("--parent-palette")] = None,
) -> None:
    """Append one selected PaletteContent JSON and make it active for new logos."""
    state = color_workflow.add_palette(
        store_from(ctx),
        SessionId(session),
        revision,
        palette_id=PaletteId(palette),
        content=PaletteContent.model_validate_json(read_source(palette_file)),
        parent_palette_id=PaletteId(parent_palette) if parent_palette is not None else None,
    )
    typer.echo(state.model_dump_json(indent=2))


def color_analyze(
    ctx: typer.Context,
    session: SessionOption,
    artifact: ArtifactOption,
    revision: RevisionOption,
    roi_file: RoiOption = None,
) -> None:
    """Append a fresh measurement from verified original PNG bytes."""
    state = color_workflow.analyze_artifact(
        store_from(ctx),
        SessionId(session),
        revision,
        artifact_id=ArtifactId(artifact),
        roi=parse_roi(roi_file),
    )
    typer.echo(state.model_dump_json(indent=2))


def color_gallery(
    ctx: typer.Context,
    session: SessionOption,
    artifacts: Annotated[str, typer.Option("--artifacts", help="Comma-separated artifact IDs.")],
    output: Annotated[str, typer.Option("--output")],
) -> None:
    """Publish a portable gallery of explicitly listed logos without changing state."""
    store = store_from(ctx)
    result = render_color_gallery(
        store,
        store.load(SessionId(session)),
        tuple(ArtifactId(item.strip()) for item in artifacts.split(",")),
        output,
    )
    typer.echo(TypeAdapter(GalleryResult).dump_json(result, indent=2).decode("utf-8"))


def register_color_commands(app: typer.Typer) -> None:
    _ = app.command("reference-add")(reference_add)
    _ = app.command("palette-propose")(palette_propose)
    _ = app.command("palette-add")(palette_add)
    _ = app.command("color-analyze")(color_analyze)
    _ = app.command("color-gallery")(color_gallery)
