def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    account_number = str(account_number)

    return f"**{account_number[-4:]}"


# Проверка
if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
    print(get_mask_account("73654108430135874305"))  # **4305
