from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


def test_filter_by_currency_usd(sample_currency_data):
    result = list(filter_by_currency(sample_currency_data, currency="USD"))
    ids = [item["id"] for item in result]
    assert ids == [1, 3]


def test_filter_by_currency_eur(sample_currency_data):
    result = list(filter_by_currency(sample_currency_data, currency="EUR"))
    ids = [item["id"] for item in result]
    assert ids == [2]


def test_filter_by_currency_not_found(sample_currency_data):
    result = list(filter_by_currency(sample_currency_data, currency="RUB"))
    assert result == []


def test_transaction_descriptions(sample_description_data):
    result = list(transaction_descriptions(sample_description_data))
    assert result == ["Оплата заказа", "Возврат средств"]


def test_card_number_generator_basic():
    result = list(card_number_generator(1, 4))
    assert result == ["0000000000000001", "0000000000000002", "0000000000000003"]
