# A Hermes production workflow for Logopia

Research checked on 15 September 2026. The proposal below combines primary design sources with the installed Hermes runtime; it is not evidence that an AI workflow outperforms professional designers.

## What changes the work

| Finding | Product decision |
| --- | --- |
| Mozilla evaluated identity directions against brand attributes, with qualitative and strategic judgment alongside surveys. | Start with an audience need, brand promise and a distinctive construction principle. Compare genuinely different ideas against these criteria. Do not substitute a popularity or beauty score. [Mozilla](https://blog.mozilla.org/opendesign/nearly-there/) |
| Figma's critique practice addresses shallow, unworkable feedback and group agreement. | Give separate critics the actual artwork and intended use before the creator's explanation. Ask what is visible, where it fails, and what to preserve or change. Two model calls remain AI reviews, not independent human certification. [Figma](https://www.figma.com/blog/design-critiques-at-figma/) |
| Kerning adjusts a letter pair; tracking adjusts spacing across a range. | Preserve exact lettering and identify the pair, counter, alignment or symbol-to-type gap being changed. Inspect the original at the requested display width as well as full size. [Adobe](https://helpx.adobe.com/illustrator/using/line-character-spacing.html) |
| The Mailchimp identity connects positioning with an existing character, color and typography. | Give colors and letterforms roles in a coherent identity; do not make every brand the same minimal geometric symbol. [COLLINS](https://wearecollins.com/case-studies/mailchimp/) |
| GOV.UK recommends asking only necessary questions and not requesting information twice. | Extract the brief from the conversation, state consequential assumptions, and ask only a missing question that would change the work. An authorized request does not need another approval at every stage. [GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/) |
| HAX recommends making partial corrections easy. Figma separates version preview from restoration. | Keep the exact parent and make keep/change feedback explicit. Previewing a candidate is different from selecting it; revisions remain accessible alongside their parents. [Microsoft HAX](https://www.microsoft.com/en-us/haxtoolkit/pattern/g9-b-rich-and-detailed-edits/), [Figma Make](https://help.figma.com/hc/en-us/articles/42009840449175-Edit-a-Figma-Make-file) |

These are workflow decisions inferred from the sources. Logo recognition, legal uniqueness, sales impact and superiority over a designer require evidence this project does not collect.

## The actual Hermes boundary

The installed NousResearch Hermes Agent exposes native Python plugins, host-owned structured model calls with image input, and the `image_generate` tool. The workflow uses these public interfaces; it does not reimplement the provider or read OAuth credentials. The local checkout was checked at `d3e2ace1dde9f1d279f99c9ebc6bce2e761b025d`; this is a local verification identifier, not a verified public GitHub permalink. Current documentation includes features newer than that checkout. [Plugin LLM API](https://hermes-agent.nousresearch.com/docs/developer-guide/plugin-llm-access).

`ctx.llm.complete_structured` supports finite, attributed text-and-image calls. Strategy, art direction, design critique and production critique can therefore be separate calls without launching another agent framework. Logopia validates every returned record; missing or invalid JSON does not approve an image. The existing local helper separately verifies PNG bytes, hashes, backgrounds and delivery requirements. [Structured calls and image inputs](https://hermes-agent.nousresearch.com/docs/developer-guide/plugin-llm-access#complete_structured).

A real preflight in a dedicated `logopia` profile returned a 1254 × 1254 PNG through Hermes's `openai-codex` image provider. Its actual tool receipt, decoded dimensions and original file were inspected. This establishes that local connection, not future availability or guaranteed image quality. There is no automatic alternative image provider if a request fails. [Image generation](https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation), [profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles).

The installed Hermes interpreter is Python 3.11; Logopia's existing helper uses Python 3.12. A subprocess with the helper's locked environment preserves that boundary. Default Hermes configuration remains separate from the named workflow profile.

## Experience and acceptance criteria

The conversation handles intent and decisions. A portable comparison page gives immediate access to originals, target-size views, concrete review findings, parent versions and a keep/change feedback draft. It explicitly distinguishes a local feedback draft from the canonical decision recorded in Hermes.

Generation, inspection, selection and delivery are separate states. All generated candidates remain available, including unsuccessful revisions. A new image receives fresh critique; a parent's approval is never inherited. An unknown image request remains unresolved until exact saved evidence can reconcile it. An explicit continuation may retry an interrupted read-only critique once; it never resubmits an image.

The acceptance test is an actual Hermes run with saved directions, original images, separate pixel critiques, a targeted edit and a verified delivery. Tests also cover interrupted work, stale feedback, malformed reports, repeated requests and direct original access. An attractive staged mockup alone is insufficient evidence. Editable vectors, exact font composition, print production and store-ready icon packages are separate capabilities and are not implied by this workflow.
