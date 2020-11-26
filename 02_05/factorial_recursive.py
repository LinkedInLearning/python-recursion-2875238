"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
import sys
from trace_recursion import trace

sys.path.append("..")  # Adds higher directory to python modules path.


def factorial(n):
    if n <= 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)


factorial = trace(factorial)
print(factorial(5))
