"""Test file for double linked list."""


import pytest


@pytest.fixture
def dll():
    """Fixture for testing iterables."""
    from double_linked_list import DoubleLinkedList
    return DoubleLinkedList([1, 2, 3])


@pytest.fixture
def empty():
    """Fixture for testing empty instantiations."""
    from double_linked_list import DoubleLinkedList
    return DoubleLinkedList()


def test_constructor(empty):
    """Test that DoubleLinkedList constructor creates a double linked list."""
    from double_linked_list import DoubleLinkedList
    assert type(empty) == DoubleLinkedList


def test_with_iterable1(dll):
    """Test that double linked list has the correct head."""
    assert dll.head.data is 3


def test_prev(dll):
    """Test that prev point to the node upwards on the chain."""
    assert dll.head.next.prev is dll.head


def test_tail(dll):
    """Test that the tail has the proper value."""
    assert dll.tail.data is 1


def test_push_empty(empty):
    """Test that we push to an empty list properly."""
    empty.push(3)
    assert empty.head.data is 3


def test_push_empty_next(empty):
    """Test that pushing into an empty dll has the right next value."""
    empty.push(3)
    assert empty.head.next is None


def test_push_empty_prev(empty):
    """Test that pushing into an empty dll has the right prev value."""
    empty.push(3)
    assert empty.head.prev is None


def test_push_full(dll):
    """Test that pushing into a list with values works."""
    dll.push(6)
    assert dll.head.data is 6


def test_push_full_next(dll):
    """Test that pushing into a filled list shows the right next value."""
    dll.push(6)
    assert dll.head.next.data is 3


def test_append(empty):
    """Test that appending to an empty list stores the right value."""
    empty.append(6)
    assert empty.tail.data is 6


def test_append_value(dll):
    """Test that appending to a list with values stores the right value."""
    dll.append(6)
    assert dll.tail.data is 6


def test_append_next(dll):
    """Test that appending to a list with values has the right next value."""
    dll.append(6)
    assert dll.tail.next is None


def test_append_prev(dll):
    """Test that appending to a list with values has the right prev value."""
    dll.append(6)
    assert dll.tail.prev.data is 1


def test_append_tail_reassign(dll):
    """Test that the old tail's next value is reassigned."""
    dll.append(6)
    assert dll.tail.prev.next is dll.tail


def test_pop_empty(empty):
    """Make sure that poping from an empty list returns the correct Exception."""
    error = False
    try:
        empty.pop()
    except AttributeError:
        error = True
    assert error


def test_pop_return(dll):
    """Make sure that popping from a populated list returns the value of the head node."""
    assert dll.pop() is 3


def test_pop_head(dll):
    """Make sure that popping from a populated list reassigns the head."""
    dll.pop()
    assert dll.head.data is 2


def test_pop_head_prev(dll):
    """Make sure that popping from a populated list reassigns the new head's prev attribute."""
    dll.pop()
    assert dll.head.prev is None


def test_shift_empty(empty):
    """Make sure that shifting from an empty list returns the correct Exception."""
    error = False
    try:
        empty.shift()
    except AttributeError:
        error = True
    assert error


def test_shift_return(dll):
    """Make sure that shifting from a populated list returns the value of the tail node."""
    assert dll.shift() is 1


def test_shift_tail(dll):
    """Make sure that shifting from a populated list reassigns the tail."""
    dll.shift()
    assert dll.tail.data is 2


def test_shift_tail_prev(dll):
    """Make sure that shifting from a populated list reassigns the new tail's prev attribute."""
    dll.shift()
    assert dll.tail.prev is None


def test_remove_empty(empty):
    """Makes sure that if removed is invoked with an empty list, an attribute error is raised."""
    error = False
    try:
        empty.search(5)
    except AttributeError:
        error = True
    assert error


def test_remove_invalid(dll):
    """Makes sure that if value isn't in list, a value error is raised."""
    error = False
    try:
        dll.remove(5)
    except ValueError:
        error = True
    assert error


def test_remove_valid(dll):
    """Makes sure that if value is valid, it removes the first node with the value."""
    dll.remove(2)
    assert dll.head.next.data is 1 and dll.tail.prev.data is 3


def test_remove_head(dll):
    """Makes sure that if value refers to head node, it will be removed properly."""
    dll.remove(3)
    assert dll.head.data is 2 and dll.head.prev is None


def test_remove_tail(dll):
    """Makes sure that if value refers to tail node, it will be removed properly."""
    dll.remove(3)
    assert dll.tail.data is 1 and dll.tail.next is None


def test_remove_multiple():
    """Makes sure that only the first value from the head is removed from the list."""
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList([1, 2, 4, 2, 3])
    dll.remove(2)
    assert dll.head.next.data is 4 and dll.tail.prev.data is 2


def test_search(dll):
    """Test that search returns a node with the given value."""

    assert dll.search(2) is dll.head.next


def test_search_none(dll):
    """Test that search returns None."""
    assert not dll.search(5)


def test_search_empty(empty):
    """Test that searching an empty list throws an attribute error."""
    error = False
    try:
        empty.search(5)
    except AttributeError:
        error = True
    assert error
