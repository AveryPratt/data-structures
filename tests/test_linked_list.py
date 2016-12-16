"""Tests for linked list class and it's methods.'"""


def test_constructor():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList()
    assert type(linked_list) == LinkedList


def test_with_iterable1():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.data is 3


def test_with_iterable2():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.next.data is 2 
    
    
def test_with_iterable3():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList([1, 2, 3])
    assert linked_list.head.next.next.data is 1


def test_with_non_iterable1():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList(42)
    assert linked_list.head.data is 42


def test_with_non_iterable2():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList(42)
    assert linked_list.head.next is None


def test_with_non_iterable3():
    from linked_list import LinkedList.__init__
    linked_list = LinkedList(42)
    assert linked_list.tail.data is 42


def test_push():
    from linked_list import LinkedList.push
    linked_list = LinkedList()
    linked_list.push(5)
    assert linked_list.head.data == 5


def test_pop():
    """Test that pop returns the correct value."""
    from linked_list import linked_list.pop
    linked_list = LinkedList([1,2,3,4])
    assert linked_list.pop() is 4


def test_pop2():
    """Test that pop properly resets next."""
    from linked_list import linked_list.pop
    linked_list = LinkedList([1,2,3,4])
    linked_list.pop()
    assert linked_list.head.data is 3

def test_pop3():
    """Test that pop properly clears tail when popping last node."""
    from linked_list import linked_list.pop
    linked_list = LinkedList(4)
    linked_list.pop()
    assert linked_list.tail is None

def test_size():
    """Test that size of an empty linked list is 0"""
    from linked_list import linked_list.size
    linked_list = LinkedList()
    assert linked_list.size is 0

def test_size2():
    """Test that the size of a linked list with values is correct."""
    from linked_list import linked_list.size
    linked_list = LinkedList([1,2,3,4])
    assert linked_list.size is 4

def test_search():
    """Test that search returns a node with the given value."""
    from linked_list import linked_list.search
    linked_list = LinkedList([1,2,3,4])
    assert linked_list.search(2) is linked_list.head.next.next 

def test_push_method():
