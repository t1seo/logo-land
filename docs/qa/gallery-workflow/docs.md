# README and unified visual gallery evidence

Owner: T2 docs, `task_5a2a1f669344` / `ctx_37cd1f277888`. Checkout: `feat/logo-land-gallery-workflow`; baseline commit `06b94c41922973fc98392fadde25fff9aa498f6e`.

## Execution ledger

- [x] Confirm exact current README/index files and recorded baseline before editing.
- [x] Restructure English/Korean README and unified gallery with existing real originals.
- [x] Add eight real new images after the native owner's `docs/gallery-workflow/samples.json` handoff.
- [x] Verify links/anchors, source preservation, language parity and bounded HTTP byte equality.
- [x] Remove owned temporary resources and report the completed documentation scope.

## Resource registration before creation

- Reserve `/tmp/ll-060-docs-http` exclusively for this worker; fail if it already exists. Temporary Ruby document/validation scripts, baseline JSON/hash inventories, HTTP responses and server log/PID records will live only here and be removed after evidence is recorded.
- Reserve `127.0.0.1:8792`; verify no listener before starting a repository-root HTTP server. Register its actual PID and directory inode after creation. Maximum lifetime 300 seconds per owned server; terminate only the registered server after requests finish. All curl calls use `--fail --max-time 20`.
- No Chrome windows/tabs, new image assets, production source, tests, historical individual pages, installation/version files or commits are owned by this worker.

## Baseline and requested observable

Read [readme-baseline.md](readme-baseline.md) before edits. Both root README files show seven badges and the existing current identity but **zero inline sample images**; the first sample appears after README → category → individual-page navigation (two clicks). The desired assertion **at least six inline representative sample images, each linking straight to its real original PNG**, therefore fails at baseline: **0 < 6**.

Final PASS requires the native manifest and all eight real new images; existing-only structure is an intermediate state. Static/HTTP evidence will establish transport, byte identity and link structure; actual Chrome rendering belongs to T4 and is not claimed here.

## Intermediate source review

The owned temporary directory was exclusively created with device `16777230`, inode `35001780`. The baseline capture contains 12 existing owned document paths and 73 existing PNG paths in `assets`, `docs/samples`, `docs/app-icons`, `docs/app-icons-quality-v1`, `docs/colors`, `docs/brand` and `docs/transparency`; no research screenshots or synthetic QA fixture images are gallery material.

Final HTTP server registration: owned Python `http.server` PID `73660`, exec session `38086`, bound to `127.0.0.1:8792`, serving the repository root under a Ruby supervisor with a 300-second lifetime bound. `lsof -nP -iTCP:8792 -sTCP:LISTEN` found no pre-existing listener before creation. Temporary script paths are `/tmp/ll-060-docs-http/{edit-docs.rb,validate.rb,add-native.rb,serve.rb,http.rb}`; all are included in this worker's previously registered cleanup scope.

The existing-only gallery has 46 linked PNG image occurrences per language: 10 brands, 16 app icons, 17 stored color-project artifacts and 3 current/archived identity originals. The color parent `white-bamgyeol/images/parent-v1.png` repeats the preserved `bamgyeol/images/a-v1.png` bytes for comparison, so these 46 paths have 45 distinct PNG hashes. No thumbnail image files were copied or generated.

An initial document validator passed all 14 owned public documents and confirmed all 73 baseline PNG hashes unchanged. In-memory malformed-link probes rejected a missing target, a missing anchor on an existing Markdown target, a `javascript:` URL and path traversal. The temporary validator initially used Ruby's `filter_map`, unavailable in the system Ruby; it was changed to `map.compact` before the successful run. No repository code was changed for that tooling compatibility adjustment.

Source review used the frozen `docs/colors/manifest.json` case and attempt records. It confirmed GROVE `a-v1` is the delivered transparent original and `a-v2`/`a-v3`/`a-v4` all fail with opaque checkerboards; the draft label was corrected before handoff. Restricted-color original results remain indeterminate, color repairs remain mismatched/opaque-checkerboard failures, and every white attempt remains indeterminate. This worker has not reassessed artistic quality or promoted any historical attempt to an approved delivery.

## Exact baseline document sources

| Path | Before SHA-256 | Bytes |
|---|---|---:|
| `README.ko.md` | `a0746d3f4df7cf036eabfdbffc07b7c0b9c94b738a63d13b1da27b6ee493cb11` | 5384 |
| `README.md` | `e3910e4a691ce1e555e8aa3461c2a01ced90f5e1c6014f4bdc21622fd89ccfec` | 4711 |
| `docs/README.ko.md` | `df4154c4b7a5ddcb60a75ad511362899125a02a5ac6e59577b23b79d7b23bd59` | 1887 |
| `docs/README.md` | `17189dd78dc4098dcecd9759d5b489966056923c3a8906a78150120b833e7bbb` | 1652 |
| `docs/app-icons/README.ko.md` | `7febf2b847fe5d104e4ba3a5c87f6a7f1e3674bf19eb87754d72048c7047421f` | 1468 |
| `docs/app-icons/README.md` | `c4e85865f13ad3ba8eaf0e5de9d6b7d491a05f629a172893251f3c9b2da117cc` | 1226 |
| `docs/brand/README.ko.md` | `a5813463b68e8f70f3d169116694eb997a432b7bdf57f8ded893b5542d28100c` | 1102 |
| `docs/brand/README.md` | `239bca8d754c76253adf0f16d7122fd428902e906b7a630c64df09a0ceb914a2` | 932 |
| `docs/colors/README.ko.md` | `70d7c6f517a0624088db05fc1a06d32d012db54619437a826a8f9d4dcb7ff605` | 1635 |
| `docs/colors/README.md` | `a95d20935575c1aea5d1036cd614338a1fc50bf07a8c17a340a07794b7b524a5` | 1484 |
| `docs/samples/README.ko.md` | `cac86de6acbf380becda90a04f9cb4d25681cc37cecf7160cda721b2b853465e` | 1189 |
| `docs/samples/README.md` | `7b870dab04532214b6dcaf8f42cdb3d73ff42225bb0169cc9dcd9e88bbd50d46` | 1027 |

## Preserved PNG inventory

These are the exact 73 pre-existing source paths captured before edits. Each hash must still match at final verification; this includes existing duplicate storage/delivery paths but creates none. The visual-gallery inventory below will identify the actual paths used for thumbnails.

| Existing PNG path | Baseline SHA-256 |
|---|---|
| `assets/logo-land-studio.png` | `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3` |
| `assets/logo-transparent.png` | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |
| `assets/logo.png` | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| `docs/app-icons-quality-v1/images/abstract-quality-v1.png` | `93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b` |
| `docs/app-icons-quality-v1/images/abstract.png` | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| `docs/app-icons-quality-v1/images/ip-a1.png` | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| `docs/app-icons-quality-v1/images/ip-a2.png` | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| `docs/app-icons-quality-v1/images/ip-b1.png` | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| `docs/app-icons-quality-v1/images/ip-b2.png` | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| `docs/app-icons-quality-v1/images/ip-c1.png` | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| `docs/app-icons-quality-v1/images/ip-c2.png` | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| `docs/app-icons-quality-v1/images/monogram-quality-v1.png` | `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f` |
| `docs/app-icons-quality-v1/images/monogram.png` | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| `docs/app-icons-quality-v1/images/pictogram-quality-v1.png` | `b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a` |
| `docs/app-icons-quality-v1/images/pictogram.png` | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| `docs/app-icons-quality-v1/images/pixel-art-quality-v1.png` | `29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328` |
| `docs/app-icons-quality-v1/images/pixel-art.png` | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| `docs/app-icons-quality-v1/images/soft-3d-quality-v1.png` | `ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2` |
| `docs/app-icons-quality-v1/images/soft-3d.png` | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| `docs/app-icons/images/abstract.png` | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| `docs/app-icons/images/ip-a1.png` | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| `docs/app-icons/images/ip-a2.png` | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| `docs/app-icons/images/ip-b1.png` | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| `docs/app-icons/images/ip-b2.png` | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| `docs/app-icons/images/ip-c1.png` | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| `docs/app-icons/images/ip-c2.png` | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| `docs/app-icons/images/monogram.png` | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| `docs/app-icons/images/pictogram.png` | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| `docs/app-icons/images/pixel-art.png` | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| `docs/app-icons/images/soft-3d.png` | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| `docs/brand/2026-identity/delivery/logo.png` | `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3` |
| `docs/brand/delivery/logo.png` | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| `docs/colors/assets/01-sunroom.png` | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/assets/02-northline.png` | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/assets/03-grove.png` | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/assets/04-grove-warm.png` | `db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7` |
| `docs/colors/assets/05-bamgyeol.png` | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/assets/06-tide.png` | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/assets/07-fieldnote.png` | `049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870` |
| `docs/colors/assets/08-bamgyeol-white.png` | `0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd` |
| `docs/colors/deliveries/grove/logo.png` | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/deliveries/northline/logo.png` | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/deliveries/tide/logo.png` | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/projects/bamgyeol/images/a-v1.png` | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/projects/bamgyeol/images/a-v2.png` | `27e010082310501ac2ca6060aa8835ff3e75cd727bb971fb76f08b153884815b` |
| `docs/colors/projects/bamgyeol/images/a-v3.png` | `0df1d666d480aae721f6ccab6fa7ff9d2388b015946e8e051381c86e9766c6f3` |
| `docs/colors/projects/fieldnote/images/a-v1.png` | `049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870` |
| `docs/colors/projects/fieldnote/images/a-v2.png` | `7dacc55d6f90f10f7206729f3f0d7cffc75b36ff6191e7430d8e01e2b76c40cb` |
| `docs/colors/projects/fieldnote/images/a-v3.png` | `05398268ac42aa8d0da04976a9c6367df1bb186e1b3fe46e927db3e494ee65e2` |
| `docs/colors/projects/fieldnote/references/grove-colors.png` | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/projects/grove/images/a-v1.png` | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/projects/grove/images/a-v2.png` | `c60c605176b39f2b26f5299a2c99906dc5cc3e93e4716691e1e2b3154af33809` |
| `docs/colors/projects/grove/images/a-v3.png` | `e0e0ba746f10f1ab0df53b6a2bda9c6d1f27d621efef68c4142d080407d0bc74` |
| `docs/colors/projects/grove/images/a-v4.png` | `db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7` |
| `docs/colors/projects/northline/images/a-v1.png` | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/projects/sunroom/images/a-v1.png` | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/projects/tide/images/a-v1.png` | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/projects/tide/references/sunroom-colors.png` | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/projects/white-bamgyeol/images/parent-v1.png` | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/projects/white-bamgyeol/images/white-v1.png` | `764557003be078c7e83fca85b7b40d43977edefa9ef46caf49f5279c403a3151` |
| `docs/colors/projects/white-bamgyeol/images/white-v2.png` | `fda77d0af6c53c4d0d28099ca6568cbb7e877ac6045ea9ca6898bf77884a29a5` |
| `docs/colors/projects/white-bamgyeol/images/white-v3.png` | `0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd` |
| `docs/samples/items/01-luma/delivery/logo.png` | `29c891de028f14cc8b8a715f105b2dd8b383fa647f691521bd0de25428f561ef` |
| `docs/samples/items/02-loop-lab/delivery/logo.png` | `c03e72b2362ed7071f52f441520a73fa9a92be697efa551ae14b3cb43da8aab4` |
| `docs/samples/items/03-goyo/delivery/logo.png` | `4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174` |
| `docs/samples/items/04-bread-bloom/delivery/logo.png` | `420ac19545143efbc4681b27b68fd074656da803869c746bd9c1eeb5678c9b8c` |
| `docs/samples/items/05-kite/delivery/logo.png` | `dffb886a7a72196a42df21e36afe23cfb6e07bd25bad35c69c44f4de5c0232a7` |
| `docs/samples/items/06-miso/delivery/logo.png` | `10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649` |
| `docs/samples/items/07-northline/delivery/logo.png` | `4eb27ce806aab3a32f58337c8b1fd00f6257f1abe970f98f12edfac6be423c06` |
| `docs/samples/items/08-mulgyeol/delivery/logo.png` | `da97616502733dcef4b6b082d7746149793a22a576f3ad179a4da641d7ed66cf` |
| `docs/samples/items/09-fern/delivery/logo.png` | `db9066ee56c2789324aa7c53e5ba68b9e6c003ba3fe98578ea8b0e6196181e27` |
| `docs/samples/items/10-nova-notes/delivery/logo.png` | `0e26b2354a22faba2128d205c377abe09e590c82f895e2716fe51e0877715553` |
| `docs/transparency/delivery/logo.png` | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |

## Final document result and complete journey

- English remains the default; the Korean files cover the same content in polite Korean. Each root README has exactly three natural-language examples and six clickable sample images: three brand logos and three app icons, including the new COMMON original and Relay child. The seven centered badges remain first; current identity is still the original `assets/logo-land-studio.png`, displayed at 200px. This worker retains development `0.5.0` and published release `v0.3.1`; integration owns the later version update.
- Before: 0 visible sample thumbnails and first sample visibility after two navigation steps. After: 6 actual inline sample images per root README, visible without sample-page navigation; one click opens a PNG. `README.md → docs/gallery.md` and `README.ko.md → docs/gallery.ko.md` are one-step routes to all originals on a GitHub-renderable Markdown page. Each gallery image then opens its actual PNG in one click.
- The unified gallery has **54 linked PNG paths / 53 unique byte hashes per language**: new 8 + brand 10 + app 16 + stored color originals 17 + current/archived identity 3. The only repeated image content is the explicitly labelled 밤결 parent in its white comparison. The 17 color originals cover all eight cases; all 73 pre-existing PNG paths retain their baseline hashes. Every new image points to the native owner's existing file; this worker created no art or thumbnail copies.
- Original/refined Relay and Sprig pairs are adjacent and explicitly labelled v1 → v2. Relay's wider opening and extra geometry change are both retained; Sprig's unclear requested stem bend and largely unchanged small-size recognition are retained. Leaflet's extra color family, small-size observations and COMMON's header/favicons distinction follow the native owner's observations, without a blanket quality or production-readiness claim.
- Historical SUNROOM subtitle failure, GROVE warmer opaque-checkerboard failures, restricted-color mismatches/indeterminate originals and unresolved white attempts remain explicit. Current identity and archived earlier identity are separate. Raster, font-appearance and platform-preparation limits and the upstream IP adaptation/MIT/pinned notices remain in both languages.
- The later redundant Samples heading/paragraph was removed; its `#samples`/`#샘플` and older sample/transparency anchors now sit beside the top preview. The conversational example requests app-home/header/16px comparison, then retention of shape while widening only the opening. Source/keep/change notes and the fact that copying notes is not selection/approval are explained in the gallery and linked comparison guide. Interactive HTML links explicitly say download/open locally; no hosted Pages/site behavior is claimed.

## Native dependency and stale-state check

Root handed off the verified eight-item manifest `d71208c269321db6bc41e474ebe7eddf2b63d04c9c561b9abb7ae9c1454209b2` and confirmed the two completed native children. The final comparison HTML was linked only after `docs/gallery-workflow/comparison/index.html` existed.

A subsequent strict manifest equality check correctly failed when the native owner added explicit parent text to the Relay/Sprig child rationale fields. Field-by-field comparison found only those two rationale changes; all eight image hashes, eight prompt hashes, IDs, relationships, dimensions, observations and revision fields were unchanged. The final captured and HTTP-fetched manifest hash is `19b5e08521fe8c685f112b3ede86a56f214ff10ccafecc50b7428194d6d9af37`. This is an observed stale-state rejection and reviewed refresh, not an ignored mismatch.

## Final exact document and link inventory

Counts cover all 14 owned public Markdown documents, excluding this evidence report: **580 reference occurrences**, **554 local occurrences**, **159 distinct local target files**, **26 external occurrences**. Repeated language/thumbnail href and src references are counted separately. Every local target and referenced fragment resolves; external links were retained, not network-tested by this static-doc worker.

| Document | Current SHA-256 | Bytes | All refs | Local refs | Unique local files | Fragment refs | Linked inline PNGs |
|---|---|---:|---:|---:|---:|---:|---:|
| `README.md` | `9c216c165febb8ee87416384d4fab50236d640af3135c879c59636ee24cffee0` | 5326 | 39 | 28 | 18 | 0 | 6 |
| `README.ko.md` | `4d9a703990d7434ea8f9a3ba497100d938edc810758cbc10736105c6423435e3` | 5974 | 39 | 28 | 18 | 0 | 6 |
| `docs/README.md` | `06cc006e64e8da6904bcf98cbfd640cac574aec9deb6e33341e20447583636d0` | 1897 | 22 | 21 | 20 | 1 | 0 |
| `docs/README.ko.md` | `a11ee2aa69d88af8d70f9ca2e843094fd12d9813dcfe67a53b40fb2e207ce73e` | 2176 | 22 | 21 | 20 | 1 | 0 |
| `docs/gallery.md` | `1453af5261fdfabd1f4a58a7796e4bbf757c41cbab03e4cb0e826e9b31a15a63` | 17847 | 166 | 165 | 105 | 6 | 54 |
| `docs/gallery.ko.md` | `e3bed14d948da7f2108935681861266a3435ff4786a8d1f2650e125436e92616` | 19138 | 166 | 165 | 105 | 6 | 54 |
| `docs/app-icons/README.ko.md` | `8e67cd86b3f9c31685d11e955764fe49d8c6c37be6b591d2b87e4d5a56d1dc69` | 1602 | 18 | 18 | 18 | 0 | 0 |
| `docs/app-icons/README.md` | `4cf65d1530be5ae3c74f3fcd7065749f2019d3fee2c77516d6ce8f19a68b2b68` | 1337 | 18 | 18 | 18 | 0 | 0 |
| `docs/brand/README.ko.md` | `10e93a49222cfe6d0bdab502d109b3e91796d6903076fa2156a5eaf768d76612` | 1236 | 11 | 11 | 10 | 0 | 0 |
| `docs/brand/README.md` | `fdbd0a78ca45f365952230f008e78449dbae7619829e8d8e00869f73a75e6b9e` | 1043 | 11 | 11 | 10 | 0 | 0 |
| `docs/colors/README.ko.md` | `274f2e20bda0feb78f26c20f7eb5432ceba59d31a9d21e8fbef410cc6446f847` | 1769 | 16 | 16 | 15 | 2 | 0 |
| `docs/colors/README.md` | `2753f130a7918c031b0a4b23d69afe5bc495e084a727083a219905d9e0f44c2d` | 1595 | 16 | 16 | 15 | 2 | 0 |
| `docs/samples/README.ko.md` | `5097cd6ff432b5faf19c81668eb54d086e87d66f7a76ccfbd589c425695e68a9` | 1323 | 18 | 18 | 18 | 0 | 0 |
| `docs/samples/README.md` | `d857a6dce2c057fa522a3c651b45426133342cde809a22a2f508fa83bb77ad48` | 1138 | 18 | 18 | 18 | 0 | 0 |

Exact distinct local target-file inventory (fragments additionally checked against Markdown headings or explicit IDs):

- `CHANGELOG.md`
- `README.ko.md`
- `README.md`
- `THIRD_PARTY_NOTICES.md`
- `assets/logo-land-studio.png`
- `assets/logo-transparent.png`
- `assets/logo.png`
- `docs/README.ko.md`
- `docs/README.md`
- `docs/app-icons-quality-v1/images/abstract-quality-v1.png`
- `docs/app-icons-quality-v1/images/monogram-quality-v1.png`
- `docs/app-icons-quality-v1/images/pictogram-quality-v1.png`
- `docs/app-icons-quality-v1/images/pixel-art-quality-v1.png`
- `docs/app-icons-quality-v1/images/soft-3d-quality-v1.png`
- `docs/app-icons-quality-v1/index.html`
- `docs/app-icons/README.ko.md`
- `docs/app-icons/README.md`
- `docs/app-icons/images/abstract.png`
- `docs/app-icons/images/ip-a1.png`
- `docs/app-icons/images/ip-a2.png`
- `docs/app-icons/images/ip-b1.png`
- `docs/app-icons/images/ip-b2.png`
- `docs/app-icons/images/ip-c1.png`
- `docs/app-icons/images/ip-c2.png`
- `docs/app-icons/images/monogram.png`
- `docs/app-icons/images/pictogram.png`
- `docs/app-icons/images/pixel-art.png`
- `docs/app-icons/images/soft-3d.png`
- `docs/app-icons/index.html`
- `docs/app-icons/samples/abstract.ko.md`
- `docs/app-icons/samples/abstract.md`
- `docs/app-icons/samples/ip-a1.ko.md`
- `docs/app-icons/samples/ip-a1.md`
- `docs/app-icons/samples/ip-a2.ko.md`
- `docs/app-icons/samples/ip-a2.md`
- `docs/app-icons/samples/ip-b1.ko.md`
- `docs/app-icons/samples/ip-b1.md`
- `docs/app-icons/samples/ip-b2.ko.md`
- `docs/app-icons/samples/ip-b2.md`
- `docs/app-icons/samples/ip-c1.ko.md`
- `docs/app-icons/samples/ip-c1.md`
- `docs/app-icons/samples/ip-c2.ko.md`
- `docs/app-icons/samples/ip-c2.md`
- `docs/app-icons/samples/monogram.ko.md`
- `docs/app-icons/samples/monogram.md`
- `docs/app-icons/samples/pictogram.ko.md`
- `docs/app-icons/samples/pictogram.md`
- `docs/app-icons/samples/pixel-art.ko.md`
- `docs/app-icons/samples/pixel-art.md`
- `docs/app-icons/samples/soft-3d.ko.md`
- `docs/app-icons/samples/soft-3d.md`
- `docs/archive.md`
- `docs/brand/2026-identity/delivery/brand-guide.md`
- `docs/brand/2026-identity/delivery/logo-package.zip`
- `docs/brand/README.ko.md`
- `docs/brand/README.md`
- `docs/brand/legacy.md`
- `docs/colors/README.ko.md`
- `docs/colors/README.md`
- `docs/colors/index.html`
- `docs/colors/projects/bamgyeol/README.ko.md`
- `docs/colors/projects/bamgyeol/README.md`
- `docs/colors/projects/bamgyeol/images/a-v1.png`
- `docs/colors/projects/bamgyeol/images/a-v2.png`
- `docs/colors/projects/bamgyeol/images/a-v3.png`
- `docs/colors/projects/fieldnote/README.ko.md`
- `docs/colors/projects/fieldnote/README.md`
- `docs/colors/projects/fieldnote/images/a-v1.png`
- `docs/colors/projects/fieldnote/images/a-v2.png`
- `docs/colors/projects/fieldnote/images/a-v3.png`
- `docs/colors/projects/grove/README.ko.md`
- `docs/colors/projects/grove/README.md`
- `docs/colors/projects/grove/images/a-v1.png`
- `docs/colors/projects/grove/images/a-v2.png`
- `docs/colors/projects/grove/images/a-v3.png`
- `docs/colors/projects/grove/images/a-v4.png`
- `docs/colors/projects/northline/README.ko.md`
- `docs/colors/projects/northline/README.md`
- `docs/colors/projects/northline/images/a-v1.png`
- `docs/colors/projects/sunroom/README.ko.md`
- `docs/colors/projects/sunroom/README.md`
- `docs/colors/projects/sunroom/images/a-v1.png`
- `docs/colors/projects/tide/README.ko.md`
- `docs/colors/projects/tide/README.md`
- `docs/colors/projects/tide/images/a-v1.png`
- `docs/colors/projects/white-bamgyeol/README.ko.md`
- `docs/colors/projects/white-bamgyeol/README.md`
- `docs/colors/projects/white-bamgyeol/images/parent-v1.png`
- `docs/colors/projects/white-bamgyeol/images/white-v1.png`
- `docs/colors/projects/white-bamgyeol/images/white-v2.png`
- `docs/colors/projects/white-bamgyeol/images/white-v3.png`
- `docs/gallery-workflow/comparison/index.html`
- `docs/gallery-workflow/images/common-v1.png`
- `docs/gallery-workflow/images/drip-v1.png`
- `docs/gallery-workflow/images/leaflet-v1.png`
- `docs/gallery-workflow/images/relay-v1.png`
- `docs/gallery-workflow/images/relay-v2.png`
- `docs/gallery-workflow/images/sprig-v1.png`
- `docs/gallery-workflow/images/sprig-v2.png`
- `docs/gallery-workflow/images/teum-v1.png`
- `docs/gallery-workflow/prompts/common-v1.txt`
- `docs/gallery-workflow/prompts/drip-v1.txt`
- `docs/gallery-workflow/prompts/leaflet-v1.txt`
- `docs/gallery-workflow/prompts/relay-v1.txt`
- `docs/gallery-workflow/prompts/relay-v2.txt`
- `docs/gallery-workflow/prompts/sprig-v1.txt`
- `docs/gallery-workflow/prompts/sprig-v2.txt`
- `docs/gallery-workflow/prompts/teum-v1.txt`
- `docs/gallery-workflow/samples.json`
- `docs/gallery.ko.md`
- `docs/gallery.md`
- `docs/installation.ko.md`
- `docs/installation.md`
- `docs/samples/README.ko.md`
- `docs/samples/README.md`
- `docs/samples/index.html`
- `docs/samples/items/01-luma/README.ko.md`
- `docs/samples/items/01-luma/README.md`
- `docs/samples/items/01-luma/delivery/logo.png`
- `docs/samples/items/02-loop-lab/README.ko.md`
- `docs/samples/items/02-loop-lab/README.md`
- `docs/samples/items/02-loop-lab/delivery/logo.png`
- `docs/samples/items/03-goyo/README.ko.md`
- `docs/samples/items/03-goyo/README.md`
- `docs/samples/items/03-goyo/delivery/logo.png`
- `docs/samples/items/04-bread-bloom/README.ko.md`
- `docs/samples/items/04-bread-bloom/README.md`
- `docs/samples/items/04-bread-bloom/delivery/logo.png`
- `docs/samples/items/05-kite/README.ko.md`
- `docs/samples/items/05-kite/README.md`
- `docs/samples/items/05-kite/delivery/logo.png`
- `docs/samples/items/06-miso/README.ko.md`
- `docs/samples/items/06-miso/README.md`
- `docs/samples/items/06-miso/delivery/logo.png`
- `docs/samples/items/07-northline/README.ko.md`
- `docs/samples/items/07-northline/README.md`
- `docs/samples/items/07-northline/delivery/logo.png`
- `docs/samples/items/08-mulgyeol/README.ko.md`
- `docs/samples/items/08-mulgyeol/README.md`
- `docs/samples/items/08-mulgyeol/delivery/logo.png`
- `docs/samples/items/09-fern/README.ko.md`
- `docs/samples/items/09-fern/README.md`
- `docs/samples/items/09-fern/delivery/logo.png`
- `docs/samples/items/10-nova-notes/README.ko.md`
- `docs/samples/items/10-nova-notes/README.md`
- `docs/samples/items/10-nova-notes/delivery/logo.png`
- `docs/samples/transparency.ko.md`
- `docs/samples/transparency.md`
- `docs/transparency/README.md`
- `skills/logo-land/SKILL.md`
- `skills/logo-land/assets/ip-as-logo.LICENSE`
- `skills/logo-land/references/app-icons.md`
- `skills/logo-land/references/color-workflow.md`
- `skills/logo-land/references/comparison-workflow.md`
- `skills/logo-land/references/delivery-checks.md`
- `skills/logo-land/references/ip-mascot.md`
- `skills/logo-land/references/logo-directions.md`
- `skills/logo-land/references/project-files.md`
- `skills/logo-land/references/typography.md`

## Actual bounded HTTP evidence

Server: repository root on `127.0.0.1:8792`, PID `73660`, bounded to 300 seconds. Timestamp: `2026-09-13T00:34:52Z`. **63 successful 200 requests**: English/Korean root README and gallery requested twice each, 54 real PNG paths, and the final native manifest. Every response body exactly equalled the current source file before and after the request. All PNG responses had `Content-type: image/png` and the real PNG signature. Repeated document URLs returned stable body hashes and performed no state writes.

The required commands were executed as argv by the owned Ruby HTTP driver, with `curl -i --fail --max-time 20` for every request, including:

```sh
curl -i --fail --max-time 20 http://127.0.0.1:8792/README.md
curl -i --fail --max-time 20 http://127.0.0.1:8792/docs/gallery.md
curl -i --fail --max-time 20 http://127.0.0.1:8792/README.ko.md
curl -i --fail --max-time 20 http://127.0.0.1:8792/docs/gallery.ko.md
```

Each command was repeated once. The driver parsed the first HTTP header/body boundary, required status 200, compared bytes with the file, computed SHA-256 and re-read the file to detect changes. It read the validated linked-image markup and fetched every actual PNG listed below; HTTP success alone did not substitute for link/anchor or byte validation.

Actual first English README headers:

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.12
Date: Sun, 13 Sep 2026 00:34:51 GMT
Content-type: text/markdown
Content-Length: 5326
Last-Modified: Sun, 13 Sep 2026 00:34:35 GMT
```

| HTTP document | Status on both reads | Body SHA-256 (same as current source) |
|---|---|---|
| `README.md` | 200 / 200 | `9c216c165febb8ee87416384d4fab50236d640af3135c879c59636ee24cffee0` |
| `docs/gallery.md` | 200 / 200 | `1453af5261fdfabd1f4a58a7796e4bbf757c41cbab03e4cb0e826e9b31a15a63` |
| `README.ko.md` | 200 / 200 | `4d9a703990d7434ea8f9a3ba497100d938edc810758cbc10736105c6423435e3` |
| `docs/gallery.ko.md` | 200 / 200 | `e3bed14d948da7f2108935681861266a3435ff4786a8d1f2650e125436e92616` |

Every following PNG was fetched with status 200; source and downloaded hashes matched exactly. Paths are the actual thumbnail destinations, not generated preview copies.

| PNG path / HTTP path | Bytes | Source = downloaded SHA-256 |
|---|---:|---|
| `assets/logo-land-studio.png` | 835901 | `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3` |
| `assets/logo-transparent.png` | 696379 | `ea31330bccf50bb53337fd118984457d8efc898fd23776b3bcf38717d3f76dd7` |
| `assets/logo.png` | 973470 | `f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343` |
| `docs/app-icons-quality-v1/images/abstract-quality-v1.png` | 944574 | `93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b` |
| `docs/app-icons-quality-v1/images/monogram-quality-v1.png` | 855003 | `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f` |
| `docs/app-icons-quality-v1/images/pictogram-quality-v1.png` | 924939 | `b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a` |
| `docs/app-icons-quality-v1/images/pixel-art-quality-v1.png` | 924570 | `29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328` |
| `docs/app-icons-quality-v1/images/soft-3d-quality-v1.png` | 1498775 | `ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2` |
| `docs/app-icons/images/abstract.png` | 961065 | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| `docs/app-icons/images/ip-a1.png` | 1060303 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| `docs/app-icons/images/ip-a2.png` | 1049136 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| `docs/app-icons/images/ip-b1.png` | 1083251 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| `docs/app-icons/images/ip-b2.png` | 1039677 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| `docs/app-icons/images/ip-c1.png` | 1096895 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| `docs/app-icons/images/ip-c2.png` | 1089169 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| `docs/app-icons/images/monogram.png` | 832716 | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| `docs/app-icons/images/pictogram.png` | 928736 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| `docs/app-icons/images/pixel-art.png` | 946180 | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| `docs/app-icons/images/soft-3d.png` | 1526612 | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| `docs/colors/projects/bamgyeol/images/a-v1.png` | 334046 | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/projects/bamgyeol/images/a-v2.png` | 1958592 | `27e010082310501ac2ca6060aa8835ff3e75cd727bb971fb76f08b153884815b` |
| `docs/colors/projects/bamgyeol/images/a-v3.png` | 1854918 | `0df1d666d480aae721f6ccab6fa7ff9d2388b015946e8e051381c86e9766c6f3` |
| `docs/colors/projects/fieldnote/images/a-v1.png` | 999504 | `049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870` |
| `docs/colors/projects/fieldnote/images/a-v2.png` | 2222167 | `7dacc55d6f90f10f7206729f3f0d7cffc75b36ff6191e7430d8e01e2b76c40cb` |
| `docs/colors/projects/fieldnote/images/a-v3.png` | 1993871 | `05398268ac42aa8d0da04976a9c6367df1bb186e1b3fe46e927db3e494ee65e2` |
| `docs/colors/projects/grove/images/a-v1.png` | 653299 | `768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06` |
| `docs/colors/projects/grove/images/a-v2.png` | 1993868 | `c60c605176b39f2b26f5299a2c99906dc5cc3e93e4716691e1e2b3154af33809` |
| `docs/colors/projects/grove/images/a-v3.png` | 1331289 | `e0e0ba746f10f1ab0df53b6a2bda9c6d1f27d621efef68c4142d080407d0bc74` |
| `docs/colors/projects/grove/images/a-v4.png` | 1589312 | `db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7` |
| `docs/colors/projects/northline/images/a-v1.png` | 882512 | `3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534` |
| `docs/colors/projects/sunroom/images/a-v1.png` | 915115 | `e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb` |
| `docs/colors/projects/tide/images/a-v1.png` | 891144 | `2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d` |
| `docs/colors/projects/white-bamgyeol/images/parent-v1.png` | 334046 | `083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941` |
| `docs/colors/projects/white-bamgyeol/images/white-v1.png` | 327144 | `764557003be078c7e83fca85b7b40d43977edefa9ef46caf49f5279c403a3151` |
| `docs/colors/projects/white-bamgyeol/images/white-v2.png` | 375026 | `fda77d0af6c53c4d0d28099ca6568cbb7e877ac6045ea9ca6898bf77884a29a5` |
| `docs/colors/projects/white-bamgyeol/images/white-v3.png` | 373191 | `0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd` |
| `docs/gallery-workflow/images/common-v1.png` | 850531 | `9d89bac4146c3cfcfd49551c7a5f0de12effd5763d1f709b18fedd45a25c741b` |
| `docs/gallery-workflow/images/drip-v1.png` | 941249 | `8f1e846ceac3d01dc1eb60bab5b5ad1679f71f51fb1a85fc7041ce62f05b1f6f` |
| `docs/gallery-workflow/images/leaflet-v1.png` | 1058156 | `256b1ee1e25d9d8160ec0751db1453ae31990cecb5c2cd68570410c668cb6b4e` |
| `docs/gallery-workflow/images/relay-v1.png` | 904317 | `6588c675013483c18bcc5fad4986c60e0ec21a78ef7c7591d055e2bb2b620b58` |
| `docs/gallery-workflow/images/relay-v2.png` | 898003 | `a4066faa64d1f58024d1a44afb011694a1808b628b988ac71a0986e90069491d` |
| `docs/gallery-workflow/images/sprig-v1.png` | 1228498 | `956577408a1a8986dd87cf430e44451739d93285352c5ebe5305d19ae216e222` |
| `docs/gallery-workflow/images/sprig-v2.png` | 1225022 | `ed16c756532ef268880f4a1d281d87323bef707cecfe3c41b41397bef74e65ac` |
| `docs/gallery-workflow/images/teum-v1.png` | 916436 | `a97780b67a304853d1b8795d6d3af8efdc4658d36703ed1cdabfa8710b73bf7e` |
| `docs/samples/items/01-luma/delivery/logo.png` | 828471 | `29c891de028f14cc8b8a715f105b2dd8b383fa647f691521bd0de25428f561ef` |
| `docs/samples/items/02-loop-lab/delivery/logo.png` | 893181 | `c03e72b2362ed7071f52f441520a73fa9a92be697efa551ae14b3cb43da8aab4` |
| `docs/samples/items/03-goyo/delivery/logo.png` | 898170 | `4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174` |
| `docs/samples/items/04-bread-bloom/delivery/logo.png` | 1057106 | `420ac19545143efbc4681b27b68fd074656da803869c746bd9c1eeb5678c9b8c` |
| `docs/samples/items/05-kite/delivery/logo.png` | 659904 | `dffb886a7a72196a42df21e36afe23cfb6e07bd25bad35c69c44f4de5c0232a7` |
| `docs/samples/items/06-miso/delivery/logo.png` | 1026254 | `10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649` |
| `docs/samples/items/07-northline/delivery/logo.png` | 797205 | `4eb27ce806aab3a32f58337c8b1fd00f6257f1abe970f98f12edfac6be423c06` |
| `docs/samples/items/08-mulgyeol/delivery/logo.png` | 869641 | `da97616502733dcef4b6b082d7746149793a22a576f3ad179a4da641d7ed66cf` |
| `docs/samples/items/09-fern/delivery/logo.png` | 985597 | `db9066ee56c2789324aa7c53e5ba68b9e6c003ba3fe98578ea8b0e6196181e27` |
| `docs/samples/items/10-nova-notes/delivery/logo.png` | 959993 | `0e26b2354a22faba2128d205c377abe09e590c82f895e2716fe51e0877715553` |

## Adversarial review: nine classes

| Class | Probe and observed result |
|---|---|
| 1. Malformed links / boundary input | In-memory validator probes rejected `missing-image.png`, an existing Markdown file with `#no-such-anchor`, `javascript:alert(1)` and `../../outside.png`. All real local targets/fragments passed. A file serving 200 does not make an invalid fragment pass. |
| 2. Injection / hostile markup | Parsed inline image rows through REXML after normalizing authored HTML void tags; allowed only `p`, `a`, `img` and known attributes. Every sample image has alt text and identical PNG href/src; no script/iframe/object/event attributes or active user markup. Paths/alt labels were HTML escaped, and no saved prompt was executed. |
| 3. Cancellation / resume | Editing resumed from the existing Markdown and exact source manifest after the named generation wait; no placeholder images or absent-file links were published. No forced editor/process cancellation was needed; application transaction rollback is N/A to static Markdown. The completed files were re-read before final validation. |
| 4. Stale / missing state | Actual native manifest drift triggered a strict mismatch; only two rationale-field additions were accepted after full field comparison. Final current manifest and all 8 PNG / 8 prompt bindings were rehashed. Missing native manifest was an explicit HTTP-driver rejection condition until the dependency existed. |
| 5. Dirty worktree / ownership | Pre-existing shared edits were retained. All 73 historical PNG hashes match baseline; `git diff --exit-code -- docs/samples/items docs/app-icons/samples docs/colors/projects docs/colors/assets assets` returned 0. Changes are limited to owned root/index/gallery Markdown and this evidence file; no image, historical page, production/test, installation/version file, commit or push was made by this worker. |
| 6. Hung commands / resource budget | Every curl had `--fail --max-time 20`; actual maximum request time was 0.015s. The owned server had a 300-second supervisor bound and only loopback binding. No unbounded external request or browser process was started. |
| 7. Flaky tests / deterministic checks | No broad pytest or mirror tests were introduced/run for this reversible documentation edit. Static validation reran only after actual document or dependency changes; both language image sequences and expected category counts matched. Build/LSP checks are N/A to Markdown-only edits; `git diff --check` passed for the owned public files. |
| 8. Misleading success / visual limits | The main gallery is actual GitHub-renderable Markdown with 54 inline originals; interactive HTML is explicitly labelled for download/local opening. Failed/indeterminate outputs remain labelled and all new samples remain unapproved. HTTP/parser checks establish transport and source/link structure; they do not claim Chrome rendering, platform readiness, accurate font composition or blanket artistic improvement. |
| 9. Repeated interruptions / reloads | Both languages' README and gallery URLs were requested twice with identical current-file body hashes; the source reads remained stable through every request. No selection or approval state was written. Actual Chrome back/forward, viewport behavior and control interaction remain the single T4 browser owner's responsibility. |

## Verification scope

Documentation/static/HTTP checks passed with the complete native dependency present. This worker did not drive Chrome; T4 must verify actual rendered desktop/narrow layouts and interactive controls. Native artistic observations are attributed to the native owner, and T3 owns version integration, installation and broad code checks. These boundaries are not represented as already completed browser or production verification.

## Final native prompt bindings

All eight exact saved prompts were hashed against the final native manifest; this worker read the text as data and executed none. PNG bindings are the matching named paths in the HTTP table above.

| Sample | Session / artifact | Parent | Prompt source | Exact SHA-256 |
|---|---|---|---|---|
| `leaflet-v1` | `leaflet / v1` | `none` | `docs/gallery-workflow/prompts/leaflet-v1.txt` | `0cad98ad36526c630cf05aa5fdde33d14e87a5545d1302f4be6ba4628e14faf5` |
| `drip-v1` | `drip / v1` | `none` | `docs/gallery-workflow/prompts/drip-v1.txt` | `67aae7296e49bd3dc0850b28f426b8b79c6ee0a926954088ddba4e4b52c1eb8d` |
| `relay-v1` | `relay / v1` | `none` | `docs/gallery-workflow/prompts/relay-v1.txt` | `68f8163701caf21ec0e3c06b43128ff5f4fbc6c67183d5a8649a13e58f7ea813` |
| `relay-v2` | `relay / v2` | `v1` | `docs/gallery-workflow/prompts/relay-v2.txt` | `7c970c80e2167fb7677c82a3ffb360e17ad6569a28b341d881952fabbcd87cef` |
| `teum-v1` | `teum / v1` | `none` | `docs/gallery-workflow/prompts/teum-v1.txt` | `8312812f546902472a7eb0d98311e3e6c1b29fe58ba8a6d55cb826c61e03721c` |
| `sprig-v1` | `sprig / v1` | `none` | `docs/gallery-workflow/prompts/sprig-v1.txt` | `9965898ff25f67a25e10e8002c7037852b7b6b99d0ca4b5a66513edd24c85094` |
| `sprig-v2` | `sprig / v2` | `v1` | `docs/gallery-workflow/prompts/sprig-v2.txt` | `b83d6deeea4f252a27962f1171618ce72e58e7e807c0e6e9c6ba7b2652e6f22a` |
| `common-v1` | `common / v1` | `none` | `docs/gallery-workflow/prompts/common-v1.txt` | `1f6e0c692b28670b0ed91fce8c7890d4ba370f8a419fb2347844dadeb5021a0a` |

## Cleanup and final receipt

- Owned PID `73660` was checked against the exact repository-root `http.server 8792` command, then terminated with SIGTERM. Supervisor exec session `38086` exited 0 with `Owned server supervisor finished`.
- `lsof -nP -iTCP:8792 -sTCP:LISTEN` returned no listener; `ps -p 73660` confirmed the server was absent.
- `/tmp/ll-060-docs-http` still matched device `16777230` / inode `35001780` immediately before secure removal. Its temporary scripts, snapshots, HTTP records and server log were removed only after the evidence was preserved here; nonexistence was asserted afterward.
- Final validation re-read all 14 owned public documents and all 63 HTTP source paths against recorded hashes, confirmed the final native manifest hash and all 73 historical PNG hashes, and passed every link/anchor/EN-KO image-sequence check. No source change occurred after those receipts within this worker's scope.
- No server, temporary directory, browser tab or pending child worker is retained. No production/test files, historical originals, versions or installation files were edited by this worker; no commit/push was performed.

**T2 docs scope: PASS.** README samples increased from 0 to 6 per language, the one-page Markdown gallery contains all 54 actual originals including the new 8, and the 63 bounded HTTP responses exactly matched source bytes. Actual Chrome rendering remains T4; integration owns subsequent metadata changes and must refresh affected document hashes after updating versions.
