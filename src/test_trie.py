"""Tests for trie data structure."""

import pytest


@pytest.fixture
def empty_trie():
    """Fixture for empty trie."""
    from trie import Trie
    empty = Trie()
    return empty


@pytest.fixture
def simple_trie():
    """Fixture for simple trie."""
    from trie import Trie
    simple = Trie()
    simple.insert('a')
    return simple


@pytest.fixture
def trie():
    """Fixture for a trie."""
    from trie import Trie

    trie = Trie()
    words = ['into', 'int', 'it', 'tea', 'ted', 'ten', 'to']
    for word in words:
        trie.insert(word)
    return trie


def test_init_creates_empty_trie(empty_trie):
    """Test empty nodes on empty tree."""
    assert empty_trie._nodes == {'': set()}


def test_contains(trie):
    """Test contains method is true for word in tree."""
    assert trie.contains('into')


def test_contains_false(simple_trie):
    """Test contains is false when not in the trie."""
    assert not simple_trie.contains('potato')


def test_contains_string(trie):
    """Test if trie contains a string that isn't a word."""
    assert trie.contains('in')


def test_insert_adds_keys(empty_trie):
    """Test insert on an empty tree adds length."""
    empty_trie.insert('hello')
    assert len(empty_trie._nodes) == 6


def test_insert_adds_keys_add_end(empty_trie):
    """Test insert on an empty tree adds a word ender."""
    empty_trie.insert('hello')
    passed = True
    for val in empty_trie._nodes.values():
        if val == '$':
            passed = False
    assert passed


def test_insert_adds_each_letter(empty_trie):
    """Test insert on an empty tree adds each leter."""
    empty_trie.insert('hi')
    assert 'h' in empty_trie._nodes.keys()
    assert 'hi' in empty_trie._nodes.keys()
