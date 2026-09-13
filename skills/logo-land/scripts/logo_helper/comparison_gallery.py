"""Read-only multi-session PNG snapshots with exclusive, index-last publication."""

from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory

from logo_helper.app_icon_publish import publish_gallery
from logo_helper.comparison_cards import render_markup
from logo_helper.comparison_models import (
    ComparisonArtifact,
    ComparisonManifest,
    ComparisonResult,
    ComparisonSelection,
)
from logo_helper.images import inspect_png
from logo_helper.models import ProjectError, Session, SessionId
from logo_helper.storage import Store, read_source, safe_path, write_new


def render_comparison_gallery(
    store: Store, selection: ComparisonSelection, output_relative: str
) -> ComparisonResult:
    """Verify explicit revisions and snapshot bytes without changing source sessions."""
    destination = safe_path(store.root, output_relative)
    relative = destination.relative_to(store.root)
    if relative.parts[0].casefold() in {".logo-generator", ".git"}:
        raise ProjectError("reserved_output", "Gallery cannot occupy reserved project storage")
    if destination.exists():
        raise ProjectError("conflict", "Gallery destination already exists")
    states: dict[SessionId, Session] = {}
    snapshots: list[ComparisonArtifact] = []
    for number, item in enumerate(selection.items, 1):
        if item.session not in states:
            states[item.session] = store.load(item.session)
        state = states[item.session]
        if state.revision != item.revision:
            raise ProjectError(
                "stale_revision",
                f"Session {item.session}: expected {item.revision}; current {state.revision}",
            )
        artifact = state.artifact(item.artifact)
        snapshots.append(
            ComparisonArtifact(
                source=item,
                parent_id=artifact.parent_id,
                brand_name=state.brief.brand_name,
                kind="app_icon" if artifact.app_icon is not None else "brand",
                style=(
                    artifact.app_icon.preset
                    if artifact.app_icon is not None
                    else state.brief.logo_type
                ),
                image_file=f"images/{number:03d}.png",
                prompt_file=f"prompts/{number:03d}.txt",
                sha256=artifact.sha256,
                prompt_sha256=sha256(artifact.prompt.encode("utf-8")).hexdigest(),
                image=artifact.image,
                app_icon=artifact.app_icon,
                lockup=artifact.lockup,
            )
        )
    manifest = ComparisonManifest(title=selection.title, artifacts=tuple(snapshots))
    markup = render_markup(manifest)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix=".comparison-gallery-", dir=destination.parent) as temporary:
        staging = Path(temporary)
        (staging / "images").mkdir()
        (staging / "prompts").mkdir()
        for snapshot in snapshots:
            source = snapshot.source
            artifact = states[source.session].artifact(source.artifact)
            data = read_source(safe_path(store.session_dir(source.session), artifact.path))
            if sha256(data).hexdigest() != snapshot.sha256:
                raise ProjectError("hash_mismatch", f"Artifact {source.artifact} changed")
            if inspect_png(data) != snapshot.image:
                raise ProjectError("invalid_state", f"Artifact {source.artifact} facts changed")
            write_new(staging / snapshot.image_file, data)
            write_new(staging / snapshot.prompt_file, artifact.prompt.encode("utf-8"))
        write_new(staging / "manifest.json", manifest.model_dump_json(indent=2).encode("utf-8"))
        write_new(staging / "index.html", markup.encode("utf-8"))
        for state in states.values():
            _ = store.expect(state.id, state.revision)
        _ = safe_path(store.root, output_relative)
        publish_gallery(staging, destination)
    return ComparisonResult(
        path=relative.as_posix(),
        index_path=f"{relative.as_posix()}/index.html",
        count=len(snapshots),
    )
