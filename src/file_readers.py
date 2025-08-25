import logging
from pathlib import Path
from typing import Any
import pandas as pd


# Создаем папку logs, если её нет
Path("logs").mkdir(exist_ok=True)

# Настраиваем логгер для модуля file_readers
logger = logging.getLogger("file_readers")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/file_readers.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv(file_path: str) -> list[dict[str, Any]]:
    """
    Прочитать CSV-файл с транзакциями и вернуть список словарей.

    Возвращает пустой список, если:
    - файл не найден;
    - файл пустой;
    - произошла ошибка при чтении.

    :param file_path: путь к CSV-файлу
    :return: список словарей с транзакциями или []
    """
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        logger.error(f"CSV-файл не найден или не является файлом: {file_path}")
        return []

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            logger.warning(f"CSV-файл пустой: {file_path}")
            return []
        data = df.to_dict(orient="records")
        logger.debug(f"CSV-файл успешно прочитан: {file_path}, количество записей: {len(data)}")
        return data
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла {file_path}: {e}")
        return []


def read_excel(file_path: str) -> list[dict[str, Any]]:
    """
    Прочитать Excel-файл с транзакциями и вернуть список словарей.

    Возвращает пустой список, если:
    - файл не найден;
    - файл пустой;
    - произошла ошибка при чтении.

    :param file_path: путь к Excel-файлу
    :return: список словарей с транзакциями или []
    """
    path = Path(file_path)
    if not path.exists() or not path.is_file():
        logger.error(f"Excel-файл не найден или не является файлом: {file_path}")
        return []

    try:
        df = pd.read_excel(file_path)
        if df.empty:
            logger.warning(f"Excel-файл пустой: {file_path}")
            return []
        data = df.to_dict(orient="records")
        logger.debug(f"Excel-файл успешно прочитан: {file_path}, количество записей: {len(data)}")
        return data
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла {file_path}: {e}")
        return []
