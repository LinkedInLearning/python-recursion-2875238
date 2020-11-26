"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import sys


def factorial(n):
    if n <= 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)


# print(sys.getrecursionlimit())  # 1000 is default
# print(factorial(1000))  # RecursionError: maximum recursion depth exceeded in comparison
sys.setrecursionlimit(1002)
print(sys.getrecursionlimit())
print(factorial(1000))
