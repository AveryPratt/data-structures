"""Implements a stack class."""


import linked_list as ll


class Stack(object):
    """A single stack."""

    def __init__(self, value=None):
        """Init the new instance of Stack."""
        self._linked_list = ll.LinkedList(value)

    def push(self, value):
        """Add a new node to the top of the stack."""
        return self._linked_list.push(value)

    def pop(self):
        """Remove the top node from the stack."""
        return self._linked_list.pop()
