"""
DESC: Calculate the n'th fibonacci number
Author: Nagesh N Nazare
Date: 31-05-2021

RUN: 
python3 ./1.fibonacci.py

NOTE:
index:      0 1 2 3 4 5 6 7  8  9  10 11 
fibonacci:  0 1 1 2 3 5 8 13 21 34 55 89

OUTPUT: 
The fibonacci number is : 55
"""


def fibonacci(n):
    assert n >= 0 and int(n) == n, "n must be positive integer number"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    print(f'The fibonacci number is : ', str(fibonacci(10)))


if __name__ == '__main__':
    main()
