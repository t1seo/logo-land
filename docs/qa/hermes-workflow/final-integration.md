# Final Hermes integration gate

**PASS on the final source.** The five independent review verdicts are collected separately in [review-summary](review-summary.md); the subsequent release and actual download are recorded in [publication](publication.md).

## Final checks

| Check | Actual result |
| --- | --- |
| Locked full pytest | **957 passed in 295.48s**, exit 0 |
| Ruff | All checks passed |
| Formatting | **490 files** already formatted |
| Full strict types | 0 errors, warnings or notes |
| Native Python 3.11 types | 0 errors, warnings or notes |
| Locked dependencies | 23 packages; consistent lock |
| Actual native installation | Logopia Studio 0.8.0 discovered, imported and registered: **2 tools** |
| Saved-state CLI | offcut-hermes-demo, **r47 / delivered / e2 / 5 originals** |
| Installation binding | **61 managed records:** 60 exact source files and 1 exact local settings record |
| Input preservation | All **209** production, test and configuration paths and bytes unchanged across the run |

Commands were `uv run --locked pytest -q --basetemp output/hermes-final-tests`, `uv run --locked ruff check .`, `uv run --locked ruff format --check .`, `uv run --locked basedpyright`, `uv run --locked basedpyright --pythonversion 3.11 integrations/hermes`, and `uv lock --check`. Actual install and saved-state commands used `integrations/hermes/studio.py install --profile logopia --json` and `show --workflow offcut-hermes-demo` in the same locked interpreter.

[Full test output](final-integration/final-pytest.txt), [lint](final-integration/final-ruff.txt), [format](final-integration/final-format.txt), [types](final-integration/final-types.txt), [native types](final-integration/final-native-types.txt), [lock](final-integration/final-lock.txt), [saved state](final-integration/final-saved-state.txt), [installation binding](final-integration/installed-binding.json).

The install ran the actual native doctor and enabled the plugin, with both named-profile tool limits at 1,800 seconds. The default Hermes configuration digest remains unchanged. The final canonical snapshot matches the saved r47 bytes. All five public originals, four public/canonical delivery files and the ZIP's three exact member bytes match their retained digests. No additional image or model request was made during this final check.

## First failure retained

The earlier final-source attempt completed with **954 passed and 2 failed in 309.89s**. Both refer to helper PID 78509: cleanup exceeded twelve seconds, then a delayed Popen destructor warning surfaced during a later color test. The color assertion itself did not fail. [Original failure](final-integration/first-pytest.txt) remains separate from the final pass.

A real SIGINT at CPython's successful poll-lock acquisition reproduced the unreaped/locked state on Python 3.11.16 and 3.12.12. The [focused correction](fix-process-integration.md) preserves the original interrupt while protecting bounded waits, including the numeric PID query. It passed the unchanged original interruption case, the added deterministic boundary, all 39 scoped tests, six independent probes, and actual double-Ctrl-C/accumulated-output/non-main-thread manual cases. The original trace does not capture its precise interrupted instruction; the deterministic probe establishes the corrected mechanism.

The first installation-binding harness used system python3 without Pydantic and failed before writing a receipt. The final verifier used the existing locked interpreter; no dependency was added. The historical 907-test [integration result](integration.md), earlier 55/59-record payloads and the successful pre-correction installation remain attributed to their original source.

## Manual, adversarial and cleanup evidence

[Chrome and CLI review](review-qa.md), [native gallery](native-gallery.md), [process correction](fix-process-integration.md), [installer recovery](fix-installer-boundary.md) and [final provenance delta](review-context-final.md) cover their explicit scenarios and all applicable adversarial classes. They distinguish stale feedback, cancelled/unknown jobs, rejected malformed records, inert instruction-like data, preserved foreign files, finite commands, first failed evidence, misleading success and repeated interruption from a clean happy path.

The final foreground commands all exited. Pytest shell **7060** is absent; its **7,518** temporary entries were removed. The first attempt's **7,513** entries and exact shell/helper PIDs were separately removed. See [final cleanup](final-integration/final-run-cleanup.json) and [first cleanup](final-integration/first-run-cleanup.json). Private raw logs and source pins remain under ignored output/hermes-final-checks; the native profile, workflow and originals are intentional deliverables.

The focused process worker verified that 43 recorded PIDs and 31 PGIDs were absent, and removed its tmux/scratch resources. Orca retained its reused terminal as external. The coordinator checked the original task-created terminal receipt, the same live incarnation and completed task-only transcript, then closed exactly term_bdee4753-d84f-4fe3-be75-878b1ed3029b and verified its absence. No user or other worker terminal was closed. All remaining independent review terminals were released after their accepted completion, before the plan was marked verified.
