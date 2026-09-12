# T3: original-pixel color analysis and reference extraction

Implemented and exercised on 2026-09-12 UTC (2026-09-13 Korea), using Python 3.12, Pillow 12.3.0 and ColorAide 8.12.1. This report covers synthetic fixtures and local CLI execution. It does not claim native image generation or visual brand approval.

## Owned changes and integration contract

Production files under `skills/logo-land/scripts/logo_helper/`:

- `color_analysis.py`: artifact/hash/palette binding, measurements, statuses and contrast evidence.
- `color_sampling.py`: original-coordinate sampling, alpha accounting and evidence limits.
- `color_profiles.py`: in-memory RGB ICC conversion and explicit profile uncertainty.
- `reference_decode.py`: bounded static PNG/JPEG decoding, verification and EXIF orientation.
- `references.py`: reference inspection and deterministic median-cut estimates.

Tests: `tests/test_color_analysis.py`, `tests/test_reference_colors.py`.

Shared types and `color_math.py` initially remained with T1/T2. After T1 completed, the coordinator explicitly transferred `color_models.py` and `tests/test_color_models.py` solely for the eight-color constraint-list bound described below; T3 made that bounded correction and changed only the corresponding `ColorConstraints` line in `contracts.md`. `color_math.py` was not changed. Public APIs were sent to the coordinator before implementation and directly to T4 after the first green integration run.

```python
from logo_helper.color_analysis import analyze_png
from logo_helper.references import inspect_reference, extract_palette

analyze_png(
    data: bytes,
    artifact: Artifact,
    palette: PaletteVersion | None,
    *,
    report_id: ReportId,
    roi: RegionOfInterest | None = None,
    surfaces: tuple[str, ...] = ("#FFFFFF", "#171717"),
    created_at: datetime | None = None,
) -> ColorReport

inspect_reference(
    data: bytes, *, roi: RegionOfInterest | None = None,
) -> ReferenceInspection

extract_palette(
    data: bytes, *, roi: RegionOfInterest | None = None, max_colors: int = 8,
) -> PaletteExtraction
```

`ReferenceInspection` is a frozen strict Pydantic model with actual `format`, original decoded `width`/`height`, and `exif_orientation`. `PaletteExtraction` is frozen and contains `swatches`, `sampling`, `profile_treatment`, `status` (`extracted`/`indeterminate`) and `reasons`. Neither API accepts a path or writes an image. The caller handles source-file/symlink safety and immutable reference copies. Decode/size/ROI/hash/binding errors propagate as `ProjectError`; uncertain profile/core evidence and unavailable ColorAide produce `indeterminate` reports. Palette-less artifacts remain `unverified`.

## Implemented measurement semantics

- Original PNG/JPEG bytes are never rewritten. CRC/format, static frames, end markers, 64 MiB and 40M-pixel bounds are checked before expensive analysis; orientation and ICC conversion affect temporary memory only.
- All coordinates are used for images/ROIs of at most 16,384 pixels. Larger scopes use integer 128-grid pixel centers without interpolation. Axes shorter than 128 use each distinct original coordinate once, avoiding inflated duplicate-pixel evidence.
- Alpha zero is omitted. Alpha 250–255 is core evidence; alpha 1–249 is recorded separately. White is retained in every mode, including palette and grayscale PNG transparency.
- Fewer than 128 core samples or more than 10% partial-alpha visible samples produces `indeterminate`. The 10% boundary itself is accepted.
- T2 `delta_e` explicitly uses Lab D50 and CIEDE2000. Distances are computed on original sampled RGB colors, once per distinct RGB/target combination. Median-cut output is never fed into conformance calculations.
- A restricted palette needs at least 99% of core samples within ΔE00 ≤ 5 of an allowed/selected target. Matched groups at 1% or more count toward the design-color limit; smaller matched groups are retained as `minor_swatches`.
- A lock or required color needs both 32 matching core samples and 0.5% core share. A nonzero but insufficient match count is `indeterminate`; zero matches in otherwise sufficient evidence is `mismatch`. Lock-only constraints do not prohibit arbitrary companion colors. Without strict constraints, palette fit is advisory evidence.
- Target `matching_samples`/`share` count all samples within ΔE00 ≤ 5 of that target; target mean/max distances describe those matching samples, with null distances when there are no matches. Observed color counts use a unique nearest-target assignment, so overlapping tolerance regions do not inflate design-color counts.
- Contrast is explicit WCAG2 foreground/surface guidance. Up to eight most frequent original visible RGB/alpha combinations are composited over the requested surfaces; it never gates status. Stored floats pass T1's finite/range constraints.
- Reference candidates use Pillow `MEDIANCUT`, at most eight colors, ordered by decreasing sample share then HEX. Unsupported profiles produce no invented measured swatches. Assumed sRGB is recorded for untagged inputs.
- ColorAide loads lazily through T2. Pillow's ICC core loads only when an embedded profile needs it. Missing ICC support is reported as unsupported profile evidence.

## Baseline, red and green evidence

Baseline command:

```text
uv run --locked pytest tests/test_boundaries.py -q
24 passed in 0.49s
```

The new reference/analysis test files initially failed collection because their new implementation modules did not exist. After initial reference implementation, the substantive red run had `10 failed, 7 passed`: PNG EXIF access had loaded the image before `verify()`. An isolated runtime toggle confirmed the mechanism:

```text
none fp_closed= False
verify=pass
frames fp_closed= False
verify=pass
exif fp_closed= True
verify= verify must be called directly after open
```

Moving verification before EXIF access made the 17 initial reference cases green. The first integrated analysis/reference/boundary run returned `67 passed in 1.94s`.

A later explicit missing-ICC-support regression test first failed:

```text
test_missing_icc_support_returns_indeterminate
AssertionError: assert 'converted_icc' == 'unsupported'
1 failed in 0.07s
```

After moving the optional ICC-core import into its profile branch and reporting import failure, the same test returned `1 passed in 0.05s`.

Final focused suite after that change:

```text
uv run --locked pytest tests/test_color_analysis.py tests/test_reference_colors.py tests/test_boundaries.py -q
77 passed in 1.25s
```

The coordinator-approved constraint correction had its own baseline/red/green cycle: the original model suite returned `30 passed in 0.04s`; three new nine-unique-color cases then failed with `DID NOT RAISE ProjectError` (`3 failed, 33 passed in 0.09s`); after the correction, `36 passed in 0.04s`. The tests separately accept eight normalized unique colors represented by eighteen raw duplicate entries.

Final expanded integration command after the constraint correction:

```text
uv run --locked pytest tests/test_color_analysis.py tests/test_reference_colors.py tests/test_boundaries.py tests/test_color_models.py tests/test_palette_compatibility.py tests/test_palette_engine.py -q
162 passed in 14.22s
```

Ruff `check`, Ruff `format --check` and basedpyright were run against all six production modules and three test files in the final ownership set. Outputs were `All checks passed!`, `9 files already formatted`, and `0 errors, 0 warnings, 0 notes`. The programming skill's `scripts/python/check-no-excuse-rules.py` returned `no violations in 9 file(s)`; every owned Python module stays below 250 nonblank, noncomment lines.

## Fixture coverage

| Scenario | Observed result |
|---|---|
| 256×256 exact half black/half `#F6F3EC` | Pass, deterministic measurements, 16,384 positions, zero matching-target ΔE |
| 100×100 restricted image, 100 red pixels | Pass at 99% matched |
| Same, 101 or 500 red pixels | Mismatch at 98.99% or 95% matched |
| `#101010` versus black; `#303030` versus black | Correct sides of ΔE00 = 5 without quantizing conformance colors |
| 31 versus 32 required/locked black samples of 6,400 | Indeterminate versus pass |
| 49 versus 50 required/locked black samples of 10,000 | Indeterminate versus pass |
| No required/locked matches with sufficient core | Mismatch |
| 127 versus 128 core samples | Indeterminate versus pass |
| 100 versus 101 partial-alpha samples of 1,000 visible | Pass versus indeterminate |
| Third allowed target at 0.99% versus 1% | Minor group retained versus third observed color and count mismatch |
| Alpha-zero red around opaque white lettering | White remains; hidden red cannot cause mismatch |
| Fully transparent or only alpha 1/249 reference | Explicit insufficient evidence |
| RGB sRGB ICC | Converted ICC treatment |
| Synthetic valid RGB ICC with swapped red/green primaries | Red source values become green analysis values; source bytes unchanged |
| Malformed ICC or embedded Lab ICC | Unsupported / indeterminate |
| Non-sRGB gamma-only PNG versus declared-sRGB PNG | Unsupported versus declared sRGB |
| JPEG EXIF orientation 6 with oriented lower-half ROI | Original 32×16 facts, 16×32 analysis scope, expected blue JPEG estimate `#0000FE` |
| GIF, BMP, WEBP inputs | Rejected as unsupported reference formats |
| Header declaring 40,000,001 pixels or bytes >64 MiB | Rejected before expensive pixel analysis |
| Invalid ROI and mismatched artifact hash | Named errors, no source alteration |
| ColorAide unavailable | Indeterminate report with `color_engine_unavailable` reason and null match fraction |
| Black alpha 128 on white surface | Explicit alpha 128/255 and contrast about 4:1 |
| Red only at selected centers of a black 256×256 image | Exactly red measured samples, proving no resize interpolation |

## Real local CLI and API usage

A disposable workspace was driven through actual subprocesses of `skills/logo-land/scripts/logo_project.py`. These were synthetic fixture files. Each successful command exited 0 with empty stderr:

```text
init --session manual --brief <brief.json>
reference-add --session manual --revision 0 --reference ref --image <original.png>
palette-add --session manual --revision 1 --palette black-ivory --palette-file <palette.json>
import --session manual --revision 2 --artifact pass --image <original.png> --prompt-file <prompt.txt>
color-analyze --session manual --revision 3 --artifact pass
import --session manual --revision 4 --artifact mismatch --image <mismatch.png> --prompt-file <prompt.txt>
```

The palette JSON selected black/ivory with `max_colors=2`. The first source was a 100×100 half-black, half-ivory image. The second replaced 5% of its area with red. Actual persisted report identifiers and metrics:

```json
{
  "pass_report": {
    "id": "report-d144518f2b5e4c93bb73f74655fafbcb",
    "artifact_id": "pass",
    "artifact_sha256": "74acc4b6b048b59a7a69c4d72b936e770a117db5ccd294c8458432c5efd2f6b0",
    "palette_id": "black-ivory",
    "palette_digest": "4041e88d2819e46c37b45d08f4435d5ca2bfef0993c8e005e247ae44577cb735",
    "status": "pass",
    "profile_treatment": "assumed_srgb",
    "matched_fraction": 1.0,
    "unmatched_fraction": 0.0,
    "observed_colors": 2,
    "measured_swatches": [
      {"hex": "#000000", "samples": 5000, "share": 0.5},
      {"hex": "#F6F3EC", "samples": 5000, "share": 0.5}
    ]
  },
  "mismatch_report": {
    "id": "report-1753ca102c8b402a8a8f4f58564751a1",
    "artifact_id": "mismatch",
    "artifact_sha256": "945b097927d1284e95af9eb1d6fca9aee4ce369d446799db3b6cb2f9904cfa63",
    "status": "mismatch",
    "matched_fraction": 0.95,
    "unmatched_fraction": 0.05,
    "observed_colors": 2,
    "reasons": ["Fewer than 99% of sampled core pixels match the target palette"]
  }
}
```

Both reports used 10,000 all-pixel positions, 10,000 core samples, no partial samples, ColorAide 8.12.1 and Pillow 12.3.0. Both matching targets had mean/max ΔE 0. The mismatch report's `observed_colors=2` names matched design groups; its red third color is separately visible in measured swatches and the 5% unmatched fraction, and still fails restricted conformance.

```text
ORIGINAL_BYTES_IDENTICAL True
REFERENCE_BYTES_IDENTICAL True
EXTRACTION status=extracted, #000000 share=0.5, #F6F3EC share=0.5
INVALID_ROI exit=1, invalid_roi: ROI leaves the oriented image, state_unchanged=True
SYMLINK_REFERENCE exit=1, invalid_file: Expected a regular non-symlink file, state_unchanged=True
```

Independent manual performance run with a 4096×4096 RGBA black fixture and a 32-pixel-wide alpha-128 edge:

```json
{"seconds":0.5086171249859035,"dimensions":[4096,4096],"positions":16384,"core":16256,"partial":128,"status":"pass","sha256":"a4f69cc0d82a1c72e36bad42fd6c156d71dee93f32055c7251f6036aa4200845"}
```

A fresh Python subprocess marked both `coloraide` and `PIL._imagingcms` unavailable before importing the helper modules:

```text
FRESH_IMPORT_WITHOUT_COLOR_ENGINES=success
UNTAGGED_EXTRACTION_WITHOUT_COLOR_ENGINES extracted #FFFFFF
```

## Cleanup and remaining integration responsibility

The manual workspace was managed by `TemporaryDirectory`; cleanup output was `TEMP_DIRECTORY_REMOVED True`. Tests use memory or pytest-owned temporary directories; the missing-engine mocks restore automatically. No debugger listeners, instrumentation, synthetic public logo assets, image-editing outputs, commits, or subagents were created. A concurrently present root `.debug-journal.md` belongs to another worker and was not modified.

T3 used the review-work checklist locally and supplied API/test evidence for the coordinator's planned independent reviews. No independent-review pass or native-image result is claimed here. T4/T5 own final CLI/export policy integration, T8 owns native samples and release-wide verification.

The unbounded `allowed_hex` observation was resolved with the coordinator-approved transfer: each `locked_hex`/`allowed_hex`/`required_hex` list now permits at most eight normalized unique colors, with `constraint_conflict` for excess. Empty allowed lists still fail. This bounds conformance work to at most 16,384 original positions and eight targets, while preserving duplicates-before-normalization behavior. T4 was notified directly and the coordinator was asked to relay the correction to T5/documentation owners.

The correction was also exercised through a fresh actual CLI workspace:

```text
NINE_UNIQUE_CLI 1 {"error": "constraint_conflict: Each constraint list supports at most eight unique colors"} state_unchanged True
SIXTEEN_RAW_EIGHT_UNIQUE_CLI 0 stored_colors 8
BOUND_FIXTURE_REMOVED True
```
