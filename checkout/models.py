"""Data shapes for ShopNorth checkout. ShopNorth is a fictional example company."""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class Item:
    sku: str
    price: Decimal
    quantity: int = 1


@dataclass(frozen=True)
class Customer:
    id: str
    guest: bool = False
    profile: dict = field(default_factory=dict)  # members: {"tier": "bronze" | "silver" | "gold"}


@dataclass(frozen=True)
class Cart:
    customer: Customer
    items: tuple[Item, ...]
