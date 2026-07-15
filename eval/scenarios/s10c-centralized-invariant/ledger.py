"""Append-only ledger of recorded charges."""

_ENTRIES = []


def record(account_id, amount):
    _ENTRIES.append((account_id, amount))


def total_for(account_id):
    return sum(amount for (aid, amount) in _ENTRIES if aid == account_id)


def reset():
    _ENTRIES.clear()
