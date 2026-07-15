"""Register and find products. Write side of the catalog.

Per the README, every SKU is normalized through utils.normalize_sku
before it touches the catalog. Do not normalize by hand here.
"""

import catalog
from models import Product
from utils import normalize_sku


def register_product(sku, name, price):
    norm = normalize_sku(sku)
    product = Product(sku=norm, name=name, price=price)
    catalog.put(product)
    return product


def find_product(sku):
    return catalog.get(normalize_sku(sku))
