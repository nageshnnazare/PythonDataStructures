"""
DESC: Check if the two lists are intersecting
Author: Nagesh N Nazare
Date: 12-08-2021

"""
from LinkedList import LinkedList, Node


def intersectingList(linkedList_A, linkedList_B):
    if linkedList_A.tail is not linkedList_B.tail:
        return False
    else:
        len_A = len(linkedList_A)
        len_B = len(linkedList_B)

        shorter = linkedList_A if len_A < len_B else linkedList_B
        longer = linkedList_A if len_A > len_B else linkedList_B
        diff = len(longer) - len(shorter)

        longerNode = longer.head
        shorterNode = shorter.head

        for i in range(diff):
            longerNode = longerNode.next

        while shorterNode is not longerNode:
            shorterNode = shorterNode.next
            longerNode = longerNode.next

        return longerNode


def addSameNode(linkedList_A, linkedList_B, value):
    tempNode = Node(value)
    linkedList_A.tail.next = tempNode
    linkedList_A.tail = tempNode
    linkedList_B.tail.next = tempNode
    linkedList_B.tail = tempNode


def main():
    ll_A = LinkedList()
    ll_A.generate(3, 0, 10)

    ll_B = LinkedList()
    ll_B.generate(5, 0, 10)

    addSameNode(ll_A, ll_B, 11)
    addSameNode(ll_A, ll_B, 14)
    addSameNode(ll_A, ll_B, 8)
    print(ll_A)
    print(ll_B)

    print(intersectingList(ll_A, ll_B))


if __name__ == "__main__":
    main()
