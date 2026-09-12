# D1 actual Chrome rendered Markdown QA

Task `task_bcee3bd3da72`, dispatch `ctx_94c5b5826f3d`. Completed: PASS for the representative local rendered Markdown/asset/navigation checks after the category-map repair; original failed navigation and process variances are retained below. D1-C final source readiness message msg_ec3c16d48c2e received.

Before creation: register one temporary QA tab in the owned comparison gallery window; close it after verification. Register `docs/qa/app-icons/readme-chrome/` raw screenshots. Reuse registered exact `/tmp/ll-quality-chrome` root only for owned downloads if required. No server, source/README/preview edits or native calls permitted. Preserve user windows/tabs.

Preview provenance checked before screenshot:
```json
[
  {
    "preview": "docs/qa/app-icons/readme-preview/brand-en.html",
    "previewHash": "64fad756f565e3a5e927ed62a824defa2060ed77eb504bac0ae41d61213c59bb",
    "source": "docs/samples/items/03-goyo/README.md",
    "embedded": "eb2fc0833a115c9bc217ece47c9e1d714fabe2eed2fae6ad64c158f4f5fb7fe3",
    "actual": "eb2fc0833a115c9bc217ece47c9e1d714fabe2eed2fae6ad64c158f4f5fb7fe3",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/brand-ko.html",
    "previewHash": "b7fd47402a5ce757de0cabd795231087c0f01b9cb3f292ea7542e2f1eeddf069",
    "source": "docs/samples/items/03-goyo/README.ko.md",
    "embedded": "bd0601f9342d2e8d03cf359705f795e763935cc7f8b6405402ad70ee973b2806",
    "actual": "bd0601f9342d2e8d03cf359705f795e763935cc7f8b6405402ad70ee973b2806",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/ip-en.html",
    "previewHash": "aa768af6b3e1a8568303ec89b7e820c75630646d35d4f07754b66b668d413e0d",
    "source": "docs/app-icons/samples/ip-a1.md",
    "embedded": "b9d35f6af0741973431ec69ffe574f977961d15fda1720b70c65c077dd41a60e",
    "actual": "b9d35f6af0741973431ec69ffe574f977961d15fda1720b70c65c077dd41a60e",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/ip-ko.html",
    "previewHash": "45907cc94bc79aac2454bb1286073440bca1be5caf1b9bd11ff16fce846c28b8",
    "source": "docs/app-icons/samples/ip-a1.ko.md",
    "embedded": "ce75bcfe7aa7978cb438451e2cc605e28b1f72192947c1be2d66b1826f8386dd",
    "actual": "ce75bcfe7aa7978cb438451e2cc605e28b1f72192947c1be2d66b1826f8386dd",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/pair-en.html",
    "previewHash": "99ef3cc4dd343a95fce5cfac85d42744ea5bcbc7a02469b29da55a7f03cfe9d2",
    "source": "docs/app-icons/samples/monogram.md",
    "embedded": "417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580",
    "actual": "417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/pair-ko.html",
    "previewHash": "82e70985fa72ed958d137ed6264cc1b67dfd894020920da9b2bff546b75c57b7",
    "source": "docs/app-icons/samples/monogram.ko.md",
    "embedded": "dcd06e3f0990625914daa690e1d95de559be2bd4d87e2c4f575ad919a9ba55f5",
    "actual": "dcd06e3f0990625914daa690e1d95de559be2bd4d87e2c4f575ad919a9ba55f5",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/readme-en.html",
    "previewHash": "b760d5dfec4b38abd65c8ac9ed71760cee8556223fa81b7b1f2f03cfaa8ddd3a",
    "source": "README.md",
    "embedded": "e3910e4a691ce1e555e8aa3461c2a01ced90f5e1c6014f4bdc21622fd89ccfec",
    "actual": "e3910e4a691ce1e555e8aa3461c2a01ced90f5e1c6014f4bdc21622fd89ccfec",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/readme-ko.html",
    "previewHash": "5addebac0106ddb8d29ff09c4d28decdd1f07c865fcec3709c022543cba72cfb",
    "source": "README.ko.md",
    "embedded": "a0746d3f4df7cf036eabfdbffc07b7c0b9c94b738a63d13b1da27b6ee493cb11",
    "actual": "a0746d3f4df7cf036eabfdbffc07b7c0b9c94b738a63d13b1da27b6ee493cb11",
    "match": true
  }
]
```

Final-file baseline:
```json
{
  "time": "2026-09-12T18:38:17.449Z",
  "files": {
    "README.md": "e3910e4a691ce1e555e8aa3461c2a01ced90f5e1c6014f4bdc21622fd89ccfec",
    "README.ko.md": "a0746d3f4df7cf036eabfdbffc07b7c0b9c94b738a63d13b1da27b6ee493cb11",
    "assets/logo-land-studio.png": "11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3",
    "docs/app-icons/README.ko.md": "7febf2b847fe5d104e4ba3a5c87f6a7f1e3674bf19eb87754d72048c7047421f",
    "docs/app-icons/README.md": "c4e85865f13ad3ba8eaf0e5de9d6b7d491a05f629a172893251f3c9b2da117cc",
    "docs/app-icons/images/abstract.png": "7e4ee1c24856ccea76e46111fa3a09a0e75b8cd958a029a764cad9a38192f0c4",
    "docs/app-icons/images/ip-a1.png": "7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b",
    "docs/app-icons/images/ip-a2.png": "74cccbfda855b1a1f623b7bb25103a9adec2d3a075df13fcabb9b3d46c72f1fd",
    "docs/app-icons/images/ip-b1.png": "1407715a0df952115cc3ed40c8a0398d7fc0afe0661d78b0f2c6d3b8983a081a",
    "docs/app-icons/images/ip-b2.png": "c7f4618ecdaaf828760f6b81deb40674b8f62126f1ffc934e452a86c86f3f069",
    "docs/app-icons/images/ip-c1.png": "93d5a457e440c05802006d908299b427771f53e61dfd51cb4c7b1316c9504f28",
    "docs/app-icons/images/ip-c2.png": "64de02e82dc46635efcdce46d51d1aefe5501c0b075495af8d063ef901416916",
    "docs/app-icons/images/monogram.png": "964a698a273333ac7aa60e72cbe244643af0d64337cc8f5f13fefc09b992fe1b",
    "docs/app-icons/images/pictogram.png": "f02af7a96e63be9756c23a926d1e058e5fb23de485d0627c6be5871a72455b42",
    "docs/app-icons/images/pixel-art.png": "87b243cde70955743793b88f0ed5aaa1b747ff8ec2b1e4b5654b0fa835991cf5",
    "docs/app-icons/images/soft-3d.png": "da5ad53245b728c0d9d44cada1394a1e3d4dfab985b3bf79d9d57ccf7673dc63",
    "docs/app-icons/index.html": "e87c1e9d3a78b6404d5560d8e778e8ef812618e7f13d1e7ed7a1d3b18e74a1bd",
    "docs/app-icons/manifest.json": "fe6b2183a34beadf3932f00a63999ba17015792f15f87511b14a0ed9d9801dc9",
    "docs/app-icons/prompts/abstract.txt": "a1e1beb899e0c01a417e2c93e7327af94ddfe0215d1ed0fb31e7ec266ba32efb",
    "docs/app-icons/prompts/ip-a1.txt": "a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd",
    "docs/app-icons/prompts/ip-a2.txt": "5a2b308974655d468cb7ce83827c5942e39504771c91fa84ec2e119436fe1b9c",
    "docs/app-icons/prompts/ip-b1.txt": "cc2e94e36d4c5c24d5da9cffca145e50e042b472fdd7b0bc4bf7f8e44bad13e3",
    "docs/app-icons/prompts/ip-b2.txt": "62127fa6c88c0a8ce7e4bb7c10ead6b354b81e1db33a6ef4228160859b3a0555",
    "docs/app-icons/prompts/ip-c1.txt": "020ea558686d1be216adb6edd03abacf71537fe95a36ec7297694c5f9a00ba6e",
    "docs/app-icons/prompts/ip-c2.txt": "e5abb62f5d389ab7122b6f8131ac32de4abf912a54c1d96bcde317e6522211f4",
    "docs/app-icons/prompts/monogram.txt": "cb035dcd19846797b1026524540ba8939fe1d17dad10c9e9767f5e2e8ef42b83",
    "docs/app-icons/prompts/pictogram.txt": "4837c47f11e2af44c80169370b98ef3b00badbf18d81c0319e55677522a3a76f",
    "docs/app-icons/prompts/pixel-art.txt": "d63cb8b72f9124c68d1b29348e9a5de74ade002e602a70828ee93f56aff4eaad",
    "docs/app-icons/prompts/soft-3d.txt": "3f102eb124652015979d134a04a8e33d16b76eaa2a1062564486ce14e1b5c98c",
    "docs/app-icons/samples/abstract.ko.md": "da522fb07d3be21528c880e85c9e371f4f0bdada115f6c3c806fe10106914ccf",
    "docs/app-icons/samples/abstract.md": "fe485ab06d4b634680ecfcb07ae7bd217e63b8030ac9b9865c2c6d6faeba1491",
    "docs/app-icons/samples/ip-a1.ko.md": "ce75bcfe7aa7978cb438451e2cc605e28b1f72192947c1be2d66b1826f8386dd",
    "docs/app-icons/samples/ip-a1.md": "b9d35f6af0741973431ec69ffe574f977961d15fda1720b70c65c077dd41a60e",
    "docs/app-icons/samples/ip-a2.ko.md": "bd06a8a466a68b84db273f72e5f6c948aa605f76ccc055ea39d9196527be87ab",
    "docs/app-icons/samples/ip-a2.md": "709a643fdc68fd883d36bd7b3d50661de52dc2971b7ea5bfdf8aea401598f06b",
    "docs/app-icons/samples/ip-b1.ko.md": "a21b753ed877e9087e9443231bc1051b891df1eb178dfe6388852a2384ef2f01",
    "docs/app-icons/samples/ip-b1.md": "ac8413878c7e3387501be3a2bd000b3a2297862d9da68c84c11f9ac06436a7a1",
    "docs/app-icons/samples/ip-b2.ko.md": "0c33faa792d1ed31489999c05df16927fb0b9006f518a63696af9ea8e28902fc",
    "docs/app-icons/samples/ip-b2.md": "d821417b4fdf2ef05b82687255c1c69528f2b62d02768bd945c834017700f74f",
    "docs/app-icons/samples/ip-c1.ko.md": "458b4f58df9e91c866ab34e51b4d971cea0590f5974bb0b972c9eb5d2df1cdc3",
    "docs/app-icons/samples/ip-c1.md": "2744f862751da80f37e753d145492b8601091400a5595389becf1bb9ccc12f58",
    "docs/app-icons/samples/ip-c2.ko.md": "e5434756c9d1d147439752c70cedc5ae2a51c6e35393f1898124a45a4788f0a3",
    "docs/app-icons/samples/ip-c2.md": "604e5d24c70ea6d554ee88dd5af3381af4975d6b3139044b4873c085d068a816",
    "docs/app-icons/samples/monogram.ko.md": "dcd06e3f0990625914daa690e1d95de559be2bd4d87e2c4f575ad919a9ba55f5",
    "docs/app-icons/samples/monogram.md": "417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580",
    "docs/app-icons/samples/pictogram.ko.md": "bc260c48649afaaf1891161076f51037017dbd4142b7a1dc002920d88505f9d8",
    "docs/app-icons/samples/pictogram.md": "cb04a2a98211b827d1c06234d9f9e31769f484f8329d44e2ed182f524b3517d4",
    "docs/app-icons/samples/pixel-art.ko.md": "d0388047ddd216367509be39f032a325609208772c49bde29c6466435307cfc5",
    "docs/app-icons/samples/pixel-art.md": "a34a71b7e0cd563844805d8b0c29df50e3d23dcfe690464d747f1164437da79d",
    "docs/app-icons/samples/soft-3d.ko.md": "a358570625ed696089b75020595d1c92cd84b4603b33cab5ee059759c07f5cfa",
    "docs/app-icons/samples/soft-3d.md": "37428e43c8b35702bb1233d5aac5fd2acaeb7f4d8b81b1a736f8afcee0dcbdbd",
    "docs/samples/README.ko.md": "cac86de6acbf380becda90a04f9cb4d25681cc37cecf7160cda721b2b853465e",
    "docs/samples/README.md": "7b870dab04532214b6dcaf8f42cdb3d73ff42225bb0169cc9dcd9e88bbd50d46",
    "docs/samples/catalog.json": "6cd286ea659c998a1563b6f4a0b56b078234dfe946054c9ccea3252b2df5f55d",
    "docs/samples/data.js": "6312b89775426b4039baac26ed6b3454532a5c38f3375c920e943a1dab30fe76",
    "docs/samples/gallery.css": "8a05900f4295d6fa1602a5edf690373150555d9b118935c9a363426b604288aa",
    "docs/samples/gallery.js": "812e7a2f78b6d786b0b9af66e32a3185e057a6d291361f37e80a0424f044ab24",
    "docs/samples/generation.json": "4868f3fc5839bf28a3f19df4328eeb1b2dab89914ea0aee166dbf2c07dee3a74",
    "docs/samples/index.html": "6195d260a64c0a2c14ca6a86caf3d89ad0c41cc90c93e4718818dea73b6c2e70",
    "docs/samples/items/01-luma/README.ko.md": "627b73ed254087c6ea50efa53847a7336d521e403e01cebdf97ba8ed468e560c",
    "docs/samples/items/01-luma/README.md": "d82b193f867d7c96ded349b3feb5626890e5e0fd0cddfa2be94c96fd820fc652",
    "docs/samples/items/01-luma/brief.json": "bfc221cb27908da79323f28eb48191f17f4d7e76a2b8b854b3976d0f505a3136",
    "docs/samples/items/01-luma/delivery/brand-guide.md": "0c17b2af701728d8181156538df5520f0d773368fd83f8457a2774c24af0fc11",
    "docs/samples/items/01-luma/delivery/logo-package.zip": "737551e69c8a5da9682b2114f3019e4f61f7f78def0e58d00ff83398d5a94b71",
    "docs/samples/items/01-luma/delivery/logo.png": "29c891de028f14cc8b8a715f105b2dd8b383fa647f691521bd0de25428f561ef",
    "docs/samples/items/01-luma/delivery/manifest.json": "cab00ce0951e6b856c2ab1397dcf8f3b800883404684d89ae48a8e901acd2a9d",
    "docs/samples/items/01-luma/export.json": "e3f3fb6361e5ab6d7e26c45903c3dd52bb9d5c056fdf76fd3f8c2b27d9ec65de",
    "docs/samples/items/01-luma/import.json": "7c7cc3bf683eb2f56cad6a329ac6b01a2a064859f590ac4662b17a0bd47719a2",
    "docs/samples/items/01-luma/init.json": "5b2734532cc99f0ac52bd1bf433c129607328555a131636f3f99a2b8c0560d8b",
    "docs/samples/items/01-luma/prompt-response.json": "6854dd49ba6fcf546206cc4b43fa96fcd175b66126a3286f6478b012b7c8d5f3",
    "docs/samples/items/01-luma/prompt.txt": "42e7a37eb050d8b9a51232b66d4f3187b4e44470abe8c35fb4366838c495ec54",
    "docs/samples/items/01-luma/review-response.json": "93eeca215736ff3e9ed03693f89ad233b60f143abd7c71eeac18e2f3c9521a23",
    "docs/samples/items/01-luma/review.json": "2dd5ae1c3ddf1498b973f85d908bd546228d59eae0f0ff9e49ae920f41756fd9",
    "docs/samples/items/01-luma/select.json": "325f8ebb6d28c3c1eeea85263f2dbf16b2358fc2d724e60da3571aacdbf98ffe",
    "docs/samples/items/02-loop-lab/README.ko.md": "c4b3f4fa9196deefe091fe50d8af211f8fa1acc0eac16c92780a199b85fcd2b6",
    "docs/samples/items/02-loop-lab/README.md": "a9f44f4ce1abd872c73fd8024f967ba7ce500b171dd8e8fae218cbc49e5c369c",
    "docs/samples/items/02-loop-lab/brief.json": "a0f1f1d3ede551adff9d891b68d88f0981ff2c09a9b75fba83545a7551bcf119",
    "docs/samples/items/02-loop-lab/delivery/brand-guide.md": "a3ce1670f7461ada41a2c25af5c01e2b1100cf897625b900b88788dd07aa71a9",
    "docs/samples/items/02-loop-lab/delivery/logo-package.zip": "d5018f24dbe40ba47b3ad91c71d7336090bc5168dcba715ab6e5f1c7fdf808bc",
    "docs/samples/items/02-loop-lab/delivery/logo.png": "c03e72b2362ed7071f52f441520a73fa9a92be697efa551ae14b3cb43da8aab4",
    "docs/samples/items/02-loop-lab/delivery/manifest.json": "7c1ea612a9976316154bfeba46dda8f7bc30f55c68d47effe9f8990d6927c672",
    "docs/samples/items/02-loop-lab/export.json": "7b2a2e4f43c0c1174b8ac7c80efbcca35b21a8b61f6dd18239b47180e3ffaefc",
    "docs/samples/items/02-loop-lab/import.json": "90502dcb7a454b02fb07a1b6758f123e0bbdc56dfe084b534b1227b229bcde5f",
    "docs/samples/items/02-loop-lab/init.json": "5e5b5f1a955e35c45a5649d344a4137f9143893d2db1fb4b20a9a0b1e5a1b593",
    "docs/samples/items/02-loop-lab/prompt-response.json": "c78f3f5163e872aff79ec36835a4a80dae932b674d130520bf1ff28c77cb03c9",
    "docs/samples/items/02-loop-lab/prompt.txt": "4ff03315be3301c0f8d800ad1e0184e35cd11abec36cfb17308a209ac90322cf",
    "docs/samples/items/02-loop-lab/review-response.json": "48b9cbe998c53fd10708b08abc7e70799bafd117cd914bf6803d1923cf0db22e",
    "docs/samples/items/02-loop-lab/review.json": "e7dd98c1064334c5741d074cf2b1f0125ba087b5104b781ac83147680242738d",
    "docs/samples/items/02-loop-lab/select.json": "dcde8374b255789519305ddece04eb090ded597525e7e7a742046c112041622a",
    "docs/samples/items/03-goyo/README.ko.md": "bd0601f9342d2e8d03cf359705f795e763935cc7f8b6405402ad70ee973b2806",
    "docs/samples/items/03-goyo/README.md": "eb2fc0833a115c9bc217ece47c9e1d714fabe2eed2fae6ad64c158f4f5fb7fe3",
    "docs/samples/items/03-goyo/brief.json": "28742b89cc5ee66f4b1a5ff8ed7b5477c57989b614330caa7d4069417a7d9543",
    "docs/samples/items/03-goyo/delivery/brand-guide.md": "c5c7d11ef37522399d997fc71c768c971a8db7998e78d7d909ba01f3b88de2ce",
    "docs/samples/items/03-goyo/delivery/logo-package.zip": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
    "docs/samples/items/03-goyo/delivery/logo.png": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
    "docs/samples/items/03-goyo/delivery/manifest.json": "3a80a87104f9cd5c28aca2f892abfb7dda8a3c1fdc87c36519b4cb82fb26f8f2",
    "docs/samples/items/03-goyo/export.json": "f009a669284d6b6914d28cffb7e3799fff306355d93e4b2cb3cd255c6f08ef97",
    "docs/samples/items/03-goyo/import.json": "8224342203e53679501faf7e8e4a251651ad71108f75910ef423f4fbdd5f04e2",
    "docs/samples/items/03-goyo/init.json": "58929251dee4718c48645c8573fc8e391304c1df34cd9b9ace6eba7329f11fbd",
    "docs/samples/items/03-goyo/prompt-response.json": "4187c86f96d94c16b06ef64ee016681c0b89d8af1d27ebe3268a354e72d59990",
    "docs/samples/items/03-goyo/prompt.txt": "8b8dcfc8d3c6d51d7ed18e17cc13cf9b890fabd96fbe28d853e288375a9feefe",
    "docs/samples/items/03-goyo/review-response.json": "7b0d03b4b87e378f39ec8b4b420190574f7af5ea254f32ccb9b637bf717f77bd",
    "docs/samples/items/03-goyo/review.json": "485968ee6daa42ccd92e383f4d4efb73498e272dafc1230a66ea8bac38073aea",
    "docs/samples/items/03-goyo/select.json": "f75ecb44a59e33cdea8c474aa5400e4c3fbad1cf22852e6597cde1ba124aedbf",
    "docs/samples/items/04-bread-bloom/README.ko.md": "c26b30b1a503bc0da02bf3058ca422ce5815d0931ea214dfae66ab329847ff5d",
    "docs/samples/items/04-bread-bloom/README.md": "bc63cadec6179d975f1c243fb4bc77ae8f3bd66636adb82c1fc5fa2980223474",
    "docs/samples/items/04-bread-bloom/brief.json": "f7e9f0bdc3820b1895cd5e1a72b9e4d5515853bf686709fbcc02124144e9699c",
    "docs/samples/items/04-bread-bloom/delivery/brand-guide.md": "45a299a04c17e4d970a60d6f5738cd7bd7a56b9dd9c77266d651d8d7b42124db",
    "docs/samples/items/04-bread-bloom/delivery/logo-package.zip": "45e1804099316f69e00f95908c7846b890db714661fd20ceb2ad4c9889d7e44d",
    "docs/samples/items/04-bread-bloom/delivery/logo.png": "420ac19545143efbc4681b27b68fd074656da803869c746bd9c1eeb5678c9b8c",
    "docs/samples/items/04-bread-bloom/delivery/manifest.json": "5703533eae24d50b619f3d1bbacbebd9a5fc42d4a1fdc9f9759a413efbf22228",
    "docs/samples/items/04-bread-bloom/export.json": "48372dda9b64049c64002359930f7f521373dc636f20e4079a7c4ac3b93139f6",
    "docs/samples/items/04-bread-bloom/import.json": "a381ab9c6215a0f7934d6f496d682eadbc718179f39f104f4f60452437c0f886",
    "docs/samples/items/04-bread-bloom/init.json": "d66a1105120aa019e7179a5e62b9996b099808454ee45b16a055881c235db5d5",
    "docs/samples/items/04-bread-bloom/prompt-response.json": "ebb2e8a4a2b904f3a9548fda60af1eaab04cf4bf1ec5e41f736a0d5d53c5ac40",
    "docs/samples/items/04-bread-bloom/prompt.txt": "d0b751283e8e01baef338a8ed8e1617f556d3f577c7a385e4622d7c5fab025f0",
    "docs/samples/items/04-bread-bloom/review-response.json": "7e01df6f958e7eb21183e9bd2e7d1a1960af85e883634aa496cf369df0c02cd7",
    "docs/samples/items/04-bread-bloom/review.json": "b14f58869c80b420869bd3758b6e03d0f3e8f34b5c45fb1f2c850c599e779515",
    "docs/samples/items/04-bread-bloom/select.json": "2deb7608d495cfee464797bd027c1721ffcb026a3fcb8d56eed220bf9544080c",
    "docs/samples/items/05-kite/README.ko.md": "6be1e882d574dfc5e81a41a316272569605b59f5e74de63fcf3de35ec2776303",
    "docs/samples/items/05-kite/README.md": "f932969f8f8dfc999eddef727bb37b21d4990545a062f340d33014440e413369",
    "docs/samples/items/05-kite/brief.json": "901dc890643041dfaae6e74de06c34ab67e9aa512b430a0888fe9691573c4dbf",
    "docs/samples/items/05-kite/delivery/brand-guide.md": "0fc4110c24574ce8a99ec60da291ed3fb03c68e648ce461e8c4245ff3ac67d06",
    "docs/samples/items/05-kite/delivery/logo-package.zip": "146b54b76b88e127ae4613dbb03722e579845bc2b00577913433ce2e9bb75a1c",
    "docs/samples/items/05-kite/delivery/logo.png": "dffb886a7a72196a42df21e36afe23cfb6e07bd25bad35c69c44f4de5c0232a7",
    "docs/samples/items/05-kite/delivery/manifest.json": "31569fc1c084b69a3bcc8867395af8e156a58816b9c159beaad6a9e33b452fcf",
    "docs/samples/items/05-kite/export.json": "cf5acd251728f04eff7cd1b211cfcd73f4d489c058f73d6f0025f4b827b4ac83",
    "docs/samples/items/05-kite/import.json": "6ce674a0cd12808ef5ef81986ecf9a26e084e400b602d6c683ccda849b75794e",
    "docs/samples/items/05-kite/init.json": "8e41faf41c4aa0e7eb42e440a619d2f0a20c6d08b36ecf4cd69e99ebffa743cd",
    "docs/samples/items/05-kite/prompt-response.json": "8550068f053bb70be94e51f047784d1289053154e80bbd1f6307c4b92e9679df",
    "docs/samples/items/05-kite/prompt.txt": "a79432dfeb4931e2d4c95c3fb5ce2241709519571633fd794b58f6ffa724ecf7",
    "docs/samples/items/05-kite/review-response.json": "e511a88e0d810f3bff87d056bcf6efab682b5c93ffbe2e85bf9bd0cd8c37ae15",
    "docs/samples/items/05-kite/review.json": "fa4899f794f2ffaccc38300afe5726b5456eda79024027173c1fe0389bde23df",
    "docs/samples/items/05-kite/select.json": "a5c9e64b6d5ada2cf9077a0955c43b99194a39bbc172ce422c47fb3e66561a09",
    "docs/samples/items/06-miso/README.ko.md": "3ecf98ddc9d86a932aed55dd1ab87943c168b6f30ff2458dab9d93f84ed60551",
    "docs/samples/items/06-miso/README.md": "2715a59521970b25d8f76bd4c83e12536660b36a57c5d54441590285c60e4028",
    "docs/samples/items/06-miso/brief.json": "5bbee46b313006e949f7c51642b8b6b90b062ec561af2a1221b4c3b12a8d30e6",
    "docs/samples/items/06-miso/delivery/brand-guide.md": "5bb3028039e259502187bc2dec43dd156aaee675bdc2b83ef034cd968011c640",
    "docs/samples/items/06-miso/delivery/logo-package.zip": "e263545af230e5db2da6e79017f3058b4336a5b7693c600bf749c18f6176eeba",
    "docs/samples/items/06-miso/delivery/logo.png": "10f3e1d9f51e35a1eced51e0efcd08061d03bbc8a184d4399992237e45ec0649",
    "docs/samples/items/06-miso/delivery/manifest.json": "017544e508286c64481b9d90493c669f309f0809aec02092d4d20373fc48de88",
    "docs/samples/items/06-miso/export.json": "38133df4745a37a55a6df8572146b24729b9844f9b5bf2d2d6e59f2e3d8af50e",
    "docs/samples/items/06-miso/import.json": "b7350c61fbbf20d69942f33f5e76aacd41535bec190b0940dd26a724ecdb31b7",
    "docs/samples/items/06-miso/init.json": "4830e443d052e1faa8ab4cf39b063524c3452dbc10ae95dd6563197791c5f421",
    "docs/samples/items/06-miso/prompt-response.json": "070b64e1a91ab561d05a8e8ccbeed7197df74c037cb2449476fd910e3b0709e9",
    "docs/samples/items/06-miso/prompt.txt": "5ff42b47c41dab0af06411b9d1fcd5e008e571ba5423004ae4fbe16dde6e144a",
    "docs/samples/items/06-miso/review-response.json": "47b657f45d2bb59d836d68a5c6a1b878dceb1db4a75d463f5310049bd48120c3",
    "docs/samples/items/06-miso/review.json": "d6ecc93bb4a1c708f91aa2a2bdfc78cc51c791eb2ee8cc6b981a4173ceb0b525",
    "docs/samples/items/06-miso/select.json": "b853cd53d923406a3f88471dbe5c1bef4a1a98646defd5e48a7203ac7772d02d",
    "docs/samples/items/07-northline/README.ko.md": "29c861afb72538d32dd65d2f245a3f87bfbde58cfe561146c370f4cbb3a1519b",
    "docs/samples/items/07-northline/README.md": "945caf4c15760f01ccdec60e01d0a564fe36d37937096fabb9e51a51a2ce988e",
    "docs/samples/items/07-northline/brief.json": "87b0024364f1a56364219627c9d89e86bdaaf3a8c4cc0e5fe8095caa08dc72fa",
    "docs/samples/items/07-northline/delivery/brand-guide.md": "8b22fa7003e480d1205f474f479b6b1acf14dc2902d5886aa6cd46e45d74c59a",
    "docs/samples/items/07-northline/delivery/logo-package.zip": "1d2a5555cb0922268acf8a99b6b060a9678d5ad64b93e84d4a4532c0b0dc620a",
    "docs/samples/items/07-northline/delivery/logo.png": "4eb27ce806aab3a32f58337c8b1fd00f6257f1abe970f98f12edfac6be423c06",
    "docs/samples/items/07-northline/delivery/manifest.json": "9c70b3e2c9464ddab72821f76908a7bef7d9fe6e7bf3b7b186ee65f6aaf70a4d",
    "docs/samples/items/07-northline/export.json": "b36decc4c94917dcf88cc4f60ba017e70cc9bd852fb5a5544f9854e30c0e545e",
    "docs/samples/items/07-northline/import.json": "53b17978e2b3967bd7f6d126c58ebd19159f8516184d4b12e9e792671d8efdae",
    "docs/samples/items/07-northline/init.json": "6965eae56b79adedfae70157f9c16d7a21cb0c2ea3091bae4e2bc72d2283d2ab",
    "docs/samples/items/07-northline/prompt-response.json": "ddcbce4b3a783cde4d833d1d67fdabdad5110b675c1e0313f398545428ff9172",
    "docs/samples/items/07-northline/prompt.txt": "c6d059d8cb95faed5246bef05fe921ac212075d5f9ffcce12e79d1596b3d8ead",
    "docs/samples/items/07-northline/review-response.json": "9923a3a8e23bab405f5256521264ef016f45916a0515b2a72d5ec958c07d70a9",
    "docs/samples/items/07-northline/review.json": "48ebf8d8fc0a49235e93deb8682c8009585d6dfb777a4fbc246a992ecba8114f",
    "docs/samples/items/07-northline/select.json": "3ed49da83a98131e8f5a77528e773399fa1833f19b69d06c595595316e2e4e95",
    "docs/samples/items/08-mulgyeol/README.ko.md": "cd715142bee98c9b283a1c3ff8dd8e66843ed28ce9872096624237e136c55691",
    "docs/samples/items/08-mulgyeol/README.md": "2036c04ea4f900d021468859ed03b50a688e530deb2b58a29b96a432b2dc1675",
    "docs/samples/items/08-mulgyeol/brief.json": "dda2b2802c795e8b45986d3d85d13ec88a8e647b5a1bdb6a8207c9e23de21bd1",
    "docs/samples/items/08-mulgyeol/delivery/brand-guide.md": "ed352474099206976d522c9912b5b5808a1edc7f5694cfd976668a681f70d2b3",
    "docs/samples/items/08-mulgyeol/delivery/logo-package.zip": "da783385149d57ef84d3678b51d7f975bba4fa2f8e4370fb7021d79b9250485d",
    "docs/samples/items/08-mulgyeol/delivery/logo.png": "da97616502733dcef4b6b082d7746149793a22a576f3ad179a4da641d7ed66cf",
    "docs/samples/items/08-mulgyeol/delivery/manifest.json": "c723f500cacadfdf2bffbea6eb01847fcd308108c503497fa1eb218295762089",
    "docs/samples/items/08-mulgyeol/export.json": "567c13ecf2aff41395cb60628e5c8f5a9bed0fd965579bad5cc6950af593c5c3",
    "docs/samples/items/08-mulgyeol/import.json": "63d2212ea4338c9984a8ca0f7844b3da6e85bc5ea8b1702dd466a46bd4fbc33a",
    "docs/samples/items/08-mulgyeol/init.json": "321246e299de00657930b6d8de659caa724f70a44b283ba73630c5f6fd20975c",
    "docs/samples/items/08-mulgyeol/prompt-response.json": "b728ecd31f81302024829ef8283cb6fae85159cd0591478951248a5c4265e89c",
    "docs/samples/items/08-mulgyeol/prompt.txt": "abfc5d06669b358f7d24ca2d03beaf1b37fad1bfbec3079554bf235007c00c7e",
    "docs/samples/items/08-mulgyeol/review-response.json": "129539e7b0e38405cfdbebaf0424c78c9661fa7f2a82796d2178761ee7d9eebe",
    "docs/samples/items/08-mulgyeol/review.json": "4deb57b145c47b3392bc90611dccd21212d05bc31490bcf2653a0e9ee3e08dd4",
    "docs/samples/items/08-mulgyeol/select.json": "5d29053c17f926c18d05c91229f0140057e834155b27cd4a85ebc01c498c05c5",
    "docs/samples/items/09-fern/README.ko.md": "2bce7318a0f04fb093693a8bf3e48283f20055e954068974c0b45315d3394847",
    "docs/samples/items/09-fern/README.md": "d4f708d90c5c6ed979e8bdd7cac50d84ec63ba7110b7d88c81d15922137618cf",
    "docs/samples/items/09-fern/brief.json": "a26c1f1f36001df6607aa7877af4babcfbc568ac90a4784388e4afd4d4de8387",
    "docs/samples/items/09-fern/delivery/brand-guide.md": "96684e2feb162efbc861c5ecaedd06a18ebdeade3aa5b996e36db3a031f7ee5a",
    "docs/samples/items/09-fern/delivery/logo-package.zip": "22251e63f3cab0143931e9c5c63641c61b1ddb6f65b9dd44bfdd8970f61b21b3",
    "docs/samples/items/09-fern/delivery/logo.png": "db9066ee56c2789324aa7c53e5ba68b9e6c003ba3fe98578ea8b0e6196181e27",
    "docs/samples/items/09-fern/delivery/manifest.json": "3bad9944a59f736691647ee2f073376fc6d1b32cfd556e7b9d55228ba7423c06",
    "docs/samples/items/09-fern/export.json": "13c2608d559f48d332c16ff87c4e5bb9091c29b79d4f1bca01db31ff26702a5f",
    "docs/samples/items/09-fern/import.json": "5d8f671f9a973666f4bd44f4a883ad4022e39f5990e4c8ff247e45069f0fa21b",
    "docs/samples/items/09-fern/init.json": "a1156d43abfebab5ec378384758d9b863fc96c5fca4a4b20a9ac27ebe0e565e6",
    "docs/samples/items/09-fern/prompt-response.json": "b900586cc2e70307d11d1b51d5e6cf892010e2e4dc69a7a19ce0ca507d857668",
    "docs/samples/items/09-fern/prompt.txt": "7e6012a8106d624db3d0271cdc621bfb2630bbb2926c30ef28601c3355e8a200",
    "docs/samples/items/09-fern/review-response.json": "d9f5ced3d2f0e60e43d434622071a981ec24c68f305a08908d90e01d2bb2d6e2",
    "docs/samples/items/09-fern/review.json": "416b0b2679e5ccdd07b66fb9b2c71cc443415bb1ce53b46bf753303e052549c7",
    "docs/samples/items/09-fern/select.json": "457e10d003b56073f8a8d3637f9139e214c2bdbaf3a077d84edb87344d459ff7",
    "docs/samples/items/10-nova-notes/README.ko.md": "dbaa306cea17a860e83ee2e5fed2c48a065f0270a08e3e2829f991545612e13d",
    "docs/samples/items/10-nova-notes/README.md": "556499f96bd1c40c056c4f11968b63c5df74b155101c6adb029dbc4bebd9eeb9",
    "docs/samples/items/10-nova-notes/brief.json": "2b05add8c82e5cf2e2e3dc3104914a17d5f3b31dd38a880e5f7b19e635ebe258",
    "docs/samples/items/10-nova-notes/delivery/brand-guide.md": "55e0a9308d077919151784f08c6859ec0cfdedb230e6d2ea5bd94f8168c1eba5",
    "docs/samples/items/10-nova-notes/delivery/logo-package.zip": "39c1363deb0a2bcb6070e6b07ab1309824a5eb958f81981dda9fe7f088e6bfe7",
    "docs/samples/items/10-nova-notes/delivery/logo.png": "0e26b2354a22faba2128d205c377abe09e590c82f895e2716fe51e0877715553",
    "docs/samples/items/10-nova-notes/delivery/manifest.json": "7476a85865e158a2f1c76775e365f53e84268228f9cc3fcec01d1e8f40dabba2",
    "docs/samples/items/10-nova-notes/export.json": "0d1085e34d31e09e3b49245880fc615ac9c1d98bb853e3e9e7bc0b486c71819b",
    "docs/samples/items/10-nova-notes/import.json": "05d91d3112119a1e3a2dc0b8305b6253ac5ef57d186b8a2074ceef166aecc56d",
    "docs/samples/items/10-nova-notes/init.json": "f7166d475c25ec1f38db8dbdaf9b74e4f25941b82e6b48d0a075a9616ba34596",
    "docs/samples/items/10-nova-notes/prompt-response.json": "f11db98370297420d13f525db1749d27ce598742045dff585b91c7c0392ad79e",
    "docs/samples/items/10-nova-notes/prompt.txt": "6d64eb9c274a8da147890b7620f29c87d41c9f5881854e642a47b9b0cb100609",
    "docs/samples/items/10-nova-notes/review-response.json": "a6b2d5cfee0a41c150123fbad9631e59a8db51654ece2647f0c755488f14af7b",
    "docs/samples/items/10-nova-notes/review.json": "176dbf2a192d6e5d8eade34353365d7f9fb8c951bf760f8f0949cf788a505892",
    "docs/samples/items/10-nova-notes/select.json": "cfecad7c34d81c01d3099926ce8334dbfce5d89f1287e209cde5e67ac6f1ef40",
    "docs/samples/transparency.ko.md": "18edf911484492db34d4264bffd0ea0347e8fbdfd35cb726230d514484fb4d79",
    "docs/samples/transparency.md": "e26e0613e4ce1a107327b26f5894991dfb1daa47d967aab051f35158b11c2958",
    "docs/colors/README.ko.md": "70d7c6f517a0624088db05fc1a06d32d012db54619437a826a8f9d4dcb7ff605",
    "docs/colors/README.md": "a95d20935575c1aea5d1036cd614338a1fc50bf07a8c17a340a07794b7b524a5",
    "docs/colors/assets/01-sunroom.png": "e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb",
    "docs/colors/assets/02-northline.png": "3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534",
    "docs/colors/assets/03-grove.png": "768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06",
    "docs/colors/assets/04-grove-warm.png": "db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7",
    "docs/colors/assets/05-bamgyeol.png": "083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941",
    "docs/colors/assets/06-tide.png": "2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d",
    "docs/colors/assets/07-fieldnote.png": "049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870",
    "docs/colors/assets/08-bamgyeol-white.png": "0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd",
    "docs/colors/deliveries/grove/brand-guide.md": "8346e72d6e0394fe08b7d299a61d57332d2a468f25624d9a5c4e5af7a797d5c5",
    "docs/colors/deliveries/grove/logo-package.zip": "61fed8500b5b562fa28e34a65d79bfd585c59132adc298a7af5a0e8413784d12",
    "docs/colors/deliveries/grove/logo.png": "768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06",
    "docs/colors/deliveries/grove/manifest.json": "7b9e94c1ccc29ab27a4499f1ffbdcefe33f1181892b08ca228eab8477a26628c",
    "docs/colors/deliveries/northline/brand-guide.md": "cf0f466fc251c941e3002d91036b7a300677b9db16a130f34356af254c0f649b",
    "docs/colors/deliveries/northline/logo-package.zip": "aae2b39736136b671db4114d88e65f10c44997151fae37a197c390e62c41a472",
    "docs/colors/deliveries/northline/logo.png": "3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534",
    "docs/colors/deliveries/northline/manifest.json": "3ab7713a789411dcb78b67f6b3b76fa2df7ffe870dec3d9917b0dc7076b06695",
    "docs/colors/deliveries/tide/brand-guide.md": "7f80155f0ec68e027ead683d15f273497b8e0c74e46ab0e7930fcc2c482301ea",
    "docs/colors/deliveries/tide/logo-package.zip": "b76d0cda7f231e10948cf48a261827d2622bb1b52253e4cd032a34b75ed23a61",
    "docs/colors/deliveries/tide/logo.png": "2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d",
    "docs/colors/deliveries/tide/manifest.json": "7465b62610871bd41b065c2bd8150ddecfe143b07ec9d16fcf5bc9ab2d0693bb",
    "docs/colors/index.html": "5a0118f37c31c6d30837f2e68bcb931d82f24873a8a547709f4edb6e7f3749f8",
    "docs/colors/manifest.json": "e13b772bd2fa4b810777bab3cec7ba145d4d227f1b47843b1d3ae7bce6d6dfea",
    "docs/colors/projects/bamgyeol/README.ko.md": "0d187ffe07a901fcfc7f2d04ec486f28f0288b21a5121de5bfa80742781d06a2",
    "docs/colors/projects/bamgyeol/README.md": "6f1dd820926c3b930c1435934722bf8d28ed7901113673031d81afc2fa849017",
    "docs/colors/projects/bamgyeol/images/a-v1.png": "083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941",
    "docs/colors/projects/bamgyeol/images/a-v2.png": "27e010082310501ac2ca6060aa8835ff3e75cd727bb971fb76f08b153884815b",
    "docs/colors/projects/bamgyeol/images/a-v3.png": "0df1d666d480aae721f6ccab6fa7ff9d2388b015946e8e051381c86e9766c6f3",
    "docs/colors/projects/bamgyeol/index.html": "314fe40653b2b7dfce0c43a0029fda6611a324bbfa9ca38d6ae4294484c63d6f",
    "docs/colors/projects/bamgyeol/prompts/a-v1.txt": "3950599ae9b733fe0111291a1a0de6cf4d95f1b30a83dff75407673172d570c9",
    "docs/colors/projects/bamgyeol/prompts/a-v2.txt": "d27ffe104061d0322cbeb644c8609af05c9dc6c211eed2c4082fc99efe10f5f8",
    "docs/colors/projects/bamgyeol/prompts/a-v3.txt": "fc168fe3993b19ca0ad02f9d51ef74d646fcde1bd0472636d8b5be313cec1363",
    "docs/colors/projects/bamgyeol/reports/report-0da294e689214a569d637c32a14c1026.json": "cbf2a0160af65977d1d2c6349527ab02834b4397922e75b0288b0b5c9ee7d15a",
    "docs/colors/projects/bamgyeol/reports/report-81d1d2403f124e45b5894589ce129d7a.json": "59d3e2cb7dcd1ecc1c0fed63b393e895b233d05245d1827bea581c208b65495d",
    "docs/colors/projects/bamgyeol/reports/report-82dcdf50196a4d55ac78ff0b522326d0.json": "476a4ccaa84f364753c98bb190034f23b0024a9896c72e3c5bf75be0fc290c19",
    "docs/colors/projects/bamgyeol/reports.html": "145ec5b6add0ca7f5b6fdd0ba7dfcaf77fe2f31761c7a50929af3ca228139a58",
    "docs/colors/projects/bamgyeol/session.json": "74c6ae2611906caac2f5b1b90b71978450bebc529abae693f54e56158754e204",
    "docs/colors/projects/fieldnote/README.ko.md": "297df6b986424eb2a35dd995ac2adfaea6c448a2f96f97e4ec7a8f2c20307a3e",
    "docs/colors/projects/fieldnote/README.md": "743ac8bc2594d996823043d355af5c4a136d2577ee599dbe888685c5c9678ccc",
    "docs/colors/projects/fieldnote/images/a-v1.png": "049de07077bb2d4ff222fb4a0d74b17f526e571292b64de804ea990933ee2870",
    "docs/colors/projects/fieldnote/images/a-v2.png": "7dacc55d6f90f10f7206729f3f0d7cffc75b36ff6191e7430d8e01e2b76c40cb",
    "docs/colors/projects/fieldnote/images/a-v3.png": "05398268ac42aa8d0da04976a9c6367df1bb186e1b3fe46e927db3e494ee65e2",
    "docs/colors/projects/fieldnote/index.html": "5df45b7a017f114261ab893711adc479989e40e956290dd62d087d5f5686255a",
    "docs/colors/projects/fieldnote/prompts/a-v1.txt": "0476d6b1666e0a408299f508e7a26965fb85308637e79fd83cae9b2416e3ef85",
    "docs/colors/projects/fieldnote/prompts/a-v2.txt": "42b5af799eac55dfae849e71c1b2f25679699892003a9036b6fadeeeb1c8529e",
    "docs/colors/projects/fieldnote/prompts/a-v3.txt": "cdd10ac6b9ec0cf5f5d4c7ccca28583b1f5c16e31af55a90f66dc95e4c06c0cd",
    "docs/colors/projects/fieldnote/references/grove-colors.png": "768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06",
    "docs/colors/projects/fieldnote/reports/report-5aaf0c21d2244f3f8aa3e402f916ed39.json": "a00694207891b48291e23f821bd54029932538a22c0f7c4018042a6cfa963f55",
    "docs/colors/projects/fieldnote/reports/report-ae8056de0d3e44b0a222bdb23fbcc579.json": "668fe2e8535312162951e3ed5640b6d55081fbf5a0eb81e90387bf2a6be7edb1",
    "docs/colors/projects/fieldnote/reports/report-bfb5fbc88c274283876c782e82632a4b.json": "e9e6caaf863980c3daa08f0f429191d70ac47bc0de601f5362c5f9d89954e1f3",
    "docs/colors/projects/fieldnote/reports.html": "a85ad18990324a98b26a9b2d46e2748737a832483338d35383d1fab192205d39",
    "docs/colors/projects/fieldnote/session.json": "5c6b0002c63b1919f23eafe2a0d284f6855336778a076e2eb152e50a8f776eaf",
    "docs/colors/projects/grove/README.ko.md": "50a14bd60cfb125d569455ac256562970c53b85537aea1ec003004a8743853a2",
    "docs/colors/projects/grove/README.md": "6cca6c9e88b51e5df5b0873ecb86e2661664265f06be6a1b826af3799c7fb7d9",
    "docs/colors/projects/grove/images/a-v1.png": "768971adfda7f0b41bb36e81c816bf5b3da275f4e54514038dc0ce01b25c6f06",
    "docs/colors/projects/grove/images/a-v2.png": "c60c605176b39f2b26f5299a2c99906dc5cc3e93e4716691e1e2b3154af33809",
    "docs/colors/projects/grove/images/a-v3.png": "e0e0ba746f10f1ab0df53b6a2bda9c6d1f27d621efef68c4142d080407d0bc74",
    "docs/colors/projects/grove/images/a-v4.png": "db4bf9aabea3c44066028d0a1b5fbee0790d3b22181156f64d8ce777169d27f7",
    "docs/colors/projects/grove/index.html": "0d060eaf03bbc641704601bb4d626087f5c77c27a6b65ac232459998ba441dbc",
    "docs/colors/projects/grove/prompts/a-v1.txt": "16ce1b74bfe18c4b1564376355765be80329fc733fefeaa39d3337be2004c722",
    "docs/colors/projects/grove/prompts/a-v2.txt": "1b3f53e4ccd609f1eee40d3ee9a5485b8b90bac8c6516ec5ceac4e81b35b4564",
    "docs/colors/projects/grove/prompts/a-v3.txt": "b8e33e4d395ff32c015a05392f3d733f6a7b07bf520949b988fce05d7126476d",
    "docs/colors/projects/grove/prompts/a-v4.txt": "4df5087d869710d451b4662764fcbd3f73db92131d861ccc215df40c3a30ef96",
    "docs/colors/projects/grove/reports/export-a8e90d0c7eb74bcfb8bbd6fcbd570a4b.json": "ebb0918c86070fc5d0d2ca3bd0c436e44a7cc8dfb7b9efe50390e82567620f57",
    "docs/colors/projects/grove/reports/report-83b2e7e69e1d441595feae69b9b970ad.json": "43ec6582ef5e10e8a5c68065bc36816a5927530fca599f4cfd1ad25623a56cd2",
    "docs/colors/projects/grove/reports/report-8ad54d5b46074ef999c7083e550f6b12.json": "7855bed8c3145b7d2b05829b4b9e43967a28323cad3e9d526fcdc31c8137edbd",
    "docs/colors/projects/grove/reports/report-9b0d511b5f634a83979e706ceb3330d1.json": "2fb9ca6fbb57648971fe0b68d68264f48fb0847e5713301dea9ab1a9e7e22815",
    "docs/colors/projects/grove/reports/report-d0483f48d4d24defa8b77f2acf4a46f9.json": "8d4030cd86d6ccb1556b8042cb4f4822b0f1b2e41e98e2538239d809e17bb181",
    "docs/colors/projects/grove/reports.html": "881f9ebeac0ff24f0c734302cfe63c48dd5e4be31e740cc91341a02a5b8421af",
    "docs/colors/projects/grove/session.json": "21f14affaaeaa5fe671f5bfb1b8030374e2ff7b03892fbc7f2c77b45a9f12107",
    "docs/colors/projects/northline/README.ko.md": "8d94d65ab14030c920b4230013254eb5eb4e1f38bf3f0ce42d78339c4ae66fbf",
    "docs/colors/projects/northline/README.md": "ce19be932a50d73a66dc7b4da8773fea4e0ab37afa08451feffa914b37f834ed",
    "docs/colors/projects/northline/images/a-v1.png": "3980a1ab42957e6fde56e94ba00419606af5ccb96cfb16f4783b147ef829d534",
    "docs/colors/projects/northline/index.html": "6f3f30f48540e1e852a1916cb97d9f85180f4325d1861f512f567d966ab6bf21",
    "docs/colors/projects/northline/prompts/a-v1.txt": "73c985fe0e290bf98cd758676a570283d0bf5695c99827d1a28f757c4ce00119",
    "docs/colors/projects/northline/reports/export-ebcbc02f93344a18ba4568016d68980e.json": "487d044505a949578bab79ecc8500951ff44ecd7ba1962e694fa374df6f50f16",
    "docs/colors/projects/northline/reports/report-a45574ad29184f6bab909f5fb77336fe.json": "132bc58664a084311017bda331f7971febab378f9c535aa8562359a712004d87",
    "docs/colors/projects/northline/reports.html": "2f37c3bc29338e172023ac70f2e49e5fc06a1c2c656754f1750d26f09579366e",
    "docs/colors/projects/northline/session.json": "f9d6a877729fe009ae0d8d61636b9de7f9ff1ef3c68371b356999e6ed99edcc4",
    "docs/colors/projects/sunroom/README.ko.md": "3f8ed9e7f6aece5ef9a033221e49c3eb8220a82674c01f684436906c4aa3a892",
    "docs/colors/projects/sunroom/README.md": "83f21473405c653580bfd5295a35475e926a41d4927a34a617a4482a99bd36ee",
    "docs/colors/projects/sunroom/images/a-v1.png": "e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb",
    "docs/colors/projects/sunroom/index.html": "5ffcb381fd8765188069138a121c6a98115d8225f6d11d786f596136f05a1fb4",
    "docs/colors/projects/sunroom/prompts/a-v1.txt": "a2b435a2be56f59df8f60305a44e6e1068cedef8346305d3499523ad7253dd60",
    "docs/colors/projects/sunroom/reports/report-4f44a0b5c1b044659f014370325adac7.json": "6e1a9c52bf505d645eac36559dda73909b4921ab70471cfdd832b25f4a22e314",
    "docs/colors/projects/sunroom/reports.html": "b3a0887359cc6916940dff000eacfee9633870dd129183478c3d2dc571cb99ff",
    "docs/colors/projects/sunroom/session.json": "c701d822d727dffa0c1fcc4fb6d49b1b3195fecceb699d85c8755ff33623a104",
    "docs/colors/projects/tide/README.ko.md": "54191680aaa6558b54488b010b2aba95836551dd7aa387f4e3fde6bcc02f07c0",
    "docs/colors/projects/tide/README.md": "1cfdfe3f1a4455b71ba960eea428f997a9c3727168b1946dbd0a671fd2b80533",
    "docs/colors/projects/tide/images/a-v1.png": "2edc489ad78de497503d91842c83350f6321570d0036b5513e8fb19dd59e5a4d",
    "docs/colors/projects/tide/index.html": "bc1e9efbcd6e9673775871d438eef41843f5f34b837956968cff22f185c0ee4f",
    "docs/colors/projects/tide/prompts/a-v1.txt": "0228783b3948e6db29bf7f443a7e41998b86df46f801489635433eb7781b520f",
    "docs/colors/projects/tide/references/sunroom-colors.png": "e0aeded204e9e6833dbfe027c0589b7f8905f7de8fc7e5c6e11422ab54b8e0bb",
    "docs/colors/projects/tide/reports/export-a93930d610d74e948324475c62b57ae1.json": "e0a35d9eab54e30fcbfdd33d279787dd09036488a8ed2e9a9114f5dfe62e654b",
    "docs/colors/projects/tide/reports/report-fd7670cbe1c547a593d960a3c93715e6.json": "130e87eb165acd22f075dad0b9cfd1400c0d7625b209d7fd6a628b60a9982692",
    "docs/colors/projects/tide/reports.html": "4f450b77c1b294aa7724cb70513818c0e123e4bfd5f445e2d7a0fee5c3227ac0",
    "docs/colors/projects/tide/session.json": "4c03b9c94d5de5722d80d7ae5388bf1371ac45a09f4e11f0535d32fb12ffba94",
    "docs/colors/projects/white-bamgyeol/README.ko.md": "4946f58769e0bb3ccf708eaf05b2bf8f4f93b30c225cbe777ef932eab1b902a8",
    "docs/colors/projects/white-bamgyeol/README.md": "0ceba12bd932d20ee65056bc1c2edc473deffc6d561331827787e62cfd883ff9",
    "docs/colors/projects/white-bamgyeol/images/parent-v1.png": "083e3a4bbaa5fae1593879efe6e6336a7727fea7c0a431a3b9e96607bac87941",
    "docs/colors/projects/white-bamgyeol/images/white-v1.png": "764557003be078c7e83fca85b7b40d43977edefa9ef46caf49f5279c403a3151",
    "docs/colors/projects/white-bamgyeol/images/white-v2.png": "fda77d0af6c53c4d0d28099ca6568cbb7e877ac6045ea9ca6898bf77884a29a5",
    "docs/colors/projects/white-bamgyeol/images/white-v3.png": "0be9b79a68e2bb9c145e4f9171db84807010be6f2478dd19b724a3dc4c0e73bd",
    "docs/colors/projects/white-bamgyeol/index.html": "f2a941d9fc8556e5b07663f4068dc1ba316e1c2678afba81acef04f4ffa4086a",
    "docs/colors/projects/white-bamgyeol/prompts/parent-v1.txt": "3950599ae9b733fe0111291a1a0de6cf4d95f1b30a83dff75407673172d570c9",
    "docs/colors/projects/white-bamgyeol/prompts/white-v1.txt": "52b4c11e7166abbe10380c59db4e44f85ec450c25c10a93c465cbaed396dfb94",
    "docs/colors/projects/white-bamgyeol/prompts/white-v2.txt": "4d3a947680ba451faafc3a59def385e56e6e7f1eaf30ab961882ce6d46009f3b",
    "docs/colors/projects/white-bamgyeol/prompts/white-v3.txt": "ef590fa42488fa88e7f093970338a7acebefab44ee09b9e9afe1c3dd25b0fc3f",
    "docs/colors/projects/white-bamgyeol/reports/report-588011cab723462bacb99a957b4dc678.json": "1bacd7f1aa60f6380074f5b2072f953ec222f905b7edb14c2363ba7ae1539d1d",
    "docs/colors/projects/white-bamgyeol/reports/report-6c1d44e25b714060af0d602866ac2d4c.json": "3e39d7c0936295a06bf05ceab2ca8da6dd4aa53205a75f1d32c80c6f6d05ba36",
    "docs/colors/projects/white-bamgyeol/reports/report-9bc44eedf2dc4aebbc1e6e4396098860.json": "069a7a799eb860e2d80e410254df422b0b9981da5c59f2253d8cf5c96dd7cf57",
    "docs/colors/projects/white-bamgyeol/reports/report-fd183d105dd74c1db560ea63ffffb1bb.json": "332e859ef21d174776149a089ed8b73f0c36da719f3e1a75907e2daab9e52b09",
    "docs/colors/projects/white-bamgyeol/reports.html": "7aa545491cc60911510c207b0ba56b460c6071937fbe2e1f4bb66f42f05a0485",
    "docs/colors/projects/white-bamgyeol/session.json": "7accd7c91aa6f56fa48862adc99982b2801c40a1e26b298a668e1453da62cee6",
    "docs/colors/verification.json": "a0edc2ce3fc0f83bdddbada15d7c4097644f25c562be1849180a1c7ea887b670",
    "docs/brand/2026-identity/adversarial.json": "2818de7f1829400a81ccf32a8cd592d5555784be589ac46b3322a95351ca0e54",
    "docs/brand/2026-identity/baseline.json": "253c3091b9938d96edc2d82cf6f036f61f5fe069a3e6b97715d86d8a8e7952ff",
    "docs/brand/2026-identity/brief.json": "872d428a6c6b9d748c055c98d725b442bda51ae6602bc163ddb8e6a6de0c11ac",
    "docs/brand/2026-identity/cleanup.json": "ffbe1af387549e7ca27ff8cb89d6f2b10c64e887b5145f425091517c601150ae",
    "docs/brand/2026-identity/color-report.json": "1a12e119e384ead68ed5ddac5038fd0ae6c3cd68c5c283da1deba1199dff0eca",
    "docs/brand/2026-identity/commands.json": "08e372d703396e72597fbce9b4192668059f106a516b8e778c3652c7fdfa0cdf",
    "docs/brand/2026-identity/delivery/brand-guide.md": "c6a2a2c5d8f7f8b635598f6fc7d8bd856927a192a22591c3911ccd365475445b",
    "docs/brand/2026-identity/delivery/logo-package.zip": "080e4f9592b31a1819b28ec050b96ec95666a32b7bb65760e67cf2992d14bd94",
    "docs/brand/2026-identity/delivery/logo.png": "11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3",
    "docs/brand/2026-identity/delivery/manifest.json": "1d309c2b538f3c3d021a4d899b888d3c4f9a71f03694d4ae0e7a92b07e902c54",
    "docs/brand/2026-identity/delivery-checks.json": "bfb870d989fc55e59ca5b5c5796fb1c24f1585f7430a5d9463172a55945b282f",
    "docs/brand/2026-identity/helper-provenance.json": "e000a6c861bd3f294548ce8692b443ce86e5187e5e5354a1fa5fe5b0d7965774",
    "docs/brand/2026-identity/http-fixed.json": "500328e07e381d2ba8d783bfbd899a2247010bbd8bc335fa3cfe357d4f9529c9",
    "docs/brand/2026-identity/icon-preservation.json": "39c0d10c06f47abf12918fb3df354ef54ab759f534dfffb495ae5e0f74b37320",
    "docs/brand/2026-identity/legacy-readme.original.txt": "ba7cb085770037fc8a3e5af65f3ba5f0717a8430b972eaf547f160a082ce70d6",
    "docs/brand/2026-identity/lockup.json": "d525c3fa94f0e85e7799a45fe781684411a2d08ba899d8c2a31a36ca66683b25",
    "docs/brand/2026-identity/native-receipt.json": "6d506fe3375188309945c730bdeecb00652da61825d98e1a485d3038f74d4629",
    "docs/brand/2026-identity/palette.json": "c754a7e38b317a6a9d033b8667360fb331578eb199131a93b3d091cb48d1e305",
    "docs/brand/2026-identity/preview.html": "bf1da531206931ffa45241bc3562b631bd305de2a20c48145dab84b783b475b7",
    "docs/brand/2026-identity/prompt-response.json": "7b8d0f820619ab6f01f2c18a6cfb8f7c9cd54fa1fe74d299b148e4b4b3b53ef0",
    "docs/brand/2026-identity/prompt.txt": "b9ddaf051eb98c1d65e43a4f2e71a315991266826135b66084edc7e4f1403da7",
    "docs/brand/2026-identity/quality-checks.json": "c3e1a4ea206d675051907b0a5bec00edcfa8c55191a100c2714ba2de474c0d85",
    "docs/brand/2026-identity/review.json": "7460811317708fee7cf3fee9aade1ee7898e8ee5822f148061f1d450ecfb74fe",
    "docs/brand/2026-identity/session.json": "9a9b54bb49e743969c6988accc02ecb0558d4fb325ce10b12d8641c7db390e28",
    "docs/brand/2026-identity/verification.json": "82cd4d9151475bdaffb6b6f116ca994782d436d630b26c74345907b7cfddf43f",
    "docs/brand/README.ko.md": "a5813463b68e8f70f3d169116694eb997a432b7bdf57f8ded893b5542d28100c",
    "docs/brand/README.md": "239bca8d754c76253adf0f16d7122fd428902e906b7a630c64df09a0ceb914a2",
    "docs/brand/brief.json": "aa0b625ab6c11286586df92513301e1e20380508bc28d6ddc62e8e9453c2a5b6",
    "docs/brand/delivery/brand-guide.md": "185b72f4752d572a793da2487d4911e2f1d3e1513bbc1493e3831be2ebc3ec65",
    "docs/brand/delivery/logo-package.zip": "16ccea597e80fbfcaacfab0dfd79126d279a4996fb15c7ee682a5030492afab2",
    "docs/brand/delivery/logo.png": "f4eb03545ca762db0f5664a3ff35f9580120b058200fbad9d5f89543d5ecf343",
    "docs/brand/delivery/manifest.json": "7c0bd506f81ad8ca18b97d5f3ef6742da8f32faaa5ff61fd618948194a49bf9d",
    "docs/brand/export.json": "7c776629054db26c33456e8e61b1140b9a9d7e37116948935cca4685fcad309b",
    "docs/brand/generation.json": "4d3425f8b10e971441e15d9cc8147f363a19a34ecab1597425a7e7629a904cce",
    "docs/brand/import.json": "84788dcb9b0912c571654eabbcf8ee866eb16fc0383f627223dc588e43c75c0f",
    "docs/brand/init.json": "af4d032602589095937de6d58448d10b97f470077770fc7e37e28ef5897ddf96",
    "docs/brand/legacy.md": "8e7f3fa70a6b84e69e2822ff8a4fff8c7354ab0d813f7f7fc4a12f9bad5f488b",
    "docs/brand/prompt-response.json": "4717bf5a1247d08835f273f60fe644854379e9671e8412de5b826f22edd770cb",
    "docs/brand/prompt.txt": "aade1fdadd545f9d551382156db17ff43010a6fa10ce293e105cdf5ce5857c21",
    "docs/brand/review-response.json": "883d1712b59e963701e2cbe17f3104ffc9609e9ebe150880dd9b3a088f1cb69f",
    "docs/brand/review.json": "4a2b2cbc5731c8f255703b4efae17401bf569c3a0207477a14f7bdcb7b401a30",
    "docs/brand/select.json": "1235aa5090ca8f0c54ab10210122a5c82b5d656695d812daeb26c41d9d791e1e",
    "docs/qa/app-icons/readme-preview/brand-en.html": "64fad756f565e3a5e927ed62a824defa2060ed77eb504bac0ae41d61213c59bb",
    "docs/qa/app-icons/readme-preview/brand-ko.html": "b7fd47402a5ce757de0cabd795231087c0f01b9cb3f292ea7542e2f1eeddf069",
    "docs/qa/app-icons/readme-preview/index.html": "dde14b144b64b86cbd56d38e1126c887cbe8220ecd5f63c9215c1d1e66471f65",
    "docs/qa/app-icons/readme-preview/ip-en.html": "aa768af6b3e1a8568303ec89b7e820c75630646d35d4f07754b66b668d413e0d",
    "docs/qa/app-icons/readme-preview/ip-ko.html": "45907cc94bc79aac2454bb1286073440bca1be5caf1b9bd11ff16fce846c28b8",
    "docs/qa/app-icons/readme-preview/pair-en.html": "99ef3cc4dd343a95fce5cfac85d42744ea5bcbc7a02469b29da55a7f03cfe9d2",
    "docs/qa/app-icons/readme-preview/pair-ko.html": "82e70985fa72ed958d137ed6264cc1b67dfd894020920da9b2bff546b75c57b7",
    "docs/qa/app-icons/readme-preview/readme-en.html": "b760d5dfec4b38abd65c8ac9ed71760cee8556223fa81b7b1f2f03cfaa8ddd3a",
    "docs/qa/app-icons/readme-preview/readme-ko.html": "5addebac0106ddb8d29ff09c4d28decdd1f07c865fcec3709c022543cba72cfb",
    "docs/README.md": "17189dd78dc4098dcecd9759d5b489966056923c3a8906a78150120b833e7bbb",
    "docs/README.ko.md": "df4154c4b7a5ddcb60a75ad511362899125a02a5ac6e59577b23b79d7b23bd59"
  }
}
```

## Initial navigation FAIL

Actual `readme-en.html` Brand logos link (fresh index94) opened `docs/samples/README.md` as raw Markdown, with no clickable sample links. Capture02 records this faithfully. Existing eight preview files cover representative individual pages but category/docs links remain raw source targets. Escalated to coordinator for D1-C-owned rendered category/link-map fix; this worker does not edit preview or source.

Resource variance: clicking the rendered hero generated an additional target=_blank PNG tab. It is clearly task-created and will be closed immediately after inspection; it was recorded after creation rather than pre-registered, so this is not claimed as perfect pre-registration. Future original-image links may create one temporary tab per click; these are registered now and each will be closed before continuing.

Independent old heading-anchor check (Git HEAD ATX headings, Unicode-preserving slug):
```json
[
  {
    "file": "README.md",
    "oldCount": 14,
    "missing": []
  },
  {
    "file": "README.ko.md",
    "oldCount": 14,
    "missing": []
  }
]
```

Register before Goyo asset actions: `/tmp/ll-quality-chrome/downloads/logo.png`, `/tmp/ll-quality-chrome/downloads/logo-package.zip`; possible Chrome default download `/Users/cillian/Downloads/logo-package.zip` (preexisting=true). Existing files will not be replaced. Original-image target=_blank tab possibility registered above; close any newly opened image tab after inspection.

ZIP collision receipt: default `logo-package.zip` preexisted (`true`) and was preserved. The actual new Chrome Done row was `logo-package (1).zip`; Chrome selected a free suffix, so this exact task-created file is registered after creation and will be removed alone. Earlier path-probe evidence for unsuffixed ZIP is not counted as the actual download.

Actual Goyo downloads:
```json
[
  {
    "path": "/Users/cillian/Downloads/logo-package (1).zip",
    "source": "docs/samples/items/03-goyo/delivery/logo-package.zip",
    "bytes": 889585,
    "sha256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
    "sourceSHA256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
    "match": true
  },
  {
    "path": "/tmp/ll-quality-chrome/downloads/logo.png",
    "source": "docs/samples/items/03-goyo/delivery/logo.png",
    "bytes": 898170,
    "sha256": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
    "sourceSHA256": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
    "match": true,
    "width": 1254,
    "height": 1254
  }
]
```

## Corrected navigation map release

D1-C msg_8b7bf230ca9e confirms14source renders + index. Rehashed before final navigation/screenshots:
```json
[
  {
    "preview": "docs/qa/app-icons/readme-preview/brand-en.html",
    "previewHash": "d658dee96580cbb6b902d410bfc16b4989f6dacb9f82b9d7619b95c346b28fe0",
    "source": "docs/samples/items/03-goyo/README.md",
    "embedded": "eb2fc0833a115c9bc217ece47c9e1d714fabe2eed2fae6ad64c158f4f5fb7fe3",
    "actual": "eb2fc0833a115c9bc217ece47c9e1d714fabe2eed2fae6ad64c158f4f5fb7fe3",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/brand-ko.html",
    "previewHash": "616c471827fb0c6d4fcc0e6e2a789a0e1c815575369b9f0e62048036a5032ce6",
    "source": "docs/samples/items/03-goyo/README.ko.md",
    "embedded": "bd0601f9342d2e8d03cf359705f795e763935cc7f8b6405402ad70ee973b2806",
    "actual": "bd0601f9342d2e8d03cf359705f795e763935cc7f8b6405402ad70ee973b2806",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/brands-en.html",
    "previewHash": "27d8cc79ec0693a8ca234d13426bda8b524c228e1e1c296ca7ca74725c2a02a0",
    "source": "docs/samples/README.md",
    "embedded": "7b870dab04532214b6dcaf8f42cdb3d73ff42225bb0169cc9dcd9e88bbd50d46",
    "actual": "7b870dab04532214b6dcaf8f42cdb3d73ff42225bb0169cc9dcd9e88bbd50d46",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/brands-ko.html",
    "previewHash": "54824dac387dd3ca9100e8fcf20c12b8dadc282c4dd2c03def86701f76537484",
    "source": "docs/samples/README.ko.md",
    "embedded": "cac86de6acbf380becda90a04f9cb4d25681cc37cecf7160cda721b2b853465e",
    "actual": "cac86de6acbf380becda90a04f9cb4d25681cc37cecf7160cda721b2b853465e",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/docs-en.html",
    "previewHash": "7ca082293e96626fa39e7c4288bc8d828890a198c6c891263faa94214414e093",
    "source": "docs/README.md",
    "embedded": "17189dd78dc4098dcecd9759d5b489966056923c3a8906a78150120b833e7bbb",
    "actual": "17189dd78dc4098dcecd9759d5b489966056923c3a8906a78150120b833e7bbb",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/docs-ko.html",
    "previewHash": "fbc13ccb3b16b62e31e9b942ccab57618dc23bd99317bf54c1b3ee1d62ecd34d",
    "source": "docs/README.ko.md",
    "embedded": "df4154c4b7a5ddcb60a75ad511362899125a02a5ac6e59577b23b79d7b23bd59",
    "actual": "df4154c4b7a5ddcb60a75ad511362899125a02a5ac6e59577b23b79d7b23bd59",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/icons-en.html",
    "previewHash": "8cd65c101e702d0bcbc6aeaa22138fe98b8947b2ceb3fe1de30f0ba4f3efb618",
    "source": "docs/app-icons/README.md",
    "embedded": "c4e85865f13ad3ba8eaf0e5de9d6b7d491a05f629a172893251f3c9b2da117cc",
    "actual": "c4e85865f13ad3ba8eaf0e5de9d6b7d491a05f629a172893251f3c9b2da117cc",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/icons-ko.html",
    "previewHash": "747371dccd742e3390940427da611014b9e744047426ae44e807d8962f9c31fc",
    "source": "docs/app-icons/README.ko.md",
    "embedded": "7febf2b847fe5d104e4ba3a5c87f6a7f1e3674bf19eb87754d72048c7047421f",
    "actual": "7febf2b847fe5d104e4ba3a5c87f6a7f1e3674bf19eb87754d72048c7047421f",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/ip-en.html",
    "previewHash": "bd93ac5d95d3b0fc8a1a8833abaac0ae09f6b54ae9f497f1c0a8a35cd7210feb",
    "source": "docs/app-icons/samples/ip-a1.md",
    "embedded": "b9d35f6af0741973431ec69ffe574f977961d15fda1720b70c65c077dd41a60e",
    "actual": "b9d35f6af0741973431ec69ffe574f977961d15fda1720b70c65c077dd41a60e",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/ip-ko.html",
    "previewHash": "f4f0acea923ac2c3765a0ccac3fb34fd79c88dcfc04f889f800eacf95e27623b",
    "source": "docs/app-icons/samples/ip-a1.ko.md",
    "embedded": "ce75bcfe7aa7978cb438451e2cc605e28b1f72192947c1be2d66b1826f8386dd",
    "actual": "ce75bcfe7aa7978cb438451e2cc605e28b1f72192947c1be2d66b1826f8386dd",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/pair-en.html",
    "previewHash": "43dc182c9b07d2aed1949e13f0001d42db42eadb400e4280d910489d8d0be33d",
    "source": "docs/app-icons/samples/monogram.md",
    "embedded": "417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580",
    "actual": "417ef63714be669145fc84e78223324e77d0f1f316808a064bfc3246c7c8b580",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/pair-ko.html",
    "previewHash": "bf89f831d06b38d1cf73924d923ef3f8f02d01b27891c5d879ecacbe84db57ed",
    "source": "docs/app-icons/samples/monogram.ko.md",
    "embedded": "dcd06e3f0990625914daa690e1d95de559be2bd4d87e2c4f575ad919a9ba55f5",
    "actual": "dcd06e3f0990625914daa690e1d95de559be2bd4d87e2c4f575ad919a9ba55f5",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/readme-en.html",
    "previewHash": "1addcd64fc9e50bdedc67c2266c9aca71cb2e94ce4a6b05b2846a59a7c2d8420",
    "source": "README.md",
    "embedded": "e3910e4a691ce1e555e8aa3461c2a01ced90f5e1c6014f4bdc21622fd89ccfec",
    "actual": "e3910e4a691ce1e555e8aa3461c2a01ced90f5e1c6014f4bdc21622fd89ccfec",
    "match": true
  },
  {
    "preview": "docs/qa/app-icons/readme-preview/readme-ko.html",
    "previewHash": "2712b4f0c436bcf22402a713fa269c231c798bbe8a87e8d7e6170ca9293e8689",
    "source": "README.ko.md",
    "embedded": "a0746d3f4df7cf036eabfdbffc07b7c0b9c94b738a63d13b1da27b6ee493cb11",
    "actual": "a0746d3f4df7cf036eabfdbffc07b7c0b9c94b738a63d13b1da27b6ee493cb11",
    "match": true
  }
]
```

Final hash/link verification:
```json
{
  "at": "2026-09-12T18:49:41.961Z",
  "oldGalleryChanged": [],
  "qualityGalleryChanged": [],
  "sourceChanged": [],
  "readmeOrAssetChanged": [],
  "expectedPreviewRevisions": [
    "docs/qa/app-icons/readme-preview/brand-en.html",
    "docs/qa/app-icons/readme-preview/brand-ko.html",
    "docs/qa/app-icons/readme-preview/index.html",
    "docs/qa/app-icons/readme-preview/ip-en.html",
    "docs/qa/app-icons/readme-preview/ip-ko.html",
    "docs/qa/app-icons/readme-preview/pair-en.html",
    "docs/qa/app-icons/readme-preview/pair-ko.html",
    "docs/qa/app-icons/readme-preview/readme-en.html",
    "docs/qa/app-icons/readme-preview/readme-ko.html"
  ],
  "finalPreviewChanged": [],
  "localLinkCount": 257,
  "missingLinks": []
}
```

Individual cleanup receipt:
```json
{
  "at": "2026-09-12T18:49:42.295Z",
  "files": [
    {
      "path": "/tmp/ll-quality-chrome/downloads/ip-a1.png",
      "sha256": "7dfbdf7195d5cb2d4c01116bc8e6a92f814f4a1b0ff87ca340af0549d4ae739b",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/ip-a1.txt",
      "sha256": "a7a745050d223646d1d0959def17cc4f83b85ed2d0152891617fcdd9ba78c4fd",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/pictogram-quality-v1.png",
      "sha256": "b0eb8adcdc2fb4ffbf2b3728217e07151d79517dd0321dbee5ce8fc3da59716a",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/pictogram-quality-v1.txt",
      "sha256": "cf7af5b39849a343c096e05c7b418f96d38f2e86777d897ea7afbb695f3392fd",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/abstract-quality-v1.png",
      "sha256": "93391909a8d835d0b97618a5075fd278e6fc4f5c5bc150ae330c95d6a23c0d9b",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/abstract-quality-v1.txt",
      "sha256": "5d4a776bab0b2ebee8c27787d85e2ff6c1c2d55ce81368a602adb13bc01c17e4",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/monogram-quality-v1.png",
      "sha256": "e5fa8ce56f0da9e879d8fb86f2c416e8fb391b466f625ef7ecf1c1847489c62f",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/monogram-quality-v1.txt",
      "sha256": "8b4e552faad9451fd3a3f91bf17b20ea7eeb9489a34480fbc5f8f29e06427756",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/soft-3d-quality-v1.png",
      "sha256": "ae58ba14b66c9953c5fa45456cf54912ed239e0434713edd50c31738cea132e2",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/soft-3d-quality-v1.txt",
      "sha256": "4ecbd90914e59d66f3924f50ae7526771ab61e4a4ce4735a442fdda7dfb1ac78",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/pixel-art-quality-v1.png",
      "sha256": "29f17526bff02d30f60d76bc0e8b32f446d16c2abac692be4587ed4cc40b0328",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/pixel-art-quality-v1.txt",
      "sha256": "706ef6130932940e17a9b0a4ac794390f9667353307e31bd75432476f52ba830",
      "removed": true
    },
    {
      "path": "/Users/cillian/Downloads/logo-package (1).zip",
      "sha256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/logo.png",
      "sha256": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
      "removed": true
    },
    {
      "path": "/tmp/ll-quality-chrome/downloads/logo-package.zip",
      "sha256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
      "removed": true
    }
  ],
  "tempRootAbsent": true,
  "preexistingZipPreserved": true,
  "preexistingZipSHA256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
  "server": "none created",
  "port": "8805 not used",
  "tmux": "none created",
  "browserContext": "no separate automation context created",
  "ownedHeroTab": "closed after inspection",
  "ownedReadmeTab": "closed via fresh index134",
  "persistentWindow": "one owned gallery tab retained at All/Square/128/Light and100% zoom",
  "userWindows": "preserved; no ambiguous New Tab cleanup attempted"
}
```

## Final observed outcome

The final English/Korean README renders use the final83-line root sources and the actual current1774×887 Logo Land PNG. Both show centered release/development/tool/docs badges, centered language links and the ivory/charcoal open-frame logo with the small warm square; visible lettering reads LOGO LAND. The hero PNG SHA-256 remains `11476b293b219b0298606ae8dea7422ca59eaf67b3e757811d7e2fa0a707aaf3`. Both rendered Credits/출처 sections explicitly state adaptation from s1dashu/ip-as-logo-skill and retain pinned-reference, license and third-party links. No new image, typography installation, vector conversion or native call was made.

| Observed case | Result | Evidence |
|---|---|---|
| Root EN/KO render + language switches | PASS: both final source hashes match embedded metadata; visible purpose, installation, usage and hero are rendered. English→한국어→English changed actual page. | 01,03 |
| Current logo original | PASS: actual image viewer title1774×887; original visible; original PNG unchanged. | 04 |
| Attribution | PASS: literal adaptation credit visible in both languages and in IP individual pages. | 05,06,13,14 |
| Narrow effective layout | PASS at independently set actual Chrome300% zoom: badges wrap, language navigation remains readable, image stays within page width, EN/KO prose wraps. Zoom restored100%. This is browser zoom exercising narrow effective layout, not mobile-device emulation or a measured device viewport. | 07–10 |
| Representative individual renders | PASS: Goyo EN/KO, IP owl EN/KO, monogram pair EN/KO all show actual source images and relevant request/download text. | 11–16 |
| Initial category flow | FAIL before fix: Brand logos opened raw .md with no clickable sample links. Escalation msg_51cb5b921a0f caused D1-C-owned preview map repair; failure capture retained. | 02 |
| Final brand category EN chain | PASS: final root→Brand logos→rendered brands-en→고요→PNG viewer1254×1254→Back; actual ZIP Save Link As to registered directory matches original889585bytes and SHA256. Then Brand samples returned to rendered category. | 17–19 plus action/download receipts |
| Final brand category KO chain | PASS: category language link→brands-ko→고요→원본 PNG viewer→Back→브랜드 샘플. KO ZIP link points at the same existing package tested through EN; no duplicate KO ZIP download claim. | 20 and action receipt |
| Final app category EN/KO | PASS: rendered category→IP owl→exact old IP PNG→Back→category; category→monogram pair→old PNG→Back→new PNG→Back→category, in both languages. PNG viewer titles1254×1254 and target paths matched source. | 22,23 and action receipt |
| Local HTML galleries | PASS: brand category opens existing10-brand gallery; app category opens new16gallery and old11gallery; Back returns to rendered category. | 21,24,25 |
| Docs EN/KO and anchors | PASS: rendered docs indexes and language switch; Korean 요청 예시 opens actual root request-section fragment. Independent14old heading anchors per root language all remain available;257local preview href/src and applicable HTML fragments resolve. | 26–28; anchor/link checks |
| Keyboard | PASS: Tab focused Preview index; Return opened the rendered preview index. The actual result is index navigation, not the initially intended next-language link. Gallery keyboard behavior is separately recorded in quality-comparison.md. | Action receipt |

All final14Markdown preview source hashes and15HTML fixture hashes were checked after the map freeze; no further changes occurred. Sources and non-preview assets among the380-file final baseline remain unchanged; nine initially existing preview files were intentionally revised by D1-C and six added, then the final15-file map was rebaselined. The initial eight representative screenshots remain exact-source body evidence, while final category/return captures use the corrected mapping. The complete preview is representative: nonrepresentative Markdown links intentionally remain their actual source destinations; this is not a fully rendered documentation site and those raw destinations are not represented as rendered-page evidence.

## Provenance and limits

D1-C prepared static HTML with the official GitHub Markdown API and a local stylesheet; the current local files embed exact source-path/source-sha256. I verified local rendered pages in external Chrome via Sky; I did not verify these changes on hosted GitHub. D1-C reports73public Markdown pages/799references/36language pairs plus bounded HTTP checks, and final map257references/37HTTPresponses; my independent final map path check also found257references with0missing paths/HTML anchors. Those source/HTTP checks supplement actual GUI evidence. No task HTTP server was required or started.

The raw JPEG captures are copied byte-for-byte from provider file URLs, never edited, cropped, resized, recompressed or synthesized. All62final captures (34quality,28README) were visually inspected when emitted. Fullscreen keeps unrelated tab/profile/address UI out of published frames; the native fullscreen tip is retained as captured. The initial05credits frame did not scroll and was replaced only after actual anchored scroll showed Credits; likewise08was replaced after language navigation reset zoom and300% was explicitly reapplied. Final inventories were rebuilt from the saved files so superseded in-memory entries are not accepted.

One ScreenCaptureKit -3811 failure occurred after the Korean category navigation; fresh state confirmed brands-ko in fullscreen, then normal/fullscreen state was re-grounded before capturing20. No ZIP save or navigation was blindly repeated. A missing inferred IP-link label stopped before clicking; the fresh AX label included its1254×1254 suffix and supplied the exact next index. The screenshot helper and click logs distinguish requested actions from observed destinations.

Process variances: the hero target=_blank tab and Chrome-generated suffixed ZIP basename were registered immediately after their unexpected creation rather than before; both were attributable to this task and are now removed. This is disclosed, not claimed as perfect pre-registration. The preexisting unsuffixed Downloads ZIP was preserved. No unowned browser window/tab/file was deleted.

## Nine-class QA

| Class | Actual observation or precise N/A |
|---|---|
| Malformed/broken path | Existing-source link checker plus257independent local preview checks pass. Actual missing rendered category was recorded FAIL and retested after the owner fixed the map. No user input/mutation API exists; corrupting product files is N/A. |
| Prompt injection | Saved prompts and page prose remained inert content; no embedded instructions were executed as task authority. Exact downloaded prompts are covered by Q5; no model immunity claim. |
| Cancel/resume | Two unsubmitted navigation-draft cancellations/reloads exercised the shared gallery workflow. README PNG navigation/Back and language return were observed. Mutation-job cancellation N/A. |
| Stale state | Fresh AX after every menu, tab, zoom, full-screen and navigation action;14source hashes checked before final screenshots; final map checked again afterward. Rejected mismatched frame names before final inventory. |
| Dirty worktree | All380baseline files either unchanged or nine expected D1-C preview-map edits; non-preview Markdown/PNG/ZIP and original gallery bytes unchanged. No source/README/gallery edit by this worker. |
| Bounded GUI/HTTP/process | Sky calls bounded30s, errors re-grounded. No own server, port listener, tmux, debugger or extra browser context created; HTTP evidence is D1-C-owned and separately attributed. |
| Flaky/artistic retry | No artificial production tests or native rerolls; failed label/capture transitions were inspected before recovery. Final ZIP replay was deliberate final-map flow verification via explicit Save Link As, not a blind repeat. |
| Misleading success | Initial raw Markdown navigation retained as FAIL, then actual corrected representative chains passed. Hosted GitHub, full-site rendering and physical mobile viewport are not claimed. Screenshots+real UI downloads+exact hashes support final result. |
| Repeated interruptions | Same saved comparison gallery retained across provider errors and navigation, then restored to All/Square/128/Light; README tab closed. Interrupted native job/production mutation N/A. |

## Final raw screenshot inventory

| File | Bytes | SHA-256 |
|---|---:|---|
| [readme-chrome/01-readme-en.jpg](readme-chrome/01-readme-en.jpg) | 102966 | `79254161087cbc982365fd243e538efa6a4162a6faa90855a663a4398abf3ff9` |
| [readme-chrome/02-category-raw-fail.jpg](readme-chrome/02-category-raw-fail.jpg) | 72574 | `5027adbc2dbe58389c2c988bf68663662da8220bda51a933ea2233e049009d0a` |
| [readme-chrome/03-readme-ko.jpg](readme-chrome/03-readme-ko.jpg) | 107083 | `5a7d347d6172f3608757061a924a46d6fd914db955e44b3868847b9417923f79` |
| [readme-chrome/04-current-logo-original.jpg](readme-chrome/04-current-logo-original.jpg) | 59776 | `2946e9d7bc45147a416a924d1f6649bf3b6bef00ef6a2b4a295e0af847c08157` |
| [readme-chrome/05-readme-en-credits.jpg](readme-chrome/05-readme-en-credits.jpg) | 124023 | `b5077bd6521d15189bee57a121ad3c9e7bef7037bdfcff4cfb647d7e2aca710b` |
| [readme-chrome/06-readme-ko-credits.jpg](readme-chrome/06-readme-ko-credits.jpg) | 117967 | `566e18e8920169cc35c424baeda5268f75325ed88354afbec430fed4938328ed` |
| [readme-chrome/07-ko-narrow-top.jpg](readme-chrome/07-ko-narrow-top.jpg) | 111087 | `fb81729d768544c0446c5cf1c3055904dd3dc4cd682a6dfc23f25787cf4621c0` |
| [readme-chrome/08-en-narrow-top.jpg](readme-chrome/08-en-narrow-top.jpg) | 107048 | `c6b2301696f928b7d4e96a39a9260d8150b4beebc6a194576e00716546fd7d17` |
| [readme-chrome/09-en-narrow-installation.jpg](readme-chrome/09-en-narrow-installation.jpg) | 109097 | `c969b8cf38527f1671a832665fa529d5fa8ae959036cb826c879e1821e24e31c` |
| [readme-chrome/10-ko-narrow-installation.jpg](readme-chrome/10-ko-narrow-installation.jpg) | 102366 | `7d89098b80a9efd1f49005aeee506c51a48e07ba848e967fd126493ca225cc26` |
| [readme-chrome/11-goyo-en.jpg](readme-chrome/11-goyo-en.jpg) | 70323 | `dfd5a5ef539051573fd2a4202f87ecc52ed0b5d178ad61b470f28988a3f2fe3f` |
| [readme-chrome/12-goyo-ko.jpg](readme-chrome/12-goyo-ko.jpg) | 70144 | `551d2885b0d49ee3fc4208d523f1e7c57e33dd587e78858fc2ead698b23984a7` |
| [readme-chrome/13-ip-en.jpg](readme-chrome/13-ip-en.jpg) | 100427 | `98d796ac2f3929fc53aa8a516a1a6c51877df7df0153d224afc15bc0024c242b` |
| [readme-chrome/14-ip-ko.jpg](readme-chrome/14-ip-ko.jpg) | 96513 | `4c5a14077892915d58b11815ade97db34042230f13461d88089ac4449a039169` |
| [readme-chrome/15-pair-en.jpg](readme-chrome/15-pair-en.jpg) | 80586 | `50457363128af0725d96580c3c18373cae9c103bd9a0a2b07cee5498393654c6` |
| [readme-chrome/16-pair-ko.jpg](readme-chrome/16-pair-ko.jpg) | 78735 | `e11d8a6a9f44cea1c22eb317b19364d723eefdc56193ef53aa246a48b3c3ec45` |
| [readme-chrome/17-goyo-downloads.jpg](readme-chrome/17-goyo-downloads.jpg) | 69069 | `d04c0000ed8a41af6e0369d14b9971efcb96c46c0aa501e15b7d8fbe82d31c43` |
| [readme-chrome/18-goyo-original.jpg](readme-chrome/18-goyo-original.jpg) | 61628 | `541e66b6102f41fd65a0db9affeadb3c1a46a7f7fb66f70bc9c009a45cc53941` |
| [readme-chrome/19-brands-en-fixed.jpg](readme-chrome/19-brands-en-fixed.jpg) | 76208 | `80ad9dc87311ccbff93b88fd64bf4bb473b23207e0d54b59601c9f7b3e0e3c2c` |
| [readme-chrome/20-brands-ko-fixed.jpg](readme-chrome/20-brands-ko-fixed.jpg) | 72174 | `2b853d4d721ea073001b41764de19db8855b2c33e8f78893b5dea3edfa20ae22` |
| [readme-chrome/21-local-brand-gallery.jpg](readme-chrome/21-local-brand-gallery.jpg) | 74554 | `3762fd4bcff01c0991ee1898f00df96710f6afe504b54d134dc329df4d1c86a2` |
| [readme-chrome/22-icons-ko-fixed.jpg](readme-chrome/22-icons-ko-fixed.jpg) | 78164 | `5b922f5ce9608018228266e98c20f7cf62d33df5c234d188ba01a3090a2adefa` |
| [readme-chrome/23-icons-en-fixed.jpg](readme-chrome/23-icons-en-fixed.jpg) | 83281 | `c6368323dd9dbae88d5f59b8df11d9071c68c3063727d47bc83974479d46cf48` |
| [readme-chrome/24-new-gallery-link.jpg](readme-chrome/24-new-gallery-link.jpg) | 120609 | `68fef7352d05374adc8fa2bf817eb968ab0355c9de8ba5672a0ccde89d5d0852` |
| [readme-chrome/25-old-gallery-link.jpg](readme-chrome/25-old-gallery-link.jpg) | 115914 | `65493fa22376c70420a02d57718265c979a0ea09a9ebd165e3661ba592e78dc1` |
| [readme-chrome/26-docs-en.jpg](readme-chrome/26-docs-en.jpg) | 99102 | `aba64eda84d990b3b545e0835a1bd6a8d2a8a8a788bcdf3b9d793b82b9e636c9` |
| [readme-chrome/27-docs-ko.jpg](readme-chrome/27-docs-ko.jpg) | 90161 | `cc9fc0a3f0d1d0ef979cbefa01d8465107733c1b137911c3a88a0542d61f1460` |
| [readme-chrome/28-docs-anchor-to-request.jpg](readme-chrome/28-docs-anchor-to-request.jpg) | 117967 | `566e18e8920169cc35c424baeda5268f75325ed88354afbec430fed4938328ed` |

## Final UI downloads

```json
[
  {
    "path": "/Users/cillian/Downloads/logo-package (1).zip",
    "source": "docs/samples/items/03-goyo/delivery/logo-package.zip",
    "bytes": 889585,
    "sha256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
    "sourceSHA256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
    "match": true
  },
  {
    "path": "/tmp/ll-quality-chrome/downloads/logo.png",
    "source": "docs/samples/items/03-goyo/delivery/logo.png",
    "bytes": 898170,
    "sha256": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
    "sourceSHA256": "4050303ae1bc5ec5a7741841b36a295ce033ed2be852fb53e893072f998d3174",
    "match": true,
    "width": 1254,
    "height": 1254
  },
  {
    "path": "/tmp/ll-quality-chrome/downloads/logo-package.zip",
    "source": "docs/samples/items/03-goyo/delivery/logo-package.zip",
    "bytes": 889585,
    "sha256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
    "sourceSHA256": "328f1158d9bb91798a8c20efa40bac9e2876920d70774826511796ded50a0ed7",
    "match": true,
    "method": "Final category chain → Save Link As… → registered directory"
  }
]
```

## Fresh action/state receipt

<details><summary>README-phase observed indices and outcomes</summary>

```json
{
  "actions": [
    {
      "at": "2026-09-12T18:38:37.543Z",
      "action": "click",
      "index": 138,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:38:41.456Z",
      "action": "click",
      "index": 94,
      "needle": "link Description: Brand logos,"
    },
    {
      "at": "2026-09-12T18:38:42.889Z",
      "action": "click",
      "index": 38,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:39:04.769Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:39:06.289Z",
      "action": "click",
      "index": 43,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:39:07.327Z",
      "action": "click",
      "index": 138,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:39:10.939Z",
      "action": "click",
      "index": 41,
      "needle": "link Description: English,"
    },
    {
      "at": "2026-09-12T18:39:12.331Z",
      "action": "click",
      "index": 50,
      "needle": "link Description: Logo Land open-frame symbol and LOGO LAND wordmark,"
    },
    {
      "at": "2026-09-12T18:39:24.525Z",
      "action": "click",
      "index": 40,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:39:30.417Z",
      "action": "click",
      "index": 138,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:39:54.118Z",
      "action": "click",
      "index": 138,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:39:57.787Z",
      "action": "click",
      "index": 43,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:40:01.284Z",
      "action": "click",
      "index": 138,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:40:42.804Z",
      "action": "click",
      "index": 139,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:40:46.549Z",
      "action": "click",
      "index": 42,
      "needle": "link Description: English,"
    },
    {
      "at": "2026-09-12T18:40:48.266Z",
      "action": "click",
      "index": 138,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:41:09.977Z",
      "action": "click",
      "index": 146,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:41:15.156Z",
      "action": "click",
      "index": 139,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:41:19.407Z",
      "action": "click",
      "index": 44,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:41:28.822Z",
      "action": "click",
      "index": 139,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:41:44.433Z",
      "action": "click",
      "index": 30,
      "needle": "link Description: Preview index,"
    },
    {
      "at": "2026-09-12T18:41:57.793Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: docs/samples/items/03-goyo/README.md,"
    },
    {
      "at": "2026-09-12T18:41:59.556Z",
      "action": "click",
      "index": 67,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:42:02.988Z",
      "action": "click",
      "index": 38,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:42:04.112Z",
      "action": "click",
      "index": 67,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:42:29.971Z",
      "action": "click",
      "index": 30,
      "needle": "link Description: Preview index,"
    },
    {
      "at": "2026-09-12T18:42:30.971Z",
      "action": "click",
      "index": 46,
      "needle": "link Description: docs/app-icons/samples/ip-a1.md,"
    },
    {
      "at": "2026-09-12T18:42:32.646Z",
      "action": "click",
      "index": 75,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:42:36.083Z",
      "action": "click",
      "index": 38,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:42:37.215Z",
      "action": "click",
      "index": 75,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:42:40.725Z",
      "action": "click",
      "index": 30,
      "needle": "link Description: Preview index,"
    },
    {
      "at": "2026-09-12T18:42:41.786Z",
      "action": "click",
      "index": 52,
      "needle": "link Description: docs/app-icons/samples/monogram.md,"
    },
    {
      "at": "2026-09-12T18:42:43.483Z",
      "action": "click",
      "index": 81,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:42:48.620Z",
      "action": "click",
      "index": 38,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:42:49.762Z",
      "action": "click",
      "index": 81,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:43:17.238Z",
      "action": "click",
      "index": 36,
      "needle": "link Description: English,"
    },
    {
      "at": "2026-09-12T18:43:38.887Z",
      "action": "click",
      "index": 55,
      "needle": "link Description: docs/samples/items/03-goyo/README.md,"
    },
    {
      "at": "2026-09-12T18:43:42.126Z",
      "action": "click",
      "index": 68,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:43:46.388Z",
      "action": "click",
      "index": 52,
      "needle": "link Description: ZIP package,"
    },
    {
      "at": "2026-09-12T18:43:58.592Z",
      "action": "click",
      "index": 50,
      "needle": "link Description: Original PNG,"
    },
    {
      "at": "2026-09-12T18:43:59.467Z",
      "action": "click",
      "index": 38,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:44:23.766Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:44:49.941Z",
      "action": "click",
      "index": 42,
      "needle": "link Description: Logo Land,"
    },
    {
      "at": "2026-09-12T18:44:50.910Z",
      "action": "click",
      "index": 6,
      "needle": "button Reload"
    },
    {
      "at": "2026-09-12T18:44:52.434Z",
      "action": "click",
      "index": 94,
      "needle": "link Description: Brand logos,"
    },
    {
      "at": "2026-09-12T18:44:54.222Z",
      "action": "click",
      "index": 116,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:45:14.226Z",
      "action": "click",
      "index": 62,
      "needle": "link Description: 고요,"
    },
    {
      "at": "2026-09-12T18:45:15.868Z",
      "action": "click",
      "index": 50,
      "needle": "link Description: Original PNG,"
    },
    {
      "at": "2026-09-12T18:45:16.774Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:45:36.129Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: Brand samples,"
    },
    {
      "at": "2026-09-12T18:45:36.869Z",
      "action": "click",
      "index": 38,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:45:37.898Z",
      "action": "click",
      "index": 116,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:45:54.867Z",
      "action": "click",
      "index": 116,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:45:58.552Z",
      "action": "click",
      "index": 62,
      "needle": "link Description: 고요,"
    },
    {
      "at": "2026-09-12T18:46:10.915Z",
      "action": "click",
      "index": 50,
      "needle": "link Description: 원본 PNG,"
    },
    {
      "at": "2026-09-12T18:46:11.799Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:46:12.497Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: 브랜드 샘플,"
    },
    {
      "at": "2026-09-12T18:46:13.082Z",
      "action": "click",
      "index": 105,
      "needle": "link Description: 인터랙티브 갤러리 (로컬에서 열기),"
    },
    {
      "at": "2026-09-12T18:46:14.196Z",
      "action": "click",
      "index": 155,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:46:17.910Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:46:19.099Z",
      "action": "click",
      "index": 42,
      "needle": "link Description: Logo Land,"
    },
    {
      "at": "2026-09-12T18:46:20.802Z",
      "action": "click",
      "index": 102,
      "needle": "link Description: 앱 아이콘,"
    },
    {
      "at": "2026-09-12T18:46:22.280Z",
      "action": "click",
      "index": 109,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:46:40.168Z",
      "action": "click",
      "index": 49,
      "needle": "link Description: 독서 부엉이 · 왼쪽 아래,"
    },
    {
      "at": "2026-09-12T18:46:53.133Z",
      "action": "click",
      "index": 47,
      "needle": "link Description: PNG 원본 다운로드 · 1254 × 1254,"
    },
    {
      "at": "2026-09-12T18:46:53.968Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:46:54.769Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: 앱 아이콘 샘플,"
    },
    {
      "at": "2026-09-12T18:46:55.404Z",
      "action": "click",
      "index": 82,
      "needle": "link Description: 메모 · 모,"
    },
    {
      "at": "2026-09-12T18:47:04.792Z",
      "action": "click",
      "index": 59,
      "needle": "link Description: PNG 원본, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png"
    },
    {
      "at": "2026-09-12T18:47:05.454Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:47:06.252Z",
      "action": "click",
      "index": 63,
      "needle": "link Description: PNG 원본, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png"
    },
    {
      "at": "2026-09-12T18:47:06.920Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:47:07.741Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: 앱 아이콘 샘플,"
    },
    {
      "at": "2026-09-12T18:47:08.389Z",
      "action": "click",
      "index": 36,
      "needle": "link Description: English,"
    },
    {
      "at": "2026-09-12T18:47:09.443Z",
      "action": "click",
      "index": 109,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:47:12.779Z",
      "action": "click",
      "index": 49,
      "needle": "link Description: Reading owl · lower-left,"
    },
    {
      "at": "2026-09-12T18:47:25.837Z",
      "action": "click",
      "index": 47,
      "needle": "link Description: Download original PNG · 1254 × 1254,"
    },
    {
      "at": "2026-09-12T18:47:26.614Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:47:27.887Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: App icon samples,"
    },
    {
      "at": "2026-09-12T18:47:29.278Z",
      "action": "click",
      "index": 82,
      "needle": "link Description: Notes · 모,"
    },
    {
      "at": "2026-09-12T18:47:30.513Z",
      "action": "click",
      "index": 59,
      "needle": "link Description: Original PNG, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png"
    },
    {
      "at": "2026-09-12T18:47:31.810Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:47:33.005Z",
      "action": "click",
      "index": 63,
      "needle": "link Description: Original PNG, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png"
    },
    {
      "at": "2026-09-12T18:47:33.845Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:47:34.587Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: App icon samples,"
    },
    {
      "at": "2026-09-12T18:47:45.153Z",
      "action": "click",
      "index": 96,
      "needle": "link Description: Interactive gallery (open locally),"
    },
    {
      "at": "2026-09-12T18:47:47.546Z",
      "action": "click",
      "index": 241,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:47:52.616Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:47:54.082Z",
      "action": "click",
      "index": 98,
      "needle": "link Description: Original gallery (open locally),"
    },
    {
      "at": "2026-09-12T18:47:55.428Z",
      "action": "click",
      "index": 191,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:47:58.847Z",
      "action": "click",
      "index": 4,
      "needle": "button Back"
    },
    {
      "at": "2026-09-12T18:48:00.101Z",
      "action": "click",
      "index": 40,
      "needle": "link Description: Docs,"
    },
    {
      "at": "2026-09-12T18:48:01.632Z",
      "action": "click",
      "index": 114,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:48:05.255Z",
      "action": "click",
      "index": 38,
      "needle": "link Description: 한국어,"
    },
    {
      "at": "2026-09-12T18:48:06.655Z",
      "action": "click",
      "index": 114,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:48:32.001Z",
      "action": "click",
      "index": 51,
      "needle": "link Description: 요청 예시,"
    },
    {
      "at": "2026-09-12T18:48:33.687Z",
      "action": "click",
      "index": 138,
      "needle": "full screen button"
    },
    {
      "at": "2026-09-12T18:49:03.215Z",
      "action": "sky.click",
      "element_index": 52,
      "label": "Reset previews"
    },
    {
      "at": "2026-09-12T18:49:05.326Z",
      "action": "click",
      "index": 239,
      "needle": "full screen button"
    }
  ],
  "observations": [
    {
      "name": "01-readme-en",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.md\n\t\t\t\t\t\t34 link Description: Release v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t35 link Description: Development version 0.5.0; unreleased, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t36 link Description: Codex Plugin, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t37 link Description: Python 3.12+, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: PNG output, Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t40 link Description: Korean documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t41 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t43 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t45 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t47 link Description: Samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t48 heading Logo Land, Value: 1\n\t\t\t\t\t\t50 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t52 heading Installation, Value: 2\n\t\t\t\t\t\t55 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t60 link Description: full plugin installation guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.md\n\t\t\t\t\t\t65 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t67 heading Try it, Value: 2\n\t\t\t\t\t\t72 heading What you can make, Value: 2\n\t\t\t\t\t\t88 heading Samples, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: Brand logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t\t\t98 link Description: Colors and typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t\t\t102 link Description: App icons, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t\t\t106 link Description: Transparent logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t\t\t110 link Description: Logo Land identity, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.md\n\t\t\t\t\t\t112 heading Credits, Value: 2\n\t\t\t\t\t\t114 text IP character guidance is adapted from \n\t\t\t\t\t\t115 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t117 link Description: pinned adaptation reference, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t119 link Description: MIT license notice, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t121 link Description: third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t123 link Description: Documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t125 link Description: Changelog, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t127 link Description: Get help, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html"
    },
    {
      "name": "FAIL category navigation raw Markdown",
      "ax": "\t\t\t\t26 HTML content file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t27 text # Brand samples\nThe focused UI element is 26 HTML content file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md"
    },
    {
      "name": "02-category-raw-fail",
      "ax": "\t\t\t\t26 HTML content file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\nThe focused UI element is 26 HTML content file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md"
    },
    {
      "name": "03-readme-ko",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.ko.md\n\t\t\t\t\t\t34 link Description: v0.3.1 릴리스, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t35 link Description: 미출시 개발 버전 0.5.0, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t36 link Description: Codex 플러그인, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t37 link Description: Python 3.12 이상, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: PNG 출력. To get missing image descriptions, open the context menu., Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t40 link Description: 한국어 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t41 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t43 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t45 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t47 link Description: 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t48 heading Logo Land (로고랜드), Value: 1\n\t\t\t\t\t\t50 link Description: Logo Land 열린 프레임 심볼과 LOGO LAND 워드마크, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t52 heading 설치, Value: 2\n\t\t\t\t\t\t55 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t60 link Description: 전체 플러그인 설치 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.ko.md\n\t\t\t\t\t\t65 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t67 heading 이렇게 요청해 보세요, Value: 2\n\t\t\t\t\t\t72 heading 만들 수 있는 것, Value: 2\n\t\t\t\t\t\t88 heading 샘플, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: 브랜드 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t\t\t98 link Description: 색상과 타이포그래피, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t\t\t102 link Description: 앱 아이콘, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.ko.md\n\t\t\t\t\t\t\t\t106 link Description: 투명 배경 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t\t\t110 link Description: Logo Land 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.ko.md\n\t\t\t\t\t\t112 heading 출처, Value: 2\n\t\t\t\t\t\t115 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t117 link Description: 고정된 원본과 각색 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t119 link Description: MIT 라이선스 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t121 link Description: 제3자 출처 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t123 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t125 link Description: 변경 이력, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t127 link Description: 도움 요청, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html"
    },
    {
      "name": "04-current-logo-original",
      "ax": ""
    },
    {
      "name": "05-readme-en-credits",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.md\n\t\t\t\t\t\t34 link Description: Release v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t35 link Description: Development version 0.5.0; unreleased, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t36 link Description: Codex Plugin, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t37 link Description: Python 3.12+, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: PNG output, Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t40 link Description: Korean documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t41 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t43 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t45 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t47 link Description: Samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t48 heading Logo Land, Value: 1\n\t\t\t\t\t\t50 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t52 heading Installation, Value: 2\n\t\t\t\t\t\t55 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t60 link Description: full plugin installation guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.md\n\t\t\t\t\t\t65 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t67 heading Try it, Value: 2\n\t\t\t\t\t\t72 heading What you can make, Value: 2\n\t\t\t\t\t\t88 heading Samples, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: Brand logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t\t\t98 link Description: Colors and typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t\t\t102 link Description: App icons, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t\t\t106 link Description: Transparent logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t\t\t110 link Description: Logo Land identity, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.md\n\t\t\t\t\t\t112 heading Credits, Value: 2\n\t\t\t\t\t\t114 text IP character guidance is adapted from \n\t\t\t\t\t\t115 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t117 link Description: pinned adaptation reference, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t119 link Description: MIT license notice, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t121 link Description: third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t123 link Description: Documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t125 link Description: Changelog, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t127 link Description: Get help, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 50 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png"
    },
    {
      "name": "05-readme-en-credits",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.md\n\t\t\t\t\t\t34 link Description: Release v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t35 link Description: Development version 0.5.0; unreleased, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t36 link Description: Codex Plugin, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t37 link Description: Python 3.12+, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: PNG output, Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t40 link Description: Korean documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t41 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t43 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t45 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t47 link Description: Samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t48 heading Logo Land, Value: 1\n\t\t\t\t\t\t50 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t52 heading Installation, Value: 2\n\t\t\t\t\t\t55 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t60 link Description: full plugin installation guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.md\n\t\t\t\t\t\t65 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t67 heading Try it, Value: 2\n\t\t\t\t\t\t72 heading What you can make, Value: 2\n\t\t\t\t\t\t88 heading Samples, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: Brand logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t\t\t98 link Description: Colors and typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t\t\t102 link Description: App icons, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t\t\t106 link Description: Transparent logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t\t\t110 link Description: Logo Land identity, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.md\n\t\t\t\t\t\t112 heading Credits, Value: 2\n\t\t\t\t\t\t114 text IP character guidance is adapted from \n\t\t\t\t\t\t115 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t117 link Description: pinned adaptation reference, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t119 link Description: MIT license notice, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t121 link Description: third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t123 link Description: Documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t125 link Description: Changelog, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t127 link Description: Get help, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 50 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png"
    },
    {
      "name": "06-readme-ko-credits",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.ko.md\n\t\t\t\t\t\t34 link Description: v0.3.1 릴리스, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t35 link Description: 미출시 개발 버전 0.5.0, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t36 link Description: Codex 플러그인, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t37 link Description: Python 3.12 이상, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: PNG 출력. To get missing image descriptions, open the context menu., Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t40 link Description: 한국어 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t41 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t43 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t45 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t47 link Description: 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t48 heading Logo Land (로고랜드), Value: 1\n\t\t\t\t\t\t50 link Description: Logo Land 열린 프레임 심볼과 LOGO LAND 워드마크, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t52 heading 설치, Value: 2\n\t\t\t\t\t\t55 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t60 link Description: 전체 플러그인 설치 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.ko.md\n\t\t\t\t\t\t65 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t67 heading 이렇게 요청해 보세요, Value: 2\n\t\t\t\t\t\t72 heading 만들 수 있는 것, Value: 2\n\t\t\t\t\t\t88 heading 샘플, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: 브랜드 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t\t\t98 link Description: 색상과 타이포그래피, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t\t\t102 link Description: 앱 아이콘, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.ko.md\n\t\t\t\t\t\t\t\t106 link Description: 투명 배경 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t\t\t110 link Description: Logo Land 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.ko.md\n\t\t\t\t\t\t112 heading 출처, Value: 2\n\t\t\t\t\t\t115 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t117 link Description: 고정된 원본과 각색 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t119 link Description: MIT 라이선스 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t121 link Description: 제3자 출처 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t123 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t125 link Description: 변경 이력, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t127 link Description: 도움 요청, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html"
    },
    {
      "name": "Narrow effective viewport",
      "zoom": "\t\t\t\t\t11 button Zoom: 300%\n\t\t138 container Zoom: 150%\n\t\t\t\t\t141 container Zoom: 300%",
      "method": "Actual Chrome300% zoom; not mobile-device emulation or measured device width"
    },
    {
      "name": "07-ko-narrow-top",
      "ax": "\t\t\t\t27 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t29 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t31 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t33 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.ko.md\n\t\t\t\t\t\t35 link Description: v0.3.1 릴리스, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t36 link Description: 미출시 개발 버전 0.5.0, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t37 link Description: Codex 플러그인, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: Python 3.12 이상, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: PNG 출력. To get missing image descriptions, open the context menu., Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t40 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t41 link Description: 한국어 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t42 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t46 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t48 link Description: 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t49 heading Logo Land (로고랜드), Value: 1\n\t\t\t\t\t\t51 link Description: Logo Land 열린 프레임 심볼과 LOGO LAND 워드마크, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t53 heading 설치, Value: 2\n\t\t\t\t\t\t56 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t61 link Description: 전체 플러그인 설치 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.ko.md\n\t\t\t\t\t\t66 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t68 heading 이렇게 요청해 보세요, Value: 2\n\t\t\t\t\t\t73 heading 만들 수 있는 것, Value: 2\n\t\t\t\t\t\t89 heading 샘플, Value: 2\n\t\t\t\t\t\t\t\t95 link Description: 브랜드 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t\t\t99 link Description: 색상과 타이포그래피, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t\t\t103 link Description: 앱 아이콘, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.ko.md\n\t\t\t\t\t\t\t\t107 link Description: 투명 배경 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t\t\t111 link Description: Logo Land 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.ko.md\n\t\t\t\t\t\t113 heading 출처, Value: 2\n\t\t\t\t\t\t116 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t118 link Description: 고정된 원본과 각색 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t120 link Description: MIT 라이선스 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t122 link Description: 제3자 출처 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t124 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t126 link Description: 변경 이력, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t128 link Description: 도움 요청, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 27 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html"
    },
    {
      "name": "08-en-narrow-top",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.md\n\t\t\t\t\t\t34 link Description: Release v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t35 link Description: Development version 0.5.0; unreleased, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t36 link Description: Codex Plugin, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t37 link Description: Python 3.12+, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: PNG output, Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t40 link Description: Korean documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t41 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t43 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t45 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t47 link Description: Samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t48 heading Logo Land, Value: 1\n\t\t\t\t\t\t50 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t52 heading Installation, Value: 2\n\t\t\t\t\t\t55 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t60 link Description: full plugin installation guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.md\n\t\t\t\t\t\t65 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t67 heading Try it, Value: 2\n\t\t\t\t\t\t72 heading What you can make, Value: 2\n\t\t\t\t\t\t88 heading Samples, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: Brand logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t\t\t98 link Description: Colors and typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t\t\t102 link Description: App icons, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t\t\t106 link Description: Transparent logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t\t\t110 link Description: Logo Land identity, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.md\n\t\t\t\t\t\t112 heading Credits, Value: 2\n\t\t\t\t\t\t114 text IP character guidance is adapted from \n\t\t\t\t\t\t115 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t117 link Description: pinned adaptation reference, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t119 link Description: MIT license notice, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t121 link Description: third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t123 link Description: Documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t125 link Description: Changelog, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t127 link Description: Get help, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html"
    },
    {
      "name": "08-en-narrow-top",
      "ax": "\t\t\t\t27 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t29 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t31 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t33 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.md\n\t\t\t\t\t\t35 link Description: Release v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t36 link Description: Development version 0.5.0; unreleased, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t37 link Description: Codex Plugin, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: Python 3.12+, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: PNG output, Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t40 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t41 link Description: Korean documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t42 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t46 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t48 link Description: Samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t49 heading Logo Land, Value: 1\n\t\t\t\t\t\t51 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t53 heading Installation, Value: 2\n\t\t\t\t\t\t56 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t61 link Description: full plugin installation guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.md\n\t\t\t\t\t\t66 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t68 heading Try it, Value: 2\n\t\t\t\t\t\t73 heading What you can make, Value: 2\n\t\t\t\t\t\t89 heading Samples, Value: 2\n\t\t\t\t\t\t\t\t95 link Description: Brand logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t\t\t99 link Description: Colors and typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t\t\t103 link Description: App icons, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t\t\t107 link Description: Transparent logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t\t\t111 link Description: Logo Land identity, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.md\n\t\t\t\t\t\t113 heading Credits, Value: 2\n\t\t\t\t\t\t115 text IP character guidance is adapted from \n\t\t\t\t\t\t116 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t118 link Description: pinned adaptation reference, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t120 link Description: MIT license notice, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t122 link Description: third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t124 link Description: Documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t126 link Description: Changelog, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t128 link Description: Get help, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 27 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html"
    },
    {
      "name": "09-en-narrow-installation",
      "ax": "\t\t\t\t27 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t29 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t31 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t33 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.md\n\t\t\t\t\t\t35 link Description: Release v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t36 link Description: Development version 0.5.0; unreleased, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t37 link Description: Codex Plugin, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: Python 3.12+, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: PNG output, Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t40 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t41 link Description: Korean documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t42 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t46 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t48 link Description: Samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t49 heading Logo Land, Value: 1\n\t\t\t\t\t\t51 link Description: Logo Land open-frame symbol and LOGO LAND wordmark, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t53 heading Installation, Value: 2\n\t\t\t\t\t\t56 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t61 link Description: full plugin installation guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.md\n\t\t\t\t\t\t66 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t68 heading Try it, Value: 2\n\t\t\t\t\t\t73 heading What you can make, Value: 2\n\t\t\t\t\t\t89 heading Samples, Value: 2\n\t\t\t\t\t\t\t\t95 link Description: Brand logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t\t\t99 link Description: Colors and typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t\t\t103 link Description: App icons, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t\t\t107 link Description: Transparent logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t\t\t111 link Description: Logo Land identity, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.md\n\t\t\t\t\t\t113 heading Credits, Value: 2\n\t\t\t\t\t\t115 text IP character guidance is adapted from \n\t\t\t\t\t\t116 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t118 link Description: pinned adaptation reference, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t120 link Description: MIT license notice, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t122 link Description: third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t124 link Description: Documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t126 link Description: Changelog, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t128 link Description: Get help, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 27 HTML content Local Markdown QA · Logo Land, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html"
    },
    {
      "name": "10-ko-narrow-installation",
      "ax": "\t\t\t\t27 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t29 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t31 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t33 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.ko.md\n\t\t\t\t\t\t35 link Description: v0.3.1 릴리스, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t36 link Description: 미출시 개발 버전 0.5.0, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t37 link Description: Codex 플러그인, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: Python 3.12 이상, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: PNG 출력. To get missing image descriptions, open the context menu., Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t40 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t41 link Description: 한국어 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t42 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t46 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t48 link Description: 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t49 heading Logo Land (로고랜드), Value: 1\n\t\t\t\t\t\t51 link Description: Logo Land 열린 프레임 심볼과 LOGO LAND 워드마크, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t53 heading 설치, Value: 2\n\t\t\t\t\t\t56 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t61 link Description: 전체 플러그인 설치 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.ko.md\n\t\t\t\t\t\t66 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t68 heading 이렇게 요청해 보세요, Value: 2\n\t\t\t\t\t\t73 heading 만들 수 있는 것, Value: 2\n\t\t\t\t\t\t89 heading 샘플, Value: 2\n\t\t\t\t\t\t\t\t95 link Description: 브랜드 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t\t\t99 link Description: 색상과 타이포그래피, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t\t\t103 link Description: 앱 아이콘, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.ko.md\n\t\t\t\t\t\t\t\t107 link Description: 투명 배경 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t\t\t111 link Description: Logo Land 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.ko.md\n\t\t\t\t\t\t113 heading 출처, Value: 2\n\t\t\t\t\t\t116 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t118 link Description: 고정된 원본과 각색 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t120 link Description: MIT 라이선스 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t122 link Description: 제3자 출처 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t124 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t126 link Description: 변경 이력, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t128 link Description: 도움 요청, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 27 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html"
    },
    {
      "name": "11-goyo-en",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 고요, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/README.md\n\t\t\t\t\t\t34 heading 고요, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-ko.html\n\t\t\t\t\t\t40 link Description: Brand samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 link Description: 고요 symbol + korean lettering original, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t\t45 heading Try a similar request, Value: 2\n\t\t\t\t\t\t48 heading Downloads, Value: 2\n\t\t\t\t\t\t50 link Description: Original PNG, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t\t52 link Description: ZIP package, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo-package.zip\n\t\t\t\t\t\t54 link Description: Brand guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/brand-guide.md\n\t\t\t\t\t\t56 link Description: Saved original prompt, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/prompt.txt\nThe focused UI element is 26 HTML content Local Markdown QA · 고요, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html"
    },
    {
      "name": "12-goyo-ko",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 고요, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/README.ko.md\n\t\t\t\t\t\t34 heading 고요, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-ko.html\n\t\t\t\t\t\t40 link Description: 브랜드 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t44 link Description: 고요 한글 조합형 원본, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t\t45 heading 비슷하게 요청해 보세요, Value: 2\n\t\t\t\t\t\t48 heading 다운로드, Value: 2\n\t\t\t\t\t\t50 link Description: 원본 PNG, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t\t52 link Description: ZIP 패키지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo-package.zip\n\t\t\t\t\t\t54 link Description: 브랜드 가이드, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/brand-guide.md\n\t\t\t\t\t\t56 link Description: 저장된 원본 프롬프트, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/prompt.txt\nThe focused UI element is 26 HTML content Local Markdown QA · 고요, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-ko.html"
    },
    {
      "name": "13-ip-en",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Reading owl · lower-left, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-a1.md\n\t\t\t\t\t\t34 heading Reading owl · lower-left, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-ko.html\n\t\t\t\t\t\t40 link Description: App icon samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 heading Original, Value: 2\n\t\t\t\t\t\t46 link Description: Reading owl · lower-left, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png\n\t\t\t\t\t\t47 link Description: Download original PNG · 1254 × 1254, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png\n\t\t\t\t\t\t49 link Description: Saved image prompt, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-a1.txt\n\t\t\t\t\t\t50 heading Try a similar request, Value: 2\n\t\t\t\t\t\t54 heading Credits, Value: 2\n\t\t\t\t\t\t56 text IP character guidance is adapted from \n\t\t\t\t\t\t57 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t59 link Description: pinned adaptation reference, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t61 link Description: MIT license notice, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t63 link Description: third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\nThe focused UI element is 26 HTML content Local Markdown QA · Reading owl · lower-left, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-en.html"
    },
    {
      "name": "14-ip-ko",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 독서 부엉이 · 왼쪽 아래, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-a1.ko.md\n\t\t\t\t\t\t34 heading 독서 부엉이 · 왼쪽 아래, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-ko.html\n\t\t\t\t\t\t40 link Description: 앱 아이콘 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.ko.md\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t44 heading 원본, Value: 2\n\t\t\t\t\t\t46 link Description: 독서 부엉이 · 왼쪽 아래, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png\n\t\t\t\t\t\t47 link Description: PNG 원본 다운로드 · 1254 × 1254, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png\n\t\t\t\t\t\t49 link Description: 저장된 이미지 프롬프트, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-a1.txt\n\t\t\t\t\t\t50 heading 비슷하게 요청해 보세요, Value: 2\n\t\t\t\t\t\t54 heading 출처, Value: 2\n\t\t\t\t\t\t57 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t59 link Description: 고정된 원본과 각색 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t61 link Description: MIT 라이선스 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t63 link Description: 제3자 출처 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\nThe focused UI element is 26 HTML content Local Markdown QA · 독서 부엉이 · 왼쪽 아래, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-ko.html"
    },
    {
      "name": "15-pair-en",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Notes · 모, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/monogram.md\n\t\t\t\t\t\t34 heading Notes · 모, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-ko.html\n\t\t\t\t\t\t40 link Description: App icon samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t\t\t\t54 link Description: Notes · 모 · Original, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png\n\t\t\t\t\t\t\t\t\t56 link Description: Notes · 모 · Revised direction, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png\n\t\t\t\t\t\t\t\t\t59 link Description: Original PNG, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png\n\t\t\t\t\t\t\t\t\t61 link Description: Saved prompt, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/monogram.txt\n\t\t\t\t\t\t\t\t\t63 link Description: Original PNG, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png\n\t\t\t\t\t\t\t\t\t65 link Description: Saved prompt, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/monogram-quality-v1.txt\n\t\t\t\t\t\t67 heading Try a similar request, Value: 2\nThe focused UI element is 26 HTML content Local Markdown QA · Notes · 모, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-en.html"
    },
    {
      "name": "16-pair-ko",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 메모 · 모, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/monogram.ko.md\n\t\t\t\t\t\t34 heading 메모 · 모, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-ko.html\n\t\t\t\t\t\t40 link Description: 앱 아이콘 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-ko.html\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t\t\t\t54 link Description: 메모 · 모 · 원본, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png\n\t\t\t\t\t\t\t\t\t56 link Description: 메모 · 모 · 수정 방향, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png\n\t\t\t\t\t\t\t\t\t59 link Description: PNG 원본, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png\n\t\t\t\t\t\t\t\t\t61 link Description: 저장된 프롬프트, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/monogram.txt\n\t\t\t\t\t\t\t\t\t63 link Description: PNG 원본, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png\n\t\t\t\t\t\t\t\t\t65 link Description: 저장된 프롬프트, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/monogram-quality-v1.txt\n\t\t\t\t\t\t67 heading 비슷하게 요청해 보세요, Value: 2\nThe focused UI element is 26 HTML content Local Markdown QA · 메모 · 모, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-ko.html"
    },
    {
      "name": "Rendered keyboard Tab",
      "ax": "html\n\t81 close button\n\t82 full screen button Help: this button also has an action to zoom the window, Secondary Actions: zoom the window\n\t83 minimize button\n84 menu bar\n\t85 Chrome\n\t86 File\n\t87 Edit\n\t88 View\n\t89 History\n\t90 Bookmarks\n\t91 Profiles\n\t92 Tab\n\t93 Window\n\t94 Help\n\nThe focused UI element is 30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html"
    },
    {
      "name": "Rendered keyboard Enter opened Preview index",
      "ax": "Window: \"README local Markdown QA\", App: Google Chrome.\n\t\t\t\t26 HTML content README local Markdown QA, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\nThe focused UI element is 26 HTML content README local Markdown QA, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html"
    },
    {
      "name": "17-goyo-downloads",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 고요, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/README.md\n\t\t\t\t\t\t34 heading 고요, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-ko.html\n\t\t\t\t\t\t40 link Description: Brand samples, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-en.html\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 link Description: 고요 symbol + korean lettering original, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t\t45 heading Try a similar request, Value: 2\n\t\t\t\t\t\t48 heading Downloads, Value: 2\n\t\t\t\t\t\t50 link Description: Original PNG, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t\t52 link Description: ZIP package, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo-package.zip\n\t\t\t\t\t\t54 link Description: Brand guide, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/brand-guide.md\n\t\t\t\t\t\t56 link Description: Saved original prompt, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/prompt.txt\nThe focused UI element is 26 HTML content Local Markdown QA · 고요, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html"
    },
    {
      "name": "18-goyo-original",
      "ax": ""
    },
    {
      "name": "19-brands-en-fixed",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Brand samples, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.md\n\t\t\t\t\t\t34 heading Brand samples, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t40 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-en.html\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t\t\t\t52 link Description: LUMA, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/01-luma/README.md\n\t\t\t\t\t\t\t\t\t57 link Description: LOOP LAB, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/02-loop-lab/README.md\n\t\t\t\t\t\t\t\t\t62 link Description: 고요, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-en.html\n\t\t\t\t\t\t\t\t\t67 link Description: BREAD & BLOOM, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/04-bread-bloom/README.md\n\t\t\t\t\t\t\t\t\t72 link Description: KITE, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/05-kite/README.md\n\t\t\t\t\t\t\t\t\t77 link Description: MISO, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/06-miso/README.md\n\t\t\t\t\t\t\t\t\t82 link Description: NORTHLINE · NL, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/07-northline/README.md\n\t\t\t\t\t\t\t\t\t87 link Description: 물결, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/08-mulgyeol/README.md\n\t\t\t\t\t\t\t\t\t92 link Description: FERN, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/09-fern/README.md\n\t\t\t\t\t\t\t\t\t97 link Description: NOVA NOTES, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/10-nova-notes/README.md\n\t\t\t\t\t\t101 link Description: transparent logo example, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t103 link Description: Colors & typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t105 link Description: Interactive gallery (open locally), Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html\nThe focused UI element is 26 HTML content Local Markdown QA · Brand samples, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-en.html"
    },
    {
      "name": "Final EN category → Goyo → PNG",
      "ax": "Window: \"logo.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: logo.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: logo.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png"
    },
    {
      "name": "20-brands-ko-fixed",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 브랜드 샘플, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t34 heading 브랜드 샘플, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t40 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t\t\t\t52 link Description: LUMA, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/01-luma/README.ko.md\n\t\t\t\t\t\t\t\t\t57 link Description: LOOP LAB, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/02-loop-lab/README.ko.md\n\t\t\t\t\t\t\t\t\t62 link Description: 고요, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-ko.html\n\t\t\t\t\t\t\t\t\t67 link Description: BREAD & BLOOM, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/04-bread-bloom/README.ko.md\n\t\t\t\t\t\t\t\t\t72 link Description: KITE, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/05-kite/README.ko.md\n\t\t\t\t\t\t\t\t\t77 link Description: MISO, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/06-miso/README.ko.md\n\t\t\t\t\t\t\t\t\t82 link Description: NORTHLINE · NL, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/07-northline/README.ko.md\n\t\t\t\t\t\t\t\t\t87 link Description: 물결, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/08-mulgyeol/README.ko.md\n\t\t\t\t\t\t\t\t\t92 link Description: FERN, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/09-fern/README.ko.md\n\t\t\t\t\t\t\t\t\t97 link Description: NOVA NOTES, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/10-nova-notes/README.ko.md\n\t\t\t\t\t\t101 link Description: 투명 로고 예제, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t103 link Description: 색상과 글자, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t105 link Description: 인터랙티브 갤러리 (로컬에서 열기), Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html\nThe focused UI element is 26 HTML content Local Markdown QA · 브랜드 샘플, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html"
    },
    {
      "name": "ScreenCaptureKit -3811 recovery",
      "detail": "Fresh state showed brands-ko fullscreen; no repeated navigation or ZIP save."
    },
    {
      "name": "20-brands-ko-fixed",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 브랜드 샘플, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/README.ko.md\n\t\t\t\t\t\t34 heading 브랜드 샘플, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t40 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t\t\t\t52 link Description: LUMA, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/01-luma/README.ko.md\n\t\t\t\t\t\t\t\t\t57 link Description: LOOP LAB, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/02-loop-lab/README.ko.md\n\t\t\t\t\t\t\t\t\t62 link Description: 고요, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brand-ko.html\n\t\t\t\t\t\t\t\t\t67 link Description: BREAD & BLOOM, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/04-bread-bloom/README.ko.md\n\t\t\t\t\t\t\t\t\t72 link Description: KITE, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/05-kite/README.ko.md\n\t\t\t\t\t\t\t\t\t77 link Description: MISO, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/06-miso/README.ko.md\n\t\t\t\t\t\t\t\t\t82 link Description: NORTHLINE · NL, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/07-northline/README.ko.md\n\t\t\t\t\t\t\t\t\t87 link Description: 물결, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/08-mulgyeol/README.ko.md\n\t\t\t\t\t\t\t\t\t92 link Description: FERN, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/09-fern/README.ko.md\n\t\t\t\t\t\t\t\t\t97 link Description: NOVA NOTES, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/10-nova-notes/README.ko.md\n\t\t\t\t\t\t101 link Description: 투명 로고 예제, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t103 link Description: 색상과 글자, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t105 link Description: 인터랙티브 갤러리 (로컬에서 열기), Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html\nThe focused UI element is 26 HTML content Local Markdown QA · 브랜드 샘플, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html"
    },
    {
      "name": "KO category → Goyo → original PNG",
      "ax": "Window: \"logo.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: logo.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: logo.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/items/03-goyo/delivery/logo.png"
    },
    {
      "name": "21-local-brand-gallery",
      "ax": "\t\t\t\t26 HTML content Logo Land (로고랜드) — 로고 샘플 아카이브, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html\n\t\t\t\t\t27 link Description: 샘플 갤러리로 바로 가기, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html#collection\n\t\t\t\t\t\t29 link Description: Logo Land 로고랜드 처음으로, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html#top\n\t\t\t\t\t\t\t31 link Description: 샘플 둘러보기 , Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html#collection\n\t\t\t\t\t\t\t32 link Description: 이렇게 만듭니다, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html#process\n\t\t\t\t\t\t\t36 heading 작은 형태, 선명한 정체성., Value: 1\n\t\t\t\t\t\t\t40 link Description: 열 가지 로고 만나보기, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html#collection\n\t\t\t\t\t\t\t48 heading 로고, 그리고 그 시작, Value: 2\n\t\t\t\t\t\t\t120 heading 말로 시작해, 형태로 다듬습니다., Value: 2\n\t\t\t\t\t\t\t\t\t127 heading 원하는 로고를 말해주세요., Value: 3\n\t\t\t\t\t\t\t\t\t132 heading 요청이 첫 시안이 됩니다., Value: 3\n\t\t\t\t\t\t\t\t\t137 heading 확인하고, 더 가깝게 다듬어요., Value: 3\n\t\t\t\t\t\t144 link Description: 처음으로 , Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html#top\nThe focused UI element is 26 HTML content Logo Land (로고랜드) — 로고 샘플 아카이브, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/index.html"
    },
    {
      "name": "22-icons-ko-fixed",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · 앱 아이콘 샘플, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.ko.md\n\t\t\t\t\t\t34 heading 앱 아이콘 샘플, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-ko.html\n\t\t\t\t\t\t40 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t44 heading IP 캐릭터, Value: 2\n\t\t\t\t\t\t\t\t49 link Description: 독서 부엉이 · 왼쪽 아래, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-ko.html\n\t\t\t\t\t\t\t\t52 link Description: 독서 부엉이 · 오른쪽 아래, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-a2.ko.md\n\t\t\t\t\t\t\t\t55 link Description: 차분한 독서 카피바라 · 왼쪽 아래, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-b1.ko.md\n\t\t\t\t\t\t\t\t58 link Description: 차분한 독서 카피바라 · 오른쪽 아래, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-b2.ko.md\n\t\t\t\t\t\t\t\t61 link Description: 친근한 독서 강아지 · 왼쪽 아래, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-c1.ko.md\n\t\t\t\t\t\t\t\t64 link Description: 친근한 독서 강아지 · 오른쪽 아래, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-c2.ko.md\n\t\t\t\t\t\t65 heading 픽토그램, Value: 2\n\t\t\t\t\t\t\t\t70 link Description: 날씨 · 해와 구름, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/pictogram.ko.md\n\t\t\t\t\t\t71 heading 추상형, Value: 2\n\t\t\t\t\t\t\t\t76 link Description: 집중 · 맞물린 곡선, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/abstract.ko.md\n\t\t\t\t\t\t77 heading 모노그램, Value: 2\n\t\t\t\t\t\t\t\t82 link Description: 메모 · 모, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-ko.html\n\t\t\t\t\t\t83 heading 소프트 3D, Value: 2\n\t\t\t\t\t\t\t\t88 link Description: 식물 관리 · 옥빛 잎, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/soft-3d.ko.md\n\t\t\t\t\t\t89 heading 픽셀 아트, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: 타이머 · 모래시계, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/pixel-art.ko.md\n\t\t\t\t\t\t96 link Description: 인터랙티브 갤러리 (로컬에서 열기), Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/index.html\n\t\t\t\t\t\t98 link Description: 기존 원본 갤러리 (로컬에서 열기), Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html\nThe focused UI element is 26 HTML content Local Markdown QA · 앱 아이콘 샘플, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-ko.html"
    },
    {
      "name": "KO icons → IP → original PNG",
      "ax": "Window: \"ip-a1.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: ip-a1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: ip-a1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png"
    },
    {
      "name": "KO pair old PNG",
      "ax": "Window: \"monogram.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: monogram.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: monogram.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png"
    },
    {
      "name": "KO pair new PNG",
      "ax": "Window: \"monogram-quality-v1.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: monogram-quality-v1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: monogram-quality-v1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png"
    },
    {
      "name": "23-icons-en-fixed",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · App icon samples, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/README.md\n\t\t\t\t\t\t34 heading App icon samples, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-ko.html\n\t\t\t\t\t\t40 link Description: Docs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-en.html\n\t\t\t\t\t\t42 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t44 heading IP character, Value: 2\n\t\t\t\t\t\t\t45 text IP character\n\t\t\t\t\t\t\t\t49 link Description: Reading owl · lower-left, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/ip-en.html\n\t\t\t\t\t\t\t\t52 link Description: Reading owl · lower-right, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-a2.md\n\t\t\t\t\t\t\t\t55 link Description: Calm reading capybara · lower-left, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-b1.md\n\t\t\t\t\t\t\t\t58 link Description: Calm reading capybara · lower-right, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-b2.md\n\t\t\t\t\t\t\t\t61 link Description: Friendly reading puppy · lower-left, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-c1.md\n\t\t\t\t\t\t\t\t64 link Description: Friendly reading puppy · lower-right, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/ip-c2.md\n\t\t\t\t\t\t65 heading Pictogram, Value: 2\n\t\t\t\t\t\t\t\t70 link Description: Weather · sun and cloud, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/pictogram.md\n\t\t\t\t\t\t71 heading Abstract, Value: 2\n\t\t\t\t\t\t\t\t76 link Description: Focus · interlocking arcs, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/abstract.md\n\t\t\t\t\t\t77 heading Monogram, Value: 2\n\t\t\t\t\t\t\t\t82 link Description: Notes · 모, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/pair-en.html\n\t\t\t\t\t\t83 heading Soft 3D, Value: 2\n\t\t\t\t\t\t\t\t88 link Description: Plant care · jade leaf, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/soft-3d.md\n\t\t\t\t\t\t89 heading Pixel art, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: Timer · hourglass, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/samples/pixel-art.md\n\t\t\t\t\t\t96 link Description: Interactive gallery (open locally), Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/index.html\n\t\t\t\t\t\t98 link Description: Original gallery (open locally), Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html\nThe focused UI element is 26 HTML content Local Markdown QA · App icon samples, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-en.html"
    },
    {
      "name": "EN icons → IP original",
      "ax": "Window: \"ip-a1.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: ip-a1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: ip-a1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png"
    },
    {
      "name": "EN pair old PNG",
      "ax": "Window: \"monogram.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: monogram.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: monogram.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png"
    },
    {
      "name": "EN pair new PNG",
      "ax": "Window: \"monogram-quality-v1.png (1254×1254)\", App: Google Chrome.\n\t\t\t\t26 Unlabeled image Description: monogram-quality-v1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png\n\t\t\t\t\t27 Unlabeled image To get missing image descriptions, open the context menu.\nThe focused UI element is 26 Unlabeled image Description: monogram-quality-v1.png (1254×1254). To get missing image descriptions, open the context menu., URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png"
    },
    {
      "name": "New16 gallery through docs link",
      "ax": "\t\t\t\t26 HTML content App icon studies: original and refined · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/index.html\n\t\t\t\t\t\t\t31 text 16 ORIGINALS · ONE COLLECTION\n\t\t\t\t\t\t\t\t40 radio button Square, Value: 1\n\t\t\t\t\t\t\t\t47 radio button 128 px, Value: 1\n\t\t\t\t\t\t\t\t50 radio button Light, Value: 1\n\t\t\t\t\t\t\t\t55 radio button All artwork, Value: 1\n\t\t\t\t\t\t\t\t\t217 text 16 PIXEL ART\nThe focused UI element is 26 HTML content App icon studies: original and refined · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/index.html"
    },
    {
      "name": "24-new-gallery-link",
      "ax": "\t\t\t\t26 HTML content App icon studies: original and refined · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/index.html\n\t\t\t\t\t27 link Description: Skip to artwork, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/index.html#artwork\n\t\t\t\t\t\t\t32 heading App icon studies: original and refined, Value: 1\n\t\t\t\t\t\t\t\t63 heading The originals, Value: 2\n\t\t\t\t\t\t\t\t\t69 heading ip-a1, Value: 2\n\t\t\t\t\t\t\t\t\t74 link Description: Download original ip-a1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/ip-a1.png\n\t\t\t\t\t\t\t\t\t75 link Description: Exact prompt ip-a1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/ip-a1.txt\n\t\t\t\t\t\t\t\t\t79 heading ip-a2, Value: 2\n\t\t\t\t\t\t\t\t\t84 link Description: Download original ip-a2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/ip-a2.png\n\t\t\t\t\t\t\t\t\t85 link Description: Exact prompt ip-a2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/ip-a2.txt\n\t\t\t\t\t\t\t\t\t89 heading ip-b1, Value: 2\n\t\t\t\t\t\t\t\t\t94 link Description: Download original ip-b1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/ip-b1.png\n\t\t\t\t\t\t\t\t\t95 link Description: Exact prompt ip-b1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/ip-b1.txt\n\t\t\t\t\t\t\t\t\t99 heading ip-b2, Value: 2\n\t\t\t\t\t\t\t\t\t104 link Description: Download original ip-b2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/ip-b2.png\n\t\t\t\t\t\t\t\t\t105 link Description: Exact prompt ip-b2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/ip-b2.txt\n\t\t\t\t\t\t\t\t\t109 heading ip-c1, Value: 2\n\t\t\t\t\t\t\t\t\t114 link Description: Download original ip-c1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/ip-c1.png\n\t\t\t\t\t\t\t\t\t115 link Description: Exact prompt ip-c1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/ip-c1.txt\n\t\t\t\t\t\t\t\t\t119 heading ip-c2, Value: 2\n\t\t\t\t\t\t\t\t\t124 link Description: Download original ip-c2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/ip-c2.png\n\t\t\t\t\t\t\t\t\t125 link Description: Exact prompt ip-c2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/ip-c2.txt\n\t\t\t\t\t\t\t\t\t129 heading pictogram, Value: 2\n\t\t\t\t\t\t\t\t\t134 link Description: Download original pictogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/pictogram.png\n\t\t\t\t\t\t\t\t\t135 link Description: Exact prompt pictogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/pictogram.txt\n\t\t\t\t\t\t\t\t\t139 heading pictogram-quality-v1, Value: 2\n\t\t\t\t\t\t\t\t\t144 link Description: Download original pictogram-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/pictogram-quality-v1.png\n\t\t\t\t\t\t\t\t\t145 link Description: Exact prompt pictogram-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/pictogram-quality-v1.txt\n\t\t\t\t\t\t\t\t\t149 heading abstract, Value: 2\n\t\t\t\t\t\t\t\t\t154 link Description: Download original abstract, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/abstract.png\n\t\t\t\t\t\t\t\t\t155 link Description: Exact prompt abstract, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/abstract.txt\n\t\t\t\t\t\t\t\t\t159 heading abstract-quality-v1, Value: 2\n\t\t\t\t\t\t\t\t\t164 link Description: Download original abstract-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/abstract-quality-v1.png\n\t\t\t\t\t\t\t\t\t165 link Description: Exact prompt abstract-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/abstract-quality-v1.txt\n\t\t\t\t\t\t\t\t\t169 heading monogram, Value: 2\n\t\t\t\t\t\t\t\t\t174 link Description: Download original monogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram.png\n\t\t\t\t\t\t\t\t\t175 link Description: Exact prompt monogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/monogram.txt\n\t\t\t\t\t\t\t\t\t179 heading monogram-quality-v1, Value: 2\n\t\t\t\t\t\t\t\t\t184 link Description: Download original monogram-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/monogram-quality-v1.png\n\t\t\t\t\t\t\t\t\t185 link Description: Exact prompt monogram-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/monogram-quality-v1.txt\n\t\t\t\t\t\t\t\t\t189 heading soft-3d, Value: 2\n\t\t\t\t\t\t\t\t\t194 link Description: Download original soft-3d, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/soft-3d.png\n\t\t\t\t\t\t\t\t\t195 link Description: Exact prompt soft-3d, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/soft-3d.txt\n\t\t\t\t\t\t\t\t\t199 heading soft-3d-quality-v1, Value: 2\n\t\t\t\t\t\t\t\t\t204 link Description: Download original soft-3d-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/soft-3d-quality-v1.png\n\t\t\t\t\t\t\t\t\t205 link Description: Exact prompt soft-3d-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/soft-3d-quality-v1.txt\n\t\t\t\t\t\t\t\t\t209 heading pixel-art, Value: 2\n\t\t\t\t\t\t\t\t\t214 link Description: Download original pixel-art, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/pixel-art.png\n\t\t\t\t\t\t\t\t\t215 link Description: Exact prompt pixel-art, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/pixel-art.txt\n\t\t\t\t\t\t\t\t\t219 heading pixel-art-quality-v1, Value: 2\n\t\t\t\t\t\t\t\t\t224 link Description: Download original pixel-art-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/images/pixel-art-quality-v1.png\n\t\t\t\t\t\t\t\t\t225 link Description: Exact prompt pixel-art-quality-v1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/prompts/pixel-art-quality-v1.txt\n\t\t\t\t\t\t\t230 link Description: Collection manifest, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/manifest.json\nThe focused UI element is 26 HTML content App icon studies: original and refined · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons-quality-v1/index.html"
    },
    {
      "name": "Old11 gallery through docs link",
      "ax": "\t\t\t\t26 HTML content Small canvas, big character. · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html\n\t\t\t\t\t\t\t31 text 11 ORIGINALS · ONE COLLECTION\n\t\t\t\t\t\t\t\t40 radio button Square, Value: 1\n\t\t\t\t\t\t\t\t47 radio button 128 px, Value: 1\n\t\t\t\t\t\t\t\t50 radio button Light, Value: 1\n\t\t\t\t\t\t\t\t55 radio button All artwork, Value: 1\n\t\t\t\t\t\t\t\t\t167 text 11 PIXEL ART\nThe focused UI element is 26 HTML content Small canvas, big character. · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html"
    },
    {
      "name": "25-old-gallery-link",
      "ax": "\t\t\t\t26 HTML content Small canvas, big character. · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html\n\t\t\t\t\t27 link Description: Skip to artwork, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html#artwork\n\t\t\t\t\t\t\t32 heading Small canvas, big character., Value: 1\n\t\t\t\t\t\t\t\t63 heading The originals, Value: 2\n\t\t\t\t\t\t\t\t\t69 heading ip-a1, Value: 2\n\t\t\t\t\t\t\t\t\t74 link Description: Download original ip-a1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a1.png\n\t\t\t\t\t\t\t\t\t75 link Description: Exact prompt ip-a1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-a1.txt\n\t\t\t\t\t\t\t\t\t79 heading ip-a2, Value: 2\n\t\t\t\t\t\t\t\t\t84 link Description: Download original ip-a2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-a2.png\n\t\t\t\t\t\t\t\t\t85 link Description: Exact prompt ip-a2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-a2.txt\n\t\t\t\t\t\t\t\t\t89 heading ip-b1, Value: 2\n\t\t\t\t\t\t\t\t\t94 link Description: Download original ip-b1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-b1.png\n\t\t\t\t\t\t\t\t\t95 link Description: Exact prompt ip-b1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-b1.txt\n\t\t\t\t\t\t\t\t\t99 heading ip-b2, Value: 2\n\t\t\t\t\t\t\t\t\t104 link Description: Download original ip-b2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-b2.png\n\t\t\t\t\t\t\t\t\t105 link Description: Exact prompt ip-b2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-b2.txt\n\t\t\t\t\t\t\t\t\t109 heading ip-c1, Value: 2\n\t\t\t\t\t\t\t\t\t114 link Description: Download original ip-c1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-c1.png\n\t\t\t\t\t\t\t\t\t115 link Description: Exact prompt ip-c1, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-c1.txt\n\t\t\t\t\t\t\t\t\t119 heading ip-c2, Value: 2\n\t\t\t\t\t\t\t\t\t124 link Description: Download original ip-c2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/ip-c2.png\n\t\t\t\t\t\t\t\t\t125 link Description: Exact prompt ip-c2, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/ip-c2.txt\n\t\t\t\t\t\t\t\t\t129 heading pictogram, Value: 2\n\t\t\t\t\t\t\t\t\t134 link Description: Download original pictogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/pictogram.png\n\t\t\t\t\t\t\t\t\t135 link Description: Exact prompt pictogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/pictogram.txt\n\t\t\t\t\t\t\t\t\t139 heading abstract, Value: 2\n\t\t\t\t\t\t\t\t\t144 link Description: Download original abstract, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/abstract.png\n\t\t\t\t\t\t\t\t\t145 link Description: Exact prompt abstract, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/abstract.txt\n\t\t\t\t\t\t\t\t\t149 heading monogram, Value: 2\n\t\t\t\t\t\t\t\t\t154 link Description: Download original monogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/monogram.png\n\t\t\t\t\t\t\t\t\t155 link Description: Exact prompt monogram, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/monogram.txt\n\t\t\t\t\t\t\t\t\t159 heading soft-3d, Value: 2\n\t\t\t\t\t\t\t\t\t164 link Description: Download original soft-3d, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/soft-3d.png\n\t\t\t\t\t\t\t\t\t165 link Description: Exact prompt soft-3d, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/soft-3d.txt\n\t\t\t\t\t\t\t\t\t169 heading pixel-art, Value: 2\n\t\t\t\t\t\t\t\t\t174 link Description: Download original pixel-art, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/images/pixel-art.png\n\t\t\t\t\t\t\t\t\t175 link Description: Exact prompt pixel-art, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/prompts/pixel-art.txt\n\t\t\t\t\t\t\t180 link Description: Collection manifest, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/manifest.json\nThe focused UI element is 26 HTML content Small canvas, big character. · App icon gallery, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/app-icons/index.html"
    },
    {
      "name": "26-docs-en",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land documentation, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-en.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.md\n\t\t\t\t\t\t34 heading Logo Land documentation, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t40 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t42 heading Start here, Value: 2\n\t\t\t\t\t\t\t\t47 link Description: Installation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.md\n\t\t\t\t\t\t\t\t51 link Description: Example requests, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html#try-it\n\t\t\t\t\t\t53 heading Samples, Value: 2\n\t\t\t\t\t\t\t\t58 link Description: Brand logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-en.html\n\t\t\t\t\t\t\t\t62 link Description: Colors and typography, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.md\n\t\t\t\t\t\t\t\t66 link Description: App icons, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-en.html\n\t\t\t\t\t\t\t\t70 link Description: Transparent logos, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.md\n\t\t\t\t\t\t\t\t74 link Description: Logo Land identity, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.md\n\t\t\t\t\t\t76 heading Guides, Value: 2\n\t\t\t\t\t\t\t\t81 link Description: Logo directions, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/logo-directions.md\n\t\t\t\t\t\t\t\t84 link Description: Colors and palettes, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/color-workflow.md\n\t\t\t\t\t\t\t\t87 link Description: Lettering and font references, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/typography.md\n\t\t\t\t\t\t\t\t90 link Description: App icon artwork, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/app-icons.md\n\t\t\t\t\t\t\t\t93 link Description: Revision history and project files, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/project-files.md\n\t\t\t\t\t\t\t\t96 link Description: Delivery checks, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/delivery-checks.md\n\t\t\t\t\t\t97 link Description: Changelog, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t99 link Description: Third-party notices, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t101 link Description: Get help, Value: github.com/t1seo/logo-land/issues\n\t\t\t\t\t\t102 link Description: Archive, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/archive.md\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land documentation, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-en.html"
    },
    {
      "name": "27-docs-ko",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land 문서, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/README.ko.md\n\t\t\t\t\t\t34 heading Logo Land 문서, Value: 1\n\t\t\t\t\t\t36 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-en.html\n\t\t\t\t\t\t38 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t40 link Description: Logo Land, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t42 heading 시작하기, Value: 2\n\t\t\t\t\t\t\t\t47 link Description: 설치, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.ko.md\n\t\t\t\t\t\t\t\t51 link Description: 요청 예시, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html#%EC%9D%B4%EB%A0%87%EA%B2%8C-%EC%9A%94%EC%B2%AD%ED%95%B4-%EB%B3%B4%EC%84%B8%EC%9A%94\n\t\t\t\t\t\t53 heading 샘플, Value: 2\n\t\t\t\t\t\t\t\t58 link Description: 브랜드 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t\t\t62 link Description: 색상과 타이포그래피, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t\t\t66 link Description: 앱 아이콘, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-ko.html\n\t\t\t\t\t\t\t\t70 link Description: 투명 배경 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t\t\t74 link Description: Logo Land 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.ko.md\n\t\t\t\t\t\t76 heading 사용 안내, Value: 2\n\t\t\t\t\t\t\t\t81 link Description: 로고 방향, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/logo-directions.md\n\t\t\t\t\t\t\t\t84 link Description: 색상과 팔레트, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/color-workflow.md\n\t\t\t\t\t\t\t\t87 link Description: 글자와 폰트 참고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/typography.md\n\t\t\t\t\t\t\t\t90 link Description: 앱 아이콘 아트워크, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/app-icons.md\n\t\t\t\t\t\t\t\t93 link Description: 수정 이력과 프로젝트 파일, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/project-files.md\n\t\t\t\t\t\t\t\t96 link Description: 전달 전 검사, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/delivery-checks.md\n\t\t\t\t\t\t97 link Description: 변경 이력, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t99 link Description: 제3자 출처 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t101 link Description: 도움 요청, Value: github.com/t1seo/logo-land/issues\n\t\t\t\t\t\t102 link Description: 보관 자료, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/archive.md\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land 문서, URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html"
    },
    {
      "name": "Docs KO example anchor",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html#%EC%9D%B4%EB%A0%87%EA%B2%8C-%EC%9A%94%EC%B2%AD%ED%95%B4-%EB%B3%B4%EC%84%B8%EC%9A%94\n\t\t\t\t\t\t48 heading Logo Land (로고랜드), Value: 1\n\t\t\t\t\t\t52 heading 설치, Value: 2\n\t\t\t\t\t\t58 text $logo-land\n\t\t\t\t\t\t67 heading 이렇게 요청해 보세요, Value: 2\n\t\t\t\t\t\t69 text $logo-land 명상 스튜디오 고요의 차분한 로고 시안 두 개를 만들어 주세요. 단순한 심볼과 정확한 한글 고요를 조합해 주세요.\n\t\t\t\t\t\t70 text $logo-land 독서 앱에 어울리는 IP 캐릭터를 제품과 관련된 세 방향으로 정하고 독립 시안 여섯 개를 만들어 주세요. 색은 알아서 골라 주세요.\n\t\t\t\t\t\t72 heading 만들 수 있는 것, Value: 2\n\t\t\t\t\t\t88 heading 샘플, Value: 2\n\t\t\t\t\t\t112 heading 출처, Value: 2\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html#%EC%9D%B4%EB%A0%87%EA%B2%8C-%EC%9A%94%EC%B2%AD%ED%95%B4-%EB%B3%B4%EC%84%B8%EC%9A%94"
    },
    {
      "name": "28-docs-anchor-to-request",
      "ax": "\t\t\t\t26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html#%EC%9D%B4%EB%A0%87%EA%B2%8C-%EC%9A%94%EC%B2%AD%ED%95%B4-%EB%B3%B4%EC%84%B8%EC%9A%94\n\t\t\t\t\t\t28 text Local static Markdown preview · GitHub Markdown API + local stylesheet. This is not a hosted GitHub page.\n\t\t\t\t\t\t\t30 link Description: Preview index, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/index.html\n\t\t\t\t\t\t\t32 link Description: Exact Markdown source, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/README.ko.md\n\t\t\t\t\t\t34 link Description: v0.3.1 릴리스, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t35 link Description: 미출시 개발 버전 0.5.0, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t36 link Description: Codex 플러그인, Value: camo.githubusercontent.com/f69d244da8dfd3ccf745da8538a8f7aef731b940c20520d0a86ae373940f8911/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d506c7567696e2d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t37 link Description: Python 3.12 이상, Value: camo.githubusercontent.com/e4702bb1947ffc2d175c04d1dbd7cbf0472ccb4ca3e6d6d67a4bc1d1ad1d7c9b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31322532422d3139313931373f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t38 link Description: PNG 출력. To get missing image descriptions, open the context menu., Value: camo.githubusercontent.com/17759c896e6b0ef69e1bb4bf6d2b3b48099127f9db8cd661cb99810225950b73/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f75747075742d504e472d6136346233323f7374796c653d666c61742d737175617265266c6162656c436f6c6f723d663666336563\n\t\t\t\t\t\t39 link Description: English documentation, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-en.html\n\t\t\t\t\t\t40 link Description: 한국어 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t41 link Description: English, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-en.html\n\t\t\t\t\t\t43 link Description: 한국어, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html\n\t\t\t\t\t\t45 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t47 link Description: 샘플, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t48 heading Logo Land (로고랜드), Value: 1\n\t\t\t\t\t\t50 link Description: Logo Land 열린 프레임 심볼과 LOGO LAND 워드마크, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/assets/logo-land-studio.png\n\t\t\t\t\t\t52 heading 설치, Value: 2\n\t\t\t\t\t\t55 link Description: skills/logo-land/SKILL.md, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/SKILL.md\n\t\t\t\t\t\t60 link Description: 전체 플러그인 설치 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/installation.ko.md\n\t\t\t\t\t\t65 link Description: v0.3.1, Value: github.com/t1seo/logo-land/releases/tag/v0.3.1\n\t\t\t\t\t\t67 heading 이렇게 요청해 보세요, Value: 2\n\t\t\t\t\t\t72 heading 만들 수 있는 것, Value: 2\n\t\t\t\t\t\t88 heading 샘플, Value: 2\n\t\t\t\t\t\t\t\t94 link Description: 브랜드 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/brands-ko.html\n\t\t\t\t\t\t\t\t98 link Description: 색상과 타이포그래피, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/colors/README.ko.md\n\t\t\t\t\t\t\t\t102 link Description: 앱 아이콘, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/icons-ko.html\n\t\t\t\t\t\t\t\t106 link Description: 투명 배경 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/samples/transparency.ko.md\n\t\t\t\t\t\t\t\t110 link Description: Logo Land 로고, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/brand/README.ko.md\n\t\t\t\t\t\t112 heading 출처, Value: 2\n\t\t\t\t\t\t115 link Description: s1dashu/ip-as-logo-skill, Value: github.com/s1dashu/ip-as-logo-skill\n\t\t\t\t\t\t117 link Description: 고정된 원본과 각색 안내, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/references/ip-mascot.md\n\t\t\t\t\t\t119 link Description: MIT 라이선스 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/skills/logo-land/assets/ip-as-logo.LICENSE\n\t\t\t\t\t\t121 link Description: 제3자 출처 고지, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/THIRD_PARTY_NOTICES.md\n\t\t\t\t\t\t123 link Description: 문서, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/docs-ko.html\n\t\t\t\t\t\t125 link Description: 변경 이력, Value: file:///Users/cillian/Documents/Github/Projects/logo-generator/CHANGELOG.md\n\t\t\t\t\t\t127 link Description: 도움 요청, Value: github.com/t1seo/logo-land/issues\nThe focused UI element is 26 HTML content Local Markdown QA · Logo Land (로고랜드), URL: file:///Users/cillian/Documents/Github/Projects/logo-generator/docs/qa/app-icons/readme-preview/readme-ko.html#%EC%9D%B4%EB%A0%87%EA%B2%8C-%EC%9A%94%EC%B2%AD%ED%95%B4-%EB%B3%B4%EC%84%B8%EC%9A%94"
    }
  ]
}
```
</details>

Work ledger: final sources and provenance, representative rendering/navigation/downloads, dependency repair retest, integrity and individual resource cleanup all completed. Build/LSP/new runtime tests are N/A to this report/raw-JPEG task; integrated implementation tests and five independent reviews remain coordinator-owned.
