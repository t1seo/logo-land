---
name: director
description: Direct a native Logopia logo workflow from a brief through distinct candidates, pixel critiques, targeted revisions and verified original PNG delivery. Use with logopia_start and logopia_action.
---

# Logopia director

Use the conversation to direct the work. Reuse the supplied product, audience,
personality and use case. Preserve `exact_text` verbatim, including spaces, case,
punctuation and Hangul. Ask only for missing information that changes the design.
Read [craft guidance](references/craft.md) before creating a brief; read
[IP guidance and credit](references/ip.md) for a character request.

Call `logopia_start` with a portable `workflow_id` and a `brief`: `name`,
`exact_text`, `product`, `audience`, `personality`, `use_case`, plus the relevant
`logo_type`, `mode`, `display_width`, `background`, `colors`, `notes` and `count`.
The default is three brand/app candidates or six IP candidates; explicit counts
from one to six are supported. Explain an unsupported count before calling.
App/IP currently require empty exact text and a filled square background.
IP uses lower-corner character composition; app uses a centered simple pictogram.
The broader existing skill provides other dedicated presets.

Colors in this native workflow are advisory visual roles. For exact palette locks,
restricted sets or strict color-count compliance, route to the existing Logo Land
skill/helper workflow; do not claim that advisory colors satisfy those constraints.
Brand artwork uses pure white presentation unless transparent is explicitly chosen.

The start tool saves a strategy and distinct visual directions, makes the agreed
native image requests and performs two independent structured pixel critiques.
These are model calls in strategist, art-director, design and production roles.
Describe them truthfully; they are not humans, market research or legal clearance.
Each image critic receives original PNG bytes and the requested display-width view;
edits also include the exact parent and its matching view. Neither a filename nor
the creator's prose establishes a passed visual check.

Show the returned gallery and original paths. Explain concrete visible strengths,
unmet criteria and the next decision without inventing a beauty score. Keep the
first failure and any retained originals visible. Gallery feedback is a JSON draft
to send to Hermes; clicking a favorite does not change the saved selection.

For later actions call `logopia_action`:

- `status`: only `workflow_id` and `action`. This reads without publishing or mutation.
- `continue`: also the exact current `expected_revision`. Resume only on an explicit
  request, including a failed or interrupted read-only critique with an unused review
  attempt. It preserves all originals. An unresolved image request is never resubmitted.
  Repeating `logopia_start` does not restart failed, cancelled or unknown work.
- `choose` / `revise`: use the copied feedback envelope with `schema_version: 1`,
  `workflow_id`, `expected_revision`, `candidate_id`, `candidate_sha256`, `action`,
  `keep` and `change`. Choosing has empty change. A revision needs a specific nonblank
  construction, spacing or detail change and features to retain. Never replace a stale
  revision/hash with a guessed current value; show the changed state first.
- `deliver`: the exact `expected_revision`. Selection is a preference, not approval;
  delivery succeeds only with the two valid current-image critiques and helper checks.
- `reconcile`: also `expected_revision` and the exact saved `job_id`. This examines saved
  receipts/commits without a model call and cannot manufacture an unknown outcome.

Revision preserves exact text, colors and background. Explain an incompatible change
before invoking it; a replacement brief belongs in a separate workflow. There are at
most two requested image revisions. The tool always keeps the real parent and creates
a separate child; it does not borrow parental approval. Never retry automatically for
aesthetics, timeout, failed native transport or unknown outcome. Return the actual
error and the saved workflow identity so the user can decide how to continue.

The installed local settings select trusted workspace/helper roots. Tools cannot set
directories, credentials or model/provider/profile overrides. If not configured,
report the tool's installation error. Do not bypass it with a second provider/client.

Deliver only the actual originals and verified package returned by the workflow.
Generated lettering is raster appearance, not proof of a font file or its license.
Do not promise editable vectors, trademark clearance, human review, store acceptance,
or professional superiority. Original PNG downloads remain available before approval.
