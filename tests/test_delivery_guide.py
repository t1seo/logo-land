from __future__ import annotations

from typing import TYPE_CHECKING

from logo_helper.delivery import guide
from logo_helper.models import ArtifactId, SessionId
from logo_helper.storage import Store

if TYPE_CHECKING:
    from tests.conftest import Harness


def test_guide_records_selected_edit_request_when_palette_has_changed(harness: Harness) -> None:
    # Given the original green brief and a selected navy revision.
    harness.init()
    _ = harness.import_image()
    _ = harness.prompt.write_text("Change green to navy and preserve exact text.", encoding="utf-8")
    _ = harness.import_image(1, "v2", "--parent", "v1")
    state = Store.at(harness.workspace).load(SessionId("demo"))
    # When the guide is generated for the selected edit.
    text = guide(state, state.artifact(ArtifactId("v2")))
    # Then initial palette intent and authoritative selected request are both explicit.
    assert "Initial brief palette" in text
    assert "green" in text
    assert "Selected version request" in text
    assert "authoritative" in text.lower()
    assert "Change green to navy and preserve exact text." in text
