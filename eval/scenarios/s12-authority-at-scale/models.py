"""Data models for pricebook."""

from dataclasses import dataclass


@dataclass(frozen=True)
class LineItem:
    sku: str
    quantity: int


@dataclass(frozen=True)
class Order:
    items: tuple
