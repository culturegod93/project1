from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция обработки и маскировки, в зависимости от типа"""
    info = str(info)
    parts = info.strip().split()
    name = parts[0]
    number = " ".join(parts[1:])

    if name.lower() in ["visa", "mastercard", "maestro"] or len(number) == 16:
        masked = get_mask_card_number(number)
    elif name.lower() in ["account", "счет", "счёт"] or len(number) > 16:
        masked = get_mask_account(number)

    return f"{name} {masked}"


def get_data(date: str) -> str:
    """Функция преобразования даты"""
    date_part = date.split("T")[0]
    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"


# Проверка
if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305
    print(get_data("2024-03-11T02:26:18.671407"))  # 11.03.2024
