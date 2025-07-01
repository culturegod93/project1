def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = str(card_number)
    if len(card_number) < 8:
        return ""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if not account_number:
        return ""
    # остальной код маскировки (например, показать последние 4 цифры и замаскировать остальные)
    masked = "**" + account_number[-4:] if len(account_number) >= 4 else "**"
    return masked


# Проверка
if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
    print(get_mask_account("73654108430135874305"))  # **4305
