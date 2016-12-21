"""Creates a binary min-heap based off of a list with push and pop methods."""


class BinHeap(object):
    """
    A binary min-heap class based off of a list.

    push(val): adds a value to the last index on the heap,
    and throws a type error if the value is not an int or float.

    pop(): removes the value in the first index (top) of the heap,
    and fills in the remaining space with the smallest number available.
    """

    def __init__(self, lst=[]):
        """Creates an instance of a binary min-heap using a list."""
        for val in lst:
            if not isinstance(val, int) and not isinstance(val, float):
                raise TypeError("Cannot create a binary heap out of a list " +
                                "that contains non-numerical members.")
        self.lst = lst

    def push(self, val):
        """Adds a value to the last index on the heap, and then sorts the heap."""
        if not isinstance(val, int) and not isinstance(val, float):
            raise TypeError("Cannot add a non-numerical member to a binary heap.")
        self.lst.append(val)


    def pop(self):
        """Removes the value at the first index on the heap, and then sorts the heap."""
        self.lst[0] = None
        self._bubble()
        for ind in range(len(self.lst) // 2, len(self.lst) - 1):
            if self.lst[ind] is None:
                self.lst[ind] = self.lst[ind + 1]
        self.lst = self.lst[:-1]
        for ind in range(len(self.lst) // 2 - 1, -1, -1):
            self._check_swap(ind)


    def _check_swap(self, ind):
        """Checks whether a node can be swapped with one of it's child nodes"""
        first = 2 * ind + 1
        second = first + 1
        try:
            lesser_ind = first if self.lst[first] <= self.lst[second] else second
        except AttributeError:
            lesser_ind = self.lst[first]
        if self.lst[lesser_ind] < self.lst[ind] or self.lst[ind] is None:
            self.lst[ind], self.lst[lesser_ind] = self.lst[lesser_ind], self.lst[ind]
            return lesser_ind
        return False


    def _bubble(self, pointer=0):
        while pointer < len(self.lst) // 2:
            pointer = self._check_swap(pointer)


    def _sink(self, pointer=None):
        if pointer is None:
            pointer = len(self.lst) // 2 - 1


    def _cascade(self):
        cascade_ind = len(self.lst) // 2 - 1
        while True:
            swapped = self._check_swap(cascade_ind)
            cascade_ind = (cascade_ind - 1) // 2
            if not swapped:
                break
