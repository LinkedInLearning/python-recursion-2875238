"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
import sys

# Add parent directory to Python path. Use '..' for Windows.
sys.path.insert(0, './') 
from trace_recursion import trace


def factorial(n):
    if n <= 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)


factorial = trace(factorial)
factorial(5)
