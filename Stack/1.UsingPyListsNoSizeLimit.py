"""
DESC: Stack Implementation using Lists without size limit
Author: Nagesh N Nazare
Date: 12-08-2021

"""


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(value) for value in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return f"{value} added to the list successfully"

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
    stack = Stack()

    # print(stack.isEmpty())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    # print(f"After push operation : \n{stack}")

    stack.pop()
    # print(f"After pop operation : \n{stack}")

    # print(stack.peek())


if __name__ == "__main__":
    main()
