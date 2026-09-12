# Native Computer Use diagnostic

Date: 2026-09-13 KST. Scope: independent read-only connection check.

An independent Orca worker imported the documented `@oai/sky` API in a fresh Node REPL, successfully called `list_apps()` and `get_app_state({app: "com.google.Chrome"})`, and received Chrome accessibility state. It did not inspect unrelated page content beyond the connection check or interact with tabs. The missing browser-initialization module did not prevent this separate native connection.

Three hypotheses were examined: changed service/client state (observed, cause unconfirmed); incompatible high-level CUA documentation versus the default export (the attempted `cua.listApps()` was absent, consistent with the inspected type declaration); and the missing browser module necessarily blocking Sky (refuted by the successful Sky calls). Installed public package versions were Sky 0.6.32 and CUA 0.2.4; no compatibility conclusion was inferred solely from version numbers.

The root REPL still failed its bounded native retry. A fresh Orca Chrome QA worker then connected and completed the actual application checks in [chrome-live.md](chrome-live.md). No browser profile, credentials, private socket protocol, runtime patch, service restart or installation was used. No product bug was fixed, so no red/green product-test claim applies. Machine-specific process paths and unrelated window titles have been removed from this public record.
