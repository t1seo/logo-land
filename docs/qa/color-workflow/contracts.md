# T1 shared contracts

Status: implemented and T1-verified. These names and fields are the downstream contract; changes will be announced. All models are frozen Pydantic v2, strict, extra-forbid. Existing imports from `logo_helper.models` remain valid; new public types are also re-exported there. No module imports ColorAide eagerly.

## Palette (`logo_helper.color_models`)

- `HexColor`: `#RGB` / `#RRGGBB` only, normalized uppercase six-digit. `normalize_hex(value: str) -> str`.
- `ColorConstraints`: `locked_hex: tuple[HexColor,...]=()`, `allowed_hex: tuple[HexColor,...]|None=None`, `max_colors: int|None=None` (1–8), `required_hex: tuple[HexColor,...]=()`, `allow_gradients: bool=False`; normalized duplicates collapse, each locked/allowed/required list permits at most eight unique colors (more raw duplicates are accepted), and excess or contradictory constraints raise `ProjectError('constraint_conflict', ...)`. Empty allowed lists remain invalid. Property `strict: bool` is true for any explicit lock/required/allowed/count constraint.
- `Swatch`: `hex: HexColor`, `role: Text`.
- `SourceEvidence`: `reference_id: ReferenceId|None=None`, `reference_sha256: Digest|None=None`, `provider: Text|None=None`, `tool: Text|None=None`, `response: Text|None=None`, `notes: tuple[Text,...]=()`; reference ID/hash must be paired; provider response is recorded text, never executable.
- `PaletteContent`: `swatches: tuple[Swatch,...]` (1–8 after first-HEX-wins deduplication), `constraints: ColorConstraints=ColorConstraints()`, `source: Literal['assistant','local_harmony','reference','leonardo']`, `source_evidence: SourceEvidence=SourceEvidence()`, `selected_by: Literal['assistant','user']`, `rationale: Text`, `calculation_version: Text='logo-color-v1'`.
- `PaletteVersion(PaletteContent)`: `id: PaletteId`, `parent_palette_id: PaletteId|None=None`, `digest: Digest`.
- `palette_digest(content: PaletteContent) -> str`: SHA256 of sorted-key compact UTF-8 JSON of the normalized PaletteContent fields only (excluding version ID/parent/digest). `PaletteVersion` verifies the supplied digest. Construct content first, then version using its fields plus this digest.

IDs `PaletteId`, `ReferenceId`, `ReportId`, existing `SessionId`/`ArtifactId` are `NewType(str)`; persisted IDs use existing portable lowercase 1–64 character syntax. `ProjectError`, `FrozenModel`, `Text`, `Digest`, `Identifier` live in `model_base` and remain exported from `models`.

## Reference (`logo_helper.reference_models`)

- `RegionOfInterest`: integer `x`, `y` >=0, `width`, `height` >0. Coordinates are after EXIF orientation.
- `Reference`: `id: ReferenceId`, `path: str` (`references/<id>.png` or `.jpg`), `sha256: Digest`, `format: Literal['PNG','JPEG']`, `width: int`, `height: int` (original decoded dimensions), `exif_orientation: int=1` (1–8), `roi: RegionOfInterest|None=None`, `created_at: datetime`. ROI containment uses oriented dimensions.

## Reports (`logo_helper.color_reports`)

- `MeasuredSwatch`: `hex: HexColor`, `samples: int>=0`, `share: float` (0–1).
- `TargetMeasurement`: `hex: HexColor`, `matching_samples: int>=0`, `share: float` (0–1), `mean_delta_e: float|None=None`, `max_delta_e: float|None=None` (finite >=0).
- `ContrastMeasurement`: `foreground: HexColor`, `surface: HexColor`, `ratio: float` (1–21), `alpha: float=1` (0–1).
- `SamplingSettings`: `width`, `height` positive ints, `roi: RegionOfInterest|None=None`, `scope: Literal['full_image','roi']='full_image'`, `coordinate_policy: Literal['all_pixels','grid_128_pixel_centers']='all_pixels'`, `sampled_positions: int` (0–16384), `sampled_fraction: float` (0–1), `visible_samples: int>=0`, `core_samples: int>=0`, `partial_alpha_samples: int>=0`; scope/ROI and count consistency validated.
- `ColorReport`: `id: ReportId`, `artifact_id: ArtifactId`, `artifact_sha256: Digest`, `palette_id: PaletteId|None=None`, `palette_digest: Digest|None=None`, `analysis_policy: Literal['logo-color-v1']='logo-color-v1'`, `color_engine_version: Text`, `pillow_version: Text`, `profile_treatment: Literal['declared_srgb','converted_icc','assumed_srgb','unsupported']`, `sampling: SamplingSettings`, `status: Literal['pass','mismatch','indeterminate','unverified']`, `reasons: tuple[Text,...]=()`, `measured_swatches: tuple[MeasuredSwatch,...]=()`, `targets: tuple[TargetMeasurement,...]=()`, `matched_fraction: float|None=None`, `unmatched_fraction: float|None=None`, `observed_colors: int|None=None`, `minor_swatches: tuple[MeasuredSwatch,...]=()`, `contrasts: tuple[ContrastMeasurement,...]=()`, `delta_e_threshold: float=5`, `created_at: datetime`.
- Reports are evidence records, not authorization to bypass recomputation. Failure statuses require a reason. Palette ID/digest must both be null or both present.

## Lockup (`logo_helper.lockup_models`)

`LockupIntent`: `layout: Literal['horizontal','stacked']`, `symbol_position: Literal['start','end']='start'`, `text_alignment: Literal['start','center','end']='start'`, `typography_style: Text`, `font_reference: Text|None=None`. Font reference records a requested visual direction only. `Brief.lockup` and `Artifact.lockup` are optional, default null. Exact brand/slogan fields are unchanged. T4 owns inheritance/CLI/prompt behavior.

## State and storage

`Session.schema_version=2`; adds `palettes: tuple[PaletteVersion,...]=()`, `active_palette_id: PaletteId|None=None`, `references: tuple[Reference,...]=()`, `color_reports: tuple[ColorReport,...]=()`. `Artifact.palette_id: PaletteId|None=None`; old artifacts preserve null. `Session.palette(id)`, `.reference(id)` and `.color_report(id)` resolve or raise `not_found`. Session validation checks IDs, ordered palette ancestry, active/artifact palette bindings, reference evidence, report artifact/hash/palette/digest bindings, and managed reference paths.

`legacy_state.LegacyBrief/LegacyArtifact/LegacySession` freeze schema 1. `legacy_state.parse_session(data: str|bytes) -> Session` strictly dispatches schema 1/2, converts schema 1 in memory, and rejects unsupported versions/unknown fields. Store public signatures remain unchanged. Existing artifact provenance (including palette/lockup bindings) is immutable; only review/reviewed_at may change. `Store.load/list_sessions/expect` never rewrite JSON. `Store.save` validates the new state and append-only palettes/references/reports, verifies/reuses an exact `session.v1.backup.json`, and atomically writes v2. A failed save can leave the verified backup for retry but leaves v1 state bytes unchanged; it never overwrites a backup. Existing mutations already hold the cooperative lock.
