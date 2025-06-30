from typing import Any

from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_default() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    expected: list[dict[str, Any]] = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    assert filter_by_state(data) == expected


def test_filter_by_state_custom_value() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "state": "CANCELED"},
        {"id": 2, "state": "EXECUTED"},
    ]
    assert filter_by_state(data, state="CANCELED") == [{"id": 1, "state": "CANCELED"}]


def test_filter_by_state_no_matching() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "state": "CANCELED"},
        {"id": 2, "state": "CANCELED"},
    ]
    assert filter_by_state(data, state="EXECUTED") == []


def test_filter_by_state_missing_key() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1},
        {"id": 2, "state": "EXECUTED"},
        {"id": 3, "status": "EXECUTED"},
    ]
    assert filter_by_state(data) == [{"id": 2, "state": "EXECUTED"}]


def test_filter_by_state_empty_list() -> None:
    data: list[dict[str, Any]] = []
    assert filter_by_state(data) == []


def test_sort_by_date_descending_default() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2021-01-01T00:00:00"},
    ]
    expected: list[dict[str, Any]] = [
        {"id": 2, "date": "2021-01-01T00:00:00"},
        {"id": 1, "date": "2020-01-01T00:00:00"},
    ]
    assert sort_by_date(data) == expected


def test_sort_by_date_ascending() -> None:
    data: list[dict[str, Any]] = [
        {"id": 2, "date": "2021-01-01T00:00:00"},
        {"id": 1, "date": "2020-01-01T00:00:00"},
    ]
    expected: list[dict[str, Any]] = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2021-01-01T00:00:00"},
    ]
    assert sort_by_date(data, reverse=False) == expected


def test_sort_by_date_with_equal_dates() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2020-01-01T00:00:00"},
    ]
    assert sort_by_date(data) == data


def test_sort_by_date_missing_key_raises_keyerror() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "date": "2021-01-01T00:00:00"},
        {"id": 2},
    ]
    try:
        sort_by_date(data)
        assert False, "Expected KeyError for missing 'date'"
    except KeyError:
        pass  # ожидаемое исключение


def test_sort_by_date_empty_list() -> None:
    data: list[dict[str, Any]] = []
    assert sort_by_date(data) == []
