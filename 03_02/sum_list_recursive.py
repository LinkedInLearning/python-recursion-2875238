"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def list_sum(a_list):
    result = 0
    for val in a_list:
        result += val
    return result


def list_sum_recursive(a_list):
    if len(a_list) == 0:
        return 0
    return a_list[0] + list_sum_recursive(a_list[1:])


assert list_sum([2, 3, 5, 7]) == 17
assert list_sum([-4, -3, -2, -1, 10]) == 0

assert list_sum_recursive([2, 3, 5, 7]) == 17
assert list_sum_recursive([-4, -3, -2, -1, 10]) == 0
assert list_sum_recursive([]) == 0
assert list_sum_recursive([3]) == 3
assert list_sum_recursive([-5, -3]) == -8
