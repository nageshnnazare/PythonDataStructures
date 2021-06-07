"""
DESC: To reverse the string
Author: Nagesh N Nazare
Date: 01-06-2021

RUN: 
python3 ./9.reverseString.py

NOTE:
ABCDEFG => G + ABCDEF => GF + ABCDE ...

OUTPUT: 
The reverse of the string is :  GFEDCBA
"""
def reverseString(str):
    if len(str) <= 1:
        return str
    else:
        return str[len(str)-1] + reverseString(str[0:len(str)-1])

def main():
    print(f'The reverse of the string is : ', str(reverseString("ABCDEFG")))

if __name__ == "__main__":
    main()