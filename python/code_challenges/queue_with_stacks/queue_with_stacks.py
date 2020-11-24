class Node:

    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next_ = self.top
        self.top = node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next_
            return value
        raise InvalidOperationError("Method not allowed on empty collection")

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        if self.top:
            return False
        return True


class PseudoQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        if self.stack1 == None:
            Stack.push(value)
            return

        while self.stack1.top:
            top_of_stack = self.stack1.pop()
            self.stack2.push(top_of_stack)
        self.stack2.push(value)

        while self.stack2.top:
            top_of_stack = self.stack2.pop()
            self.stack1.push(top_of_stack)

    def dequeue(self):
        return self.stack1.pop()


class InvalidOperationError(Exception):
    pass
