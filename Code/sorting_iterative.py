#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
        Were `n` is the number of items in the given list `items`
        Running time: O(n), when the list is already sorted
        Memory usage: O(1), in all cases"""
    limit = len(items)

    if limit < 2:
        return True

    for i in range(1, limit):
        if items[i-1] > items[i]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2), Reversed order worst case
    Memory usage: O(1), under all conditions"""
    limit = len(items)

    if limit < 2:
        return True

    while True:  # O(n)
        swapped = False
        for i in range(1, limit):  # O(n)
            if items[i] < items[i - 1]:
                # Swap the items
                items[i - 1], items[i] = items[i], items[i - 1]
                swapped = True
        limit -= 1
        if not swapped:
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) Under all conditions
    Memory usage: O(1) Under all conditions"""
    limit = len(items)

    if limit < 2:
        return True

    start = 0
    while start + 1 < limit:
        min_dex = start
        to_swap = False
        for i in range(start, limit):
            if items[i] < items[min_dex]:
                min_dex = i
                to_swap = True
        if to_swap:
            # Swap the items
            items[start], items[min_dex] = items[min_dex], items[start]
        start += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) Reverse ordered list
    Memory usage: O(1) Under all conditions"""
    limit = len(items)

    if limit < 2:
        return True

    for i in range(1, limit):
        tmp = items[i]
        to_compare = i
        # Before we reach the begining of the list and
        # while what we have is smaller than prev value
        while to_compare > 0 and items[to_compare - 1] > tmp:
            # Move the prev value up by one
            items[to_compare] = items[to_compare - 1]
            to_compare -= 1  # Then look at the next thing down
        # Put the element in the proper position
        # relative to what we already checked
        items[to_compare] = tmp
