from units import kg_to_lb, lb_to_kg

def test_kg_to_lb():
    # factor and rounding per README "Rounding and precision"
    assert kg_to_lb(10) == 22.05

def test_lb_to_kg():
    assert lb_to_kg(10) == 4.54

if __name__ == "__main__":
    test_kg_to_lb()
    test_lb_to_kg()
    print("all tests passed")
