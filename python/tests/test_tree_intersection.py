import pytest

from code_challenges.tree_intersection.tree_intersection import Node, BinaryTree, BinarySearchTree

def test_no_value():
    tree1 = BinarySearchTree()
    tree1.root = Node(6)
    tree1.root.left = Node(5)
    tree1.root.right = Node(7)

    tree2 = BinarySearchTree()
    tree2.root = Node(9)
    tree2.root.right = Node(10)
    tree2.root.left = Node(8)

    actual = tree2.tree_intersection(tree1)
    expected = []
    assert actual == expected

def test_one_match():
    tree1 = BinarySearchTree()
    tree1.root = Node(6)
    tree1.root.left = Node(5)
    tree1.root.right = Node(7)

    tree2 = BinarySearchTree()
    tree2.root = Node(8)
    tree2.root.left = Node(6)
    tree2.root.right = Node(10)

    actual = tree2.tree_intersection(tree1)
    expected = [6]
    assert actual == expected

def test_two_matches():
    tree1 = BinarySearchTree()
    node1 = Node(5)
    node2 = Node(1)
    node3 = Node(3)
    node4 = Node(7)
    node5 = Node(9)
    tree1.root = node1
    node1.left = node3
    node1.right = node4
    node3.left = node2
    node4.right = node5

    tree2 = BinarySearchTree()
    node1 = Node(6)
    node2 = Node(7)
    node3 = Node(8)
    node4 = Node(4)
    node5 = Node(5)
    tree2.root = node1
    node1.right = node2
    node1.left = node5
    node2.right = node3
    node5.left = node4

    actual = tree1.tree_intersection(tree2)
    expected = [5,7]
    assert actual == expected
