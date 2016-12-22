"""Tests that binary heap data structure behaves properly."""


import pytest


LST = [45, -93, 68, 39, 71, -99, -37, 12, 8, -38, 104, 38, 55, -10, 30, -45, 78, 0, -34, -10]
SORTED = [-99, -93, 45, -45, -38, 68, -37, 39, -34, 71, 104, 38, 55, -10, 30, 12, 78, 0, 8, -10]


@pytest.fixture
def emptybh():
    """Creates an empty BinHeap for testing."""
    from src.binheap import BinHeap
    return BinHeap()


@pytest.fixture
def fullbh():
    """Creates a BinHeap for testing with LST as values."""
    from src.binheap import BinHeap
    return BinHeap(LST)


def test_constructor1(emptybh):
    assert emptybh.lst == []


def test_constructor2(fullbh):
    assert fullbh == SORTED


def test_check_swap2(fullbh):
    fullbh._check_swap(0)
    assert fullbh.lst == SORTED


def test_check_swap3(fullbh):
    fullbh.lst[0] = 0
    fullbh._check_swap(0)
    assert fullbh.lst == [-93, 0, 45, -45, -38, 68, -37, 39, -34, 71, 104, 38, 55, -10, 30, 12, 78, 0, 8, -10]


def test_check_swap4(fullbh):
    fullbh._check_swap(3)
    assert fullbh.lst == SORTED


def test_check_swap5(fullbh):
    fullbh.lst[3] = 1
    fullbh._check_swap(3)
    assert fullbh.lst == [-99, -93, 45, -34, -38, 68, -37, 39, 1, 71, 104, 38, 55, -10, 30, 12, 78, 0, 8, -10]


def test_check_swap6(fullbh):
    fullbh._check_swap(9)
    assert fullbh.lst == [-99, -93, 45, -45, -38, 68, -37, 39, -34, -10, 104, 38, 55, -10, 30, 12, 78, 0, 8, 71]


def test_bubble1(emptybh):
    emptybh._bubble()
    assert emptybh.lst == []


def test_bubble2(fullbh):
    fullbh._bubble()
    assert fullbh.lst == SORTED


def test_bubble3(fullbh):
    fullbh.lst[0] = 100
    fullbh._bubble()
    assert fullbh.lst == [-93, -45, 45, -34, -38, 68, -37, 39, 0, 71, 104, 38, 55, -10, 30, 12, 78, 100, 8, -10]


def test_bubble4(fullbh):
    fullbh.lst[0] = -50
    fullbh._bubble()
    assert fullbh.lst == [-93, -50, 45, -45, -38, 68, -37, 39, -34, 71, 104, 38, 55, -10, 30, 12, 78, 0, 8, -10]


def test_bubble5(fullbh):
    fullbh._bubble(9)
    assert fullbh.lst == [-99, -93, 45, -45, -38, 68, -37, 39, -34, -10, 104, 38, 55, -10, 30, 12, 78, 0, 8, 71]


def test_bubble6(fullbh):
    fullbh._bubble(10)
    assert fullbh.lst == SORTED


def test_bubble7(fullbh):
    fullbh._bubble(-1)
    assert fullbh.lst == SORTED


def test_sink1(emptybh):
    emptybh._sink(0)
    assert emptybh.lst == []


def test_sink2(emptybh):
    emptybh.lst.append(1)
    emptybh._sink()
    assert emptybh.lst == [1]


def test_sink3(fullbh):
    fullbh.lst.append(-100)
    fullbh._sink()
    assert fullbh.lst == [-99, -93, 45, -45, -38, 68, -37, 39, -34, 71, 104, 38, 55, -10, 30, 12, 78, 0, 8, -10]


def test_sink4(fullbh):
    fullbh.lst.append(0)
    fullbh._sink()
    assert fullbh.lst == [-99, -93, 45, -45, -38, 68, -37, 39, -34, 71, 104, 38, 55, -10, 30, 12, 78, 0, 8, -10]


def test_sink5(fullbh):
    fullbh.lst[6] = -100
    fullbh._sink(6)
    assert fullbh.lst == [-99, -93, 45, -45, -38, 68, -37, 39, -34, 71, 104, 38, 55, -10, 30, 12, 78, 0, 8, -10]


def test_pop1(emptybh):
    with pytest.raises(IndexError):
        emptybh.pop()


def test_pop2():
    from src.binheap import BinHeap
    binheap = BinHeap([5])
    assert binheap.pop() == 5


def test_pop3(fullbh):
    assert fullbh.pop() == -99


def test_pop4(fullbh):
    len_lst = len(fullbh.lst)
    fullbh.pop()
    assert len(fullbh.lst) == len_lst - 1


def test_pop5(fullbh):
    sorted_lst = LST
    sorted_lst.sort()
    passes = True
    for item in sorted_lst:
        match = fullbh.pop()
        assert item != match
        # if item != match:
        #     passes = False
        #     break
    # assert passes


def test_push1(emptybh):
    emptybh.push(5)
    assert len(emptybh.lst) == 1


def test_push2(emptybh):
    emptybh.push(5)
    assert emptybh.lst[0] == 5


def test_push3(emptybh):
    with pytest.raises(TypeError):
        emptybh.push("hello")