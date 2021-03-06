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
        # check parent from node, until unbalanced.

    def remove(self, val):
        """Remove a value and its node from the tree."""
        node = self.search(val)
        if not node:
            return
        if node.left and not node.right:
            self._remove_parent(node.left)
            self.size_number -= 1
            return
        elif node.right and not node.left:
            self._remove_parent(node.right)
            self.size_number -= 1
            return
        nxt = None
        nxt = self._nxt_inorder(nxt, node, val)
        if nxt is None:
            try:
                self._redirect(node, None)
            except AttributeError:
                self.root = None
            self.size_number -= 1
            return
        self.remove(nxt.data)
        self._replace_node(nxt, node)

        #  check balance on parent of the node we just removed

    def _rebalance(self, val=None):
        """Re-balance tree after node insertion or deletion."""
        node = self.search(val)
        if node is None:
            node = self.root
            if self.root is None:
                return
        try:
            self._rebalance(node.left.data)
        except AttributeError:
            pass
        try:
            self._rebalance(node.right.data)
        except AttributeError:
            pass
        if self.balance(node) > 1:
            if self.balance(node.right) == -1: # should this be > 0?
                self.rotate(node.right.left.data)
            self.rotate(node.right.data)
        elif self.balance(node) < -1:
            if self.balance(node.left) == 1:
                self.rotate(node.left.right.data)
            self.rotate(node.left.data)
        # result = [x for x in self.breadth_first_traversal()]
        # for num in result:
        #     print(num)
        # print()
        # print()

    def _replace_node(self, nxt, node):
        """Helper to replace the connections to node to nxt."""
        nxt.left = node.left
        nxt.right = node.right
        nxt.parent = node.parent
        if node is self.root:
            self.root = nxt
        if nxt.left:
            nxt.left.parent = nxt
        if nxt.right:
            nxt.right.parent = nxt
        if nxt.parent:
            if nxt.parent.right is node:
                nxt.parent.right = nxt
            else:
                nxt.parent.left = nxt

    def _nxt_inorder(self, nxt, node, val):
        """Get the next node in the inorder traversal."""
        if node.left and node.right:
            gen = self.in_order_traversal()
            path = None
            while path is not val:
                path = next(gen)
            nxt = self.search(next(gen))
        return nxt

    def _remove_parent(self, child):
        """Remove parent node."""
        try:
            self._redirect(child.parent, child)
            child.parent = child.parent.parent
        except AttributeError:
            self.root = child
        return

    def _redirect(self, node1, node2):
        """Redirect from node1 to node2."""
        if node1.parent.right is node1:
            node1.parent.right = node2
        else:
            node1.parent.left = node2

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

    def balance(self, node=None):
        """Return the difference in length between the left and right sides...

        ...of the tree. (negative value if left is longer)
        """
        if node is None:
            node = self.root
            if self.root is None:
                return 0
        if not node.left and not node.right:
            return 0
        elif not node.left:
            return node.right.balance_number
        elif not node.right:
            return -node.left.balance_number
        return node.right.balance_number - node.left.balance_number

    def rotate(self, val):
        """Replace node's parent with node...

        ...and rebalances the children of both.
        """
        node = self.search(val)
        n_par = node.parent
        if n_par:
            is_left = n_par.right == node
        else:
            raise ValueError("Cannot rotate the root node of the tree.")
        child = node.left if is_left else node.right
        self._remove_parent(node)
        if child:
            self._redirect(child, n_par)
        elif is_left:
            node.left = n_par
        else:
            node.right = n_par
        node.parent = n_par.parent
        n_par.parent = node
        if is_left:
            n_par.right = child
        else:
            n_par.left = child
        curr = n_par

        while curr:
            if curr.left:
                left_number = curr.left.balance_number
            else:
                left_number = 0
            if curr.right:
                right_number = curr.right.balance_number
            else:
                right_number = 0
            max_balance_number = max(
                left_number,
                right_number,
            )
            if curr.left or curr.right:
                curr.balance_number = max_balance_number + 1
            else:
                curr.balance_number = 0
            curr = curr.parent

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
        """Traverse the list depth-first...

        ... and return a list of values in pre-order (starting at the root).
        """
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
        """Traverse the list depth-first...

        ...and return a list of values in sorted order.
        """
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
        """Traverse the list depth-first...

        ...and return a list of values in post-order (ending at the root).
        """
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


if __name__ == '__main__':
    bst = BinarySearchTree([8, 3, 10, 1, 6, 9])
    print(bst.balance())
    print(bst.root.right.left.balance_number)
    for x in [12, 13, 14, 9.5, 15, 16, 17]:
        bst.insert(x)
    print(bst.balance())
    print(bst.root.right.left.balance_number)
    bst2 = BinarySearchTree(1)
    print(bst2.balance())
