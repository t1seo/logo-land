# Security review: Logopia 0.8.0

**PASS. No blocking security issue remains.** The final source, actual installed payload and bounded checks pass; the coordinator's FIXES_READY message msg_ec657bc3e7ea confirms the final integration gates. Confidence is high for the observed local boundaries, exact artifacts and file bindings; this is not a live-provider adversarial test or an aesthetic-quality measurement.

Reviewed against f7dd3268313d2422b87efea63eef8257b0e651b9, including the full relevant untracked implementation, adjacent helper/launcher/export code, G1–G7, plan and integration/native evidence. No production source, artwork, profile/configuration, dependency, branch or worktree was changed by this reviewer. Publication remains root-owned T6; its pending status is not an implementation defect.

## Final source and privacy binding

The canonical demo remains **r47 / delivered / e2**, SHA-256 16eea6dc8c32e979c432fbdffee137d76cb68a230aad9e5b65cc740d59e26e04. The five originals and actual delivery retain their exact bytes: three initial image jobs plus two edits, c1 → e1 → e2. e1's failed preservation observations remain; e2 has two fresh passing model critiques. Existing job fields are equal after optional retry_of:null normalization; raw historical job JSON byte equality is not claimed.

- Independently hashed all **61 actual installed files** and **60 checkout counterparts**, including both new process modules. All matched the final private binding. [Sanitized summary](review-security/final-installed-binding-summary.json), [source checks](review-security/final-installed-source-check.txt), [actual-file exits](review-security/final-installed-actual-check.exit).
- **204 of the original 210 pins remain unchanged.** Six changes are authorized: installer.py, launcher_process.py, helper_process.py, CONTRACT.md and the English/Korean Hermes docs. Seven additions are the two process modules and five regression files. [Original pins](review-security/pin.sha256), [expected delta](review-security/final-original-pin-check.txt), [current pins](review-security/final-current-pins.sha256), [added files](review-security/final-added-source.sha256), [frozen process checks](review-security/final-process-pin-check.txt).
- The four unrelated .omo drafts, public sample, canonical state and original private receipts remain pinned. Authorized native-run wording and new installation receipts have [separate hashes](review-security/final-new-binding-pins.sha256). Root's final binding reports unchanged default configuration and matching workspace settings; the earlier independent three-configuration checks remain historical evidence.
- The final public marker scan found **zero matching paths**; the index had **zero staged paths**, and output/ plus .logo-generator/ had **zero tracked paths**. [Public scan](review-security/final-public-private-marker-paths.txt), [staged set](review-security/final-staged-paths.txt), [tracked-private set](review-security/final-tracked-private-paths.txt). No private session export, system/reasoning transcript, auth cache or credential content was read or published here.
- The dependency lock still differs from the base only in the root helper version, 0.7.0 → 0.8.0. No dependency version/hash changed. [Exact lock diff](review-security/lockfile.diff).

Root authorized the final read-only binding in msg_041d616e4d81. The 61-file installed binding supersedes the original 59-file receipt for final source identity; the old receipt is retained without changing its historical meaning. Final root verification records **957 passed in 295.48s, exit 0**, unchanged inventory/bytes across 209 production/test/config inputs, full Ruff/types/native Python 3.11 types, 490-file formatting, lock and saved-state gates all passing. These are attributed coordinator executions, personally checked in the [final pytest output](final-integration/final-pytest.txt) and [eight-gate/source/cleanup receipt](final-integration/final-run-cleanup.json), not a new broad run by this reviewer.

## Findings and their resolution

All rows below were **Major / blocking when observed**. Their original failures remain available. No Critical finding or unresolved Minor finding is asserted.

| Boundary | Initial failure and final evidence |
| --- | --- |
| Nested foreign installation marker | A foreign user-notes/.logopia-install.json was deleted, although an ordinary note was refused. The exemption now matches the exact root-relative marker; symlinks are checked first. Original failure and independent GREEN: [defensive RED](review-code/defensive-tests.txt), [defensive GREEN](review-code/defensive-final-tests.txt). |
| Second publication rename interruption | KeyboardInterrupt bypassed rollback and deleted the old install; the OSError control preserved it. Both renames are now inside recovery. [Original pair](review-code/install-rollback-tests.txt), [resolved pair](review-code/install-rollback-final-tests.txt). |
| First backup rename interruption, independently found here | Actual SIGINT immediately after the real first rename left target_exists=false and no previous bytes. The unchanged control passed first. On frozen installer 8f75ba7f123f2550d405f4015de54319453b867044f635e0c7d3ed4b4de02116, the **same original two cases pass in 0.11s**, with exact prior bytes restored. [Original source/probe](review-security/first-rename-probe.py.txt), [control](review-security/first-rename-control.txt), [RED](review-security/first-rename-interrupt.txt), [GREEN](review-security/first-rename-fixed.txt). |
| Launcher/helper descendants | Reaped leaders were mistaken for settled groups; a helper survived interruption, and an actual nested helper survived forced launcher exit. The launcher now owns its fresh session, while helpers retain separate groups inside it. [Original nested failure](review-code/nested-helper-tests.txt), [independent nested GREEN](review-code/nested-helper-final-tests.txt), [process evidence](fix-process.md). |
| Forced cleanup bound | Popen context exit could wait beyond the forced-settlement budget. The callers now own streams without an implicit Popen context wait and return explicit failure if settlement cannot be verified. [Original failure](fix-process/red-force-bound.txt), [bounded outcomes](fix-process/green-nested-boundaries.txt). |
| Repeated-interrupt acquisition race | Root's first full rerun exposed a held Popen poll lock and delayed ResourceWarning. A deterministic real-SIGINT fixture reproduced it on Python 3.11/3.12. Bounded interrupt deferral now releases the lock before preserving the original interrupt. [RED](fix-process-integration/red-acquisition.txt), [39 scoped passes](fix-process-integration/green-scoped.txt), [3.11 GREEN](fix-process-integration/probe-py311-green.txt), [3.12 GREEN](fix-process-integration/probe-py312-green.txt). |

This reviewer made no source fix. The first-rename failure was escalated as msg_977fa4ddb4d1 and routed to task_8aa6c56bce98. The exact original driver bytes and assertions were retained across RED/GREEN. Restoration failure or an occupied foreign file/directory/symlink now preserves the old backup, annotates the original exception and avoids a success receipt. Both strengthened installer regression files were read in full. Their 42-test and actual two-runtime manual results are attributed to [installer boundary QA](fix-installer-boundary.md), not counted as new executions here.

## Requirements and trust boundaries

| Requirement | Assessment |
| --- | --- |
| G1 / runtime and supply chain | Native code remains Python 3.11-compatible, with Pydantic >=2.12,<3 and Pillow >=11.2,<13. The helper uses its separate locked Python 3.12 environment through fixed uv argv. No vendored private Hermes implementation, dependency upgrade or credential copying was found. |
| G2 / G7 / bounded recovery | Reservations, strict revisions, unknown-job fences and exact critique-retry eligibility remain unchanged. No fallback resubmission or cache guessing was added. Local settlement does not claim provider cancellation. |
| G3 / preservation | Deterministic import/export identity, original/parent/prompt hashes and helper receipt validation remain authoritative. Fresh gallery output rolls back only owned files. Installer recovery preserves both foreign target bytes and unresolved old backup bytes. |
| G4 / actual evidence | Two distinct critic roles/call IDs bind the original, parent and target-view digests and five criteria. Failed preservation remains a failure; incomplete or mismatched reviews cannot authorize delivery. Actual originals and the public delivery validator passed. |
| G5 / G6 / input and intent | Frozen strict schemas reject extras, bad revision types, invalid identifiers, duplicate keys, oversized input and unsupported strict color policy. Exact keep/change, saved intent, revision and candidate digest remain bound. Instruction-like text is serialized data; it cannot select roots, commands or provider settings. |
| Literal argv / trusted settings / authentication | Model input cannot supply workspace/helper roots or executable strings. Strict installed-local settings supply them. Native calls use public structured-completion and image dispatch facades; no raw provider HTTP/auth implementation was found. |
| Path and symlink boundaries | Managed reads reject traversal, symlinks, nonregular/oversized files and digest mismatches. Benign fixtures preserved the foreign target. Trusted user-selected roots are a desktop trust boundary; hostile concurrent filesystem replacement is not claimed to be sandboxed. |
| DOM and public payload | Prose is escaped, embedded JSON protects HTML delimiters, and dynamic UI uses textContent/form values. Native CSP denies network connections. The curated public projection is separate from the private local gallery's full workflow. |
| Bounded ZIP | The public validator enforces exactly three unique regular members, size/compression/encryption constraints, exact hashes and bounded reads without extraction. The actual ZIP passed; a tiny harmless extra-member fixture was refused. |
| Final process delta | Only fixed /bin/ps numeric PID output is read. SID/PGID membership is checked before signalling, IDs <=1 and the caller's own group/session are refused, and another-session control is preserved. No process-name/argv/environment scan, IPC broker, pre-exec hook or watcher was added. |

The process code and all five new regression files were read. Launcher grace remains ten seconds by default, followed by a fixed ten-second forced verification budget and bounded active-PID-probe cleanup. Repeated interrupts do not reset these deadlines. Wait/communicate protection uses at most 0.1-second slices under the original deadline; PID queries and exact probe cleanup use bounded 0.25-second periods. Inspection failure prevents a successful settled receipt. Current exact source is bound by the frozen hashes above.

## Fresh automated and manual execution

Required unchanged-source baseline: **23 passed in 0.08s, exit 0**. [Output](review-security/pytest.txt).

~~~sh
env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 \
  UV_CACHE_DIR=/tmp/logopia-review-security-080/uv-cache \
  PYTEST_ADDOPTS='-p no:cacheprovider' \
  /usr/bin/perl -e 'alarm 120; exec @ARGV' \
  uv run --locked pytest -q \
  tests/hermes/test_installer.py tests/hermes/test_host_requests.py \
  --basetemp /tmp/logopia-review-security-080/pytest
~~~

Two owned typed drivers used the same offline environment, PYTHONPATH=integrations/hermes and a 120-second outer deadline:

~~~sh
uv run --locked python /tmp/logopia-review-security-080/audit_public.py
uv run --locked python /tmp/logopia-review-security-080/probe_boundaries.py
uv run --locked ruff check --no-cache --config pyproject.toml /tmp/logopia-review-security-080/audit_public.py /tmp/logopia-review-security-080/probe_boundaries.py
uv run --locked basedpyright --project pyproject.toml /tmp/logopia-review-security-080/audit_public.py /tmp/logopia-review-security-080/probe_boundaries.py
~~~

[Public audit](review-security/public-audit-final.txt), [boundary observations](review-security/boundaries.txt), [Ruff](review-security/ruff-final.txt) and [zero-error types](review-security/types-final.txt) passed. Scripts were removed after [hash capture](review-security/driver-hashes.txt).

Original installer replay, unchanged bytes, both cases together after code-ready:

~~~sh
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=integrations/hermes \
  PYTEST_ADDOPTS='-p no:cacheprovider' /usr/bin/perl -e 'alarm 30; exec @ARGV' \
  .venv/bin/python -B -m pytest -q -s -c pyproject.toml \
  /tmp/logopia-review-security-080/first_rename_probe.py \
  --basetemp /tmp/logopia-review-security-080/first-rename-fixed
~~~

Before the fix, this command used -k control and -k interrupt separately with their respective first-rename-control and first-rename-interrupt basetemps. Control: 1 pass in 0.07s/exit 0; interruption: 1 failure in 0.16s/exit 1. Final: 2 pass in 0.11s/exit 0. Source, canonical and four protected hashes matched before/after. [Exact post-run check](review-security/first-rename-fixed-pin-check.txt).

Actual required HTTP channel, using only a scratch mirror of the already verified public JSON:

~~~sh
.venv/bin/python -B -m http.server 8815 --bind 127.0.0.1 --directory /tmp/logopia-review-security-080/public
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8815/docs/hermes-demo/example.json
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8815/docs/hermes-demo/missing.json
~~~

The server had a 120-second outer alarm. Both curl exits were 0, independently distinguished from HTTP status:

- [Example](review-security/http-example.response): **200**, application/json, **38,785-byte body**, exactly equal by cmp to the allowlisted public record; SHA-256 415184581278b1317132c6c380b5255081bb9146dd02db9a1e227f67b4c624fe.
- [Missing file](review-security/http-missing.response): **404**, ordinary 335-byte error, with no local cache/auth/session/reasoning content.
- All five public originals matched canonical bytes. The actual ZIP SHA-256 is 0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04, with exactly PNG/manifest/guide. The HTML-embedded ZIP matched it. Fourteen public files and seven text files were checked.

HTTP, Chrome and native image generation were not repeated after the narrow fixes. The unchanged public/canonical pins preserve the applicability of that evidence.

## All nine adversarial classes

| Class | Concrete result and evidence boundary |
| --- | --- |
| 1. Malformed input | Fresh PASS: required 23 tests plus duplicate JSON keys, boolean revision, extra root field, >32 KiB input, non-PNG and incomplete receipt fixtures; intended typed failures in boundaries.txt. |
| 2. Instruction-like brief/feedback | Fresh PASS: harmless quoted wording round-trips as exact JSON/query data and never enters command argv; Korean/space-containing paths remain one argument. This is not a universal claim about provider prompt-injection resistance. |
| 3. Cancel/resume | Fresh no-inference engine fixture stays cancelled across repeated produce calls. The original installer interruption now restores exact bytes. Actual critique-only native continuation is attributed to native-run.md; no new image was generated here. |
| 4. Stale state | Fresh PASS: stale Store.expect and wrong candidate digest fail with unchanged scratch state. Reviewed late-return/CAS and unknown-job logic preserves the exact recorded intent and newer choice. |
| 5. Dirty worktree / foreign data | Fresh foreign-file/symlink preservation checks pass; the independent first-rename RED is resolved. Final 204 unchanged pins plus six authorized edits and seven additions preserve the four unrelated drafts and real demo. |
| 6. Hung/long commands | Fresh owned sleep times out after 1s/0.2s grace, exits -2 and is reaped. Final descendant/session, forced-bound and inspection-failure results are attributed to the process reviewers' bounded tests and manual receipts, not rerun here. |
| 7. Flaky tests / timing | No flake occurred in this review's required baseline. Root's later acquisition timing failure was retained and converted to deterministic SIGINT RED/GREEN on both runtimes. No repeat-until-green claim, hidden retry or weakened assertion is used. |
| 8. Misleading success | Fresh missing-image success receipt, wrong digest and extra ZIP member are refused. Curl status/body and exact real package were checked separately from exit 0. Process receipts require settlement or an explicit failure; installation interruption cannot return success. |
| 9. Repeated interruptions | Fresh engine fixture completes three cancel/produce cycles with zero jobs. Final actual two-Ctrl-C, first-exception identity, no ResourceWarning and subsequent exact stdout are attributed to the source-bound process manual record. |

N/A boundaries are narrow: no third-party target, live model adversarial experiment, new native cancellation/image retry, fresh browser context or upstream dependency-vulnerability survey was authorized or needed. [Original boundary output](review-security/boundaries.txt), [final manual process record](fix-process-integration/manual-joined.txt), [native evidence](native-run.md).

## First failures, attribution and cleanup

All first failures and the original pre-fix review remain in [review history](review-security/review-history.md). A preliminary public-key query assumed critiques instead of reviews; temporary-driver Ruff/type issues were corrected without production edits or weakened assertions. The first-rename driver's six S101 findings reflected its scratch location outside the existing test-path exception; identical bytes pass under the existing test policy via Ruff --stdin-filename tests/hermes/test_review_security_first_rename.py. Its typecheck had zero errors. A preliminary final-binding query assumed a files member; enumerating the actual managed_records established the verified 61-file count. No result relied on the missing field. Necessary metadata/privacy-comment hooks were acknowledged; first diagnostics remain.

The original **907 tests in 270.93s**, repository static/458-file-format checks, native doctor and Chrome evidence belong to [integration.md](integration.md) and its linked artifacts. The subsequent installer 42-test and process 39-test runs, dual-runtime probes and actual manual work are other workers' evidence. They are not represented as new tests performed here. The final **957-test** result supersedes the earlier whole-suite result for current source and preserves the first integrated failure as historical evidence. The seven private native session exports were never opened by this reviewer.

[Final cleanup receipt](review-security/final-cleanup.json) is PASS. Resource TODOs were written before each scratch/script/server/fixture started and retained in review-history.md. Initial 3.2 MiB scratch, both drivers, basetemp/cache, public mirror and bounded fixtures were inventoried and removed. The later 36 KiB first-rename RED root and unchanged GREEN replay root were also removed; their separate cleanup receipts remain. Final read-only binding created no temporary resources.

The original HTTP server PID 23637/session 25070 exited 0 after Ctrl-C; exact PIDs 23637, 20743 and 23741 were absent at their teardown. TCP 8815 is still free and /tmp/logopia-review-security-080 is absent in the final check. [Final absence status](review-security/final-cleanup-check.exit), [original server log](review-security/http-server.log), [original PID absence](review-security/owned-processes-after.txt), [RED cleanup](review-security/first-rename-cleanup.json), [GREEN cleanup](review-security/first-rename-fixed-cleanup.json). No other worker's resource or user browser was stopped.

Only this report and sanitized review-security artifacts were authored. No native call, credential copy, source/configuration edit, artwork transformation, commit, push or release was performed. All review requirements and owned cleanup are complete; publication remains root-owned.
