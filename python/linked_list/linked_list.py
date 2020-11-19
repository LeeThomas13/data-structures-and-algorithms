class Node:
    #defines what a node will be, its starting value is none.
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        self.head = Node(data)

    def insert_before(self, value, new_value):
        if not self.head:
            return

        if self.head == value:
            self.insert(new_value)

        current = self.head

        while current.next:
            if current.next.value == value:
                current.next = Node(new_value, current.next)
                return

            current = current.next

    def insert_after(self, value):
        if not self.head:
            return

        current = self.head

        while current:
            if current.value == value:
                current.next = Node(new_value, current.next)
                return

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

    # def kth_from_end(self, k):
    #     list = []
    #     counter = 0
    #     runner = self.head
    #     follower = self.head
    #     while runner.next:
    #         runner = runner.next
    #         counter += 1
    #         if counter > k:
    #             follower = follower.next
    #         return follower.data
    #     if counter > k:

    def kth_from_end(self, k):
        list = []
        current = self.head
        if k < 0:
            raise valueError("value of k should be positive")
        count = 0
        while current != None:
            if count == k:
                value_seeking = self.head
            elif count > k:
                value_seeking = value_seeking.next
            current = current.next
            count+= 1
        if count > k:
            return value_seeking.data

    def zip_lists(lista, listb):
        list_a_node = lista.head
        list_b_node = listb.head
        zip_list = LinkedList()
        while list_a_node or list_b_node:
            if list_a_node:
                zip_list.append(list_a_node.data)
                list_a_node = list_a_node.next
            if list_b_node:
                zip_list.append(list_b_node.data)
                list_b_node = list_b_node.next
        return zip_list


lista = LinkedList()
lista.insert(1)
lista.insert(2)
lista.insert(3)
listb = LinkedList()
listb.insert(4)
listb.insert(5)
listb.insert(6)
print(LinkedList.zip_lists(lista, listb))






