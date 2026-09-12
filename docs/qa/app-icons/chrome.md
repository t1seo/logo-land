# Chrome app icon gallery QA

Date: 2026-09-13 KST. Task: `task_ebdc21bdffc4`. Dispatch: `ctx_1c8e695f1937`.

**PASS for gallery behavior and byte-preserving downloads.** Actual external Google Chrome displayed all 11 originals at 32, 64 and 128 px; all six preset filters, masks, surfaces, reset, keyboard controls and the tested download/prompt links worked. This is functional/observational QA, not artistic approval, pixel compliance or platform export approval. Cleanup exception: two identically named blank New Tab windows could not be attributed safely after early focus changes; one may be an early task-created window, so both were preserved and the coordinator was informed.

## Scope and baseline

Read plan T5, sample manifest, native receipts and prior [working Chrome QA](../color-workflow/chrome-live.md). Applied the official macOS Computer Use skill at the locally installed OpenAI bundled computer-use SKILL.md and its documented `@oai/sky` API surface. Applied omo:debugging setup/investigation guidance for the observed fullscreen targeting issue, within the task's read-only, no-children restrictions.

All GUI actions used `tools.mcp__node_repl__js` and the documented Sky API. The exact first Computer Use invocation was `sky.get_app_state({app:'com.google.Chrome'})`. Address bars were set using `set_value` to the full URL, followed by Return. Every action was grounded in fresh app state; control IDs came from the current accessibility tree. No AppleScript, CDP, browser DOM automation, runtime patch, service restart, new image generation or synthetic product test was used.

The collection contains 11 separate original PNGs, 11 exact prompts, six presets and six IP candidates. Each PNG's IHDR is **1254 × 1254**, matching its displayed dimensions and manifest. Each image and prompt hash matches the manifest, and all hashes are present in the corresponding native receipt. The initial convenience lookup of a flat receipt field did not cover the nested ip-c2 and soft-3d receipt layouts; inspecting those nested fields resolved the apparent mismatch. Native image calls by this task: **0**.

## Observed behavior

| Scenario | Actual result | Evidence |
| --- | --- | --- |
| Square / Rounded / Circle | Exclusive selection, visible square / 23% rounded / circular CSS mask; source PNG is preserved | [Rounded](chrome/05-rounded-128-all.jpg), [circle and dark](chrome/06-circle-128-dark.jpg) |
| 128 px | All 11 images viewed while scrolling; no broken images | [Top](chrome/04-http-square-128-all-top.jpg), [IP rows](chrome/07-square-128-ip-01-06.jpg), [middle](chrome/08-square-128-middle.jpg), [bottom](chrome/09-square-128-bottom.jpg) |
| 32 px | All 11 images viewed; subject silhouettes remain, small character details shrink | [Top](chrome/10-square-32-all-top.jpg), [IP](chrome/11-square-32-ip.jpg), [middle](chrome/12-square-32-middle.jpg), [bottom](chrome/13-square-32-bottom.jpg) |
| 64 px / Dark | All 11 originals viewed; dark surrounding surfaces change while their opaque artwork backgrounds remain | [Top](chrome/14-square-64-dark-top.jpg), [IP](chrome/15-square-64-dark-ip.jpg), [middle](chrome/16-square-64-dark-middle.jpg), [bottom](chrome/17-square-64-dark-bottom.jpg) |
| IP mascot filter | Exactly six images, ip-a1/a2, ip-b1/b2, ip-c1/c2, all retained | [Upper](chrome/18-filter-ip-mascot.jpg), [lower](chrome/19-filter-ip-mascot-lower.jpg) |
| Other preset filters | Pictogram, Abstract, Monogram, Soft 3D and Pixel art each show exactly their one image | [Pictogram](chrome/20-filter-pictogram.jpg), [Abstract](chrome/21-filter-abstract.jpg), [Monogram](chrome/22-filter-monogram.jpg), [Soft 3D](chrome/24-filter-soft-3d.jpg), [Pixel art](chrome/25-filter-pixel-art.jpg) |
| Expanded intent | Monogram reports preset monogram, placement center, exact lettering 모, parent None and matching SHA-256 | [Expanded intent](chrome/23-monogram-exact-intent.jpg) |
| Keyboard | From Square: Right → Rounded, Right → Circle, Tab → 128 px, Left → 64, Left → 32, Tab → Light, Right → Dark, Tab → Reset, Space → default Square/128/Light/All | [Before Space](chrome/26-keyboard-circle-32-dark-pixel.jpg), [after Space](chrome/27-keyboard-reset-all.jpg) |
| Exact prompt | Clicked the monogram Exact prompt link, downloaded bytes, and opened the original prompt file URL in Chrome; both exact_lettering and descriptive text preserve 모 | [Prompt file](chrome/29-exact-korean-prompt-file.jpg) |
| Original download | Clicked IP ip-a1 and monogram Download original links in actual Chrome; downloaded PNG hashes equal source | [Filtered completed downloads](chrome/28-downloads-hash-matched.jpg) |
| File URL replay | Rounded, Circle, 32/64/128, Dark/Light, every preset and All were exercised again at the real file URL; image counts were 6/1/1/1/1/1 and 11 for All | Final AX state and [file URL reset](chrome/30-final-file-url-reset.jpg) |
| Cancel / reload / reset | Twice: select Pixel art + 32 + Dark, edit an unsubmitted file URL fragment, Escape to cancel the draft, reload current file, click Reset; each cycle ends Square/128/Light/All with 11 images | Final [reset view](chrome/30-final-file-url-reset.jpg) |

No claim is made that every one of the 22 download links was individually clicked. The actual image/prompt link types were exercised as described, and all 22 referenced image/prompt files were hash checked.

## Actual visual observations

- The six IP images show two baby owls, two capybaras and two puppies holding books, with their distinct colors, poses and backgrounds preserved. At 128 px the faces, ears/wings, hands and book shapes are distinguishable. At 32 px the small eyes, fingers and book details become much less distinct. No candidate was removed, ranked, rejected or regenerated.
- The circular preview cuts away square corners and visibly reduces the lower outer parts of the off-center IP composition, including feet/body edges in the first row. Rounded masks remove less of those corners. These are preview cropping observations, not original-pixel edits.
- Pictogram shows a yellow sun behind a pale cloud on blue. Abstract shows broad blue and coral curved forms on a pale background. Soft 3D shows a green folded heart-shaped leaf on yellow. Pixel art shows a turquoise framed hourglass with coral sand on navy; its stair-step edge detail is reduced at 32 px.
- The sapphire Korean **모** is readable in the 128 and 64 px monogram and remains recognizable in the 32 px view. The expanded intent and original UTF-8 prompt also display the same syllable.
- Browser screenshot dimensions are those returned by Sky; selected CSS display sizes are not a guarantee of physical device pixels. The gallery explicitly states that masks are illustrative and separate platform preparation/validation is required. No Icon Composer, adaptive-layer, app build, store acceptance or strict-color approval was inferred.

## Runtime limits and fallback

The named task window is **App Icons QA ctx_1c8e695f1937**. An early fullscreen AX click reported both Square and Rounded as 1 while the screenshot stayed square; [the raw mismatch capture](chrome/02-fullscreen-ax-mismatch.jpg) is not counted as a pass. A later coordinate action switched to the existing normal Chrome window. A screenshot containing unrelated tabs was discarded immediately without editing its pixels. The cause of the runtime's target selection was not proven; returning to the named task window through Window menu and exiting fullscreen made the same radio action exclusive and visibly correct.

For consistent task-only screenshots, the same untouched gallery was then opened in a normal Chrome window through task-owned localhost port 8783. The initial and final URL were the requested file URL, and all controls were replayed there. Fullscreen was used afterward only for static privacy-clean prompt/final captures, followed by the native View → Exit Full Screen menu. No global service was restarted. Temporary menu capture nulls and stale AX observations were never treated as passing screenshots.

The bounded supplementary command `curl -i --fail --connect-timeout 2 --max-time 10 http://127.0.0.1:8783/index.html` returned HTTP 200; it is connectivity evidence only. Server logs show HTTP 200 for the gallery, all 11 images and tested downloads. Chrome also requested absent `favicon.ico` and received 404, which did not break any gallery image or control.

## Adversarial coverage and limits

| Class | Result |
| --- | --- |
| Unicode / exact text | 모 matches image, intent and downloaded/viewed prompt |
| Executable metadata | Supplemental read-only HTML inspection found 0 script tags, 0 inline event attributes and 0 javascript: href/src URLs; metadata is rendered as text. No injection fixture was written |
| Stale controls / hidden candidates | Multiple filter transitions, keyboard reset and two file reload/reset cycles each restore all 11 |
| Dirty worktree | Existing source/document changes were observed before QA and preserved; this worker wrote only this report and raw screenshots in the repository |
| Misleading success | AX/fullscreen mismatch and HTTP favicon 404 are disclosed; HTTP success and attractive previews were not substituted for GUI or platform approval |
| Bounded / interrupted actions | GUI calls bounded at 30 seconds; user-changed-state responses prompted re-grounding; no repeated image generation or process restart |
| Actual transport cancellation / killed generation | Not applicable: this read-only GUI task made no native calls and killed no generation process; the performed cancellation was an unsubmitted browser URL draft |
| Malformed helper inputs / transaction rollback | Not applicable to this read-only GUI; separately owned core evidence remains in [core.md](core.md) |
| Build / LSP / synthetic tests | Not applicable to Markdown/JPEG-only work; integrated implementation checks remain coordinator-owned |

## Source hashes before and after

All **24 files** below (11 images, 11 prompts, manifest and HTML) were hashed before real interaction and again after the interaction/download/cleanup sequence. Every before/after pair is equal.

- index.html: `e87c1e9d3a78b6404d5560d8e778e8ef812618e7f13d1e7ed7a1d3b18e74a1bd`
- manifest.json: `fe6b2183a34beadf3932f00a63999ba17015792f15f87511b14a0ed9d9801dc9`

| Original | PNG SHA-256, before = after | Prompt SHA-256, before = after |
| --- | --- | --- |
| ip-a1 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| ip-a2 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| ip-b1 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| ip-b2 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| ip-c1 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| ip-c2 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| pictogram | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| abstract | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| monogram | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| soft-3d | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
| pixel-art | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |

## Downloads and cleanup

Before any download, the matching names in Downloads were absent. Registered exact test filenames were ip-a1.png, monogram.png and monogram.txt; each was created by clicking the actual Chrome gallery link. Their SHA-256 values matched the table above. Each was re-hashed immediately before removing that exact test copy; afterward all three names were absent. Unrelated download files and history entries were untouched.

Temporary localhost registry was written before launch: 127.0.0.1:8783, root docs/app-icons, foreground PID **40419**, exec session **94517**, stdout/stderr captured in the exec session only, no log file. The PID was recorded immediately before exec. After QA, only PID 40419 received SIGTERM; session exited 143 as expected, and `lsof -nP -iTCP:8783 -sTCP:LISTEN` returned no listener. No HTTP server or log file remains.

One known temporary QA tab was registered, used for filtered download history and original prompt viewing, and closed. The named persistent task window contains exactly **one gallery tab**, kept open at:

`file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html`

Final state: **Square / 128 px / Light / All artwork, 11 images, page top**, normal Chrome window. The pre-existing gallery tab and other user tabs were preserved. Two indistinguishable blank New Tab windows from early focus changes were not closed because ownership was uncertain; the coordinator was explicitly informed of that exception.

No source code, catalog HTML, manifest, generated image or prompt file was changed. No commit, push, native call or child worker was made. Baseline, GUI scenarios, byte checks and known-resource cleanup are completed; only the disclosed ambiguous-window cleanup decision is left to the coordinator/user.

## Raw screenshot inventory

29 original Sky JPEG files were copied byte-for-byte; none were cropped, rescaled or pixel-edited by this worker. Screenshots contain task pages only, with no unrelated tabs or download entries. The mismatch capture is retained with its limitation stated above. All JPEG signatures and report links were verified from the final files.

| Screenshot | Scenario |
| --- | --- |
| [01-square-128-all-top.jpg](chrome/01-square-128-all-top.jpg) | square 128 all top |
| [02-fullscreen-ax-mismatch.jpg](chrome/02-fullscreen-ax-mismatch.jpg) | Fullscreen AX mismatch; not a passing interaction |
| [04-http-square-128-all-top.jpg](chrome/04-http-square-128-all-top.jpg) | http square 128 all top |
| [05-rounded-128-all.jpg](chrome/05-rounded-128-all.jpg) | rounded 128 all |
| [06-circle-128-dark.jpg](chrome/06-circle-128-dark.jpg) | circle 128 dark |
| [07-square-128-ip-01-06.jpg](chrome/07-square-128-ip-01-06.jpg) | square 128 ip 01 06 |
| [08-square-128-middle.jpg](chrome/08-square-128-middle.jpg) | square 128 middle |
| [09-square-128-bottom.jpg](chrome/09-square-128-bottom.jpg) | square 128 bottom |
| [10-square-32-all-top.jpg](chrome/10-square-32-all-top.jpg) | square 32 all top |
| [11-square-32-ip.jpg](chrome/11-square-32-ip.jpg) | square 32 ip |
| [12-square-32-middle.jpg](chrome/12-square-32-middle.jpg) | square 32 middle |
| [13-square-32-bottom.jpg](chrome/13-square-32-bottom.jpg) | square 32 bottom |
| [14-square-64-dark-top.jpg](chrome/14-square-64-dark-top.jpg) | square 64 dark top |
| [15-square-64-dark-ip.jpg](chrome/15-square-64-dark-ip.jpg) | square 64 dark ip |
| [16-square-64-dark-middle.jpg](chrome/16-square-64-dark-middle.jpg) | square 64 dark middle |
| [17-square-64-dark-bottom.jpg](chrome/17-square-64-dark-bottom.jpg) | square 64 dark bottom |
| [18-filter-ip-mascot.jpg](chrome/18-filter-ip-mascot.jpg) | filter ip mascot |
| [19-filter-ip-mascot-lower.jpg](chrome/19-filter-ip-mascot-lower.jpg) | filter ip mascot lower |
| [20-filter-pictogram.jpg](chrome/20-filter-pictogram.jpg) | filter pictogram |
| [21-filter-abstract.jpg](chrome/21-filter-abstract.jpg) | filter abstract |
| [22-filter-monogram.jpg](chrome/22-filter-monogram.jpg) | filter monogram |
| [23-monogram-exact-intent.jpg](chrome/23-monogram-exact-intent.jpg) | monogram exact intent |
| [24-filter-soft-3d.jpg](chrome/24-filter-soft-3d.jpg) | filter soft 3d |
| [25-filter-pixel-art.jpg](chrome/25-filter-pixel-art.jpg) | filter pixel art |
| [26-keyboard-circle-32-dark-pixel.jpg](chrome/26-keyboard-circle-32-dark-pixel.jpg) | keyboard circle 32 dark pixel |
| [27-keyboard-reset-all.jpg](chrome/27-keyboard-reset-all.jpg) | keyboard reset all |
| [28-downloads-hash-matched.jpg](chrome/28-downloads-hash-matched.jpg) | Chrome downloads filtered to task port |
| [29-exact-korean-prompt-file.jpg](chrome/29-exact-korean-prompt-file.jpg) | Exact Korean prompt at original file URL |
| [30-final-file-url-reset.jpg](chrome/30-final-file-url-reset.jpg) | Final file URL reset, 11 originals |
