"""Shared typed CLI boundaries for session options and structured intent files."""

from pathlib import Path
from typing import Annotated

import typer
from pydantic import TypeAdapter

from logo_helper.models import AppIconIntent, LockupIntent, RegionOfInterest
from logo_helper.storage import Store, read_source

SessionOption = Annotated[str, typer.Option("--session")]
ArtifactOption = Annotated[str, typer.Option("--artifact")]
RevisionOption = Annotated[int, typer.Option("--revision", min=0)]
ParentOption = Annotated[str | None, typer.Option("--parent")]
PaletteOption = Annotated[str | None, typer.Option("--palette")]
LockupOption = Annotated[Path | None, typer.Option("--lockup-file")]
RoiOption = Annotated[Path | None, typer.Option("--roi-file")]
AppIconOption = Annotated[Path | None, typer.Option("--app-icon-file")]


def store_from(ctx: typer.Context) -> Store:
    workspace = ctx.find_root().params.get("workspace")
    return Store.at(TypeAdapter(Path).validate_python(workspace))


def parse_lockup(path: Path | None) -> LockupIntent | None:
    return LockupIntent.model_validate_json(read_source(path)) if path is not None else None


def parse_roi(path: Path | None) -> RegionOfInterest | None:
    return RegionOfInterest.model_validate_json(read_source(path)) if path is not None else None


def parse_app_icon(path: Path | None) -> AppIconIntent | None:
    """An explicit file must contain a complete intent; JSON null cannot clear lineage."""
    return AppIconIntent.model_validate_json(read_source(path)) if path is not None else None
