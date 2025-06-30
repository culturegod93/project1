from src.processing import filter_by_state, sort_by_date
import pytest
from typing import Any


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 6]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(sample_operations: list[dict[str, Any]], state: str, expected_ids: list[int]) -> None:
    result = filter_by_state(sample_operations, state=state)
    ids = [item["id"] for item in result]
    assert ids == expected_ids


def test_filter_by_state_missing_key(sample_operations: list[dict[str, Any]]) -> None:
    # Проверяем что элементы без "state" не включаются
    result = filter_by_state(sample_operations)
    for item in result:
        assert "state" in item


@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (True, [4, 5, 2, 1, 3, 6]),  # по убыванию даты; элементы без даты в конце
        (False, [3, 1, 2, 4, 5, 6]),  # по возрастанию даты
    ],
)
def test_sort_by_date(sample_operations: list[dict[str, Any]], reverse: bool, expected_order: list[int]) -> None:
    # Для сортировки обработаем элементы с пропущенной датой: поставим пустую дату в конец (проверка)
    def safe_date(item):
        return item.get("date") or ("9999-99-99T99:99:99" if reverse else "0000-00-00T00:00:00")

    sorted_ops = sorted(sample_operations, key=safe_date, reverse=reverse)
    result = sort_by_date(sample_operations, reverse=reverse)
    result_ids = [item["id"] for item in result]
    expected_ids = [item["id"] for item in sorted_ops]

    assert result_ids == expected_ids


def test_sort_by_date_keyerror() -> None:
    data = [{"id": 1, "date": "2020-01-01T00:00:00"}, {"id": 2}]
    with pytest.raises(KeyError):
        sort_by_date(data)


def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([]) == []
