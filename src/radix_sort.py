"""Implementation of radix sort algorithm."""


def radix_sort(itr, base=10):
    """Sort iterable using radix sort algorithm."""
    divisor = base
    digit = 0
    try:
        for item in range(max(itr) // divisor + 1):
            buckets = []
            for b in range(base):
                buckets.append([])
            for item in itr:
                idx = item % divisor // base ** digit
                buckets[idx].append(item)
            itr = []
            for bucket in buckets:
                itr.extend(bucket)
            divisor *= base
            digit += 1
    except ValueError:
        pass
    return itr


if __name__ == "__main__":
    from timeit import Timer
    print("sorting...")
    cmd1 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(10000):\n" +
        "    pile_of_crap.append(rand.randint(0, 1000))\n" +
        "radix_sort(pile_of_crap, 2)"
    )
    cmd2 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(10000):\n" +
        "    pile_of_crap.append(rand.randint(0, 1000))\n" +
        "radix_sort(pile_of_crap)"
    )
    cmd3 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(10000):\n" +
        "    pile_of_crap.append(rand.randint(0, 1000))\n" +
        "radix_sort(pile_of_crap, 16)"
    )
    cmd4 = (
        "from random import Random\n" +
        "rand = Random()\n" +
        "pile_of_crap = []\n" +
        "for i in range(1000000):\n" +
        "    pile_of_crap.append(rand.randint(0, 1000000))\n" +
        "radix_sort(pile_of_crap, 100000)"
    )
    timer = Timer(stmt=cmd1, setup="from __main__ import radix_sort")
    print("Sort 10,000 random numbers between 0 and 999 in binary (base 2): ", timer.timeit(1))
    timer = Timer(stmt=cmd2, setup="from __main__ import radix_sort")
    print("Sort 10,000 random numbers between 0 and 999 in decimal (base 10): ", timer.timeit(1))
    timer = Timer(stmt=cmd3, setup="from __main__ import radix_sort")
    print("Sort 10,000 random numbers between 0 and 999 in hexadecimal (base 16): ", timer.timeit(1))
    timer = Timer(stmt=cmd4, setup="from __main__ import radix_sort")
    print("Sort 1,000,000 random numbers between 0 and 999,999 in base 100,000: ", timer.timeit(1))
