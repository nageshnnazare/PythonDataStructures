"""
DESC: Circular Doubly Linked List Implementation
Author: Nagesh N Nazare
Date: 11-08-2021

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.tail = node
        return f'Circular Doubly Linked List created succesfully'

    def insertinCDLL(self, value, location):
        if self.head is None:
            return "Circular Doubly linked List does not exist!"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node is successfully inserted"

    def traverseCDLL(self):
        if self.head is None:
            return "Circular Doubly linked List does not exist!"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reversetraverseCDLL(self):
        if self.head is None:
            return "Circular Doubly linked List does not exist!"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def searchinCDLL(self, value):
        if self.head is None:
            return "Circular Doubly linked List does not exist!"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                if tempNode == self.tail:
                    return "Value does not exist in the list"
                tempNode = tempNode.next

    def deleteinCDLL(self, location):
        if self.head is None:
            return "Circular Doubly linked List does not exist!"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode
            return "Node deleted successfully"

    def deleteEntireCDLL(self):
        if self.head is None:
            print('Circular Doubly linked list does not exists!')
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
        return "CDLL deleted successfully"


def main():
    cdll = CircularDoublyLinkedList()
    cdll.createCDLL(1)

    cdll.insertinCDLL(0, 0)
    cdll.insertinCDLL(4, -1)
    cdll.insertinCDLL(2, 2)
    cdll.insertinCDLL(3, 3)

    # cdll.traverseCDLL()
    # cdll.reversetraverseCDLL()
    # print(cdll.searchinCDLL(4))
    # print(cdll.searchinCDLL(6))
    # cdll.deleteinCDLL(2)
    cdll.deleteEntireCDLL()

    print([node.value for node in cdll])


if __name__ == "__main__":
    main()
