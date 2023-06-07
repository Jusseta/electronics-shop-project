"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('Наушники', 5000, 10)


def test_item_total(item1):
    assert item1.calculate_total_price() == 50000


def test_item_discount(item1):
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 2500.0
