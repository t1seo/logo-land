# Hermes documentation verification

Documentation-only work for `task_1fc8a276d869`, dispatch `ctx_2cddb9c52220`, in the shared Logopia checkout. The implementation plan is `plans/logopia-hermes-workflow.md`. No source Python, manifest, lockfile, native model/image call, profile setting or commit is owned by this task.

## Work and named dependencies

1. Completed: pin both READMEs, all sixteen direct legacy originals and the pre-edit layout failures.
2. Completed: update the English/Korean entry points, Hermes guide and unreleased 0.8.0 notes.
3. Completed: receive the coordinator's final native-delivery receipt and the public sample worker's final child/ZIP/status receipt; only then add the actual example and outcome.
4. Completed: check local links/anchors, bilingual parity, legacy bytes, HTTP bodies and native PNG hashes; inspect both rendered layouts if an existing renderer is available.
5. Completed: remove owned temporary resources, verify their absence and report the final result.

Native delivery and final public sample readiness are named dependencies, not inferred from a running process or an existing partial directory. The supplied baseline says T2 passed 907 tests and T3 is still root-owned; this worker does not claim those as its own test execution.

## Resource register (before creation)

- Owned temporary directory: `/tmp/logopia-docs-ctx_2cddb9c52220/`. Its initial absence will be checked before creation. It may contain initial document snapshots, a file/hash inventory, bounded HTTP response headers/bodies, server logs, a local-only document-check script, and rendered README previews/screenshots. These are temporary QA resources, not public samples or production tests.
- Owned HTTP listener reservation: `127.0.0.1:8811`, serving this checkout only. Port absence will be checked before launch; the actual PID and process command will be recorded immediately after launch. No other listener may be stopped.
- Tool installations: none planned. Only already available interpreters/renderers may be used; no user Chrome setting/profile changes.
- Kept output: this report and the authorized public documentation/release notes. No private workflow session is copied into documentation.

## Initial pin and failures

The inventory will be recorded before the first edit of any public entry-point document.

PIN captured 2026-09-14T16:34:13.409Z. Both README direct-link lists contain the same 16 originals, in the same order. Every file exists and has nonzero bytes.

| Original path | Bytes | SHA-256 |
|---|---:|---|
| `docs/showcase/2026-09-white/images/01-luma.png` | 798465 | `3b49d26a6d5fba9e4f69dad637a0c1e7f39583643e46223c4193c79c77b24225` |
| `docs/showcase/2026-09-white/images/02-loop-lab.png` | 729678 | `57d8e07b8ab0ae657c006a7febe787365597b2d8db469ee383cc994ac9843ccd` |
| `docs/showcase/2026-09-white/images/03-goyo.png` | 740692 | `2b488bc638ca055861f38e07267e86f8c402bc1fa7953dd844c02c2dce317d5c` |
| `docs/showcase/2026-09-white/images/04-bread-bloom.png` | 833781 | `5120edfaba615320c386d98bfcfb44f6529bded5f1d91131908fb91ca98a6a00` |
| `docs/showcase/2026-09-white/images/05-kite.png` | 629706 | `22985e993c4574dedeb494ba83a7eced4856ffc3e6437958bcdb42361950f342` |
| `docs/showcase/2026-09-white/images/06-miso.png` | 969040 | `c513aa948995d94316627cf37ec8076956defb71df89060e211d54c807e03adf` |
| `docs/showcase/2026-09-white/images/07-northline.png` | 677160 | `29a4b49efe2af236b618d799d21b2d1659eca5a501097d5bea0ceda7574d7f89` |
| `docs/showcase/2026-09-white/images/08-mulgyeol.png` | 752277 | `29d26d6e674a8f3845f093e2d30a3c5239f5062a5be1e2dd5c48efcbe8d6c6fa` |
| `docs/showcase/2026-09-white/images/09-fern.png` | 853222 | `9610b4389a7218cf46529a0f3b38e10df428e30ef8518fc518782162f535ed50` |
| `docs/showcase/2026-09-white/images/10-nova-notes.png` | 712661 | `dbd2e8bf107d1001715d9f9fd23eae16d883dccf97119c76c7849ad729e5f771` |
| `docs/showcase/2026-09-white/images/11-reading-owl.png` | 939745 | `691097f42f608f1e908be3a3ac3712f0a715dc2dce356111b4db420e1479b52a` |
| `docs/showcase/2026-09-white/images/12-weather.png` | 716106 | `10a955d2e0a07e61353a7092d5221227f6960665b1ce74a8bbdc609f83a24a77` |
| `docs/showcase/2026-09-white/images/13-flow.png` | 758554 | `158ec3f77d7a6afb7ff26d70f260ef15334180d590d15a4f0fea56788dff4041` |
| `docs/showcase/2026-09-white/images/14-notes.png` | 772414 | `5fac76281959aaf4b503590870e09e0a5ec3ef301ff3877f6ca6eed83f5acc36` |
| `docs/showcase/2026-09-white/images/15-cloud.png` | 1103327 | `d215022d9a033ee69ba2488d6e7493cf0b3ee0f8eb96cf67b2983674403a3921` |
| `docs/showcase/2026-09-white/images/16-sprout.png` | 669198 | `ce5d6629c5bf71dd5cb9eff11c22ae3349df8dd7f63a409eefacde118e6adb46` |

First RED checks, before entry-point edits:

```json
[
  {
    "file": "README.md",
    "sha256": "3fc39506749f0accf3e9370a7f34410acbb1263419c6a810a1a87b98a6bdae1a",
    "bytes": 11359,
    "hermesLine": 66,
    "lastOriginalLine": 60,
    "hermesBeforeLegacy": false,
    "directHermesExampleCount": 0
  },
  {
    "file": "README.ko.md",
    "sha256": "adeae6da39f85b26afe889d246fa90795eb6d0bc3fcfdeb65d7813b4bedc5a18",
    "bytes": 12605,
    "hermesLine": 66,
    "lastOriginalLine": 60,
    "hermesBeforeLegacy": false,
    "directHermesExampleCount": 0
  }
]
```

Both required checks fail as expected: the Hermes section is below the sixteenth original, and there is no direct actual Hermes PNG example. These are retained failures, not skipped assertions.

Protected baseline:

```json
[
  {
    "file": ".codex-plugin/plugin.json",
    "bytes": 1768,
    "sha256": "a5c05e88df05eac399a6105592f83c845904f0dd1bc61f6445aa4f8f7bcdef21"
  },
  {
    "file": "pyproject.toml",
    "bytes": 1723,
    "sha256": "84161b724692b7ea54fb091360a3b3a57074910c4fc8887e4430d3b9ec10a990"
  },
  {
    "file": "uv.lock",
    "bytes": 65010,
    "sha256": "6ba5fda3da53b5f19fa10a5fbfbb20dcd854949c49437b6ce6f9a91704772a21"
  },
  {
    "file": ".omo/drafts/logo-land-next-capability.md",
    "bytes": 19599,
    "sha256": "650c8d31b7e0c524ec818941e3e61b65e4f79c9c2d4ee54d8fb715056faa2eea"
  },
  {
    "file": ".omo/drafts/logo-land-next-delivery.md",
    "bytes": 16530,
    "sha256": "bdcafac3287afaf27a5908fde1dfcffb22981cbaa54102abd360897e6f316a7a"
  },
  {
    "file": ".omo/drafts/logo-land-next-metis.md",
    "bytes": 17665,
    "sha256": "af8c6e61497651195a5c884ce5af52fb9bb2246e6acdcd0279e128562d4133fa"
  },
  {
    "file": ".omo/drafts/logo-land-next-tools.md",
    "bytes": 14664,
    "sha256": "e8afad487b95bceb7d60a517156882dee5a5639b2f5a86c43d15486c01ed6612"
  }
]
```

Initial dirty worktree, including the coordinator's existing draft edits:

```text
 M .codex-plugin/plugin.json
 M README.ko.md
 M README.md
 M docs/README.ko.md
 M docs/README.md
 M pyproject.toml
 M uv.lock
?? .omo/drafts/hermes-design-ux-research.md
?? .omo/drafts/hermes-logopia.md
?? .omo/drafts/hermes-plan-gap.md
?? .omo/drafts/hermes-repo-research.md
?? .omo/drafts/hermes-runtime-research.md
?? .omo/drafts/logo-land-next-capability.md
?? .omo/drafts/logo-land-next-delivery.md
?? .omo/drafts/logo-land-next-metis.md
?? .omo/drafts/logo-land-next-tools.md
?? docs/hermes.ko.md
?? docs/hermes.md
?? docs/qa/hermes-workflow/
?? docs/research/hermes-design-workflow.md
?? integrations/
?? plans/logopia-hermes-workflow.md
?? tests/hermes/
```

## HTTP server registration

Port 8811 was absent (`lsof -nP -iTCP:8811 -sTCP:LISTEN` exited 1) before launch. The owned loopback-only server has an automatic 1,800-second deadline.

```json
{
  "parentPid": 86630,
  "serverPid": 86634,
  "bind": "127.0.0.1",
  "port": 8811,
  "cwd": "/Users/cillian/Documents/Github/Projects/logo-generator",
  "deadlineSeconds": 1800,
  "command": "python3 -u -m http.server 8811 --bind 127.0.0.1 --directory /Users/cillian/Documents/Github/Projects/logo-generator"
}
```

## First HTTP and content checks

Both required commands were run against the actual loopback server, using `curl -i --max-time 15 http://127.0.0.1:8811/README.md` and its `README.ko.md` counterpart; headers and bodies were captured separately before further edits.

```json
{
  "rows": [
    {
      "file": "README.md",
      "status": "HTTP/1.0 200 OK",
      "contentLength": 11594,
      "sha256": "abaf11868a3fd4c73041cc1cd6bf0e5785001d7d8d519ef09f14554660ec9f66",
      "exactSavedBody": true,
      "hermesBeforeLegacy": true
    },
    {
      "file": "README.ko.md",
      "status": "HTTP/1.0 200 OK",
      "contentLength": 12895,
      "sha256": "080817a0372ba930f2d3a10eb17bcc13a406caa150741e98a1a813596f8f2c49",
      "exactSavedBody": true,
      "hermesBeforeLegacy": true
    }
  ],
  "response200AloneRejected": true
}
```

The first static pass checked 245 rendered link/image targets, local file existence, referenced anchors, three bilingual target sets, eleven Hermes feature pairs, unchanged legacy originals, release badges, internal skill names and MIT credits. All passed. Direct actual sample links are still a named pending dependency, not counted as passing in this intermediate check. Missing files, missing anchors, malformed links and active markup were rejected by deliberately failing checker fixtures; quoted instruction-like text remained inert. No public document failure was hidden or relaxed.

## Repeated HTTP interruption and recovery

Two rate-limited GETs were deliberately interrupted with SIGINT, then a full bounded fetch recovered the exact original bytes. This tests document download recovery, not provider cancellation.

```json
{
  "attempts": [
    {
      "attempt": 1,
      "code": null,
      "signal": "SIGINT",
      "elapsedMs": 455,
      "partialBytes": 0
    },
    {
      "attempt": 2,
      "code": null,
      "signal": "SIGINT",
      "elapsedMs": 453,
      "partialBytes": 0
    }
  ],
  "recovery": {
    "status": "HTTP/1.0 200 OK",
    "bytes": 798465,
    "sha256": "3b49d26a6d5fba9e4f69dad637a0c1e7f39583643e46223c4193c79c77b24225",
    "exactSavedBody": true
  },
  "missingPathStatus": "HTTP/1.0 404 File not found",
  "unchangedFile": true
}
```

The first cancellation captures above contain zero written bytes because curl output was buffered. To verify a partial-body interruption rather than infer it, the same two bounded GETs were repeated with `--no-buffer`; both then captured actual PNG bytes before SIGINT. The original first captures remain recorded.

```json
{
  "attempts": [
    {
      "attempt": 1,
      "code": null,
      "signal": "SIGINT",
      "partialBytes": 1212,
      "partialBodyBytes": 1024
    },
    {
      "attempt": 2,
      "code": null,
      "signal": "SIGINT",
      "partialBytes": 1024,
      "partialBodyBytes": 836
    }
  ],
  "recovery": {
    "status": "HTTP/1.0 200 OK",
    "bytes": 798465,
    "sha256": "3b49d26a6d5fba9e4f69dad637a0c1e7f39583643e46223c4193c79c77b24225",
    "unchangedFile": true
  }
}
```

## Dependency checkpoint

Coordinator message `msg_824c6fcaeeaf` reports the real e2 child at revision 44, 1774 × 887, SHA-256 `882dd3318064ef2573344d9b4dfef5bf9d460f5a9bb0aaf2f585dd2473c887bb`, exact parent e1. Both model critiques pass and the coordinator visually checked the restored symbol-to-word gap. This is review evidence, not a delivery receipt. Final choose/ZIP and the public e2 copy remain pending at this checkpoint.

The existing repository `markdown-it-py` renderer is available; no package was installed. Planned layout QA uses the existing Chrome binary in headless mode with owned temporary profiles under the registered scratch directory. It does not inspect or change the user's Chrome profile and is separate from the coordinator's full Chrome QA.

## Final native dependency received

The coordinator's final receipt was received before adding native outcome or final-package claims. Its canonical copy and independent binding receipt agree on r47, delivered, selected e2. The documentation worker performed read-only parsing; native inference and delivery verification remain attributed to the coordinator.

```json
{
  "message": "msg_cfd1e8da46b8",
  "workflowId": "offcut-hermes-demo",
  "revision": 47,
  "phase": "delivered",
  "selectedId": "e2",
  "sourceReceipt": "output/hermes-demo/final-binding.json",
  "originals": [
    {
      "id": "c1",
      "parentId": null,
      "sha256": "30e46b31716db37cfa51d7fb2f5406e48275727c9ccaef6d54a0d1ee4a2a878f",
      "width": 1774,
      "height": 887
    },
    {
      "id": "c2",
      "parentId": null,
      "sha256": "f7962dee46e27c406039da75e1bd314322e4cd3510cfc8d9686d5cd64a3961c3",
      "width": 1254,
      "height": 1254
    },
    {
      "id": "c3",
      "parentId": null,
      "sha256": "68734a451c89f499e54f5366e5fe04cc49d6b58ca329604373ee6657c9720aea",
      "width": 1254,
      "height": 1254
    },
    {
      "id": "e1",
      "parentId": "c1",
      "sha256": "08196269c02184cd99237a0e2a8306e039f1d13eac0a9261ce652f6c5b0a6560",
      "width": 1774,
      "height": 887
    },
    {
      "id": "e2",
      "parentId": "e1",
      "sha256": "882dd3318064ef2573344d9b4dfef5bf9d460f5a9bb0aaf2f585dd2473c887bb",
      "width": 1774,
      "height": 887
    }
  ],
  "zipSha256": "0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04",
  "repeatDeliveryNoInferenceOrMutation": true
}
```

The public sample-ready dependency is still pending at this checkpoint. The documentation will preserve the full c1 → e1 → e2 lineage and the e1 preservation failure; the README pair will compare the initial and final originals, not imply that e2 was a direct edit of c1.

## Public sample dependency received

Sample worker `ctx_ae88e23a670f` sent `msg_f8ad630b3982` (sample-ready, r47). Before adding links, all five public PNG hashes were compared to the coordinator's final workflow and the public ZIP hash was compared to its delivery receipt. Both public README files, the offline HTML page and actual guide exist. Native c1/e2 links and the ZIP were added only after this receipt and those byte checks.

## Release-page link preparation

Coordinator message `msg_c38d67319186` requires absolute GitHub v0.8.0 links because these notes will be passed to `gh --notes-file`. Each future-tag URL was mapped to an existing checkout file before replacement. The notes explicitly label those URLs as publication-dependent; this task does not claim they currently return HTTP 200. Root owns publication and the final remote tag/link check. Release badges remain v0.7.0.

```json
[
  {
    "url": "https://github.com/t1seo/logopia/blob/v0.8.0/docs/hermes-demo/README.md",
    "localTarget": "docs/hermes-demo/README.md"
  },
  {
    "url": "https://github.com/t1seo/logopia/blob/v0.8.0/docs/hermes-demo/README.md",
    "localTarget": "docs/hermes-demo/README.md"
  },
  {
    "url": "https://github.com/t1seo/logopia/blob/v0.8.0/docs/qa/hermes-workflow/native-run.md",
    "localTarget": "docs/qa/hermes-workflow/native-run.md"
  },
  {
    "url": "https://github.com/t1seo/logopia/blob/v0.8.0/docs/hermes.md",
    "localTarget": "docs/hermes.md"
  },
  {
    "url": "https://github.com/t1seo/logopia/blob/v0.8.0/docs/hermes.ko.md",
    "localTarget": "docs/hermes.ko.md"
  },
  {
    "url": "https://github.com/t1seo/logopia/blob/v0.8.0/integrations/hermes/skills/director/references/ip-as-logo.LICENSE",
    "localTarget": "integrations/hermes/skills/director/references/ip-as-logo.LICENSE"
  },
  {
    "url": "https://github.com/t1seo/logopia/blob/v0.8.0/THIRD_PARTY_NOTICES.md",
    "localTarget": "THIRD_PARTY_NOTICES.md"
  }
]
```

## Headless QA harness investigation

First failure retained: both original Chrome `spawnSync` calls produced a complete screenshot and DOM but reported `error=ETIMEDOUT`, despite `status=0`, at the 30-second command deadline. They are not counted as clean command exits.

Hypotheses: (1) missing or slow document images keep rendering incomplete; distinguish using actual DOM image completion and dimensions, (2) the owned Chrome parent remains active after rendering; distinguish by exact profile process presence, (3) inherited stdout/stderr pipes remain open in a descendant after the parent exits; distinguish by a bounded inherited-descriptor reproduction and direct-file-descriptor rerun. Both actual DOMs show all 18 document PNGs loaded and 1280px document width, refuting incomplete image loading. No Chrome command containing either owned profile path remained after the first calls.

The debug resource journal is this authorized report, not an extra repository file. Before creation: the registered scratch directory may receive descriptor-reproduction logs/PID receipts and final DOM/screenshot/log captures. Each reproduction descendant has a 1.5-second self-termination timer. No debugger port, source edit, production test, profile setting change or new agent is used.

The descriptor-only reproduction was RED → GREEN → RED when toggling pipes/file descriptors:

```json
[
  {
    "mode": "pipes",
    "status": 0,
    "error": "ETIMEDOUT",
    "elapsedMs": 303
  },
  {
    "mode": "files",
    "status": 0,
    "error": null,
    "elapsedMs": 76
  },
  {
    "mode": "pipes",
    "status": 0,
    "error": "ETIMEDOUT",
    "elapsedMs": 302
  }
]
```

This proves the reproduction mechanism only. Both actual Chrome reruns with direct log/DOM file descriptors still returned `ETIMEDOUT` at about 30 seconds, so inherited pipe handling is **not a confirmed cause of the browser shutdown delay**. No browser/application source or configuration was changed to hide this result. The optional headless CLI clean-exit check remains a limitation; full interactive Chrome QA belongs to the coordinator. No additional agent was spawned, as the task explicitly prohibits it.

## Final document and HTTP gates

Content/link gate: **PASS**, 9 public documentation files, 274 rendered href/src targets, three bilingual link sets and eleven feature pairs. The nine public files are:

- `README.md`: 70 targets, 0 errors.
- `README.ko.md`: 70 targets, 0 errors.
- `docs/README.md`: 34 targets, 0 errors.
- `docs/README.ko.md`: 34 targets, 0 errors.
- `docs/hermes.md`: 12 targets, 0 errors.
- `docs/hermes.ko.md`: 12 targets, 0 errors.
- `CHANGELOG.md`: 19 targets, 0 errors.
- `docs/releases.md`: 14 targets, 0 errors.
- `docs/qa/hermes-workflow/release-notes.md`: 9 targets, 0 errors.

All 16 prior direct-original paths occur once as links in each README, in the original order, and every pinned size/hash remains identical. All 18 prior explicit anchors in each README remain; `hermes-workflow` is the single added explicit anchor.

```json
[
  {
    "file": "README.md",
    "preservedCount": 18,
    "anchors": [
      "logo-land",
      "logopia",
      "samples",
      "ten-real-samples",
      "transparent-background-logos",
      "get-started",
      "use-the-repository-directly",
      "image-generation-and-the-file-helper",
      "install-as-a-codex-plugin",
      "releases-and-versioning",
      "use-natural-language",
      "six-app-icon-directions",
      "choose-colors-in-four-ways",
      "pair-a-symbol-with-exact-lettering",
      "eight-logo-types",
      "revisions-and-delivery",
      "what-you-can-make",
      "research-and-verification"
    ],
    "newAnchors": [
      "hermes-workflow"
    ],
    "missing": []
  },
  {
    "file": "README.ko.md",
    "preservedCount": 18,
    "anchors": [
      "logo-land-로고랜드",
      "logopia",
      "샘플",
      "샘플-10개",
      "투명-배경-로고",
      "시작하기",
      "저장소에서-바로-사용",
      "이미지-생성과-파일-보조-도구의-차이",
      "codex-플러그인으로-설치",
      "릴리스와-버전-관리",
      "대화로-사용하기",
      "앱-아이콘-방향-여섯-가지",
      "네-가지-방식으로-색상-정하기",
      "심볼과-정확한-글자-조합하기",
      "로고-유형-8가지",
      "수정과-전달-파일",
      "만들-수-있는-것",
      "조사와-제작-근거"
    ],
    "newAnchors": [
      "hermes-workflow"
    ],
    "missing": []
  }
]
```

Final HTTP gate: **PASS**. The exact required `curl -i --max-time 15` commands were repeated after sample readiness and the final README edits. Each row below is an actual HTTP 200 response whose body equals the current saved file, not merely a successful status code. Native PNG/ZIP hashes also equal the root receipt; PNG signature and dimensions match.

| File | HTTP | Bytes | SHA-256 |
|---|---|---:|---|
| `README.md` | 200, exact body | 12538 | `077c932532866e4dba4fe247bdfaa0dee4f765a129dbc20c9f02bab3e616ca86` |
| `README.ko.md` | 200, exact body | 13918 | `d05d87e663dfad1c848349639902e5eca91968d9a9201d8c4b9981428d5886be` |
| `docs/hermes-demo/originals/c1.png` | 200, exact body | 739942 | `30e46b31716db37cfa51d7fb2f5406e48275727c9ccaef6d54a0d1ee4a2a878f` |
| `docs/hermes-demo/originals/c2.png` | 200, exact body | 755315 | `f7962dee46e27c406039da75e1bd314322e4cd3510cfc8d9686d5cd64a3961c3` |
| `docs/hermes-demo/originals/c3.png` | 200, exact body | 752532 | `68734a451c89f499e54f5366e5fe04cc49d6b58ca329604373ee6657c9720aea` |
| `docs/hermes-demo/originals/e1.png` | 200, exact body | 788171 | `08196269c02184cd99237a0e2a8306e039f1d13eac0a9261ce652f6c5b0a6560` |
| `docs/hermes-demo/originals/e2.png` | 200, exact body | 714393 | `882dd3318064ef2573344d9b4dfef5bf9d460f5a9bb0aaf2f585dd2473c887bb` |
| `docs/hermes-demo/delivery/logo-package.zip` | 200, exact body | 711451 | `0d1a4c2266ad6f04b3d1b78ab32c41b89ed5bd6c3b0c0d514fd580a9513d7c04` |
| `docs/hermes-demo/delivery/brand-guide.md` | 200, exact body | 10559 | `c2dbb61367f5a16b732660de1289b4799e0b4eb356434f0a86431e1d9259699a` |
| `docs/hermes-demo/index.html` | 200, exact body | 984969 | `148ba37ffc2795285386e1053d92703c0f4f17a265573fcb4d4d56a0994beed6` |
| `docs/hermes.md` | 200, exact body | 6983 | `056cd7d63378855014ba63be8e08a171ed04abc8d1d3d6134381a066386341c7` |
| `docs/hermes.ko.md` | 200, exact body | 8308 | `182c1e19867db116c42a2b294a0456658657f288ba9eca79faacd8d1e9694fac` |

The final README bodies both place the Hermes anchor and both direct c1/e2 links before the legacy showcase. The five-original sample retains c1 → e1 → e2 and the e1 preservation failure. Actual native behavior is attributed to the coordinator's final receipt and `native-run.md`; this worker made no model/image call or profile change.

## Rendered layout inspection

Both English and Korean final screenshots were opened and visually inspected. The compact pair, clear initial/refined labels, explicit intermediate failure and both setup routes are readable above the sixteen-logo showcase. The existing `markdown-it-py` renderer and temporary GitHub-like CSS were used; this is an actual local Chrome rendering, not a claim about live GitHub or the user's full Chrome session.

```json
[
  {
    "name": "README",
    "pid": 98010,
    "status": 0,
    "error": "ETIMEDOUT",
    "elapsedMs": 30032,
    "screenshotExists": true,
    "layout": {
      "viewportWidth": 1280,
      "documentWidth": 1280,
      "hermesY": 506.875,
      "firstLegacyY": 1554.875,
      "sampleImages": [
        {
          "src": "docs/hermes-demo/originals/c1.png",
          "naturalWidth": 1774,
          "naturalHeight": 887,
          "renderedWidth": 400,
          "y": 743.875
        },
        {
          "src": "docs/hermes-demo/originals/e2.png",
          "naturalWidth": 1774,
          "naturalHeight": 887,
          "renderedWidth": 400,
          "y": 743.875
        }
      ],
      "documentImages": 18,
      "allImagesLoaded": true,
      "hermesBeforeLegacy": true
    }
  },
  {
    "name": "README.ko",
    "pid": 98009,
    "status": 0,
    "error": "ETIMEDOUT",
    "elapsedMs": 30029,
    "screenshotExists": true,
    "layout": {
      "viewportWidth": 1280,
      "documentWidth": 1280,
      "hermesY": 506.875,
      "firstLegacyY": 1530.875,
      "sampleImages": [
        {
          "src": "docs/hermes-demo/originals/c1.png",
          "naturalWidth": 1774,
          "naturalHeight": 887,
          "renderedWidth": 400,
          "y": 719.875
        },
        {
          "src": "docs/hermes-demo/originals/e2.png",
          "naturalWidth": 1774,
          "naturalHeight": 887,
          "renderedWidth": 400,
          "y": 719.875
        }
      ],
      "documentImages": 18,
      "allImagesLoaded": true,
      "hermesBeforeLegacy": true
    }
  }
]
```

The 18 document PNGs loaded at their actual original dimensions; the two new images each display at 400px wide, and the document width equals its 1280px viewport. The reported legacy coordinate is the inline original link's bounding box, not the top of its image. Both DOM/screenshot outputs are valid observation evidence, while the clean-exit check is explicitly failed above. Final screenshots are temporary QA resources and will be removed after inspection.

## Adversarial and scope receipt

- Missing file: the actual server returns HTTP 404; the local checker rejects a missing destination.
- Missing fragment: the checker rejects a nonexistent anchor even when the underlying file exists.
- Malformed Markdown and active script/scheme fixture: rejected; quoted instruction-like examples remain inert.
- Misleading success: a synthetic HTTP 200 with the wrong body was rejected; Chrome status 0 plus an `ETIMEDOUT` error was recorded as a failed command exit.
- Repeated cancellation: two actual partial-body GETs were interrupted with SIGINT, then an unchanged original recovered at the expected SHA-256.
- Stale/publication claims: Release badge remains v0.7.0; 0.8.0 and the prepared absolute tag URLs remain explicitly unreleased/publication-dependent. No live HTML hosting, human approval or numerical professional superiority is claimed.
- Dirty worktree: the seven protected manifest/lock/draft files match the initial hashes. Root-native and public-sample worker changes are preserved. No baseline file was deleted.
- Provider interruption: not applicable to this documentation task; source-linked coordinator native evidence covers its actual timeout and critique-only recovery.
- Source build, production tests and code LSP diagnostics: not applicable to this Markdown-only change; no production test was created, deleted or weakened. The supplied 907-test result is a coordinator/T2 receipt, not this worker's execution.

## Cleanup and final outcome

The coordinator reviewed the final entry-point structure, direct c1/e2 pair, guide and absolute release-note links with no new issue (`msg_64551a3fd342`). It explicitly requested preservation of the first Chrome timeout evidence and cleanup of proven owned descendants only. No broader test or source change was made.

The registered loopback server was terminated only after matching its exact PID and command; its wrapper settled with exit 0. Both known final Chrome parent PIDs and all three descriptor-fixture child PIDs are absent, and no command uses either owned Chrome profile path. Unscoped/shared browser processes were not terminated. The complete registered scratch directory, including document snapshots, response bodies, scripts, Chrome profiles, screenshots and logs, was removed after receipts were transcribed. No tool was installed, no default profile/settings were edited and no private session was published.

```json
{
  "timestamp": "2026-09-14T16:49:22.051Z",
  "server": [
    {
      "pid": 86634,
      "absent": true
    },
    {
      "pid": 86630,
      "absent": true
    }
  ],
  "knownFinalChromeAndProbePids": [
    {
      "pid": 98009,
      "absent": true
    },
    {
      "pid": 98010,
      "absent": true
    },
    {
      "pid": 97764,
      "absent": true
    },
    {
      "pid": 97766,
      "absent": true
    },
    {
      "pid": 97768,
      "absent": true
    }
  ],
  "ownedChromeProfileProcesses": 0,
  "port8811ListenerAbsent": true,
  "tempRoot": "/tmp/logopia-docs-ctx_2cddb9c52220",
  "tempRootAbsent": true,
  "temporaryEntryCountRemoved": 682,
  "toolInstalls": 0,
  "protectedFiles": [
    {
      "file": ".codex-plugin/plugin.json",
      "sha256": "a5c05e88df05eac399a6105592f83c845904f0dd1bc61f6445aa4f8f7bcdef21",
      "unchanged": true
    },
    {
      "file": "pyproject.toml",
      "sha256": "84161b724692b7ea54fb091360a3b3a57074910c4fc8887e4430d3b9ec10a990",
      "unchanged": true
    },
    {
      "file": "uv.lock",
      "sha256": "6ba5fda3da53b5f19fa10a5fbfbb20dcd854949c49437b6ce6f9a91704772a21",
      "unchanged": true
    },
    {
      "file": ".omo/drafts/logo-land-next-capability.md",
      "sha256": "650c8d31b7e0c524ec818941e3e61b65e4f79c9c2d4ee54d8fb715056faa2eea",
      "unchanged": true
    },
    {
      "file": ".omo/drafts/logo-land-next-delivery.md",
      "sha256": "bdcafac3287afaf27a5908fde1dfcffb22981cbaa54102abd360897e6f316a7a",
      "unchanged": true
    },
    {
      "file": ".omo/drafts/logo-land-next-metis.md",
      "sha256": "af8c6e61497651195a5c884ce5af52fb9bb2246e6acdcd0279e128562d4133fa",
      "unchanged": true
    },
    {
      "file": ".omo/drafts/logo-land-next-tools.md",
      "sha256": "e8afad487b95bceb7d60a517156882dee5a5639b2f5a86c43d15486c01ed6612",
      "unchanged": true
    }
  ],
  "otherWorkersExistingFilesChanged": [
    "docs/qa/hermes-workflow/native-run.md",
    "docs/qa/hermes-workflow/public-sample.md"
  ],
  "baselineFilesDeleted": [],
  "ownedDocumentationPaths": [
    "README.md",
    "README.ko.md",
    "docs/README.md",
    "docs/README.ko.md",
    "docs/hermes.md",
    "docs/hermes.ko.md",
    "CHANGELOG.md",
    "docs/releases.md",
    "docs/qa/hermes-workflow/release-notes.md",
    "docs/qa/hermes-workflow/docs.md"
  ]
}
```

**Documentation task complete.** The content/link/HTTP/hash gates pass, the actual initial/refined layout was visually inspected, both named native/public-file dependencies were received, and the owned resources are absent. The optional headless clean-exit limitation remains recorded rather than presented as a pass; the coordinator owns full interactive Chrome and publication verification. Release v0.7.0 and development 0.8.0 terminology remain distinct.
