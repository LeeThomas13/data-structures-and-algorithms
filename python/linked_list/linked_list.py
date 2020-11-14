class Node:
    #defines what a node will be, its starting value is none.
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinkedList():

    def __init__(self):
        self.head = Node()

    def append(self, data):
        #pushes new nodes into the linked list.
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node


LinkedList.append(1)
LinkedList.append(2)
LinkedList.append(3)




