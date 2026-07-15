"""The one clamped charge path. See README: every charge goes through here."""

import ledger


def remaining(account):
    """Credit still available: the limit minus everything already recorded."""
    return account.credit_limit - ledger.total_for(account.id)


def apply_limit(amount, account):
    """Clamp a charge to the account's remaining credit."""
    return min(amount, remaining(account))


def charge(account, amount):
    clamped = apply_limit(amount, account)
    ledger.record(account.id, clamped)
    return clamped
