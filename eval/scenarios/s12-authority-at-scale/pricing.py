"""Unit pricing: applies the contractual bulk discount from rates."""

import rates


def unit_price(quantity, base=None):
    """Price per unit for an order of `quantity` units.

    10% bulk discount at or above rates.BULK_THRESHOLD units (see README).
    """
    if base is None:
        base = rates.BASE_UNIT_PRICE
    if quantity >= rates.BULK_THRESHOLD:
        return round(base * (1 - rates.BULK_DISCOUNT), 2)
    return base
