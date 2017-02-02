"""Implementation of radix sort algorithm."""


def radix_sort(itr, base=10):
    """Sort iterable using radix sort algorithm."""
    rng = range(base)
    divisor = base
    try:
        for times in range(max(itr) // divisor + 1):
            buckets = []
            for b in range(base):
                buckets.append([])
            for item in itr:
                idx = (item % divisor) // (base ** (times + 1))
                try:
                    buckets[idx].append(item)
                except IndexError:
                    import pdb; pdb.set_trace()
            itr = []
            for bucket in buckets:
                itr.extend(bucket)
            divisor *= base
    except ValueError:
        pass
    return itr


if __name__ == "__main__":
    from timeit import Timer
    cmd1 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(10000):\n" +
        "    pile_of_crap.append(rand.randint(0, 10000))\n" +
        "radix_sort(pile_of_crap)"
    )
    cmd2 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(10000):\n" +
        "    pile_of_crap.append(rand.randint(0, 1000))\n" +
        "radix_sort(pile_of_crap, 2)"
    )
    cmd3 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(1000000):\n" +
        "    pile_of_crap.append(rand.randint(0, 1000000))\n" +
        "radix_sort(pile_of_crap, 100000)"
    )
    cmd4 = "radix_sort([ord('q'), ord('w'), ord('e'), ord('r'), ord('t'), ord('y'), ord('u'), ord('i'), ord('o'), ord('p'), ord('a'), ord('s'), ord('d'), ord('f'), ord('g'), ord('h'), ord('j'), ord('k'), ord('l'), ord('z'), ord('x'), ord('c'), ord('v'), ord('b'), ord('n'), ord('m')])"
    # timer = Timer(stmt=cmd1, setup="from __main__ import radix_sort")
    # print("Sort 10000 random numbers base 10: ", timer.timeit(1))
    # timer = Timer(stmt=cmd2, setup="from __main__ import radix_sort")
    # print("Sort 10000 random numbers base 2: ", timer.timeit(1))
    timer = Timer(stmt=cmd3, setup="from __main__ import radix_sort")
    print("Sort 10000 random numbers base 10000: ", timer.timeit(1))

    # timer = Timer(stmt=cmd4, setup="from __main__ import radix_sort")
    # print("Sort qwerty alphabet 100000 times: ", timer.timeit(100000))
