"""
DESC: Calculate the factorial of a number n
Author: Nagesh N Nazare
Date: 31-05-2021

RUN: 
python3 ./1.factorial.py

NOTE: 
5! = 5 * 4 * 3 * 2 * 1 = 120

OUTPUT: 
The factorial of the number is : 120
"""

import sys
sys.setrecursionlimit(1000)


def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


def main():
    print(f'The factorial of the number is : ', str(factorial(5)))


if __name__ == '__main__':
    main()
