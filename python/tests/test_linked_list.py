from linked_list.linked_list import Node, LinkedList

import pytest

def test_import():
    assert LinkedList

#can instantiate an empty linked list
def test_empty_linked_list():
    expected = LinkedList().head
    actual = None
    assert actual == expected

#can push a value into the linked list
def test_insert_into_linked_list():
    ll= LinkedList()
    ll.append(8)
    assert ll.head.data == 8

#head node points to first index
def test_head_points_to_first_index():
    ll = LinkedList()
    assert ll.head == None

#test to see if the linked list can hold data
def test_multiple_node_insertion():
    ll = LinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')
    assert ll.head.data == 'c'
    assert ll.head.next.data == 'b'
    assert ll.head.next.next.data == 'a'

#search through linked list to see if there is a specified value, returns boolean True or False
def test_value_is_true():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert ll.verify_index(5) == True

#search through linked list to see if there is a specified value, returns boolean True or False
def test_value_is_false():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    assert ll.verify_index(7) == False



