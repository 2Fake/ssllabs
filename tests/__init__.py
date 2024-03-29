"""Tests for ssllabs."""

from functools import lru_cache
from json import loads
from pathlib import Path
from typing import Any


@lru_cache
def load_fixture(filename: str) -> Any:
    """Load a fixture."""
    path = Path(__file__).parent / "test_data" / f"{filename}.json"
    return loads(path.read_text())
