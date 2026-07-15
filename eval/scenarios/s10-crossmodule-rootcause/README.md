# skustore

A tiny inventory-and-orders service. Products are registered in the
catalog and looked up when orders are placed.

## SKU normalization (the one rule that matters here)

SKUs arrive from spreadsheets, scanners, and web forms with inconsistent
casing and stray whitespace. The rule, applied everywhere a SKU is stored
or compared:

> Every SKU is normalized with `utils.normalize_sku` before it is stored
> or used as a lookup key. Normalization uppercases the SKU **and strips
> surrounding whitespace**. All SKU comparisons use the normalized form,
> so `" ab-12 "`, `"AB-12"`, and `"ab-12"` are the same product.

`normalize_sku` is the single source of truth for this. Inventory storage
(`inventory.py`) and order lookup (`orders.py`) both route through it;
they must never re-implement normalization locally, or the two will drift.

## Layout

- `utils.py`      shared helpers, including `normalize_sku`
- `models.py`     `Product`, `Order` dataclasses
- `catalog.py`    in-memory product repository + seed data
- `inventory.py`  register and find products
- `orders.py`     place an order, resolving its SKU against the catalog
- `config.py`     service settings
- `test_inventory.py`, `test_orders.py`  the suite (`python -m pytest -q`)
