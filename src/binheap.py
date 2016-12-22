"""Creates a binary min-heap based off of a list with push and pop methods."""


class BinHeap(object):
    """
    A binary min-heap class based off of a list.

    push(val): adds a value to the last index on the heap,
    and throws a type error if the value is not an int or float.

    pop(): removes the value in the first index (top) of the heap,
    and fills in the remaining space with the smallest number available.
    """

    def __init__(self, lst=None):
        """Creates an instance of a binary min-heap using a list."""
        self.lst = []
        for val in lst:
            self.push(val)


    def push(self, val):
        """Adds a value to the last index on the heap, and then sorts the heap."""
        if not isinstance(val, int) and not isinstance(val, float):
            raise TypeError("Cannot add a non-numerical member to a binary heap.")
        self.lst.append(val)
        self._sink(self.lst[-1])


    def pop(self):
        """Removes the value at the first index on the heap, and then sorts the heap."""
        if len(self.lst) < 1:
            raise IndexError("Cannot pop from an empty heap.")
        val = self.lst[0]
        self.lst[0] = None
        self._bubble()
        return val


    def _check_swap(self, ind):
        """Checks whether a node can be swapped with one of it's child nodes"""
        first = 2 * ind + 1
        second = first + 1
        try:
            lesser_ind = first if self.lst[first] <= self.lst[second] else second
        except IndexError:
            lesser_ind = self.lst[first]
        if self.lst[lesser_ind] < self.lst[ind] or self.lst[ind] is None:
            self.lst[ind], self.lst[lesser_ind] = self.lst[lesser_ind], self.lst[ind]
            return lesser_ind
        return None


    def _bubble(self):
        if len(self.lst) > 1:
            pointer = 0
            while pointer is not None and pointer < len(self.lst) // 2:
                pointer = self._check_swap(pointer)
            for ind in range(pointer, len(self.lst) - 1):
                self.lst[ind] = self.lst[ind + 1]
            self.lst = self.lst[-1]
            return True
        return False


    def _sink(self, pointer):
        if len(self.lst) > 1 and pointer >= 0 and pointer < len(self.lst):
            swapped = 0
            while swapped is not None:
                pointer = (pointer - 1) // 2
                swapped = self._check_swap(pointer)
            return True
        return False
