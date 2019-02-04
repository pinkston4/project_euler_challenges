#! /usr/bin/env python3

def solution(n, check):
    for num in range(n, 999999999, n):
        if all((num % j == 0 for j in check)):
            return num
    return None

if __name__ == "__main__":
    checklist = [11, 13, 14, 16, 17, 18, 19, 20]
    print(solution(20, checklist))
