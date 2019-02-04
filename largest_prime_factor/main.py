#! /usr/bin/env python3
import sys


def largest_prime_fact(n):
    i = 2
    n = int(n)
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors[-1]

if __name__ == "__main__":
    print(largest_prime_fact(sys.argv[1]))

