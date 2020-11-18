from linked_list.linked_list import Node, LinkedList

import pytest

#Code Challenge 05
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
    assert ll.verify_index(2) == True

#search through linked list to see if there is a specified value, returns boolean True or False
def test_value_is_false():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    assert ll.verify_index(7) == False

#test to see if we can properly return a collection of all the values that exits in the linked list.
def test_collection():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert str(ll) == '{5} -> {4} -> {3} -> {2} -> Null'

#Code Challenge 06
#still in progress

#Code Challenge 07
#test to see if we can return the k value
def test_linked_list_kth_from_end():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(9)
    ll.insert(3)
    ll.insert(7)
    actual = ll.kth_from_end(2)
    expected = 9
    assert actual == expected

#Code Challenge 08
#test to see if we can 'zip' two linked lists together
def test_zipped_linked_list():
    ll= LinkedList()
    ll.insert(a)
    ll.insert(b)
    ll.insert(c)
    expected = str(ll) == '{a} -> {b} ->{c}'
