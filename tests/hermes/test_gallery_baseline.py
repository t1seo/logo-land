from hashlib import sha256
from pathlib import Path


def test_existing_comparison_stays_unchanged() -> None:
    # Given: the existing comparison implementation at the dispatch baseline.
    root = Path(__file__).resolve().parents[2]
    implementation = "skills/logo-land/scripts/logo_helper/comparison_gallery.py"
    template = "skills/logo-land/assets/comparison-gallery.template.html"
    expected = {
        implementation: "17a81c7eb7488f500babe27eb653948ea88ca1c46467cfb81d3e55db141e2879",
        template: "2e9760669f0aa2d9d34267fce0241452f43de435c9c4985bce80be70afb309a3",
    }
    # When: the independent studio gallery is introduced.
    actual = {name: sha256((root / name).read_bytes()).hexdigest() for name in expected}
    # Then: legacy comparison bytes remain identical.
    assert actual == expected
