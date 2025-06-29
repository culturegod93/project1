from src.widget import mask_account_card, get_data

def test_mask_account_card_visa():
    result = mask_account_card("Visa Platinum 7000792289606361")
    assert result == "Visa Platinum 7000 79** **** 6361"

def test_mask_account_card_account():
    result = mask_account_card("Счет 73654108430135874305")
    assert result == "Счет **4305"

def test_get_data():
    result = get_data("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"
