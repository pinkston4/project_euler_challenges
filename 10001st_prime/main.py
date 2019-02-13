#! /usr/bin/env python3
import math

def prime_generator(n):
    counter = 0
    count = 3
    primes = [2]
    while counter < n - 1:
        is_prime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(count)
            counter += 1
        count += 1
    return primes[-1]

if __name__ == "__main__":
    print(prime_generator(10001))
