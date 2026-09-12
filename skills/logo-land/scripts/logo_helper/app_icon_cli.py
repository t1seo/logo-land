"""Discover icon styles and publish explicitly chosen original artwork."""

from typing import Annotated

import typer
from pydantic import TypeAdapter

from logo_helper.app_icon_gallery import render_app_icon_gallery
from logo_helper.app_icon_presets import APP_ICON_PRESETS, AppIconPresetChoice
from logo_helper.cli_options import SessionOption, store_from
from logo_helper.color_gallery import GalleryResult
from logo_helper.models import ArtifactId, SessionId


def register_app_icon_commands(app: typer.Typer) -> None:
    _ = app.command("icon-presets")(icon_presets_command)
    _ = app.command("icon-gallery")(icon_gallery_command)


def icon_presets_command() -> None:
    """List six styles with conversational defaults, without writing session state."""
    typer.echo(
        TypeAdapter(tuple[AppIconPresetChoice, ...]).dump_json(APP_ICON_PRESETS, indent=2).decode()
    )


def icon_gallery_command(
    ctx: typer.Context,
    session: SessionOption,
    artifacts: Annotated[str, typer.Option("--artifacts")],
    output: Annotated[str, typer.Option("--output")],
) -> None:
    """Publish chosen originals and their exact prompts without approval or state mutation."""
    store = store_from(ctx)
    result = render_app_icon_gallery(
        store,
        store.load(SessionId(session)),
        tuple(ArtifactId(item) for item in artifacts.split(",")),
        output,
    )
    typer.echo(TypeAdapter(GalleryResult).dump_json(result, indent=2).decode("utf-8"))
