from typing import Any
from typing import Dict
from typing import List

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-06-01T09:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2019-05-15T15:45:00"},
        {"id": 4, "state": "PENDING", "date": "2023-03-22T10:00:00"},
        {"id": 5, "date": "2022-03-22T10:00:00"},
        {"id": 6, "state": "EXECUTED"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 6]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(sample_operations: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    result = filter_by_state(sample_operations, state=state)
    ids = [item["id"] for item in result]
    assert ids == expected_ids


def test_filter_by_state_missing_key(sample_operations: List[Dict[str, Any]]) -> None:
    result = filter_by_state(sample_operations)
    for item in result:
        assert "state" in item and item["state"] == "EXECUTED"


@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (True, [6, 4, 5, 2, 1, 3]),
        (False, [6, 3, 1, 2, 5, 4]),
    ],
)
def test_sort_by_date(sample_operations: List[Dict[str, Any]], reverse: bool, expected_order: List[int]) -> None:
    result = sort_by_date(sample_operations, reverse=reverse)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_order


def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([]) == []


def test_sort_by_date_all_missing_date() -> None:
    data: List[Dict[str, Any]] = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    result = sort_by_date(data)
    assert [item["id"] for item in result] == [1, 2]


def test_sort_by_date_no_date_reverse_true() -> None:
    data: List[Dict[str, Any]] = [
        {"id": 1, "date": "2023-01-01T00:00:00"},
        {"id": 2},  # без даты → становится 9999-12-31
    ]
    result = sort_by_date(data, reverse=True)
    assert [item["id"] for item in result] == [2, 1]


def test_sort_by_date_no_date_reverse_false() -> None:
    data: List[Dict[str, Any]] = [
        {"id": 1, "date": "2023-01-01T00:00:00"},
        {"id": 2},  # без даты
    ]
    result = sort_by_date(data, reverse=False)
    assert [item["id"] for item in result] == [2, 1]


def test_filter_by_state_empty_input() -> None:
    empty_data: List[Dict[str, Any]] = []
    result = filter_by_state(empty_data, state="EXECUTED")
    assert result == []
