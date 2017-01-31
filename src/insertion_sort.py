"""Implementation of Insertion Sort."""


def insertion_sort(input):
    """sorts input using insertion sorting algorithm."""
    for idx in range(len(input)):
        while idx > 0 and input[idx] < input[idx - 1]:
            input[idx], input[idx - 1] = input[idx - 1], input[idx]
            idx -= 1
    return input


if __name__ == "__main__":
    from timeit import Timer
    stuff = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
    timer = Timer(stmt="insertion_sort(stuff)")
    print(timer.timeit(1000))
