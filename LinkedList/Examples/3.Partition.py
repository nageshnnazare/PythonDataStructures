"""
DESC: Partition the Linked List around a value x
        value < x => Left Partition
        value >= x => Right Partition
Author: Nagesh N Nazare
Date: 11-08-2021

"""
from LinkedList import LinkedList


def partitionAroundX(linkedList, x):
    currNode = linkedList.head
    linkedList.tail = linkedList.head

    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value < x:
            currNode.next = linkedList.head
            linkedList.head = currNode
        else:
            linkedList.tail.next = currNode
            linkedList.tail = currNode
        currNode = nextNode

    if linkedList.tail.next is not None:
        linkedList.tail.next = None


def main():
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)

    partitionAroundX(ll, 80)
    print(ll)


if __name__ == "__main__":
    main()
