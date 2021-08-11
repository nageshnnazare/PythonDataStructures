"""
DESC: Circular Linked List Implementation
Author: Nagesh N Nazare
Date: 26-07-2021

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if (node == self.tail.next):
                break

    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return f'Circular Linked List is created!'

    def insertinCSLL(self, value, location):
        if(self.head is None):
            return "Circular Singly Linked List does not exists!"
        else:
            newNode = Node(value)
            if(location == 0):
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif(location == -1):
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while(index < location - 1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "Node has been successfully inserted"

    def traverseCSLL(self):
        if(self.head is None):
            return f'Circular Singly Linked List does not exists!'
        else:
            tempNode = self.head
            while(tempNode):
                print(tempNode.value)
                tempNode = tempNode.next
                if(tempNode == self.tail.next):
                    break

    def searchinCSLL(self, value):
        if(self.head is None):
            return f'Circular Singly Linked List does not exists!'
        else:
            tempNode = self.head
            while(tempNode):
                if(tempNode.value == value):
                    return tempNode.value
                tempNode = tempNode.next
                if(tempNode == self.tail.next):
                    return "Element does not exists in the list"

    def deleteinCSSL(self, location):
        if(self.head is None):
            return "Circular Singly Linked List is empty!"
        else:
            if(location == 0):
                if(self.head == self.tail):
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif(location == -1):
                if(self.head == self.tail):
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while(node is not None):
                        if(node.next == self.tail):
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while(index < location - 1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteEntireSLL(self):
        if(self.head is None):
            return "Circular Singly Linked List is empty!"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None


def main():
    csll = CircularSLinkedList()
    csll.createCSLL(1)

    csll.insertinCSLL(0, 0)
    csll.insertinCSLL(2, 1)
    csll.insertinCSLL(3, 2)
    csll.insertinCSLL(4, 3)

    print([node.value for node in csll])

    csll.traverseCSLL()
    print(csll.searchinCSLL(5))
    print(csll.searchinCSLL(0))

    csll.deleteinCSSL(0)
    print([node.value for node in csll])

    csll.deleteinCSSL(3)
    print([node.value for node in csll])


if __name__ == '__main__':
    main()
