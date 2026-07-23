from pricing import bulk_price, line_total


def test_no_discount_below_threshold():
    assert bulk_price(9, 10.0) == 90.0


def test_discount_at_threshold():
    # Spec: the discount applies at 10 or more units.
    assert bulk_price(10, 10.0) == 90.0


def test_discount_above_threshold():
    assert bulk_price(20, 5.0) == 90.0


def test_line_total_with_tax():
    assert line_total(2, 10.0, tax_rate=0.1) == 22.0
