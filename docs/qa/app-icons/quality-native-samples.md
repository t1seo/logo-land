# Original and refined app-icon provenance

Verified 2026-09-12T18:28:39.889Z. The [comparison gallery](../../app-icons-quality-v1/index.html) contains all sixteen originals: six unchanged IP examples and five original/refined non-IP pairs. The [machine-readable aggregate](quality-native-samples.json) records every exact prompt, source receipt/response, native filename, intent, dimensions and hash.

Five fresh native attempts returned once each. Eleven previous attempts remain unchanged. The catalog made **zero native calls** and performed sixteen normal helper imports; model identity is **unreported**. Actual outputs are all 1254 × 1254 PNGs, preserved without resizing or repair, although the prompts request approximately 1536-square.

Generation revision 0 and source-session revision 1 apply to each native attempt. Catalog expected revisions 0–15 identify copies in session `icon-quality-v1`, ending at revision 16. Historic prompts are copied verbatim and are never regenerated with the updated builder.

| ID | Era | Style | Generation → source session | Catalog before → after | Actual size | Provenance |
|---|---|---|---|---|---|---|
| ip-a1 | original | ip_mascot | 0 → 1 | 0 → 1 | 1254 × 1254 | [receipt](native/ip-a1.json) |
| ip-a2 | original | ip_mascot | 0 → 1 | 1 → 2 | 1254 × 1254 | [receipt](native/ip-a2.json) |
| ip-b1 | original | ip_mascot | 0 → 1 | 2 → 3 | 1254 × 1254 | [receipt](native/ip-b1.json) |
| ip-b2 | original | ip_mascot | 0 → 1 | 3 → 4 | 1254 × 1254 | [receipt](native/ip-b2.json) |
| ip-c1 | original | ip_mascot | 0 → 1 | 4 → 5 | 1254 × 1254 | [receipt](native/ip-c1.json) |
| ip-c2 | original | ip_mascot | 0 → 1 | 5 → 6 | 1254 × 1254 | [receipt](native/ip-c2.json) |
| pictogram | original | pictogram | 0 → 1 | 6 → 7 | 1254 × 1254 | [receipt](native/pictogram.json) |
| pictogram-quality-v1 | refined | pictogram | 0 → 1 | 7 → 8 | 1254 × 1254 | [receipt](native/pictogram-quality-v1.json) |
| abstract | original | abstract | 0 → 1 | 8 → 9 | 1254 × 1254 | [receipt](native/abstract.json) |
| abstract-quality-v1 | refined | abstract | 0 → 1 | 9 → 10 | 1254 × 1254 | [receipt](native/abstract-quality-v1.json) |
| monogram | original | monogram | 0 → 1 | 10 → 11 | 1254 × 1254 | [receipt](native/monogram.json) |
| monogram-quality-v1 | refined | monogram | 0 → 1 | 11 → 12 | 1254 × 1254 | [receipt](native/monogram-quality-v1.json) |
| soft-3d | original | soft_3d | 0 → 1 | 12 → 13 | 1254 × 1254 | [receipt](native/soft-3d.json) |
| soft-3d-quality-v1 | refined | soft_3d | 0 → 1 | 13 → 14 | 1254 × 1254 | [receipt](native/soft-3d-quality-v1.json) |
| pixel-art | original | pixel_art | 0 → 1 | 14 → 15 | 1254 × 1254 | [receipt](native/pixel-art.json) |
| pixel-art-quality-v1 | refined | pixel_art | 0 → 1 | 15 → 16 | 1254 × 1254 | [receipt](native/pixel-art-quality-v1.json) |

## Integrity

For all sixteen entries, exact native file, retained original, source helper import, new catalog import, generated gallery image, public image and HTTP body have one matching PNG SHA-256. Prompt file, saved source/catalog prompt, generated/public prompt download and HTTP body also match. All five saved native request prompts match the exact generation intent, planned concept and final stored prompt; complete app_icon intent, opaque background, null parent and original briefs were verified. Original receipts and785 protected files remain byte-identical.

| ID | PNG SHA-256 | Exact prompt SHA-256 |
|---|---|---|
| ip-a1 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| ip-a2 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| ip-b1 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| ip-b2 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| ip-c1 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| ip-c2 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| pictogram | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| pictogram-quality-v1 | `b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a` | `cf7af5b39849a343c096e05c7b418f96d38f2e86777d897ea7afbb695f3392fd` |
| abstract | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| abstract-quality-v1 | `93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b` | `5d4a776bab0b2ebee8c27787d85e2ff6c1c2d55ce81368a602adb13bc01c17e4` |
| monogram | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| monogram-quality-v1 | `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f` | `8b4e552faad9451fd3a3f91bf17b20ea7eeb9489a34480fbc5f8f29e06427756` |
| soft-3d | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
| soft-3d-quality-v1 | `ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2` | `4ecbd90914e59d66f3924f50ae7526771ab61e4a4ce4735a442fdda7dfb1ac78` |
| pixel-art | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| pixel-art-quality-v1 | `29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328` | `706ef6130932940e17a9b0a4ac794390f9667353307e31bd75432476f52ba830` |

## Limits and verification

The gallery has34 files, enumerated as16 PNGs +16 exact prompts +HTML +manifest. All 34 bounded HTTP requests returned 200 with matching bodies; [catalog QA](quality-catalog.md) covers local links, actual rejection/resume scenarios and resource cleanup. No image was selected, reviewed or exported; no strict-color, artistic, model-benchmark or platform-acceptance claim is made. Real Chrome/native-size comparisons and user-facing sample pages remain the coordinator and D1 responsibilities respectively.
