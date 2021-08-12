"""
DESC: Stack Implementation using Linked List
Author: Nagesh N Nazare
Date: 12-08-2021

"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(node.value) for node in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "No element to pop, Stack Empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "No element to pop, Stack Empty"
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None


def main():
    stack = Stack()
    # print(stack.isEmpty())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    # print(stack)

    stack.pop()
    # print(stack)

    # print(stack.peek())


if __name__ == "__main__":
    main()
