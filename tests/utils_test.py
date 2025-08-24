from __future__ import annotations

import json
from pathlib import Path

from src.utils import read_json


def test_read_json_valid(tmp_path: Path) -> None:
    file = tmp_path / "data.json"
    content = [{"amount": 100, "currency": "USD"}]
    file.write_text(json.dumps(content), encoding="utf-8")

    result = read_json(str(file))
    assert result == content


def test_read_json_empty_file(tmp_path: Path) -> None:
    file = tmp_path / "empty.json"
    file.write_text("", encoding="utf-8")

    result = read_json(str(file))
    assert result == []


def test_read_json_invalid_json(tmp_path: Path) -> None:
    file = tmp_path / "broken.json"
    file.write_text("{not-json", encoding="utf-8")

    result = read_json(str(file))
    assert result == []


def test_read_json_root_not_list(tmp_path: Path) -> None:
    file = tmp_path / "obj.json"
    file.write_text(json.dumps({"a": 1}), encoding="utf-8")

    result = read_json(str(file))
    assert result == []


def test_read_json_not_found() -> None:
    result = read_json("no_such_file.json")
    assert result == []
