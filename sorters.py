#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01: Implement a Selection Sort"""

import random


def selection(iterable):
    """selection sort algorithm"""

    for cur_pos in range(len(iterable)):
        min_pos = cur_pos

        for scan_pos in range(cur_pos, len(iterable)):
            if iterable[scan_pos] < iterable[min_pos]:
                min_pos = scan_pos

        temp = iterable[min_pos]
        iterable[min_pos] = iterable[cur_pos]
        iterable[cur_pos] = temp

    return iterable


def print_list(sort_list):
    """print sorted list"""

    for item in sort_list:
        print "{:3}".format(item)
    print()


def quick(iterable):
    """quick sort algorithm"""

    less = []
    equal = []
    greater = []

    if len(iterable) > 1:
        pivot = iterable[0]
        for num in iterable:
            if num < pivot:
                less.append(num)
            if num == pivot:
                equal.append(num)
            if num > pivot:
                greater.append(num)

        return quick(less) + equal + quick(greater)

    else:
        return iterable


if __name__ == "__main__":

    VAR_LIST = []
    for var in range(10):
        VAR_LIST.append(random.randrange(100))
    print_list(VAR_LIST)
    selection(VAR_LIST)
    print_list(VAR_LIST)

    QUICK = [10, 1, 9, 2, 4, 3, 8, 6, 5, 7]
    print quick(QUICK)
