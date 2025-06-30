from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("", ""),
        ("1234", ""),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234567890", "**7890"),
        ("", ""),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
