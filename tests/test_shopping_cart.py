import pytest

from src.shopping_cart import Item, ShoppingCart


@pytest.fixture
def cart_with_items() -> ShoppingCart:
    item1 = Item(name="Apple", price=1)
    item2 = Item(name="Orange", price=2)

    cart = ShoppingCart()
    cart.add(item1)
    cart.add(item2)

    return cart

def test_item_can_get_price():
    item1 = Item(name="Apple", price=1)
    assert item1.price == 1

def test_shopping_cart_total(cart_with_items: ShoppingCart):
    assert cart_with_items.total() == 3


def test_shopping_cart_len(cart_with_items: ShoppingCart):
    assert len(cart_with_items) == 2