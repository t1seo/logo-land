# T2 app-icon delivery evidence

Task `task_0fd9a9daba8f`, dispatch `ctx_e70cfbdfe235`, 2026-09-13 KST.

## Result

Manifest schema remains version 2 with optional `app_icon` and
`artwork_limitations` fields. Export binds both to the selected artifact, even
when the brief and a newer child carry a different icon intent. The guide adds
the selected preset/subject/placement/exact lettering and a concise limitation:
the PNG does not establish an Icon Composer document, Android adaptive layers,
an app build or store acceptance. The existing payload names remain `logo.png`,
`manifest.json`, and `brand-guide.md`; the ZIP includes exactly those three files.

The delivery diff adds two imports, two optional fields, one guide composition
and two manifest constructor arguments. Selection, review, background, source
integrity, fresh color analysis, destination and state-commit code is unchanged.
Legacy exports have null icon fields and no appended icon guide section.

## Executed receipts

Baseline: 64 legacy gallery/export/transaction/reserved-output tests passed
before source edits. RED: `Manifest.app_icon` was absent, so its new metadata
contract assertion failed (together with the dedicated gallery API assertion).
Final combined regression: `101 passed in 94.51s`; final icon-only rerun:
`37 passed in 10.95s`. Full commands and environment/resource receipts are in
[gallery.md](gallery.md).

The selected-snapshot case runs the actual export CLI. It prepares an opaque
reviewed monogram parent (`메모`), then adds a newer weather pictogram child and
sets the current brief to that newer intent while retaining selection of the
parent. The resulting manifest and guide describe the monogram parent; the
weather subject is absent from the guide. The original PNG remains byte-equal,
and every ZIP member is byte-equal to the corresponding loose delivery file.

Parameterized actual-CLI rejection cases observed:

| Condition | Error | Outcome |
| --- | --- | --- |
| No selected artifact | `not_selected` | Exit nonzero; state byte-equal; no output directory |
| Missing passing review | `review_required` | Same rollback outcome |
| Opaque intent with partial alpha | `background_mismatch` | Same rollback outcome |
| Changed original bytes | `hash_mismatch` | Same rollback outcome |
| Strict palette with no prior report | `color_review_required` | Same rollback outcome |
| Strict green intent with forged stored PASS for a red original | `color_mismatch` | Fresh recomputation rejects; same rollback outcome |
| Stale expected revision | `stale_revision` | Same rollback outcome |

Strict forged evidence updates the synthetic fixture's image hash/report binding
consistently so that the test reaches fresh color recomputation; it does not
merely fail the earlier hash gate. No bypass option or alternate export path was
added. Existing legacy metadata/ROI/background/color tests remain passing.

## Transaction coverage

The cohesive `app_icon_publish.py` helper is gallery-only. Its tests live beside
delivery tests because they exercise package publication/rollback: injected disk
failure and keyboard interruption both remove owned files twice and allow a
subsequent complete publication; an independently existing destination is
preserved; a foreign file appearing during publication survives rollback.
The gallery tests separately advance session state during final publication,
showing that the read-only snapshot renderer never restores stale state.

Ruff, formatting, basedpyright, six per-file LSP diagnostics and the no-excuse
checker passed. All changed Python modules remain below 250 substantive lines.
No build system beyond the Python helper applies. All temporary test resources
were removed and HTTP port 8768 released; exact receipts are in gallery.md.

T2 is complete. Integrated native-sample Chrome/file-URL checks, full-repository
checks, installation verification and independent final reviews remain named
T4/T5/F1–F4 dependencies owned by the coordinator, not unperformed T2 claims.
