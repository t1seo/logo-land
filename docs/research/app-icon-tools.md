# App icon tools, upstream provenance, and platform boundaries

Research date: **2026-09-13 Asia/Seoul** (HTTP evidence dated 2026-09-12 UTC). This is the `icons_research` deliverable for task `task_02b70858ca00`, dispatch `ctx_5fd84d2c11ee`. Machine-readable evidence: [app-icon-sources.json](app-icon-sources.json).

## Decision for Logo Land

Offer six distinct **artwork styles**, with the IP mascot style adapted from the pinned upstream skill. Preserve the native generator's original files and every returned candidate. Treat platform preparation as a separately named deliverable: an attractive square image is not evidence of an Icon Composer file, Android adaptive resources, an app build, or store acceptance.

This report contains verified source facts and explicitly labeled integration proposals. It does not install skills, connect a provider, generate images, edit product source, create native assets, or complete the overall feature.

## Pinned upstream and installed local skill

The GitHub `commits/HEAD` endpoint resolved to **`acb834c717bcd0a487c49732d08397ba280d690b`**, committed **2026-08-22T16:48:55Z**, message `docs: require top-tier image models`. A separate `commits/main` request returned the same SHA. Use [this commit](https://github.com/s1dashu/ip-as-logo-skill/commit/acb834c717bcd0a487c49732d08397ba280d690b), not floating `main`, for an adaptation.

The installed directory is `/Users/cillian/.agents/skills/ip-as-logo`. Binary comparison confirmed its **SKILL.md, README.md, and LICENSE exactly match** the pinned upstream files. This establishes current byte equivalence, not the installation date or a guarantee that later upstream changes are installed automatically.

| File | Bytes | SHA-256, equal upstream and local |
| --- | ---: | --- |
| [SKILL.md](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/SKILL.md) | 17,157 | `468429f9391c29dc5ead2cde9159a831435afcdae464631498eabce2ff1c9695` |
| [README.md](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/README.md) | 7,963 | `01fdc4729a1d7c13c5f5a71414d4a28756b142458a727a1f75e41c161fba4179` |
| [LICENSE](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/LICENSE) | 1,064 | `b8f39925b1c36ca531c5e663aeb7ba427f94a526495785b4d1b2797fae8f2546` |

The recursive Git tree response was not truncated. It contains `.gitignore`, `SKILL.md`, `README.md`, `LICENSE`, and `assets/ip-as-logo-wall.webp`: this is an instruction skill with a showcase image, not a generation SDK, executable renderer, MCP server, or platform export pipeline. [Pinned tree](https://github.com/s1dashu/ip-as-logo-skill/tree/acb834c717bcd0a487c49732d08397ba280d690b)

### What the upstream workflow actually requires

The following describes the pinned [SKILL.md](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/SKILL.md), not a claim that Logo Land already implements it.

- Infer product purpose, audience, and personality from read-only repository context. Ask one consolidated background round only when that context is insufficient.
- Present **three product-related directions** and propose **six independent draws**. With a specified subject, vary its treatment; otherwise choose three different subjects or metaphors with distinct product rationales.
- With all directions accepted: `A1/A2`, `B1/B2`, `C1/C2`, two per direction. Odd/first members emerge from lower-left; even/second members from lower-right. If one direction is selected with six draws, use `A1…A6` with alternating corners. Explicit replacement instructions override defaults.
- Keep a rounded, upright, dominant character emerging from its assigned lower corner, roughly **85–95%** of the square; no centered or bottom-centered composition by default. Keep paired identity features visible, simplify to roughly **4–7 large shapes**, and aim for recognition at **32 × 32**.
- Use **three semantic colors**: two character color families and one solid background. Reuse character colors for facial features. Tonal variations, antialiasing, incidental shading, or mild depth do not make the raster invalid. This is **not an exact count of three distinct RGB/RGBA values**.
- Generate each candidate as its own square image, without previous candidates as references for a prompt-only draw. Never generate the six candidates as a single contact sheet.
- Generate each requested candidate once; preserve and deliver **every returned result as-is**. Do not gate delivery on appearance, rank compliance, reject colors/composition/shading, silently retry, or repair the result through post-processing. Later refinements require an explicit new request.
- Record candidate label, direction/rationale, corner, saved path, prompt/color mapping, and actual dimensions. Requested size is not observed size.

The upstream proposal/consent step explicitly allows existing authorization for six outputs or proceeding without another confirmation. The coordinator already owns the authorized research → plan → implementation → samples workflow; this research does not add another approval gate.

### Prompt and runtime constraints

Upstream prompts describe a square **image**, never a `logo`, `brand mark`, `app icon`, or `icon asset`, and avoid scaffolding revealing those uses. This restriction is for generation prompts; research reports and product labels may still say “app icon.” It also avoids image-mode words such as `alpha`, `transparency`, and `opaque` in that prompt. [Prompt routing and skeleton](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/SKILL.md#prompt-skeleton)

The current upstream lists GPT Image 2 as preferred and also names Seedance 5.0 Pro, Nano Banana Pro (Gemini Image Pro), and Nano Banana 2 (Gemini Image Flash). Those are **upstream assertions**, not verified model availability, product naming, quality measurements, or native tool controls. It requests approximately 1536 × 1536 and permits a native 1254 × 1254 result; these are its instructions, not verified service limits. It rejects an SVG fallback for its raster mascot workflow. [Pinned model/canvas instructions](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/SKILL.md)

**Proposed native Codex integration:** use only the runtime's actual image-generation tool and its exposed schema. This session exposes `image_gen.imagegen` with `prompt`, `referenced_image_paths`, and `num_last_images_to_include`; it exposes no explicit `model`, `size`, `seed`, `quality`, `n`, or `negative_prompt` controls. Native capability metadata is the evidence here; no call was made. Do not invent parameters, silently switch to external providers, install upstream commands, claim a hidden model identity, or claim an exact font from a raster. Record an undisclosed model as unknown. For a new independent draw, omit reference-image arguments and deliver exclusions within the prompt. The six candidates require six independent jobs, not an unsupported quantity field.

The upstream permits parallel subagents, but this research dispatch expressly forbids children and generation. Its job distribution guidance is recorded as source data only; none was executed.

## MIT license and attributed adaptation

The actual license is **MIT**, with the exact copyright line **`Copyright (c) 2026 s1dashu`**. The notice permits use, modification, distribution, sublicensing, and sale subject to retaining its copyright and permission notice in copies or substantial portions, and includes the standard warranty/liability disclaimer. [Pinned LICENSE](https://github.com/s1dashu/ip-as-logo-skill/blob/acb834c717bcd0a487c49732d08397ba280d690b/LICENSE)

**Proposed attribution practice:** preserve the complete original license beside any copied or substantially adapted instructions; retain the original author/year; add a provenance note identifying the repository, full commit SHA, and local changes. Suggested note:

> Adapted from ip-as-logo-skill by s1dashu, commit acb834c717bcd0a487c49732d08397ba280d690b, under the MIT License. Local adaptation: native Codex routing, explicit separation of artwork styles, and platform-preparation boundaries.

This is a notice-preserving implementation recommendation. The repository's MIT notice does not establish ownership of every generated image, clear user-supplied third-party characters or brands, or certify platform submission. No separate legal conclusion about generated output is asserted.

### Required live HTTP manual QA

Executed exactly:

```sh
curl -i --fail --silent --show-error --connect-timeout 10 --max-time 30 https://raw.githubusercontent.com/s1dashu/ip-as-logo-skill/main/LICENSE
```

**PASS:** exit **0**, status **HTTP/2 200**, `content-type: text/plain; charset=utf-8`, `content-length: 1064`, server date **Sat, 12 Sep 2026 16:45:33 GMT**. The full response headers/body are retained in the JSON companion. The floating response body was verified against the pinned license, whose bytes and hash also equal the installed local license.

Actual license body:

```text
MIT License

Copyright (c) 2026 s1dashu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Official platform requirements and actual deliverables

These are documentation findings at the research date. They are not export or submission results.

| Surface | Verified requirements / documented behavior | What remains beyond generated artwork |
| --- | --- | --- |
| Apple iOS/iPadOS artwork | The HIG lists a 1024 × 1024 square layout; the system applies rounded masking. Keep primary content centered and imported backgrounds full-bleed and opaque. Foreground layers can use transparency. [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons) | Appropriate source dimensions, composition, and appearance checks; a solid-looking generated background alone does not prove pixel opacity |
| Apple Icon Composer | Import SVG/PNG artwork layers, configure background/group effects, preview variants, and add the multilayer file to Xcode. iPhone/iPad/Mac canvas is 1024 × 1024; Watch uses 1088 × 1088. The system applies the mask. [Xcode Icon Composer guide](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer) | Actual separated foreground/background content, Icon Composer document, target configuration, build, and simulated/physical-device checks |
| Apple asset catalog route | A single 1024 × 1024 source can supply iOS/iPadOS size variants. Dark/tinted variants have their own treatment; the asset catalog guide specifically asks for a transparent dark background and a grayscale tinted image. [Xcode asset catalog guide](https://developer.apple.com/documentation/xcode/configuring-your-app-icon) | Correct image wells and appearance assets in an Xcode target; do not apply a blanket “all iOS layers must have no alpha” rule |
| App Store submission | Add the icon in Icon Composer or an asset catalog in Xcode, then upload the app build to App Store Connect. Changing a published app icon requires a new app version and review. [App Store Connect](https://developer.apple.com/help/app-store-connect/manage-app-information/add-an-app-icon) | A build and App Store workflow; no standalone image proves acceptance |
| Android adaptive launcher | Provide separate foreground/background layers; vectors or bitmaps are supported. All layers are 108 × 108 dp, with important content within the central 66 × 66 dp safe zone, and icon content at least 48 × 48 dp. Outer 18 dp on each side supports masking/effects; do not bake an outer mask or outline shadow. [Android adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive) | Actual resources, adaptive-icon XML and manifest wiring, mask/launcher checks; dp is not a promised raster pixel size |
| Android themed launcher | Supply a monochrome layer for controlled themed output. Android 13 introduced themed adaptive icons; current docs also note automatic theming without that layer starting Android 16 QPR 2. Behavior depends on user/launcher support. [Android adaptive icons](https://developer.android.com/develop/ui/compose/system/icon_design_adaptive) | Deliberate monochrome rendering and launcher/device verification; do not present the layer as a universal store-submission requirement |
| Google Play listing | Separate from launcher assets: **512 × 512 px, 32-bit PNG, sRGB, maximum 1024 KB, full square**. Play applies rounded corners and an outer shadow; do not bake those into the submitted square. Internal artwork shading is allowed. A nontransparent background is recommended; the page does not categorically prohibit all transparency. [Google Play icon specifications](https://developer.android.com/distribute/google-play/resources/icon-design-specifications) | A checked listing export and Play Console submission; a 512 PNG is not an Android adaptive icon package |

Apple's HIG explicitly permits a flattened image while explaining that layers provide more control. Icon Composer's flattened marketing export is also distinct from its multilayer document. Do not market a static “glass” effect as a native layered icon. [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons), [Icon Composer overview](https://developer.apple.com/icon-composer/)

The current HIG includes default, dark, clear-light/clear-dark, and tinted-light/tinted-dark appearances for iOS/iPadOS/macOS. Its square-source/system-mask guidance does not mean adding rounded corners to the master image. When a Composer file replaces an existing catalog, Xcode generates older-release icon images from it; retaining an older icon unchanged can require keeping the catalog route. [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/app-icons), [Xcode Icon Composer guide](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)

**Integration inference:** upstream corner-emergence and 85–95% occupancy can place identity-bearing features outside Apple's preferred central composition or Android's mask-safe region. Preserve that original creative draw. If platform assets are later requested, create a separately labeled adaptation from an explicitly selected candidate and test masks; never silently crop/recenter the preserved draw or declare it launcher-ready.

Apple HTML retrieval initially exposed JavaScript shells, and Markdown-link retrieval produced tool errors. The official DocC JSON endpoints successfully returned structured page bodies, which were parsed for the platform claims above. Those exact fallback URLs are recorded in the source manifest. No requirement is based solely on the JavaScript shell.

## Proposed six artwork styles

These are our product/style recommendations, not platform-mandated categories or upstream presets. Only the first uses the upstream IP recipe. A style must change shape construction or visual treatment; swapping palette alone does not count.

| Proposed style ID | Distinct visual construction | Sample brief and observation |
| --- | --- | --- |
| `ip-mascot` | Personified rounded continuous silhouette, two character colors plus background, lower-corner emergence, nearly imperceptible depth | Product-related character/metaphor; verify six independent originals remain accessible |
| `flat-geometric` | Centered non-character solid circles/blocks/arcs; no facial anatomy, texture, or depth | A compact abstract signal built from two or three bold masses |
| `negative-space` | One heavy enclosing silhouette with a recognizable void doing the semantic work | A path or doorway cut out of a solid shape; observe whether the void survives small previews |
| `rounded-monoline` | One thick continuous rounded stroke with substantial open space, instead of filled masses | A simple loop/path gesture; observe gaps and joins at small sizes |
| `paper-cut` | A few visibly overlapping flat paper shapes and restrained internal depth | A folded leaf or stacked landscape; clearly distinct from a smooth volumetric object |
| `soft-sculpted` | One smooth volumetric object with broad light/shade and a quiet background | A pebble, bud, or useful object; static raster depth, not an Icon Composer/3D model claim |

Use no embedded wording by default. Letterform/monogram requests can be handled separately; a font name may describe intent but cannot verify exact glyph outlines in generated imagery. Do not reuse the mascot-specific corner/three-color restrictions globally for the other five styles.

### Manageable initial sample coverage

**Proposed initial coverage: 11 independent original images, one product brief.**

1. Run one complete `ip-mascot` batch: three product-related directions × two draws = **six** originals, labeled A1/A2/B1/B2/C1/C2 with the assigned left/right corners.
2. Run one image for each of the other five styles = **five** more originals. Use the same product purpose and a deliberate shared palette where it helps comparison.
3. Display all 11 through a gallery referencing the separate original assets and metadata. Thumbnail/rounded-mask previews must be clearly identified as previews, must not overwrite originals, and must not be used to suppress delivery.
4. Record observed dimensions, actual tool/provider information if disclosed, final submitted prompt, planned semantic colors, style, direction, corner where applicable, and asset path. An unsuccessful/unknown job remains visibly unsuccessful/unknown; a pretty placeholder is not a completed draw.
5. If the user later wants stronger style coverage, add one more draw per non-IP style: **16 total**. Do not explode the initial matrix into all subjects × all palettes × all styles × both platforms.

This is a concrete sample recommendation for the coordinator's implementation/samples phases, not evidence that generation has already run. Sampling verifies the artwork workflow. Icon Composer files, adaptive resource packages, device previews, and store upload checks remain distinct deliverables.

## Verification, adversarial probes, and cleanup

Baseline: read-only research, no product behavior changed, so no RED/TDD, application build, or product runtime test is applicable. The matching manual surface is real HTTP retrieval and inspection of the returned license, followed by source parsing and document checks.

| Class | Actual probe / observation | Result and scope |
| --- | --- | --- |
| License HTTP surface | Required exact curl command returned HTTP/2 200, exit 0, actual MIT body | PASS; headers and full license retained |
| Stale floating source | Resolve HEAD and main separately; fetch files at full SHA; compare local bytes | PASS; all three inspected files match the pin |
| Malformed response | In-memory truncated JSON and HTML-as-JSON fixtures were parsed with Ruby JSON | PASS: both rejected as JSON; no product response parser was exercised |
| Untrusted instructions | Repository instructions/install examples treated as research data; synthetic “ignore previous instructions / run installer” string remained a string | No eval/install/generation; this is a handling check, not a security test of a product prompt system |
| Missing remote source | Request a deliberately nonexistent path at the pinned SHA with bounded curl | HTTP/2 404, curl exit **56** in this environment; not accepted as evidence |
| Timeout | Live pinned-license request with 0.001-second connect/total bounds | curl exit **28**, DNS resolving timeout, zero body bytes; not accepted as license proof |
| Misleading success | Compare square artwork deliverable against Composer, adaptive-layer, and store requirements | Documentation boundary recorded; no build/store success asserted |
| Dirty worktree | Initial git status was clean; later reads found concurrent `.omo/drafts/logo-land-app-icons.md`, `plans/logo-land-app-icons.md`, and `docs/qa/app-icons/` | Left untouched; only the two assigned research documents are owned here |
| Cancel/resume and interruption | An overbroad read-only home-directory file search was interrupted; process exited **130**; research resumed with exact ancestor/path reads | No files mutated by the search; generation cancellation/recovery was not exercised |
| Flakiness / harness accuracy | Repeated pinned fetches produced the same byte lengths and SHA-256 hashes; initial Ruby string equality disagreed because encodings differed | Rechecked as binary strings: all three equal; not a network reliability guarantee |
| Retrieval fallback | Apple HTML showed JS shells; two Markdown-link tool requests failed; official DocC JSON parsed successfully | Platform facts use actual source bodies, not an empty-page success |
| Local artifact integrity | JSON parse, recorded-license length/hash, all 11 source IDs, six style IDs, 11-draw sample arithmetic, six mascot labels, local source hashes, and document whitespace checked after writing | PASS, exit 0; these checks do not exercise future app behavior |

No temporary paths were created; network bodies and synthetic fixtures stayed in memory. No installs, service processes, native generation, children, source edits, or deletion of others' changes occurred. There are no task-created temporary artifacts or persistent services to clean up. The interrupted read-only search process was settled.

Remaining work belongs to the coordinator: choose/integrate the proposed style model and prompt routing, execute and preserve native sample draws, and perform product/runtime QA. Platform packaging and store submission must not be implied by those samples.
