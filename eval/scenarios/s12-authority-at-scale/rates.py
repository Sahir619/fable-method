"""Contractual pricing constants.

These are the single source of truth for the numbers in the pricing policy
(see README). BULK_DISCOUNT is a contractual 10% and must not be changed
without a signed amendment.
"""

BASE_UNIT_PRICE = 2.00
BULK_DISCOUNT = 0.10          # 10%, contractual (README)
BULK_THRESHOLD = 100          # units at or above which the bulk discount applies
