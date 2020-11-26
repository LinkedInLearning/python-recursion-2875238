"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def count_down(n):
    print(n)
    if n == 0:
        # Base case
        print('Algorithm has hit the base case. Time to unwind.')
        return
    else:
        # Recursive case
        count_down(n - 1)
        print(n)
        return


count_down(3)
