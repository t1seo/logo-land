"""Escaped comparison cards; user content is data, never executable code or URLs."""

from html import escape
from pathlib import Path
from string import Template
from typing import Final

from logo_helper.comparison_models import ComparisonArtifact, ComparisonManifest

_SPACE: Final = 32


def _text(value: str) -> str:
    return escape(
        "".join(
            f"\\u{ord(character):04x}"
            if ord(character) < _SPACE and character not in "\n\r\t"
            else character
            for character in value
        )
    )


def _card(item: ComparisonArtifact, number: int) -> str:
    source = item.source
    identity = f"{source.session} / {source.artifact} · revision {source.revision}"
    image = (
        f'<img src="{item.image_file}" alt="{_text(item.brand_name)} candidate" '
        f'width="{item.image.width}" height="{item.image.height}">'
    )
    notes = (
        ("Rationale", source.rationale),
        ("Preserve", source.preserve),
        ("Change", source.change),
        ("Observation", source.observation),
    )
    decision = "\n".join(
        (
            f"Source: {identity}",
            f"PNG SHA-256: {item.sha256}",
            *(f"{key}: {value}" for key, value in notes),
        )
    )
    heading = (
        f'<article class="candidate" data-session="{source.session}" '
        f'data-artifact="{source.artifact}" data-kind="{item.kind}" '
        f'data-style="{_text(item.style)}">'
        f'<div class="card-top"><span>{number:02d}</span><span>{_text(item.kind.replace("_", " "))}'
        f" · {_text(item.style.replace('_', ' '))}</span></div>"
        f'<div class="preview artwork">{image}</div>'
        f'<div class="preview app-home" aria-label="Illustrative app home"><div class="home-icon">'
        f"{image}<span>{_text(item.brand_name)}</span></div>"
        '<div class="dummy-app"></div><div class="dummy-app"></div></div>'
        f'<div class="preview web-header" aria-label="Illustrative web header">{image}'
        '<span>Home</span><span>About</span><span class="header-button">Explore</span></div>'
        '<div class="preview favicon" aria-label="Illustrative browser tab">'
        f'<div class="browser-tab">{image}<span>{_text(item.brand_name)}</span>'
        "<span>&times;</span></div></div>"
        f'<div class="card-body"><h2>{_text(item.brand_name)}</h2>'
        f'<p class="identity">{_text(identity)}</p><p class="facts">'
        f"{item.image.width} &times; {item.image.height} px · Original PNG</p>"
        '<div class="actual-sizes" aria-label="Actual pixel sizes">'
    )
    sizes = "".join(
        (
            f'<figure><img src="{item.image_file}" alt="{size} pixel candidate" '
            f'width="{size}" height="{size}" style="width:{size}px;height:{size}px">'
            f"<figcaption>{size}px</figcaption></figure>"
        )
        for size in (16, 32, 64, 128)
    )
    decisions = "".join(f"<dt>{key}</dt><dd>{_text(value) or '—'}</dd>" for key, value in notes)
    ending = (
        "</dl><details><summary>Source and decision text</summary>"
        f'<label class="sr-only" for="decision-{number}">Source and decision text for '
        f'{_text(identity)}</label><textarea id="decision-{number}" readonly>'
        f"{_text(decision)}</textarea>"
        f'<button type="button" data-copy="decision-{number}">Copy source + notes</button>'
        '<p class="copy-status" role="status"></p></details><div class="downloads">'
        f'<a href="{item.image_file}" download>Original PNG<span class="sr-only"> '
        f'{_text(identity)}</span></a><a href="{item.prompt_file}" download>Exact prompt'
        f'<span class="sr-only"> {_text(identity)}</span></a></div></div></article>'
    )
    return heading + sizes + '</div><dl class="notes">' + decisions + ending


def render_markup(manifest: ComparisonManifest) -> str:
    """Render offline markup without interpolating any user data into JavaScript."""
    template = Path(__file__).resolve().parents[2] / "assets/comparison-gallery.template.html"
    styles = sorted({item.style for item in manifest.artifacts})
    return Template(template.read_text(encoding="utf-8")).substitute(
        title=_text(manifest.title),
        count=len(manifest.artifacts),
        styles="".join(
            f'<option value="{_text(style)}">{_text(style.replace("_", " "))}</option>'
            for style in styles
        ),
        cards="".join(_card(item, number) for number, item in enumerate(manifest.artifacts, 1)),
    )
