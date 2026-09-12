# T2 icon gallery evidence

Task `task_0fd9a9daba8f`, dispatch `ctx_e70cfbdfe235`, 2026-09-13 KST.

## Result and scope

Completed the dedicated portable renderer, CSS controls, exact original/prompt
publication, typed manifest, and rollback verification. Public API:
`render_app_icon_gallery(store, state, artifact_ids, output_relative) -> GalleryResult`.
The core owner's actual `AppIconIntent` and `Artifact.app_icon` are integrated.
The supplied session is an explicit revision snapshot: a concurrent writer may
advance persisted state, and the gallery neither replaces nor rewrites that state.

The finalized twelve decisions were read before edits. Existing color/sample
galleries, sample assets and historical color-workflow gates remain untouched.
No native calls, child workers, commits, pushes or releases were made by T2.
Integrated Chrome/file-URL interaction and native samples remain T5/T4 work;
HTTP evidence below is not represented as browser interaction or visual approval.

## Baseline, RED and GREEN receipts

Before source changes:

```text
uv run --locked pytest -q tests/test_color_gallery.py tests/test_delivery_guide.py tests/test_color_export_compatibility.py tests/test_transactions.py tests/test_reserved_output.py
64 passed in 45.02s
Independent saved baseline receipt: 64 passed in 49.66s

uv run --locked pytest -q tests/test_app_icon_gallery.py tests/test_app_icon_delivery.py
2 failed in 0.07s
```

The RED assertions were missing dedicated `logo_helper.app_icon_gallery` module
and missing `Manifest.app_icon`; neither failure was a missing dependency import.
The tests also require `artwork_limitations`. After the core models became
available, the first complete new suite passed 36 tests in 8.77s. Adding concurrent
state verification and separating the collision case produced the final receipts:

```text
uv run --locked pytest -q tests/test_app_icon_gallery.py tests/test_app_icon_delivery.py tests/test_color_gallery.py tests/test_delivery_guide.py tests/test_color_export_compatibility.py tests/test_transactions.py tests/test_reserved_output.py
101 passed in 94.51s

uv run --locked pytest -q tests/test_app_icon_gallery.py tests/test_app_icon_delivery.py
37 passed in 10.95s
```

The focused cases cover original byte equality, exact UTF-8/CRLF prompt equality,
explicit order, same-artifact intent and dimensions, unselected/unreviewed access,
non-square and partial-alpha variance preservation, malicious display metadata,
empty/duplicate/missing/non-icon IDs, reserved/escaping paths, leaf/ancestor/source
symlinks, collisions, missing/tampered files, stale image facts and state advances.

## Actual CLI and HTTP fixture

Registered task workspace `/tmp/logo-icons-t2-http.GhYWXX`; synthetic 96 x 64 PNG
with one partially transparent pixel and color variation. It is explicitly a QA
fixture, not a native sample. Actual commands used the core owner's CLI:

```sh
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace /tmp/logo-icons-t2-http.GhYWXX init --session fixture --brief /tmp/logo-icons-t2-http.GhYWXX/brief.json
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace /tmp/logo-icons-t2-http.GhYWXX import --session fixture --artifact original --revision 0 --image /tmp/logo-icons-t2-http.GhYWXX/synthetic-original.png --prompt-file /tmp/logo-icons-t2-http.GhYWXX/prompt.txt
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace /tmp/logo-icons-t2-http.GhYWXX icon-gallery --session fixture --artifacts original --output gallery
```

All exited zero. The renderer returned `gallery/index.html` with artifact
`original`, without selection or review. Port 8768 had no listener before start.
Registered server PID `49455`, exec session `52327`:

```sh
uv run --locked python -m http.server 8768 --bind 127.0.0.1 --directory /tmp/logo-icons-t2-http.GhYWXX/gallery
curl -i --fail --connect-timeout 2 --max-time 10 http://127.0.0.1:8768/index.html -o /tmp/logo-icons-t2-http.GhYWXX/http-index.txt
curl --fail --silent --show-error --connect-timeout 2 --max-time 10 http://127.0.0.1:8768/images/original.png -o /tmp/logo-icons-t2-http.GhYWXX/download.png
curl --fail --silent --show-error --connect-timeout 2 --max-time 10 http://127.0.0.1:8768/prompts/original.txt -o /tmp/logo-icons-t2-http.GhYWXX/download-prompt.txt
```

Observed receipt at 2026-09-12 17:04:12 UTC:

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sat, 12 Sep 2026 17:04:12 GMT
Content-type: text/html
Content-Length: 11074
Last-Modified: Sat, 12 Sep 2026 17:03:36 GMT
```

The response body was byte-equal to saved `index.html`. All fifteen radio IDs,
reset control and original/prompt relative references matched the saved output;
there was no executable script or network dependency. PNG dimensions remained
96 x 64. Original, gallery and downloaded PNG all had SHA-256
`6cedf06b5ce67e89df6759e14f4ac438d3e7931b4f5223cbe6a1ca9a77636c20`.
The input, gallery and downloaded prompt all had SHA-256
`06b310fe989b6094a8c45e5ed2c03a4cc09aff923e85ac63fefe046cd5595e1b`.
Both matched their manifest fields. HTTP HTML SHA-256:
`a46cafcc652fe8ad858989addf156c1f304827c3c8d9388907fe96109d8f3dab`.

Supplementary actual CLI probes all exited 1 with the expected errors and
unchanged session bytes: duplicate IDs `invalid_selection`, missing ID
`not_found`, `../escape` destination `unsafe_path`, existing gallery `conflict`.
The completed probe's state hash was
`14a0396c7e13480dd35ccbb357cb8b581293a6bfe57ac9726f7d2b6cdbcdaaa1`.
One earlier supplementary probe was interrupted when scratch cleanup started
before its shell session finished; after the first two successful cases its
assertion failed. The fixture was reconstructed and all four cases were rerun
successfully, awaiting process exit before final cleanup. This was a QA harness
ordering error, not an application failure or hidden passing receipt.

## Adversarial observations

| Class | Executed observation |
| --- | --- |
| Malformed input | Empty/duplicate/non-icon/missing selections, reserved/escaping paths, stale facts and tampered originals reject without partial publication. CLI duplicate/missing/path probes also failed as expected. |
| Prompt injection | Script/attribute/template text remains escaped; exact hostile prompt is a separate text download. Served HTML contains no executable script. No model-level injection-immunity claim. |
| Cancel/resume | KeyboardInterrupt injected before final index publication twice; owned output removed each time; a subsequent normal publication succeeds. |
| Stale state | A real Store.save advances revision and selection during publication; manifest retains requested old revision/ID while the writer's new state remains. Stale export revision is separately rejected. |
| Dirty worktree | The tree began dirty with research/plan/QA files and accumulated parallel core/docs edits. Only T2-owned files were edited; no reset, checkout, commit or revert occurred. |
| Hung commands | HTTP requests used explicit connect and total timeouts; CLI subprocesses used 20-second bounds. Shutdown health probe failed promptly with curl exit 7. No spontaneous application hang was observed. |
| Flaky tests | Initial, combined and final focused suites passed; failure injections are deterministic. The supplementary QA cleanup race above was observed, corrected and explicitly rerun. |
| Misleading success | HTML existence alone is never sufficient: HTTP 200, body equality, control/reference checks and download/manifest hash equality were asserted. Incomplete publication has no index; export gates remain checked. |
| Repeated interruptions | Both synthetic disk and keyboard interruptions were attempted twice, followed by successful resume; unrelated foreign files survived rollback. No native call/unknown receipt is retried by this task. |

## Static checks, review and cleanup

Ruff check: `All checks passed!`; Ruff format check: `6 files already formatted`.
Basedpyright on the six owned Python files: `0 errors, 0 warnings, 0 notes`.
LSP error diagnostics for each of the same six files: `No diagnostics found`.
Programming skill no-excuse checker: `no violations in 6 file(s)`.
The checker has no `--help` flag; the initial help probe exited 2, then the actual
file-list invocation above exited zero. Substantive LOC: gallery 113, publication
50, icon guide 23, delivery 162, gallery tests 247, delivery tests 193.

A local review checked the exact plan, complete owned code, caller integration,
legacy delivery diff and related history (`b391ca8`, `04e10ac`). No existing export
gate changed. The review-work skill's five-agent phase was not run because the
dispatch explicitly forbids children; the coordinator owns independent F1–F4
reviews. No independent-review verdict is claimed here.

Server PID 49455 was terminated with SIGTERM after HTTP checks; its process exited
143 and recorded three GET 200 responses. `lsof` then found no listener and a
bounded curl to 8768 failed with exit 7. The temporary workspace, downloaded
copies, `/tmp/logo-icons-t2-orchestration-guide.txt`, and
`/tmp/logo-icons-t2-baseline.txt` were removed. Final cleanup also removes the
reconstructed supplementary fixture after its probe completed. No task server,
port, child process or fixture is intentionally retained.

## Source receipt

| File | SHA-256 |
| --- | --- |
| app_icon_gallery.py | `71a2a7873af195cdeefe312f6d0462552fd1bb8856c117b5a20349649371e43f` |
| app_icon_publish.py | `fb4dea5c484a4c617e898626d324a1aed5335e7b853299f45827d15d8a652ae5` |
| app_icon_guide.py | `c063bf22bbcfa82c982caa2c066db2b069b34f8d633ba3f6afdb1e9d4fd17012` |
| delivery.py | `ed3713421b316e43568641451f41fc5a71332608acc8b8b2bf6c1db6f4469859` |
| app-icon-gallery.template.html | `960c682d45807c8a7f1a0dfb5f031f6a17f3fb6d4ca0c84501514375bd8cb9dd` |
| test_app_icon_gallery.py | `b8dd4d265a753048d5b342b6d99e6099669e78f8b795390a8f89a2e44964a833` |
| test_app_icon_delivery.py | `90fc8d5693de59cf4c2c8e0ab267d0db145f8066d01090c93c87067ca46d3035` |
