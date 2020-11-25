import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import Node, Queue, AnimalShelter, InvalidOperationError

def test_enqueue_cat():
    ams = AnimalShelter()
    ams.enqueue('cat')
    assert ams.cat_queue.peek() == 'cat'

def test_enqueue_dog():
    ams = AnimalShelter()
    ams.enqueue('dog')
    assert ams.dog_queue.peek() == 'dog'

def test_dequeue_cat():
    ams = AnimalShelter()
    ams.enqueue('cat')
    ams.enqueue('dog')
    ams.dequeue('cat')
    assert ams.cat_queue.is_empty() == True

def test_dequeue_dog():
    ams = AnimalShelter()
    ams.enqueue('cat')
    ams.enqueue('dog')
    ams.dequeue('dog')
    assert ams.dog_queue.is_empty() == True

def test_dequeue_not_cat_or_dog():
    ams = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        ams.dequeue('mouse')
