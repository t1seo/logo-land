# Hermes workflow preflight

15 September 2026 KST. Implementation baseline: `f7dd3268313d2422b87efea63eef8257b0e651b9`.

- Existing suite: **642 passed in 149.59s** (`output/hermes-preflight/baseline-tests.txt`).
- New unchanged-code characterization: **2 passed in 0.79s**, `tests/hermes/test_existing_helper.py`. A future workflow sidecar leaves legacy show/list and session bytes unchanged; PNG import does not select or approve the original. Initial test collection used the wrong fixture import (`conftest`); corrected to the repository's `tests.conftest` convention before the passing baseline. No production change preceded it.
- Native runtime: Hermes v0.21.0; installed source `d3e2ace1dde9f1d279f99c9ebc6bce2e761b025d`; Python 3.11.16, Pydantic 2.13.4, Pillow 12.3.0. Existing helper remains Python 3.12.
- Isolated `logopia` profile created without aliases/bundled skills. Main model/provider follows the existing `gpt-5.6-sol` / `openai-codex` selection; native image provider is configured only in that profile. No credentials copied or default profile changed.

## Actual native image channel

The finite Hermes chat prompt requested one diagnostic teal open ring on white. The exported session `20260915_001913_1307d4` contains **one actual `image_generate` tool result**, provider `openai-codex`, model label `gpt-image-2-medium`, success and exact local file path. The original was independently opened and visually inspected, decoded by `sips`, and hashed.

- Decoded PNG dimensions: **1254 × 1254**.
- SHA-256: `79fd22cebe5303e7e67d42be7b6766f5194acccbb2032746243283b834422ba6`.
- Requested provider dimensions were 1024 × 1024; the actual 1254 × 1254 output is the measured fact. No upscaling was performed.
- Exact prompt, stdout, stderr and redacted session are retained privately under `output/hermes-preflight/`. The actual image is retained in the isolated profile's image cache. This diagnostic is not presented as a finished brand logo.

This is connection and generation proof only. Real structured critique, reference edit, interruption handling and final delivery remain implementation acceptance work.

## Primary research and design review

Three real Orca research tasks completed in `run_ad4a666ccb76`: installed runtime/API, repository contracts, and design/UX. Their findings are synthesized in [research](../../research/hermes-design-workflow.md). Runtime and repository terminals were released; the design worker was explicitly transferred to the bounded plan-gap review.

The gap review found six contracts requiring decisions: actual Python3.11 QA, fixed call/recovery budgets, two-store import/export reconciliation, image-bound critique aggregation, advisory color/fixed-intent edit scope, and strict copy-back feedback. All six have concrete resolutions in [CONTRACT.md](../../../integrations/hermes/CONTRACT.md). No additional approval or platform is required.

## Adversarial scope and resources

The research phase verified source-version mismatch and the difference between requested versus decoded image size; neither documentation nor a success string is treated as production-quality evidence. Existing dirty drafts and all source/artwork were preserved. Bounded CLI/HTTP probes completed, no polling-generated native retries occurred, and only the specific diagnostic session was exported.

Malformed input, instruction-like feedback, cancellation, stale workflow state and repeated interruptions are runtime implementation tests, not claims made from this research phase. Flaky-test recovery is not established by the baseline; its first fixture import failure remains disclosed above.

All research download/temp resources were removed by their owning workers; the baseline/probe subprocesses exited. The installed named profile, diagnostic original and private evidence are intentional retained resources. No QA browser/server/port was created during preflight.
