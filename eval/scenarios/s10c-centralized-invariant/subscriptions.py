"""Subscription renewal."""

import ledger
from plans import price_of


def renew(account, plan_name):
    price = price_of(plan_name)
    ledger.record(account.id, price)
    return price
