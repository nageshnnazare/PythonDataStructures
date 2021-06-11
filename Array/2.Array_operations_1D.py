"""
DESC: Advanced 1D Array operations
Author: Nagesh N Nazare
Date: 07-06-2021
"""

from array import *

# 1. Creating an Array and Traversing
print(f"\nCreating and Traversing an array")

my_array = array('i', [1,2,3,4,5,6])
for i in my_array:
    print(i)
    
# 2. Accessing individual elements through indexes
print(f"\nAccessing individual elements through indexes")

print(my_array[2])

# 3. Adding a value to the array using append()
print(f"\nAdding a value to the array using append()")

my_array.append(7)
print(my_array)

# 4. Insert a value in an array using insert()
print(f"\nInserting a value in an array using insert()")

my_array.insert(3, 10)
print(my_array)

# 5. Extend python array with extend()
print(f"\nExtending python array with extend()")

my_array_2 = array('i', [90,91,92])
my_array.extend(my_array_2)
print(my_array)

# 6. Add elements from list into array with fromlist()
print(f"\nAdd elements from list into array with fromlist()")

temp_list = [6,7,50,51,52]
my_array.fromlist(temp_list)
print(my_array)

# 7. Remove an element from an array with remove()
print(f"\nRemove an element from an array with remove()")

my_array.remove(52)
print(my_array)

# 8. Remove last element in an array with pop()
print(f"\nRemove last element in an array with pop()")

my_array.pop()
print(my_array)

# 9. Fetch any element in an array using index()
print(f"\nFetch index of any element in an array using index()")

print(my_array.index(90))

# 10. Reverse a python array using reverse()
print(f"\nReverse a python array using reverse()")

my_array.reverse()
print(my_array)

# 11. Get array buffer information with buffer_info()
print(f"\nGet array buffer information with buffer_info()")

print(my_array.buffer_info())

# 12. Check the number of occurances of an element in an array with count()
print(f"\nCheck the number of occurances of an element in an array with count()")

print(my_array.count(6))

# 13. Convert an array to bytes using tobytes()
print(f"\nConvert an array to string using tobytes()")

my_bytes = my_array.tobytes()
print(type(my_bytes))
print(my_bytes)

# 14. Convert from bytes to array using frombytes()
print(f"\nConvert from bytes to array using frombytes()")

arr = array('i')
arr.frombytes(my_bytes)
print(type(arr))
print(arr)

# 15. Convert a array to list using tolist()
print(f"\nConvert a array to list using tolist()")

print(type(my_array.tolist()))
print(my_array.tolist())

# 16. Slice element from an array
print(f"\nSlice element from an array")

print(my_array[1:5])