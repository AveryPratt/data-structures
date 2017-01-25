"""Tests hash table."""

import pytest
from src.hash_table import HashTable


@pytest.fixture
def hash_table():
    """A hash table using addative."""
    hash_table = HashTable(10)
    return hash_table


@pytest.fixture
def hash_xor():
    """A hash table using xor."""
    hash_table = HashTable(10, 'xor')
    return hash_table


def test_create_hash_table_on_a_non_str_errors(hash_table):
    """Test that set a value on not str raises an error."""
    with pytest.raises(TypeError):
        hash_table.set(1, 'value')


def test_hash_table_init():
    """Test that hash table is initialized with correct number of buckets."""
    my_table = HashTable(10)
    assert len(my_table.buckets) == 10


def test_hash_table_additive():
    """Test hash table using additive method."""
    my_table = HashTable(100)
    assert my_table._hash("hello") == 32


def test_hash_table_set(hash_table):
    """Test hash table set using addative method."""
    hash_table.set("hello", "value")
    assert hash_table.buckets[2] == [("hello", "value")]


def test_hash_table_get(hash_table):
    """Test hash table get using addative method."""
    hash_table.set("hello", "value")
    assert hash_table.get("hello") == "value"


def test_hash_table_xor_set(hash_xor):
    """Test hash table set using xor method."""
    hash_xor.set("hello", "value")
    print(hash_xor.buckets)
    assert hash_xor.buckets[8] == [("hello", "value")]


def test_hash_table_xor_get(hash_xor):
    """Test hash table get using xor method."""
    hash_xor.set("hello", "value")
    assert hash_xor.get("hello") == "value"


def test_hash_table_xor_get_set(hash_xor):
    """Test hash table with xor method."""
    hash_xor.set("hello", "value")
    assert hash_xor.get("hello") == "value"


def test_set_key_twice_updates_val(hash_table):
    """Test that setting the same key twice updates the value."""
    hash_table.set('hello', 'value')
    hash_table.set('hello', 'value2')
    assert hash_table.get('hello') == 'value2'


def test_set_key_twice_updates_val_xor(hash_xor):
    """Test that setting the same key twice updates the value."""
    hash_xor.set('hello', 'value')
    hash_xor.set('hello', 'value2')
    assert hash_xor.get('hello') == 'value2'


def test_set_key_twice_increases_len(hash_table):
    """Test setting key to the same bucket adds length."""
    hash_table.set('a', 'value')
    hash_table.set('k', 'value2')

    assert len(hash_table.buckets[7]) == 2
