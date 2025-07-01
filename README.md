# Project 1

## Описание:

Project 1 - виджет на Python для банковских операций.

## Структура проекта:

Project 1
├── src
│ ├── init.py
│ ├── masks.py
│ ├── widget.py
│ └── processing.py
├── tests
│ ├── init.py
│ ├── conftest.py
│ ├── masks_test.py
│ ├── widget_test.py
│ └── processing_test.py
├── .coverage
├── .flake8
├── .gitignore
├── README.md
├── poetry.lock
└── poetry.toml

## Тестирование:

В проекте реализованы автоматические тесты с использованием pytest и фикстур.

1. Запуск тестов:
poetry run pytest

2. Проверка покрытия:
poetry run pytest --cov=src

Тестируемые модули: masks.py, widget.py, processing.py.

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
