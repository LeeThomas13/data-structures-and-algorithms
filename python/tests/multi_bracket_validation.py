import pytest
from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_happy_path():
    string = '{}{}[]()'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_expected_failure():
    string = '()('
    actual = multi_bracket_validation(string)
    expected = False
    assert actual == expected

def test_nothing_edge_case():
    string = ''
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_jumbled_brackets():
    string = '{{[]}([])}'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

def test_many_brackets():
    string = '{{[]}([])}{{[]}([])}{{[]}([])}{}{}[](){}{}[](){}{}[]()'
    actual = multi_bracket_validation(string)
    expected = True
    assert actual == expected

# Unfortunately my solution does not know how to handle
# any letters being in the string so this fails
def test_string_with_letters():
    string = '(letters)'
    actual = multi_bracket_validation(string)
    expected = False
    assert actual == expected
