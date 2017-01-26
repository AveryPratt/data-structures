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
    assert not trie.contains('in')


def test_insert_adds_keys(empty_trie):
    """Test insert on an empty tree adds length."""
    empty_trie.insert('hello')
    assert len(empty_trie._nodes) == 6


def test_insert_adds_keys_add_end(empty_trie):
    """Test insert on an empty tree adds a word ender."""
    empty_trie.insert('hello')
    assert set(['$']) in empty_trie._nodes.values()


def test_insert_adds_each_letter(empty_trie):
    """Test insert on an empty tree adds each leter."""
    empty_trie.insert('hi')
    assert 'h' in empty_trie._nodes.keys()
    assert 'hi' in empty_trie._nodes.keys()


def test_insert_non_string_raises_error(empty_trie):
    """Test insert a list object on an empty tree raises type error."""
    with pytest.raises(TypeError):
        empty_trie.insert(False)


def test_insert_none_raises_error(empty_trie):
    """Test insert a list object on an empty tree raises type error."""
    with pytest.raises(TypeError):
        empty_trie.insert(None)


def test_insert_iterable_raises_error(empty_trie):
    """Test insert a list object on an empty tree raises type error."""
    with pytest.raises(TypeError):
        empty_trie.insert([1, 2, 3])


def test_size_of_trie(trie):
    """Test size of trie."""
    assert trie.size() == 7


def test_size_of_simple_trie(simple_trie):
    """Test size of trie."""
    assert simple_trie.size() == 1


def test_size_of_empty_trie(empty_trie):
    """Test size of trie."""
    assert empty_trie.size() == 0


def test_remove_of_trie(trie):
    """Test remove word from trie."""
    trie.remove('to')
    assert not trie.contains('to')


def test_remove_of_trie_non_word(trie):
    """Test remove trie for not a word."""
    trie.remove('in')
    assert not trie.contains('in')


def test_remove_word_keeps_longer_word(trie):
    """Test remove trie for a short word that is contained in others."""
    trie.remove('int')
    assert trie.contains('into')


def test_size_decrease_with_remove(trie):
    """Test remove trie decreases size."""
    size = trie.size()
    trie.remove('int')
    assert trie.size() == size - 1


def test_size_increases_with_insert(trie):
    """Test insert trie increases size."""
    size = trie.size()
    trie.insert('tear')
    assert trie.size() == size + 1


def test_remove_word_that_doesnt_exist(trie):
    """Test remove a node that doesn't exist is key error."""
    with pytest.raises(KeyError):
        trie.remove('tear')


def test_insert_not_a_string_is_an_error(trie):
    """Test error is triggered if try to insert a non str."""
    with pytest.raises(TypeError):
        trie.insert(1)
