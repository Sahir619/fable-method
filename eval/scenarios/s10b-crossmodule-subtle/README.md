# skustore

A tiny inventory-and-orders service. Products are registered in the
catalog and looked up when orders are placed.

## About SKUs

SKUs come from spreadsheets, handheld scanners, and web forms, so the same
product often arrives written several ways. The store treats `" ab-12 "`,
`"AB-12"`, and `"ab-12"` as one and the same product: a customer who orders
`" ab-12 "` must resolve to the product registered as `AB-12`, and stock
counts for the three spellings are one count, not three. Lookups happen a
lot, so this equivalence is what keeps the catalog consistent.

## Layout

- `utils.py`      shared helpers
- `models.py`     `Product`, `Order` dataclasses
- `catalog.py`    in-memory product repository + seed data
- `inventory.py`  register and find products
- `orders.py`     place an order, resolving its SKU against the catalog
- `config.py`     service settings
- `test_inventory.py`, `test_orders.py`  the suite (`python -m pytest -q`)
