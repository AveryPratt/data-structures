"""Test file for priority queue."""
import pytest


INIT = [
    [134, 0, (45, 5)],
    [2346, 5, (2346, 5)],
    ['sdf', 10, ('sdf', 10)],
]


@pytest.fixture
def pri_q_empty():
    """Create an empty instance of our Priority Queue."""
    from priority_queue import PriorityQueue
    return PriorityQueue()


def test_init_type():
    """Test that a pri_q is an instance of PriorityQueue."""
    from priority_queue import PriorityQueue
    pri_q = PriorityQueue()
    assert isinstance(pri_q, PriorityQueue)


def test_init_data():
    """Test that init properly calls _prioritize."""
    from priority_queue import PriorityQueue
    pri_q = PriorityQueue(4, 6)
    assert pri_q._q == [(4, 6)]


def test_insert(pri_q_empty):
    """Test that insert properly adds to the _q list."""
    pri_q_empty.insert(1)
    pri_q_empty.insert(3, 5)
    assert pri_q_empty._q == [(1, 0), (3, 5)]


@pytest.mark.parametrize('input, pri, answer', INIT)
def test_pop(pri_q_empty, input, pri, answer):
    pri_q_empty.insert(3, 4)
    pri_q_empty.insert(input, pri)
    pri_q_empty.insert(45, 5)
    assert pri_q_empty.pop() == answer


@pytest.mark.parametrize('input, pri, answer', INIT)
def test_peek(pri_q_empty, input, pri, answer):
    pri_q_empty.insert(3, 4)
    pri_q_empty.insert(input, pri)
    pri_q_empty.insert(45, 5)
    assert pri_q_empty.peek() == answer
