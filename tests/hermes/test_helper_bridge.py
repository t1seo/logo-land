import sys

import pytest
from logopia_studio.helper_models import parse_session
from logopia_studio.helper_process import run_cli
from logopia_studio.models import StudioError
from tests.hermes.test_core_fixtures import REPO


def test_helper_process_timeout_is_bounded() -> None:
    # Given an owned subprocess that outlasts its finite deadline.
    assert (REPO / "integrations/hermes/logopia_studio/helper_process.py").is_file(), (
        "Bridge not implemented"
    )

    # When its deadline expires, then the process group is settled and a typed failure is returned.
    with pytest.raises(StudioError, match="helper_timeout"):
        _ = run_cli((sys.executable, "-c", "import time; time.sleep(30)"), 0.05)


@pytest.mark.parametrize("raw", ['{"success":true}', "{broken", '{"schema_version":true}'])
def test_malformed_helper_json_is_rejected(raw: str) -> None:
    # Given an incomplete or malformed helper response.
    assert (REPO / "integrations/hermes/logopia_studio/helper_models.py").is_file(), (
        "Bridge not implemented"
    )

    # When parsed, then a success flag cannot stand in for a validated session.
    with pytest.raises(StudioError, match="invalid_helper"):
        _ = parse_session(raw)
