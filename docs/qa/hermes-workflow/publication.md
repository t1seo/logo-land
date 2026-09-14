# Logopia 0.8.0 publication record

**PASS.** The implementation is on main, and [v0.8.0](https://github.com/t1seo/logopia/releases/tag/v0.8.0) is the published latest release. Its actual downloaded sample matches the verified original byte for byte. [Machine-readable publication evidence](publication-evidence.json).

The final gate is [957 passing tests and actual installed-source verification](final-integration.md), with [all five review roles approved](review-summary.md). The source is frozen; only release wording, this receipt and plan completion metadata may change during publication.

## Registered publication resources

- `output/hermes-release-checks/`: retain private bounded command receipts and metadata; no native sessions or secrets are copied.
- Five task-owned `hermes-*.md` research drafts move from `.omo/drafts/` into `output/hermes-release-checks/research-drafts/`, with original SHA-256 mappings. The published synthesis remains in `docs/research/hermes-design-workflow.md`. The four unrelated `logo-land-next-*` drafts remain in place.
- A single downloaded `output/hermes-release-checks/release-package.zip` verifies the actual published sample asset; compare its digest with the original and remove this exact download afterward.
- Git and GitHub commands are finite foreground operations. No new server, browser automation profile, tmux session, image request or package installation is needed.
- Opening the public sample in the user's regular Google Chrome is an intentional requested deliverable; retain that tab.

Historical releases and the failed v0.4.0 draft remain untouched.

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

## Published identities and real download

- Implementation commit: `c09072da07da7af5b6c08c5345bb32a3adb726be`.
- Annotated `v0.8.0` tag object: `bcd95fe49492e4be773e00091fabe72bdebf7ea5`; its peeled commit equals the implementation commit.
- Actual `git push --atomic origin main refs/tags/v0.8.0` exited 0. Live remote main, local main and tracking main matched the implementation commit after that push.
- GitHub release ID `388611593`, published at `2026-09-14T18:14:38Z`, is neither draft nor prerelease. The latest-release API returns `v0.8.0`.
- The uploaded `logo-package.zip` is **711,451 bytes**, SHA-256 `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04`.
- Actual public download returned **HTTP 200**. ZIP members are exactly `logo.png`, `manifest.json` and `brand-guide.md`, each byte-identical to the reviewed delivery. The GitHub asset digest also agrees.
- GitHub About now describes Codex and Hermes in English; its actual API readback matches the submitted description.

The receipt-only follow-up on main contains completion documents and this evidence. The release tag remains fixed on the tested implementation commit; it is not moved to a documentation-only commit.

## Publication QA and cleanup

The actual HTTP channel was `curl -i --head --location --connect-timeout 5 --max-time 45 https://github.com/t1seo/logopia/releases/download/v0.8.0/logo-package.zip`, followed by a bounded full download and independent ZIP/hash checks. The header chain ended in 200 and all download commands exited.

| Adversarial class | Observable or applicability |
| --- | --- |
| Malformed input | Fixed reviewed paths and tag; exact release flags, asset count, names, dimensions-independent bytes and ZIP members asserted. No new input parser changed. |
| Prompt injection | Literal fixed arguments; downloaded contents treated only as bytes. No remote text or ZIP member was executed. |
| Cancel/resume | Publication resumed by reading durable commit, tag, release and exit receipts; no duplicate release or native image request. |
| Stale state | Actual remote refs, latest-release API, public digest and exact 209 source bindings agree. |
| Dirty worktree | Four unrelated drafts retain their original hashes and remain unstaged. Private sessions are excluded. |
| Hung commands | HTTP connection limit 5 seconds and total limit 45 seconds; all foreground commands settled. |
| Flaky tests | No executable changes after the 957-test pass; no unrelated repeat or removal of earlier failed evidence. |
| Misleading success | Release state, actual HTTP body, original equality, ZIP member hashes and active Chrome URL verified independently of exit status. |
| Repeated interruptions | No interrupt-sensitive production code changed in publication. Durable identities prevent repeated creation; the runtime's repeated-interruption probes are recorded in the final integration gate. |

The exact verification download was removed after its digest check; the original public ZIP remains. No temporary server, browser automation context, tmux session or installation was created. The five task-owned research drafts were archived under ignored output with exact hash mappings. Existing scoped QA cleanup receipts remain valid, all **23 Orca tasks** are completed, and the run has no pending messages.

The public sample was opened in the user's regular Google Chrome. Its active URL is `docs/hermes-demo/index.html` and its title is **OFFCUT — a Hermes study by Logopia**. This requested tab, the named Hermes profile, original artwork and workflow are intentional deliverables.
