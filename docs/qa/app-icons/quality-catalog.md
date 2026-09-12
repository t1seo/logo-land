# Quality comparison catalog QA

Verified 2026-09-12T18:28:39.889Z; owner task_e0d330c517d9 / ctx_94223035ac44. The [published gallery](../../app-icons-quality-v1/index.html) and [manifest](../../app-icons-quality-v1/manifest.json) contain 16 original/prompt pairs in the required order. All 34 files are byte-identical to the helper-generated `output/app-icons-quality-catalog-v1/comparison` directory. The public destination did not exist before exclusive copy; gallery HTML was not rewritten.

## Catalog and provenance

Normal helper init → 16 imports → icon-gallery ran in `output/app-icons-quality-catalog-v1`, session `icon-quality-v1`, title “App icon studies: original and refined”, expected import revisions 0–15 and final revision 16. Every import explicitly supplied the complete corresponding app_icon JSON, exact historic/new prompt file and opaque background. Source generation revisions remain 0. See [aggregate](quality-native-samples.json) and [provenance narrative](quality-native-samples.md).

Native/source/import/catalog/generated/public/HTTP image and prompt SHA-256 bindings, all actual dimensions, six styles, six old IP and five paired non-IP cases passed. The 50 local href/src references resolve;16 cards use original PNG URLs, and all 32 download links point to exact saved original/prompt files. No selected_id, review, exports or color reports exist.

## Actual HTTP channel

Resource registration `msg_fc9bd37bfee4` preceded creation of `/tmp/ll-quality-catalog` and own 127.0.0.1:8801 server. PID 52715 served the published source. The required command executed exactly:

```sh
curl -i --fail --silent --show-error --connect-timeout 2 --max-time 10 http://127.0.0.1:8801/index.html -o /tmp/ll-quality-catalog/index.http
```

The manifest and all 32 original/prompt URLs used the same bounds. All 34 responses were HTTP 200; header blocks, body hashes, byte lengths, exact argv and elapsed times are preserved in `output/app-icons-quality-catalog-v1/http-evidence.json` and embedded in the aggregate. Bodies match both generated and published files, including each manifest-declared image/prompt hash.

| URL path | HTTP | Body bytes | Body SHA-256 |
|---|---|---|---|
| index.html | 200 | 27010 | `257154a6f6b4a77d355482f01462b76988610c85a0f4ff07d999ac0a3d3013e5` |
| manifest.json | 200 | 9721 | `ac8680b966658d0906914a4afd456ee21e9597f19a924815f0b6b7cfafb43a44` |
| images/ip-a1.png | 200 | 1060303 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| prompts/ip-a1.txt | 200 | 1377 | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| images/ip-a2.png | 200 | 1049136 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| prompts/ip-a2.txt | 200 | 1393 | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| images/ip-b1.png | 200 | 1083251 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| prompts/ip-b1.txt | 200 | 1391 | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| images/ip-b2.png | 200 | 1039677 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| prompts/ip-b2.txt | 200 | 1394 | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| images/ip-c1.png | 200 | 1096895 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| prompts/ip-c1.txt | 200 | 1388 | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| images/ip-c2.png | 200 | 1089169 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| prompts/ip-c2.txt | 200 | 1403 | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| images/pictogram.png | 200 | 928736 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| prompts/pictogram.txt | 200 | 1056 | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| images/pictogram-quality-v1.png | 200 | 924939 | `b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a` |
| prompts/pictogram-quality-v1.txt | 200 | 1786 | `cf7af5b39849a343c096e05c7b418f96d38f2e86777d897ea7afbb695f3392fd` |
| images/abstract.png | 200 | 961065 | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| prompts/abstract.txt | 200 | 1097 | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| images/abstract-quality-v1.png | 200 | 944574 | `93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b` |
| prompts/abstract-quality-v1.txt | 200 | 1774 | `5d4a776bab0b2ebee8c27787d85e2ff6c1c2d55ce81368a602adb13bc01c17e4` |
| images/monogram.png | 200 | 832716 | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| prompts/monogram.txt | 200 | 1060 | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| images/monogram-quality-v1.png | 200 | 855003 | `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f` |
| prompts/monogram-quality-v1.txt | 200 | 1847 | `8b4e552faad9451fd3a3f91bf17b20ea7eeb9489a34480fbc5f8f29e06427756` |
| images/soft-3d.png | 200 | 1526612 | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| prompts/soft-3d.txt | 200 | 1091 | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
| images/soft-3d-quality-v1.png | 200 | 1498775 | `ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2` |
| prompts/soft-3d-quality-v1.txt | 200 | 2004 | `4ecbd90914e59d66f3924f50ae7526771ab61e4a4ce4735a442fdda7dfb1ac78` |
| images/pixel-art.png | 200 | 946180 | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| prompts/pixel-art.txt | 200 | 1110 | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| images/pixel-art-quality-v1.png | 200 | 924570 | `29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328` |
| prompts/pixel-art-quality-v1.txt | 200 | 1899 | `706ef6130932940e17a9b0a4ac794390f9667353307e31bd75432476f52ba830` |

## Nine-class scenarios

All rejection fixtures lived under the registered temporary root. Real source originals were never altered.

| Class | Scenario | Status | Observed result / precise limit |
|---|---|---|---|
| 1 | malformed_receipt_missing_identity | PASS | Truncated JSON and a missing candidate ID rejected by the aggregation preflight in disposable receipt copies; CLI unknown artifact lookup also rejected. The helper does not parse native receipts; this is aggregation validation. |
| 2 | prompt_injection_data | PASS | Literal hostile prompt preserved as an exact UTF-8 download; brand and subject escaped in generated HTML; zero script tags and no shell marker. No hostile native call and no model-level immunity claim. |
| 3 | fresh_process_saved_resume | PASS | Six fresh helper show processes resumed catalog revision 16 with identical saved state; no prompt regeneration or native calls. No forced runtime cancellation was needed. |
| 4 | stale_duplicate_collision | PASS | Duplicate import and gallery IDs, stale revision 15, missing artifact, existing destination, and a disposable metadata hash mismatch all rejected; no files overwritten and no stale-hash gallery remained.  |
| 5 | dirty_worktree_preservation | PASS | Already dirty shared tree recorded before/after; 785 baseline files remain byte-identical, including existing original gallery, native sources, brand/color gallery assets and implementation files. Concurrent documentation work is outside this owner; Markdown changes by those owners are not reverted. |
| 6 | bounded_commands_http | PASS | Helper commands bounded to 30 seconds; curl connect 2 seconds / total 10 seconds; all 34 HTTP 200 bodies hashed; only recorded own PID 52715 stopped and port 8801 rebind verified. Native workers had already settled; no cancellation or induced network-hang probe is applicable. |
| 7 | flaky_or_artistic_retry | PASS | All five fixed new returned results retained at 1254 × 1254, no artistic reroll or image transform, no synthetic source tests added. Creative stochastic behavior is not an automated pass/fail benchmark. |
| 8 | native_calls_vs_catalog_copies | PASS | 16 historical/native originals = 11 previous calls + 5 fresh returned calls; this catalog worker invoked 0 native calls and imported 16 catalog copies. Selection/review/export/color-report state is empty. No model identity, strict color, export, platform or artistic approval claim. |
| 9 | repeat_identity_resume | PASS | Repeated per-receipt exact native paths, response hashes, prompts, source sessions and fixed attempt IDs unchanged; generation revision 0 kept separate from catalog expected revisions 0–15. No interrupted native attempt was restarted or replaced. |

Actual CLI errors were conflict for duplicate import/destination, stale_revision for revision 15, invalid_selection for duplicate IDs, not_found for an unknown artifact, and hash_mismatch for copied metadata with an altered hash. Workspace snapshots were unchanged across each rejection. The initial QA harness parsed stdout while the expected conflict JSON was on stderr; that harness error was recorded, corrected to parse the nonempty response stream, and the same disposable fixtures resumed. It caused no extra native call or production change.

## Resource inventory and cleanup

Persistent evidence is under `output/app-icons-quality-catalog-v1`: exact command transcript, per-file baseline/published hashes, source locators (private), normalized records, scenarios, HTTP evidence, server transcript, resource inventory and completed work ledger. Persistent deliverables are that catalog workspace, the 34-file public gallery and these three QA reports. Native source workspaces remain existing deliverables.

Temporary resources: `/tmp/ll-quality-catalog` with four QA scripts, copied catalog/session and injection fixtures, malformed/missing-ID receipts,34 HTTP download files and server log. The full 102-file temporary inventory, byte sizes and hashes were recorded before exact-root removal in `output/app-icons-quality-catalog-v1/resources.json`. The directory is absent. Server PID 52715 was verified as the port owner, stopped with SIGTERM, and confirmed absent; port 8801 is free and successful bind/close confirmed reuse. No other process or temporary directory was touched.

All 785 protected baseline files remain unchanged, including the complete original 11 gallery, existing color/brand gallery assets, native originals/prompts/receipts, source modules/templates/tests and old catalog. The initial dirty worktree and final status are recorded; other owners’ Markdown edits were preserved. Build/LSP/new software tests are not applicable to this artifact-only task. Actual CLI and HTTP behavior was exercised. Coordinator owns Chrome/native visual conclusions and D1 owns public documentation.

## Enumerated published files

| File | Bytes | SHA-256 |
|---|---|---|
| images/abstract-quality-v1.png | 944574 | `93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b` |
| images/abstract.png | 961065 | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| images/ip-a1.png | 1060303 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| images/ip-a2.png | 1049136 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| images/ip-b1.png | 1083251 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| images/ip-b2.png | 1039677 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| images/ip-c1.png | 1096895 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| images/ip-c2.png | 1089169 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| images/monogram-quality-v1.png | 855003 | `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f` |
| images/monogram.png | 832716 | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| images/pictogram-quality-v1.png | 924939 | `b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a` |
| images/pictogram.png | 928736 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| images/pixel-art-quality-v1.png | 924570 | `29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328` |
| images/pixel-art.png | 946180 | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| images/soft-3d-quality-v1.png | 1498775 | `ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2` |
| images/soft-3d.png | 1526612 | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| index.html | 27010 | `257154a6f6b4a77d355482f01462b76988610c85a0f4ff07d999ac0a3d3013e5` |
| manifest.json | 9721 | `ac8680b966658d0906914a4afd456ee21e9597f19a924815f0b6b7cfafb43a44` |
| prompts/abstract-quality-v1.txt | 1774 | `5d4a776bab0b2ebee8c27787d85e2ff6c1c2d55ce81368a602adb13bc01c17e4` |
| prompts/abstract.txt | 1097 | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| prompts/ip-a1.txt | 1377 | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| prompts/ip-a2.txt | 1393 | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| prompts/ip-b1.txt | 1391 | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| prompts/ip-b2.txt | 1394 | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| prompts/ip-c1.txt | 1388 | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| prompts/ip-c2.txt | 1403 | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| prompts/monogram-quality-v1.txt | 1847 | `8b4e552faad9451fd3a3f91bf17b20ea7eeb9489a34480fbc5f8f29e06427756` |
| prompts/monogram.txt | 1060 | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| prompts/pictogram-quality-v1.txt | 1786 | `cf7af5b39849a343c096e05c7b418f96d38f2e86777d897ea7afbb695f3392fd` |
| prompts/pictogram.txt | 1056 | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| prompts/pixel-art-quality-v1.txt | 1899 | `706ef6130932940e17a9b0a4ac794390f9667353307e31bd75432476f52ba830` |
| prompts/pixel-art.txt | 1110 | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| prompts/soft-3d-quality-v1.txt | 2004 | `4ecbd90914e59d66f3924f50ae7526771ab61e4a4ce4735a442fdda7dfb1ac78` |
| prompts/soft-3d.txt | 1091 | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
