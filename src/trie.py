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

    depth_first_traversal(self, start):
    returns a generator that returns a pre-order path of letters in a depth-first traversal
    starting at the input value.
    """

    def __init__(self):
        """Create a new instance of a trie."""
        self._nodes = {"": set()}

    def insert(self, val):
        """Insert a value into the trie as a new branch."""
        if type(val) is not str:
            raise TypeError("Trie can only take values that are strings.")
        for num in range(len(val) + 1):
            if self._in_chain(val[:len(val) - num]):
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
        for key, value in self._nodes.items():
            if key == val and "$" in value:
                return True
        return False

    def _in_chain(self, val):
        """Return whether a value is part of a branch of the trie."""
        return val in self._nodes

    def size(self):
        """Return the number of branches in the trie."""
        return sum(1 for x in self._nodes.values() if '$' in x)

    def remove(self, val):
        """Remove the branch of the trie containing the value.

        (doesn't remove nodes that lead to other branches)
        """
        if not self.contains(val):
            raise ValueError("Cannot remove a value that is not in the trie.")
        for num in range(len(val) + 1):
            if len(self._nodes[val[:len(val) - num]]) > 1:
                self._delete_branch(val, num)
                break

    def _delete_branch(self, val, num):
        """Delete a branch."""
        if num <= 0:
            self._nodes[val[:len(val) - num]].remove("$")
        for itr in range(num):
            idx = len(val) + itr - num
            del self._nodes[val[:idx + 1]]

    def depth_first_traversal(self, start=""):
        """Return all the possibe words that could result from start."""
        to_visit = [start]
        while to_visit:
            curr = to_visit[-1]
            yield curr[-1] if curr else ""
            try:
                if len(self._nodes[curr]) == 1 and "$" in self._nodes[curr]:
                    to_visit.pop()
                    if not len(to_visit):
                        break
                elif len(self._nodes[curr]) == 1:
                    to_visit[-1] = list(self._nodes[curr])[0]
                else:
                    new_nodes = self._nodes[curr]
                    if "$" in new_nodes:
                        new_nodes.remove("$")
                    if len(new_nodes) == 1:
                        to_visit[-1] = list(new_nodes)[0]
                    else:
                        if start in to_visit:
                            to_visit.remove(start)
                        tmp = list(new_nodes)
                        new_list = sorted(tmp, reverse=True)
                        if to_visit:
                            to_visit.pop()
                        to_visit.extend(new_list)
                        try:
                            curr = to_visit[-1]
                        except IndexError:
                            break
            except KeyError:
                raise ValueError("starting value is not in trie.")
        raise StopIteration
