import logging
from pathlib import Path
from typing import Any

import pytest

from src.decorators import log


@log()
def add(a: int, b: int) -> int:
    return a + b


@log("test_log.log")
def divide(a: int, b: int) -> float:
    return a / b


@log("test_log_error.log")
def fail_func(x: int) -> int:
    raise ValueError("Intentional error")


def test_log_to_console(caplog: Any) -> None:
    with caplog.at_level(logging.INFO):
        result = add(2, 3)
    assert result == 5
    assert "Called add with args=(2, 3)," in caplog.text


def test_log_to_file(tmp_path: Path) -> None:
    log_file: Path = tmp_path / "output.log"

    @log(str(log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(4, 5)
    assert result == 20

    with open(log_file, encoding="utf-8") as f:
        content = f.read()
    assert "Called multiply with args=(4, 5)," in content


def test_log_exception(tmp_path: Path) -> None:
    log_file: Path = tmp_path / "error.log"

    @log(str(log_file))
    def crash() -> None:
        raise RuntimeError("Boom!")

    with pytest.raises(RuntimeError):
        crash()

    with open(log_file, encoding="utf-8") as f:
        content = f.read()
    assert "Error in crash" in content
    assert "Boom!" in content
