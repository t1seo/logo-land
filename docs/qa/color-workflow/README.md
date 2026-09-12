# Color and typography validation

Date: 2026-09-13 KST. Source version: **0.4.0, unreleased**. Orca run: `run_c07646c87b07`.

The color workflow, typography research and symbol-plus-text layout support are implemented. The final integrated suite passed **315 tests**, including the legacy metadata export correction. The complete release goal is **not achieved**: the required restricted-color and white-transparent native samples remain unresolved after the permitted repairs. The latest published release remains 0.3.1.

The implementation is committed and pushed to main. A v0.4.0 GitHub draft is prepared with `published_at=null`; no public v0.4.0 tag exists. See the [commit and release record](release.md).

## Actual native results

The [eight-case gallery](../../colors/index.html) contains real Codex native images, including unsuccessful candidates. Eight initial requests and eight additional native edits produced sixteen new images. The separate white-variant session also stores a byte-identical copy of the original Korean parent, so its seventeen stored artifacts do not mean seventeen generation calls.

| Case | Color evidence | Visual/delivery outcome |
|---|---|---|
| SUNROOM BAKERY | Automatic palette; sampled pass | Exact text and composition are correct. The BAKERY subtitle is too small at 128px; visual review records `small_size_ok=false`, with no delivery. |
| NORTHLINE | Local automatic palette; advisory pass | Stacked symbol and text reviewed in Chrome; original PNG, guide and ZIP exported. |
| GROVE SUPPLY | Fixed green anchor; strict pass | Horizontal transparent logo reviewed and exported. Recommended for light surfaces; green has limited dark-surface contrast. |
| GROVE warm edit | Anchor-only color pass | Initial edit and both repairs contain an opaque painted checkerboard. A color pass does not establish background correctness. No delivery. |
| 밤결 | Restricted black/ivory; original indeterminate | Correct Korean lettering, but partial-alpha coverage exceeds 10%. Both repairs introduce an opaque checkerboard and color mismatch. No delivery. |
| TIDE & TYPE | Reference-derived palette; advisory pass | Horizontal symbol and text reviewed in Chrome; original PNG, guide and ZIP exported. |
| FIELD NOTE | Reference + locked green + two-color limit; original indeterminate | Partial-alpha coverage exceeds 10%; both repairs produce an opaque checkerboard and color mismatch. No delivery. |
| White 밤결 | White-only palette; all three attempts indeterminate | Final attempt has 923 partial-alpha samples among 3,483 visible samples (26.5%) despite a clean-looking Chrome preview. Its 100% core-pixel color coverage does not make it a pass. No delivery. |

No alpha or color thresholds were relaxed. No programmatic recoloring, background removal or raster repainting was used. Every generated original and each actual prompt remain traceable. Font references describe requested appearance; no exact font outlines or installed font files are claimed.

The white logo looks clean in the Chrome preview. A read-only [alpha diagnostic](alpha-explanation.json) found that 606 of its 923 partial-alpha samples have alpha 1–5, below 2% opacity. This helps explain why the conservative sampling result differs from ordinary appearance. It does not alter the declared policy, establish whole-image conformance, or authorize export. Earlier native-tool preview descriptions of visible white damage were corrected after Chrome inspection.

Evidence: [native cases](native-cases.md), [structured case record](native-cases.json), [Chrome observations and screenshots](chrome-live.md), [export byte checks](native-export-check.json).

The three exported PNGs match both their imported originals and the PNG inside each ZIP, byte for byte. Each ZIP contains exactly `logo.png`, `manifest.json` and `brand-guide.md`. The manifests record schema 2, measured color evidence, the applicable strict/advisory policy and `appearance-reference-only` font usage.

## Implementation checks

| Check | Evidence |
|---|---|
| Final integrated tests: 315 passed | [Final test output](final-tests.txt) |
| Ruff passed | [Final lint output](final-ruff.txt) |
| Basedpyright: 0 errors, warnings or notes | [Final type output](final-types.txt) |
| Formatting passed, 145 files checked | [Final format output](final-format.txt) |
| Locked dependencies passed | [Final lock check](final-lock.txt) |
| Legacy EXIF export compatibility and ICC reason preservation | [Correction and regression evidence](metadata-export-fix.md) |
| Five independent review perspectives | [Review integration](review-summary.md) |
| Staged authored-file whitespace check passed; five raw evidence files retain their captured trailing spaces | [Scope and preserved-byte rationale](whitespace.md) |
| State, v1 compatibility and immutable bindings | [T1](t1-state.md) |
| Local palettes and conflicting restrictions | [T2](t2-palettes.md) |
| Reference decoding, sampling, alpha and color analysis | [T3](t3-analysis.md) |
| CLI state transitions and provenance | [T4](t4-workflow.md) |
| Strict/advisory exports and original-byte preservation | [T5](t5-export.md) |
| Conversation and typography guidance | [T6](t6-conversation.md) |
| Portable comparison gallery | [T7](t7-gallery.md) |
| Bilingual instructions and actual CLI examples | [T8 documentation](t8-docs.md) |

The earlier integration checkpoint passed [299 tests](full-tests.txt). The final 315-test result includes 16 new metadata compatibility cases. The earlier format check found only a pre-existing wrapped test constant in `tests/conftest.py`; formatting that expression changed no behavior. Worker red/green logs and the original five reviews describe their respective checkpoints; use the final outputs and review integration for subsequent corrections. Public logs replace machine-specific home/project paths with placeholders.

## Remaining release gate

The plan requires a successful anchor case, a successful restricted-color case, a white-transparent case, and five independent final reviews before publication. The anchor requirement passed; the restricted and white-transparent requirements did not. The bounded native attempts are finished. Software tests are not a substitute for those native results.

The [continuation escalation audit](continuation-escalation.md) independently confirmed three consecutive white-native failures under the same alpha policy. This bounded automation run stopped at its retry limit with T8, VERIFY and T9 still unchecked. The requested specialist agent type was unavailable; the report identifies the available independent reviewer accurately and claims no specialist approval.

The final personal installation completed 29 CLI calls from the refreshed cache: 27 successes and two expected strict refusals. Its 55-file payload matches source apart from the official manifest cachebuster; see [final installation evidence](installation-040-final.md). The [earlier 15-call checkpoint](installation-040.md) remains historical evidence. Chrome QA completed 46 original JPEG screenshots, real link/control checks and three downloads with matching SHA-256 values. Five independent reviews and subsequent corrections are recorded in [review integration](review-summary.md). This page does not claim that a tag or public release exists for 0.4.0. See [the plan](../../../plans/logo-land-color-workflow.md) and [release procedure](../../releases.md).
