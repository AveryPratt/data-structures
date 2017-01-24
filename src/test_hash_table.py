"""Tests hash table."""

import pytest
from src.hash_table import HashTable


def test_hash_table_init():
    """Test that hash table is initialized with the correct number of buckets."""
    my_table = HashTable(10)
    assert len(my_table.buckets) == 10


def test_hash_table_additive():
    """Test hash table using additive method."""
    my_table = HashTable(100)
    assert my_table._hash("hello") == 32


def test_hash_table_set():
    """Test hash table set using addative method."""
    my_table = HashTable(10)
    my_table.set("hello", "value")
    assert my_table.buckets[2] == ["value"]


def test_hash_table_get():
    """Test hash table get using addative method."""
    my_table = HashTable(10)
    my_table.set("hello", "value")
    assert my_table.get("hello") == ["value"]


def test_hash_table_xor():
    """Test hash table with xor method."""
    my_table = HashTable(10, "xor")
    my_table.set("hello", "value")
    assert my_table.get("hello") == ["value"]
