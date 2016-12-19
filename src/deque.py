


class Deque(object):
    """A doubly-ended queue where nodes can be removed from the head or the tail.
    
    append(val): adds value to the end of the deque.

    appendleft(val): adds a value to the front of the deque.

    pop(): removes a value from the end of the deque and returns it
    (raises an exception if the deque is empty).

    popleft(): removes a value from the front of the deque and returns it
    (raises an exception if deque is empty).

    peek(): returns the next value that would be returned by pop but leaves the value in the deue
    (returns None if the deque is empty).

    peekleft(): returns the next value that would be returned by popleft but leaves the value in the
    deque (returns None if the deque is empty).

    size(): returns the count of items in the queue (returns 0 if the queue is empty)."""
    def __init__(self):
        """Creates a new instance of a doubly-ended queue."""
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, val):
        """adds value to the end of the deque."""
        pass


    def appendleft(self, val):
        """adds a value to the front of the deque."""
        pass


    def pop(self):
        """removes a value from the end of the deque and returns it
        (raises an exception if the deque is empty)."""
        if self.head.val is None:
            raise ValueError("Cannot pop from an empty deque.")


    def popleft(self):
        """removes a value from the front of the deque and returns it
        (raises an exception if deque is empty)."""
        if self.tail.val is None:
            raise ValueError("Cannot popleft from an empty deque.")


    def peek(self):
        """returns the next value that would be returned by pop but leaves the value in the deque
        (returns None if the deque is empty)."""
        pass


    def peekleft(self):
        """returns the next value that would be returned by popleft but leaves the value in the
        deque (returns None if the deque is empty)."""
        pass


    def size(self):
        """returns the count of items in the queue (returns 0 if the queue is empty)."""
        pass


class Node(object):
    """A container to store data inside of a Deque."""

    def __init__(self, val, next_node, prev_node):
        """Sets value, and links to other nodes in Deque."""
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node
