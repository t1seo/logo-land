# Final review integration

Date: 2026-09-13 KST. Orca run: `run_c07646c87b07`.

Five independent Orca workers reviewed the implementation, existing behavior, actual CLI workflows, public evidence and installation. Their reports preserve the findings at their review checkpoints; this page records the subsequent integration decisions.

**Development-source readiness: PASS after independent correction review. Public release and whole-goal completion: blocked by the required native results.**

| Perspective | Development-source finding | Evidence |
|---|---|---|
| Goal and constraints | G3 Dark-preview discrepancy resolved for new output; essential native release gates remain unmet. | [Goal review](review-goal.md), [independent correction review](review-corrections.md) |
| Code quality | C1 legacy EXIF export regression corrected and independently rechecked: PASS. | [Code review](review-code.md), [correction evidence](metadata-export-fix.md), [independent recheck](review-corrections.md) |
| Security and integrity | No new actionable security blocker. A pre-existing low-severity error-message disclosure remains outside this change. | [Security review](review-security.md) |
| Hands-on QA | 98 real source-CLI calls across 30 scenarios; no additional CLI blocker. Required native success scenario fails. | [QA review](review-qa.md) |
| Git, documentation and research | English/Korean release wording corrected; source attribution, installation identity and original sample preservation verified. | [Context review](review-context.md) |

## Corrections

- C1 correction: accepted legacy/advisory PNGs retain original-byte delivery with truthful unavailable color evidence when optional EXIF analysis cannot proceed. Unsupported ICC reasons are preserved. Strict refusal, hash/fact checks and propagation of programming errors remain enforced. The correction passed 94 focused tests and an actual v0.3.1 schema-1 export. An independent reviewer reproduced the old failure and corrected success, passed 67 focused tests, and approved C1/G3 without a new actionable finding.
- G3: the production comparison template now uses `#171717` for its Dark surface, matching the default measured surface and public overview. Earlier generated comparison HTML remains an unchanged historical snapshot using `#252a32`; its measured contrast reports explicitly name their own surfaces. No existing PNG or quantitative report was changed.
- Both README release badges and release links now identify published v0.3.1 separately from unreleased development v0.4.0. The Korean opening includes the same incomplete-native-validation notice as the English opening.
- The white-logo editorial result follows the actual Chrome observation: clean-looking lettering with indeterminate quantitative alpha evidence. Unsupported earlier descriptions of visible damage were removed; originals, prompts and measured reports were preserved.

## Publication decision

**Public v0.4.0 release: blocked.** No approved restricted-color or white-transparent native delivery exists under the current policy. The allowed repairs are exhausted. A clean-looking preview or a passing synthetic fixture cannot replace these requirements. The whole goal remains incomplete even after software corrections pass.

The final source suite passed **315 tests**, with clean lint, types, formatting and locked dependencies. The refreshed installed payload matches all **55 files**, apart from its explicit manifest cachebuster; **29 installed-helper calls** produced 27 successes and two expected strict refusals. See the [final installation record](installation-040-final.md). All implementation and review workers have completed their assigned scopes and have been released.

The assembled staged diff exposed trailing spaces in five generated guide/log evidence files. Those captured bytes are preserved; the authored-file whitespace check passes. The [exact exception](whitespace.md) distinguishes this from an unrestricted staged check.

The verified development source and truthful evidence are approved for preservation on main. A development commit or an unpublished release draft does not declare the native release gates satisfied. See [validation](README.md), [native results](native-cases.md) and the [execution plan](../../../plans/logo-land-color-workflow.md).
