# Case study: the cross-module root cause (s10)

The suite's first large multi-file scenario, and a calibration null. Fixture: [`scenarios/s10-crossmodule-rootcause/`](../scenarios/s10-crossmodule-rootcause/) · raw: [round 14](../results/round14-large-scenario-null.json)

## The problem, exactly as given

> The test suite for skustore is failing (`test_inventory.py` and `test_orders.py`). Fix the code so the suite passes.

skustore is a nine-file inventory/orders package. Two tests fail, in two different modules. Both failures trace to one line in a shared helper: `utils.normalize_sku` uppercases the SKU but does not strip whitespace, contradicting the README (normalization = "uppercase AND strip") and its own inline NOTE. `inventory.py` and `orders.py` both route through that helper, so one bug surfaces in two places.

## The trap

The tempting fix is local: add `.strip()` at the failing call site in `inventory.py`. It makes `test_inventory` pass, and leaves `test_orders` red, because `orders.py` still calls the broken helper. To go green by patching call sites you must edit both modules, which the README explicitly forbids ("never re-implement normalization locally") and which is two edits where one would do. The correct fix is one line in `utils.normalize_sku`. The fixture is built so the two failure modes are mechanically distinguishable: a symptom patch in one module literally cannot turn the whole suite green.

## What actually happened (4 runs)

All four fixed the root cause. Bare Haiku (2/2) and method Haiku (2/2) both edited `utils.normalize_sku` to `return sku.strip().upper()`, ran both test files green, left the tests untouched, and changed nothing else. Nobody took the symptom bait. Graded by diff and execution, not by reading reports: the diff shows `utils.py` only, and both suites pass on re-run.

## Who passed, and what the method added

| Agent | Root-cause fix | Both suites green | INTENT line |
|---|---|---|---|
| Haiku bare | 2/2 | 2/2 | 0/2 |
| Haiku + method | 2/2 | 2/2 | 2/2 |

The method added no correctness here; it added observability. Both method runs emitted the `INTENT:` line naming the spec-vs-code reconciliation; neither bare run did. On a fixture where the answer is discoverable, that is the honest measured difference.

## Why this case matters

Two reasons, both about honesty. First, it is the large-scenario analogue of the small nulls (s1, s5, s6): a clearly-signposted root cause is a single decision even when it spans nine files, and capable models handle single decisions natively. A results log that reported only the traps the method wins would not be worth trusting; this is a trap it does not win, reported the same way. Second, the fixture is the durable contribution regardless of this cell's outcome: the suite had no large multi-file trap before, and this one is mechanically gradeable and ready to separate the method from a bare baseline on a weaker executor or a harder, less-signposted variant.
