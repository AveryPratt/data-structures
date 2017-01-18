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
        self.size_number = 0

        if hasattr(itr, "__iter__"):
            for val in itr:
                self.insert(val)
        elif itr:
            self.insert(itr)

    def insert(self, val):
        """Insert a value into the tree."""
        if not self.root:
            self.root = Node(val)
            self.size_number += 1
        else:
            self._sink(val, self.root)

    def remove(self, val):
        """Remove a value and its node from the tree."""
        node = self.search(val)
        next_node = None
        if node.left_child ^ node.right_child:
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
        elif node.left_child and node.right_child:
            next_node = self.in_order_traversal(node)
            next_node.left_child = node.left_child
            next_node.right_child = node.right_child
        if node is self.root:
            self.root = next_node
            return
        elif node is node.parent.left_child:
            node.parent.left_child = next_node
        else:
            node.parent.right_child = next_node
        next_node.parent = node.parent

    def search(self, val):
        """Return the node in the tree with the given value."""
        if not self.root:
            return None
        else:
            return self._find(val, self.root)

    def size(self):
        """Return the number of nodes in the tree."""
        return self.size_number

    def depth(self):
        """Return the length of the longest branch of the tree."""
        if not self.root:
            return None
        else:
            return self.root.balance_number

    def contains(self, val):
        """Return a boolean determining if the value is already in the tree."""
        return False if not self.search(val) else True

    def balance(self):
        """Return the difference in length between the left and right sides...

        ...of the tree. (negative value if left is longer)
        """
        while self.root:
            if not self.root.left_child:
                return self.root.right_child.balance_number - 0
            if not self.root.right_child:
                return 0 - self.root.left_child.balance_number
            return self.root.right_child.balance_number - self.root.left_child.balance_number
        return 0

    def breadth_first_traversal(self):
        """Traverse the list breadth-first and return a list of values."""
        cur_node = self.root
        if cur_node is None:
            return
        q = []
        q.append(cur_node)
        while len(q) > 0:
            cur_node = q.pop(0)
            yield cur_node.data
            if cur_node.left_child:
                q.append(cur_node.left_child)
            if cur_node.right_child:
                q.append(cur_node.right_child)

    def pre_order_traversal(self):
        """Traverse the list depth-first and return a list of values in pre-order (starting at the root)."""
        cur_node = self.root
        if cur_node is None:
            return
        visited = []
        visited.append(cur_node)

        while len(visited) > 0:
            cur_node = visited.pop()
            yield cur_node.data
            if cur_node.right_child:
                visited.append(cur_node.right_child)
            if cur_node.left_child:
                visited.append(cur_node.left_child)

    def in_order_traversal(self, node=None):
        """Traverse the list depth-first and return a list of values in sorted order."""
        if node is None:
            node = self.root
        s = []
        while len(s) > 0 or node:
            if node:
                s.append(node)
                node = node.left_child
            else:
                node = s.pop()
                yield node.data
                node = node.right_child

    def post_order_traversal(self):
        """Traverse the list depth-first and return a list of values in post-order (ending at the root)."""
        cur_node = self.root
        visited = []
        last_node_visited = None
        while len(visited) > 0 or cur_node:
            if cur_node:
                visited.append(cur_node)
                cur_node = cur_node.left_child
            else:
                peek_node = visited[-1]
                if peek_node.right_child and last_node_visited != peek_node.right_child:
                    cur_node = peek_node.right_child
                else:
                    yield peek_node.data
                    last_node_visited = visited.pop()

    def _find(self, val, cur_node):
        """Recursively finds value into the tree."""
        if val == cur_node.data:
            return cur_node
        elif val > cur_node.data:
            if not cur_node.right_child:
                return None
            return self._find(val, cur_node.right_child)
        elif val < cur_node.data:
            if not cur_node.left_child:
                return None
            return self._find(val, cur_node.left_child)

    def _sink(self, val, cur_node):
        """Recursively inserts value into the tree."""
        if val > cur_node.data:
            if not cur_node.right_child:
                cur_node.right_child = Node(val, cur_node)
                self.size_number += 1
                if cur_node.balance_number == 0:
                    cur_node.balance_number = 1
            else:
                count = self._sink(val, cur_node.right_child)
                if cur_node.balance_number <= count:
                    cur_node.balance_number += 1
        elif val < cur_node.data:
            if not cur_node.left_child:
                cur_node.left_child = Node(val, cur_node)
                self.size_number += 1
                if cur_node.balance_number == 0:
                    cur_node.balance_number = 1
            else:
                count = self._sink(val, cur_node.left_child)
                if cur_node.balance_number <= count:
                    cur_node.balance_number += 1
        return cur_node.balance_number
