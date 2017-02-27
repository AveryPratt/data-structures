"""Test insertion sorting algorithm sorts properly."""


def test_insertion_sort_empty():
    """Sort an empty list."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort([]) == []


def test_insertion_sort_one_number():
    """Sort a list containing a single number."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort([1]) == [1]


def test_insertion_sort_ordered_numbers():
    """Sort a list containing ordered numbers."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]


def test_insertion_sort_unordered_numbers():
    """Sort a list containing unordered numbers."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]


def test_insertion_sort_duplicate_numbers():
    """Sort a list containing unordered numbers with duplicates."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort([3, 2, 1, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]


def test_insertion_sort_one_letter():
    """Sort a list containing a single letter."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort(["a"]) == ["a"]


def test_insertion_sort_ordered_letters():
    """Sort a list containing ordered letters."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort(["a", "b", "c"]) == ["a", "b", "c"]


def test_insertion_sort_unordered_letters():
    """Sort a list containing unordered letters."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort(["c", "b", "a"]) == ["a", "b", "c"]


def test_insertion_sort_duplicate_letters():
    """Sort a list containing unordered letters with duplicates."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort(
        ["c", "b", "a", "a", "b", "c"]) == ["a", "a", "b", "b", "c", "c"]


def test_insertion_sort_capitalized_letters():
    """Sort a list containing unordered letters with duplicates."""
    from src.insertion_sort import insertion_sort
    assert insertion_sort(
        ["c", "B", "a", "A", "b", "C"]) == ["A", "B", "C", "a", "b", "c"]
