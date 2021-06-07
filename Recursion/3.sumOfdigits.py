"""
DESC: Calculate the sum of digits of a positive integer number
Author: Nagesh N Nazare
Date: 31-05-2021

RUN: 
python3 ./3.sumOfdigits.py

NOTE:
112 :      
112/10 = 11 , rem = 2
11/10 = 1, rem = 1
1 + 1 + 2 = 4

OUTPUT: 
The sum of the digits is : 4
"""

def sumOfdigits(n):
    assert n >= 0 and int(n) == n, "The number has to positive integer number only"
    if n in [0]:
        return 0
    else:
        return int(n%10) + sumOfdigits(n//10)


def main():
    print(f'The sum of the digits is : ', str(sumOfdigits(112)))


if __name__ == '__main__':
    main()