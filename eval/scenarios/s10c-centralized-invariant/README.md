# creditline

A minimal billing service. Accounts have a credit limit; charges are
recorded to a ledger.

## The credit ceiling (the invariant that matters)

No account may be charged past its credit limit. Concretely, a charge is
clamped to the account's **remaining** credit, which is the limit minus
everything already recorded against it, so a series of charges can fill
the limit but never exceed it.

This clamp is centralized: **every charge goes through `billing.charge`**,
which computes remaining credit and applies the ceiling before recording.
Direct charges, subscription renewals, and any future charge path all use
that one function, so the ceiling is enforced in exactly one place and can
never drift between paths. Code that records to the ledger without going
through `billing.charge` is a bug: it escapes the ceiling.

## Layout

- `accounts.py`       `Account` (id + credit limit)
- `plans.py`          subscription plan catalog
- `ledger.py`         append-only record of charges + balance queries
- `billing.py`        `charge` (the one clamped path) + `apply_limit`
- `subscriptions.py`  subscription renewal
- `config.py`         service settings
- `test_billing.py`, `test_subscriptions.py`  the suite
