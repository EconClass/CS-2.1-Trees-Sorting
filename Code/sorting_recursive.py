#!python

from sorting_iterative import insertion_sort, bubble_sort


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
    bubble_sort(right)  # O(n^2)

    # Merge sorted halves into one list in sorted order
    # Overwrite content of original list with content of sorted list
    items[:] = merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n*2*log(n)) -> O(n*log(n))
        Same runtime in all cases
        We are continuously iterating through half of the given list
        With each successive call's given list shrinks by half
    Memory usage: O(n)
        We create a sorted copy of the given list at every function call
        except for the call at the base case
        In the worst case the sorted copy is equal to the original in size"""

    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:  # O(1)
        return items

    # Split items list into approximately equal halves
    middle = len(items) // 2
    left = items[:middle]  # O(n/2)
    right = items[middle:]  # O(n/2)

    # Sort each half by recursively calling merge sort
    left = merge_sort(left)  # O(n/2) -> O(l)
    right = merge_sort(right)  # O(n/2) -> O(r)

    # Merge sorted halves into one list in sorted order
    # Overwrite content of original list with content of sorted list
    items[:] = merge(left, right)  # O(l + r) = O(n/2 + n/2) -> O(n)
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot, which is always the lowest index from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(log(n))
        Each successive partition proportionally reduces
        the number of items to iterate through
    Memory usage: O(1)
        New memory created are constant in all cases"""
    # Choose a pivot any way and document your method in docstring above
    pivot = low
    to_swap = low + 1

    # Loop through all items in range [low...high]
    for i in range(low + 1, high):

        # Move items less than pivot into front of range [low...p-1]
        if items[i] < items[pivot]:

            # Move items greater than pivot into back of range [p+1...high]
            items[to_swap], items[i] = items[i], items[to_swap]
            to_swap += 1

    # Move pivot item into final position [p] and return index p
    items[low], items[to_swap - 1] = items[to_swap - 1], items[low]

    # Return index after in-place partitioning in range [low...high]
    return to_swap - 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n*log(n))
        We make `log(n)` iterations for `n` number of items in a given list
    Worst case running time: O(n^2)
        Quick Sort takes `n` iterations for `n` amount of items if,
        the list is reversed
    Memory usage: O(1)
        We only create references to positions in the given list"""
    # Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low = 0
        high = len(items)
    # Check if list or range is so small it's already sorted (base case)
    delta = high - low
    if delta < 2:
        return
    # Partition items in-place around a pivot and get index of pivot
    piv_dex = partition(items, low, high)

    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, piv_dex)
    quick_sort(items, piv_dex + 1, high)
