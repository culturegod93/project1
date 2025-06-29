from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_default() -> None:
    data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "EXECUTED"}]
    result = filter_by_state(data)
    assert result == [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}]


def test_filter_by_state_custom() -> None:
    data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}, {"id": 3, "state": "CANCELED"}]
    result = filter_by_state(data, state="CANCELED")
    assert result == [{"id": 2, "state": "CANCELED"}, {"id": 3, "state": "CANCELED"}]


def test_filter_by_state_empty_result() -> None:
    data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "EXECUTED"}]
    result = filter_by_state(data, state="UNKNOWN")
    assert result == []


def test_sort_by_date_desc() -> None:
    data = [
        {"id": 1, "date": "2022-01-01T12:00:00.000000"},
        {"id": 2, "date": "2023-01-01T12:00:00.000000"},
        {"id": 3, "date": "2021-01-01T12:00:00.000000"},
    ]
    result = sort_by_date(data)
    assert [item["id"] for item in result] == [2, 1, 3]


def test_sort_by_date_asc() -> None:
    data = [
        {"id": 1, "date": "2022-01-01T12:00:00.000000"},
        {"id": 2, "date": "2023-01-01T12:00:00.000000"},
        {"id": 3, "date": "2021-01-01T12:00:00.000000"},
    ]
    result = sort_by_date(data, reverse=False)
    assert [item["id"] for item in result] == [3, 1, 2]
