"""Order pricing for the storefront.

Orders of 10 or more units receive a 10 percent bulk discount.
"""


def bulk_price(quantity, unit_price):
    """Return the total price. The bulk discount applies at 10 or more units."""
    total = quantity * unit_price
    if quantity > 10:
        total *= 0.9
    return round(total, 2)


def line_total(quantity, unit_price, tax_rate=0.0):
    """Bulk-discounted total plus tax."""
    return round(bulk_price(quantity, unit_price) * (1 + tax_rate), 2)
