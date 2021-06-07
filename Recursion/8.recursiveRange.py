"""
DESC: Calculate the recursive range of the number
Author: Nagesh N Nazare
Date: 01-06-2021

RUN: 
python3 ./8.recursiveRange.py

NOTE:
11 => 11+10+9+8+....

OUTPUT: 
The recursive range is :  66
"""

def recursiveRange(num):
    if num <= 0:
        return 0
    else:
        return num + recursiveRange(num - 1)

def main():
    print(f"The recursive range is : ", str(recursiveRange(11)))


if __name__ == "__main__":
    main()