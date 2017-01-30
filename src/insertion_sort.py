"""Implementation of Insertion Sort."""


def insertion_sort(input):
    """sorts input using insertion sorting algorithm."""
    for idx in range(len(input)):
        while idx > 0 and input[idx] < input[idx - 1]:
            input[idx], input[idx - 1] = input[idx - 1], input[idx]
            idx -= 1
    return input
