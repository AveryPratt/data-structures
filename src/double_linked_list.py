"""Creats a double linked list."""


class DoubleLinkedList(object):
    """A singly-linked list."""

    def __init__(self, data=None):
        """Create an instance of type LinkedList. Allow data to be passed in."""
        self.head = None
        self.tail = None
        if data is not None:
            try:
                for item in data:
                    if item is data[0]:
                        self.head = Node(item, next=None, prev=None)
                        self.tail = self.head
                    else:
                        node = Node(item, self.head, prev=None)
                        self.head.prev = node
                        self.head = node
            except TypeError:
                node = Node(data, next=None, prev=None)
                self.head = node
                self.tail = self.head


    def push(self, val):
        """Push a val to the end of the list."""
        node = Node(val, self.head, None)
        if self.head is not None:
            self.head.prev = node
        self.head = node


    def append(self, val):
        """Append a val to the  start of the list."""
        node = Node(val, None, self.tail)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node


    def pop(self):
        try:
            val = self.head.data
            if self.head.next == None:
                self.tail = None
                return val
            self.head = self.head.next
            self.head.prev = None
            return val
        except AttributeError:
            raise AttributeError("Cannot pop from an empty list.")


    def shift(self):
        try:
            val = self.tail.data
            if self.tail.prev == None:
                self.head = None
                return val
            self.tail = self.tail.prev
            self.tail.next = None
            return val
        except AttributeError:
            raise AttributeError("Cannot shift from an empty list.")


    def search(self, val):
        node = self.head
        while True:
            try:
                if node.data == val:
                    return node
                elif node == self.tail:
                    return None
                node = node.next
            except AttributeError:
                raise AttributeError("Cannot search an empty list.")


    def remove(self, val):
        """Searches each node starting from the head and removes the first node found containing the specified value."""
        node = self.search(val)
        if node == None:
            raise ValueError("Value not found: no nodes removed.")
        a = self.head
        while a is not node:
            a = a.next
        if a is self.tail:
            a.prev.next = None
            self.tail = a.prev
        elif a is self.head:
            a.next.prev = None
            self.head = a.next
        else:
            a.prev.next = a.next
            a.next.prev = a.prev


class Node(object):
    """Contains data to be organized into a doubly-linked list."""
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
