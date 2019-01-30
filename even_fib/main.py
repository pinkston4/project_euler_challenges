#! /usr/bin/env python3

def sum_of_even_fib():
    fib = [0, 1]
    index = 0
    while fib[-1] < 4000000:
        fib.append(fib[index] + fib[index+1])
        index += 1
    print(sum([x for x in fib if x % 2 == 0]))

if __name__ == "__main__":
    sum_of_even_fib()

