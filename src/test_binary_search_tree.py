"""Test implementation of binary search tree."""

import pytest


@pytest.fixture()
def new_bst():
    """Fixture for a bst."""
    from binary_search_tree import BinarySearchTree
    bst = BinarySearchTree([8, 3, 10, 1, 6, 9])
    bst_empty = BinarySearchTree()
    bst_one_node = BinarySearchTree(3)
    bst_ordered = BinarySearchTree([1, 2, 3, 4, 5])
    bst_reversed = BinarySearchTree([5, 4, 3, 2, 1])
    return bst, bst_empty, bst_one_node, bst_ordered, bst_reversed


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


def test_search_empty(new_bst):
    """Test searching an empty tree returns None."""
    assert new_bst[1].search(5) is None


def test_search_root_found(new_bst):
    """Test searching for the root value in tree returns the root."""
    assert new_bst[0].search(8) is new_bst[0].root


def test_search_child_found(new_bst):
    """Test searching for a value in tree returns correct node."""
    assert new_bst[0].search(6) is new_bst[0].root.left_child.right_child


def test_search_not_found(new_bst):
    """Test searching for a value that doesn't exist returns None."""
    assert new_bst[0].search(100) is None


def test_size_of_bst(new_bst):
    """Test size of a bst."""
    assert new_bst[0].size() == 6


def test_size_of_empty_bst(new_bst):
    """Test size of an empty bst."""
    assert new_bst[1].size() == 0


def test_size_of_bst_of_one(new_bst):
    """Test size of a bst of one."""
    assert new_bst[2].size() == 1


def test_size_is_increased_when_I_insert(new_bst):
    """Test size of bst increases when insert."""
    old_size = new_bst[0].size()
    new_bst[0].insert(0)
    assert old_size + 1 == new_bst[0].size()


def test_depth_empty(new_bst):
    """Test depth of empty tree is None."""
    assert new_bst[1].depth() is None


def test_depth_root(new_bst):
    """Test depth of tree with only the root node is 0."""
    assert new_bst[2].depth() == 0


def test_depth_balanced(new_bst):
    """Test depth of balanced tree is accurate."""
    assert new_bst[0].depth() == 2


def test_depth_unbalanced(new_bst):
    """Test depth of unbalanced tree is accurate."""
    assert new_bst[3].depth() == 4


def test_depth_after_add_repeat(new_bst):
    """Test that adding a repeat value doesn't mess up the depth."""
    new_bst[0].insert(6)
    assert new_bst[0].depth() == 2


def test_contains_is_true(new_bst):
    """Test that contains is true for value in tree."""
    assert new_bst[2].contains(3)


def test_contains_is_false(new_bst):
    """Test that contains is false for value not in tree."""
    assert not new_bst[2].contains(5)


def test_contains_is_false_on_empty(new_bst):
    """Test that contains is false for empty tree."""
    assert not new_bst[1].contains(5)


def test_contains_root_node(new_bst):
    """Test contains returns true if root node is val."""
    assert new_bst[0].contains(8)


def test_balance_on_balanced_tree(new_bst):
    """Test balance returns 0 for balanced."""
    assert new_bst[0].balance() == 0


def test_balance_on_unbalanced_tree(new_bst):
    """Test balance returns negative for left."""
    assert new_bst[3].balance() == 3


def test_balance_on_empty(new_bst):
    """Test when root is none, balace is 0."""
    assert new_bst[1].balance() == 0


def test_preorder_traversal(new_bst):
    """Test preorder traversal."""
    result = [x for x in new_bst[0].pre_order_traversal()]

    assert [8, 3, 1, 6, 10, 9] == result


def test_preorder_traversal_empty(new_bst):
    """Test preorder traversal on empty list."""
    result = [x for x in new_bst[1].pre_order_traversal()]

    assert [] == result


def test_preorder_traversal_one_node(new_bst):
    """Test preorder traversal on a list with one node."""
    result = [x for x in new_bst[2].pre_order_traversal()]

    assert [3] == result


def test_preorder_traversal_unbalanced_right(new_bst):
    """Test preorder traversal on a list with a right side larger than the left."""
    result = [x for x in new_bst[3].pre_order_traversal()]

    assert [1, 2, 3, 4, 5] == result


def test_preorder_traversal_unbalanced_left(new_bst):
    """Test preorder traversal on a list with a left side larger than the right."""
    result = [x for x in new_bst[4].pre_order_traversal()]

    assert [5, 4, 3, 2, 1] == result


def test_post_traversal(new_bst):
    """Test post_order traversal."""
    result = [x for x in new_bst[0].post_order_traversal()]
    assert [1, 6, 3, 9, 10, 8] == result


def test_post_traversal_empty(new_bst):
    """Test postorder traversal on empty list."""
    result = [x for x in new_bst[1].post_order_traversal()]
    assert [] == result


def test_post_traversal_one_node(new_bst):
    """Test postorder traversal on a list with one node."""
    result = [x for x in new_bst[2].post_order_traversal()]
    assert [3] == result


def test_post_traversal_unbalanced_right(new_bst):
    """Test postorder traversal on a list with a right side larger than the left."""
    result = [x for x in new_bst[3].post_order_traversal()]
    assert [5, 4, 3, 2, 1] == result


def test_post_traversal_unbalanced_left(new_bst):
    """Test postorder traversal on a list with a left side larger than the right."""
    result = [x for x in new_bst[4].post_order_traversal()]
    assert [1, 2, 3, 4, 5] == result


def test_inorder_traversal(new_bst):
    """Test inorder traversal."""
    result = [x for x in new_bst[0].in_order_traversal()]
    assert [1, 3, 6, 8, 9, 10] == result


def test_inorder_traversal_empty(new_bst):
    """Test inorder traversal on empty list."""
    result = [x for x in new_bst[1].in_order_traversal()]
    assert result == []


def test_inorder_traversal_one_node(new_bst):
    """Test inorder traversal on a list with one node."""
    result = [x for x in new_bst[2].in_order_traversal()]
    assert result == [3]


def test_inorder_traversal_unbalanced_right(new_bst):
    """Test inorder traversal on a list with a right side larger than the left."""
    result = [x for x in new_bst[3].in_order_traversal()]
    assert result == [1, 2, 3, 4, 5]


def test_inorder_traversal_unbalanced_left(new_bst):
    """Test inorder traversal on a list with a left side larger than the right."""
    result = [x for x in new_bst[4].in_order_traversal()]
    assert result == [1, 2, 3, 4, 5]


def test_breadth_first_traversal(new_bst):
    """Test breadth-first traversal."""
    result = [x for x in new_bst[0].breadth_first_traversal()]

    assert result == [8, 3, 10, 1, 6, 9]


def test_breadth_first_traversal_empty(new_bst):
    """Test breadth-first traversal on empty list."""
    result = [x for x in new_bst[1].breadth_first_traversal()]

    assert result == []


def test_breadth_first_traversal_one_node(new_bst):
    """Test breadth-first traversal on a list with one node."""
    result = [x for x in new_bst[2].breadth_first_traversal()]

    assert result == [3]


def test_breadth_first_traversal_unbalanced_right(new_bst):
    """Test breadth-first traversal on a list with a right side larger than the left."""
    result = [x for x in new_bst[3].breadth_first_traversal()]

    assert result == [1, 2, 3, 4, 5]


def test_breadth_first_traversal_unbalanced_left(new_bst):
    """Test breadth-first traversal on a list with a left side larger than the right."""
    result = [x for x in new_bst[4].breadth_first_traversal()]

    assert result == [5, 4, 3, 2, 1]


