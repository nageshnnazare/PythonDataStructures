"""
DESC: Stack Implementation using Lists with size limit
Author: Nagesh N Nazare
Date: 12-08-2021

"""


class Stack:
    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size

    def __str__(self):
        values = self.list.reverse()
        values = [str(value) for value in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The Stack is Full"
        else:
            self.list.append(value)
            return f"{value} is successfully added to the list"

    def pop(self):
        if self.isEmpty():
            return f"List is Empty!"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return f"List is Empty!"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


def main():
    stack = Stack(3)

    # print(stack.isEmpty())
    # print(stack.isFull())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    # print(stack)


if __name__ == "__main__":
    main()
