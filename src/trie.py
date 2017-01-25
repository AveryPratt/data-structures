"""Implementation of a trie data structure."""


class Trie(object):
    """A tree data structure that groups related words in branches,
    which split where they differ from each other.

    insert(self, val):
    creates a new branch containing nodes that spell the value
    which diverges where the spelling differs from an existing branch

    contains(self, val):
    returns whether or not a value is contained as a branch of the trie

    size(self):
    returns the number of branches in the tree

    remove(self, val):
    finds the branch that the value is on and removes the nodes that are unique to that branch
    """

    def __init__(self):
        """Create a new instance of a trie."""
        pass

    def insert(self, val):
        """Insert a value into the trie as a new branch."""
        pass

    def contains(self, val):
        """Return whether a value is contained as a branch of the trie."""
        pass

    def size(self):
        """Return the number of branches in the trie."""
        pass

    def remove(self, val):
        """Remove the branch of the trie containing the value.
        (doesn't remove nodes that lead to other branches)"""
        pass
