"""Creates a binary min-heap based off of a list with push and pop methods."""


class BinHeap(object):
    """
    A binary min-heap class based off of a list.

    push(val): adds a value to the last index on the heap,
    and throws a type error if the value is not an int or float.

    pop(): removes the value in the first index of the heap,
    and fills in the remaining space with the smallest number available.
    """
    def __init__(self, lst=None):
        """Creates an instance of a binary min-heap using a list."""
        self._lst = []
        if lst == None:
            lst = []
        for val in lst:
            self.push(val)

    def push(self, val):
        """Adds a value to the last index on the heap, and then sorts the heap."""
        self._lst.append(val)
        self._sink(len(self._lst) - 1)

    def pop(self):
        """Removes the value at the first index on the heap, and then sorts the heap."""
        val = self._lst[0]
        self._lst[0] = self._lst[len(self._lst) - 1]
        self._bubble(0)
        self._lst = self._lst[:-1]
        return val

    def _bubble(self, ind):
        """Pushes value at ind up the heap until both of it's children's values are greater."""
        first_child = (2 * ind) + 1
        if first_child >= len(self._lst):
            return
        second_child = first_child + 1
        try:
            child_ind = first_child if self._lst[first_child] < self._lst[second_child] else second_child
        except IndexError:
            child_ind = first_child
        if self._lst[ind] > self._lst[child_ind]:
            self._lst[ind], self._lst[child_ind] = self._lst[child_ind], self._lst[ind]
            self._bubble(child_ind)

    def _sink(self, ind):
        """Pushes value down the heap until it's parent's value is less."""
        if ind == 0:
            return
        parent_ind = (ind - 1) // 2
        if self._lst[ind] < self._lst[parent_ind]:
            self._lst[ind], self._lst[parent_ind] = self._lst[parent_ind], self._lst[ind]
            self._sink(parent_ind)
