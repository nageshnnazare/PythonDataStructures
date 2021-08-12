"""
DESC: Sum of 2 numbers represented by two Linked Lists (digits stored in reverse order)
Author: Nagesh N Nazare
Date: 11-08-2021

"""
from LinkedList import LinkedList


def sumList(linkedList_1, linkedList_2):
    n1 = linkedList_1.head
    n2 = linkedList_2.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(int(result % 10))
        carry = result/10
    return ll


def main():
    list_A = LinkedList()
    list_A.add(7)
    list_A.add(1)
    list_A.add(6)
    print(list_A)

    list_B = LinkedList()
    list_B.add(5)
    list_B.add(9)
    list_B.add(2)
    print(list_B)

    print(sumList(list_A, list_B))


if __name__ == "__main__":
    main()
