# Logopia 0.8.0 publication record

Status: prepared; no publication is claimed until remote checks complete.

The final gate is [957 passing tests and actual installed-source verification](final-integration.md), with [all five review roles approved](review-summary.md). The source is frozen; only release wording, this receipt and plan completion metadata may change during publication.

## Registered publication resources

- `output/hermes-release-checks/`: retain private bounded command receipts and metadata; no native sessions or secrets are copied.
- Five task-owned `hermes-*.md` research drafts move from `.omo/drafts/` into `output/hermes-release-checks/research-drafts/`, with original SHA-256 mappings. The published synthesis remains in `docs/research/hermes-design-workflow.md`. The four unrelated `logo-land-next-*` drafts remain in place.
- A single downloaded `output/hermes-release-checks/release-package.zip` verifies the actual published sample asset; compare its digest with the original and remove this exact download afterward.
- Git and GitHub commands are finite foreground operations. No new server, browser automation profile, tmux session, image request or package installation is needed.
- Opening the public sample in the user's regular Google Chrome is an intentional requested deliverable; retain that tab.

The implementation commit, annotated tag, actual release/asset, remote main identity and final cleanup are recorded below after each is verified. Historical releases and the failed v0.4.0 draft remain untouched.

## Prepublication checks

All 209 validated source/test/configuration hashes remain unchanged, all three
manifests declare 0.8.0, and 295 local documentation links resolve. The four
unrelated drafts match their original hashes and are not staged. The first
metadata verifier used system Python without tomllib; the identical verifier
passed in the existing locked interpreter, without a dependency change.

The unfiltered staged whitespace check reports spaces retained in captured QA
output/diffs and in the byte-bound delivered brand guide. Those original records
are preserved. The code and authored-documentation check, excluding only captured
QA `.txt`/`.diff`/`.response` files and the exact delivered `brand-guide.md`, passes. No product lint
rule or test assertion was suppressed; the actual delivery bytes still match the
verified ZIP. The staged scope contains only the reviewed task paths.
