from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234567890") == "**7890"
    assert get_mask_account("1234567890") == "**7890"
