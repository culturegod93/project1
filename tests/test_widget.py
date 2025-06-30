from src.widget import get_data
from src.widget import mask_account_card


def test_mask_account_card_visa() -> None:
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account() -> None:
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"


def test_mask_account_card_mastercard() -> None:
    result = mask_account_card("Mastercard 1234567890123456")
    assert result == "Mastercard 1234 56** **** 3456"


def test_mask_account_card_maestro() -> None:
    result = mask_account_card("Maestro 9876543210987654")
    assert result == "Maestro 9876 54** **** 7654"


def test_mask_account_card_unknown_format() -> None:
    result = mask_account_card("NoDigitsHere")
    assert result == "NoDigitsHere"


def test_get_data() -> None:
    result = get_data("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"


def test_get_data_with_different_date() -> None:
    result = get_data("2023-12-31T23:59:59.999999")
    assert result == "31.12.2023"
