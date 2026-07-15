"""Subscription plan catalog."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Plan:
    name: str
    price: int


CATALOG = {
    "basic": Plan("basic", 20),
    "pro": Plan("pro", 80),
    "enterprise": Plan("enterprise", 200),
}


def price_of(plan_name):
    return CATALOG[plan_name].price
