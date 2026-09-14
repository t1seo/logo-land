"""Installed-local settings are parsed only when a native tool is invoked."""

from pathlib import Path
from typing import Self

from pydantic import ValidationError, model_validator

from .models import StudioError
from .models_base import FrozenModel, SchemaVersion


class HostSettings(FrozenModel):
    """The coordinator installs the two trusted roots outside model arguments."""

    schema_version: SchemaVersion
    workspace: Path
    helper_repo: Path

    @model_validator(mode="after")
    def absolute_roots(self) -> Self:
        if not self.workspace.is_absolute() or not self.helper_repo.is_absolute():
            raise StudioError(
                "invalid_settings", "workspace and helper_repo must be absolute paths"
            )
        if not self.workspace.is_dir() or not self.helper_repo.is_dir():
            raise StudioError("invalid_settings", "Configured workspace/helper_repo must exist")
        return self


def load_settings(plugin_root: Path) -> HostSettings:
    path = plugin_root / "settings.json"
    try:
        if path.stat().st_size > 32 * 1024:
            raise StudioError("invalid_settings", "settings.json exceeds 32 KiB")
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise StudioError(
            "not_configured",
            "Install this plugin into an explicit Hermes profile with settings.json",
        ) from exc
    except (OSError, UnicodeError) as exc:
        raise StudioError(
            "invalid_settings", f"Cannot read installed settings.json: {exc}"
        ) from exc
    try:
        return HostSettings.model_validate_json(raw)
    except ValidationError as exc:
        raise StudioError("invalid_settings", str(exc)) from exc
