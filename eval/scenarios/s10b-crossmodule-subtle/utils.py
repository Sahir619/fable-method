"""Shared helpers for skustore."""


def normalize_sku(sku):
    """Return the canonical form of a SKU for storage and comparison."""
    return sku.upper()


def money(amount):
    return round(amount, 2)
