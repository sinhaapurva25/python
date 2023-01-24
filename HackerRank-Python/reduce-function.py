from fractions import Fraction
from functools import reduce

def product(fracs):
    n = 1
    d = 1
    for i in fracs:
        n *= i.numerator
        d *= i.denominator
    t = Fraction(n, d)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)