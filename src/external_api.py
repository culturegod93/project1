import os
from typing import Any
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env

API_KEY: str = os.getenv("EXCHANGE_API_KEY", "")
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Если транзакция в USD или EUR, обращается к Exchange Rates Data API.
    Возвращает сумму в рублях (float).
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    if currency not in {"USD", "EUR"}:
        return float(amount)

    headers = {"apikey": API_KEY}
    params = {"from": currency, "to": "RUB", "amount": amount}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return float(data.get("result", 0.0))
    except Exception:
        return float(amount)  # В случае ошибки возвращаем исходную сумму
