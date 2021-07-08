"""
DESC: Singly Linked List Implementation
Author: Nagesh N Nazare
Date: 08-07-2021

"""


class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertinSLL(self, value, location):
        newNode = Node(value)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            if (location == 0):
                newNode.next = self.head
                self.head = newNode
            elif (location == -1):
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while (index < location - 1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if(tempNode == self.tail):
                    self.tail == None

    def traverseSLL(self):
        if(self.head is None):
            return "Singly Linked List is empty!"
        else:
            node = self.head
            while node is not None:
                print(f'{node.value}')
                node = node.next

    def searchinSLL(self, nodeValue):
        if(self.head is None):
            return "Singly Linked List is empty!"
        else:
            node = self.head
            while(node is not None):
                if(node.value == nodeValue):
                    return node.value
                node = node.next
            return "The value does not exist in this list!"

    def deleteinSLL(self, location):
        if(self.head is None):
            return "Singly Linked List is empty!"
        else:
            if(location == 0):
                if(self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif(location == -1):
                if(self.head == self.tail):
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while(node is not None):
                        if(node.next == self.tail):
                            break
                        node = node.next
                    node.next = None
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
            return "Singly Linked List is empty!"
        else:
            self.tail = None
            self.head = None


def main():
    # Creating a Singly Linked List Object
    singlyLL = SLinkedList()

    # Inserting Elements in the Singly Linked List
    singlyLL.insertinSLL(1, 1)
    singlyLL.insertinSLL(2, 1)
    singlyLL.insertinSLL(0, 0)
    singlyLL.insertinSLL(3, 3)
    singlyLL.insertinSLL(4, 4)
    singlyLL.insertinSLL(5, 5)

    # Iterating the Singly Linked List
    print([node.value for node in singlyLL])

    # Traverse the Singly Linked List
    # singlyLL.traverseSLL()

    # Searching a value in the Singly Linked List
    # print(singlyLL.searchinSLL(3))
    # print(singlyLL.searchinSLL(6))

    # Deleting an element from the Singly Linked List
    # singlyLL.deleteinSLL(5)
    # print([node.value for node in singlyLL])

    # Delete the entire Singly Linked List
    # singlyLL.deleteEntireSLL()
    # print([node.value for node in singlyLL])


if __name__ == '__main__':
    main()
