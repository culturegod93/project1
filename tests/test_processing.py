from src.processing import filter_by_state, sort_by_date

sample_data = [
    {"id": 1, "state": "EXECUTED", "date": "2022-01-01T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2021-01-01T10:00:00"},
    {"id": 3, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
]

def test_filter_by_state_default():
    result = filter_by_state(sample_data)
    assert all(op["state"] == "EXECUTED" for op in result)

def test_filter_by_state_custom():
    result = filter_by_state(sample_data, "CANCELED")
    assert all(op["state"] == "CANCELED" for op in result)

def test_sort_by_date():
    result = sort_by_date(sample_data)
    assert result[0]["date"] == "2023-01-01T10:00:00"
