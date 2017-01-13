"""Test file for deque.py."""
from double_linked_list import DoubleLinkedList
import pytest


@pytest.fixture
def dq():
    """Create a deque."""
    from deque import Deque
    return Deque()


def test_init(dq):
    """Test that init creates a new instance of a dll."""
    assert type(dq.dll) is DoubleLinkedList


def test_append(dq):
    """Test that append adds a new value to the end of the deque."""
    dq.append(5)
    assert dq.dll.tail.data is 5


def test_append_left(dq):
    """Test that append left adds a new value to the start of the deque."""
    dq.appendleft(3)
    assert dq.dll.head.data is 3


def test_pop(dq):
    """Test that pop removes and returns the value from the end of the deque."""
    dq.append(4)
    assert dq.pop() is 4


def test_pop_head(dq):
    """Test that pop can remove the head when it is the only value."""
    dq.appendleft(4)
    assert dq.pop() is 4


def test_pop_empty(dq):
    """Test that pop on an empty list throws an error."""
    with pytest.raises(AttributeError):
        dq.pop()


def test_pop_left(dq):
    """Test pop left returns the value head."""
    dq.appendleft(4)
    assert dq.popleft() is 4


def test_pop_left_tail(dq):
    """Test left pop remove tail when only a value."""
    dq.append(4)
    assert dq.popleft() is 4


def test_pop_left_empty(dq):
    """Test pop left on an empty list."""
    with pytest.raises(AttributeError):
        dq.popleft()


def test_peek(dq):
    """Test next value that would be pop without popping itself."""
    dq.appendleft(5)
    assert dq.dll.head.data is 5


def test_peekleft(dq):
    """Test for value popleft without popping."""
    dq.appendleft(4)
    assert dq.peekleft() is 4


def test_size(dq):
    """Test size returns length of the dq."""
    dq.appendleft(4)
    dq.append(4)
    assert dq.size() is 2
