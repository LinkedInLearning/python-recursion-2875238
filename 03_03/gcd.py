"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
import sys
from trace_recursion import trace

sys.path.append("..")  # Adds higher directory to python modules path.


def gcd_recursive(a, b):
    if b == 0:
        # Base case
        return a
    else:
        # Recursive case
        return gcd_recursive(b, a % b)


gcd_recursive = trace(gcd_recursive)
print(gcd_recursive(32, 12))  # From slides
print(gcd_recursive(50, 15))
print(gcd_recursive(42, 28))
print(gcd_recursive(28, 42))
print(gcd_recursive(345, 766))  # Co-prime
