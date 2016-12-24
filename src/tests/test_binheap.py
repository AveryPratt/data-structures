"""Tests that binary heap data structure behaves properly."""


import pytest


START = [45, -93, 68, 39, 71, -99, -37, 12, 8, -38, 104, 38, 55, -10, 30, -45, 78, 0, -34, -10]
SORTED = [-99, -45, -93, -38, -10, 38, -37, 12, -34, 8, 104, 68, 55, -10, 30, 45, 78, 39, 0, 71]


@pytest.fixture
def emptybh():
    """Creates an empty BinHeap for testing."""
    from src.binheap import BinHeap
    return BinHeap()


@pytest.fixture
def fullbh():
    """Creates a BinHeap for testing with heap as values."""
    from src.binheap import BinHeap
    return BinHeap(START)


def test_constructor1(emptybh):
    assert emptybh._lst == []


def test_constructor2(fullbh):
    assert fullbh._lst == SORTED


def test_bubble1(emptybh):
    emptybh._bubble(0)
    assert emptybh._lst == []


def test_bubble2(fullbh):
    fullbh._bubble(0)
    assert fullbh._lst == SORTED


def test_bubble3(fullbh):
    fullbh._lst[0] = 100
    fullbh._bubble(0)
    assert fullbh._lst == [-93, -45, -37, -38, -10, 38, -10, 12, -34, 8, 104, 68, 55, 100, 30, 45, 78, 39, 0, 71]


def test_bubble4(fullbh):
    fullbh._lst[0] = -50
    fullbh._bubble(0)
    assert fullbh._lst == [-93, -45, -50, -38, -10, 38, -37, 12, -34, 8, 104, 68, 55, -10, 30, 45, 78, 39, 0, 71]


def test_bubble5(fullbh):
    fullbh._bubble(9)
    assert fullbh._lst == SORTED


def test_bubble6(fullbh):
    fullbh._bubble(10)
    assert fullbh._lst == SORTED


def test_sink1(emptybh):
    emptybh._sink(0)
    assert emptybh._lst == []


def test_sink2(emptybh):
    emptybh._lst.append(1)
    emptybh._sink(0)
    assert emptybh._lst == [1]


def test_sink3(fullbh):
    fullbh._lst.append(-100)
    fullbh._sink(len(fullbh._lst) - 1)
    assert fullbh._lst == [-100, -99, -93, -38, -45, 38, -37, 12, -34, -10, 104, 68, 55, -10, 30, 45, 78, 39, 0, 71, 8]


def test_sink4(fullbh):
    fullbh._lst.append(0)
    fullbh._sink(len(fullbh._lst) - 1)
    assert fullbh._lst == [-99, -45, -93, -38, -10, 38, -37, 12, -34, 0, 104, 68, 55, -10, 30, 45, 78, 39, 0, 71, 8]


def test_sink5(fullbh):
    fullbh._lst[6] = -100
    fullbh._sink(6)
    assert fullbh._lst == [-100, -45, -99, -38, -10, 38, -93, 12, -34, 8, 104, 68, 55, -10, 30, 45, 78, 39, 0, 71]


def test_pop1(emptybh):
    with pytest.raises(IndexError):
        emptybh.pop()


def test_pop2():
    from src.binheap import BinHeap
    bh = BinHeap([5])
    assert bh.pop() == 5


def test_pop3(fullbh):
    assert fullbh.pop() == -99


def test_pop4(fullbh):
    len_heap = len(fullbh._lst)
    fullbh.pop()
    assert len(fullbh._lst) == len_heap - 1


def test_pop5(fullbh):
    sorted_heap = START
    sorted_heap.sort()
    passes = True
    for item in sorted_heap:
        match = fullbh.pop()
        if item != match:
            passes = False
            break
    assert passes


def test_push1(emptybh):
    emptybh.push(5)
    assert len(emptybh._lst) == 1


def test_push2(emptybh):
    emptybh.push(5)
    assert emptybh._lst[0] == 5
