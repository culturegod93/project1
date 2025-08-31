import logging
from pathlib import Path
from typing import Any

import pandas as pd

# Создаём папку logs, если её нет
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
    Считать CSV-файл и вернуть список транзакций.

    Возвращает пустой список, если файл пустой или произошла ошибка.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            logger.warning(f"CSV-файл пустой: {file_path}")
            return []
        result: list[dict[str, Any]] = [{str(k): v for k, v in row.items()} for row in df.to_dict(orient="records")]
        logger.debug(f"CSV-файл успешно прочитан: {file_path}, строк: {len(result)}")
        return result
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла {file_path}: {e}")
        return []


def read_excel(file_path: str) -> list[dict[str, Any]]:
    """
    Считать Excel-файл и вернуть список транзакций.

    Возвращает пустой список, если файл пустой или произошла ошибка.
    """
    try:
        df = pd.read_excel(file_path)
        if df.empty:
            logger.warning(f"Excel-файл пустой: {file_path}")
            return []
        result: list[dict[str, Any]] = [{str(k): v for k, v in row.items()} for row in df.to_dict(orient="records")]
        logger.debug(f"Excel-файл успешно прочитан: {file_path}, строк: {len(result)}")
        return result
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла {file_path}: {e}")
        return []
