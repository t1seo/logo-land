"""Publish an explicit cross-session comparison through the local CLI."""

from pathlib import Path
from typing import Annotated

import typer

from logo_helper.cli_options import store_from
from logo_helper.comparison_gallery import render_comparison_gallery
from logo_helper.comparison_models import ComparisonSelection
from logo_helper.models import ProjectError
from logo_helper.storage import read_source


def register_comparison_commands(app: typer.Typer) -> None:
    _ = app.command("compare-gallery")(compare_gallery_command)


def compare_gallery_command(
    ctx: typer.Context,
    selection_file: Annotated[Path, typer.Option("--selection-file")],
    output: Annotated[str, typer.Option("--output")],
) -> None:
    """Compare explicit session/revision/artifact PNGs; keep originals and approvals intact."""
    data = read_source(selection_file)
    if len(data) > 4 * 1024 * 1024:
        raise ProjectError("invalid_selection", "Selection JSON exceeds the 4 MiB limit")
    selection = ComparisonSelection.model_validate_json(data)
    result = render_comparison_gallery(store_from(ctx), selection, output)
    typer.echo(result.model_dump_json(indent=2))
