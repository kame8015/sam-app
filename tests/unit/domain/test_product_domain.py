import pytest

from app.domain.product import Product

def test_ok_product():
    # given
    name = "sample"
    price = 100
    stock = 20

    # when
    product = Product(name, price, stock)

    # then
    assert type(product) == Product
    assert product.name == name
    assert product.price == price
    assert product.stock == stock
