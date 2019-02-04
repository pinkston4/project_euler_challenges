#! /usr/bin/env python3

def sum_of_multiples(n=1000):
    a = []
    for j in range(n):
        if j % 3 == 0 or j % 5 == 0:
            a.append(j)
    return sum(a)

if __name__ == "__main__":
    print(sum_of_multiples())
