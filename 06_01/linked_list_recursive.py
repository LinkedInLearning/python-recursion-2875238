"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def traverse(head):
    # Base case
    if head is None:
        return
    # Recursive case
    print(head.data)
    traverse(head.next)


item1 = Node("dog")
item2 = Node("cat")
item3 = Node("rat")
item1.next = item2
item2.next = item3

# traverse(item1)

head = Node("dog", Node("cat", Node("rat", None)))
traverse(head)
