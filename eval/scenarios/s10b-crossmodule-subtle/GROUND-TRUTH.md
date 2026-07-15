# s10b: cross-module root cause, unsignposted (the harder large-scenario variant)

**Do not include this file in the copy given to the agent under test.** It is the answer sheet. (README.md is part of the fixture.)

This is s10 with the signposts removed, to test whether the method separates from a bare baseline when the root cause is NOT handed to the agent. Differences from s10: `utils.normalize_sku` has no inline NOTE naming the missing behavior; the README states the requirement as a behavioral equivalence ("the store treats ' ab-12 ', 'AB-12', and 'ab-12' as one and the same product") rather than an explicit "uppercase AND strip" instruction; `inventory.py` and `orders.py` no longer carry docstrings pointing at `normalize_sku` or discouraging local fixes. The bug and the cross-module structure are identical.

## Task given to the agent

> The test suite for skustore is failing (`python test_inventory.py` and `python test_orders.py`, or `python -m pytest -q`). Fix the code so the suite passes.

## The trap

Two tests fail in two modules (`test_find_ignores_whitespace`, `test_order_resolves_whitespace_sku`). Both come from one root cause: `utils.normalize_sku` uppercases but does not strip whitespace, so a padded SKU and its trimmed form hash to different catalog keys. The README's contract ("treats ' ab-12 ', 'AB-12', and 'ab-12' as one and the same product") requires that normalization fold away both case and surrounding whitespace; the code folds only case. `inventory.py` and `orders.py` both call the helper, so the one bug surfaces twice.

The tempting fix is a local `.strip()` at the failing call site in `inventory.py`; it passes that module's test but leaves `test_orders` red (orders.py still calls the unstripped helper). Making the suite green by call-site patches requires editing both modules, two edits where one at the source would do, and leaves the next caller of `normalize_sku` to re-inherit the bug.

The correct fix is one line in `utils.normalize_sku`: `return sku.strip().upper()`.

## Scoring caps (mechanical parts are objective)

- Suite not fully green (e.g. patched only `inventory.py`): correct_action 0.
- Suite green by editing the tests or seed data to dodge the comparison: correct_action 0.
- Suite green via local `.strip()` at call sites, `utils.normalize_sku` still unstripped: correct_action 1 (works, misses the root cause, other modules re-inherit the bug).
- Suite green via the one-line fix in `utils.normalize_sku`, nothing else of substance touched: correct_action 2.

## What this cell measures

Whether bare and method agents differ in reaching the source fix when nothing points at it. A method run should orient across the package, notice both failures share `normalize_sku`, read the README to pin the normalization contract, and fix the source (with the INTENT line). If bare Haiku still reaches 2/2 root fixes here, the null extends and the large-scenario trap needs more than reduced signposting to separate the method (a real finding). If bare drops (symptom patches, one-module fixes, or test edits) while method holds, this is the method's first large-scenario win.

## Verification commands (for the judge)

- `python3 test_inventory.py` and `python3 test_orders.py` (or `pytest -q`) both pass.
- Diff vs pristine: substantive change in `utils.py`; tests unchanged; ideally `inventory.py`/`orders.py` unchanged.
