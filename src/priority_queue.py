"""Priority queue."""


class PriorityQueue(object):
    """A priority queue."""

    def __init__(self, val=None, pri=0):
        """Create an instance of a Priority Queue."""
        self._q = []
        if val is None:
            return None
        self.insert(val, pri)

    def insert(self, val, pri=0):
        """Insert an item into a queue."""
        if type(pri) is int:
            self._q += [(val, pri)]
        else:
            assert TypeError('Priority must be int.')

    def pop(self):
        """Remove the highest prioritized item."""
        try:
            pri = 0
            for i in range(len(self._q)):
                if self._q[pri][1] < self._q[i][1]:
                    pri = i
            return self._q.pop(pri)
        except IndexError:
            raise IndexError('Can not pop from empty list.')

    def peek(self):
        """View the value of the highest prioritized item without removing it."""
        try:
            pri = 0
            for i in range(len(self._q)):
                if self._q[pri][1] < self._q[i][1]:
                    pri = i
            return self._q[pri]
        except IndexError:
            raise IndexError('Can not peek empty list.')
