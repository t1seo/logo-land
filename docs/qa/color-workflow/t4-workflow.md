# T4 CLI and workflow evidence

Status: T4 implementation and verification complete. This is synthetic CLI evidence; native image calls and the final review/release wave belong to the coordinator and T8.

## Stable CLI signatures

The global `--workspace PATH` precedes the command. All inputs are local regular files. Mutations require the exact current `--revision`; proposal/prompt/gallery do not mutate the session.

```sh
uv run --script skills/logo-land/scripts/logo_project.py --help
helper() { uv run --locked python skills/logo-land/scripts/logo_project.py "$@"; }
helper --workspace WORKSPACE reference-add --session demo --reference photo --image reference.png --revision 0 --roi-file roi.json
helper --workspace WORKSPACE palette-propose --session demo --request-file request.json --reference photo
helper --workspace WORKSPACE palette-add --session demo --palette green --palette-file candidate.json --revision 1
helper --workspace WORKSPACE palette-add --session demo --palette navy --palette-file navy.json --parent-palette green --revision 3
helper --workspace WORKSPACE prompt --session demo --palette green --lockup-file lockup.json
helper --workspace WORKSPACE import --session demo --artifact v1 --image native.png --prompt-file prompt.txt --revision 2 --palette green --lockup-file lockup.json
helper --workspace WORKSPACE color-analyze --session demo --artifact v1 --revision 3 --roi-file roi.json
helper --workspace WORKSPACE color-gallery --session demo --artifacts v1,v2 --output output/color-galleries/demo
```

`--roi-file`, `--reference` on palette-propose, `--parent-palette`, `--palette` on prompt/import and `--lockup-file` are optional. Analysis report IDs are generated; there is no flag to supply caller-written reports or claim a pass. Import creates the initial report if it has structured palette intent; explicit color-analyze appends another report.

Local request JSON:

```json
{"seed_hex":"#247A52","constraints":{"locked_hex":["#247A52"],"max_colors":2},"selected_by":"assistant","rationale":"Warm companions while preserving the green anchor"}
```

The same request works with `--reference photo`: the CLI uses the stored original image, ROI and actual extraction; it fills the source, extracted colors and canonical source evidence. Proposal output is `{session_id, revision, candidates, warnings, extraction}`. `extraction` is null without a reference. Save exactly one `candidates[i]` as `candidate.json`; palette-add expects PaletteContent rather than the whole proposal or a PaletteVersion. Source evidence must be retained byte-equivalently as structured data: changed/fabricated reference evidence is rejected against recomputed original-byte extraction.

Assistant/Leonardo inputs use T2 PaletteRequest: explicit `source`, `swatches:[{hex,role}]`, `constraints`, `selected_by`, `rationale`, and real `source_evidence` as applicable. No provider calls are made by these commands.

Lockup JSON:

```json
{"layout":"horizontal","symbol_position":"start","text_alignment":"start","typography_style":"Rounded, legible Hangul and Latin sans","font_reference":"Pretendard visual direction"}
```

ROI JSON uses oriented integer coordinates:

```json
{"x":0,"y":0,"width":16,"height":16}
```

PromptResult adds `palette_id`, `palette_digest`, and `lockup` to the existing prompt/parent/revision fields. Use the returned revision and matching intent flags on import; an intervening mutation makes import fail without creating a PNG. Explicit palette wins, otherwise edits inherit the parent palette including null, otherwise generation uses the active palette. Lockup uses explicit override, parent value, then brief value. Background omission intentionally retains the original brief default, independently of parent palette/lockup inheritance.

## Verification tracking

- [x] Read plan, font extension and shared contracts; publish CLI signatures to coordinator/T6.
- [x] Red: six new CLI/palette/lockup tests fail because commands/options are missing (`t4-red.txt`).
- [x] First green: new workflow tests and transaction/safety cases pass; four preloaded manifest-class failures during concurrent T5 editing require a fresh process (`t4-first-green.txt`).
- [x] Reference red: fabricated extraction evidence was accepted before the persistence guard (`t4-evidence-red.txt`).
- [x] Final focused pytest, Ruff, basedpyright and module-size verification.
- [x] Actual manual CLI exercise and portable gallery output.
- [x] Cleanup and final outcome.

## Final verification results

| Check | Actual result | Evidence |
|---|---|---|
| Workflow, new CLI integration, failure transactions, existing transactions, CLI safety, background compatibility and CLI workflow | 59 passed in 36.82s, fresh process | `t4-green.txt` |
| Final owned tests after formatting and provenance guard | 20 passed in 14.50s | `t4-final-owned.txt` |
| Ruff check | All checks passed | `t4-ruff.txt` |
| Ruff format check | 13 files already formatted | `t4-format.txt` |
| basedpyright | 0 errors, 0 warnings, 0 notes | `t4-types.txt` |
| Programming no-excuse audit | No violations in 13 files | `t4-no-excuse.txt` |
| Pure module lines | All <=250; largest owned Python file 175 lines | `t4-module-sizes.txt` |
| Entry script PEP 723, primed cache, `--offline` | Loaded revision 4 with both reports and ColorAide 8.12.1 | `t4-pep723.txt` |
| Actual manual CLI invocation | Reference, proposal, palette, prompt, import, analysis, gallery, all command helps succeeded | `t4-cli.txt` |

Focused command:

```sh
uv run --locked pytest tests/test_palette_workflow.py tests/test_color_cli_integration.py tests/test_color_workflow_transactions.py tests/test_transactions.py tests/test_cli_safety.py tests/test_background_compatibility.py tests/test_cli_workflow.py -q
```

The manual scenario generated a 32×32 synthetic green RGBA fixture, including one alpha-zero pixel with unrelated hidden RGB. It added a reference and moved the external source, proposed a reference-plus-locked-anchor/two-color palette, persisted the candidate, and generated a horizontal symbol/text prompt. Import recorded `v1` with palette `green` and report `report-c6276faa0dfd4e03a33f8abdda965cae`; explicit analysis appended `report-99c4f4303ba54c43a9b712dfb271552b`. Both reports passed the sampled policy for this controlled fixture. This is not evidence of native image quality.

Manual `cmp` checks proved the gallery PNG was byte-identical to the import and session JSON stayed unchanged. Stale import (`revision=2`, current=4), escaping gallery output and existing gallery output all failed with their named errors; the stale artifact never existed. The final session remained at revision 4 with one artifact and two independent report IDs. All seven new/extended command help invocations exited successfully.

## Adversarial coverage and limits

- Green parent → navy child → newer active green palette → geometry-only child retains navy in both prompt and artifact; import adds initial bound reports.
- Unknown palette/reference, stale revision, duplicate palette/reference, traversal, managed reference symlink and malformed/out-of-bounds ROI preserve state and existing bytes.
- A forged extraction response and a reference palette lacking a reference ID were accepted in recorded red runs, then rejected after the actual-byte provenance guard. Reference evidence is stored unchanged and future session writes preserve append-only history through T1 storage.
- A simulated domain commit failure removes newly copied artifact/reference files, while the original session stays byte-identical. Existing disk-write failure tests also pass.
- A simulated initial analysis error preserves the PNG and appends an `unverified` report with the actual error reason; it does not invent a failed generation or erase the artifact.
- Explicit requested font direction and lockup survive parent edits; exact lettering stays in the prompt. Background omission continues to use the original brief independently of these new fields.
- No CLI accepts supplied measurement reports or a caller `passed=true` field. Strict/advisory export and review gating stay in T5 ownership.

One early test process loaded the previous Manifest class while T5 changed delivery serialization, producing four extra-field/schema errors. The fresh 59-test run passed all four without changes to unrelated files. The programming audit script initially needed its actual `skills/programming/scripts/python/` path (the shorter path in the reference was absent); the located checker completed successfully.

The PEP 723 dependency pins were preserved. Offline verification used an already populated uv cache and does not claim a cold-cache installation. Gallery visual/browser review, full repository release checks, copied-skill portability and native image calls remain assigned to T7/T8/coordinator; this worker executed the actual CLI surface and did not modify delivery/export ownership.

## Cleanup and ownership

The disposable `/tmp/logo-land-t4-7HsSYD` workspace and `/tmp/t4-manual.sh` driver were removed after saving the command transcript and results; the transcript remains sufficient to reconstruct the fixture and scenario. The unused `/tmp/t4-fixes.sed` scratch file was also removed. No commit, push, sub-worker, external service call or modification to another owner's files was performed. The coordinator retains plan/Boulder/ledger/git/release ownership and the final five-reviewer wave.
