"""User-facing Logopia CLI; command options are local configuration only."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Annotated, Final, TypeAlias, assert_never

import typer

from .engine import Studio
from .launcher_install import install_profile
from .launcher_output import CommandResult, format_result, fresh_gallery, state_result
from .launcher_process import LaunchError
from .launcher_runner import RunOptions, run_request
from .launcher_state import NoInferenceHost
from .models import StudioError

SOURCE: Final = Path(__file__).resolve().parents[1]
REPO: Final = SOURCE.parents[1]
app: Final = typer.Typer(
    help="Logopia: direct logo production through an explicit Hermes profile.",
    no_args_is_help=True,
    add_completion=False,
    pretty_exceptions_enable=False,
    rich_markup_mode=None,
)
Profile: TypeAlias = Annotated[
    str,
    typer.Option("--profile", help="Existing nondefault Hermes profile, e.g. logopia."),
]
ProfileHome: TypeAlias = Annotated[
    Path | None,
    typer.Option("--profile-home", help="Exact absolute profiles/NAME for custom HERMES_HOME."),
]
Workspace: TypeAlias = Annotated[
    Path | None,
    typer.Option("--workspace", help="Workspace; run must match installed settings."),
]
JsonOutput: TypeAlias = Annotated[
    bool,
    typer.Option("--json", help="Print a small machine-readable command receipt."),
]


def _emit(result: CommandResult, json_output: bool) -> None:
    typer.echo(
        result.model_dump_json() if json_output else format_result(result), err=not result.success
    )
    if not result.success:
        raise typer.Exit(code=1)


@app.command("install")
def install_command(
    profile: Profile,
    workspace: Workspace = None,
    profile_home: ProfileHome = None,
    json_output: JsonOutput = False,
) -> None:
    """Copy, doctor and enable the plugin without any model calls."""
    _emit(
        install_profile(profile, profile_home, workspace or Path.cwd(), SOURCE, REPO), json_output
    )


@app.command("run")
def run_command(
    profile: Profile,
    request: Annotated[
        Path,
        typer.Option("--request", help="Exact StartRequest or ActionRequest JSON, at most 32 KiB."),
    ],
    timeout: Annotated[
        int,
        typer.Option(
            "--timeout",
            min=1,
            max=3600,
            help="Owned Hermes deadline in seconds; grace is 10 seconds.",
        ),
    ] = 1800,
    workspace: Workspace = None,
    profile_home: ProfileHome = None,
    json_output: JsonOutput = False,
) -> None:
    """Submit one validated request and verify its saved result."""
    _emit(run_request(RunOptions(profile, request, profile_home, workspace, timeout)), json_output)


@app.command("show")
def show_command(
    workflow: Annotated[str, typer.Option("--workflow", help="Saved workflow ID.")],
    workspace: Workspace = None,
    json_output: JsonOutput = False,
) -> None:
    """Show validated saved state without starting Hermes."""
    studio = Studio(workspace or Path.cwd(), REPO, NoInferenceHost())
    _emit(state_result(studio.status(workflow)), json_output)


@app.command("gallery")
def gallery_command(
    workflow: Annotated[str, typer.Option("--workflow", help="Saved workflow ID.")],
    workspace: Workspace = None,
    output: Annotated[
        Path | None,
        typer.Option("--output", help="Fresh gallery folder; existing output is preserved."),
    ] = None,
    json_output: JsonOutput = False,
) -> None:
    """Publish a fresh offline comparison page from saved state."""
    root = (workspace or Path.cwd()).resolve(strict=True)
    state = Studio(root, REPO, NoInferenceHost()).status(workflow)
    _emit(state_result(state, gallery=fresh_gallery(root, state, output)), json_output)


def main() -> None:
    try:
        app()
    except (LaunchError, StudioError, OSError) as error:
        match error:
            case LaunchError() | StudioError():
                result = CommandResult(success=False, message=error.detail[:1200], error=error.code)
            case OSError():
                result = CommandResult(
                    success=False, message=str(error)[:1200], error="filesystem_error"
                )
            case _:
                assert_never(error)
        output = result.model_dump_json() if "--json" in sys.argv else format_result(result)
        typer.echo(output, err=True)
        raise SystemExit(1) from error
