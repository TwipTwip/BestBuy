import pytest

from BestBuy.products import Product


def test_creating_prod():
    prod = Product("Item", 50, 1000)
    assert prod.is_active() is True


def test_creating_prod_invalid_details():
    with pytest.raises(TypeError):
        assert Product(50, 100) is TypeError


def test_prod_becomes_invalid():
    product = Product("Item2", 50, 0)
    assert product.is_active() is False


def test_buy_modifies_quantity():
    item = Product("Item3", 50, 100)
    item.buy(50)
    assert item.get_quantity() != 100


def test_buy_too_much():
    thing = Product("Item4", 50, 100)
    with pytest.raises(AssertionError):
        thing.buy(101)


pytest.main()
