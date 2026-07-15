"""Place orders. Read side of the catalog.

An order carries the raw SKU the customer supplied; we normalize it the
same way inventory.py did on the way in, so the lookup matches regardless
of casing or stray whitespace. Normalization is utils.normalize_sku's job.
"""

import catalog
import config
from utils import normalize_sku, money


class UnknownSku(Exception):
    pass


def resolve(order_sku):
    product = catalog.get(normalize_sku(order_sku))
    if product is None and config.STRICT_LOOKUP:
        raise UnknownSku(order_sku)
    return product


def order_total(order_sku, quantity):
    product = resolve(order_sku)
    return money(product.price * quantity)
