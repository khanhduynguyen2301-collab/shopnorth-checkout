"""Order pricing for ShopNorth checkout (fictional example company)."""
from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal

from checkout.models import Cart

TAX_RATE = Decimal("0.13")
CENT = Decimal("0.01")


def subtotal(cart: Cart) -> Decimal:
    return sum((item.price * item.quantity for item in cart.items), Decimal("0"))


def order_total(cart: Cart) -> Decimal:
    """Subtotal plus tax, rounded to the cent."""
    return (subtotal(cart) * (1 + TAX_RATE)).quantize(CENT, rounding=ROUND_HALF_UP)
