#!/usr/bin/env python3

from random import shuffle


def shuflist(size):
    """Creates a randomised list of numbers for sorting."""
    nums = [i for i in range(1, size + 1)]
    shuffle(nums)
    print(nums)
    return nums


def quicksort(obj):
    """Sorts obj using a quicksort algorithm"""
    partitions = [obj]
    while len(partitions) != len(obj):
        part_update = []

        # Splits each partition into new parts using first value as pivot.
        for partition in partitions:
            new_parts = [[], [], []]
            
            # Prevents sorting parts with only one value.
            if len(partition) == 1:
                part_update.append(partition)
                continue
            else:
                pivot = partition.pop(0)
                new_parts[1].append(pivot)

            # Sorts partition into new_parts.
            for i in partition:
                if i <= pivot:
                    new_parts[0].append(i)
                elif i > pivot:
                    new_parts[2].append(i)
                else:
                    pass

            for i in new_parts:
                if len(i) >= 1:
                    part_update.append(i)
                else:
                    pass
        partitions = part_update

    qsout = [partitions[i][0] for i in range(len(partitions))]
    return qsout


print(quicksort(shuflist(100)))
