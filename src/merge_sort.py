"""Implementation of merge sort algorithm."""


def merge_sort(itr):
    """Sort iterable using merge sort algorithm."""
    new_itr = []
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
