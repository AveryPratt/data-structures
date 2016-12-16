"""Implementation of queue data structure."""


class Queue(object):
    """A singly-linked list."""

    def __init__(self):
        """Create an instance of type Queue. Allow data to be passed in."""
        self.head = None
        self.tail = None

    def enqueue(self, val):
        """Append a val to the end of the queue."""
        node = Node(val, None, self.tail)
        if self.size() == 0:
            self.head = node
        old_tail = self.tail
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        self.tail.prev = old_tail

    def dequeue(self):
        """Remove and returns the first item in the queue."""
        try:
            val = self.head.data
            if self.head.next is None:
                self.tail = None
            self.head = self.head.next
            self.head.prev = None
            return val
        except AttributeError:
            raise AttributeError("Cannot pop from an empty list.")

    def size(self):
        """Count the number of items in the queue."""
        cur = self.head
        count = 0
        if self.head:
            count = 1
        while self.tail is not cur:
            count += 1
            cur = cur.next
        return count

    def peek(self):
        """Return the data attribute of Head."""
        return self.head.data


class Node(object):
    """Contain data to be organized into a doubly-linked list."""

    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
