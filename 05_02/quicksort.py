"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import sys

sys.path.append("..")  # Adds higher directory to python modules path.
from trace_recursion import trace


def quicksort(arr):
    pass


def quicksort_verbose(arr):
    print(f"Calling quicksort on {arr}")
    if len(arr) <= 1:
        print(f"returning {arr}")
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    print(f"left: {left}; ", end="")
    middle = [x for x in arr if x == pivot]
    print(f"middle: {middle}; ", end="")
    right = [x for x in arr if x > pivot]
    print(f"right: {right}")
    to_return = quicksort_verbose(left) + middle + quicksort_verbose(right)
    print(f"returning: {to_return}")
    return to_return


data = [5, 2, 6, 1]
# print(quicksort(data))
# print(quicksort_verbose(data))

# quicksort = trace(quicksort)
# quicksort(data)
#

# What about data with duplicates?
# data = [1, 6, 5, 5, 2, 6, 1]
# print(quicksort(data))

# for challenge
data = [5, 4, 3, 2, 1]
print(quicksort_verbose(data))
