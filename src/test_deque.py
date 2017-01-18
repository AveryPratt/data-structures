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
    """Tests that an empty deque can append an item to the head."""
    emptydq.append("hi")
    assert emptydq.head.val is "hi"


def test_append2(fulldq):
    """Tests that the last item appended to a deque is the head."""
    assert fulldq.head.val is 3


def test_append3(fulldq):
    """Tests that the head is connected to the next node in the deque."""
    assert fulldq.head.next_node.val is 2


def test_append4(fulldq):
    """Tests that the second node is connected to the head of the deque."""
    assert fulldq.head.next_node.prev_node.val is 3


def test_appendleft(emptydq):
    """Tests that appendleft function works on an empty deque."""
    emptydq.appendleft("hi")
    assert emptydq.tail.val is "hi"


def test_appendleft2(emptydq):
    """Tests that appendleft adds value to a node at the tail."""
    emptydq.appendleft(1)
    emptydq.appendleft(2)
    emptydq.appendleft(3)
    assert emptydq.tail.val is 3


def test_appendleft3(emptydq):
    """Tests that a node appendlefted to a deque is connected to the previous node."""
    emptydq.appendleft(1)
    emptydq.appendleft(2)
    emptydq.appendleft(3)
    assert emptydq.tail.prev_node.val is 2


def test_appendleft4(emptydq):
    """Tests that the previous node is connected to the tail after appendlefting."""
    emptydq.appendleft(1)
    emptydq.appendleft(2)
    emptydq.appendleft(3)
    assert emptydq.tail.prev_node.next_node.val is 3


def test_pop1(fulldq):
    """Tests that pop returns the value at the head of the deque."""
    assert fulldq.pop() == 3


def test_pop2(fulldq):
    """Tests that pop removes the value at the head of the deque and sets the head to the next node."""
    fulldq.pop()
    assert fulldq.head.val == 2


def test_pop3(fulldq):
    """Tests that head is connected to next node after popping."""
    fulldq.pop()
    assert fulldq.head.next_node.val is 1


def test_pop4(emptydq):
    """Tests that popping from an empty deque raises a value error."""
    with pytest.raises(ValueError, "Cannot pop from an empty deque.")
        emptydq.pop()


def test_popleft1(fulldq):
    """Tests that popleft returns value at tail of deque."""
    assert fulldq.popleft() == 1


def test_popleft2(fulldq):
    """Tests that popleft removes value at tail of deque and replaces it with the previous node."""
    fulldq.popleft()
    assert fulldq.tail.val == 2


def test_popleft3(fulldq):
    """Tests that tail is connected to previous node after poplefting."""
    fulldq.popleft()
    assert fulldq.tail.prev_node.val is 3


def test_popleft4(emptydq):
    """Tests that poplefting from an empty deque raises a value error."""
    with pytest.raises(ValueError) as excinfo:
        emptydq.popleft()
    excinfo.match("Cannot popleft from an empty deque.")


def test_peek1(emptydq):
    """Tests that peeking at an empty deque returns None."""
    assert emptydq.peek() == None


def test_peek2(fulldq):
    """Tests that peeking at a full deque returns the value at the head of the deque."""
    assert fulldq.peek() == 3


def test_peek3(fulldq):
    """Tests that peeking at a full deque doesn't remove the node at the head of the deque."""
    fulldq.peek()
    assert fulldq.peek() == 3


def test_peekleft1(emptydq):
    """Tests that peeklefting at an empty deque returns None."""
    assert emptydq.peekleft() == None


def test_peekleft2(fulldq):
    """Tests that peeklefting at a full deque returns the value at the tail."""
    assert fulldq.peekleft() == 1


def test_peekleft3(fulldq):
    """Tests that peeklefting at a full deque doesn't remove the node at the tail."""
    fulldq.peekleft()
    assert fulldq.peekleft() == 1


def test_size1(emptydq):
    """Tests that size returns 0 from an empty deque."""
    assert emptydq.size() == 0


def test_size2(emptydq):
    """Tests that size returns the correct length after appending and appendlefting to a deque."""
    emptydq.append(1)
    emptydq.appendleft(2)
    assert emptydq.size() == 2


def test_size3(emptydq):
    """Tests that size returns the correct length after appending and popping (right and left) to a deque."""
    emptydq.append(1)
    emptydq.appendleft(2)
    emptydq.append(3)
    emptydq.pop()
    emptydq.popleft()
    assert emptydq.size() == 1
