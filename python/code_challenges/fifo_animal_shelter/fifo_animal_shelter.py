class Node:

    def __init__(self, value =None, next_=None):

        self.value = value
        self.next_ = next_


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


class AnimalShelter:

    def __init__(self):

        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, value):

        if value == 'cat':
            new_animal = self.cat_queue.enqueue(value)


        elif value == 'dog':
            self.dog_queue.enqueue(value)

        else:
            return None

    def  dequeue(self, pref):

        if pref == 'cat':
            selected_cat = self.cat_queue.dequeue()
            return selected_cat

        elif pref == 'dog':
            selected_dog = self.dog_queue.dequeue()
            return selected_dog

        else:
            raise InvalidOperationError()


class InvalidOperationError(Exception):
    pass


