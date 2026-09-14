# Real Hermes workflow execution

Status: the actual workflow completed at revision 47 with five originals, two reviewed edits and a verified e2 delivery. The [final native Chrome checks](native-gallery.md) passed, including actual downloads, parent comparison, mobile layout and unchanged canonical bytes; all owned browser resources were removed. The earlier ring image was a connectivity diagnostic, not this demo.

## Registered resources and intent

- The dedicated `logopia` Hermes profile and installed `logopia-studio` plugin are intentional deliverables. The default profile, credentials and other plugins are preserved.
- Installation stages and locks are owned by the installer and removed on settlement. Its retained lock file is an unlocked coordination inode, not a running process.
- `output/hermes-demo/` holds the exact request, private CLI/session logs and installation receipts. Keep source evidence private; publish only reviewed artwork and concise attribution.
- Workflow `offcut-hermes-demo` and its exact helper session preserve originals, prompts, attempts, critiques and revisions. The fictional OFFCUT brief demonstrates a reclaimed-material furniture identity; it does not claim trademark availability.
- Each actual Hermes CLI child has a 1,800-second owned deadline and ten-second grace. Await its exit before another profile call. On interruption, preserve unresolved native outcomes instead of resubmitting.
- The final portable gallery and generated original/package downloads are intentional deliverables. Temporary QA browser profiles, tabs and drivers will be separately registered and closed; retain only the final user-facing Chrome tab.

Expected scenario: three distinct white-background brand candidates, two actual pixel critiques per candidate, a selected parent with one requested construction/spacing revision, fresh child critique, and delivery only when the existing checks permit it. Failures remain evidence and are not converted into approval.

## First native attempt

Session `20260915_005825_705e1e` used `openai-codex / gpt-5.6-sol` for the two structured planning calls and image critiques, and `gpt-image-2-medium` through Hermes's public image tool. The normalized saved brief exactly equals `output/hermes-demo/start.json`. All three initial image jobs succeeded; c1 and c2 each have two complete, separately bound critique reports. The final c3 review was interrupted at workflow revision 23.

The actual Hermes response reported a **420-second** sequential-tool timeout. The owned launcher was set to 1,800 seconds and its child exited 0; its original generic interruption message incorrectly attributed the unfinished job to the launcher. The public installed resolver reads `timeouts.tools.sequential_call`, falling back to `concurrent_batch`. Contract G7 and the focused timeout/recovery work preserve this first failure and fix the distinct native limit without changing Hermes core or the default profile.

The c1 design critic requested optical spacing changes around FF/FC/UT, while the production critic passed text. The conservative gate retains that revision requirement. Both c2 reports requested a flatter white background. These observations are model critiques, not human designer approval. The c3 reports were not persisted and are not counted as completed.

The actual originals were visually inspected. c1 is 1774 × 887; c2 and c3 are 1254 × 1254. Requested dimensions do not override actual decoded dimensions. No original has been cropped, rescaled or repainted for this demo. The existing PNG bytes remained identical during explicit critique-only recovery. Existing job fields were preserved; serialization added the optional `retry_of: null` default, so raw job JSON is not byte-identical. The [context review](review-context.md) verifies the defaults-normalized records separately.

## Repeated-start regression

The coordinator pinned a fresh draft calling create/produce (1 pass), then captured three RED assertions: repeated native start also called produce in failed, outcome_unknown and cancelled phases. The narrow registration guard now returns saved state in those phases. The scoped host action/registration suite passed **15 tests**, Ruff passed and Python 3.11 basedpyright reported zero errors/warnings/notes. Evidence remains under `output/hermes-demo/host-resume-*.txt`; the real no-call channel check follows fresh installation.

Registered for the actual no-call check: own tmux session `logopia-native-no-call`, to run the exact saved start request against the interrupted workflow and capture its refusal. It must be closed after capture; no other tmux session may be touched. The registered PIN/RED/GREEN fixture directories have already been removed, and the retained default pytest roots 158–160 were verified as this task's prompt/helper fixtures and removed. The default pytest directory is now empty.

The refreshed native 0.8.0 installation succeeded through doctor → sequential limit → concurrent limit → enable. Public `config get` returns 1800 for both named-profile limits, and the default profile's pre-install digest still matches. Installation receipt: `output/hermes-demo/install-080.json`.

The actual tmux command `uv run --locked python integrations/hermes/studio.py run --profile logopia --request output/hermes-demo/start.json --json` returned `outcome_unknown` with `logs: null`. Canonical workflow bytes were identical before/after, so the repeated start submitted no Hermes job. Capture: `output/hermes-demo/no-call-tmux.txt`. The owned session was killed and its pane PID 73301 is absent.

## Actual critique-only continuation

The explicit `continue` request at revision 23 completed at **revision 27 / awaiting_choice**. Independent strict parsing confirms exactly one new job: a successful critique linked to j7. There were **zero new image or planning jobs**; all three PNG hashes, both existing critique pairs, strategy, directions and brief match the pre-recovery state. The seven prior job records match after normalizing the optional default described above. The old error remains in its original job. Evidence: `continue-result.json`, `continue-binding.json` and the before-state copy under `output/hermes-demo/`.

Both new native critique calls are present in the profile's structured-call audit. c3 still needs composition, text or small-size refinement, so it is not approved. The demonstration proceeds with c1 because its identified issue is narrower: optical letter spacing. This is the coordinator's sample choice, not a claim that the user approved it.

## Two actual parent-based edits

The sample choice of c1 was recorded at revision 28. The first requested edit opened FF/FC/UT spacing while preserving the symbol, word construction, colors and white horizontal presentation. Its e1 output is an unchanged **1774 × 887** native PNG, SHA-256 `08196269c02184cd99237a0e2a8306e039f1d13eac0a9261ce652f6c5b0a6560`, with exact parent c1.

Both e1 critics passed text, composition, small-size readability and background, but failed preservation: the symbol-to-word gap had narrowed. The coordinator viewed both originals and confirmed the narrower gap. The failed e1 remains visible. A second explicit edit of e1 requested only a slight rightward shift of the intact wordmark to restore that clear space, retaining its improved internal spacing.

The e2 output is also **1774 × 887**, SHA-256 `882dd3318064ef2573344d9b4dfef5bf9d460f5a9bb0aaf2f585dd2473c887bb`. Both fresh critics passed all five criteria; neither inherited a parent's approval. The coordinator viewed the actual PNG. The reports observed the requested gap restoration and retained readability at 192px; this is a visual/model assessment, not a pixel-exact editing or professional-superiority benchmark.

Both edit receipts identify `openai-codex / gpt-image-2-medium` and one input image. The canonical lineage is **c1 → e1 → e2**; all parents and initial candidates remain byte-identical. The workflow consumed exactly three initial image jobs and its two allowed edit jobs. No additional aesthetic retry, provider fallback or scripted artwork transformation was used.

## Actual delivery and recorded sessions

Explicit selection of e2 produced `ready` at revision 45. Delivery completed at **revision 47 / delivered**, with these original files under `output/logopia/offcut-hermes-demo/`:

- `logo.png`: exact e2 bytes, SHA-256 `882dd3318064ef2573344d9b4dfef5bf9d460f5a9bb0aaf2f585dd2473c887bb`.
- `logo-package.zip`: SHA-256 `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04`.
- `manifest.json`: SHA-256 `51de33aaa6b85fe3103b0440ceb22a0bd7a3158a7df5f69ebafbb084d0791f8d`.
- `brand-guide.md`: its exact bytes match the ZIP member.

The ZIP contains exactly the PNG, manifest and guide. Root independently ran bounded gallery delivery validation, checked ZIP members and hashes, then repeated the core's public `deliver` using `NoInferenceHost`. It returned the existing receipt without inference, another package or a canonical byte change. Final snapshot and verification receipt are privately retained as `output/hermes-demo/final-workflow.json` and `final-binding.json`.

The seven actual Hermes sessions are retained as redacted JSONL under `output/hermes-demo/`: start `20260915_005825_705e1e`, continue `20260915_012549_9f2d3c`, parent choice `20260915_012851_0ae55f`, first edit `20260915_013036_ced3a1`, second edit `20260915_013346_39fb02`, final choice `20260915_013634_f02e0c`, and delivery `20260915_013738_d587f4`. Full sessions, system content and local cache receipts are not public sample payloads.

The session-binding check initially omitted the local integration import path, then assumed direct tool-call names. Inspection of non-content metadata showed the installed runtime's public deferred `tool_call` envelope. The corrected verifier unwraps that envelope and compares its parsed arguments with the exact saved request, without reading or publishing reasoning. These were QA harness corrections, not generation retries or runtime source changes.
