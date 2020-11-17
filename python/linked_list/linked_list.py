class Node:
    #defines what a node will be, its starting value is none.
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head = None

    def append (self, data):
        new_node = Node(data)
        old = self.head
        self.head = new_node
        self.head.next = old

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total+=1
            current = current.next
        return total

    def verify_index (self, index):
        if index >= self.length():
            return False
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return True
            current_index += 1

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += "{" + f"{current.data}" + "} -> "
            current = current.next
        result += "Null"
        return result







