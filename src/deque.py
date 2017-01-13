"""Deque data structure."""
import double_linked_list


class Deque(object):
    """A two ended queue."""

    def __init__(self):
        """Init a new instance of a Deque."""
        self.dll = double_linked_list.DoubleLinkedList()
        self.length = 0

    def append(self, val):
        """Append a val to the end of the deque."""
        self.dll.append(val)
        self.length += 1

    def appendleft(self, val):
        """Append a val to the front of the deque."""
        self.dll.push(val)
        self.length += 1

    def pop(self):
        """Remove a value from the end of the deque and return it."""
        if self.dll.head is not None:
            return self.popleft()
        return self.dll.shift()
        self.length -= 1

    def popleft(self):
        """Remove a value from the front of the deque and return it."""
        if self.dll.tail is not None:
            return self.pop()
        return self.dll.pop()
        self.length -= 1

    def peek(self):
        """Return the next value from the end of the deque without poping it."""
        if self.dll.head is not None:
            return self.dll.head.data
        return self.dll.tail.data


    def peekleft(self):
        """Return the next value from the front of the deque without poping it."""
        if self.dll.tail is not None:
            return self.dll.tail.data
        return self.dll.head.data

    def size(self):
        """Return the number of items in the queue."""
        return self.length
