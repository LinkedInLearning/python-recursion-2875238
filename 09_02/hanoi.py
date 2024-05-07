"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
import sys

# Add parent directory to Python path. Use '..' for Windows.
sys.path.insert(0, './') 
from trace_recursion import trace


def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    towers_of_hanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    towers_of_hanoi(n - 1, auxiliary, destination, source)


n = 3
towers_of_hanoi = trace(towers_of_hanoi)
# A, C, B are the names of the rods.
# They correspond to source, destination, auxiliary
towers_of_hanoi(n, 'A', 'C', 'B')
