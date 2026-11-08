"""Guard tests added after the 2:04 a.m. checkout incident. CI runs them on every pull request.

A good fix: a missing or unknown tier means a 0% loyalty discount. Guests pay full price.
A lazy fix that catches the error and makes the order free must fail here.
"""
from decimal import Decimal

import pytest

from checkout.models import Cart, Customer, Item
from checkout.pricing import order_total

ITEMS = (Item("mug", Decimal("12.00"), 2), Item("tea", Decimal("6.00")))  # subtotal 30.00
FULL_PRICE = Decimal("33.90")                                             # 30.00 + 13% tax

GUEST = Customer("g1", guest=True)
UNKNOWN_TIER = Customer("c9", profile={"tier": "platinum"})
NO_PROFILE = Customer("c8")
GOLD = Customer("c2", profile={"tier": "gold"})


@pytest.mark.parametrize("customer", [GUEST, UNKNOWN_TIER, NO_PROFILE], ids=["guest", "unknown-tier", "no-profile"])
def test_customers_without_a_known_tier_pay_full_price(customer):
    assert order_total(Cart(customer, ITEMS)) == FULL_PRICE


@pytest.mark.parametrize("customer", [GUEST, UNKNOWN_TIER, NO_PROFILE, GOLD], ids=["guest", "unknown", "none", "gold"])
def test_no_order_is_ever_free(customer):
    assert order_total(Cart(customer, ITEMS)) > 0


def test_members_still_get_their_discount():
    assert order_total(Cart(GOLD, ITEMS)) == Decimal("28.82")
