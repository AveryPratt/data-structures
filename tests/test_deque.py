"""Tests methods on Deque object."""

import pytest


@pytest.fixture
def emptydq():
    """Creates an empty Deque for testing."""
    from src.deque import Deque
    return Deque()


@pytest.fixture
def fulldq():
    """Creates an empty Deque for testing."""
    from src.deque import Deque
    deq = Deque()
    deq.append(1)
    deq.append(2)
    deq.append(3)
    return deq


def test_append1(emptydq):
    emptydq.append("hi")
    assert emptydq.head.val is "hi"


def test_append2(fulldq):
    assert fulldq.head.val is 3


def test_append3(fulldq):
    assert fulldq.head.next_node.val is 2


def test_append4(fulldq):
    assert fulldq.head.next_node.prev_node.val is 3


def test_appendleft(emptydq):
    emptydq.appendleft("hi")
    assert emptydq.tail.val is "hi"


def test_appendleft2(emptydq):
    emptydq.appendleft(1)
    emptydq.appendleft(2)
    emptydq.appendleft(3)
    assert emptydq.tail.val is 3


def test_appendleft3(emptydq):
    emptydq.appendleft(1)
    emptydq.appendleft(2)
    emptydq.appendleft(3)
    assert emptydq.tail.prev_node.val is 2


def test_appendleft4(emptydq):
    emptydq.appendleft(1)
    emptydq.appendleft(2)
    emptydq.appendleft(3)
    assert emptydq.tail.prev_node.next_node is 3


def test_pop1(fulldq):
    assert fulldq.pop() == 3


def test_pop2(fulldq):
    fulldq.pop()
    assert fulldq.head.val == 2


def test_pop3(fulldq):
    fulldq.pop()
    assert fulldq.head.next_node is None


def test_pop4(emptydq):
    with pytest.raises(ValueError) as excinfo:
        emptydq.pop()
    excinfo.match("Cannot pop from an empty deque.")


def test_popleft1(fulldq):
    assert fulldq.popleft() == 1


def test_popleft2(fulldq):
    fulldq.popleft()
    assert fulldq.tail.val == 2


def test_popleft3(fulldq):
    fulldq.popleft()
    assert fulldq.tail.prev_node is None


def test_popleft4(emptydq):
    with pytest.raises(ValueError) as excinfo:
        emptydq.pop()
    excinfo.match("Cannot popleft from an empty deque.")


def test_peek1(emptydq):
    assert emptydq.peek() == None


def test_peek2(fulldq):
    assert fulldq.peek() == 3


def test_peek3(fulldq):
    fulldq.peek()
    assert fulldq.peek() == 3


def test_peekleft1(emptydq):
    assert emptydq.peekleft() == None


def test_peekleft2(fulldq):
    assert fulldq.peekleft() == 1


def test_peekleft3(fulldq):
    fulldq.peekleft()
    assert fulldq.peekleft() == 1


def test_size1(emptydq):
    assert emptydq.size() == 0


def test_size2(emptydq):
    emptydq.append(1)
    emptydq.appendleft(2)
    assert emptydq.size() == 2


def test_size3(emptydq):
    emptydq.append(1)
    emptydq.appendleft(2)
    emptydq.append(3)
    emptydq.pop()
    emptydq.popleft()
    assert emptydq.size() == 1
