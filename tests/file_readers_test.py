from unittest.mock import MagicMock
from unittest.mock import patch

import pandas as pd

from src import file_readers


# Тест для read_csv
@patch("pandas.read_csv")
def test_read_csv_success(mock_read_csv: MagicMock) -> None:
    mock_df = pd.DataFrame([{"amount": 100, "currency": "USD"}, {"amount": 200, "currency": "EUR"}])
    mock_read_csv.return_value = mock_df

    result = file_readers.read_csv("dummy.csv")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == 100
    assert result[1]["currency"] == "EUR"


@patch("pandas.read_csv")
def test_read_csv_empty(mock_read_csv: MagicMock) -> None:
    mock_df = pd.DataFrame()
    mock_read_csv.return_value = mock_df

    result = file_readers.read_csv("empty.csv")
    assert result == []


@patch("pandas.read_csv")
def test_read_csv_exception(mock_read_csv: MagicMock) -> None:
    mock_read_csv.side_effect = Exception("Ошибка чтения")
    result = file_readers.read_csv("fail.csv")
    assert result == []


# Тест для read_excel
@patch("pandas.read_excel")
def test_read_excel_success(mock_read_excel: MagicMock) -> None:
    mock_df = pd.DataFrame([{"amount": 500, "currency": "RUB"}])
    mock_read_excel.return_value = mock_df

    result = file_readers.read_excel("dummy.xlsx")
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["currency"] == "RUB"


@patch("pandas.read_excel")
def test_read_excel_empty(mock_read_excel: MagicMock) -> None:
    mock_df = pd.DataFrame()
    mock_read_excel.return_value = mock_df

    result = file_readers.read_excel("empty.xlsx")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_exception(mock_read_excel: MagicMock) -> None:
    mock_read_excel.side_effect = Exception("Ошибка чтения Excel")
    result = file_readers.read_excel("fail.xlsx")
    assert result == []
