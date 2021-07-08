"""
DESC: Basic Array operations
Author: Nagesh N Nazare
Date: 07-06-2021
"""

from array import *

# Creating an array
print(f"\nCreating an array")
arr1 = array('i', [1, 2, 3, 4, 5, 6])  # int type
print(arr1)

arr2 = array('d', [1.1, 2.2, 3.3, 4.4, 5.5, 6.6])  # double type
print(arr2)

# Inserting element to the array
print(f"\nInserting element in an array")
arr1.insert(6, 7)  # End of array = O(1) operation
print(arr1)

arr1.insert(0, 0)  # Beginning of array = O(n) operation
print(arr1)

# Traversing an array
print(f"\nTraversing an array")


def traverseArray(arr):
    for i in arr:
        print(i)


print(traverseArray(arr2))  # O(n) operation

# Accessing element in an array
print(f"\nAccessing element in an array")


def accessElement(arr, index):
    if index > len(arr):
        print("There is no element in the index")
    else:
        return arr[index]


print(accessElement(arr2, 3))  # O(1) operation

# Searching an element in an array
print(f"\nSeaching an element in an array")


def searchElement(arr, key):
    for i in arr:
        if i == key:
            return arr.index(key)
    return "Element not found"


print(searchElement(arr2, 5.5))  # O(n) operation
print(searchElement(arr2, 5))

# Deleting an element from an array
print(f"\nDeleting an element from an array")


def deleteElement(arr, index):
    return arr.remove(index)


deleteElement(arr1, 2)  # O(n) operation
print(arr1)


"""
SUMMARY: 
Operation                                       Time Complexity             Space Complexity
1. Creating an empty array                          O(1)                            O(n)
2. Inserting an element in an array                 O(1)/ O(n)                      O(1)     
3. Traversing a given array                         O(n)                            O(1)
4. Accessing a given element in an array            O(1)                            O(1)
5. Searching a given element in an array            O(n)                            O(1)
6. Deleting a given element in an array             O(1)/ O(n)                      O(1)
"""
