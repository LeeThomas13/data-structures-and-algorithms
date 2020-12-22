from code_challenges.repeated_word.repeated_word import find_repeats
import pytest


def test_repeated_word():
    str = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = find_repeats(str)
    expected = 'summer'
    assert actual == expected

def test_repeated_word_two():
    str = "Once upon a time, there was a brave princess who..."
    actual = find_repeats(str)
    expected = 'a'
    assert actual == expected

def test_repeated_word_three():
    str = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = find_repeats(str)
    expected = 'times'
    assert actual == expected

def test_no_input():
    str = ''
    actual = find_repeats(str)
    expected = 'There\'s no string here...'
    assert actual == expected
