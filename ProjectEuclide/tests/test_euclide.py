from euclide import gcd


def test_gcd_1_1():
    g = gcd(1, 1)
    assert g == 1

def test_gcd_1_other():
    g = gcd(1, 27)
    assert g == 1
