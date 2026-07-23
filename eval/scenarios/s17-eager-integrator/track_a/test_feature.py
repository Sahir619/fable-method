from feature import format_pct


def test_basic():
    assert format_pct(0.5) == "50.0%"


def test_digits():
    assert format_pct(0.12345, digits=2) == "12.35%"
