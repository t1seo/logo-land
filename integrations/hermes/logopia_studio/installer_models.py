"""Local installation records bind managed files without storing credentials."""

from pathlib import Path
from typing import Annotated, ClassVar

from pydantic import BaseModel, ConfigDict, Field


class InstallSettings(BaseModel):
    """Installed-local paths; the model cannot supply or override these settings."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, strict=True, extra="forbid")
    schema_version: Annotated[int, Field(ge=1, le=1)] = 1
    workspace: Path
    helper_repo: Path


class ManagedFile(BaseModel):
    """Prior bytes must match before a managed file may be replaced."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, strict=True, extra="forbid")
    path: Annotated[str, Field(min_length=1, max_length=500)]
    sha256: Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]


class ManagedInstall(BaseModel):
    """Versioned ownership record used to reject unknown installation content."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, strict=True, extra="forbid")
    schema_version: Annotated[int, Field(ge=1, le=1)] = 1
    files: Annotated[tuple[ManagedFile, ...], Field(min_length=1, max_length=300)]


class InstallReceipt(BaseModel):
    """Payload publication evidence, separate from Hermes enablement or inference."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, strict=True, extra="forbid")
    destination: Path
    file_count: int
