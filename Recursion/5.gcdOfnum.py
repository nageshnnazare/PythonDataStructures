"""
DESC: Calculate the Greatest Common Divisor (GCD) of two numbers
Author: Nagesh N Nazare
Date: 31-05-2021

RUN: 
python3 ./5.gcdOfnum.py

NOTE:
Euclidean Algorithm
gcd(48, 18): 
48/18 = 2, rem = 12
18/12 = 1, rem = 6
12/6 = 2, rem = 0
GCD = 6

METHOD:
gcd(a, 0) = a 
gcd(a, b) = gcd(b, a mod b)

OUTPUT: 
The GCD of the numbers is :  6
"""

def gcd(a, b):
    assert a >=0 and b>=0 and int(a) == a and int(b) == b, "The numbers must be positive integer numbers"
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def main():
    print(f'The GCD of the numbers is : ', str(gcd(48, 18)))

if __name__ == "__main__":
    main()