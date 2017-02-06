"""Test radix sorting algorithm sorts properly."""


def test_radix_sort_empty():
    """Sort an empty list."""
    from src.radix_sort import radix_sort
    assert radix_sort([]) == []


def test_radix_sort_one_number():
    """Sort a list containing a single number."""
    from src.radix_sort import radix_sort
    assert radix_sort([1]) == [1]


def test_radix_sort_ordered_numbers():
    """Sort a list containing ordered numbers."""
    from src.radix_sort import radix_sort
    assert radix_sort([1, 2, 3]) == [1, 2, 3]


# def test_radix_sort_unordered_numbers():
#     """Sort a list containing unordered numbers."""
#     from src.radix_sort import radix_sort
#     assert radix_sort([3, 2, 1]) == [1, 2, 3]


# def test_radix_sort_duplicate_numbers():
#     """Sort a list containing unordered numbers with duplicates."""
#     from src.radix_sort import radix_sort
#     assert radix_sort([3, 2, 1, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]


# def test_radix_sort_floats():
#     """Sort a list containing unordered numbers with duplicates."""
#     from src.radix_sort import radix_sort
#     assert radix_sort([3.5, 2.75, 0.333, 100.01]) == [0.333, 2.75, 3.5, 100.01]


# def test_radix_sort_one_letter():
#     """Sort a list containing a single letter."""
#     from src.radix_sort import radix_sort
#     assert radix_sort(["a"]) == ["a"]


# def test_radix_sort_ordered_letters():
#     """Sort a list containing ordered letters."""
#     from src.radix_sort import radix_sort
#     assert radix_sort(["a", "b", "c"]) == ["a", "b", "c"]


# def test_radix_sort_unordered_letters():
#     """Sort a list containing unordered letters."""
#     from src.radix_sort import radix_sort
#     assert radix_sort(["c", "b", "a"]) == ["a", "b", "c"]


# def test_radix_sort_duplicate_letters():
#     """Sort a list containing unordered letters with duplicates."""
#     from src.radix_sort import radix_sort
#     assert radix_sort(
#         ["c", "b", "a", "a", "b", "c"]) == ["a", "a", "b", "b", "c", "c"]


# def test_radix_sort_capitalized_letters():
#     """Sort a list containing unordered letters with duplicates."""
#     from src.radix_sort import radix_sort
#     assert radix_sort(
#         ["c", "B", "a", "A", "b", "C"]) == ["A", "B", "C", "a", "b", "c"]
