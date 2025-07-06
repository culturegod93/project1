from typing import Any
from typing import Dict
from typing import List

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),
        ("EUR", [2]),
        ("RUB", []),
    ],
)
def test_filter_by_currency_parametrized(
    sample_currency_data: List[Dict[str, Any]],
    currency: str,
    expected_ids: List[int],
) -> None:
    result = list(filter_by_currency(sample_currency_data, currency=currency))
    ids = [item["id"] for item in result]
    assert ids == expected_ids


def test_transaction_descriptions(sample_description_data: List[Dict[str, Any]]) -> None:
    result = list(transaction_descriptions(sample_description_data))
    assert result == ["Оплата заказа", "Возврат средств"]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 4, ["0000000000000001", "0000000000000002", "0000000000000003"]),
        (0, 2, ["0000000000000000", "0000000000000001"]),
        (10, 10, []),
    ],
)
def test_card_number_generator_parametrized(
    start: int,
    stop: int,
    expected: List[str],
) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected
