# Project 1

## Описание:

Project 1 - виджет на Python для банковских операций.

## Структура проекта:

Project 1
├── data
│ ├── transactions.csv
│ ├── transactions_excel.xlsx
│ └── operations.json
├── htmlcov
│ └── index.html
├── logs
├── src
│ ├── init.py
│ ├── decorators.py
│ ├── external_api.py
│ ├── file_readers.py
│ ├── filters.py
│ ├── generators.py
│ ├── main.py
│ ├── masks.py
│ ├── processing.py
│ ├── utils.py
│ └── widget.py
├── tests
│ ├── init.py
│ ├── conftest.py
│ ├── decorators_test.py
│ ├── external_api_test.py
│ ├── file_readers_test.py
│ ├── filters_test.py
│ ├── generators_test.py
│ ├── masks_test.py
│ ├── processing_test.py
│ ├── utils_test.py
│ └──  widget_test.py
├── .coverage
├── .env.template
├── .flake8
├── .gitignore
├── README.md
├── poetry.lock
└── poetry.toml

## Тестирование:

В проекте реализованы автоматические тесты с использованием pytest, фикстур, mock и patch. Добавлен новый тест (filters_test.py).

1. Запуск тестов:
~~~
poetry run pytest
~~~

2. Проверка покрытия:
~~~
poetry run pytest --cov=src
~~~

Тестируемые модули: decorators.py, external_api.py, file_readers.py, filters.py, generators.py, masks.py, processing.py, utils.py, widget.py. 

Используется: параметризация и фикстуры (conftest.py).

## Ссылка:

[GitHub](https://github.com/culturegod93/project1)

## Установка:

1. Клонируйте репозиторий:
~~~
git clone https://github.com/culturegod93/project1
~~~
2. Установите зависимости:
~~~
poetry install
~~~

## Документация:

Дополнительная информация о проекте в README.md.

## Разработчик:

Дмитрий Смирнов.

## Лицензия

Проект лицензирован по лицензии MIT.
