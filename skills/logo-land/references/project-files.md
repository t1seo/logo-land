# Project files and helper

Resolve the plugin root from the installed skill location (two directories above `SKILL.md`). `--workspace` is the user's project directory; it is independent of the plugin location. Python 3.12+, uv, Pydantic v2 and Pillow are needed for file helpers. The native image tool needs no API key.

Invoke the helper with an argv-based shell tool or correctly quoted arguments. Put arbitrary user text in JSON/text files, not interpolated shell command strings. Commands emit JSON. Read errors and exit codes before proceeding.

The workspace must already exist. Session and artifact IDs match `^[a-z0-9][a-z0-9_-]{0,63}$`; brand text can contain Unicode. Successful commands emit JSON on stdout. Known file/schema/domain errors emit JSON on stderr with exit 1; invalid CLI arguments use Typer's exit 2. `--help` is human-readable text. Inputs have a 64 MiB file limit; images must be static PNG with at most 40 million pixels.

The first invocation may download dependencies. Direct execution of the `.py` script through uv uses its PEP 723 environment with pinned direct dependencies, separately from the project's lockfile. To run the full locked project environment, use `uv run --locked --project /absolute/path/to/logo-land python /absolute/path/to/logo-land/skills/logo-land/scripts/logo_project.py ...`.

```sh
uv run --project /absolute/path/to/logo-land /absolute/path/to/logo-land/skills/logo-land/scripts/logo_project.py --workspace /absolute/path/to/workspace list
```

The long prefix above is omitted from the command examples below. Never run the bare subcommands as standalone shell commands.

## Brief

Required string fields: `brand_name`, `exact_text`, `industry`, `audience`. Set `exact_text` to an empty string for a deliberately text-free symbol. Preserve user text verbatim.

Optional fields:

| Field | Type / default |
|---|---|
| `slogan` | string, empty |
| `logo_type` | wordmark / lettermark / monogram / symbol / abstract / combination / emblem / mascot; combination |
| `styles`, `palette`, `forbidden`, `use_cases`, `assumptions` | arrays of strings, empty |
| `background` | opaque / transparent; opaque |
| `concept_count` | integer, 3 |

Use [brief.example.json](../assets/brief.example.json) as a starting shape. Do not treat its fictional brand as the user's brand. For an unknown audience or other nonessential field, record a reasonable assumption rather than claiming the user supplied it.

## Session lifecycle

```text
init --session morrow-demo --brief /workspace/brief.json
list
show --session morrow-demo
prompt --session morrow-demo --concept "Open geometric M with generous negative space"
```

`init` creates revision 0. `prompt` returns proposed `prompt` text and `parent_image_path` when applicable; it does not call image generation or mutate state. Save the final prompt as a UTF-8 file before the actual image call. Import only the actual returned PNG:

```text
import --session morrow-demo --artifact a-v1 --image /actual/generated/image.png --prompt-file /workspace/prompts/a-v1.txt --revision 0
```

Every mutation increments `revision`. Use the revision from the latest successful response or `show`; do not copy the illustrative numbers blindly. Stable IDs must be unique. The helper copies the source and preserves the original.

For an edit:

```text
prompt --session morrow-demo --concept "Chosen geometric direction" --parent a-v1 --changes "Change green to navy, preserving shape and exact text"
import --session morrow-demo --artifact a-v2 --image /actual/edited/image.png --prompt-file /workspace/prompts/a-v2.txt --parent a-v1 --revision 1
```

Between those commands the assistant must view the actual parent, invoke the native edit tool with it, and inspect the returned image. Saving a prompt or importing an unrelated file does not prove an edit happened.

When the user changes the background requirement, pass `--background opaque` or `--background transparent` on import. This records that artifact's requested background independently of the original brief. For example, a transparent child of an opaque original uses `--parent a-v1 --background transparent`. On subsequent edits retaining that variant, pass the same override again. Omitting it defaults to the original brief, not the parent's override. Never infer or weaken the request from the generated pixels. Legacy sessions without this field remain readable and use their original brief.

For a tool failure, preserve the attempt without a fake artifact:

```text
failure --session morrow-demo --prompt-file /workspace/prompts/a-v2.txt --reason "Actual tool error summary" --parent a-v1 --revision 1
```

## Select, review and export

Select the user's choice or a choice they delegated to the assistant. Write a visual review JSON with the schema in [delivery-checks.md](delivery-checks.md), based on actual inspection.

```text
select --session morrow-demo --artifact a-v2 --revision 2
review --session morrow-demo --artifact a-v2 --review-file /workspace/review.json --revision 3
export --session morrow-demo --revision 4
```

The default final output is `output/logo-generator/<session-id>/` under the workspace. `--output` can select a new workspace-relative destination. Use a fresh output directory for another delivery version; never replace an earlier package. If the requested destination is outside the workspace, first export and verify inside it, then copy the complete verified package to the explicitly requested location without overwriting existing files.

The internal `.logo-generator` directory is reserved for sessions and locks and cannot be used as an export destination. Use a normal output folder such as `deliveries/version-2`.

The helper requires all visual checks to pass and rechecks real file metadata and hashes. It cannot independently certify a reviewer's design judgment. If it rejects a corrupt, opaque-when-transparent-required, or modified image, fix the underlying problem; do not edit the state JSON to bypass it.

## Resume and preserve

Sessions live at `.logo-generator/sessions/<session-id>/`. Read them through `show` in a new conversation, reopen relevant PNGs, and continue using saved IDs. Missing or changed images, unsupported schema, stale revisions and duplicate IDs are errors, not reasons to reset the workspace. Do not delete a lock unless it has been independently proven stale and recovery is explicitly warranted.

Keep final prompts and failed attempts for reproducibility. The prompt records the requested design; generated lettering, intended palette values and font appearance still need visual verification. Do not store account credentials or base64 images in brief/state text.

## Compatibility after the Logo Land rename

Logo Land was previously called `logo-generator`. The skill path and invocation are now `skills/logo-land` and `$logo-land`. Existing `.logo-generator/` session storage and `output/logo-generator/` default deliveries remain unchanged so saved projects resume without migration. Historical sample prompts retain the original invocation.
