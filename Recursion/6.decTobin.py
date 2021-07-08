"""
DESC: Convert a decimal number into binary
Author: Nagesh N Nazare
Date: 31-05-2021

RUN: 
python3 ./6.decTobin.py

NOTE:
decTobin(13):
13/2 = 6, rem = 1
6/2 = 3, rem = 0
3/2 = 1, rem = 1
1/2 = 0, rem = 1 

d'13 = b'1101

METHOD:
decTobin(n) = n mod 2 + 10 * decTobin(n/2)

OUTPUT: 
The decimal form of the number is :  1101
"""


def decTobin(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer number"
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decTobin(int(n/2))


def main():
    print(f'The decimal form of the number is : ', str(decTobin(13)))


if __name__ == "__main__":
    main()
