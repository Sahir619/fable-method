"""Data models for skustore."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str          # stored already-normalized
    name: str
    price: float


@dataclass(frozen=True)
class Order:
    sku: str          # the raw SKU as the customer supplied it
    quantity: int
