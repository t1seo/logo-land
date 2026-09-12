# T8 documentation verification

Date: 2026-09-13 (Asia/Seoul). Scope: English/Korean READMEs, `project-files.md`, `delivery-checks.md`, `brief.example.json`, and this record. The integration coordinator owns native image calls, public sample assets/gallery, full-suite QA, installation/release metadata and publication. This record does not certify those tasks.

## Work and red baseline

The pre-edit READMEs documented v0.3.1 file management, ten historical native samples and transparency. They did not explain four color entry points/combined restrictions, immutable palette inheritance, strict/advisory measured reports, structured horizontal/stacked lockups, font-reference boundaries or schema-2 migration. The helper reference lacked runnable color commands/JSON, and the example brief had no lockup. These were observed documentation gaps, not failing implementation tests.

Applied `skill-creator` for the skill reference/asset edits and `orchestration` for contract coordination. T4 owns CLI behavior; T5 owns export behavior; T6's accepted skill/typography/color references and final `docs/research/font-tools.md` supply narrative boundaries. The shared model contract is [contracts.md](contracts.md).

| Deliverable | State |
|---|---|
| English-default README and matching Korean coverage, centered v0.4.0 badges | Complete; verification below |
| Runnable palette/reference/lockup/report/gallery examples and schema-1 boundary | Complete; verification below |
| Exact JSON parsing, actual CLI execution and link/diff audit | Complete; two coordinator-owned publication targets remain pending |
| Eight real native cases and public comparison page | Pending coordinator evidence |

## Validation evidence

The documented native-import step requires an actual returned PNG. Documentation smoke checks may reuse a pre-existing historical native PNG only to exercise file/analysis plumbing; that is not a new generation, brand-quality approval or color-conformance claim. No all-true review is used to create a fake delivery.

Executed the six `sh` blocks in [project-files.md](../../../skills/logo-land/references/project-files.md)'s “Runnable color examples” section with `bash -e`, from the repository root. Only the workspace was replaced with a fresh OS temporary directory and the explicitly marked native-output placeholder with the historical [고요 delivery PNG](../../samples/items/03-goyo/delivery/logo.png). No generated script or fixture was added to the repository. The flow exercised `init`, automatic/anchor/restricted proposals, `reference-add`, reference/combined proposals, candidate extraction, `palette-add`, lockup-aware `prompt`, `import`, `color-analyze` and `color-gallery`.

Observed output:

```text
PASS 6 documented shell blocks
STATE revision=4, active_palette_id=green-reference-v1, artifact=a-v1
PROMPT revision=2, palette_id=green-reference-v1
REPORT status=mismatch, scope=full_image
  Fewer than 99% of sampled core pixels match the target palette
  Required color #247A52 has no matching core samples
PASS gallery index.html created with green-reference-v1 and relative PNG reference
PASS gallery PNG equals historical source bytes
SHA256 4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174
PASS reference-add/palette-propose/palette-add/color-analyze/color-gallery/prompt/import --help
PASS temporary workspace removed
```

The mismatch is an expected plumbing observation for that historical image under the new demonstration intent. It is not evidence about the coordinator's forthcoming GROVE or other native cases. No review or export was performed for this mismatched demonstration.

Actual parser check: extracted every fenced JSON object and shell JSON heredoc in the four edited Markdown guides and parsed them with `json.loads`. The two marketplace examples passed JSON syntax; the ten helper objects passed the actual `PaletteRequest`, `PaletteContent`, `LockupIntent`, `RegionOfInterest` or `VisualReview` parser as appropriate. `Brief.model_validate_json` also accepted [brief.example.json](../../../skills/logo-land/assets/brief.example.json). Result: **12 Markdown JSON objects plus the example brief passed**. Both horizontal and stacked lockup schemas were included.

Applicable negative CLI checks ran against the same temporary session. Every expected failure preserved the exact `session.json` bytes:

| Input | Actual outcome |
|---|---|
| Lock #247A52 with allowed set containing only #000000 | Exit 1, `constraint_conflict` |
| Reference ID `missing` | Exit 1, `not_found` |
| `color-analyze --revision 2` when current revision is 4 | Exit 1, `stale_revision` |
| Reuse existing gallery destination | Exit 1, `conflict` |
| Gallery artifact ID `missing` | Exit 1, `not_found`; no destination created |
| Attempt `color-analyze --passed true` | Exit 2, `No such option` |

Read the published [T4 CLI contract](t4-workflow.md) and the implemented T5 `Manifest`, `export_colors` and gallery interfaces. CLI names/flags, proposal envelope/candidate extraction, matching prompt/import intent, generated report IDs, manifest fields and strict/advisory/unverified policies agree with these guides. Font links use T6's typography reference and the final [research](../../research/font-tools.md); Space Grotesk and Noto Sans KR are explicitly requested appearance references, not asserted font provenance.

Validation commands:

```sh
uv run --locked python skills/logo-land/scripts/logo_project.py --workspace . --help
uv run --with PyYAML==6.0.2 python '/path/to/skill-creator/scripts/quick_validate.py' skills/logo-land
git diff --check -- README.md README.ko.md skills/logo-land/references/project-files.md skills/logo-land/references/delivery-checks.md skills/logo-land/assets/brief.example.json docs/qa/color-workflow/t8-docs.md
```

The validator was run from the installed `skill-creator` skill's actual path. The initial locked-environment invocation failed because PyYAML is not a project dependency; rerunning with isolated `--with PyYAML==6.0.2` returned **`Skill is valid!`** without editing dependency metadata. The initial section-preservation audit used an incorrect English heading string; correcting the audit to the actual `Revisions and delivery` heading passed. These verification-tool corrections did not change application code.

Local link audit checked 138 occurrences at its first run. Only the planned `docs/colors/index.html` and `docs/qa/color-workflow/README.md` targets were absent; both belong to the coordinator and are explicitly pending. Compared each README's entire ten-sample and transparency sections against `HEAD`: **byte-identical**. Top-centered badges remain, and both languages use v0.4.0. Shared palette, exact-text, font-reference, backup and gallery facts agree across both READMEs. Whitespace validation passed.

Full build/type/test verification, installed-copy behavior, actual browser preview inspection and native export validation belong to the coordinator and are not inferred from Markdown/JSON edits. This task exercised generated HTML through its CLI/file surface but did not claim visual browser QA.

## Public links and pending native evidence

The coordinator supplied the following final paths; file existence and case outcomes remain pending actual publication into the worktree:

- [Color comparison gallery](../../colors/index.html)
- [Integrated color QA](README.md)
- `docs/colors/assets/01-sunroom.png`: automatic warm bakery direction.
- `docs/colors/assets/02-northline.png`: technology palette with exact NORTHLINE lettering.
- `docs/colors/assets/03-grove.png`: transparent fixed #247A52 intent.
- `docs/colors/assets/04-grove-warm.png`: real child edit with warmer companions.
- `docs/colors/assets/05-bamgyeol.png`: black/ivory maximum-two-color intent with exact 밤결 lettering.
- `docs/colors/assets/06-tide.png`: reference-derived palette.
- `docs/colors/assets/07-fieldnote.png`: combined reference/anchor/count intent.
- `docs/colors/assets/08-bamgyeol-white.png`: transparent white-letter child.

These labels describe requested scenarios, not observed results. No sample image, report, native call ID or success result was fabricated. The README explicitly leaves live evidence pending. The original [ten samples](../../samples/index.html) and [transparency documentation](../../transparency/README.md) remain intact.

## Cleanup and limits

No commits, pushes, subagents, MCP installation, new accounts, font downloads or native image calls were performed. The temporary workspace and generated JSON/PNG/gallery files were removed automatically after assertions. The isolated PyYAML validator may retain uv's normal external cache; no shared cache was deleted and no project dependency metadata was changed. No Python, TypeScript, Rust or Go source was edited; implementation LSP/build gates are handled by their owners. The six owned files are the complete documentation diff.
