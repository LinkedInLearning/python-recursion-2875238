"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def multiply_recursive(n, a):
    if n == 1:
        return a
    return multiply_recursive(n - 1, a) + a


assert multiply_recursive(5, 4) == 20  # 5 is the multiplier, 4 is the multiplicand
assert multiply_recursive(5, -4) == -20  # 5 is the multiplier, -4 is the multiplicand
assert multiply_recursive(1, 4) == 4  # 1 is the multiplier, 4 is the multiplicand
assert multiply_recursive(7, 8) == 56  # 7 is the multiplier, 8 is the multiplicand
