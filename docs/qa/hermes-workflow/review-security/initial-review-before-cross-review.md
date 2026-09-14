# Security review: Logopia 0.8.0

**PASS. No blocking security findings.** Confidence is high for the inspected local request, execution, storage, installation and public-delivery boundaries. This is a read-only review against f7dd3268313d2422b87efea63eef8257b0e651b9; HEAD remained at that commit.

No Critical, High or Medium finding requires a source change. The public sample is an exact allowlisted projection of **r47 / delivered / e2**, with five unchanged original PNGs and the actual delivery ZIP. No private native session export, reasoning, authentication cache or credential value was published by this review.

Two observations are informational, not blockers:

- The native local gallery intentionally saves the full workflow, including prompts and native receipt paths, through gallery.py:25. It is private local output. The reviewed public docs/hermes-demo record is a separate projection; its 14-file allowlist contains no native workflow/session dump.
- Instruction-like wording is carried as data and has no command/settings authority. This does not establish that every possible natural-language instruction will be ignored by every provider. Existing dependency locks were preserved; this was not a new upstream vulnerability survey or a real-model quality benchmark.

## Completed review plan

1. Pinned 210 source, sample, canonical/receipt and protected files before probes; all baseline hashes matched.
2. Read full trust-boundary modules, adjacent core/launcher/helper code and defensive test scenarios, including untracked implementation files.
3. Ran the required unchanged-source test modules once: 23 passed in 0.08 seconds, exit 0.
4. Verified the exact public projection, originals/delivery, benign boundary fixtures and real HTTP 200/404 responses.
5. Rechecked pins and inventories, accounted for all nine scenario classes, removed exact owned resources and completed this report.

No production edit, native inference, installation/configuration write, source artwork transformation, commit, push or release occurred. Earlier 907-test/native evidence is attributed below. Publication is coordinator-owned T6, and its pending status is not an implementation defect.

## Requirements and boundary findings

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

## Resource ledger: registered before creation, now closed

Each TODO below was written before its resource started. All temporary entries are closed; only the retained evidence directory remains intentionally.

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

The previously completed **907 tests in 270.93s**, repository Ruff/type/458-file-format checks and actual native doctor belong to [integration.md](integration.md). The real c1 → e1 → e2 chain, first native 420-second timeout and explicit critique-only recovery belong to [native-run.md](native-run.md). Those seven private session exports were not opened here; canonical structured state, exact artwork/package and bounded binding metadata were sufficient. No human-expertise or measured aesthetic-superiority claim is made.

## Actual cleanup receipt

[cleanup.json](review-security/cleanup.json) records teardown. The inventoried **3.2 MiB** scratch root, both drivers, fixture workspaces/copies, pytest basetemp, uv cache, public HTTP mirror and temporary receipts were removed using only rm -r /tmp/logopia-review-security-080. The exact root was then checked absent.

Server PID **23637**, session **25070**, exited **0** after Ctrl-C. lsof on TCP 8815 returned no listener (exit 1); ps for exact PIDs 23637, 20743 and 23741 returned no process (exit 1). [Server receipt](review-security/http-server.log), [port absence](review-security/port-after.txt), [process absence](review-security/owned-processes-after.txt) and [removed inventory](review-security/cleanup-inventory.txt) remain.

All **210 pins** still match and the final inventory is identical. Three default/named/settings configuration pins match; all 59 installed records and 58 corresponding source records match. HEAD is unchanged, the index has zero staged changes, and the real demo remains **r47 / delivered / e2**. No owned browser, tmux session or child remains; no other worker's resource was stopped. Only this report and sanitized review-security evidence are retained. No review-owned work remains outstanding.
