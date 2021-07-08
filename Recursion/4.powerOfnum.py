"""
DESC: Calculate the power of a number
Author: Nagesh N Nazare
Date: 31-05-2021

RUN: 
python3 ./4.powerOfnum.py

NOTE:
x^n = x * x^n-1
2^3 = 2 * 2^2 = 2 * 2 * 2 = 8

OUTPUT: 
The result is :  8
"""


def powerof(base, exponent):
    assert exponent >= 0 and int(
        exponent) == exponent, "The Exponent cannot be negative / non-integer number"
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    else:
        return base * powerof(base, exponent-1)


def main():
    print(f"The result is : ", str(powerof(2, 3)))


if __name__ == '__main__':
    main()
