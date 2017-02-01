"""Test quick sorting algorithm sorts properly."""


def test_quick_sort_empty():
    """Sort an empty list."""
    from src.quick_sort import quick_sort
    assert quick_sort([]) == []


def test_quick_sort_one_number():
    """Sort a list containing a single number."""
    from src.quick_sort import quick_sort
    assert quick_sort([1]) == [1]


def test_quick_sort_ordered_numbers():
    """Sort a list containing ordered numbers."""
    from src.quick_sort import quick_sort
    assert quick_sort([1, 2, 3]) == [1, 2, 3]


def test_quick_sort_unordered_numbers():
    """Sort a list containing unordered numbers."""
    from src.quick_sort import quick_sort
    assert quick_sort([3, 2, 1]) == [1, 2, 3]


def test_quick_sort_duplicate_numbers():
    """Sort a list containing unordered numbers with duplicates."""
    from src.quick_sort import quick_sort
    assert quick_sort([3, 2, 1, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]


def test_quick_sort_one_letter():
    """Sort a list containing a single letter."""
    from src.quick_sort import quick_sort
    assert quick_sort(["a"]) == ["a"]


def test_quick_sort_ordered_letters():
    """Sort a list containing ordered letters."""
    from src.quick_sort import quick_sort
    assert quick_sort(["a", "b", "c"]) == ["a", "b", "c"]


def test_quick_sort_unordered_letters():
    """Sort a list containing unordered letters."""
    from src.quick_sort import quick_sort
    assert quick_sort(["c", "b", "a"]) == ["a", "b", "c"]


def test_quick_sort_duplicate_letters():
    """Sort a list containing unordered letters with duplicates."""
    from src.quick_sort import quick_sort
    assert quick_sort(
        ["c", "b", "a", "a", "b", "c"]) == ["a", "a", "b", "b", "c", "c"]


def test_quick_sort_capitalized_letters():
    """Sort a list containing unordered letters with duplicates."""
    from src.quick_sort import quick_sort
    assert quick_sort(
        ["c", "B", "a", "A", "b", "C"]) == ["A", "B", "C", "a", "b", "c"]
