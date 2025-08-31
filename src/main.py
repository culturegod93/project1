from typing import Dict
from typing import List

from src.file_readers import read_csv
from src.file_readers import read_excel
from src.filters import process_bank_search
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import read_json


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Выбор (1/2/3): ").strip()
    data: List[Dict] = []

    if choice == "1":
        path = input("Введите путь к JSON-файлу: ").strip()
        data = read_json(path)
    elif choice == "2":
        path = input("Введите путь к CSV-файлу: ").strip()
        data = read_csv(path)
    elif choice == "3":
        path = input("Введите путь к XLSX-файлу: ").strip()
        data = read_excel(path)
    else:
        print("Некорректный выбор!")
        return

    if not data:
        print("Файл пуст или не найден.")
        return

    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = input(f"Введите статус для фильтрации ({', '.join(valid_states)}): ").strip().upper()
        if state in valid_states:
            data = filter_by_state(data, state)
            print(f'Операции отфильтрованы по статусу "{state}"')
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    sort_input = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_input == "да":
        order_input = input("Сортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = False if "возрастанию" in order_input else True
        data = sort_by_date(data, reverse)

    rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_only == "да":
        data = [item for item in data if "amount" in item and str(item.get("currency", "")).upper() == "RUB"]

    search_input = input("Фильтровать по слову в описании? Да/Нет: ").strip().lower()
    if search_input == "да":
        search_str = input("Введите слово для поиска: ").strip()
        data = process_bank_search(data, search_str)

    print("Распечатываю итоговый список транзакций...")
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(data)}")
    for item in data:
        desc = item.get("description", "")
        amount = item.get("amount", "")
        currency = item.get("currency", "")
        date = item.get("date", "")
        print(f"{date} {desc}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
