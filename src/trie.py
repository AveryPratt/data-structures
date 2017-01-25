"""Implementation of a trie data structure."""


class Trie(object):
    """A tree data structure...

    ...that groups related words in branches, which split where they
    differ from each other.

    insert(self, val):
    creates a new branch containing nodes that spell the value
    which diverges where the spelling differs from an existing branch

    contains(self, val):
    returns whether or not a value is contained as a branch of the trie

    size(self):
    returns the number of branches in the tree

    remove(self, val):
    finds the branch that the value is on and removes the nodes that are
    unique to that branch.
    """

    def __init__(self):
        """Create a new instance of a trie."""
        self._nodes = {"": set()}

    def insert(self, val):
        """Insert a value into the trie as a new branch."""
        for num in range(len(val) + 1):
            if self.contains(val[:len(val) - num]):
                self._add_branch(val, num)
                break

    def _add_branch(self, val, num):
        """Iteratively creates a branch by linking nodes...

        ...that add a letter each time until it spells the word.
        """
        for itr in range(num):
            idx = len(val) + itr - num
            self._nodes[val[:idx + 1]] = set()
            self._nodes[val[:idx]].add(val[:idx + 1])
        self._nodes[val].add("$")

    def contains(self, val):
        """Return whether a value is contained as a branch of the trie."""
        return val in self._nodes

    def size(self):
        """Return the number of branches in the trie."""
        return sum(1 for x in self._nodes.values() if '$' in x)

    def remove(self, val):
        """Remove the branch of the trie containing the value.

        (doesn't remove nodes that lead to other branches)
        """
        for num in range(len(val) + 1):
            if len(self._nodes[val[:len(val) - num]]) > 1:
                self._delete_branch(val, num)
                break

    def _delete_branch(self, val, num):
        """Delete a branch."""
        for itr in range(num):
            idx = len(val) + itr - num
            try:
                self._nodes[val[:idx]].remove(val[:idx + 1])
                del self._nodes[val[:idx + 1]]
            except KeyError:
                del self._nodes[val[:idx + 1]]
