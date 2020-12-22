from linked_list.linked_list import LinkedList

class HashTable:
    def __init__(self, size = 1024):
        self._size = size
        self._buckets = size * [None]


    def _hash(self, key):

        sum = 0

        for ch in key:
            sum += ord(ch)

        primed = sum * 19

        index = primed % self._size

        return index


    def set(self, key, value):
        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].insert((key, value))

    def get(self, key):
        hashed_key_index = self._hash(key)

        bucket = self._buckets[hashed_key_index]

        current = bucket.head

        while current:

            pair = current.data

            if pair[0] == key:
                return pair[1]

            current = current.next

    def contains(self, key):
        hashed_key_index = self._hash(key)

        bucket = self._buckets[hashed_key_index]

        current = bucket.head

        while current:

            pair = current.data

            if pair[0] == key:
                return True

            else:
                return False


            current = current.next


class Node:
    #defines what a node will be, its starting value is none.
    def __init__(self, data, next_=None):
        self.data=data
        self.next_=next_


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        self.head = Node(data, self.head)

    def insert_before(self, data, new_value):
        current = self.head

        if current == None:
            return "something broke :/"

        if current.data == data:
            self.insert(new_value)

        while current.next_:
            if current.next_.data == data:
                current.next_ = Node(new_value, current.next_)
                break
            current = current.next_
            if current.next_ == None:
                return "something went wrong"

    def insert_after(self, data):
        if not self.head:
            return

        current = self.head

        while current:
            if current.data == data:
                current.next_ = Node(new_value, current.next_)
                return

    def append (self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_:
            current = current.next_
        current.next_ = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next_ is not None:
            total+=1
            current = current.next_
        return total

    def verify_index (self, index):
        if index >= self.length():
            return False
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next_
            if current_index == index:
                return True
            current_index += 1

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += "{" + f"{current.data}" + "} -> "
            current = current.next_
        result += "None"
        return result

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
                value_seeking = value_seeking.next_
            current = current.next_
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
                list_a_node = list_a_node.next_
            if list_b_node:
                zip_list.append(list_b_node.data)
                list_b_node = list_b_node.next_
        return zip_list


