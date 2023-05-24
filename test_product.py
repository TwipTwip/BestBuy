import pytest

from BestBuy.products import Product


def test_creating_prod():
    assert Product("Item", 50, 1000)


def test_creating_prod_invalid_details():
    assert Product(50, 100)


def test_prod_becomes_invalid():
    product = Product("Item2", 50, 0)
    assert product.is_active() is False


def test_buy_modifies_quantity():
    item = Product("Item3", 50, 100)
    item.buy(50)
    assert item.get_quantity() != 100


def test_buy_too_much():
    thing = Product("Item4", 50, 100)
    assert thing.buy(101)
