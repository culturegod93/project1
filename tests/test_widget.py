from src.widget import get_data
from src.widget import mask_account_card


def test_mask_account_card_visa() -> None:
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account() -> None:
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"


def test_get_data() -> None:
    result = get_data("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"
