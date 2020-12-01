import pytest

from code_challenges.tree.tree import Node, BinaryTree, BinarySearchTree

# Code Challenge 16

def test_make_empty_tree():
    tree = BinaryTree()
    assert tree.root == None

def test_tree_with_single_root():
    tree = BinaryTree()
    node1 = Node(1)
    tree.root = node1
    assert tree.root.value == 1

def test_add_left_and_right():
    tree = BinaryTree()
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node1.left = node2
    node1.right = node3
    tree.root = node1
    assert node1.left.value == 3 and node1.right.value == 5


def test_preorder_traversal():
    tree = BinaryTree()
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node1.left = node2
    node1.right = node3
    tree.root = node1
    actual = tree.pre_order()
    expected = [1, 3, 5]
    assert actual == expected

def test_inorder_traversal():
    tree = BinaryTree()
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node1.left = node2
    node1.right = node3
    tree.root = node1
    actual = tree.in_order()
    expected = [3, 1, 5]
    assert actual == expected

def test_postorder_traversal():
    tree = BinaryTree()
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node1.left = node2
    node1.right = node3
    tree.root = node1
    actual = tree.post_order()
    expected = [3, 5, 1]
    assert actual == expected


# Code Challenge 17

def test_return_desired_value():
    tree = BinaryTree()
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node1.left = node2
    node1.right = node3
    tree.root = node1
    actual = tree.find_max_value()
    expected = 5
    assert actual == expected

def test_nothing_in_tree():
   tree = BinaryTree()
   actual = tree.find_max_value()
   expected = None
   assert actual == expected

