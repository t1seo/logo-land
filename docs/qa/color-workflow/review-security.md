# Independent security and integrity review

Date: 2026-09-13 KST. Base: `fd1d89c66e2fb2193954a5ee732cd1a688bdba6d`. Scope: the uncommitted color/typography implementation and new public evidence. This is the security reviewer in the coordinator's five-part `omo:review-work` review, dispatched through Orca; it is not the combined verdict of all reviewers.

| Decision | Verdict | Confidence |
| --- | --- | --- |
| Security/integrity of the reviewed implementation | **PASS**; no new actionable CRITICAL/HIGH issue found | HIGH within the local CLI trust model |
| Commit code and truthful documentation as an explicitly unreleased development preview | **PASS from this review's scope** | HIGH |
| Whole goal complete / public v0.4.0 release ready | **FAIL** | HIGH |

The implementation preserves original bytes, rejects tested path escapes and stale inputs, and recomputes strict export evidence instead of accepting stored pass metrics. Required restricted-color and white-transparent native successes remain absent. A development commit is reasonable with the existing unreleased labels and failure evidence; this security approval does not waive the other reviewers or authorize publication.

## Blocking issues

**Security blockers: none identified.** The existing low-severity diagnostic exposure below is non-blocking for this local tool.

**Release blocker: essential native gates remain unmet.** `docs/qa/color-workflow/README.md:52` records the missing restricted and white-transparent successes. The release rule at `plans/logo-land-color-workflow.md:313` requires leaving the release unpublished when required live QA remains unresolved. Independent read-only recomputation in this review confirmed:

- Black/ivory 밤결 `a-v1`: `indeterminate`, 615 partial-alpha samples among 2,697 visible samples; both repairs remain `mismatch`.
- Combined reference/anchor/count FIELD NOTE `a-v1`: `indeterminate`, 371 / 3,019; both repairs remain `mismatch`.
- White 밤결 `white-v3`: `indeterminate`, 923 / 3,483 (26.50%); prior white attempts also remain indeterminate.
- GROVE's warm edits have an anchor-only sampled `pass`, which does not establish requested transparency or excuse the documented opaque checkerboard. They are not successful deliveries.

The clean-looking final white Chrome preview does not alter these measurements. The permitted two repairs per request have been exhausted; this reviewer made no generation/edit calls and does not recommend further attempts under the settled requests, relaxed thresholds, or a release claim based on synthetic tests. The coordinator still owns aggregation of all five reviews.

## Concrete non-blocking finding

### S1 — LOW, pre-existing: rejected JSON values are echoed into stderr

**Location:** `skills/logo-land/scripts/logo_project.py:208`–`209`; `skills/logo-land/scripts/logo_helper/model_base.py:40`–`43`.

The CLI serializes `str(ValidationError)`, while the base model does not suppress input values. An unexpected field is correctly rejected, but its value appears in the error. This behavior was already present before this change and documented in `docs/qa/review-security.md`; it is not a new color-workflow regression.

**Reproduction:** the review's disposable `output/review-security/manual/invalid-brief.json` contains a valid minimal brief plus `"password":"SYNTHETIC-REVIEW-NOT-A-SECRET"`. Running the real helper with `--workspace output/review-security/manual init --session bad-brief --brief output/review-security/manual/invalid-brief.json` exits 1 and includes that synthetic value as `input_value` in stderr. No session is created. Filesystem diagnostics also include caller-local paths, as the symlink-negative probes demonstrate.

**Impact:** a user who accidentally includes sensitive values in invalid input can disclose them when sharing terminal logs. No actual credential exposure was found in the reviewed public evidence.

**Suggested remediation:** suppress Pydantic input values in diagnostics or emit structured field/error information without rejected values; continue replacing local paths before publishing logs. This is a bounded privacy improvement, not a release security blocker under the current trust model.

## Boundary review

| Boundary | Evidence and conclusion |
| --- | --- |
| PNG/JPEG input and resource limits | `storage.py:61` bounds reads to 64 MiB and rejects leaf symlinks/special files. `reference_decode.py:47` verifies actual static PNG/JPEG format, end markers, dimensions and the 40M-pixel bound before loading. Existing logo import additionally uses `images.py:18` for static, complete, nonempty PNG checks. Oversize headers, malformed formats, truncation, animation and alpha fixtures passed. Sampling is bounded; decoding still allocates full-image buffers. |
| ICC, EXIF and ROI | `reference_decode.py` verifies before reading EXIF, bounds orientation and checks ROI in oriented coordinates. `color_profiles.py` converts supported RGB ICC only in memory; malformed/non-RGB ICC, unavailable ICC support and unsupported gamma-only metadata produce uncertainty. RGB profile conversion, JPEG orientation, palette/grayscale transparency and ROI tests passed. These operations never save an altered master. |
| Paths, symlinks and publication | `safe_path` rejects absolute, parent, backslash and drive-style escapes and existing symlinks below the canonical workspace. IDs and stored artifact/reference paths are constrained. Both publishers use fresh directories and exclusive files/links. Exports reserve `.logo-generator`; galleries also reserve `.git`. Existing destinations, static symlinks and reserved paths were rejected through the CLI; tested publication/save failures preserve prior state and files. |
| Original and reference provenance | `Store.load` checks every artifact hash and decoded PNG facts and every reference hash. Reference extraction rechecks the bytes, and `verify_reference_evidence` recomputes actual extraction before accepting supplied provenance. Forged/missing reference evidence tests and an actual changed-reference CLI probe passed. Reference metadata is originally obtained from decoding; resume authenticates reference bytes by hash rather than independently re-decoding all reference metadata fields. |
| Immutable state and migration | Strict frozen models reject unknown/coerced data and inconsistent graph bindings. `Store.save` checks append-only palette/reference/report history and immutable artifact facts. First successful v1 mutation preserves the exact prior JSON backup; conflicting backup and failed-save tests passed. Cooperative locks and optimistic revisions prevent the tested conflicting updates. |
| Stored/tampered reports | `session_models.py` checks artifact hash and palette ID/digest bindings. `color_delivery.py:58` reanalyzes the verified bytes with current fixed policy, retaining an explicitly recorded ROI and surfaces. Tests forged stored pass/mismatch statuses, inflated ΔE thresholds and matching metrics; mismatch/uncertainty still blocked strict export. Gallery labels explicitly describe a stored measurement snapshot, not delivery approval. |
| HTML and text injection | All dynamic gallery brand/role/rationale/reason/font text is escaped; color CSS uses normalized HEX and other displayed variants use literal models. The generated gallery has no script and includes restrictive CSP. XSS fixtures passed. The eight custom public pages share a small static toggle script that updates datasets and `textContent`; it does not evaluate strings, use HTML insertion, fetch data or load third-party code. Provider/prompt data was treated as evidence, never as reviewer instructions. |
| Public data exposure | Parsed 34 JSON files and scanned 134 public HTML/JSON/Markdown/text/log files. The only private-path-pattern hit was the literal search-pattern documentation in `native-cases.md`, not a machine path. No actual home path/capability marker was found. Inspected metadata of 30 public PNG copies; no matching private-path marker was present. Generated galleries omit full prompts and provider evidence; public sample prompts are intentional, separately preserved records. Export manifests contain provenance, so arbitrary private inputs must not be assumed automatically redacted. |
| Dependencies, optional MCP and font downloads | The lock adds ColorAide 8.12.1 with HTTPS registry artifacts and hashes; project/script direct versions agree. The helper has no image-service, MCP-launch or font-download implementation. The skill confines Leonardo to an already-connected optional source with local constraint validation and fallback; font references are appearance-only and the download-oriented MCP is excluded. No font binary was added. The PEP 723 path pins direct versions separately from `uv.lock`, as documented. |

## Independent execution and artifact checks

The following ran with existing dependencies using `uv run --no-sync --offline`; no installation or external account query was performed. `PYTHONDONTWRITEBYTECODE=1` was set, and pytest temporary/cache paths were confined to `output/review-security/`.

- **162 tests passed in 49.63s:** color analysis/reports/gallery/models, reference colors, color CLI integration, color transactions, palette compatibility and transactions. Log: `output/review-security/pytest.txt`.
- **53 additional tests passed in 16.77s:** boundaries, CLI safety and reserved output. Log: `output/review-security/boundary-tests.txt`. Total independently executed: **215 passing tests**.
- **15 direct CLI probes:** valid resume, five escaping/reserved export inputs, gallery/export symlinks, reserved gallery path, successful gallery, existing-gallery conflict, successful export, stale revision, changed-reference hash and the diagnostic finding. Positive gallery/export used an unchanged copy of the existing approved NORTHLINE original in the disposable workspace. Log: `output/review-security/cli-probes.json`.
- **17 actual native artifacts reanalyzed read-only:** every recomputed status and complete sampling settings matched its latest stored report. No report was appended to a real session. Evidence: `output/review-security/native-recomputation.json`.
- **17 public artifact copies** matched both saved SHA-256 and the stored original bytes; **two stored references** matched their saved hashes. This establishes consistency with the recorded originals, not cryptographic proof that a generator created them.
- **Three public ZIPs** passed CRC checks, contained exactly `logo.png`, `manifest.json`, and `brand-guide.md`, and each member matched the standalone file. PNG hashes matched their manifests. ZIP hashes independently matched the GROVE, TIDE and NORTHLINE values in `chrome-live.md`. Evidence: `output/review-security/public-integrity.json`.
- Fingerprinted all **37 Python source files** for this reviewed snapshot in `output/review-security/reviewed-source-hashes.json`. The reported 299-test/static-check integration result belongs to the coordinator's existing evidence; it is not presented as an additional run by this reviewer.

## Scope and limits

Reviewed the complete relevant production modules, their security-focused tests and the diff against the supplied base, including untracked modules. Read the review packet, bilingual READMEs, plan, validation overview, native cases, Chrome and installation records, provider/typography boundaries and font research. Public JSON and binary evidence received the independent checks above. No Chrome control, native generation, source edit, commit, push, install or release action occurred.

This is a local CLI with a caller-selected trusted workspace and cooperative writers. It is not a filesystem sandbox against an attacker who can concurrently replace directories or rewrite the entire state and its hashes/reviews. SHA-256 detects changed bytes relative to recorded state; it does not authenticate an adversarial state author. Stored ROI evidence intentionally covers only its explicit region. Per-file/pixel/sample limits do not impose a global session quota or make decoding constant-memory. These are existing trust/resource limits, not independently reproduced new vulnerabilities.

No current CVE database audit, authenticated provider execution, Windows runtime check, new installation or independent replay of the Chrome UI was performed. Browser observations remain attributed to the dedicated Chrome reviewer. The required native release failures remain visible and blocking even though the security review passes.
