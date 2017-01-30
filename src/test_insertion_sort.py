"""Test insertion sorting algorithm sorts properly."""


import pytest


def test_insertion_sort_empty():
    """Sort an empty list."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort([]) == []
