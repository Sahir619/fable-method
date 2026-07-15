"""Place orders. Read side of the catalog."""

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
