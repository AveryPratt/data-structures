"""Test implementation of binary search tree."""

import pytest


@pytest.fixture()
def new_bst():
    """Fixture for a bst."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree([8, 3, 10, 1, 6, 9])
    bst_empty = BinarySearchTree()
    bst_one_node = BinarySearchTree(3)
    return bst, bst_empty, bst_one_node


def test_initiate_node_data():
    """Test node data on init."""
    from binary_search_tree import Node
    node = Node(5)
    assert node.data == 5


def test_initiate_node_children():
    """Test node children on init is None."""
    from binary_search_tree import Node
    node = Node(5)
    assert node.right_child is None
    assert node.left_child is None


def test_initiate_bst(new_bst):
    """Test if bst is initiated has a root with data."""
    assert new_bst[2].root.data == 3


def test_insert_on_an_empty_bst(new_bst):
    """Test insert on an empty bst updates the root."""
    new_bst[1].insert(5)
    assert new_bst[1].root.data == 5


def test_insert_larger_number_on_a_bst_of_one(new_bst):
    """Test insert on a bst of one is the right."""
    new_bst[2].insert(5)
    assert new_bst[2].root.right_child.data == 5


def test_insert_smaller_number_on_a_bst_of_one(new_bst):
    """Test insert on a bst of one is on the left when val< root."""
    new_bst[2].insert(1)
    assert new_bst[2].root.left_child.data == 1


def test_insert_small_number_on_a_bst(new_bst):
    """Test insert on a bst less than root."""
    new_bst[0].insert(0)
    expected = new_bst[0].root.left_child.left_child.left_child
    assert expected.data == 0


def test_insert_larger_number_on_a_bst(new_bst):
    """Test insert on a bst greater than root."""
    new_bst[0].insert(11)
    expected = new_bst[0].root.right_child.right_child
    assert expected.data == 11


def test_insert_a_number_already_there(new_bst):
    """Test insert does nothing."""
    new_bst[2].insert(3)
    assert new_bst[2].root.data == 3
    assert new_bst[2].root.right_child is None and new_bst[2].root.left_child is None
