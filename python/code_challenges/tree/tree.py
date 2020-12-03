class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None
        self.next_ = None
        self.front = None
        self.back = None

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
            return
        return self.front.value

    def is_empty(self):
        return not self.front


class BinaryTree:

    def __init__(self):

        self.root = None

    def pre_order(self):

        values = []

        def walk(current):

            if not current:
                return
            values.append(current.value)
            walk(current.left)
            walk(current.right)
        walk(self.root)
        return values

    def in_order(self):

        values = []

        def walk(current):

            if not current:
                return
            walk(current.left)
            values.append(current.value)
            walk(current.right)
        walk(self.root)
        return values

    def post_order(self):

        values = []

        def walk(current):

            if not current:
                return
            walk(current.left)
            walk(current.right)
            values.append(current.value)
        walk(self.root)
        return values

    def breadth_first(self):

        # make a list to append to
        node_list = []

        #error check
        if not self.root:
            raise ValueError('Something went wrong')

        breadth_first = Queue()
        breadth_first.enqueue(self.root)

        #while the queue is not empty
        while breadth_first.peek():
            appended_value = breadth_first.dequeue()

            #append peeked value to node list, and dequeue it
            node_list.append(appended_value.value)
            if appended_value.left:
                breadth_first.enqueue(appended_value.left)
            if appended_value.right:
                breadth_first.enqueue(appended_value.right)

        return node_list


    def find_max_value(self):

        current = self.root
        if not self.root:
            return None

        def traverse(root):

            if not root:
                return
            nonlocal current
            if root.value > current.value:
                current = root
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return current.value


class BinarySearchTree(BinaryTree):

    def __init__(self):

        self.root = None

    def add(self, value):

        def walk(node, value):

            new_node = Node(value)
            if node is None:
                self.root = new_node
                return
            if value < node.value:
                if not node.left:
                    node.left = new_node
                else:
                   walk(node.left)
            else:
                if not node.right:
                    node.right = new_node
                else:
                    walk(node.right)
        walk(self.root, value)

    def contains(self, value):

        def walk(node):

            if not node:
                return False
            if node.value == value:
                return True
            else:
                if value < node.value:
                    return walk(node.left)
                else:
                    return walk(node.right)
        found = walk(self.root)
        return found

