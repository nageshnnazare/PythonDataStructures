"""
DESC: Queue Implementation using Lists without size limit
Author: Nagesh N Nazare
Date: 13-08-2021

"""


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(value) for value in self.items]
        return '\t'.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return f"{value} inserted at the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return f"There are no elements in the queue to remove"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return f"There are no elements in the queue to remove"
        else:
            return self.items[0]

    def delete(self):
        self.items = []


def main():
    queue = Queue()

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
