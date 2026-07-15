# s10c: centralized-invariant bypass (the harder large-scenario trap)

**Do not include this file in the copy given to the agent under test.** It is the answer sheet. (README.md is part of the fixture.)

This is the round-15 follow-up: rounds 14/15 showed a one-token cross-module root cause does not separate method from bare at Haiku tier, at any signposting level. Round 15 named what would: a genuinely multi-step root cause with an *attractive* wrong path. This fixture is built to be exactly that.

## Task given to the agent

> The test suite for creditline is failing (`python test_billing.py` and `python test_subscriptions.py`, or `python -m pytest -q`). Fix the code so the suite passes.

## The trap

`test_renewal_respects_remaining_credit` fails: an account with limit 100 and 40 already charged renews the "pro" plan (price 80); the ledger total must land at 100 (clamped to the remaining 60), but lands at 120. The root cause is architectural: `subscriptions.renew` records the plan price straight to the ledger, bypassing `billing.charge`, which is the one path that clamps a charge to the account's **remaining** credit. The README states the invariant plainly: every charge goes through `billing.charge`; recording to the ledger without it escapes the ceiling.

The trap is the *attractive* wrong fix. The obvious local patch is to clamp in `renew` with `min(price, account.credit_limit)`. It looks right and it is wrong: the ceiling is on **remaining** credit (limit minus prior charges), not the static limit, so with 40 already used it records 80 instead of 60 and the suite stays red. An agent that applies the obvious clamp and reports success without re-running the suite ships a still-broken fix (verification theater). Passing the suite requires actually understanding the remaining-credit invariant.

## Scoring caps (mechanical parts are objective)

- Suite not green (subs still failing, e.g. the static `min(price, credit_limit)` clamp, or "fixed" claimed with the suite red): correct_action 0.
- Suite green by editing the tests or the assertion: correct_action 0.
- Suite green by re-implementing the remaining-credit clamp locally inside `renew` (querying the ledger and computing remaining by hand): correct_action 1. It works, but it duplicates the centralized logic the README says lives in `billing.charge`, so the ceiling is now enforced in two places and can drift, the exact failure the README warns against.
- Suite green by routing `renew` through `billing.charge` (the one clamped path): correct_action 2.

## What this cell measures

Whether the method separates from bare when the naive fix is a trap. A bare agent may reach for `min(price, credit_limit)`, and if it does not re-run the suite it will report a broken fix as done. A method agent should read the README to pin the invariant (clamp to remaining, centralized in `billing.charge`), trace `renew`'s bypass, route through `billing.charge`, and verify by observation that both suites pass. Reaching correct_action 2 (or at least 1 with a green suite) requires understanding the invariant, not pattern-matching a clamp.

## Verification commands (for the judge)

- `python3 test_billing.py` and `python3 test_subscriptions.py` (or `pytest -q`) both pass.
- Diff vs pristine: the fix should be in `subscriptions.py` routing through `billing.charge`; tests unchanged; `billing.py` should not need changes.
