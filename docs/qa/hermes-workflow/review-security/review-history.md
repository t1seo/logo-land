# Security review: Logopia 0.8.0

**PENDING FIXES_READY; high confidence in the recorded local observations.** The original installer control and first-rename SIGINT pair now independently PASS on frozen installer 8f75ba7f123f2550d405f4015de54319453b867044f635e0c7d3ed4b4de02116. Root reports another process-interruption timing failure, so final process/source and installed binding remain pending. Final verdict and worker_done are held for the named dependency. This is a read-only review against f7dd3268313d2422b87efea63eef8257b0e651b9.

The initial narrow PASS record is preserved in review-security/initial-review-before-cross-review.md and is superseded by this pending review. Message msg_9fbd8af00b45 reports independent GREEN for the original 3+2 probes and accepts the installer fix after 29 tests and dual-runtime actual SIGINT/cleanup. It also records two further actual process failures: a nested helper in a new session surviving forced launcher exit, and Popen context cleanup exceeding the forced-settlement deadline. The process owner is correcting both; final source freeze and installed binding remain pending. Public sample checks still bind **r47 / delivered / e2**; no private native session export, reasoning, authentication cache or credential value was published by this review.

Two observations are informational, not blockers:

- The native local gallery intentionally saves the full workflow, including prompts and native receipt paths, through gallery.py:25. It is private local output. The reviewed public docs/hermes-demo record is a separate projection; its 14-file allowlist contains no native workflow/session dump.
- Instruction-like wording is carried as data and has no command/settings authority. This does not establish that every possible natural-language instruction will be ignored by every provider. Existing dependency locks were preserved; this was not a new upstream vulnerability survey or a real-model quality benchmark.

## Completed review plan

1. Pinned 210 source, sample, canonical/receipt and protected files before probes; all baseline hashes matched.
2. Read full trust-boundary modules, adjacent core/launcher/helper code and defensive test scenarios, including untracked implementation files.
3. Ran the required unchanged-source test modules once: 23 passed in 0.08 seconds, exit 0.
4. Verified the exact public projection, originals/delivery, benign boundary fixtures and real HTTP 200/404 responses.
5. Original pins/inventories and cleanup complete; IN PROGRESS: wait for FIXES_READY, inspect the authorized three-module delta and regression evidence, then rebind source/protected hashes and finalize.

No production edit, native inference, installation/configuration write, source artwork transformation, commit, push or release was performed by this reviewer. Coordinator-routed workers now own changes to launcher_process.py, helper_process.py, installer.py, the announced shared process_group.py and dedicated regression tests. Message msg_88c147d3d748 also authorizes native-run.md's precision correction: original PNG bytes remain identical, while prior job records are compared after optional retry_of:null default normalization, not as raw JSON bytes. Earlier 907-test/native evidence is attributed below. Publication is coordinator-owned T6; its pending status is not the blocker.

## Original scenario results, pending corrective-delta review

### Resolved independent blocker: first-rename interruption

**Independent GREEN after code-ready:** the exact original driver bytes were restored from the retained reproduction and run once without selector or assertion changes. Both original cases passed in 0.11s, exit 0, under the same 30-second outer deadline. Actual SIGINT now reports target_exists=true, prior_bytes_preserved=true, actual_backup_bytes_match=[true] and only logopia-studio remaining in the plugin directory. The normal update also passed. [Exact output](review-security/first-rename-fixed.txt), [fixed source/protected pins](review-security/first-rename-fixed-pin.sha256), [post-run pin checks](review-security/first-rename-fixed-pin-check.txt) and [actual cleanup receipt](review-security/first-rename-fixed-cleanup.json) bind this result. Only the owned script and pytest fixture root were recreated, inventoried and removed; exact scratch absence was verified. No native call, broad test rerun or profile mutation occurred. Root instructions msg_0d89537b7517 keep the final process/source binding pending.

**Major / blocking.** After the real target-to-backup rename completes, a real SIGINT raises KeyboardInterrupt before the current rollback try block is entered. Observed exact backup bytes match, but unwind leaves target_exists=false, prior_bytes_preserved=false and remaining_plugin_entries=[]: the previous managed installation is deleted. This is an actual local filesystem fixture, with no real profile or native operation. A normal update on the unchanged accepted installer passed first (1 passed in 0.07s, exit 0); the interruption then failed (1 failed in 0.16s, exit 1). Escalated as msg_977fa4ddb4d1; no source fix was made by this reviewer.

[Exact reproduction](review-security/first-rename-probe.py.txt), [passing control](review-security/first-rename-control.txt), [first failure](review-security/first-rename-interrupt.txt), [source snapshot](review-security/installer-first-rename-before.py.txt) and [unchanged source/protected pins](review-security/first-rename-pin-check.txt) preserve the evidence. H1 matches the observed boundary; H2 is refuted by passing normal update and exact backup bytes; H3 is refuted by the empty plugin directory after unwind. Required resolution is exact old-byte preservation across this first rename, with existing publication/foreign-data guards retained. Root message msg_93b6a9bc9c69 reports an independent matching goal-review failure and routes task_8aa6c56bce98 to installer.py and a new test_installer_backup_interrupt.py; the publication-interruption regression may be strengthened to preserve the old backup on restoration failure or an occupied target. Normal refusal/recovery must still leave no temporary debris. Exact unchanged-probe replay is authorized after code-ready; source-level correction remains with that fix owner.

Exact control and failure command (run separately with the respective selector/basetemp):

~~~sh
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=integrations/hermes \
  PYTEST_ADDOPTS='-p no:cacheprovider' /usr/bin/perl -e 'alarm 30; exec @ARGV' \
  .venv/bin/python -B -m pytest -q -s -c pyproject.toml \
  /tmp/logopia-review-security-080/first_rename_probe.py -k control \
  --basetemp /tmp/logopia-review-security-080/first-rename-control
# Failure used -k interrupt and --basetemp /tmp/logopia-review-security-080/first-rename-interrupt
~~~

The coordinator's messages msg_0301a184f046 and msg_6e64fa261a81 route these four **Major/blocking** defects to separate fix owners. This reviewer read the original bounded reproduction code, failures and passing controls; these are attributed independent failures, not new reproductions here.

| Finding | Exact observed failure | Required final evidence |
| --- | --- | --- |
| Installer interrupt rollback | Previous plugin disappears when KeyboardInterrupt occurs after the old-target rename; the PermissionError control preserves it. | Same interruption/control regressions pass and previous bytes survive. |
| Launcher descendant settlement | Timeout receipt returns while same-group descendant PID 19778 is still sleeping, PPID 1. | Remaining owned descendants settle before receipt/profile unlock, without signaling unrelated processes. |
| Helper interruption | KeyboardInterrupt propagates while the new-session helper PID 19859 remains alive; a ResourceWarning is observed. | Helper interruption settles its own group before propagation. |
| Nested foreign marker | An ordinary foreign file is refused, but user-notes/.logopia-install.json is incorrectly exempted and deleted by update. | Only the exact root ownership marker is exempt; nested foreign bytes survive. |

Original evidence: [three bounded failures](review-code/defensive-tests.txt), [installer rollback/control](review-code/install-rollback-tests.txt), [initial probe](review-code/defensive-probes.py.txt), [rollback probe](review-code/install-rollback-probe.py.txt), and [code review](review-code.md). Both surviving fixture processes were cleaned by their owner. These findings override the original narrower PASS observations in the table below until FIXES_READY is validated.

| Requirement | Result and concrete evidence |
| --- | --- |
| G1: supported runtime and locked helper | PASS. Native declarations retain Pydantic >=2.12,<3 and Pillow >=11.2,<13. [HelperBridge](../../../integrations/hermes/logopia_studio/helper.py) builds the specified locked uv/helper argv. Native modules and adjacent helper transport/export code were read. Python 3.11 native doctor evidence is attributed to [integration.md](integration.md), not rerun here. |
| G2/G7: bounded calls and recovery | PASS. [Process runner](../../../integrations/hermes/logopia_studio/launcher_process.py) uses literal argv, its own process group and finite waits. A real owned sleeping child timed out and was reaped. [Recovery](../../../integrations/hermes/logopia_studio/engine_recovery.py) permits only the exact eligible unknown critique; retry links, CAS reservation and late-return fences were read in full. New fixture cancellation checks produced no jobs across three cycles. Actual native critique recovery is attributed to [native-run.md](native-run.md). |
| G3: exact import/export and foreign data | PASS. Import verifies deterministic artifact, prompt, parent, requested background and bytes. Delivery checks the committed export record and actual manifest/PNG/ZIP. [Installer](../../../integrations/hermes/logopia_studio/installer.py) refuses unmanaged/changed files and source symlinks; all five installer tests passed. [Gallery writer](../../../integrations/hermes/logopia_studio/gallery_files.py) reserves fresh output and rolls back recorded owned files. Foreign-file interruption tests were read, not newly rerun. |
| G4: bound critique evidence | PASS. Core checks original, parent and target-view digests, two unique roles/call IDs and five unique criteria. Actual originals and delivery passed original_bytes and the public delivery_files validator. A benign in-memory wrong digest produced gallery_source. e1 retains both failed preservation observations; e2 has its two fresh all-pass reports. |
| G5/G6: strict input and immutable intent | PASS. [Tool schemas](../../../integrations/hermes/logopia_studio/host_requests.py), [file parser](../../../integrations/hermes/logopia_studio/launcher_requests.py) and feedback checks reject extras, boolean/string revisions, missing fields, duplicate JSON keys, oversized bytes and incompatible strict color policy. Model arguments cannot supply workspace, helper path, command or provider/model settings. Required tests and new bounded fixtures passed. |
| Trusted settings and authentication | PASS. Strict installed-local settings supply the roots. Native transport uses only the public structured-completion facade and image_generate dispatcher. No raw provider HTTP/auth implementation or credential-copy operation was found. Default config, named config and installed settings hashes stayed unchanged. The broad source search's one hit was the ordinary docstring word “requests.”, not an HTTP client. |
| Containment and symlinks | PASS for the local boundary. [safe_path/read_file](../../../integrations/hermes/logopia_studio/store_files.py) reject traversal, symlinks and nonregular/oversized managed inputs; candidate paths are deterministic. New benign traversal, symlink and text-as-PNG fixtures failed with intended typed errors and preserved target bytes. Trusted user-selected roots and malicious concurrent filesystem replacement are not claimed to be sandboxed by this desktop integration. |
| Escaped DOM and offline behavior | PASS by full source review and attributed browser evidence. Prose uses html.escape; embedded JSON escapes angle-bracket/ampersand and line-separator characters. UI writes use textContent/form values; IDs/digests have safe strict grammars. Native CSP denies network connections. Actual public HTML has no script, iframe, object or embed; its embedded ZIP exactly matches the standalone ZIP. Browser interaction evidence belongs to [public-sample.md](public-sample.md). |
| Bounded ZIP parsing | PASS. [Public delivery validator](../../../integrations/hermes/logopia_studio/gallery_delivery.py) verifies exactly three unique names, sizes, regular-file attributes, encryption/compression policy and bounded reads without extraction. The actual package passed. A scratch package with one small harmless optional-readme.txt member failed with gallery_delivery through the public validator. Scratch original copies were byte-identical. |
| Lockfile and installed payload | PASS. [Exact lock diff](review-security/lockfile.diff) changes only root logo-land-helper from 0.7.0 to 0.8.0; all other package records and hashes are unchanged. Independently verified all **59 installed records**, including settings, and **58 source records** against this checkout. No install, dependency download or config mutation was needed. |
| Public/staged privacy and dirty worktree | PASS. Every nested field group in the public record is allowlisted and matches the canonical projection. Seven public text files have zero private markers; original/package comparisons pass. Index changes were empty before/after, and zero paths in output/ or .logo-generator/ are tracked. Future T6 staging is coordinator-owned. All 210 pins, including the four protected drafts, are unchanged; concurrent review artifacts were preserved. |

## New execution and exact commands

The required test run completed once: **23 passed in 0.08s, exit 0**. No test was deleted, weakened or retried to conceal a failure. [Output](review-security/pytest.txt).

~~~sh
env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 \
  UV_CACHE_DIR=/tmp/logopia-review-security-080/uv-cache \
  PYTEST_ADDOPTS='-p no:cacheprovider' \
  /usr/bin/perl -e 'alarm 120; exec @ARGV' \
  uv run --locked pytest -q \
  tests/hermes/test_installer.py tests/hermes/test_host_requests.py \
  --basetemp /tmp/logopia-review-security-080/pytest
~~~

The two owned drivers ran with the same offline uv/cache/bytecode environment, PYTHONPATH=integrations/hermes and a 120-second outer alarm:

~~~sh
uv run --locked python /tmp/logopia-review-security-080/audit_public.py
uv run --locked python /tmp/logopia-review-security-080/probe_boundaries.py
uv run --locked ruff check --no-cache --config pyproject.toml /tmp/logopia-review-security-080/audit_public.py /tmp/logopia-review-security-080/probe_boundaries.py
uv run --locked basedpyright --project pyproject.toml /tmp/logopia-review-security-080/audit_public.py /tmp/logopia-review-security-080/probe_boundaries.py
~~~

Final results: [public audit](review-security/public-audit-final.txt), [boundary observations](review-security/boundaries.txt), [Ruff PASS](review-security/ruff-final.txt), [types: 0 errors/warnings/notes](review-security/types-final.txt). Only these authored temporary scripts received new static checks; their [hashes](review-security/driver-hashes.txt) remain after deletion.

The real HTTP server served only the registered scratch mirror containing the verified public JSON, never the repository/private workflow root:

~~~sh
.venv/bin/python -B -m http.server 8815 --bind 127.0.0.1 --directory /tmp/logopia-review-security-080/public
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8815/docs/hermes-demo/example.json
curl -i --connect-timeout 2 --max-time 15 http://127.0.0.1:8815/docs/hermes-demo/missing.json
~~~

The server was also wrapped in the 120-second alarm. Both curl processes exited 0; HTTP status and body were checked separately:

- [Example response](review-security/http-example.response): **200**, application/json, **38,785 bytes**, body exactly equal by cmp to docs/hermes-demo/example.json; SHA-256 415184581278b1317132c6c380b5255081bb9146dd02db9a1e227f67b4c624fe.
- [Missing response](review-security/http-missing.response): **404**, ordinary 335-byte error body with no filesystem/cache/auth/session/reasoning disclosure.
- Actual ZIP SHA-256: 0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04. Exactly PNG, manifest and guide; no disk extraction. All five canonical/public originals matched.
- Canonical snapshot SHA-256: 16eea6dc8c32e979c432fbdffee137d76cb68a230aad9e5b65cc740d59e26e04. The logical job record remains exactly three initial image jobs and two edits; no new native call was made.

## All nine scenario classes

| Class | Result, execution boundary and artifact |
| --- | --- |
| 1. Malformed input | PASS, new execution: 23 required tests plus duplicate-key, boolean-revision, extra-directory-field, oversized-byte, non-PNG and incomplete-success-receipt fixtures. Intended invalid_request, invalid_png and invalid_receipt errors are in [boundaries.txt](review-security/boundaries.txt). |
| 2. Instruction-like brief/feedback | PASS, new execution: harmless quoted “ignore prior instructions” wording round-trips in exact JSON/query data and is absent from command argv. The Korean/space-containing query path stays one argv element. Exact feedback and host role separation are additionally attributed to [host.md](host.md) and [critique-resume.md](critique-resume.md); no live prompt-injection experiment occurred. |
| 3. Cancel/resume | PASS, new no-inference fixture: the real engine interrupts a scratch draft and repeated produce returns the saved cancellation. Positive native critique-only recovery is attributed to [native-run.md](native-run.md), with zero new images and preserved error; it was not repeated here. |
| 4. Stale state | PASS, new execution: stale Store.expect fails and scratch state bytes stay identical; wrong candidate digest fails original verification. Required tests reject inappropriate envelope shapes. [Boundary record](review-security/boundaries.txt). |
| 5. Dirty worktree | PASS, new execution: foreign/edited installer files and scratch symlink target survive. [Baseline pins](review-security/pin.sha256), [identical final inventory](review-security/pin-final.sha256) and [final checks](review-security/pin-final-check.txt) cover 210 files and all four protected drafts. No branch/worktree change. |
| 6. Hung/long commands | PASS, new execution: an owned sleep receives a one-second deadline/0.2-second grace, exits -2, and its exact PID is absent. Final child PID 23741; first driver child 20743 also settled. Native 420-second failure/1800-second settings are attributed evidence, not recreated. |
| 7. Flaky tests | No flaky product test observed: required tests passed once. First query/static-check harness failures are retained below. Repeat-until-green stress is N/A because no flaky product failure was observed and broad reruns were prohibited. |
| 8. Misleading success | PASS, new execution: success-shaped receipt without image/attribution, wrong PNG digest and extra ZIP member fail. Curl exit 0 is distinguished from HTTP status. Full launcher review confirms saved-state postconditions, rather than prose/exit 0, determine action success. Actual package bytes were checked. |
| 9. Repeated interruptions | PASS, new engine fixture: three interrupt/produce cycles stay cancelled with zero jobs. Actual double-Ctrl-C forced shutdown and unknown-image no-resubmission are attributed to [process.md](process.md) and [critique-resume.md](critique-resume.md). Another native interruption was not authorized. |

No fresh native execution, external target test, browser profile, provider cancellation experiment or image retry was required for this role. Prior evidence is not represented as new execution.

## Resource ledger: registered before creation

Installer code-ready replay TODO, before creation: message msg_0a2d075d8578 freezes installer SHA-256 8f75ba7f123f2550d405f4015de54319453b867044f635e0c7d3ed4b4de02116 and authorizes the unchanged original probe. Recreate only /tmp/logopia-review-security-080/ and copy the retained original bytes to first_rename_probe.py; create first-rename-fixed/ as the pytest basetemp. Capture installer/canonical/protected pins before and after; run both original cases once with a 30-second outer deadline, command-local bytecode/cache suppression and no native/profile operation. Retain exact output/exit/hash and remove the owned script/root immediately afterward. No new background process, server, browser, downloaded package or source edit is needed.

Reopened narrow review resource TODO, before creation: recreate only /tmp/logopia-review-security-080/ for an installer first-rename interruption probe, its single Python driver and pytest fixture root. Capture the accepted installer hash and protected hashes before this harmless local filesystem scenario; use a 30-second outer deadline, no native/profile configuration calls, retain the failure/control output and remove the exact resources after routing.

First-rename investigation journal: Python 3.12.12 from the existing project venv; unchanged installer SHA-256 768da32cdf90da78fd519a39b9b65bd3bdd4cf81c20dc4e45452ffc3e060708b. No debugger port or provider/configuration access is needed. Read debugging Python runtime, setup and investigation references; this owned report is the journal because root journal edits and nested agents are prohibited. H1: interruption after the real first rename bypasses rollback; distinguish exact backup bytes observed inside the rename wrapper from an absent target after unwind (routing: widen transaction). H2: fixture/stale source invalidates ownership before rename; distinguish a passing normal-update control and actual backup observation (routing: correct fixture). H3: temporary-directory cleanup retains the backup safely; distinguish retained plugin-directory entries and exact old bytes after interruption (routing: document recovery). Register first_rename_probe.py, its two pytest basetemps, command-local PYTHONPATH/PYTHONDONTWRITEBYTECODE/PYTEST_ADDOPTS and finite foreground pytest/static processes before creation; retain sanitized script/output/hash copies only, remove all scratch resources afterward.

Each TODO below was written before its resource started. The initial resources below and the reopened first-rename fixture are now closed. [First-rename cleanup](review-security/first-rename-cleanup.json) records the exact scratch removal/absence after saving byte-identical reproduction text, first outputs and the inventory; no background process, server, browser, native session or dependency download was created by that additional scenario.

| Registered resource | Final state |
| --- | --- |
| docs/qa/hermes-workflow/review-security/ | Retained sanitized receipts only |
| /tmp/logopia-review-security-080/ | Inventoried and removed; absence verified |
| pytest/ and uv-cache/; required pytest process | Process exit 0; basetemp/cache removed; offline/no cacheprovider/no bytecode |
| audit_public.py and probe_boundaries.py | 120-second bounds; final Ruff/types pass; hashes retained; scripts removed |
| fixtures/ text, symlink, scratch workflow and deadline logs | First fixture root removed before final run; final root removed after capture |
| fixtures/package-case/ | Exact e1/e2/source member copies and tiny extra-member ZIP; removed |
| public/docs/hermes-demo/example.json | Exact public mirror; removed |
| Loopback 127.0.0.1:8815, Python HTTP server | PID 23637, maximum 120 seconds, stopped/reaped, port free |
| Fixed PID-printing shell followed by exec /bin/sleep 30 | No user data in command; one-second timeout/0.2-second grace; both runs reaped |
| Temporary config/installed-file hashes and HTTP body/stderr | No credential contents copied; temporary receipts removed |

## First harness failures and attribution

A preliminary jq shape query assumed the public candidate field was critiques rather than reviews and reported “null (null) has no keys”. Enumerating actual keys resolved the query error; no source/data changed.

The [first Ruff check](review-security/ruff-first.txt) found 13 temporary-driver issues: executable mode, line length, output calls, import placement, temporary-root literal and loop binding. The [first typecheck](review-security/types-first.txt) found three: implicit concatenation, regex return typing and use of a private validator. Only the owned drivers changed. Output became explicit stdout writes, bindings/typing became precise, and the ZIP fixture used public delivery_files. Both final checks pass. Initial successful executions remain in [public-audit.txt](review-security/public-audit.txt) and [boundaries-first.txt](review-security/boundaries-first.txt). No failed behavior assertion was removed or relaxed.

Comment-checker notices involved required PEP 723 metadata, reproducible commands and the drivers' privacy/no-inference scope; each was acknowledged. A first report-writing tool wrapper had a JavaScript quoting syntax error before any filesystem operation; the literal document write was then corrected. The broad source-auth search's one match was an ordinary docstring word, checked against the full source.

The additional first-rename fixture's first Ruff run reported six S101 assertions because the scratch file sits outside the repository's existing tests/**/*.py exception. The identical file bytes passed using Ruff's --stdin-filename tests/hermes/test_review_security_first_rename.py with the existing project configuration; no ignore rule, test or assertion was changed. [First diagnostic](review-security/first-rename-ruff-first.txt), [final Ruff](review-security/first-rename-ruff-final.txt), [types: 0 errors/warnings/notes](review-security/first-rename-types-first.txt) and [identical driver hashes](review-security/first-rename-driver-hashes.txt) remain. The product failure is still recorded as FAIL, independently of successful script static checks and cleanup.

The previously completed **907 tests in 270.93s**, repository Ruff/type/458-file-format checks and actual native doctor belong to [integration.md](integration.md). The real c1 → e1 → e2 chain, first native 420-second timeout and explicit critique-only recovery belong to [native-run.md](native-run.md). Those seven private session exports were not opened here; canonical structured state, exact artwork/package and bounded binding metadata were sufficient. No human-expertise or measured aesthetic-superiority claim is made.

## Actual cleanup receipt

[cleanup.json](review-security/cleanup.json) records teardown. The inventoried **3.2 MiB** scratch root, both drivers, fixture workspaces/copies, pytest basetemp, uv cache, public HTTP mirror and temporary receipts were removed using only rm -r /tmp/logopia-review-security-080. The exact root was then checked absent.

Server PID **23637**, session **25070**, exited **0** after Ctrl-C. lsof on TCP 8815 returned no listener (exit 1); ps for exact PIDs 23637, 20743 and 23741 returned no process (exit 1). [Server receipt](review-security/http-server.log), [port absence](review-security/port-after.txt), [process absence](review-security/owned-processes-after.txt) and [removed inventory](review-security/cleanup-inventory.txt) remain.

At completion of the original scenarios, all **210 pins** matched and the inventory was identical. Three configuration pins and all 59 installed records/58 source counterparts also matched. Those are pre-fix receipts, retained without rewriting their meaning. HEAD was unchanged, the index had zero staged changes, and the real demo remained **r47 / delivered / e2**. No owned browser, tmux session or child remains; no other worker's resource was stopped. Only this report and sanitized review-security evidence are retained. Narrow corrective-delta review remains pending FIXES_READY; no final verdict or worker_done has been sent.
