


class Deque(object):
    """
    A doubly-ended queue where nodes can be removed from the head or the tail.

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

    size(): returns the count of items in the queue (returns 0 if the queue is empty).
    """
    def __init__(self):
        """Create a new instance of a doubly-ended queue."""
        self.head = None
        self.tail = None
        self.length = 0
        self.persist = True

    def append(self, val):
        """Add value to the end of the deque."""
        new_node = Node(val)
        if self.head is not None:
            self.head.prev_node = new_node
            new_node.next_node = self.head
        else:
            self.tail = new_node
        self.head = new_node
        self.persist = False

    def appendleft(self, val):
        """Add a value to the front of the deque."""
        new_node = Node(val)
        if self.tail is not None:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        else:
            self.head = new_node
        self.tail = new_node
        self.persist = False

    def pop(self):
        """Remove a value from the end of the deque and returns it
        (raises an exception if the deque is empty)."""
        if self.head is None:
            raise ValueError("Cannot pop from an empty deque.")
        val = self.head.val
        self.head = self.head.next_node
        self.head.prev_node = None
        self.persist = False
        return val

    def popleft(self):
        """Remove a value from the front of the deque and returns it
        (raises an exception if deque is empty)."""
        if self.tail is None:
            raise ValueError("Cannot popleft from an empty deque.")
        val = self.tail.val
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        self.persist = False
        return val

    def peek(self):
        """Return the next value that would be returned by pop but leaves the value in the deque
        (returns None if the deque is empty)."""
        if self.head:
            return self.head.val
        return None

    def peekleft(self):
        """Return the next value that would be returned by popleft but leaves the value in the
        deque (returns None if the deque is empty)."""
        if self.tail:
            return self.tail.val
        return None

    def size(self):
        """Return the count of items in the queue (returns 0 if the queue is empty)."""
        if not self.persist:
            self.length = 0
            if self.head:
                self.length = 1
            curr = self.head
            while curr is not self.tail:
                curr = curr.next_node
                self.length += 1
            return self.length
        return self.length


class Node(object):
    """A container to store data inside of a Deque."""

    def __init__(self, val, next_node=None, prev_node=None):
        """Set value, and links to other nodes in Deque."""
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node
