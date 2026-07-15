import ledger
import billing
from accounts import Account


def test_direct_charge_clamps_to_remaining():
    ledger.reset()
    acct = Account("A", 100)
    ledger.record("A", 40)                 # 40 already used
    recorded = billing.charge(acct, 80)    # remaining is 60, so clamp to 60
    assert recorded == 60
    assert ledger.total_for("A") == 100


def test_direct_charge_under_limit_records_full():
    ledger.reset()
    acct = Account("B", 100)
    recorded = billing.charge(acct, 30)
    assert recorded == 30
    assert ledger.total_for("B") == 30


if __name__ == "__main__":
    test_direct_charge_clamps_to_remaining()
    test_direct_charge_under_limit_records_full()
    print("billing: all tests passed")
