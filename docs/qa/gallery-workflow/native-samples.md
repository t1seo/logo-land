# Native sample workflow evidence

Status: PASS for the requested creative workflow and artifact-serving checks. Eight native originals are retained: six independent initial candidates and two targeted child edits. Visual observations remain mixed where the outputs differ from intent; no artifact is selected, reviewed for export or approved.

## Provenance and scope

- Task: T2 native samples, approved Logo Land first milestone; branch `feat/logo-land-gallery-workflow`.
- Tool: `image_gen__imagegen`, host native image generation. Model and seed are unreported; no model, size, quality, output-path, polling or batch-count argument was invented.
- Every call had a durable planned/running receipt before invocation, then returned/imported events. Exact tool-returned paths remain in the ignored private receipts; public receipts retain native basenames, hashes, decoded facts and portable image/prompt references.
- New images used only `prompt`. Both edits used `prompt` plus one exact helper-returned `referenced_image_paths` entry, reopened through `view_image` before the call.
- Initial Leaflet ran alone; the other five initials ran concurrently with isolated sessions/receipts. A coordinator note capping initial concurrency at two was read only after that batch finished; this deviation was reported. Both children waited for native-size and 32/64/128px parent inspection, then ran independently. No rerolls or hidden retries occurred.
- All originals were viewed through `view_image` at original size. Temporary display-only 32/64/128px copies were made with `sips -Z` and viewed separately; originals were never resized, recolored or edited by scripts.
- Helper source and tests were not edited. This creative-only task adds no source/test or LSP/build obligation; repository implementation QA belongs to the coordinator.

## Actual native calls

Each link contains the complete exact submitted prompt, not a reconstruction. Generation/import revisions are the actual helper responses; the comparison uses the current revision for every artifact in each session.

| ID | Mode / parent | Prompt revision → import revision | Current revision | Actual PNG | Receipt |
|---|---|---|---|---|---|
| [leaflet-v1](../../gallery-workflow/images/leaflet-v1.png) | independent initial | 0 → 1 | 1 | 1254 × 1254, RGB | [receipt](../../gallery-workflow/receipts/leaflet-v1.json) |
| [drip-v1](../../gallery-workflow/images/drip-v1.png) | independent initial | 0 → 1 | 1 | 1254 × 1254, RGB | [receipt](../../gallery-workflow/receipts/drip-v1.json) |
| [relay-v1](../../gallery-workflow/images/relay-v1.png) | independent initial | 0 → 1 | 2 | 1254 × 1254, RGB | [receipt](../../gallery-workflow/receipts/relay-v1.json) |
| [relay-v2](../../gallery-workflow/images/relay-v2.png) | edit / relay/v1 | 1 → 2 | 2 | 1254 × 1254, RGB | [receipt](../../gallery-workflow/receipts/relay-v2.json) |
| [teum-v1](../../gallery-workflow/images/teum-v1.png) | independent initial | 0 → 1 | 1 | 1254 × 1254, RGB | [receipt](../../gallery-workflow/receipts/teum-v1.json) |
| [sprig-v1](../../gallery-workflow/images/sprig-v1.png) | independent initial | 0 → 1 | 2 | 1254 × 1254, RGB | [receipt](../../gallery-workflow/receipts/sprig-v1.json) |
| [sprig-v2](../../gallery-workflow/images/sprig-v2.png) | edit / sprig/v1 | 1 → 2 | 2 | 1254 × 1254, RGB | [receipt](../../gallery-workflow/receipts/sprig-v2.json) |
| [common-v1](../../gallery-workflow/images/common-v1.png) | independent initial | 0 → 1 | 1 | 1774 × 887, RGB | [receipt](../../gallery-workflow/receipts/common-v1.json) |

| ID | Exact prompt SHA-256 | Native output SHA-256 |
|---|---|---|
| [leaflet-v1 prompt](../../gallery-workflow/prompts/leaflet-v1.txt) | `0cad98ad36526c630cf05aa5fdde33d14e87a5545d1302f4be6ba4628e14faf5` | `256b1ee1e25d9d8160ec0751db1453ae31990cecb5c2cd68570410c668cb6b4e` |
| [drip-v1 prompt](../../gallery-workflow/prompts/drip-v1.txt) | `67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d` | `8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f` |
| [relay-v1 prompt](../../gallery-workflow/prompts/relay-v1.txt) | `68f8163701caf21ec0e3c06b43128ff5f4fbc6c67183d5a8649a13e58f7ea813` | `6588c675013483c18bcc5fad4986c60e0ec21a78ef7c7591d055e2bb2b620b58` |
| [relay-v2 prompt](../../gallery-workflow/prompts/relay-v2.txt) | `7c970c80e2167fb7677c82a3ffb360e17ad6569a28b341d881952fabbcd87cef` | `a4066faa64d1f58024d1a44afb011694a1808b628b988ac71a0986e90069491d` |
| [teum-v1 prompt](../../gallery-workflow/prompts/teum-v1.txt) | `8312812f546902472a7eb0d98311e3e6c1b29fe58ba8a6d55cb826c61e03721c` | `a97780b67a304853d1b8795d6d3af8efdc4658d36703ed1cdabfa8710b73bf7e` |
| [sprig-v1 prompt](../../gallery-workflow/prompts/sprig-v1.txt) | `9965898ff25f67a25e10e8002c7037852b7b6b99d0ca4b5a66513edd24c85094` | `956577408a1a8986dd87cf430e44451739d93285352c5ebe5305d19ae216e222` |
| [sprig-v2 prompt](../../gallery-workflow/prompts/sprig-v2.txt) | `b83d6deeea4f252a27962f1171618ce72e58e7e807c0e6e9c6ba7b2652e6f22a` | `ed16c756532ef268880f4a1d281d87323bef707cecfe3c41b41397bef74e65ac` |
| [common-v1 prompt](../../gallery-workflow/prompts/common-v1.txt) | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` |

Child input SHA-256 equals the preserved parent output:

- Relay v2 input: `6588c675013483c18bcc5fad4986c60e0ec21a78ef7c7591d055e2bb2b620b58` (relay/v1).
- Sprig v2 input: `956577408a1a8986dd87cf430e44451739d93285352c5ebe5305d19ae216e222` (sprig/v1).

The requested approximately 1536-square icon size was prompt text. Actual icon returns were 1254 × 1254; COMMON was 1774 × 887. All eight decoded as RGB PNG with no transparent pixels. Native source files, public originals, helper imports and comparison/download copies match exactly.

## Original and child observations

### Leaflet / reading fox / v1

- Reason: A fox holding a book gives the reading companion a warm, visible reading cue.
- Preserve: Friendly face, broad closed book, apricot/navy identity and large lower-left emphasis.
- Requested change: No child requested.
- Observed: Original: friendly upright fox visibly holds a book; face and ears remain clear, with space at the right. At 32px the book merges with the body and the hands read more clearly than its pages. Cream muzzle, inner ears and tail introduce a third character color family; shading and extra contours exceed the two-color, few-shape intent. No lettering is visible.

### Drip / water reminder / v1

- Reason: A droplet and a broad waterline communicate a simple hydration reminder.
- Preserve: One cobalt droplet, rounded tip and open pale-blue wave-shaped interior.
- Requested change: No child requested.
- Observed: Original: one centered cobalt droplet surrounds a broad pale-blue water cue; no text, decorative pieces or external shadow. At 32px the drop and wave opening remain legible, while the right interior tip becomes thin. Subtle raster tonal variation remains despite flat-color intent.

### Relay / quiet handoff / v1

- Reason: Two offset receiving arcs suggest a quiet handoff without a literal arrow.
- Preserve: Exactly two broad offset open arcs, pine upper-left and terracotta lower-right, same arc centers and visual weight, shared curvature and ivory background; no text, arrows, dots or dimensional effects.
- Requested change: Widen only the central diagonal passage by about one third at its closest clearance: trim back the two inward-facing ends without moving the arc centers or thinning the bodies; keep both arcs open and the overall offset gesture.
- Observed: Original and 32/64/128px: both arcs already read as separate open forms. The central diagonal clearance is the most compact part of the gesture and gives less breathing room than the open outer ends; this is a useful refinement, not a failed initial. Flat-color intent still has subtle raster texture.

### Relay / quiet handoff / v2

- Reason: Child of relay / v1. Two offset receiving arcs suggest a quiet handoff without a literal arrow.
- Preserve: Exactly two broad offset open arcs, pine upper-left and terracotta lower-right, same arc centers and visual weight, shared curvature and ivory background; no text, arrows, dots or dimensional effects.
- Requested change: Widen only the central diagonal passage by about one third at its closest clearance: trim back the two inward-facing ends without moving the arc centers or thinning the bodies; keep both arcs open and the overall offset gesture.
- Observed: Mixed refinement: the central diagonal passage is visibly wider in the original and at 64/128px; at 32px the difference is modest because v1 was already open. Both pine/terracotta arcs, ivory field and nonliteral gesture survive. The terracotta inner end moved left and its curvature/extent changed beyond a pure end trim, so arc-center preservation is not exact. No added text, arrows or dots; subtle raster texture remains.

### 틈 / notes / v1

- Reason: The exact Korean syllable 틈 expresses a small space reserved for a note.
- Preserve: Exact 틈 glyph structure, bold aubergine strokes, open lower counter and butter-yellow background.
- Requested change: No child requested.
- Observed: Original: the single syllable reads 틈, with distinguishable ㅌ, ㅡ and ㅁ components and no added text. At 64/128px the counter and horizontal spaces are clear; at 32px the narrow horizontal gaps become compressed but remain visible. Rounded heavy lettering is observed appearance, not verified font composition.

### Sprig / gentle plant care / v1

- Reason: A single tactile leaf connects a gentle daily-care product to plant growth.
- Preserve: One asymmetric jade leaf, pointed upper-right tip, single shallow fold, matte soft material, restrained green shading, near-frontal view and blush background.
- Requested change: Clarify only the bottom leaf-to-stem contour: narrow the join slightly and give the existing short stem a small leftward bend so its short hooked silhouette stays distinct from the leaf body at 32px; retain the leaf tip, overall scale, material and color identity.
- Observed: Original and 32/64/128px: the pointed asymmetric silhouette already reads as a leaf rather than a heart. At 32px the nearly straight short stem blends into the central fold; making that connection more distinct is an incremental recognition refinement. Fine surface grain is visible in the original despite a simple matte-surface request.

### Sprig / gentle plant care / v2

- Reason: Child of sprig / v1. A single tactile leaf connects a gentle daily-care product to plant growth.
- Preserve: One asymmetric jade leaf, pointed upper-right tip, single shallow fold, matte soft material, restrained green shading, near-frontal view and blush background.
- Requested change: Clarify only the bottom leaf-to-stem contour: narrow the join slightly and give the existing short stem a small leftward bend so its short hooked silhouette stays distinct from the leaf body at 32px; retain the leaf tip, overall scale, material and color identity.
- Observed: Mixed, mostly unchanged recognition: the lower join is slightly narrower and the stem transition looks cleaner, while the asymmetric leaf tip, jade shading, matte texture and blush field survive. The requested leftward stem bend is not clearly realized; the stem still leans right. At 32px it reads essentially the same recognizable leaf as v1, so no demonstrated small-size recognition gain is claimed.

### COMMON / shared workspace / v1

- Reason: An open meeting-space symbol and shared table convey an inviting workspace beside a readable name.
- Preserve: Exact COMMON uppercase lettering, left-hand open charcoal U symbol with terracotta table, horizontal lockup and ivory background.
- Requested change: No child requested.
- Observed: Original: COMMON is spelled C-O-M-M-O-N in one horizontal line; a separate open U-shaped space and terracotta table sit to its left with a readable gap. Letter counters are open and no slogan is present. The whole lockup stays readable around 128px wide, becomes tiny at 64px and is unsuitable as a 32px favicon; its intended use is a wider header. Subtle surface variation is visible, and no actual font-file usage is established.

## Helper lineage and publication

- Used real `init`, `prompt`, `import` and `show` commands for six distinct sessions in `output/gallery-workflow-native/workspace`. Initial prompts used revision 0 and imports returned revision 1; child prompts used revision 1 and imports returned revision 2. No `select`, `review` or `export` was used.
- Final selection: [selection-final.json](../../gallery-workflow/inputs/selection-final.json). Relay and Sprig v1/v2 all use current revision 2; other entries use revision 1. [Initial revision-1 selection](../../gallery-workflow/inputs/selection-initial-r1.json) remains historical.
- Actual publication command: `.venv/bin/python skills/logo-land/scripts/logo_project.py --workspace output/gallery-workflow-native/workspace compare-gallery --selection-file output/gallery-workflow-native/workspace/selection-final.json --output comparison`.
- The helper generated the complete 18-file portable result. It was copied byte-for-byte to [comparison/index.html](../../gallery-workflow/comparison/index.html); no replacement gallery was hand-authored. One helper rebuild added explicit child-of labels to decision data; its earlier selection and gallery remain privately retained.
- Two evidence-assembly errors were corrected without native reruns: COMMON omits optional null `app_icon` in stored JSON, and comparison results return workspace-relative paths. The first premature manifest-ready status was corrected immediately, followed by a verified ready status only after the file existed.
- [Publication receipt](../../gallery-workflow/receipts/comparison-publication.json) records every copied-file digest and session-state digest. [Final show receipt](../../gallery-workflow/receipts/final-show.json) confirms all six live sessions remain byte-identical after comparison/adversarial checks, with null selection and reviews.
- [Portable snapshots](../../gallery-workflow/states/README.md) preserve unmodified helper states plus relative original/prompt bindings. All six were reconstructed in a registered temporary workspace and passed real helper `show` with equal state, image hashes and prompt strings. See [portable integrity](../../gallery-workflow/receipts/portable-integrity.json).

## Actual HTTP channel

Served `docs/gallery-workflow` at `127.0.0.1:8791` using the registered Python HTTP server. Ran exactly:

```sh
curl -i --fail --max-time 20 http://127.0.0.1:8791/comparison/index.html
```

- Result: `HTTP/1.0 200 OK`, exit 0; body equals the published index byte-for-byte. SHA-256: `7d90d12a54e901d2b6033a062103870efbd5ab1104108cc563c2b3d69759496c`.
- Parsed eight unique source identities from the served HTML and checked their revisions. Both explicit child labels are present; the served exact manifest independently binds relay/v2 → relay/v1 and sprig/v2 → sprig/v1 at current revision 2.
- Downloaded all eight original PNGs and all eight exact prompts with bounded `curl`; every byte sequence and SHA-256 matches its native original/exact prompt and both public manifests.
- Full evidence: [HTTP receipt](../../gallery-workflow/receipts/http-verification.json). Private raw header/body response and server log are retained under the ignored native output directory.
- Browser layout, controls and desktop/narrow viewport review are reserved for coordinator T4; this worker did not control Chrome.

## Nine adversarial classes

| Class | Actual evidence / disposition |
|---|---|
| Malformed input | Comparison with revision -1 and with absent artifact `missing` each returned nonzero and created no output directory. |
| Prompt injection | Passed shell metacharacters and script markup as argv/JSON data; no sentinel file was created. HTML escaped the markup, and helper prompt kept quoted data before authoritative constraints. No native injection experiment was added. |
| Cancel/resume | All eight receipts recorded planned/running before calls and returned/imported after. Destructive cancellation of a costly native call is N/A; no call was cancelled or resubmitted for testing. |
| Stale state | Relay revision 1 selection was refused after its current revision became 2, with no output. Final selections and all six final `show` responses use actual current revisions. |
| Dirty worktree | Baseline inventory captured 223 existing sample/assets files and 66 helper source/reference files. Older image/prompt bytes stayed unchanged; four category README files changed through the separate docs worker. No unowned edits were reverted. |
| Hung commands | Helper subprocesses had 30-second bounds; curl used 20 seconds with an outer 25-second bound. Native calls used the required 120-second exec-yield setting; orchestration heartbeats reported liveness. No native hang occurred and no polling API was invented. |
| Flaky tests | No source tests were added or rerun for this creative task, and no image was regenerated to mask artistic variance. Two local evidence assembly errors are disclosed above. |
| Misleading success | Eight returned originals have verified paths, hashes, PNG facts and original/small-size observations. Leaflet extra colors, Relay geometric drift and Sprig unachieved hook are recorded; tool return does not imply quality acceptance, color compliance or approval. |
| Repeated interruptions | Receipt IDs and artifact IDs remained stable through status messages and metadata corrections. No unknown native attempt was reset; destructive repeated-interruption testing is N/A for the paid/limited creative calls. |

Actual refusal/injection receipts: [adversarial-checks.json](../../gallery-workflow/receipts/adversarial-checks.json). Helper state and original bytes stayed unchanged throughout.

## Cleanup and limits

- Registered teardown before creating `/tmp/ll-060-native-http` and before starting the HTTP server; owned PID `72733` was verified, stopped and port 8791 was confirmed released.
- Removed the owned temporary root, all 24 display previews, 16 downloaded files, restored snapshot workspace and the injection comparison directory. No temporary scripts were left. See [cleanup receipt](../../gallery-workflow/receipts/cleanup.json).
- Intentionally retain `output/gallery-workflow-native/` as the resumable private project and `docs/gallery-workflow/` as public originals/prompts/receipts/snapshots/gallery. No commit, push, installation or browser action was performed.
- These fictional samples demonstrate workflow, not a controlled model benchmark, certified export, actual font composition, vector delivery, trademark finding or platform-ready app package. Exact HEX fidelity and full export review were not certified. All candidates remain unapproved.
