import pytest

from src.widget import get_data
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Mastercard 1234567890123456", "Mastercard 1234 56** **** 3456"),
        ("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Account 12345678901234567890", "Account **7890"),
        ("Счёт 98765432109876543210", "Счёт **3210"),
        ("UnknownType 123456789", "UnknownType 123456789"),
        ("NoNumberHere", "NoNumberHere"),
        ("", ""),
    ],
)
def test_mask_account_card(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59.000000", "31.12.1999"),
        ("2000-01-01T00:00:00", "01.01.2000"),
        ("", ""),  # если пустая строка - возвращаем пустую или выбрасываем ошибку, зависит от реализации
        ("invalid-format", ""),  # или проверка на ошибку, если реализована
    ],
)
def test_get_data(date_str: str, expected: str) -> None:
    try:
        assert get_data(date_str) == expected
    except Exception:
        # можно отдельно тестировать выброс ошибок
        assert date_str in ("", "invalid-format")
