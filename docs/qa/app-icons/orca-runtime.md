# Orca input recovery

The twelve worker launches returned `ready / input_accepted`. At 17:15 UTC on 2026-09-12, nine native workers had saved receipts, while pictogram, abstract and installation had no reported agent session. This was an orchestration observation, not a Logo Land test failure.

Three hypotheses were checked: an unsubmitted pasted prompt, a startup wait, or active work whose session hook had not reported. Independent bounded `worker-read` calls showed pictogram and installation at `[Pasted Content ... chars]`, without transcript or heartbeat. Abstract's terminal stream contained animated redraw output and likewise no reported session. Their exact `worker-show` records confirmed live owned terminals; there was no evidence of a native call for either missing candidate.

The coordinator sent only one Enter byte to each existing terminal using `orca terminal send --terminal <exact-owned-handle> --enter --json`. It did not resend a task, create a replacement worker, interrupt a running image call, or modify runtime/source/configuration. The commands each returned `accepted: true, bytesWritten: 1`.

The subsequent exact-dispatch reads switched all three from `source: terminal, fallbackReason: session_not_reported` to `source: transcript` with actual user/task input; pictogram and installation were already executing their first tool calls. This confirms that submitting the existing input restored progress. The reason the original Enter was not processed is not established. No native attempt identity or budget was reset.

Affected dispatches: pictogram `ctx_e499233eb5d1`, abstract `ctx_2262ecc61774`, installation `ctx_260a5957592a`. No debugging files, processes, ports or replacement sessions were created. The existing supervised workers retain their original task IDs and normal completion/release obligations. This operational recovery changes no product code and therefore has no new product regression test.
