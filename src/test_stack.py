"""Test file for stack.py."""


import pytest


@pytest.fixture
def st():
    """Create a fixture with a list as the value."""
    from stack import Stack
    return Stack([1, 2, 3])


def test_init():
    """Test creation of an empty stack."""
    from stack import Stack
    st = Stack()
    assert type(st) is Stack


def test_with_iterable(st):
    """Test creation of a stack with an iterable."""
    assert st._linked_list.head.data is 3


def test_with_iterable2(st):
    """Test creation of a stack with an iterable."""
    assert st._linked_list.head.next.data is 2


def test_with_iterable3(st):
    """Test creation of a stack with an iterable."""
    assert st._linked_list.head.next.next.data is 1


def test_push_iterable1(st):
    """Test push method with iterable input."""
    st.push(4)
    assert st._linked_list.head.data is 4


def test_push_iterable2(st):
    """Test push method with iterable input."""
    st.push(4)
    assert st._linked_list.head.next.data is 3


def test_pop(st):
    """Test that pop removes the top object."""
    st.pop()
    assert st._linked_list.head.data is 2


def test_pop_empty():
    """Test that popping from an empty stack returns None."""
    from stack import Stack
    st = Stack()
    assert st.pop() is None


def test_pop_return(st):
    """Test that pop returns the right value."""
    assert st.pop() is 3
