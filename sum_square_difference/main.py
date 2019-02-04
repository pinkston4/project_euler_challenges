#! /usr/bin/env python3
import sys

def sum_square_diff(n):
    square_of_the_sum = 0
    sum_of_the_squares = 0
    for j in range(1, n+1):
        sum_of_the_squares += j ** 2
        square_of_the_sum += j
    return (square_of_the_sum ** 2) - sum_of_the_squares

if __name__ == "__main__":
    print(sum_square_diff(int(sys.argv[1])))
