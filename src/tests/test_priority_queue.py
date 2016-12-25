"""Tests for priority queue."""


import pytest


@pytest.fixture
def empty_priorityqueue():
    """Define new instance of PriorityQueue class."""
    from src.priority_queue import PriorityQueue
    return PriorityQueue()


@pytest.fixture
def full_priorityqueue():
    """Define new instance of PriorityQueue class."""
    from src.priority_queue import PriorityQueue
    return PriorityQueue([(100, 7), (150, 1), (200, 5), (250, 0), (300, 5)])


def test_insert_in_empty_priorityqueue(empty_priorityqueue):
    """Test insert on empty queue without priority."""
    epq = empty_priorityqueue
    epq.insert(123)
    assert epq.tuples[0] == (123, 0)


def test_insert_in_empty_priorityqueue_with_priority(empty_priorityqueue):
    """Test insert on empty queue with priority."""
    epq = empty_priorityqueue
    epq.insert(123, 4)
    assert epq.tuples[0] == (123, 4)


def test_insert_in_full_priorityqueue(full_priorityqueue):
    """Test insert on full queue without priority."""
    fpq = full_priorityqueue
    fpq.insert(123)
    assert (123, 0) in fpq.tuples


def test_insert_in_full_priorityqueue_with_priority(full_priorityqueue):
    """Test insert on full queue with priority."""
    fpq = full_priorityqueue
    fpq.insert(123, 4)
    assert (123, 4) in fpq.tuples


def test_pop_empty(empty_priorityqueue):
    """Tests popping from an empty queue."""
    epq = empty_priorityqueue
    with pytest.raises(IndexError):
        epq.pop()


def test_pop_full(full_priorityqueue):
    """Tests popping from a full queue."""
    fpq = full_priorityqueue
    assert fpq.pop() == 250


def test_pop_remove(full_priorityqueue):
    """Tests that popping removes value from queue."""
    fpq = full_priorityqueue
    fpq.pop()
    assert fpq.pop() == 150


def test_peek_empty(empty_priorityqueue):
    """Tests that peeking at an empty priority queue returns None."""
    epq = empty_priorityqueue
    assert epq.peek() is None

def test_peek_full(full_priorityqueue):
    """Tests that peeking at a full priority queue returns the value with the lowest priority."""
    fpq = full_priorityqueue
    assert fpq.peek() == 250
