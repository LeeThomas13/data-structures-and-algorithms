from data_structures.hash_table.hash_table import HashTable
import pytest

def test_create():
    ht = HashTable()
    assert ht

def test_structure_of_hash():
    ht = HashTable()
    initial = ht._hash('spam')
    secondary = ht._hash('spam')
    assert initial == secondary

def test_in_rage_hash():
    ht = HashTable()
    actual = ht._hash('spam')
    assert 0 <= actual < ht._size

