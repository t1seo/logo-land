# Final review launch and cleanup

Orca run `run_1bb653ce3b14`, observed 2026-09-12 UTC. Q5, D1 and T5 completed before the five independent review tasks were launched. The application source, original assets, final README text and preview files remain frozen; coordinator updates to the plan, evidence index, changelog and this receipt are expected bookkeeping changes.

## Startup recovery

The first simultaneous launch wave returned `terminal_handle_stale` at `agent_readiness` for goal, code and hands-on QA. No task input was accepted for those three attempts. Security and context reached `input_accepted` normally.

`orca orchestration worker-show --dispatch <id> --json` reported each failed dispatch with no assignee and `terminal: null`. `worker-release` returned `retained / no_owned_resource`; that response did **not** prove its newly created terminal process had exited. A fresh `orca terminal list --json` subsequently exposed the three original handles. The specific Orca lifecycle cause was not established, and no runtime code was changed.

| Review | Failed readiness attempt | Accepted attempt | Final review terminal |
|---|---|---|---|
| Goal | `ctx_7e36c0fc0cc5` | `ctx_458c292798d5` | `term_11444b0c-b0ef-4716-9b2c-c25e84722127` |
| Code | `ctx_4981bc71a7f9` | `ctx_e04f3400e6b8` | `term_6fa8b333-b8ab-4e1c-8958-ee902e0cc337` |
| Hands-on QA | `ctx_9148c8040cab` | `ctx_300ac0234524` | `term_4b474584-0f91-435f-a342-5e2338833385` |
| Security | None | `ctx_e3b1ce8b9f98` | `term_39298f79-fe5b-469f-93ab-cedb7e71c412` |
| Context | None | `ctx_89ee5894fd23` | `term_cf45c2b1-9195-49de-9b90-ae0f54fd003d` |

The documented `worker-start --retry-of` flow reused each existing task. Goal and code retries were started individually; hands-on QA reused its rediscovered original terminal explicitly. All five accepted receipts report `state: ready`, `stage: input_accepted`. This records successful dispatch, not a review verdict. Each reviewer received the final seven-section scope amendment covering the original identity, five revised recipes, sixteen originals, concise bilingual pages, current installation, exact HTTP scenario, adversarial checks and cleanup.

## Owned startup resources

The failed goal/code creation receipts identify two extra terminals. Fresh `terminal read` showed only the initial Codex welcome/loading output, with no assigned task or user prompt; these were the exact terminals created by this coordinator's failed launch attempts. The fresh list and failed dispatch records were checked before targeted cleanup.

```sh
orca terminal close --terminal term_d1299a86-8313-46bd-8586-060e3f19379d --json
orca terminal close --terminal term_591078eb-7371-441c-9f6d-39ec33272ed3 --json
```

Both commands returned their exact handle and `ptyKilled: true`. No bulk close, user terminal, running reviewer, source file, browser or installed plugin was affected. The third initially created terminal was reused by the hands-on QA worker; its cleanup remained assigned to the coordinator.

## Final results and terminal cleanup

All five reviews returned accepted `worker_done` with outcome `succeeded` and PASS verdicts. Each review retained its exact channel, adversarial checks and fixture/process cleanup in its own report.

| Review | Completion message | Terminal cleanup |
|---|---|---|
| [Goal](review-goal.md) | `msg_5cbf8af548e8` | `worker-release`: released, closed_agent_terminal |
| [Code](review-code.md) | `msg_d2ba731f32ea` | `worker-release`: released, closed_agent_terminal |
| [Hands-on QA](review-qa.md) | `msg_8456e1bd456b` | Release retained external_terminal; exact coordinator-created terminal closed below |
| [Security](review-security.md) | `msg_171f24977d02` | `worker-release`: released, closed_agent_terminal |
| [Context](review-context.md) | `msg_e6c0c35cb8e4` | `worker-release`: released, closed_agent_terminal |

For QA, the fresh dispatch transcript ended at its accepted completion message and the terminal list still identified the original task-created handle. There was no new user assignment. The coordinator ran `orca terminal close --terminal term_4b474584-0f91-435f-a342-5e2338833385 --json`; it returned that exact handle and `ptyKilled: true`. A fresh terminal list confirmed all seven final/startup review terminals absent. No active worker was closed.

The coordinator independently confirmed all five exact `/tmp/ll-icons-review-{goal,code,qa,security,context}` roots absent and successfully bound/released ports8784–8788. All205 final integration file hashes still matched. No production tests, native image calls, HTTP servers or temporary files were created by this launch recovery. An optional status message raced context completion and was rejected as `dispatch_inactive`; it was not replayed to a settled worker, and no task was restarted.
