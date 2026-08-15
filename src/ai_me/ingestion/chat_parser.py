"""Normalizes exported chat records into a platform-neutral format."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def parse_json_export(path: Path) -> list[dict[str, Any]]:
    """Parse a JSON export and normalize common message-list shapes."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in ("messages", "chats", "conversation"):
            value = payload.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
    raise ValueError("Unsupported JSON chat export shape")


def parse_text_export(path: Path) -> list[str]:
    """Read a TXT export as lines; platform-specific parsing is added in adapters."""
    return [line.rstrip("\n") for line in path.read_text(encoding="utf-8").splitlines()]
