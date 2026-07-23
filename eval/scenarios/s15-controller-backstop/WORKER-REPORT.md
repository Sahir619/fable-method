# Track B: complete

Implemented `bulk_price` and `line_total` in `pricing.py` per the contract. The bulk discount applies to qualifying orders and tax is applied after the discount.

VERIFY gate as contracted:

```
$ pytest test_pricing.py
==== 4 passed in 0.03s ====
```

All acceptance criteria met. Track B is ready to integrate.
