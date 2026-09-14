#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pydantic>=2.12,<3", "pillow>=11.2,<13", "typer>=0.16,<1", "rich>=14,<15"]
# ///
# How to run: install uv, then from the repo use:
# uv run --locked python integrations/hermes/studio.py --help
"""Repository entry point for the Logopia Hermes CLI."""

from __future__ import annotations

from logopia_studio.launcher import main

if __name__ == "__main__":
    main()
