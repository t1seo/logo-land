from __future__ import annotations

import os
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Final

import pytest
from pydantic import TypeAdapter

RUNTIME: Final = Path.home() / ".hermes/hermes-agent"
NATIVE_PYTHON: Final = RUNTIME / "venv/bin/python"
RESOLVE: Final = """import json, sys
from pathlib import Path
from agent.deadline import resolve_timeout
from hermes_cli.config import get_config_path
assert get_config_path() == Path(sys.argv[1]) / 'config.yaml'
concurrent = resolve_timeout(
    'tools.concurrent_batch', default=420,
    env_var='HERMES_CONCURRENT_TOOL_TIMEOUT_S')
sequential = resolve_timeout('tools.sequential_call', default=concurrent)
print(json.dumps([sequential, concurrent]))
"""


def read_native_deadlines(home: Path) -> tuple[float, float]:
    environment = {
        "PATH": os.defpath,
        "HERMES_HOME": str(home),
        "HERMES_MANAGED_DIR": str(home.parent / "managed-fixture"),
        "HERMES_CONCURRENT_TOOL_TIMEOUT_S": "420",
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    result = subprocess.run(  # noqa: S603 - fixed read-only resolver, isolated Hermes home.
        (str(NATIVE_PYTHON), "-c", RESOLVE, str(home)),
        cwd=RUNTIME,
        env=environment,
        text=True,
        capture_output=True,
        check=True,
        timeout=30,
    )
    return TypeAdapter(tuple[float, float]).validate_json(result.stdout)


@pytest.mark.skipif(not NATIVE_PYTHON.is_file(), reason="Installed native Hermes is unavailable")
def test_installed_public_resolver_reads_both_finite_keys(tmp_path: Path) -> None:
    with TemporaryDirectory(prefix="logopia-timeout-", dir=tmp_path) as temporary:
        home = Path(temporary).resolve() / "native-home"
        home.mkdir()
        config = home / "config.yaml"
        sentinel = "model: fixture-preserved\n"
        _ = config.write_text(sentinel, encoding="utf-8")
        assert read_native_deadlines(home) == (420.0, 420.0)
        configured = f"""{sentinel}timeouts:
  tools:
    sequential_call: 1800
    concurrent_batch: 1800
"""
        _ = config.write_text(configured, encoding="utf-8")
        assert read_native_deadlines(home) == (1800.0, 1800.0)
        assert config.read_text(encoding="utf-8") == configured
