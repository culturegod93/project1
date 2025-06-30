import pytest
from typing import Any


@pytest.fixture
def sample_operations() -> list[dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2021-06-01T09:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2019-11-15T18:45:00"},
        {"id": 4, "state": "PENDING", "date": "2022-03-22T10:00:00"},
        {"id": 5, "date": "2022-03-22T10:00:00"},  # Без state
        {"id": 6, "state": "EXECUTED"},            # Без даты
    ]


@pytest.fixture
def sample_card_numbers() -> list[str]:
    return [
        "7000792289606361",
        "1234567890123456",
        "1111222233334444",
        "",  # пустой номер
        "1234",  # короткий номер
    ]


@pytest.fixture
def sample_account_numbers() -> list[str]:
    return [
        "73654108430135874305",
        "1234567890",
        "98765432109876543210",
        "",  # пустой номер
    ]


@pytest.fixture
def sample_mask_account_card_inputs() -> list[str]:
    return [
        "Visa Platinum 7000792289606361",
        "Mastercard 1234567890123456",
        "Maestro 1111222233334444",
        "Счет 73654108430135874305",
        "Account 12345678901234567890",
        "Счёт 98765432109876543210",
        "UnknownType 123456789",
        "NoNumberHere",
        "",
    ]


@pytest.fixture
def sample_dates() -> list[str]:
    return [
        "2024-03-11T02:26:18.671407",
        "1999-12-31T23:59:59.000000",
        "2000-01-01T00:00:00",
        "",  # пустая дата
        "invalid-date-format",
    ]
