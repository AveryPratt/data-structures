"""Test radix sorting algorithm sorts properly."""


def test_radix_sort_empty():
    """Sort an empty list."""
    from src.radix_sort import radix_sort
    assert radix_sort([]) == []


def test_radix_sort_one_number():
    """Sort a list containing a single number."""
    from src.radix_sort import radix_sort
    assert radix_sort([1]) == [1]


def test_radix_sort_ordered_integers():
    """Sort a list containing ordered integers."""
    from src.radix_sort import radix_sort
    assert radix_sort([1, 2, 3]) == [1, 2, 3]


def test_radix_sort_unordered_integers():
    """Sort a list containing unordered integers."""
    from src.radix_sort import radix_sort
    assert radix_sort([3, 2, 1]) == [1, 2, 3]


def test_radix_sort_duplicate_integers():
    """Sort a list containing unordered integers with duplicates."""
    from src.radix_sort import radix_sort
    assert radix_sort([3, 2, 1, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]


def test_radix_sort_large_integers():
    """Sort a list containing unordered integers greater than 100."""
    from src.radix_sort import radix_sort
    result = [100, 111, 175, 300, 301, 310, 375, 999]
    assert radix_sort([301, 300, 310, 111, 375, 175, 999, 100]) == result


def test_radix_sort_binary_base():
    """Sort a list containing unordered integers with duplicates using base 2."""
    from src.radix_sort import radix_sort
    result = [100, 111, 175, 300, 301, 310, 375, 999]
    assert radix_sort([301, 300, 310, 111, 375, 175, 999, 100], 2) == result


def test_radix_sort_hexadecimal_base():
    """Sort a list containing unordered integers with duplicates using base 16."""
    from src.radix_sort import radix_sort
    result = [100, 111, 175, 300, 301, 310, 375, 999]
    assert radix_sort([301, 300, 310, 111, 375, 175, 999, 100], 16) == result


def test_radix_sort_enourmous_base():
    """Sort a list containing unordered integers with duplicates using base 100."""
    from src.radix_sort import radix_sort
    result = [100, 111, 175, 300, 301, 310, 375, 999]
    assert radix_sort([301, 300, 310, 111, 375, 175, 999, 100], 100) == result


def test_radix_sort_randomized():
    """Sort a giant list of 1000000 random integers between 1 and 1000000 using base 10000"""
    from src.radix_sort import radix_sort
    from random import Random
    rand = Random()
    pile_of_crap = []
    for i in range(10000000):
        pile_of_crap.append(rand.randint(0, 100000))
    radix_sort(pile_of_crap, 10000000)
