from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default() -> None:
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = filter_by_state(data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)
    assert result[0]["id"] == 41428829
    assert result[1]["id"] == 939719570


def test_filter_by_state_canceled() -> None:
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = filter_by_state(data, state="CANCELED")
    assert len(result) == 2
    assert all(item["state"] == "CANCELED" for item in result)
    assert result[0]["id"] == 594226727
    assert result[1]["id"] == 615064591


def test_sort_by_date_descending() -> None:
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = sort_by_date(data)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)
    assert result[0]["id"] == 41428829
    assert result[-1]["id"] == 939719570


def test_sort_by_date_ascending() -> None:
    data = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result = sort_by_date(data, reverse=False)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=False)
    assert result[0]["id"] == 939719570
    assert result[-1]["id"] == 41428829
