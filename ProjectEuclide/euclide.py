# module euclide

def gcd(a: int, b: int) -> int:
    """compute gcd of a and b

    a and b must be natural integers, strictly positive
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

