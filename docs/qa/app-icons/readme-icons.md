# App-icon Markdown pages QA

Task `task_e1a2dcc52a4d`; dispatch `ctx_8e56f18158dd`. Ownership: two app-icon Markdown indexes, 22 sample language files, and this report. The shared dirty tree and all other workers' files are preserved.

## Active work plan

The plan tool is unavailable; this ledger follows the final D1 contract in `plans/logo-land-app-icons.md` and `docs/research/readme-structure.md`. No new plan or child worker is required for this bounded dispatched implementation.

1. Completed: Verified 16 actual originals against native receipts, source/import/public PNGs, exact prompt bytes, session intents and IDs; all are 1254 × 1254. All 58 gallery baseline hashes match.
2. Completed: Wrote both indexes and all 22 sample language files; static verification passed and the coordinator was notified that D1-C may start. Only the Korean docs-index backlink awaits D1-C.
3. Completed: Verified all 24 public pages, 12 language pairs, 12 IP credit paragraphs and 254 local references with the single documented D1-C backlink pending. All 37 HTTP captures match final files; all 16 PNG and 16 prompt downloads match manifests. Nine QA classes are recorded below.
4. Completed: Recorded final evidence, terminated only the owned PID 60056, verified exec session 53458 exited 143 and port 8803 was free, and removed all 48 exact registered temporary files plus the empty temporary root.

## Resource register

Registered before creation/start with coordinator message `msg_62976417fb43`. Temporary root and port were absent at preflight.

- `/tmp/ll-readme-icons`: exact task-owned temporary root; remove after evidence transcription.
- Temporary scripts: `write-pages.rb`, `verify-pages.rb` (Ruby standard library, documentation helpers only).
- Temporary records/probes: `baseline.json`, `source-check.json`, `validation.json`, `malformed.json`, `missing-file.json`, `stale-manifest.json`, `quoted-input.md`.
- Temporary HTTP records: `monogram.http`, `ip-a1.http`, `ip-a1-ko.http`, `monogram-ko.http`, `monogram-reload.http`, `http-evidence.json`; `<16actualid>-image.http` and `<16actualid>-prompt.http` responses fetched from the authored pages' links.
- `python3 -m http.server 8803 --bind 127.0.0.1`, serving this repository only: register PID/session after start; `server.json`, `server.log` under the exact temporary root. No other server is owned by this task.

## Dependency evidence

Coordinator stable handoff `msg_b29037e27136` confirms catalog owner's `msg_438fb622e669` and independent byte comparison of all 34 published files. The catalog report and Chrome comparison can finish independently. No aesthetic verdict is awaited or inferred.

## Gallery hashes before any writes

Snapshot 2026-09-12T18:27:18Z; HEAD `ffecf1538963ddca5df1119d4e9d4d8dd2d5aac5` identifies the shared dirty snapshot, not committed content. All 24 old gallery files and 34 new gallery files are recorded here before page creation.

| File | Bytes | SHA-256 before writes |
|---|---:|---|
| `docs/app-icons-quality-v1/images/abstract-quality-v1.png` | 944574 | `93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b` |
| `docs/app-icons-quality-v1/images/abstract.png` | 961065 | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| `docs/app-icons-quality-v1/images/ip-a1.png` | 1060303 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| `docs/app-icons-quality-v1/images/ip-a2.png` | 1049136 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| `docs/app-icons-quality-v1/images/ip-b1.png` | 1083251 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| `docs/app-icons-quality-v1/images/ip-b2.png` | 1039677 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| `docs/app-icons-quality-v1/images/ip-c1.png` | 1096895 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| `docs/app-icons-quality-v1/images/ip-c2.png` | 1089169 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| `docs/app-icons-quality-v1/images/monogram-quality-v1.png` | 855003 | `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f` |
| `docs/app-icons-quality-v1/images/monogram.png` | 832716 | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| `docs/app-icons-quality-v1/images/pictogram-quality-v1.png` | 924939 | `b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a` |
| `docs/app-icons-quality-v1/images/pictogram.png` | 928736 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| `docs/app-icons-quality-v1/images/pixel-art-quality-v1.png` | 924570 | `29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328` |
| `docs/app-icons-quality-v1/images/pixel-art.png` | 946180 | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| `docs/app-icons-quality-v1/images/soft-3d-quality-v1.png` | 1498775 | `ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2` |
| `docs/app-icons-quality-v1/images/soft-3d.png` | 1526612 | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| `docs/app-icons-quality-v1/index.html` | 27010 | `257154a6f6b4a77d355482f01462b76988610c85a0f4ff07d999ac0a3d3013e5` |
| `docs/app-icons-quality-v1/manifest.json` | 9721 | `ac8680b966658d0906914a4afd456ee21e9597f19a924815f0b6b7cfafb43a44` |
| `docs/app-icons-quality-v1/prompts/abstract-quality-v1.txt` | 1774 | `5d4a776bab0b2ebee8c27787d85e2ff6c1c2d55ce81368a602adb13bc01c17e4` |
| `docs/app-icons-quality-v1/prompts/abstract.txt` | 1097 | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| `docs/app-icons-quality-v1/prompts/ip-a1.txt` | 1377 | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| `docs/app-icons-quality-v1/prompts/ip-a2.txt` | 1393 | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| `docs/app-icons-quality-v1/prompts/ip-b1.txt` | 1391 | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| `docs/app-icons-quality-v1/prompts/ip-b2.txt` | 1394 | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| `docs/app-icons-quality-v1/prompts/ip-c1.txt` | 1388 | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| `docs/app-icons-quality-v1/prompts/ip-c2.txt` | 1403 | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| `docs/app-icons-quality-v1/prompts/monogram-quality-v1.txt` | 1847 | `8b4e552faad9451fd3a3f91bf17b20ea7eeb9489a34480fbc5f8f29e06427756` |
| `docs/app-icons-quality-v1/prompts/monogram.txt` | 1060 | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| `docs/app-icons-quality-v1/prompts/pictogram-quality-v1.txt` | 1786 | `cf7af5b39849a343c096e05c7b418f96d38f2e86777d897ea7afbb695f3392fd` |
| `docs/app-icons-quality-v1/prompts/pictogram.txt` | 1056 | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| `docs/app-icons-quality-v1/prompts/pixel-art-quality-v1.txt` | 1899 | `706ef6130932940e17a9b0a4ac794390f9667353307e31bd75432476f52ba830` |
| `docs/app-icons-quality-v1/prompts/pixel-art.txt` | 1110 | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| `docs/app-icons-quality-v1/prompts/soft-3d-quality-v1.txt` | 2004 | `4ecbd90914e59d66f3924f50ae7526771ab61e4a4ce4735a442fdda7dfb1ac78` |
| `docs/app-icons-quality-v1/prompts/soft-3d.txt` | 1091 | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
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
| `docs/app-icons/index.html` | 21510 | `e87c1e9d3a78b6404d5560d8e778e8ef812618e7f13d1e7ed7a1d3b18e74a1bd` |
| `docs/app-icons/manifest.json` | 6655 | `fe6b2183a34beadf3932f00a63999ba17015792f15f87511b14a0ed9d9801dc9` |
| `docs/app-icons/prompts/abstract.txt` | 1097 | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| `docs/app-icons/prompts/ip-a1.txt` | 1377 | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| `docs/app-icons/prompts/ip-a2.txt` | 1393 | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| `docs/app-icons/prompts/ip-b1.txt` | 1391 | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| `docs/app-icons/prompts/ip-b2.txt` | 1394 | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| `docs/app-icons/prompts/ip-c1.txt` | 1388 | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| `docs/app-icons/prompts/ip-c2.txt` | 1403 | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| `docs/app-icons/prompts/monogram.txt` | 1060 | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| `docs/app-icons/prompts/pictogram.txt` | 1056 | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| `docs/app-icons/prompts/pixel-art.txt` | 1110 | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| `docs/app-icons/prompts/soft-3d.txt` | 1091 | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |

## Authored page map and final hashes

Two category indexes and 11 sample pages per language are retained, for 24 public Markdown files. The six IP samples each contain exactly one requested subject/corner example and one original. Five non-IP sample pages contain an Original / Revised direction pair with two separately linked original files and exact saved prompts. The current two monogram intent records and both localized example requests retain `모` (U+BAA8).

Coordinator steering `msg_edeaf514d4db` requested a compact comparison after initial authoring. The final five bilingual pairs use ordinary Markdown tables with GitHub-supported `img` elements at width 144; each IP preview uses width 288. No CSS, framework, image derivative or HTML gallery edit was made. Initial page HTTP captures were replaced by fresh final-page captures after this change. Final stable-page handoff is `msg_4ba07fe5b8ec`; primary paths did not change.

| Authored public file | Bytes | Final SHA-256 |
|---|---:|---|
| `docs/app-icons/samples/abstract.ko.md` | 1194 | `da522fb07d3be21528c880e85c9e371f4f0bdada115f6c3c806fe10106914ccf` |
| `docs/app-icons/samples/abstract.md` | 1062 | `fe485ab06d4b634680ecfcb07ae7bd217e63b8030ac9b9865c2c6d6faeba1491` |
| `docs/app-icons/samples/ip-a1.ko.md` | 1419 | `ce75bcfe7aa7978cb438451e2cc605e28b1f72192947c1be2d66b1826f8386dd` |
| `docs/app-icons/samples/ip-a1.md` | 1234 | `b9d35f6af0741973431ec69ffe574f977961d15fda1720b70c65c077dd41a60e` |
| `docs/app-icons/samples/ip-a2.ko.md` | 1431 | `bd06a8a466a68b84db273f72e5f6c948aa605f76ccc055ea39d9196527be87ab` |
| `docs/app-icons/samples/ip-a2.md` | 1238 | `709a643fdc68fd883d36bd7b3d50661de52dc2971b7ea5bfdf8aea401598f06b` |
| `docs/app-icons/samples/ip-b1.ko.md` | 1451 | `a21b753ed877e9087e9443231bc1051b891df1eb178dfe6388852a2384ef2f01` |
| `docs/app-icons/samples/ip-b1.md` | 1266 | `ac8413878c7e3387501be3a2bd000b3a2297862d9da68c84c11f9ac06436a7a1` |
| `docs/app-icons/samples/ip-b2.ko.md` | 1463 | `0c33faa792d1ed31489999c05df16927fb0b9006f518a63696af9ea8e28902fc` |
| `docs/app-icons/samples/ip-b2.md` | 1270 | `d821417b4fdf2ef05b82687255c1c69528f2b62d02768bd945c834017700f74f` |
| `docs/app-icons/samples/ip-c1.ko.md` | 1425 | `458b4f58df9e91c866ab34e51b4d971cea0590f5974bb0b972c9eb5d2df1cdc3` |
| `docs/app-icons/samples/ip-c1.md` | 1238 | `2744f862751da80f37e753d145492b8601091400a5595389becf1bb9ccc12f58` |
| `docs/app-icons/samples/ip-c2.ko.md` | 1437 | `e5434756c9d1d147439752c70cedc5ae2a51c6e35393f1898124a45a4788f0a3` |
| `docs/app-icons/samples/ip-c2.md` | 1242 | `604e5d24c70ea6d554ee88dd5af3381af4975d6b3139044b4873c085d068a816` |
| `docs/app-icons/samples/monogram.ko.md` | 1274 | `dcd06e3f0990625914daa690e1d95de559be2bd4d87e2c4f575ad919a9ba55f5` |
| `docs/app-icons/samples/monogram.md` | 1090 | `417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580` |
| `docs/app-icons/samples/pictogram.ko.md` | 1174 | `bc260c48649afaaf1891161076f51037017dbd4142b7a1dc002920d88505f9d8` |
| `docs/app-icons/samples/pictogram.md` | 1037 | `cb04a2a98211b827d1c06234d9f9e31769f484f8329d44e2ed182f524b3517d4` |
| `docs/app-icons/samples/pixel-art.ko.md` | 1241 | `d0388047ddd216367509be39f032a325609208772c49bde29c6466435307cfc5` |
| `docs/app-icons/samples/pixel-art.md` | 1073 | `a34a71b7e0cd563844805d8b0c29df50e3d23dcfe690464d747f1164437da79d` |
| `docs/app-icons/samples/soft-3d.ko.md` | 1232 | `a358570625ed696089b75020595d1c92cd84b4603b33cab5ee059759c07f5cfa` |
| `docs/app-icons/samples/soft-3d.md` | 1053 | `37428e43c8b35702bb1233d5aac5fd2acaeb7f4d8b81b1a736f8afcee0dcbdbd` |
| `docs/app-icons/README.ko.md` | 1468 | `7febf2b847fe5d104e4ba3a5c87f6a7f1e3674bf19eb87754d72048c7047421f` |
| `docs/app-icons/README.md` | 1226 | `c4e85865f13ad3ba8eaf0e5de9d6b7d491a05f629a172893251f3c9b2da117cc` |

## Source, prompt and image verification

At 2026-09-12T18:28:12Z, independently parsed both manifests and all 16 native receipts. Each artifact ID, receipt image/prompt digest, preserved native original, session imported PNG, session intent and exact session prompt agreed with the published manifest. The 11 old entries are identical in the new manifest, with five additional actual originals. PNG signature/IHDR dimensions and a separate read-only macOS `sips -g format -g pixelWidth -g pixelHeight` inspection recognize all 16 files as 1254 × 1254 PNGs.

The source prompt path for every row is `output/app-icons-native/<id>/prompt.txt`; each was compared byte-for-byte by SHA-256 with the exact session prompt and published prompt. Receipt path is `docs/qa/app-icons/native/<id>.json`. The saved exact prompts remain unchanged; newly authored blockquote requests are labeled examples.

| ID | Preserved source PNG | Imported session PNG | PNG bytes / prompt bytes |
|---|---|---|---:|
| `ip-a1` | `output/app-icons-native/ip-a1/original.png` | `output/app-icons-native/ip-a1/.logo-generator/sessions/ip-a1/artifacts/ip-a1.png` | 1060303 / 1377 |
| `ip-a2` | `output/app-icons-native/ip-a2/original.png` | `output/app-icons-native/ip-a2/.logo-generator/sessions/ip-a2/artifacts/ip-a2.png` | 1049136 / 1393 |
| `ip-b1` | `output/app-icons-native/ip-b1/original.png` | `output/app-icons-native/ip-b1/.logo-generator/sessions/ip-b1/artifacts/ip-b1.png` | 1083251 / 1391 |
| `ip-b2` | `output/app-icons-native/ip-b2/original.png` | `output/app-icons-native/ip-b2/.logo-generator/sessions/ip-b2/artifacts/ip-b2.png` | 1039677 / 1394 |
| `ip-c1` | `output/app-icons-native/ip-c1/original.png` | `output/app-icons-native/ip-c1/.logo-generator/sessions/ip-c1/artifacts/ip-c1.png` | 1096895 / 1388 |
| `ip-c2` | `output/app-icons-native/ip-c2/original.png` | `output/app-icons-native/ip-c2/.logo-generator/sessions/ip-c2/artifacts/ip-c2.png` | 1089169 / 1403 |
| `pictogram` | `output/app-icons-native/pictogram/original.png` | `output/app-icons-native/pictogram/.logo-generator/sessions/pictogram/artifacts/pictogram.png` | 928736 / 1056 |
| `pictogram-quality-v1` | `output/app-icons-native/pictogram-quality-v1/original.png` | `output/app-icons-native/pictogram-quality-v1/.logo-generator/sessions/pictogram-quality-v1/artifacts/pictogram-quality-v1.png` | 924939 / 1786 |
| `abstract` | `output/app-icons-native/abstract/original.png` | `output/app-icons-native/abstract/.logo-generator/sessions/abstract/artifacts/abstract.png` | 961065 / 1097 |
| `abstract-quality-v1` | `output/app-icons-native/abstract-quality-v1/original.png` | `output/app-icons-native/abstract-quality-v1/.logo-generator/sessions/abstract-quality-v1/artifacts/abstract-quality-v1.png` | 944574 / 1774 |
| `monogram` | `output/app-icons-native/monogram/original.png` | `output/app-icons-native/monogram/.logo-generator/sessions/monogram/artifacts/monogram.png` | 832716 / 1060 |
| `monogram-quality-v1` | `output/app-icons-native/monogram-quality-v1/original.png` | `output/app-icons-native/monogram-quality-v1/.logo-generator/sessions/monogram-quality-v1/artifacts/monogram-quality-v1.png` | 855003 / 1847 |
| `soft-3d` | `output/app-icons-native/soft-3d/original.png` | `output/app-icons-native/soft-3d/.logo-generator/sessions/soft-3d/artifacts/soft-3d.png` | 1526612 / 1091 |
| `soft-3d-quality-v1` | `output/app-icons-native/soft-3d-quality-v1/original.png` | `output/app-icons-native/soft-3d-quality-v1/.logo-generator/sessions/soft-3d-quality-v1/artifacts/soft-3d-quality-v1.png` | 1498775 / 2004 |
| `pixel-art` | `output/app-icons-native/pixel-art/original.png` | `output/app-icons-native/pixel-art/.logo-generator/sessions/pixel-art/artifacts/pixel-art.png` | 946180 / 1110 |
| `pixel-art-quality-v1` | `output/app-icons-native/pixel-art-quality-v1/original.png` | `output/app-icons-native/pixel-art-quality-v1/.logo-generator/sessions/pixel-art-quality-v1/artifacts/pixel-art-quality-v1.png` | 924570 / 1899 |

Read [Q5 catalog receipt](quality-catalog.md) after it became available: its completed provenance/download observations agree with this independent verification. [Q5 Chrome comparison](quality-comparison.md) was still marked “In progress” when inspected and contained registration/baseline records rather than paired conclusions. Public pages therefore describe product, subject and direction factually; they make no automatic improvement, selection, production-readiness or store-approval claim. The category indexes state the raster/platform preparation limit in both languages. Final artistic comparison and narrow rendered layout are assigned to the separate Chrome owner.

## Link, language and credit verification

The final read-only documentation verifier found 254 local link/image occurrences and 12 direct upstream credit URLs. All sample pages have reciprocal language switches and matching normalized navigation, image, original-download, prompt and credit targets. Each index lists all 11 named samples in six style groups. Every public page is valid UTF-8, ends in a newline and has no trailing whitespace. `git diff --check` for the owned scope exited 0; untracked Markdown was also checked directly.

All six IP pages in both languages say “adapted from” / “바탕으로 각색했습니다” with a direct `https://github.com/s1dashu/ip-as-logo-skill` link and links to the pinned adaptation reference, MIT notice and third-party notices. The referenced local adaptation pins `acb834c717bcd0a487c49732d08397ba280d690b`; its bundled license is an actual MIT notice. No whole-repository MIT declaration was added. Each English IP example says “exactly one IP character candidate”; each Korean example says “시안 한 개만” and preserves its specific owl/capybara/puppy subject and left/right placement.

The only pending local destination at the final scoped scan was `docs/app-icons/README.ko.md` → `../README.ko.md`, owned by future D1-C. All other 253 local occurrences resolved. These pages introduce no fragment links; the verifier supports explicit HTML anchors and Markdown headings, but no new fragment behavior was exercised. Existing gallery/anchor bytes remain protected by the 58-file baseline. This is not a full-repository link-success claim.

## Actual bounded HTTP evidence

Owned server: PID `60056`, exec session `53458`, `127.0.0.1:8803`, repository root. The exact required command ran successfully against the final compact page:

```sh
curl -i --fail --silent --show-error --connect-timeout 2 --max-time 10 http://127.0.0.1:8803/docs/app-icons/samples/monogram.md -o /tmp/ll-readme-icons/monogram.http
```

Final response:

```http
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.9.6
Date: Sat, 12 Sep 2026 18:31:39 GMT
Content-type: application/octet-stream
Content-Length: 1090
Last-Modified: Sat, 12 Sep 2026 18:31:18 GMT
```

Splitting each capture at the first CRLF/CRLF yielded a body exactly equal to its final repository file. Five final page captures include the monogram page twice, its Korean counterpart, and the actual English/Korean IP attribution pages. Final page refresh timestamp: 2026-09-12T18:31:39Z. Korean responses are valid UTF-8; monogram responses contain exact `모`, and both IP responses contain the real direct credit URL.

The other 32 captures were fetched from actual authored Markdown download links: 16 PNGs and 16 exact prompt files. All returned HTTP 200 and matched both local original bytes and manifest hashes. In particular, the old monogram body is 832,716 bytes with SHA-256 `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b`; the revised original is 855,003 bytes with SHA-256 `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f`. Every curl used a 2-second connect timeout and 10-second total timeout, with no blind retries.

| Actual repository URL path | HTTP | Body bytes | Body SHA-256 |
|---|---:|---:|---|
| `docs/app-icons/samples/monogram.md` | 200 | 1090 | `417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580` |
| `docs/app-icons/samples/ip-a1.md` | 200 | 1234 | `b9d35f6af0741973431ec69ffe574f977961d15fda1720b70c65c077dd41a60e` |
| `docs/app-icons/samples/ip-a1.ko.md` | 200 | 1419 | `ce75bcfe7aa7978cb438451e2cc605e28b1f72192947c1be2d66b1826f8386dd` |
| `docs/app-icons/samples/monogram.ko.md` | 200 | 1274 | `dcd06e3f0990625914daa690e1d95de559be2bd4d87e2c4f575ad919a9ba55f5` |
| `docs/app-icons/samples/monogram.md` | 200 | 1090 | `417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580` |
| `docs/app-icons/images/ip-a1.png` | 200 | 1060303 | `7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b` |
| `docs/app-icons/prompts/ip-a1.txt` | 200 | 1377 | `a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd` |
| `docs/app-icons/images/ip-a2.png` | 200 | 1049136 | `74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd` |
| `docs/app-icons/prompts/ip-a2.txt` | 200 | 1393 | `5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c` |
| `docs/app-icons/images/ip-b1.png` | 200 | 1083251 | `1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a` |
| `docs/app-icons/prompts/ip-b1.txt` | 200 | 1391 | `cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3` |
| `docs/app-icons/images/ip-b2.png` | 200 | 1039677 | `c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069` |
| `docs/app-icons/prompts/ip-b2.txt` | 200 | 1394 | `62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555` |
| `docs/app-icons/images/ip-c1.png` | 200 | 1096895 | `93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28` |
| `docs/app-icons/prompts/ip-c1.txt` | 200 | 1388 | `020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e` |
| `docs/app-icons/images/ip-c2.png` | 200 | 1089169 | `64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916` |
| `docs/app-icons/prompts/ip-c2.txt` | 200 | 1403 | `e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4` |
| `docs/app-icons/images/pictogram.png` | 200 | 928736 | `f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42` |
| `docs/app-icons/prompts/pictogram.txt` | 200 | 1056 | `4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f` |
| `docs/app-icons-quality-v1/images/pictogram-quality-v1.png` | 200 | 924939 | `b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a` |
| `docs/app-icons-quality-v1/prompts/pictogram-quality-v1.txt` | 200 | 1786 | `cf7af5b39849a343c096e05c7b418f96d38f2e86777d897ea7afbb695f3392fd` |
| `docs/app-icons/images/abstract.png` | 200 | 961065 | `7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4` |
| `docs/app-icons/prompts/abstract.txt` | 200 | 1097 | `a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb` |
| `docs/app-icons-quality-v1/images/abstract-quality-v1.png` | 200 | 944574 | `93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b` |
| `docs/app-icons-quality-v1/prompts/abstract-quality-v1.txt` | 200 | 1774 | `5d4a776bab0b2ebee8c27787d85e2ff6c1c2d55ce81368a602adb13bc01c17e4` |
| `docs/app-icons/images/monogram.png` | 200 | 832716 | `964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b` |
| `docs/app-icons/prompts/monogram.txt` | 200 | 1060 | `cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83` |
| `docs/app-icons-quality-v1/images/monogram-quality-v1.png` | 200 | 855003 | `e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f` |
| `docs/app-icons-quality-v1/prompts/monogram-quality-v1.txt` | 200 | 1847 | `8b4e552faad9451fd3a3f91bf17b20ea7eeb9489a34480fbc5f8f29e06427756` |
| `docs/app-icons/images/soft-3d.png` | 200 | 1526612 | `da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63` |
| `docs/app-icons/prompts/soft-3d.txt` | 200 | 1091 | `3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c` |
| `docs/app-icons-quality-v1/images/soft-3d-quality-v1.png` | 200 | 1498775 | `ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2` |
| `docs/app-icons-quality-v1/prompts/soft-3d-quality-v1.txt` | 200 | 2004 | `4ecbd90914e59d66f3924f50ae7526771ab61e4a4ce4735a442fdda7dfb1ac78` |
| `docs/app-icons/images/pixel-art.png` | 200 | 946180 | `87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5` |
| `docs/app-icons/prompts/pixel-art.txt` | 200 | 1110 | `d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad` |
| `docs/app-icons-quality-v1/images/pixel-art-quality-v1.png` | 200 | 924570 | `29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328` |
| `docs/app-icons-quality-v1/prompts/pixel-art-quality-v1.txt` | 200 | 1899 | `706ef6130932940e17a9b0a4ac794390f9667353307e31bd75432476f52ba830` |

HTTP proves exact delivery of Markdown and original files. It does not establish hosted GitHub rendering, narrow layout appearance, or an artistic quality verdict. Actual Chrome rendering belongs to the separate final owner.

## Nine-class audit

| Class | Actual observation or precise N/A |
|---|---|
| 1. Malformed/missing input | Disposable malformed JSON was rejected with `JSON::ParserError`; absent manifest with `Errno::ENOENT`; a copied manifest pointing to an absent image was rejected as “missing image file.” Production originals were never removed or changed. These exercise the documentation verifier, not the product CLI. |
| 2. Quoted untrusted example | A temporary Markdown blockquote contained literal shell substitutions/backticks and “ignore prior instructions.” It was read as string data, produced no link/action, and the named execution sentinel remained absent. Saved prompts were read/downloaded as bytes; no native/model injection-resistance claim is made. |
| 3. Cancellation/resume | A fresh Ruby process reloaded baseline/manifests/pages and repeated the complete checks successfully; a second HTTP monogram fetch matched the final page. Forced cancellation, transaction recovery and native-call resume are N/A: this task created only static documentation and a read-only server. |
| 4. Stale hashes | A copied manifest with a zeroed image digest was rejected as “stale image hash.” The real 58-file baseline was checked before authoring and after probes/revisions; all hashes match. IDs/intent were checked directly against fresh session and manifest reads. |
| 5. Shared dirty tree | Pre-existing source, root README, sibling pages and QA changes were visible at initial `git status`. Writes were limited to 24 owned pages, this report and registered temporary resources. No unrelated edits were reverted, committed or attributed to this worker. |
| 6. Bounded resources | Server/port/temp were registered before creation. All HTTP operations used 2/10-second bounds. One owned server PID/session is recorded; no GUI, child workers, installs or new dependency was started. |
| 7. Retry/artistic variance | No generation, image editing, reroll or pixel repair occurred. HTTP refresh followed the concrete compact-layout edit and retained the same original downloads. No aesthetic retry or fictional generation result was introduced. |
| 8. Truthful success and authority | Only 16 actual native source/import/published originals are shown; “Original” and “Revised direction” are labels, not acceptance. Source tests, build and LSP diagnostics are N/A for these static Markdown edits; no artificial product tests were added. HTTP and static checks do not substitute for the separate final Chrome owner, platform preparation or artistic review. |
| 9. Repeated reads/history | Original 24-file gallery and new 34-file catalog stay byte-identical through fresh reads, negative probes, compact-layout steering and HTTP download checks. All 11 original pages/IDs are retained; exact prompts and old HTML history are intact. Coordinator instructions were incorporated into the same task. |

## Temporary inventory and cleanup

The 48 actual temporary files below are transcribed before deletion. `write-pages.rb` was reserved but never created because pages were written through structured patches. The missing-manifest and injection-sentinel names were absence probes and never created. No temporary file outside this exact root was created.

```text
/tmp/ll-readme-icons/abstract-image.http
/tmp/ll-readme-icons/abstract-prompt.http
/tmp/ll-readme-icons/abstract-quality-v1-image.http
/tmp/ll-readme-icons/abstract-quality-v1-prompt.http
/tmp/ll-readme-icons/baseline.json
/tmp/ll-readme-icons/http-evidence.json
/tmp/ll-readme-icons/ip-a1-image.http
/tmp/ll-readme-icons/ip-a1-ko.http
/tmp/ll-readme-icons/ip-a1-prompt.http
/tmp/ll-readme-icons/ip-a1.http
/tmp/ll-readme-icons/ip-a2-image.http
/tmp/ll-readme-icons/ip-a2-prompt.http
/tmp/ll-readme-icons/ip-b1-image.http
/tmp/ll-readme-icons/ip-b1-prompt.http
/tmp/ll-readme-icons/ip-b2-image.http
/tmp/ll-readme-icons/ip-b2-prompt.http
/tmp/ll-readme-icons/ip-c1-image.http
/tmp/ll-readme-icons/ip-c1-prompt.http
/tmp/ll-readme-icons/ip-c2-image.http
/tmp/ll-readme-icons/ip-c2-prompt.http
/tmp/ll-readme-icons/malformed.json
/tmp/ll-readme-icons/missing-file.json
/tmp/ll-readme-icons/monogram-image.http
/tmp/ll-readme-icons/monogram-ko.http
/tmp/ll-readme-icons/monogram-prompt.http
/tmp/ll-readme-icons/monogram-quality-v1-image.http
/tmp/ll-readme-icons/monogram-quality-v1-prompt.http
/tmp/ll-readme-icons/monogram-reload.http
/tmp/ll-readme-icons/monogram.http
/tmp/ll-readme-icons/pictogram-image.http
/tmp/ll-readme-icons/pictogram-prompt.http
/tmp/ll-readme-icons/pictogram-quality-v1-image.http
/tmp/ll-readme-icons/pictogram-quality-v1-prompt.http
/tmp/ll-readme-icons/pixel-art-image.http
/tmp/ll-readme-icons/pixel-art-prompt.http
/tmp/ll-readme-icons/pixel-art-quality-v1-image.http
/tmp/ll-readme-icons/pixel-art-quality-v1-prompt.http
/tmp/ll-readme-icons/quoted-input.md
/tmp/ll-readme-icons/server.json
/tmp/ll-readme-icons/server.log
/tmp/ll-readme-icons/soft-3d-image.http
/tmp/ll-readme-icons/soft-3d-prompt.http
/tmp/ll-readme-icons/soft-3d-quality-v1-image.http
/tmp/ll-readme-icons/soft-3d-quality-v1-prompt.http
/tmp/ll-readme-icons/source-check.json
/tmp/ll-readme-icons/stale-manifest.json
/tmp/ll-readme-icons/validation.json
/tmp/ll-readme-icons/verify-pages.rb
```

Cleanup completed on 2026-09-12 UTC: only owned PID 60056 received TERM after its command identity was checked; exec session 53458 exited 143. `lsof -nP -iTCP:8803 -sTCP:LISTEN` returned no listener. The exact 48 registered files were removed, then the empty `/tmp/ll-readme-icons` directory; its absence was verified. Public pages and this report are retained. No gallery restoration is required.

The final fresh-process scan at 2026-09-12T18:33:16Z passed the same 24 pages, 12 language pairs, 12 credit paragraphs, all negative probes and all 58 preserved gallery hashes. The single Korean docs-index backlink remained a D1-C dependency. Actual Chrome/narrow rendering is separately owned and not claimed by this worker.
