# Logopia: Hermes production workflow

Status: implementation. Six gap-review findings are resolved in the binding section of `integrations/hermes/CONTRACT.md`.

## Goal

Make Hermes actually direct logo production: a concise brief, distinct visual directions, native image generation, separate structured visual critiques, preserved decisions and targeted revisions, with an immediately usable comparison page and verified original delivery. Existing Codex skills, PNG provenance, palette checks, IP defaults and exports remain compatible.

## Decisions and boundaries

- Use the installed NousResearch Hermes Agent and its public native plugin APIs. The isolated `logopia` profile successfully called `image_generate` through its existing `openai-codex` provider; no separate provider client, copied credentials, paid fallback or Hermes core changes.
- Use bounded `ctx.llm.complete_structured` calls for strategy/art direction and two separate pixel critics (design/lettering and production/use-size). These are separate model calls, not human experts or autonomous specialist agents. Critics receive actual PNG bytes, target-size renders, and parent bytes for edits. The first critique does not receive the creator's self-evaluation.
- Build a compact, Python 3.11-compatible native plugin in `integrations/hermes/` so it runs in the installed Hermes interpreter. Its core has strict Pydantic v2 records and no Hermes imports. Use the existing locked Python 3.12 helper CLI as the artifact/import/review/export boundary, not an in-process import.
- Store independent strict workflow state under `.logo-generator/workflows/<id>/`. Keep the existing session schema unchanged. Persist exact prompts, request identity, original bytes/hash, parent links, critique history, chosen direction and keep/change feedback. A running image request after interruption becomes an unresolved outcome; resume never submits it again automatically.
- Default to three meaningfully different concepts (six for IP); honor an explicit count within the displayed supported bound, and reject an unsupported count rather than silently truncate. At most two requested revision calls per workflow. No automatic aesthetic retry loop or invented quality score.
- Hermes conversation is the primary interaction. A portable, offline HTML studio shows current stage, concise strategy, all originals, separate review status, size previews, parent/child comparison and keep/change feedback. Copying feedback does not mutate canonical selection; the page says to send it to Hermes. No new web server, accounts, paid service or hidden analytics is required.
- Tools expose create/produce/status/revise/choose/deliver. Stage changes are deterministic and evidence-bound; helper review/export requires actual passed required checks. Original downloads remain available before final approval. Unknown/invalid critique means unreviewed, not passed.
- An installer and launcher use a named profile explicitly, preserve the user's default Hermes configuration, use argv/query files and an owned-process deadline. CLI interruption stops future calls and preserves completed outputs. No process-global kill, automatic unknown-job retry, or unbounded native calls.
- Documentation remains concise, English default and Korean counterpart. Include one direct Hermes workflow example with actual generated candidates and revision. Preserve IP reference credit. Do not promise editable vector, real font typesetting, trademark clearance or measured professional superiority.

## Ownership and integration contract

The coordinator owns the plan, shared contract, payload installer, process wrapper, integration, research synthesis, demo and final docs. Parallel workers own: (A) core models/storage/engine/helper bridge; (B) Hermes host adapter, plugin manifest and director instructions; (C) offline gallery renderer/template and its browser tests; (D) launcher CLI, request preflight, profile coordination and completion checks. The exact public interface is frozen in `integrations/hermes/CONTRACT.md` before implementation dispatch. Workers are not alone in the repository and must preserve others' edits and the four unrelated drafts. No worker changes version metadata, README, pyproject or another worker's files without coordinator routing.

## TODOs

- [x] T1 — Finish primary-source research, gap review and executable contract.
  - Evidence: three Orca research reports, actual native image/tool transcript, 642-test unchanged baseline, installed API and Python boundary; gap review resolved.
- [x] T2 — Implement core, native Hermes plugin and offline comparison UX in parallel.
  - PIN existing helper behavior before adapter changes; RED tests before new production code.
  - Strict models and transitions, immutable originals, bounded jobs, actual critique inputs, exact references and truthful failure/unknown states.
  - Native plugin registration/doctor, core integration tests, gallery Chrome scenario, all applicable adversarial classes and owned-resource cleanup.
- [x] T3 — Install and exercise the real Hermes workflow, including revision and delivery.
  - Installer/launcher tests first; isolated profile plugin installed and enabled without changing default settings.
  - Actual strategy and direction calls; three original image calls; separate real image critiques; a targeted parent-based revision and fresh review; final artifact/ZIP only after required gates pass.
  - Capture actual tool receipts/session, model attribution, original/prompt hashes, gallery screenshots, interrupted-state resume behavior and no duplicate native submissions.
- [x] T4 — Publish a direct sample and concise bilingual documentation.
  - Document setup, one-command use, feedback/resume and actual limitations. New sample page shows originals and actual decisions without nested navigation. White backgrounds for README sample presentation.
  - Update version consistently for the additive Hermes feature; keep internal `logo-land` compatibility and IP attribution.

## Final Verification Wave

- [x] T5 — Complete independent review and integrated QA.
  - Five Orca reviews: goal, code, safety, hands-on QA, context/provenance. Resolve findings without deleting failed evidence.
  - Existing full tests, new tests, strict typecheck/lint, real plugin doctor, Chrome keyboard/mobile/direct-download checks and real Hermes evidence.
  - Probe malformed input, instruction-like brief/feedback as inert data, cancel/resume, stale state, dirty worktree, long calls/deadlines, flaky-test handling, misleading success and repeated interruption where applicable. Record explicit N/A reasons otherwise.
- [ ] T6 — Commit, push and verify main; finish cleanup and delivery record.
  - Stage only reviewed task files, preserve unrelated drafts and private sessions. No force/reset/amend. Verify actual remote main SHA, finish all worker/resource cleanup, and show the local sample in Chrome.

## Verification and cleanup contract

Each worker receives all seven start-work sections, exact tests and a real manual channel (tmux or Chrome, not dry-run). Evidence lives under `docs/qa/hermes-workflow/`; large/private raw sessions stay ignored under `output/hermes-preflight/` or `.logo-generator/`. Register each temporary script, tmux session, browser context, port or child process for cleanup when created. The intentional installed profile/plugin, user-facing gallery and actual logo project are deliverables, not QA leftovers. Mark a checkbox only after source review, automated checks, manual channel, applicable adversarial checks and teardown receipts.
