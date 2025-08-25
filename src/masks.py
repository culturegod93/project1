import logging
from pathlib import Path

# Создаём папку logs, если её нет
Path("logs").mkdir(exist_ok=True)

# Настраиваем логгер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    try:
        card_number = str(card_number)
        if len(card_number) < 8:
            logger.warning(f"Недостаточно цифр для маскировки карты: {card_number}")
            return ""
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.debug(f"Маскировка карты прошла успешно: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке карты {card_number}: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    try:
        if not account_number:
            logger.warning("Пустой номер счета")
            return ""
        masked = "**" + account_number[-4:] if len(account_number) >= 4 else "**"
        logger.debug(f"Маскировка счета прошла успешно: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке счета {account_number}: {e}")
        raise
