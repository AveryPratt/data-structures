"""Test file for stack.py."""


import pytest


@pytest.fixture
def st():
    from stack import Stack
    return Stack([1, 2, 3])


def test_init():
    from stack import Stack
    st = Stack()
    assert type(st) is Stack


def test_with_iterable(st):
    assert st._linked_list.head.data is 3


def test_with_iterable2(st):
    assert st._linked_list.head.next.data is 2


def test_with_iterable3(st):
    assert st._linked_list.head.next.next.data is 1


def test_push_iterable1(st):
    st.push(4)
    assert st._linked_list.head.data is 4


def test_push_iterable2(st):
    st.push(4)
    assert st._linked_list.head.next.data is 3


def test_pop(st):
    st.pop()
    assert st._linked_list.head.data is 2


def test_pop_return(st):
    assert st.pop() is 3
