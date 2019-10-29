#!python

from sorting_iterative import insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m)
        We have to iterate through all items in both lists in any scenario
    Memory usage: O(n + m)
        New memory is created to store new ordered list
        New ordered list grows until it contains all items from both inputs"""
    head1 = 0
    head2 = 0
    final = []

    # Repeat until one list is empty
    while head1 < len(items1) and head2 < len(items2):
        # Find minimum item in both lists and append it to new list
        small_1 = items1[head1]
        small_2 = items2[head2]
        if small_1 < small_2:
            final.append(small_1)
            head1 += 1
        else:
            final.append(small_2)
            head2 += 1

    # Append remaining items in non-empty list to new list
    while head1 < len(items1):
        final.append(items1[head1])
        head1 += 1

    while head2 < len(items2):
        final.append(items2[head2])
        head2 += 1

    return final


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O((n/2)^2) -> O(n^2)
        When the left and right halves are in reverse order
    Memory usage: O(n)
        New memory is created to store new ordered list"""
    # Split items list into approximately equal halves
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]

    # Sort each half using any other sorting algorithm
    insertion_sort(left)  # O(n^2)
    insertion_sort(right)  # O(n^2)

    # Merge sorted halves into one list in sorted order
    merged = merge(left, right)

    assert len(items) == len(merged)
    # Overwrite content of original list with content of sorted list
    for i in range(len(items)):
        items[i] = merged[i]


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return items

    # Split items list into approximately equal halves
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]

    # Sort each half by recursively calling merge sort
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge sorted halves into one list in sorted order
    merged = merge(left, right)

    # Overwrite content of original list with content of sorted list
    for i in range(len(items)):
        items[i] = merged[i]
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
