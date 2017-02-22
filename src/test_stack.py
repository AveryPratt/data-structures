"""Test file for stack.py."""


import pytest


ITER_TESTS = [
    [1, 2, 3],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    ["hi", "my", "name", "is", "bob"]
]


@pytest.fixture(params=ITER_TESTS)
def st(request):
    """Create a fixture with a list as the value."""
    from stack import Stack
    return Stack(request.param), request.param


def test_init(st):
    """Test creation of an empty stack."""
    from stack import Stack
    assert type(st[0]) is Stack


def test_with_iterable(st):
    """Test creation of a stack with an iterable."""
    assert st[0]._linked_list.head.data is st[1][-1]


def test_with_iterable2(st):
    """Test creation of a stack with an iterable."""
    assert st[0]._linked_list.head.next.data is st[1][-2]


def test_with_iterable3(st):
    """Test creation of a stack with an iterable."""
    assert st[0]._linked_list.head.next.next.data is st[1][-3]


def test_push_iterable1(st):
    """Test push method with iterable input."""
    st[0].push(4)
    assert st[0]._linked_list.head.data is 4


def test_push_iterable2(st):
    """Test push method with iterable input."""
    st[0].push(4)
    assert st[0]._linked_list.head.next.data is st[1][-1]


def test_pop(st):
    """Test that pop removes the top object."""
    st[0].pop()
    assert st[0]._linked_list.head.data is st[1][-2]


def test_pop_empty():
    """Test that popping from an empty stack returns None."""
    from stack import Stack
    st = Stack()
    assert st.pop() is None


def test_pop_return(st):
    """Test that pop returns the right value."""
    assert st[0].pop() is st[1][-1]
