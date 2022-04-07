"""
Haily Nguyen, UCP 2022, Mar 26

Part 3:
Challenge: Implement the Stack class from scratch (do not use your language’s standard
stack or queue library/package methods). In this challenge, your Stack will only accept
Integer values.
"""


# Implement stack using array list
class Stack:
    def __init__(self):
        self.list = []
        self.min_list = []

    def push(self, item):
        # Bonus 2: Instead of comparing integers to integers, we will convert
        # all inputs to string and compare them abide by ASCII rules.
        item = str(item)
        self.list.append(item)
        if len(self.min_list):
            item = min(self.min_list[-1], item)
        self.min_list.append(item)

    def pop(self):
        item = self.list.pop()
        if item is self.min_list[-1]:
            self.min_list.pop()
        return item

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if self.list:
            return self.list[-1]
        else:
            return None

    def size(self):
        return len(self.list)

    # Bonus 1
    def min(self):
        return self.min_list[-1]


# Driver program
print("TESTING PROGRAM FOR STACK")
if __name__ == '__main__':
    myStack = Stack()
    myStack.push(42)
    print("Top of stack: ", myStack.top())
    print("Size of stack: ", myStack.size())
    myStack.push(9)
    myStack.push(100)
    myStack.push('abcd')
    print("Min of Stack: ", myStack.min())
    print("Popped value: ", myStack.pop())
    print("Size of stack: ", myStack.size())
    print('9' > '100')


"""
Implement a Queue class from scratch that handles any types of data.
"""


# Implement queue using linked list.
class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        if self.head is None:
            print("Empty queue!")
        return self.head is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            self.head = self.tail = None
            print("Empty queue!")
        else:
            item = self.head.item
            self.head = self.head.next
            self.length -= 1
            return item

    def front(self):
        if self.head is None:
            print("Empty queue!")
        return self.head.item

    def rear(self):
        if self.head is None:
            print("Empty queue!")
        return self.tail.item

    def size(self):
        return self.length


# Driver program
print("TESTING PROGRAM FOR QUEUE")
if __name__ == '__main__':
    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(True)
    myQueue.enqueue('abc')
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print("Size of queue: ", myQueue.size())
    print("Front of queue: ", myQueue.front())
    print("Rear of queue: ", myQueue.rear())
    dequeuedItem = myQueue.dequeue()
    print("Dequeue item: ", dequeuedItem)
    # If you dequeue more items than you enqueue, throw an empty exception.
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    myQueue.dequeue()
    print("Size of queue: ", myQueue.size())
    myQueue.dequeue()
    print("Dequeue of empty queue... is it empty?", myQueue.isEmpty())







