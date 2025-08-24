from typing import Any
from typing import Dict
from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@pytest.mark.parametrize(
    "transaction, expected",
    [
        ({"amount": 100, "currency": "RUB"}, 100.0),
        ({"amount": 50, "currency": "GBP"}, 50.0),
    ],
)
def test_no_conversion(transaction: Dict[str, Any], expected: float) -> None:
    assert convert_to_rub(transaction) == expected


@patch("src.external_api.requests.get")
def test_usd_conversion(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {"result": 8200.0}
    mock_get.return_value.raise_for_status = lambda: None

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 8200.0


@patch("src.external_api.requests.get")
def test_eur_conversion(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {"result": 9000.0}
    mock_get.return_value.raise_for_status = lambda: None

    transaction = {"amount": 100, "currency": "EUR"}
    result = convert_to_rub(transaction)
    assert result == 9000.0


@patch("src.external_api.requests.get")
def test_api_failure(mock_get: Any) -> None:
    mock_get.side_effect = Exception("API error")

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 100.0  # Вернуло исходную сумму при ошибке
