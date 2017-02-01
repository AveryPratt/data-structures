"""Implementation of quick sort algorithm."""


def quick_sort(itr):
    """Sort iterable using quick sort algorithm."""


if __name__ == "__main__":
    from timeit import Timer
    cmd1 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(10000):\n" +
        "    pile_of_crap.append(rand.random())\n" +
        "quick_sort(pile_of_crap)"
    )
    cmd2 = "quick_sort(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'])"
    timer = Timer(stmt=cmd1, setup="from __main__ import quick_sort")
    print("Sort 10000 random numbers: ", timer.timeit(1))
    timer = Timer(stmt=cmd2, setup="from __main__ import quick_sort")
    print("Sort qwerty alphabet 100000 times: ", timer.timeit(100000))
