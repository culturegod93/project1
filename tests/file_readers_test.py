import pytest
from unittest.mock import patch, MagicMock
from src import file_readers


@pytest.fixture
def sample_csv_data():
    return [
        {"date": "2025-01-01", "amount": 100, "currency": "RUB"},
        {"date": "2025-01-02", "amount": 200, "currency": "USD"},
    ]


@pytest.fixture
def sample_excel_data():
    return [
        {"date": "2025-01-03", "amount": 150, "currency": "EUR"},
        {"date": "2025-01-04", "amount": 300, "currency": "RUB"},
    ]


@patch("pandas.read_csv")
def test_read_csv_success(mock_read_csv, sample_csv_data):
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.to_dict.return_value = sample_csv_data
    mock_read_csv.return_value = mock_df

    result = file_readers.read_csv("dummy.csv")
    assert result == sample_csv_data
    mock_read_csv.assert_called_once_with("dummy.csv")


@patch("pandas.read_csv")
def test_read_csv_empty_file(mock_read_csv):
    mock_df = MagicMock()
    mock_df.empty = True
    mock_read_csv.return_value = mock_df

    result = file_readers.read_csv("empty.csv")
    assert result == []


@patch("pandas.read_csv", side_effect=Exception("read error"))
def test_read_csv_error(mock_read_csv):
    result = file_readers.read_csv("error.csv")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_success(mock_read_excel, sample_excel_data):
    mock_df = MagicMock()
    mock_df.empty = False
    mock_df.to_dict.return_value = sample_excel_data
    mock_read_excel.return_value = mock_df

    result = file_readers.read_excel("dummy.xlsx")
    assert result == sample_excel_data
    mock_read_excel.assert_called_once_with("dummy.xlsx")


@patch("pandas.read_excel")
def test_read_excel_empty_file(mock_read_excel):
    mock_df = MagicMock()
    mock_df.empty = True
    mock_read_excel.return_value = mock_df

    result = file_readers.read_excel("empty.xlsx")
    assert result == []


@patch("pandas.read_excel", side_effect=Exception("read error"))
def test_read_excel_error(mock_read_excel):
    result = file_readers.read_excel("error.xlsx")
    assert result == []
