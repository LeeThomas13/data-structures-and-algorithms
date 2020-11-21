class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        top_node = Node(value, self.top)
        self.top = top_node


class Queue:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def enqueue(self, value):
        current_last = self.last
        current_last.next_ = Node(value)
        self.last = current_last.next_

    def dequeue(self):
        pass


class InvalidOperationError(Exception):
    pass
