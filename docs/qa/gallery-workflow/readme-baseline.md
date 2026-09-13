# README sample navigation baseline

Captured before documentation edits on 2026-09-13 KST, source `06b94c41922973fc98392fadde25fff9aa498f6e`.

| Source | SHA-256 | Observed sample visibility |
|---|---|---|
| `README.md` | `e3910e4a691ce1e555e8aa3461c2a01ced90f5e1c6014f4bdc21622fd89ccfec` | Seven badge images and current identity image; zero inline sample images. |
| `README.ko.md` | `a0746d3f4df7cf036eabfdbffc07b7c0b9c94b738a63d13b1da27b6ee493cb11` | Same image structure; zero inline sample images. |
| `docs/samples/README.md` | `7b870dab04532214b6dcaf8f42cdb3d73ff42225bb0169cc9dcd9e88bbd50d46` | Text table linking ten individual sample pages; no images. |
| `docs/app-icons/README.md` | `c4e85865f13ad3ba8eaf0e5de9d6b7d491a05f629a172893251f3c9b2da117cc` | Text sections linking individual icon pages; no images. |

Static navigation: README → category index → individual sample page → original PNG. The sample first becomes visible after two navigation steps. The new requirement, at least six directly visible representative sample images and direct original links in each root README, fails on this baseline (actual count zero).

Method: read exact Markdown and image/link targets using Ruby with SHA-256; no browser or runtime behavior is claimed by this baseline. Final actual Chrome navigation is a separate T4 check. No production files changed, no tests added for this reversible documentation layout change, and no servers, temporary files or browser resources were created.
