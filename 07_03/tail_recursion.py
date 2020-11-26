"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import inspect


def factorial(n):
    print("Non tail optimised stack size: ", len(inspect.stack(0)))
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def tail_factorial_attempt(n, accumulator=1):
    print("Attempted tail optimised stack size: ", len(inspect.stack(0)))
    pass


if __name__ == "__main__":
    print(factorial(5))
    print(tail_factorial_attempt(5))
