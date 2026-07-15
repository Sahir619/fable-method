import ledger
import subscriptions
from accounts import Account


def test_renewal_respects_remaining_credit():
    # Account limit 100, already 40 used. Renewing "pro" (price 80) must be
    # clamped to the remaining 60, exactly like a direct charge, so the
    # ledger total lands at the ceiling and never above it.
    ledger.reset()
    acct = Account("A", 100)
    ledger.record("A", 40)
    subscriptions.renew(acct, "pro")
    assert ledger.total_for("A") == 100


if __name__ == "__main__":
    test_renewal_respects_remaining_credit()
    print("subscriptions: all tests passed")
