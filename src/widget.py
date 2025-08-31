from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция обработки и маскировки, в зависимости от типа"""
    info = str(info)
    parts = info.strip().split()

    number_index = None
    for i, part in enumerate(parts):
        if part and part[0].isdigit():
            number_index = i
            break

    if number_index is None:
        return info

    name = " ".join(parts[:number_index])
    number = "".join(parts[number_index:])

    if name.lower().split()[0] in ["visa", "mastercard", "maestro"] or len(number) == 16:
        masked = get_mask_card_number(number)
    elif name.lower().split()[0] in ["account", "счет", "счёт"] or len(number) > 16:
        masked = get_mask_account(number)
    else:
        masked = number  # если не удалось определить тип — верни как есть

    return f"{name} {masked}"


def get_data(date: str) -> str:
    """Функция преобразования даты"""
    date_part = date.split("T")[0]
    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"
