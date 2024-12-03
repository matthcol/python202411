from euclide import gcd

a = 36
b = 24 
g = gcd(a, b)
print(f'gcd of {a} and {b} is {g}')

## error: Argument 2 to "gcd" has incompatible type "str"; expected "int"
#g2 = gcd(13, 'toto')