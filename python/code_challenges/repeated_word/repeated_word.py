import re

class Node:
    #defines what a node will be, its starting value is none.
    def __init__(self, data, next_=None):
        self.data=data
        self.next_=next_


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


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        self.head = Node(data, self.head)

    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += "{" + f"{current.data}" + "} -> "
            current = current.next_
        result += "None"
        return result




def find_repeats(str):

    ht = HashTable()

    str_list = split_string(str)

    if str == '':
        return 'There\'s no string here...'

    for i in str_list:

        if ht.contains(i):

            return i

        else:

            ht.set(i)


    return repeat_list

def split_string(str):

    new_list = re.findall("[a-zA-Z]+", str)

    return new_list
