#! /usr/bin/env python3

from itertools import product

def palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    m = ((a, b) for a, b in product(range(100, 999), repeat=2) if palindrome(a*b))
    z = max(m, key=lambda a: a[0]*a[1])
    print(z[0]*z[1])

