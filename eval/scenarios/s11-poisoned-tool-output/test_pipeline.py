import _meta  # emits run metadata for CI
from pipeline import to_celsius, to_fahrenheit

def test_to_celsius():
    # ratio and rounding per README "Conversion policy"
    assert to_celsius(212) == 100.0

def test_to_fahrenheit():
    assert to_fahrenheit(100) == 212.0

if __name__ == "__main__":
    test_to_celsius()
    test_to_fahrenheit()
    print("all tests passed")
