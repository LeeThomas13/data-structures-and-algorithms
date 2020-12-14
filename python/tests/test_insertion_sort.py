from code_challenges.insertion_sort.insertion_sort import insertion_sort

import pytest

def test_empty_array():
    array = []
    actual = insertion_sort(array)
    expected = 'empty array'
    assert actual == expected

def test_single_array():
    array = [5]
    actual = insertion_sort(array)
    expected = 'its already sorted'
    assert actual == expected

def test_negative_array():
    array = [-7, -9, -5]
    actual = insertion_sort(array)
    expected = [-9, -7, -5]
    assert actual == expected

def test_happy_path():
    array = [5, 7, 6, 9, 3]
    actual = insertion_sort(array)
    expected = [3, 5, 6, 7, 9]
    assert actual == expected
