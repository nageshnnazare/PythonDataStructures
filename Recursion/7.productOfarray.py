"""
DESC: Calculate the product of an array
Author: Nagesh N Nazare
Date: 01-06-2021

RUN: 
python3 ./7.productOfarray.py

NOTE:
[1 2 3 4 5] = 1* [2 3 4 5] = 2* [3 4 5] 
= 6* [4 5] ...

OUTPUT: 
The product of the array is 120
"""


def productofarray(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * productofarray(arr[1:])


def main():
    print(f'The product of the array is', str(productofarray([1, 2, 3, 4, 5])))


if __name__ == "__main__":
    main()
