"""
    quick_sort.py

    Implementation of quick sort on a list and returns a sorted list.

    Quick Sort Overview:
    ------------------------
    Uses partitioning to recursively divide and sort the list

    Time Complexity: O(n**2) worst case

    Space Complexity: O(n**2) this version

    Stable: No

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def sort(seq):

    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return sort(left) + [pivot] + sort(right)
