"""Implements a linked list class."""


class LinkedList(object):
    """A singly-linked list."""

    def __init__(self, data=None):
        """Create an instance of type LinkedList. Allow data to be passed in."""
        self.head = None
        self.tail = None
        if data is not None:
            try:
                for item in data:
                    if item is data[0]:
                        self.head = Node(item, next=None)
                        self.tail = self.head
                    else:
                        self.head = Node(item, self.head)
            except TypeError:
                node = Node(data, next=None)
                self.head = node
                self.tail = self.head


    def push(self, val):
        self.head = Node(val, self.head)


    def pop(self):
        val = self.head.data
        if self.head.next == None:
            self.tail = None
        self.head = self.head.next
        return val

    def size(self):
        a = self.head
        count = 0
        if self.head:
            count = 1
        while self.tail is not a:
            count +=1
            a = a.next
        return count


    def search(self, val):
        node = self.head
        while True:
            if node.data == val:
                return node
            elif node == self.tail:
                return None
            node = node.next


    def remove(self, node):
        if node is self.head:
            self.head = node.next
        else:
            a = self.head
            while a.next is not node:
                a = a.next
            if node is self.tail:
                self.tail = a
                a.next = None
            else:
                a.next = node.next


    def display(self):
        if self.head is None:
            return '()'
        elif self.head is self.tail:
            return '(' + str(self.head.data) + ')'
        dis = '(' + str(self.head.data)
        a = self.head
        while a.next is not self.tail:
            dis += ', ' + str(a.next.data)
            a = a.next

        return dis + ', ' + str(self.tail.data) + ')'


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next
