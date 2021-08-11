"""
DESC: Doubly Linked List Implementation
Author: Nagesh N Nazare
Date: 10-08-2021

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return f'Doubly Linked List created succesfully'

    def insertinDLL(self, value, location):
        if self.head is None:
            print('Doubly linked list does not exists!')
        else:
            newNode = Node(value)
            if(location == 0):
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif(location == -1):
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while(index < location - 1):
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def traverseDLL(self):
        if self.head is None:
            print('Doubly linked list does not exists!')
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reverseTraverseDLL(self):
        if self.head is None:
            print('Doubly linked list does not exists!')
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def searchinDLL(self, value):
        if self.head is None:
            print('Doubly linked list does not exists!')
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
            return "Element does not exists in the list!"

    def deleteinDLL(self, location):
        if self.head is None:
            print('Doubly linked list does not exists!')
        else:
            if(location == 0):
                if(self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif(location == -1):
                if(self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currNode = self.head
                index = 0
                while index < location - 1:
                    currNode = currNode.next
                    index += 1
                currNode.next = currNode.next.next
                currNode.next.prev = currNode
            print('Node deleted successfully')

    def deleteEntireDLL(self):
        if self.head is None:
            print('Doubly linked list does not exists!')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
        print('Linked list deleted successfully')


def main():
    dll = DoublyLinkedList()
    dll.createDLL(1)

    dll.insertinDLL(2, 0)
    dll.insertinDLL(5, -1)
    dll.insertinDLL(3, 2)
    # dll.traverseDLL()
    # dll.reverseTraverseDLL()

    # print(dll.searchinDLL(6))
    # print(dll.searchinDLL(5))
    dll.deleteinDLL(0)

    print([node.value for node in dll])


if __name__ == "__main__":
    main()
