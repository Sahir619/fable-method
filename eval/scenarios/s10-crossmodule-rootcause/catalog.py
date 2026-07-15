"""In-memory product repository plus seed data.

The catalog stores products keyed by their normalized SKU. It never
normalizes on its own; callers hand it already-normalized SKUs (that is
inventory.py's job on the write side and orders.py's on the read side).
"""

from models import Product

# Seed products. Keys are the normalized SKUs as inventory.py would store them.
_PRODUCTS = {
    "AB-12": Product(sku="AB-12", name="Widget", price=9.99),
    "CD-34": Product(sku="CD-34", name="Gadget", price=19.50),
    "EF-56": Product(sku="EF-56", name="Doohickey", price=4.25),
}


def get(normalized_sku):
    return _PRODUCTS.get(normalized_sku)


def put(product):
    _PRODUCTS[product.sku] = product


def all_skus():
    return sorted(_PRODUCTS)
