# Logopia 0.8.0 code review

Status: IN PROGRESS. Review-only scope; production source is frozen.

## Plan

1. In progress: pin source, canonical workflow, public originals and protected drafts; read contract/evidence and full native source plus helper boundary.
2. Pending: execute the two assigned regression files with a finite deadline and the exact tmux read-only manual scenarios.
3. Pending: map nine adversarial classes to concrete observations, assess findings, verify unchanged inputs, clean owned resources and report once.

## Resource ledger (register before creation)

- TODO: create `docs/qa/hermes-workflow/review-code/` for retained sanitized review evidence; intentional report artifact, retain.
- TODO: create `/tmp/logopia-review-code-080` for owned QA scratch; remove exact directory and contents after evidence capture.

No production edits, native inference, artwork changes, profile/config writes, nested agents, private export publication, commit, push or release are authorized by this review.

## Bounded verification resources and hypotheses

- TODO (before creation): `/tmp/logopia-review-code-080/run_assigned.py`, one finite test-runner child/process group and `/tmp/logopia-review-code-080/pytest`; 180-second outer limit, existing helper children retain their 60-second bound. Retain sanitized logs in this report's artifact directory and remove scratch after settlement.
- TODO (before creation): tmux session `logopia-review-code-080`, its single shell pane PID, and its two finite read-only CLI children; close only this owned session and confirm pane PID absent. No model process or network service is started.
- Hypothesis A: launcher settlement only waits for the direct leader, so a same-group descendant can outlive a timed-out command. Compare ordinary finite child with a harmless bounded descendant and inspect exact PID after receipt.
- Hypothesis B: the helper's `Popen` context handles a local interrupt differently from its explicit timeout path. Distinguish exception propagation from actual child exit; no provider calls involved.
- Hypothesis C: installer extra-file checks exempt the marker basename below the root as well as the real root marker. Compare an ordinary foreign file with a nested file of that basename in a temporary fixture.
- Alternative to A/B: observed survivors may be harness timing or already-exited zombies. Require exact PID/process-state evidence, readiness signaling and bounded cleanup.

Assigned unchanged baseline: 10 passed in 25.38s; outer receipt exit 0, not timed out, 25.655s. Actual tmux show: success, r47/delivered/e2, five candidates and exit 0. Canonical SHA remained `16eea6dc8c32e979c432fbdffee137d76cb68a230aad9e5b65cc740d59e26e04`.

- TODO (before creation): `/tmp/logopia-review-code-080/test_review_boundaries.py` and `/tmp/logopia-review-code-080/probe-pytest` for three narrowly justified defensive tests; fake installer roots exist only under this scratch root. Every child script has a 10-second self-deadline, launcher has a 2-second deadline, the helper probe a 5-second transport deadline, and test-runner outer deadline is 60 seconds. Preserve the first assertions/output; never change production or weaken expectations.
- TODO (before creation): child fixture scripts, readiness pipes and exact child/descendant PIDs under the owned `probe-pytest` root; close both pipe ends, signal only recorded owned PIDs, and retain their post-cleanup absence evidence. No service/port/browser/download is created.
- First harness-only static check: runner Ruff reported executable-bit and fixed `/tmp` path warnings; basedpyright was clean. Make the owned script executable and derive basetemp from its registered parent; do not alter tests or source.

- Confirmed RED: three defensive assertions failed in 2.63s. Launcher descendant PID 19778 was sleeping and orphaned (PPID 1); interrupted helper PID 19859 was still sleeping; both were explicitly settled and confirmed absent. Installer returned success and removed its fixture user's nested marker file. The exact first failure is retained in `review-code/defensive-tests.txt`; source is unchanged.
- TODO (before creation): `/tmp/logopia-review-code-080/test_install_recovery.py` and `/tmp/logopia-review-code-080/install-pytest`, containing an ordinary rename-failure rollback control and the corresponding interrupted-rename test; all fake profile/source files remain under scratch. This targeted follow-up is justified by the same installer's backup being inside `TemporaryDirectory` while rollback catches only `OSError`.
- TODO (before creation): `/tmp/logopia-review-code-080/source_audit.py`, a read-only Python 3.11 grammar/type-escape scan; no imports from the helper or Hermes, no cache compilation, no processes/network.

## Initial verdict and root-routed dependency

Initial verdict: **FAIL, high confidence**, four observed blocking defects. The source grammar audit passed on actual Python 3.11.16: all 50 native Python files parsed, no `Any`/`object`/`cast` name uses, no helper imports, maximum 229 nonblank/noncomment lines. The helper remains separately locked Python 3.12; dependency versions are unchanged from f7dd326.

The root's `FIXES_READY` dependency (message `msg_3a5fc02de0ae`) explicitly permits separate implementation workers to change only the process/installer modules and dedicated regression tests. This reviewer remains read-only and must preserve the first failures, inspect the final narrow delta and rerun identical assertions after that signal before final settlement. The fourth rollback finding was sent in `msg_20d82679d089`.

- TODO (before creation): retained sanitized `review-code/pre-fix/` source snapshots of `launcher_process.py`, `helper_process.py` and `installer.py` for comparing the authorized fixes. These are evidence artifacts, not production files.
- Follow-up RED: injected `KeyboardInterrupt` at the second installer rename removed the entire prior install; ordinary `PermissionError` at that same boundary restored exact bytes (1 failed, 1 passed in 0.05s). No live profile was accessed.

The `omo:debugging` runtime/setup/investigation references are used for these focused local concerns. The task's explicit review-only ownership replaces the skill's source-fix and nested-agent defaults.

## FIXES_READY revalidation resource registration

- TODO before use: `/tmp/logopia-review-code-080/defensive-fixed-pytest` and `/tmp/logopia-review-code-080/pytest-cache-fixed` for the identical three behavioral regressions after the coordinator's fix-ready signal; finite 60-second test child, self-bounded fixtures, exact recorded PID cleanup.
- TODO before use: `/tmp/logopia-review-code-080/install-fixed-pytest` for unchanged installer rollback assertions after the fix; 20-second self-deadline. Preserve the first RED logs and source beside the new final evidence.
- TODO before use: reuse only the session name `logopia-review-code-080` for a final read-only show/malformed-ID replay after helper source changes; capture its new pane PID, close it and verify absence.
- No current test children remain: initial uv/pytest/fixture PIDs 13647, 19759, 19760, 19775, 19778 and 19859 returned no rows from exact `ps` query. Original tmux pane PID was 13716; its prior post-close query also returned no rows.
- Owned-code lint/types are clean. The preserved follow-up probe has only cosmetic invocation-comment wrapping, an unused-return assignment and removal of the injected PermissionError's incidental message; its exception classes and all behavioral expectations remain unchanged.

## Authorized code-ready delta and one newly exposed composition boundary

`FIXES_CODE_READY` (`msg_6296f97247e9`) authorized the unchanged original probes. They passed: 3/3 in 2.62s, plus both installer rollback variants in 0.04s. The source parser now covers 51 native files. Root also explicitly announced `process_group.py` and the native-run wording correction (`msg_9d1ab6277ac2`).

- TODO before creation: `/tmp/logopia-review-code-080/test_nested_helper.py` and `/tmp/logopia-review-code-080/nested-pytest`. This single new probe is justified by composition of the new one-PGID settlement with the existing actual helper's `start_new_session=True`: if the leader must be forcibly killed, can that helper group survive? Both fixture programs self-terminate at 10 seconds, launcher deadline is 2 seconds plus 0.2-second grace, helper timeout is 8 seconds, test parent is bounded at 20 seconds.
- TODO before creation: two fixture script files, one owned launcher leader/process group and its one owned actual `run_cli` child group, all below `nested-pytest`; record exact PIDs and settle only those if still present. No Hermes process, profile, inference, external target, network or user process is involved.
- TODO before creation: `/tmp/logopia-review-code-080/pyrightconfig.json` for strict temporary-module import resolution. Initial nested-probe typecheck could not resolve its sibling scratch module under the repo-only import roots; preserve that diagnostic, add only the owned scratch/repo import roots with all-mode Python 3.11 checking, and do not suppress type errors.

## Final fix dependency preparation

Root decision `msg_799670983937` permits numeric PID-only enumeration scoped to the launcher's own new SID, with membership rechecked before signals, and `process_group=0` for helper groups in that session. Standalone helper cleanup remains PGID-only; no IPC, Python preexec_fn or watcher is requested. Final implementation and unchanged nested reproduction remain pending.

- TODO before creation/reuse: `/tmp/logopia-review-code-080/defensive-final-pytest`, the existing `install-fixed-pytest` and `nested-pytest` paths, and the owned pytest-cache directory for final unchanged assertions after code-ready. No test expectations will change. The original three-test runner retains a 60-second limit; the two installer and one nested fixture retain their 20-second parent limit and all fixture-child deadlines.
- TODO before modification: extend only the owned `run_assigned.py` output/basetemp selector with a distinct `defensive-final` label so prior RED and first-GREEN logs remain immutable; preserve the final harness as a retained text artifact. This is harness routing, not source or assertion modification.

Final process-ready message `msg_106cf19ad510` authorized the unchanged original probes. Results: 3 passed in 2.65s, 2 installer variants passed in 0.03s, nested actual-helper case passed in 2.33s. Recorded final descendant/helper PIDs 71206, 71268 and 71528 were absent before each receipt assertion; all tests returned exit 0 and final source hashes matched before/after.

- TODO immediately before reuse: create only tmux session `logopia-review-code-080`, record its one new shell pane PID, send the exact read-only native demo `show` command and malformed-ID command, capture actual JSON/exit status and canonical hashes, then close only that owned session and confirm its pane PID is absent. No model, image job, server or browser is started.

Final tmux actual JSON again reported r47/delivered/e2 and five candidates, exit 0; malformed ID returned invalid_id/exit 1. Pane PID 72876 and final fixture PIDs 71203/71206/71268/71528 were confirmed absent after exact-session closure. All 13 protected files and all 14 public files still matched the initial pin at this manual checkpoint.

Root message `msg_2f4d0c5fda08` announces the operational G2/doc clarification (ten-second grace plus ten-second force verification and bounded query cleanup; retained installer backup path). Final source comparison has exactly four changed original files: CONTRACT.md and the three announced production modules; seven new source/test files are explicitly listed in source-added-paths.txt. No unexplained source drift was found.

- TODO immediately before cleanup: remove only `/tmp/logopia-review-code-080` after retaining the final scripts/config as text artifacts, including all basetemps, fixture profiles/originals, pytest cache and bytecode under that exact root. Verify both `/tmp` and `/private/tmp` aliases absent, the registered tmux session absent, and exact recorded owned PIDs absent. No owned network port, browser, download or installed package exists; shared repository/uv caches are not owned and are preserved.

Integration hold (`msg_48a63491e96f`): root reports one failure in the repeated helper-interruption test during a 956-test full run; traceback pending. This is attributed incomplete integration evidence, not a failure of this reviewer's unchanged final probes. Root's first binding-verifier attempt separately used bare Python without Pydantic and made no mutation. Preserve all successful independent receipts and do not issue final PASS/worker_done until this hold is resolved. The first report-only hold update failed exact patch matching without applying any edit; a full-line match then updated the report successfully.

## Reopened narrow validation for the routed integration correction

Root messages `msg_492c223721fc` and `msg_2cdf4f9f2963` require review of the same acquisition-window defect across the already owned launcher/helper/PID-query boundaries, then original/targeted probes after owner SOURCE_FROZEN. The prior cleanup receipt remains a truthful completed checkpoint, not a claim that this new scratch phase never existed.

- TODO immediately before creation: recreate exactly `/tmp/logopia-review-code-080`, restore byte-identical `test_review_boundaries.py` and `test_nested_helper.py` from this review's retained artifacts, and restore `source_audit.py` for the actual native parser. These are the same assertions, not new scenarios.
- TODO immediately before creation: `/tmp/logopia-review-code-080/run_settled.py`, a fixed six-case runner for the original three boundaries, original nested helper, and the existing repeated-helper-interruption test's original/additional acquisition parameters. It will have a 60-second outer limit, exact-PID/session cleanup, and fresh `settled-pytest`/`settled-cache` under the registered root. All fixture children retain their ten-second self-deadline. No execution before SOURCE_FROZEN.
- TODO before owned final child creation: one owned uv/pytest runner and its already existing finite fixture descendants; retain exact exit/log/PID observations in new settled artifacts. No inference, real profile, real image, server, browser or package installation is involved.
- TODO before later manual reuse: the same registered tmux session name `logopia-review-code-080`, its one new pane PID and only the exact read-only show/malformed commands; capture, close and verify absence again after final source changes.

Source-frozen message `msg_ed9dba9542fb` authorized the six fixed cases. They passed in 5.45s (outer 5.729s, exit 0, no timeout); source-frozen checks passed before and after. Exact final fixture PIDs 6089/6251/6259/6432/6442 were absent in their result observations, and the repeated-interruption assertions preserved original exception identity and zero warnings. The runner's initial implicit-string-concatenation lint/type diagnostics are retained; only selector construction was corrected before clean checks, without changing any assertion.

- TODO immediately before final manual reuse: create only `logopia-review-code-080`, record its fresh pane PID, replay the exact show and malformed-ID commands, preserve before/after canonical SHA and exit captures, close that session and confirm the fresh pane PID absent. This reuses the previously registered channel after the integration fix; no native/model invocation occurs.

Final installed binding `msg_06698fafefde` is available at `output/hermes-demo/installed-final-binding.json`. This reviewer read only its explicit verification metadata, independently matched all 61 installed managed hashes and all 60 corresponding repository source files (settings is installed-local), and retained a sanitized count/boolean summary. Default-config preservation is attributed to root's pre/post binding, not a new reviewer pre-install measurement. All original 13 protected files and 14 public files still match; final native show is r47/delivered/e2, exit 0, malformed refusal exit 1, canonical SHA unchanged.

- TODO immediately before second cleanup: remove exactly `/tmp/logopia-review-code-080` with `rm -r`, after the final runner and unchanged probes are already retained as review artifacts. Verify both tmp aliases absent, the owned tmux session absent and the current dispatch's last fixture PIDs 6085/6089/6251/6259/6432/6442 plus pane9049 absent. Earlier PID checks remain historical receipts because numeric PIDs can be reused. No unrelated process/session/cache is touched.

## Final settlement

Root FIXES_READY `msg_8f4972033e5f` reports 957 passed in 295.48s, all eight gates exit 0, unchanged 209-file input inventory, exact final installation and its cleanup. This reviewer read the actual sanitized final test/static/input/install receipts and attributes them correctly. Independent final six-case PASS, actual three read-only tmux checkpoints, 61 installed/60 source hash checks and final cleanup are complete. Final review verdict: PASS, high confidence, no open blocking findings. No source/model/profile/publication action or nested agent was performed by this reviewer; only the owned report/artifacts remain. One worker_done will settle this dispatch after final report-link verification.
