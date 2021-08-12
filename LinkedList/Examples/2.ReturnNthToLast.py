"""
DESC: Return Nth element to the Last of the Linked List
Author: Nagesh N Nazare
Date: 11-08-2021

"""
from LinkedList import LinkedList


def NthToLast(linkedList, n):
    ptr1 = linkedList.head
    ptr2 = linkedList.head

    for i in range(n):
        if ptr2 is None:
            return None
        else:
            ptr2 = ptr2.next

    while ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1


def main():
    ll = LinkedList()
    ll.generate(10, 0, 20)
    print(ll)

    print(NthToLast(ll, 4))


if __name__ == "__main__":
    main()
