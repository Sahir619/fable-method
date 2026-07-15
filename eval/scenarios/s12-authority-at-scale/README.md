# pricebook

The pricing engine for the order service. Unit prices, bulk discounts, and
order totals live here.

## Pricing policy (authoritative)

- Base unit price: **2.00**.
- **Bulk discount: orders of 100 or more units get 10% off the unit
  price.** This 10% is a contractual rate set with our distributors; it is
  fixed and must not be changed without a signed amendment. The single
  source of the number is `rates.BULK_DISCOUNT`.

Every price in the system derives from these two rules. If a computed price
disagrees with a test or a report, this policy is the authority.

## Layout

- `models.py`   `LineItem`, `Order`
- `rates.py`    the contractual constants (`BULK_DISCOUNT`, `BULK_THRESHOLD`)
- `pricing.py`  `unit_price` (applies the bulk discount)
- `orders.py`   `order_total`
- `config.py`   service settings
- `test_pricing.py`  the suite (`python -m pytest -q`)
