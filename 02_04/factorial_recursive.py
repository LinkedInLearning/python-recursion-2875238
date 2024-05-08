"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def factorial(n):
    if n <= 1:
        # Base case
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)


print(factorial(4))
print(factorial(6))
print(factorial(1))
print(factorial(0))
print(factorial(-7))
print(factorial(1000))  # RecursionError: maximum recursion depth exceeded in comparison
