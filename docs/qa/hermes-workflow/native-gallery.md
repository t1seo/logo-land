# Final native Studio browser QA

Status: **actual native Studio browser checks passed and resources cleaned up**. This read-only extension was assigned by the coordinator in message `msg_07dc8c76e845` under the public sample task. Final native delivery dependency `msg_c795c1a910a4` is ready at revision 47, phase `delivered`, selected `e2`.

The source is the actual native Studio `output/logopia-studio/offcut-hermes-demo/revision-47-214fe913c2d5402d87a73d148d5ed485/index.html`. No production source or canonical state is changed. A new production RED is N/A because this task requests browser verification only; any initial harness failure is retained.

## Additional resources registered before creation

- `output/hermes-preflight/public-sample-task9f041573/native.cjs`: task-owned temporary native browser runner; remove after QA.
- `…/downloads/native-package.zip`, `…/downloads/native-repeat.zip`: exact actual downloads; compare and remove.
- `…/native-before.json`: private read-only source/receipt pins; remove after sanitized comparison is retained.
- Existing registered `…/chrome-profile/`, `…/chrome-artifacts/` and `…/downloads/`: reuse sequentially after prior context closure; close the new owned context and remove these exact directories at final cleanup.
- Native browser child PIDs: record immediately after launch and verify absent after close.
- `…/chrome-native/`: fresh isolated profile for this pass, registered also in the shared public QA resource ledger. Temporary browser internals are confined beneath the already registered `…/chrome-artifacts/` with a task-process-only `TMPDIR`.
- Retain `native-gallery/` screenshots and sanitized verification/cleanup receipts as QA evidence.

## Planned checks

1. Complete: pin final workflow and five original hashes, verify r47/e2 and five actual candidate cards.
2. Complete: actual ZIP download, embedded PNG, direct original, keyboard, 390px viewport, parent comparison, reload/back/repeated download and denied clipboard fallback.
3. Complete: verify canonical byte immutability.
4. Complete: shared exact owned-resource cleanup and absence receipts.

Live model execution, provider cancellation and missing/tampered canonical source experiments are N/A; the coordinator owns live execution and existing tests cover source tampering without changing these originals.

## Observed result

The exact coordinator-provided file URL was opened in headed installed **Google Chrome 152.0.7977.83**, driven by task-local **Playwright 1.63.0** through a fresh isolated profile. [Verification receipt](native-gallery/verification.json) records an exit-0 pass on the first native-gallery run:

- **Five real cards**, snapshot `offcut-hermes-demo · r47`, canonical selection **e2**, package binding `offcut-hermes-demo · r47 · e2` and visible phase **전달 파일 준비됨**.
- `page.waitForEvent('download')`, `page.click('#download-package')` and `download.saveAs(ownedDownloadPath)` produced the exact **711,451-byte ZIP**. The same real package was downloaded and verified **three times**, including after reload.
- Every ZIP SHA256 equals `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04`. Each embedded `logo.png` equals the actual selected e2 original byte-for-byte, SHA256 `882dd3318064ef2573344d9b4dfef5bf9d460f5a9bb0aaf2f585dd2473c887bb`.
- Keyboard skip navigation and Enter on the direct e2 PNG link worked. The original decoded at **1774 × 887** and its hash matched the receipt; back returned to the native page.
- The actual e1→e2 parent comparison opened. Desktop and **390px** mobile views retained exact document width, including the expanded parent comparison.
- A browser-only `NotAllowedError` for clipboard writing exercised the existing denied-copy fallback. The complete draft was selected for manual copy with r47, e2 and its exact SHA256; clearing the local draft preserved canonical selection. This is a controlled permission-failure simulation, not a live operating-system permission claim.
- Real ZIP cancellation returned `canceled`. Completed downloads were deleted; **zero files** remained in the owned download directory after context close.
- **Zero page errors, external requests or failed requests**. Canonical workflow, final snapshot, binding receipt, native gallery HTML and all five canonical original hashes remained unchanged across reload/back/repeated downloads and draft interactions.

Screenshots: [desktop overview](native-gallery/desktop.png), [desktop package](native-gallery/desktop-package.png), [actual parent/child](native-gallery/parent-child.png), [390px overview](native-gallery/mobile.png), [mobile package](native-gallery/mobile-package.png), [mobile parent/child](native-gallery/mobile-parent-child.png). The native page was not modified. Browser-harness corrections discovered on the public sample are documented in [public sample QA](public-sample.md); the native run used the corrected cleanup from the outset.

## Cleanup

[Cleanup receipt](native-gallery/cleanup.json) confirms all shared task-owned browser profiles, temporary tooling/scripts, private pins, downloads and browser artifacts are absent, with **zero owned Chrome processes** and **no opened server/port**. Canonical r47, native gallery HTML and all five originals remain byte-identical. Only intentional screenshots/reports/receipts and ten ignored raw logs remain. This native browser subtask has no outstanding work.
