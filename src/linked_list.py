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
        if not self.head:
            return None
        val = self.head.data
        if self.head.next == None:
            self.tail = None
        self.head = self.head.next
        return val

    def size(self):
        count = 0
        if self.head:
            count = 1
            cur = self.head
            while cur.next:
                count +=1
                cur = cur.next
            return count
        return 0


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
            curr = self.head
            try:
                while curr.next is not node:
                    curr = curr.next
                if node is self.tail:
                    self.tail = curr
                    curr.next = None
                else:
                    curr.next = node.next
            except AttributeError:
                raise AttributeError("Node does not exist on the list.")


    def display(self):
        if self.head is None:
            return '()'
        elif not self.head.next:
            # import pdb; pdb.set_trace()
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
