from inventory import register_product, find_product


def test_register_and_find_basic():
    register_product("kl-11", "Bracket", 2.0)
    assert find_product("KL-11").name == "Bracket"


def test_find_ignores_whitespace():
    # SKU arrives from a scanner with stray padding; per the README it is
    # the same product as its trimmed, upcased form.
    register_product("  gh-78  ", "Sprocket", 3.0)
    assert find_product("gh-78").name == "Sprocket"


if __name__ == "__main__":
    test_register_and_find_basic()
    test_find_ignores_whitespace()
    print("inventory: all tests passed")
