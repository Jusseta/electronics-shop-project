"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item1():
    return Item('Наушники', 5000, 10)

@pytest.fixture
def item2():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_item_total(item1):
    assert item1.calculate_total_price() == 50000


def test_item_discount(item1):
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 2500.0


def test_name(item1):
    assert item1.name == 'Наушники'
    item1.name = "Лампа"
    assert item1.name == "Лампа"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item_all = Item.all[2]
    assert item_all.name == 'Кабель'
    assert item_all.price == 10
    assert item_all.quantity == 5


def test_string_to_number():
    assert Item.string_to_number('100') == 100
    assert Item.string_to_number('10.00') == 10
    assert Item.string_to_number('10.11') == 10


def test__repr__(item1):
    assert repr(item1) == "Item('Наушники', 5000, 10)"
    item2 = Item("Смартфон", 10000, 20)
    assert repr(item2) == "Item('Смартфон', 10000, 20)"


def test__str__(item1):
    assert str(item1) == 'Наушники'
    item2 = Item("Смартфон", 10000, 20)
    assert str(item2) == 'Смартфон'


def test__add__(item1, item2):
    assert item1 + item2 == 15
    item2.quantity = 3
    assert item1 + item2 == 13
