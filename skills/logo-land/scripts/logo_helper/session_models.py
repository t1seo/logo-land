"""Version-two session graph with immutable color/reference evidence bindings."""

from datetime import datetime
from typing import Annotated, Literal, Self

from pydantic import BeforeValidator, Field, model_validator

from logo_helper.artifact_models import Artifact, ExportRecord, FailedAttempt
from logo_helper.brief_models import Brief
from logo_helper.color_models import PaletteVersion
from logo_helper.color_reports import ColorReport
from logo_helper.model_base import (
    ArtifactId,
    FrozenModel,
    PaletteId,
    ProjectError,
    ReferenceId,
    ReportId,
    SessionId,
    schema_integer,
)
from logo_helper.reference_models import Reference


class Session(FrozenModel):
    """Persisted ordered provenance graph; legacy sessions migrate only in memory."""

    schema_version: Annotated[Literal[2], BeforeValidator(schema_integer)] = 2
    id: Annotated[SessionId, Field(pattern=r"^[a-z0-9][a-z0-9_-]{0,63}$")]
    revision: Annotated[int, Field(ge=0)] = 0
    created_at: datetime
    updated_at: datetime
    brief: Brief
    artifacts: tuple[Artifact, ...] = ()
    selected_id: ArtifactId | None = None
    failures: tuple[FailedAttempt, ...] = ()
    exports: tuple[ExportRecord, ...] = ()
    palettes: tuple[PaletteVersion, ...] = ()
    active_palette_id: PaletteId | None = None
    references: tuple[Reference, ...] = ()
    color_reports: tuple[ColorReport, ...] = ()

    @model_validator(mode="after")
    def consistent_lineage(self) -> Self:
        """Reject tampered paths, duplicate IDs, missing parents, and cycles on resume."""
        seen: set[ArtifactId] = set()
        for artifact in self.artifacts:
            if artifact.id in seen or (
                artifact.parent_id is not None and artifact.parent_id not in seen
            ):
                raise ProjectError(
                    "invalid_state", "Duplicate artifact ID or invalid parent lineage"
                )
            if artifact.path != f"artifacts/{artifact.id}.png":
                raise ProjectError("unsafe_path", "Artifact path does not match its immutable ID")
            seen.add(artifact.id)
        if self.selected_id is not None and self.selected_id not in seen:
            raise ProjectError("invalid_state", "Selected artifact does not exist")
        if any(item.parent_id is not None and item.parent_id not in seen for item in self.failures):
            raise ProjectError("invalid_state", "Failed attempt parent does not exist")
        if any(item.artifact_id not in seen for item in self.exports):
            raise ProjectError("invalid_state", "Export artifact does not exist")
        return self

    @model_validator(mode="after")
    def consistent_color_graph(self) -> Self:
        references = {item.id: item for item in self.references}
        if len(references) != len(self.references):
            raise ProjectError("invalid_state", "Duplicate reference ID")
        seen: set[PaletteId] = set()
        for palette in self.palettes:
            if palette.id in seen or (
                palette.parent_palette_id is not None and palette.parent_palette_id not in seen
            ):
                raise ProjectError(
                    "invalid_state", "Duplicate palette ID or invalid parent lineage"
                )
            evidence = palette.source_evidence
            if evidence.reference_id is not None:
                reference = references.get(evidence.reference_id)
                if reference is None or reference.sha256 != evidence.reference_sha256:
                    raise ProjectError("invalid_state", "Palette reference evidence does not match")
            seen.add(palette.id)
        if self.active_palette_id is not None and self.active_palette_id not in seen:
            raise ProjectError("invalid_state", "Active palette does not exist")
        if any(
            item.palette_id is not None and item.palette_id not in seen for item in self.artifacts
        ):
            raise ProjectError("invalid_state", "Artifact palette does not exist")
        return self

    @model_validator(mode="after")
    def consistent_reports(self) -> Self:
        reports: set[ReportId] = set()
        artifacts = {item.id: item for item in self.artifacts}
        palettes = {item.id: item for item in self.palettes}
        for report in self.color_reports:
            if report.id in reports:
                raise ProjectError("invalid_state", "Duplicate report ID")
            artifact = artifacts.get(report.artifact_id)
            if artifact is None or artifact.sha256 != report.artifact_sha256:
                raise ProjectError("invalid_state", "Report artifact hash does not match")
            if artifact.palette_id != report.palette_id:
                raise ProjectError("invalid_state", "Report palette differs from artifact intent")
            if report.palette_id is not None:
                palette = palettes.get(report.palette_id)
                if palette is None or palette.digest != report.palette_digest:
                    raise ProjectError("invalid_state", "Report palette digest does not match")
            reports.add(report.id)
        return self

    def artifact(self, identifier: ArtifactId) -> Artifact:
        """Resolve an explicit image rather than selecting the latest implicitly."""
        for artifact in self.artifacts:
            if artifact.id == identifier:
                return artifact
        raise ProjectError("not_found", f"Artifact {identifier!r} does not exist")

    def palette(self, identifier: PaletteId) -> PaletteVersion:
        for palette in self.palettes:
            if palette.id == identifier:
                return palette
        raise ProjectError("not_found", f"Palette {identifier!r} does not exist")

    def reference(self, identifier: ReferenceId) -> Reference:
        for reference in self.references:
            if reference.id == identifier:
                return reference
        raise ProjectError("not_found", f"Reference {identifier!r} does not exist")

    def color_report(self, identifier: ReportId) -> ColorReport:
        for report in self.color_reports:
            if report.id == identifier:
                return report
        raise ProjectError("not_found", f"Report {identifier!r} does not exist")
