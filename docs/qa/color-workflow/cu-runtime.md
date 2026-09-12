# Computer Use initialization diagnostic

Date: 2026-09-13 KST. Scope: read-only local runtime diagnosis.

The coordinator's browser initialization requested a missing browser-service module from cache version 26.901.51231 while version 26.903.61454 was present. This confirms a path mismatch, not the component that supplied the old path, nor the cause of the separate native Sky pipe failure. Public documentation provided no initialization option to override that module path. No installation, patch, symlink, service restart or product-code change was attempted.

Three hypotheses were considered: stale requested path (confirmed mismatch), service absent from the whole installation (refuted), and a documented path-reset API (not found in the inspected docs). The official installed CUA package was 0.2.4. Only public package metadata and documentation were inspected.

A subsequent independent worker successfully used native Sky in a fresh REPL without changing the runtime; see [native diagnostic](cu-native.md) and [actual Chrome QA](chrome-live.md). Browser initialization and native Sky are separate paths, so the initial diagnostic is not a current blocker for native Chrome QA. Machine-specific paths and unrelated window metadata are omitted from this public record.
