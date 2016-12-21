"""Tests that binary heap data structure behaves properly."""


import pytest


LST = [45, -93, 68, 39, 71, -99, -37, 12, 8, -38, 104, 38, 55, -10, 30, -45, 78, 0, -34, -10]
SORTED = []


@pytest.fixture
def emptybh():
    """Creates an empty Deque for testing."""
    from src.binheap import BinHeap
    return BinHeap()


@pytest.fixture
def fullbh():
    """Creates an empty Deque for testing."""
    from src.binheap import BinHeap
    return BinHeap(LST)


def test_constructor1(emptybh):
    assert emptybh.lst == []


def test_constructor2(fullbh):
    assert fullbh == LST


def test_sortheap1(emptybh):
    emptybh._sortheap()
    assert emptybh.lst == []


def test_sortheap2(fullbh):
    fullbh._sortheap()
    assert fullbh.lst == LST


def test_push():
    pass

def test_pop():
    pass
