"""Tests for linked list class and it's methods."""


import pytest


def test_constructor():
    """Test that LinkedList constructor creates a linked list."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    assert type(linked_list) == LinkedList


def test_with_iterable1():
    """Test that linked list has the correct head."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.data is 3


def test_with_iterable2():
    """Test that linked list nodes point to the proper nodes."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.next.data is 2


def test_with_iterable3():
    """Test that linked list nodes create a chain."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.next.next.data is 1


def test_with_non_iterable1():
    """Test that linked list with non-iterable data works."""
    from linked_list import LinkedList
    linked_list = LinkedList(42)
    assert linked_list.head.data is 42


def test_with_non_iterable2():
    """Test that linked list with non-iterable data doesn't point to anything."""
    from linked_list import LinkedList
    linked_list = LinkedList(42)
    assert linked_list.head.next is None


def test_with_non_iterable3():
    """Test that linked list creates a tail."""
    from linked_list import LinkedList
    linked_list = LinkedList(42)
    assert linked_list.tail.data is 42


def test_push():
    """Test that linked_list.push adds a node at the head."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(5)
    assert linked_list.head.data == 5


def test_pop():
    """Test that pop returns the correct value."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    assert linked_list.pop() is 4


def test_pop2():
    """Test that pop properly resets next."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    linked_list.pop()
    assert linked_list.head.data is 3


def test_pop3():
    """Test that pop properly clears tail when popping last node."""
    from linked_list import LinkedList
    linked_list = LinkedList(4)
    linked_list.pop()
    assert linked_list.tail is None


def test_pop4():
    """Test that popping from an empty list returns None."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    assert linked_list.pop() is None


def test_size():
    """Test that size of an empty linked list is 0."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    assert linked_list.size() is 0


def test_size2():
    """Test that the size of a linked list with values is correct."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    assert linked_list.size() is 4


def test_size3():
    """Test that the size of a linked list after pushing a value is 1."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(50)
    assert linked_list.size() == 1


def test_search():
    """Test that search returns a node with the given value."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    assert linked_list.search(2) is linked_list.head.next.next


def test_search2():
    """Test that search returns None."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    assert not linked_list.search(5)


def test_remove():
    """Test that node is properly removed."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    linked_list.remove(linked_list.head.next)
    assert linked_list.head.next.data is 2


def test_remove2():
    """Test that node is properly removed."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    linked_list.remove(linked_list.head)
    assert linked_list.head.data is 3


def test_remove3():
    """Test that node is properly removed."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    linked_list.remove(linked_list.tail)
    assert linked_list.tail.data is 2


def test_remove4():
    """Test that node is properly removed."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    with pytest.raises(AttributeError):
        linked_list.remove(linked_list.head)


def test_display():
    """Test that display returns a unicode string."""
    from linked_list import LinkedList
    linked_list = LinkedList([1, 2, 3, 4])
    assert linked_list.display() == '(4, 3, 2, 1)'


def test_display2():
    """Test that display returns a unicode string."""
    from linked_list import LinkedList
    linked_list = LinkedList(1)
    assert linked_list.display() == '(1)'


def test_display3():
    """Test that display returns a unicode string."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    assert linked_list.display() == '()'

def test_display4():
    """Test that display returns a string with the value that was pushed."""
    from linked_list import LinkedList
    linked_list = LinkedList()
    linked_list.push(50)
    assert linked_list.display() == "(50)"
