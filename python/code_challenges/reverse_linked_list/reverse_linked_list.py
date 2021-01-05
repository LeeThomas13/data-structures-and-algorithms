class Node:
    #defines what a node will be, its starting value is none.
    def __init__(self, data, next_=None):
        self.data=data
        self.next_=next_

class LinkedList:

    def __init__(self, next_=None):
        self.head = None
        self.next_ = next_

    def insert(self, data):
        self.head = Node(data, self.head)

    def append (self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_:
            current = current.next_
        current.next_ = new_node

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += "{" + f"{current.data}" + "} -> "
            current = current.next_
        result += "None"
        return result

    def reverse_linked_list(self):
        # empty linked list check
        if self.head == None:
            return

        p1 = None
        p2 = self.head
        # recurse through the linked list, reversing the pointers
        while p2:
            # ll arrow flip
            p3 = p2.next_
            p2.next_ = p1
            # pointer reassignment
            p1 = p2
            p2 = p3
        return p1.data

