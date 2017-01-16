"""Test implementation of binary search tree."""

import pytest

@pytest.fixture()
def new_bst():
    """Fixture for a bst."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree([8, 3, 10, 1, 6, 9])
    bst_empty = BinarySearchTree()
    bst_one_node = BinarySearchTree(3)
    return bst


def test_initiate_node_data():
    """Test node data on init."""
    from binary_search_tree import Node
    node = Node(5)
    assert Node.data == n


def test_initiate_node_children():
    """Test node children on init is None."""
    from binary_search_tree import Node
    node = Node(5)
    assert Node.right == None
    assert Node.left == None


def test_initiate_bst():
    """Test if bst is initiated has a root with data."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree(3)
    assert bst.root.data == 3


def test_insert_on_an_empty_bst():
    """Test insert on an empty bst updates the root."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(5)
    assert bst.root.data == 5


