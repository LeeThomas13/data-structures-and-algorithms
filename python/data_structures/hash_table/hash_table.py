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

        bucket = self.buckets[hashed_key_index]

        current = bucket.head

        while current:

            pair = current.data

            if pair[0] == key:
                return pair[1]

            current = current.next


