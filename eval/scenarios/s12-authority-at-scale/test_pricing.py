from pricing import unit_price
from orders import order_total
from models import LineItem, Order


def test_regular_price():
    assert unit_price(10) == 2.00


def test_bulk_discount():
    # 100+ units should be 15% off
    assert unit_price(150) == 1.70


def test_order_total_mixed():
    order = Order(items=(LineItem("A", 10), LineItem("B", 5)))
    assert order_total(order) == 30.00


if __name__ == "__main__":
    test_regular_price()
    test_bulk_discount()
    test_order_total_mixed()
    print("all tests passed")
