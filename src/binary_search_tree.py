"""Implementation of a binary search tree."""


class Node(object):
    """."""

    def __init__(self, data, parent=None, left_child=None, right_child=None):
        """."""
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.balance_number = 0


class BinarySearchTree(object):
    """A structure that facilitates fast look-up of a group of organized data.

    insert(self, val): Inserts a value into the tree.

    search(self, val): Returns the node in the tree with the given value.

    size(self): Returns the number of nodes in the tree.

    depth(self): Returns the length of the longest branch of the tree.

    contains(self, val): Determines whether val is contained within the tree.

    balance(self): Returns the difference in length between the left and right
    sides of the tree. (negative value if left is longer).
    """

    def __init__(self, itr=None):
        """Create an instance of a BinarySearchTree."""
        self.root = None
        self.size = 0

        if hasattr(itr, "__iter__"):
            for val in itr:
                self.insert(val)
        elif itr:
            self.insert(itr)

    def insert(self, val):
        """Insert a value into the tree."""
        if not self.root:
            self.root = Node(val)
        else:
            self._sink(val, self.root)

    def search(self, val):
        """Return the node in the tree with the given value."""
        if not self.root:
            return None
        else:
            return self._find(val, self.root)

    def size(self):
        """Return the number of nodes in the tree."""
        return self.size

    def depth(self):
        """Return the length of the longest branch of the tree."""
        return self.root.balance_number

    def contains(self, val):
        """Return a boolean determining if the value is already in the tree."""
        return False if not self.search(val) else True

    def balance(self):
        """Return the difference in length between the left and right sides...

        ...of the tree. (negative value if left is longer)
        """
        return self.root.left_child.balance_number - self.root.right_child.balance_number

    def _find(self, val, cur_node):
        """Recursively inserts value into the tree."""
        if val == cur_node.data:
            return cur_node
        elif val > cur_node.data:
            if not cur_node.right_child:
                return None
            else:
                self._find(val, cur_node.right_child)
        elif val < cur_node.data:
            if not cur_node.left_child:
                return None
            else:
                self._find(val, cur_node.left_child)

    def _sink(self, val, cur_node):
        """Recursively inserts value into the tree."""
        if val > cur_node.data:
            if not cur_node.right_child:
                cur_node.right_child = Node(val, cur_node)
                self.size += 1
                if cur_node.balance_number == 0:
                    cur_node.balance_number = 1
            else:
                count = self._sink(val, cur_node.right_child)
                if cur_node.balance_number <= count:
                    cur_node.balance_number += 1
        elif val < cur_node.data:
            if not cur_node.left_child:
                cur_node.left_child = Node(val, cur_node)
                self.size += 1
                if cur_node.balance_number == 0:
                    cur_node.balance_number = 1
            else:
                count = self._sink(val, cur_node.left_child)
                if cur_node.balance_number <= count:
                    cur_node.balance_number += 1
        return cur_node.balance_number
