"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def exp_iterative(a, n):
    base = a
    for i in range(n - 1):
        a *= base
    return a


def exp_recursive(a, n):
    if n == 1:
        return a
    else:
        return exp_recursive(a, n - 1) * a


assert exp_iterative(5, 3) == 125
assert exp_iterative(2, 4) == 16
assert exp_iterative(1, 19) == 1
assert exp_iterative(0, 2) == 0

assert exp_recursive(5, 3) == 125
assert exp_recursive(2, 4) == 16
assert exp_recursive(1, 19) == 1
assert exp_recursive(0, 2) == 0
