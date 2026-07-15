from inventory import register_product
from orders import order_total, resolve


def test_order_total_basic():
    # AB-12 is seeded in the catalog at price 9.99.
    assert order_total("AB-12", 2) == 19.98


def test_order_resolves_whitespace_sku():
    # Product registered clean; the order carries a padded, lowercased SKU.
    # Per the README they are the same product, so the lookup must resolve.
    register_product("ij-90", "Flange", 5.0)
    assert resolve("  ij-90  ").name == "Flange"


if __name__ == "__main__":
    test_order_total_basic()
    test_order_resolves_whitespace_sku()
    print("orders: all tests passed")
