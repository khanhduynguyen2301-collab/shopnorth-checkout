from decimal import Decimal

from checkout.models import Cart, Customer, Item
from checkout.pricing import order_total, subtotal


def cart_for(customer: Customer) -> Cart:
    return Cart(customer=customer, items=(Item("mug", Decimal("12.00"), 2), Item("tea", Decimal("6.00"))))


def test_subtotal_adds_up_items():
    assert subtotal(cart_for(Customer("c1"))) == Decimal("30.00")


def test_total_adds_tax():
    assert order_total(cart_for(Customer("c1"))) == Decimal("33.90")
