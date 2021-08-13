"""
DESC: Queue Implementation using Lists with size limit (Circular Queue)
Author: Nagesh N Nazare
Date: 13-08-2021

"""


class Queue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(value) for value in self.items]
        return '\t'.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return f"Queue max limit reached!"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return f"{value} inserted at the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1


def main():
    queue = Queue(3)
    # print(queue.isFull())
    # print(queue.isEmpty())

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    # print(queue)

    queue.dequeue()
    # print(queue)
    print(queue.peek())


if __name__ == "__main__":
    main()
