"""Order pricing for ShopNorth checkout (fictional example company)."""
from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal

from checkout.models import Cart, Customer

TAX_RATE = Decimal("0.13")
CENT = Decimal("0.01")
LOYALTY_PERCENT = {"bronze": 5, "silver": 10, "gold": 15}


def subtotal(cart: Cart) -> Decimal:
    return sum((item.price * item.quantity for item in cart.items), Decimal("0"))


def loyalty_percent(customer: Customer) -> int:
    """Loyalty members get a discount by tier. Guests and unknown tiers get no discount."""
    tier = customer.profile.get("tier")
    return LOYALTY_PERCENT.get(tier, 0)


def order_total(cart: Cart) -> Decimal:
    """Subtotal minus the loyalty discount, plus tax, rounded to the cent."""
    discounted = subtotal(cart) * (100 - loyalty_percent(cart.customer)) / 100
    return (discounted * (1 + TAX_RATE)).quantize(CENT, rounding=ROUND_HALF_UP)
