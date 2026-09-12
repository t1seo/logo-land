# T1 state, compatibility, and lockup contracts

T1 implements the shared types, strict legacy reader, storage invariants, and dependency pin. The contract was published before implementation at [contracts.md](contracts.md); downstream workers were notified when it became available and when artifact immutability was strengthened. No CLI/prompt/delivery implementation, native image generation, font installation, release, or commit was performed by this worker.

## Delivered behavior

- Shared models are split by responsibility: primitives/errors (`model_base`), exact brand intent (`brief_models`), artifact provenance/reviews (`artifact_models`), color constraints/versions (`color_models`), references/ROI (`reference_models`), report evidence (`color_reports`), lockup intent (`lockup_models`), and session graph (`session_models`). Existing `logo_helper.models` import paths remain available.
- Structured HEX accepts only opaque #RGB/#RRGGBB and normalizes to uppercase six-digit sRGB. Normalized duplicates collapse, incompatible constraints fail with `constraint_conflict`, canonical palette content is SHA256-bound, and model/history mutations cannot replace earlier intent.
- `LockupIntent` records horizontal/stacked layout, start/end symbol position, text alignment, plain-language typography style, and optional requested font reference. Brief/artifact lockup fields default to null; exact lettering and slogans are unchanged. Inheritance and prompt wording belong to T4; generated raster font provenance is not asserted.
- Schema-1 models retain their original allowed fields. Schema-1 data is converted in memory to v2 without creating palettes, reports, or lockup claims. Boolean/float schema versions are rejected rather than being accepted through Python literal equality. Unknown fields/versions are rejected.
- `Store.load/list_sessions/expect` do not rewrite legacy bytes. First mutation writes and verifies `session.v1.backup.json` exclusively, then atomically commits v2. A failed state write may leave the verified backup for retry, but cannot replace v1 state or overwrite an existing backup. Palette/reference/report histories are append-only, and existing artifact provenance is immutable except for explicit review/reviewed_at.
- Original PNG hash/decoded-fact verification remains; referenced original bytes are hash-checked on resume. Cross-record validation binds report artifact hashes and palette ID/digests, palette reference evidence, ordered palette ancestry, managed paths, and active/selected IDs.
- ColorAide is pinned to 8.12.1 in pyproject/uv.lock and the PEP 723 header. No existing dependency was upgraded. Shared models/storage do not import the engine; [lazy-import evidence](t1-lazy-import.txt) confirms this and the installed version.

## Checks and evidence

| Check | Observed result | Evidence |
| --- | --- | --- |
| Existing pre-change baseline: background compatibility, transactions, boundaries | 39 passed | [baseline](t1-baseline.txt) |
| New contract tests before implementation | Collection failed because new model/legacy modules did not exist | [red](t1-red.txt) |
| Strict schema number regression | Boolean/float versions incorrectly accepted, then rejected after fix | [red](t1-strict-version-red.txt), [green](t1-strict-version-green.txt) |
| Retroactive artifact palette regression | Existing image could gain inferred palette intent, then blocked by immutable provenance validation | [red](t1-artifact-binding-red.txt), [final green](t1-green.txt) |
| Final T1 model and compatibility tests | 41 passed | [green](t1-green.txt) |
| Legacy edited lineage, selected image, existing export preservation | Passed | [history](t1-history.txt) |
| Owned Python Ruff + formatting | Passed; 13 files formatted | [Ruff](t1-owned-ruff.txt) |
| Owned Python strict basedpyright | 0 errors, 0 warnings, 0 notes | [types](t1-types.txt) |
| Programming rule scanner | No violations in 13 files | [code rules](t1-code-rules.txt) |
| Dependency lock consistency | Passed | [lock](t1-lock.txt) |
| Fresh parent-background prompt regression | 2 passed | [fresh background](t1-background-fresh.txt) |
| Fresh existing background compatibility + transactions | 15 passed | [existing fresh](t1-existing-fresh.txt) |

The final T1 commands were:

```sh
uv run --locked pytest tests/test_color_models.py tests/test_palette_compatibility.py
uv run --locked pytest tests/test_background_variants.py -k parent_background
uv run --locked pytest tests/test_background_compatibility.py tests/test_transactions.py
uv lock --check
```

Ruff/basedpyright/rule checks targeted the 11 owned shared Python modules plus the two owned test files. All source modules are below 200 pure lines; `test_color_models.py` is 213 pure lines, within the 250-line ceiling, with no further additions planned in T1.

## Actual CLI surface evidence

[CLI transcript](t1-cli.txt) contains real locked subprocess commands and assertions, using an explicitly synthetic 16×16 PNG fixture:

1. `init` produced schema 2; `import` recorded the original PNG bytes.
2. A schema-1 fixture preserved a free-text green brief, navy edit intent in its saved prompt, exact `모로  Studio` lettering, and missing per-artifact background intent.
3. `show`, `list`, and parent `prompt` preserved state bytes and created no backup.
4. `select` followed by `review` yielded v2 revision 3, kept the selection, original image hash and text, and retained an exact original v1 backup.
5. A copied scripts directory executed `uv run --offline --script ... show` successfully from outside the checkout using the already-prepared dependency cache. This is not a cold-cache offline installation claim.

No synthetic fixture or automated review boolean is native image QA evidence.

## Adversarial classes and integration observations

| Class | Coverage / outcome |
| --- | --- |
| Untrusted color/schema input | Invalid HEX, alpha/names/CSS expressions, unknown fields, wrong scalar types, future schema, locked/allowed/count/gradient conflicts rejected |
| Provenance and graph tampering | Duplicate IDs, missing palette parents, changed digest, invalid active palette, report hash/ID/digest shape, ROI/path mismatches, retroactive artifact palette assignment rejected |
| Storage durability and retry | Disk failure leaves v1 intact and exact backup reusable; unrelated existing backup is never overwritten; immutable histories cannot be removed |
| Existing filesystem/CLI boundaries | Pre-change 39-case baseline and broad legacy regression covered cooperative locks, path checks, corrupt PNGs, rollback, background defaults and exports |
| Measured evidence truth | Report records are typed and bound, but stored `pass` is not authorization; T5 must recompute from verified originals |
| Generated-image/font quality | Not performed; belongs to the coordinator's native-image and font/lockup sample QA |

Concurrent integration work was active throughout final broad testing:

- An early whole-repository collection stopped while T7 had not yet defined `render_color_gallery`: [snapshot](t1-suite.txt).
- A 136-case existing/T1 run had **134 pass, 2 fail** because the test process retained old `PromptResult` while the concurrently updated CLI returned new palette/lockup fields: [snapshot](t1-broad-concurrent.txt). Both affected cases passed in a fresh process: [confirmation](t1-background-fresh.txt).
- A subsequent 56-case run had **55 pass, 1 fail** because T5 changed the delivery manifest during that process, leaving its imported Manifest class stale: [snapshot](t1-focused-concurrent.txt). All 15 fresh background/transaction cases passed: [existing fresh](t1-existing-fresh.txt).
- A CLI-body import formatting warning appeared while T4 was editing `logo_project.py`; [snapshot](t1-ruff.txt) retains it. The only T1 edits in this shared file are its PEP 723 header, which passed its check before T4's body changes.

These snapshots are not claims that the integrated release passes. The coordinator owns final integration/reviewer checks. T4 was notified that new `Store.save` domain errors such as `backup_conflict`/`immutable_history` must participate in staging rollback, and that existing artifact palette/lockup intent cannot be reassigned.

## Review and cleanup

Self-review used the programming/review-work checklists. Each source module owns one model category; boundary data is parsed with strict frozen Pydantic types; schema/reference variants are exhaustively handled; there are no new Any/cast/ignore/broad-except escapes. Meaningful failing tests lock normalization, migration, schema strictness, and artifact intent immutability. Independent multi-agent review remains coordinator-owned under the explicit no-subagents instruction.

The manually created `/tmp/logo-land-t1.*` workspace, copied scripts, synthetic PNG and temporary Ruff scratch file were removed after verification. Pytest fixtures remain managed by pytest's normal temporary-directory lifecycle. Evidence logs and these two documents are intentional retained artifacts; no image masters, unrelated worker files, plan/Boulder/ledger, commits, or release metadata were altered by T1.
