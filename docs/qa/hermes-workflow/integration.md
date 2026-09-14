# Integrated Hermes workflow verification

Status: T2 implementation gates passed. Individual core, host, gallery, launcher and recovery reports retain their first failures and manual evidence. Real revision/delivery and independent final reviews are tracked separately.

## Registered coordinator resources

- `output/hermes-integration/` retains bounded test/static-check logs and source bindings as evidence.
- `output/hermes-integration-tests/` is the exact full-suite pytest basetemp; remove after recording results. All subprocess fixtures must settle before cleanup.
- No model/image calls, QA web server, browser profile or tmux session are created by these automated commands. Real native execution has its separate resource record in [native-run.md](native-run.md).
- The four unrelated draft files and all existing artwork remain outside changes and staging. Root verified local HEAD and freshly fetched `origin/main` had zero divergence before integration.

## Preliminary validation

Native director skill validation passed with the installed Hermes Python 3.11 interpreter. The first attempt with the repository environment lacked PyYAML; no dependency was added or upgraded. The official `plugin-creator` validator passed for the repository manifest.

Codex/plugin, native/plugin and helper source versions are aligned at 0.8.0. `uv lock` changed only the root helper version; all 23 resolved dependencies retained their previous versions. The published GitHub release remains v0.7.0 until the authorized publication step succeeds.

## Integrated result

- `uv run --locked pytest -q --basetemp output/hermes-integration-tests`: **907 passed in 270.93 seconds**. The subsequent collection still contains 907 tests, including the final cancellation cases.
- `uv run --locked ruff check .`: passed. `uv run --locked basedpyright`: zero errors, warnings or notes.
- `uv run --locked ruff format --check .`: **458 files formatted**. The first check identified one test-only chained expression; its owner formatted it and verified identical AST. First-failure logs remain.
- `uv lock --check` and `git diff --check`: passed. The official Codex manifest validator and native director skill validator passed.
- Actual installed Hermes doctor reports **logopia-studio 0.8.0**, two tools and successful native import/registration. Independent comparison verified all **59 installed payload records** against saved hashes and current source; installed workspace/helper settings match this checkout.

Manual channels are documented in [core](core.md), [host](host.md), [gallery](gallery.md), [package and real-content Chrome QA](gallery-delivery.md), [launcher](launcher.md), [process interruption](process.md), [native timeout](native-timeout.md) and [critique recovery](critique-resume.md). They cover every applicable adversarial class: malformed records, inert instruction-like data, cancel/resume, stale state, foreign/dirty data, bounded calls, disclosed first failures, misleading success and repeated interruption. Live model generation is separately recorded in [native execution](native-run.md), not inferred from fixtures.

The full-suite process settled with exit 0. Its 26 MiB fixture directory was removed and independently checked absent. All implementation workers settled; gallery and launcher follow-up terminals were released by Orca. The core retry terminal was recorded as external, so its original failed dispatch's creation receipt, exact current incarnation, completed status and transcript were checked before closing that one terminal. Its transcript remains private under `output/hermes-critique-resume/`. The root no-call tmux session and PID 73301 are absent. No implementation QA server, browser context or child remains.
