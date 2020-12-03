class Node:

    def __init__(self, value =None, next_=None):
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

    def is_empty(self):
        if self.top:
            return False
        return True
        # (return not self.top) most pythonic

    def peek(self):
        if not self.top:
            raise InvalidOperationError(
                "Method not allowed on empty collection")
        return self.top.value

class Queue:

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.back = node
            return
        self.back.next_ = node
        self.back = node

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError()
        target_node = self.front
        self.front = target_node.next_
        return target_node.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError()
        return self.front.value

    def is_empty(self):
        return not self.front

class InvalidOperationError(Exception):
    pass

