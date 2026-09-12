# T7 portable color and lockup gallery

Implemented in the shared checkout on 2026-09-13 KST. T7 owns only the template, gallery renderer/projection modules, gallery test file and this report. No shared model, plan, Boulder state, ledger, existing sample gallery, commit or remote was changed by this worker. No subagents or native image-generation calls were used.

## Public API delivered to T4

```python
from logo_helper.color_gallery import GalleryResult, render_color_gallery, render_palette_cards

render_color_gallery(
    store: Store,
    state: Session,
    artifact_ids: tuple[ArtifactId, ...],
    output_relative: str,
) -> GalleryResult

render_palette_cards(candidates: tuple[PaletteContent, ...]) -> str
```

`GalleryResult` is a frozen, slotted dataclass with `path: str`, `index_path: str`, and `artifact_ids: tuple[ArtifactId, ...]`. Both paths are relative to the workspace. `ProjectError` remains the shared domain error. The result directory contains only `index.html` and `images/<explicit-artifact-id>.png`.

`color_gallery.py` owns staged publication; `color_gallery_cards.py` owns reusable escaped palette cards; `color_gallery_data.py` owns public intent/report/lockup projection. Shared Pydantic models are consumed unchanged. The template is resolved relative to the installed skill, not the checkout root.

## Result behavior

- Ivory/black layout follows the existing samples and transparency pages. Responsive cards show parent artifact/palette IDs, palette source, selection provenance, roles, HEX, rationale, intended versus measured swatches, stored report status/date, scope/ROI, sample counts/fraction, ΔE target mean/max/threshold, profile/policy and escaped reasons.
- Legacy artifacts retain unknown intent. Missing reports and reports with no bound palette render `unverified`, even when an unbound stored report contains `pass`. Bound advisory and strict statuses remain explicit stored snapshots, never export authorization or fresh verification.
- Requested lockup layout, symbol position, alignment, typography direction and font reference are plain text. The page explicitly states that these do not prove a font file was used. Computed gallery typography is `system-ui, sans-serif`; no fonts are downloaded or bundled.
- Light, dark and transparency surfaces and large/128px preview sizes use native radio controls and CSS only. Candidate cards expose a separate native radio group that makes no state writes.
- No full artifact prompt, provider response, source absolute path or unselected reference asset is serialized. All visible strings are HTML escaped. There is no JavaScript, remote asset, font dependency or external link; CSP also blocks scripts and external resources.
- Explicit IDs are required and duplicates/empty selections are rejected. Source hashes are checked again during copying. Existing output directories, reserved `.logo-generator`/`.git` destinations, escaping paths and symlink components are rejected. Exclusive publication never overwrites files; staging and partially published files are cleaned after failure.

## Test evidence

1. Existing pytest baseline began while T1 was publishing its models: the first full collection reported missing new exports/modules. A legacy-only run then recorded 82 passed/14 failed because its already-imported schema-1 model differed from schema-2 subprocess output. These failures were outside T7, and their files were not edited.
2. Candidate-card red: `render_palette_cards` did not exist; after adding it, its escaping/private-evidence/read-only test passed.
3. Gallery red: importing the absent `render_color_gallery` API failed as expected. The implementation initially produced 23 passed/2 failed; the two failing assertions accidentally matched the CSS pass selector rather than a report element. Narrowing those assertions to `<section data-status=...>` yielded 25 passed.
4. Final review added a real red regression for a stored `pass` with no bound palette: the renderer incorrectly displayed `pass`. The minimal projection fix changed that case to `unverified`; all 26 gallery tests passed.
5. A later 96-test legacy regression run recorded 90 passed/6 failures when T4 changed `PromptResult` during execution. A fresh run of both affected background modules plus gallery tests passed all 42 tests, confirming those six failures were transient shared-checkout model timing. Final integration across all workers remains coordinator-owned.

Commands executed:

```sh
uv run --locked pytest -q tests/test_color_gallery.py
uv run --locked pytest -q tests/test_background_variants.py tests/test_background_compatibility.py tests/test_color_gallery.py
uv run ruff check skills/logo-land/scripts/logo_helper/color_gallery*.py tests/test_color_gallery.py
uv run basedpyright skills/logo-land/scripts/logo_helper/color_gallery*.py tests/test_color_gallery.py
```

Final gallery suite: **26 passed**. Ruff: **all checks passed**. Basedpyright: **0 errors, 0 warnings, 0 notes**. The programming skill's `check-no-excuse-rules.py` also reported **no violations in 4 files**. All Python files stay within 250 pure code lines; the test file remains in the 200–250 warning band and should be split by behavior before further expansion.

## Actual CLI and adversarial use

Created a disposable workspace with the real `init` command and four real `import` commands using synthetic transparent PNG fixtures. The white symbol fixture verifies visibility on dark surfaces. Measurement records in the visual fixture are deliberately synthetic snapshots, not claims that the color engine or a native image generator inspected these shapes.

The newly connected T4 command was then driven directly:

```sh
uv run --locked python skills/logo-land/scripts/logo_project.py \
  --workspace <fixture-root>/source color-gallery \
  --session demo --artifacts v1,v2,v3,v4 --output output/cli-gallery
```

It exited 0 with `path=output/cli-gallery`, `index_path=output/cli-gallery/index.html` and exactly the four requested IDs. Reusing that destination exited 1 with `conflict: Gallery destination already exists`. Using `--output ../escape` exited 1 with `unsafe_path: Paths must remain relative to the workspace`.

Pytest exercised relative/absolute/backslash escapes, reserved paths, output symlinks, missing and tampered PNGs, existing output preservation, empty/duplicate IDs, explicit child-only selection, relocated byte equality, missing reports, every report status in both advisory and strict mode, unknown palette evidence and XSS in brand/role/rationale/reasons. A local fault injection at the `os.link` syscall additionally verified publication rollback, unchanged session bytes and no `.logo-gallery-*` leftovers. An unknown ID produced `not_found` without output. A manual ROI projection displayed `roi · x=2, y=3, 8 x 8` with its mismatch status.

## Browser evidence

Used Orca's supported embedded-browser CLI with a dedicated page. Opened the relocated gallery directly through `file://`, without a development server. Native radio-label clicks were followed by snapshots and computed-style checks.

| Check | Observed result |
| --- | --- |
| Desktop 1440 × 1000 | Four cards; four loaded PNGs; each large preview 360px; no horizontal overflow |
| Dark surface | Every surface computed to `rgb(37, 42, 50)`; white artwork visibly legible |
| Mobile 360 × 800 | Single-column layout; no horizontal overflow; all four small previews exactly 128px |
| Transparency control | Checked native radio; computed conic-gradient checker background |
| Report badges | `unverified`, stored `pass`, `mismatch`, `unverified` for the four synthetic snapshots |
| Resource safety | Zero scripts; zero external src/href assets; no observed resource network requests |
| Actual XSS browser case | Literal `<script>...`/`<img onerror=...>` text in heading; `document.scripts.length=0`, one legitimate image, zero `onerror` elements, injected dataset value absent, no mobile overflow |
| Candidate selection | Native Candidate 2 radio selected value `2`; zero scripts; private provider text absent |

Retained local evidence root (intentionally outside the shared checkout):

```text
$TMPDIR/logo-t7-manual-o3a0c0go
```

`desktop.png` and `mobile.png` were opened and visually inspected. `desktop-snapshot.json`, `mobile-snapshot.json`, `xss-snapshot.json`, and `candidates-snapshot.json` retain the accessibility evidence. `relocated/index.html`, `source/output/cli-gallery/index.html`, `source/output/xss/index.html` and `candidates.html` remain available for coordinator inspection. Raw screenshot base64 JSON was deleted, the dedicated browser tab was closed, and no staging directories or background servers remain. The final Chrome Computer Use pass and native-image sample review are explicitly coordinator-owned, as assigned.

## Review and remaining scope

Direct review covered the requested outcomes, type boundaries, exact status mapping, privacy allowlist, path containment, no-overwrite behavior, rollback and installed-relative template lookup. Public input uses the existing typed models; no `Any`, casts, suppressed type errors, new dependencies or replacement shared types were introduced. No known T7 blocker remains. The coordinator still owns the complete multi-worker integration run, final Chrome/native-image QA and any publication or commits.
