"""Order totals built from unit prices."""

from pricing import unit_price


def order_total(order):
    return round(sum(unit_price(item.quantity) * item.quantity for item in order.items), 2)
