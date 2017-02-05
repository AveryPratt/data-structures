"""Implementation of merge sort algorithm."""


def merge_sort(itr):
    """Sort iterable using merge sort algorithm."""
    new_itr = []
    print(len(itr))
    if len(itr) > 1:
        pile1 = merge_sort(itr[:len(itr) // 2])
        pile2 = merge_sort(itr[len(itr) // 2:])
        while len(pile1) > 0 and len(pile2) > 0:
            if pile1[0] > pile2[0]:
                new_itr.append(pile2[0])
                pile2 = pile2[1:]
            else:
                new_itr.append(pile1[0])
                pile1 = pile1[1:]
        return new_itr + pile1 + pile2
    else:
        return itr


if __name__ == "__main__":
    from timeit import Timer
    cmd1 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(1000000):\n" +
        "    pile_of_crap.append(rand.random())\n" +
        "merge_sort(pile_of_crap)"
    )
    cmd2 = "merge_sort(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'])"
    timer = Timer(stmt=cmd1, setup="from __main__ import merge_sort")
    print("Sort 10000 random numbers: ", timer.timeit(1))
    timer = Timer(stmt=cmd2, setup="from __main__ import merge_sort")
    print("Sort qwerty alphabet 100000 times: ", timer.timeit(100000))
