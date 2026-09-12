# Color suggestion providers

Local proposals work without Leonardo. The host may use an already-connected Leonardo capability as an optional source of suggestions. This is a palette workflow, not an image-generation provider. Helper commands and input schemas are documented in [project-files.md](project-files.md).

## Choose the source honestly

| Situation | Action | Evidence |
|---|---|---|
| User delegates ordinary color choice | Make an assistant proposal or use local harmony | Actual source, selected-by and rationale. |
| Actual image supplied as a color reference | Use local reference extraction | Saved reference ID/hash, profile treatment and scope. |
| Leonardo is already exposed and useful | Make one suggestion attempt through the live schema | Actual tool name, arguments and returned result/call identity. |
| Leonardo absent, errors, or returns invalid output | Record that outcome; continue with assistant/local candidates | Unavailable/error/invalid reason and the fallback's true source. |

Do not call a fallback `leonardo`, fabricate an external response, or use an unavailable-tool case as evidence of a live integration. Keep failure history distinct from the successfully selected palette's source evidence. If the local calculation engine is missing, report `color_engine_unavailable`; an assistant can still discuss an explicit proposal, but must not claim local calculation or conformance occurred.

Do not install packages, invoke `npx`, add MCP configuration or connect accounts automatically. A request for a logo authorizes the existing workflow, not new services. This release bundles no Pantone data, paid palette API or second runtime.

## Already-connected Leonardo

The pinned [Adobe MCP documentation](https://github.com/adobe/leonardo/blob/eb6481da40df27654ac8efa42038007f6fad2431/packages/mcp/README.md) describes four tools:

| Tool | Documented purpose |
|---|---|
| `generate-theme` | Contrast-driven theme from color/background definitions and lightness. |
| `create-palette` | Interpolated scale from color keys and a requested step count. |
| `check-contrast` | Foreground/background contrast guidance. |
| `convert-color` | Color-format conversion. |

Inspect the host's actual tool schema before calling. Prefer `create-palette` for companion exploration; use `generate-theme` when target surface/contrast is relevant. A scale is not semantic brand judgment or proof of anchor preservation. Choose usable returned swatches for the logo, label roles and explain why they fit the brief. Do not assume the MCP includes every feature of the Leonardo web app.

Keep provider requests small and omit unrelated brand/reference data. Request HEX output where supported. Normalize returned HEX and deduplicate through the same local typed candidate boundary as assistant suggestions, applying every user constraint. An interpolated near-green cannot replace locked `#247A52`; a third distinct swatch cannot escape a two-color cap. Do not accept malformed CSS/alpha values, missing locks, invalid metadata or a caller-supplied measurement pass. Reject an invalid suggestion and use the local route, keeping the reason.

Use at most one suggestion attempt per selection request rather than retrying indefinitely. An actual optional `check-contrast` call may supplement advice for a named foreground/surface pair; use explicit WCAG 2 when comparing with the local report. Provider contrast output never overrides the local sampled raster policy, required-color evidence or export gate.

## Source and attribution

Tool-purpose and contrast-pair guidance is summarized and adapted from Adobe's [Leonardo colors skill](https://github.com/adobe/leonardo/blob/eb6481da40df27654ac8efa42038007f6fad2431/skills/leonardo-colors/SKILL.md) and MCP documentation at commit `eb6481da40df27654ac8efa42038007f6fad2431`, licensed [Apache-2.0](https://github.com/adobe/leonardo/blob/eb6481da40df27654ac8efa42038007f6fad2431/LICENSE). Logo Land adds optional availability, one-attempt fallback, exact local constraints and artifact verification; it does not copy upstream installation instructions or implementation. Full attribution scope is in [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md).
