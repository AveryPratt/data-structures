"""Implementation of Insertion Sort."""


def insertion_sort(itr):
    """sorts itr using insertion sorting algorithm."""
    for idx in range(len(itr)):
        while idx > 0 and itr[idx] < itr[idx - 1]:
            itr[idx], itr[idx - 1] = itr[idx - 1], itr[idx]
            idx -= 1
    return itr


if __name__ == "__main__":
    from timeit import Timer
    cmd1 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(10000):\n" +
        "    pile_of_crap.append(rand.random())\n" +
        "insertion_sort(pile_of_crap)"
    )
    timer = Timer(stmt=cmd1, setup="from __main__ import insertion_sort")
    print("Sort 10000 random numbers: ", timer.timeit(1))

    timer = Timer(stmt="insertion_sort(range(1000))", setup="from __main__ import insertion_sort")
    print("Sort 1000 ordered numbers: ", timer.timeit(1))

    timer = Timer(stmt="insertion_sort(range(1000, 0, -1))", setup="from __main__ import insertion_sort")
    print("Sort 1000 reversed numbers: ", timer.timeit(1))

    cmd2 = "insertion_sort(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'])"
    timer = Timer(stmt=cmd2, setup="from __main__ import insertion_sort")
    print("Sort qwerty alphabet 100000 times: ", timer.timeit(100000))
