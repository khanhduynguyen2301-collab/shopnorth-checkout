from decimal import Decimal

from checkout.models import Cart, Customer, Item
from checkout.pricing import loyalty_percent, order_total, subtotal

BRONZE = Customer("c1", profile={"tier": "bronze"})
GOLD = Customer("c2", profile={"tier": "gold"})


def cart_for(customer: Customer) -> Cart:
    return Cart(customer=customer, items=(Item("mug", Decimal("12.00"), 2), Item("tea", Decimal("6.00"))))


def test_subtotal_adds_up_items():
    assert subtotal(cart_for(BRONZE)) == Decimal("30.00")


def test_loyalty_percent_by_tier():
    assert loyalty_percent(BRONZE) == 5
    assert loyalty_percent(GOLD) == 15


def test_total_applies_discount_then_tax():
    assert order_total(cart_for(BRONZE)) == Decimal("32.21")  # 30.00 - 5% = 28.50, + 13% tax
    assert order_total(cart_for(GOLD)) == Decimal("28.82")    # 30.00 - 15% = 25.50, + 13% tax


def test_guest_checkout_pays_full_price():
    """Incident 2:04 a.m.: guests have no loyalty tier and checkout crashed."""
    guest = Customer("g1", guest=True)
    assert order_total(cart_for(guest)) == Decimal("33.90")  # 30.00 + 13% tax, no discount
