# Logopia logo craft and white-background showcase

## Scope

Upgrade the conversational skill using primary design research; create a Pokopia-inspired Logopia identity and regenerate all 16 current README examples on opaque white backgrounds. Keep the English-first and Korean README concise, show the samples immediately, and retain the IP adaptation credit. Commit and push the completed rebranding iteration to main under the user's existing authorization.

## Decisions and review

- Research: Pentagram Slack/Mastercard, IBM 8-Bar, Google identity, Design Council framework, Apple app-icon guidance and the actual official Pokopia image.
- Existing `styles`, `concept`, `exact_text`, palette and logo types suffice; no runtime/schema changes or fabricated image service.
- Route a shared title backplate to `emblem`, lettering without it to `wordmark`, and a distinct motif plus title to `combination`.
- Professional craft means brief relevance, recognizable construction, optical lettering, deliberate color roles and fitness at intended size. Do not claim expert certification or universally impose minimalism.
- Gap review completed by game_title_gap_review: predeclare empty white-background regions for each composition; IP may occupy lower corners. Pixel checks supplement full-image inspection and cannot prove every background pixel.
- Preserve previous image bytes, receipts and deliveries. Use a new `docs/showcase/2026-09-white/` collection and `docs/brand/2026-game-title/` identity record.
- Native PNGs only. No recoloring, white CSS matting, cutting out images, or scripted lettering to simulate generation. One initial call per item, preserve actual output, fix required text/background failures with targeted native edits and retain parents.
- White background is this showcase's requirement, not a new default that overrides future users. No release/tag change requested.

## Ownership and dependencies

The skill worker owns only skill Markdown and the research note. The coordinator owns the plan, briefs, native calls, provenance, brand/README/gallery files, validation and git publication. Skill updates precede the native sample calls. Documentation rendering follows returned images. Reviews precede publication. All existing unrelated drafts are preserved.

## TODOs

- [x] 1. Research professional practice and inspect the actual reference; review scope gaps.
  Evidence: cited primary sources, local private official reference, read-only gap-review result.
- [x] 2. Upgrade skill routing, craft workflow, game-title directions and evidence-based visual review.
  Verify: skill validator; actual helper prompts for emblem, lettering, Hangul and white IP; inspect that examples preserve exact text, use existing types, and do not introduce global palette/approval rules.
- [x] 3. Generate one new Logopia identity and 16 new originals with recorded briefs/prompts/receipts.
  Verify: native output path and SHA256, actual PNG size and alpha, predefined white-background pixel regions, exact spelling, distinct construction and intended-use size. Record unresolved limitations; never mark a failed image approved.
- [x] 4. Update bilingual README, current identity/gallery/download links and white presentation board.
  Verify: real Chrome desktop/mobile, all 16 images loaded, direct original links work, no horizontal overflow, new identity and IP attribution visible. Old outputs remain explicitly archived.
- [x] 5. Complete integrated verification and independent reviews, then commit and push main.
  Verify: local links, prompt/image hashes, original-preserving ZIP, plugin/skill validators, clean diff, remote commit equality. Run appropriate existing tests only if runtime code changes become necessary. Close QA browser contexts/processes and record cleanup.

## Completion standard

Verification record: [logo craft QA](../docs/qa/logo-craft.md). The final README uses
two columns after actual Chrome testing found mobile overflow in the initial four-column
layout. All five independent reviews passed after the IP prompt vocabulary correction.
Implementation commit `fa6c1422de6dc3216b04a7e00acc47ccf9531966` was pushed to
`origin/main`; `git ls-remote` matched the local commit. Final local link validation
checked 856 targets without a missing file. Unrelated draft files were preserved.

Report actual changes and sampled/visual evidence, with a direct README/commit link. No aesthetic guarantee, vector/font-file claim, platform-ready icon claim, or invented strict color pass. Research and execution details belong in supporting files rather than the main README.
