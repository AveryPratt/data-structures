"""Implementation of a binary search tree."""


class Node(object):
    """."""

    def __init__(self, data, parent=None, left=None, right=None):
        """."""
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
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
        if self.size() == 1 and self.root.data is val:
            self.root = None
            self.size_number -= 1
            return
        node = self.search(val)
        if node.left and not node.right:
            try:
                node.left.parent = node.parent
            except AttributeError:
                pass
            try:
                if node.parent.left is node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            except AttributeError:
                self.root = node.left
            self.size_number -= 1
            return

        elif node.right and not node.left:
            try:
                node.right.parent = node.parent
            except AttributeError:
                pass
            try:
                if node.parent.right is node:
                    node.parent.right = node.right
                else:
                    node.parent.left = node.right
            except AttributeError:
                self.root = node.right
            self.size_number -= 1
            return

        nxt = None
        if node.left and node.right:
            gen = self.in_order_traversal()
            path = None
            while path is not val:
                path = next(gen)
            nxt = self.search(next(gen))
        if nxt is None:
            try:
                if node.parent.right is node:
                    node.parent.right = None
                else:
                    node.parent.left = None
            except AttributeError:
                pass
            self.size_number -= 1
            return

        self.remove(nxt.data)  # 9
        nxt.left = node.left
        nxt.right = node.right
        nxt.parent = node.parent
        if node is self.root:
            self.root = nxt
        try:
            nxt.left.parent = nxt
        except AttributeError:
            pass
        try:
            nxt.right.parent = nxt
        except AttributeError:
            pass

        try:
            if nxt.parent.right is node:
                nxt.parent.right = nxt
            else:
                nxt.parent.left = nxt
        except AttributeError:
            pass

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
            if not self.root.left:
                return self.root.right.balance_number - 0
            if not self.root.right:
                return 0 - self.root.left.balance_number
            return self.root.right.balance_number - self.root.left.balance_number
        return 0

    def breadth_first_traversal(self, cur_node=None):
        """Traverse the list breadth-first and return a list of values."""
        if cur_node is None:
            cur_node = self.root
        if cur_node is None:
            return
        q = []
        q.append(cur_node)
        while len(q) > 0:
            cur_node = q.pop(0)
            yield cur_node.data
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

    def pre_order_traversal(self, cur_node=None):
        """Traverse the list depth-first and return a list of values in pre-order (starting at the root)."""
        if cur_node is None:
            cur_node = self.root
        if cur_node is None:
            return
        visited = []
        visited.append(cur_node)

        while len(visited) > 0:
            cur_node = visited.pop()
            yield cur_node.data
            if cur_node.right:
                visited.append(cur_node.right)
            if cur_node.left:
                visited.append(cur_node.left)

    def in_order_traversal(self, node=None):
        """Traverse the list depth-first and return a list of values in sorted order."""
        if node is None:
            node = self.root
        s = []
        while len(s) > 0 or node:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                yield node.data
                node = node.right

    def post_order_traversal(self, cur_node=None):
        """Traverse the list depth-first and return a list of values in post-order (ending at the root)."""
        if cur_node is None:
            cur_node = self.root
        visited = []
        last_node_visited = None
        while len(visited) > 0 or cur_node:
            if cur_node:
                visited.append(cur_node)
                cur_node = cur_node.left
            else:
                peek_node = visited[-1]
                if peek_node.right and last_node_visited != peek_node.right:
                    cur_node = peek_node.right
                else:
                    yield peek_node.data
                    last_node_visited = visited.pop()

    def _find(self, val, cur_node):
        """Recursively finds value into the tree."""
        if val == cur_node.data:
            return cur_node
        elif val > cur_node.data:
            if not cur_node.right:
                return None
            return self._find(val, cur_node.right)
        elif val < cur_node.data:
            if not cur_node.left:
                return None
            return self._find(val, cur_node.left)

    def _sink(self, val, cur_node):
        """Recursively inserts value into the tree."""
        if val > cur_node.data:
            if not cur_node.right:
                cur_node.right = Node(val, cur_node)
                self.size_number += 1
                if cur_node.balance_number == 0:
                    cur_node.balance_number = 1
            else:
                count = self._sink(val, cur_node.right)
                if cur_node.balance_number <= count:
                    cur_node.balance_number += 1
        elif val < cur_node.data:
            if not cur_node.left:
                cur_node.left = Node(val, cur_node)
                self.size_number += 1
                if cur_node.balance_number == 0:
                    cur_node.balance_number = 1
            else:
                count = self._sink(val, cur_node.left)
                if cur_node.balance_number <= count:
                    cur_node.balance_number += 1
        return cur_node.balance_number
