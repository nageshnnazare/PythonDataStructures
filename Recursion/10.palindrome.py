"""
DESC: Check whether Palindrome or not
Author: Nagesh N Nazare
Date: 01-06-2021

RUN: 
python3 ./8.recursiveRange.py

NOTE:
abcbcba => a, bcbcb => ab, cbc => abc

OUTPUT: 
Is the string Hello a palindrome :  False
Is the string abcbcba a palindrome :  True
"""


def isPalindrome(str):
    assert len(str) % 2 != 0, "The length of the str cannot of even"
    if len(str) == 1:
        return True
    if str[0] != str[len(str)-1]:
        return False
    return isPalindrome(str[1:-1])


def main():
    str1 = "Hello"
    print(f'Is the string {str1} a palindrome : ', str(isPalindrome(str1)))

    str2 = "abcbcba"
    print(f'Is the string {str2} a palindrome : ', str(isPalindrome(str2)))


if __name__ == "__main__":
    main()
