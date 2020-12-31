import pytest

from code_challenges.pascal_triangle.pascal_triangle import pascal_triangle, coefficient

def test_happy_path():
    n = 5
    actual = pascal_triangle(n)
    expected = [2, 3, 3, 4, 4, 6, 4]
    assert actual == expected

def test_expected_failure():
    n = 0
    actual = pascal_triangle(n)
    expected = None
    assert actual == expected

def test_edge_case():
    n = -1
    actual = pascal_triangle(n)
    expected = None
    assert actual == expected

def test_edge_case():
    n = d
    actual = pascal_triangle(n)
    expected = None
    assert actual == expected
