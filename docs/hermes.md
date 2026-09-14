# Make a logo with Hermes

[English](hermes.md) · [한국어](hermes.ko.md) · [Logopia](../README.md)

Describe the brand once. Hermes develops distinct directions, generates original artwork, checks the pixels in two separate reviews, and refines the candidate you choose.

**Brief → directions → original candidates → visual review → your choice → focused revision → delivery**

## Start a conversation

Use [Hermes Agent](https://hermes-agent.nousresearch.com/) on macOS or Linux, a working Hermes image provider, Python 3.12+ and `uv`. This native plugin uses Hermes's public plugin and structured-image APIs. Its code supports the Hermes Python 3.11+ runtime; the local file helper runs separately in the repository's locked Python 3.12+ environment. The installer checks the plugin and its dependencies (Pydantic 2.12+ below 3, Pillow 11.2+ below 13); it does not install Hermes or configure an image provider.

From your Logopia checkout, create a dedicated profile once and configure its model and tools:

```sh
uv sync --locked
hermes profile create logopia --no-alias --no-skills
hermes -p logopia setup
uv run --locked python integrations/hermes/studio.py install --profile logopia
hermes -p logopia chat --toolsets logopia-studio,image_gen --skills logopia-studio:director
```

If the profile already exists, skip creation and reuse its working settings. Installation sets that named profile's native sequential and concurrent tool limits (`timeouts.tools.sequential_call` and `timeouts.tools.concurrent_batch`) to 1,800 seconds each, or 30 minutes, so the complete workflow can finish. It keeps the profile's existing provider/model selection and leaves the default profile separate. For a different project directory, add `--workspace /absolute/path/to/project` to installation.

An interrupted update restores the previous plugin when possible. If another file occupies its location or restoration fails, the old files remain under that profile's `plugins/.logopia-install-*/previous` directory. Keep that recovery copy until the installation is restored; the interrupted update is not reported as successful.

Try:

> Create three concepts for OFFCUT, a repairable furniture studio using reclaimed wood. Our customers live in small city homes. Make it warm, resourceful and precise. Combine a memorable symbol with the exact text OFFCUT on white. Compare the whole logo at 192 pixels wide.

The comparison page opens original PNGs directly. It shows each direction, its small-size view, concrete review findings and parent versions. Reviewing or drafting feedback in that page does not change your saved selection.

## Choose and refine

Select a candidate in the page, describe **what to keep** and **what to change**, then copy its request back to Hermes. For example:

> Keep the symbol, OFFCUT lettering and colors. Increase the gap between the symbol and lettering, and open the narrow internal gap in the symbol.

Every revision uses the exact parent image and receives new reviews. The parent remains available. Ask Hermes to deliver the selected candidate after its required checks pass; choosing a candidate alone does not approve its quality.

## Actual example: OFFCUT

The [OFFCUT example](hermes-demo/README.md) preserves three initial candidates and two native edits, with the exact chain **c1 → e1 → e2**. The first edit improved letter spacing but failed preservation because the symbol-to-word gap narrowed. The final e2 restored that gap, passed both model critiques and was delivered at workflow revision 47. Compare the [initial c1 PNG](hermes-demo/originals/c1.png) and [refined e2 PNG](hermes-demo/originals/e2.png), or download the actual [delivery ZIP](hermes-demo/delivery/logo-package.zip).

This is a curated example with the coordinator's recorded selection, not user approval or resumable private state. Download its folder and open `index.html` locally to use the offline comparison. The [execution record](qa/hermes-workflow/native-run.md) also retains the initial 420-second native timeout and the explicit critique-only continuation that added no image jobs.

## Continue saved work

Ask Hermes for the workflow's status or use the local commands below, replacing `offcut-hermes-demo` with your saved workflow ID. Reading status and rebuilding the page do not call an image model.

```sh
uv run --locked python integrations/hermes/studio.py show --workflow offcut-hermes-demo
uv run --locked python integrations/hermes/studio.py gallery --workflow offcut-hermes-demo
```

For a saved tool-request JSON file, the bounded launcher checks the exact workflow revision and, for candidate actions, the original hash before starting Hermes:

```sh
uv run --locked python integrations/hermes/studio.py run --profile logopia --request request.json
```

The launcher's own deadline defaults to 30 minutes; `--timeout` accepts 1–3,600 seconds. Shutdown allows a ten-second graceful period followed by up to ten seconds for forced-stop verification, plus bounded cleanup of an active PID query. It checks the groups in its own session, including the local helper. These bounds are separate from the named profile's native tool limits. A process exit code or Hermes's final message alone cannot establish success: the launcher checks the saved workflow result. Stopping the local process does not prove that the image provider cancelled its request.

If an old feedback request is rejected, open the latest state and explicitly reapply your change. An interrupted image request can have an unknown outcome; it is never resubmitted automatically. Completed originals stay saved under `.logo-generator/sessions/`; workflow decisions live under `.logo-generator/workflows/`.

If only a read-only image critique failed or was interrupted, explicitly ask Hermes to continue the saved workflow. An eligible candidate may use its one remaining review attempt without generating new images, retaining the failed attempt in its history. An unresolved image request remains blocked until its exact recorded outcome can be reconciled; no retry, new cache-file guess or fresh original is automatic. Repeating the original creation request does not restart failed or interrupted work.

## Scope

- Brand logos, centered pictogram app icons and simple IP characters. The default is three brand/app concepts or six IP candidates; request one to six explicitly.
- Requests for exact brand lettering and optional transparent brand PNGs. Inspect the generated spelling; app/IP artwork currently uses a filled square with no lettering.
- Advisory colors, two separate model critiques and up to two requested revisions. Each edit is based on the exact parent PNG and receives fresh design/lettering and production/use-size reviews. The two calls are model observations, not independent human reviewers or proof of professional superiority. Revisions preserve the wording, colors and background; use a new brief for those changes. For strict palettes or other dedicated app styles, use the existing [`$logo-land` Codex skill](../skills/logo-land/SKILL.md).
- Original raster PNGs and verified delivery packages. The reviews are AI observations, not human certification. Editable vectors, font files, trademark clearance and platform icon packages are separate work.

The IP direction adapts [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill), with its [MIT notice](../integrations/hermes/skills/director/references/ip-as-logo.LICENSE).
