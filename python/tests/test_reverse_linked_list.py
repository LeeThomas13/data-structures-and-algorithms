from code_challenges.reverse_linked_list.reverse_linked_list import Node, LinkedList

import pytest

def test_happy_path():
    ll = LinkedList()
    ll.insert(5)
    ll.append(6)
    ll.append(7)
    actual = ll.reverse_linked_list()
    expected = 7
    assert actual == expected

def test_expected_failure():
    ll = LinkedList()
    actual = ll.reverse_linked_list()
    expected = None
    assert actual == expected

def test_edge_case():
    ll = LinkedList()
    ll.insert('cat')
    ll.append('spam')
    ll.append('dog')
    ll.append('eggs')
    actual = ll.reverse_linked_list()
    expected = 'eggs'
    assert actual == expected

def test_edge_case_two():
    ll = LinkedList()
    ll.insert('one')
    actual = ll.reverse_linked_list()
    expected = 'one'
    assert actual == expected

def test_edge_case_three():
    ll = LinkedList()
    ll.insert('^&&')
    ll.append('((')
    actual = ll.reverse_linked_list()
    expected = '(('
    assert actual == expected
