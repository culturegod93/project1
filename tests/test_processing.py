from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state_default() -> None:
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    expected = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    assert filter_by_state(data) == expected


def test_filter_by_state_custom_value() -> None:
    data = [
        {"id": 1, "state": "CANCELED"},
        {"id": 2, "state": "EXECUTED"},
    ]
    result = filter_by_state(data, state="CANCELED")
    assert result == [{"id": 1, "state": "CANCELED"}]


def test_filter_by_state_no_matching() -> None:
    data = [
        {"id": 1, "state": "CANCELED"},
        {"id": 2, "state": "CANCELED"},
    ]
    result = filter_by_state(data, state="EXECUTED")
    assert result == []


def test_filter_by_state_missing_key() -> None:
    data = [
        {"id": 1},
        {"id": 2, "state": "EXECUTED"},
        {"id": 3, "status": "EXECUTED"},
    ]
    result = filter_by_state(data)
    assert result == [{"id": 2, "state": "EXECUTED"}]


def test_filter_by_state_empty_list() -> None:
    assert filter_by_state([]) == []


def test_sort_by_date_descending_default() -> None:
    data = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2021-01-01T00:00:00"},
    ]
    result = sort_by_date(data)
    expected = [
        {"id": 2, "date": "2021-01-01T00:00:00"},
        {"id": 1, "date": "2020-01-01T00:00:00"},
    ]
    assert result == expected


def test_sort_by_date_ascending() -> None:
    data = [
        {"id": 2, "date": "2021-01-01T00:00:00"},
        {"id": 1, "date": "2020-01-01T00:00:00"},
    ]
    result = sort_by_date(data, reverse=False)
    expected = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2021-01-01T00:00:00"},
    ]
    assert result == expected


def test_sort_by_date_with_equal_dates() -> None:
    data = [
        {"id": 1, "date": "2020-01-01T00:00:00"},
        {"id": 2, "date": "2020-01-01T00:00:00"},
    ]
    result = sort_by_date(data)
    assert result == data


def test_sort_by_date_missing_key_raises_keyerror() -> None:
    data = [
        {"id": 1, "date": "2021-01-01T00:00:00"},
        {"id": 2},
    ]
    try:
        sort_by_date(data)
        assert False, "Expected KeyError for missing 'date'"
    except KeyError:
        assert True


def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([]) == []
