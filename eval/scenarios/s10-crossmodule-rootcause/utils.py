"""Shared helpers for skustore.

normalize_sku is the single source of truth for SKU normalization (see
README): uppercase AND strip surrounding whitespace. inventory.py and
orders.py both depend on it; do not re-implement normalization elsewhere.
"""


def normalize_sku(sku):
    # NOTE: per README, this must uppercase AND strip surrounding whitespace.
    return sku.upper()


def money(amount):
    return round(amount, 2)
