"""
DESC: Remove Duplicates from the Linked List
Author: Nagesh N Nazare
Date: 09-08-2021

"""
from LinkedList import LinkedList

# using a temporary buffer


def removeDuplicates_1(linkedList):
    if linkedList.head is None:
        return
    else:
        currentNode = linkedList.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return linkedList

# without using a temporary buffer


def removeDuplicates_2(linkedList):
    if linkedList.head is None:
        return
    else:
        currentNode = linkedList.head
        while currentNode:
            runner = currentNode
            while runner.next:
                if runner.next.value == currentNode.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currentNode = currentNode.next
        return linkedList.head


def main():
    ll = LinkedList()
    ll.generate(10, 0, 10)
    print(ll)
    # removeDuplicates_1(ll)
    removeDuplicates_2(ll)
    print(ll)


if __name__ == "__main__":
    main()
