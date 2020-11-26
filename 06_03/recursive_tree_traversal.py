"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


class Node(object):
    pass


def preorder_print(root, path=""):
    """Root->Left->Right"""
    pass


def inorder_print(root, path=""):
    """Left->Root->Right"""
    pass


def postorder_print(root, path=""):
    """Left->Right->Root"""
    pass


if __name__ == '__main__':
    # Set up tree:
    root = Node("F")
    root.left = Node("D")
    root.left.left = Node("B")
    root.left.left.left = Node("A")
    root.left.left.right = Node("C")
    root.left.right = Node("E")
    root.right = Node("I")
    root.right.left = Node("G")
    root.right.left.right = Node("H")
    root.right.right = Node("J")

print("Preorder:", preorder_print(root))
print("Inorder:", inorder_print(root))
print("Postorder", postorder_print(root))

r"""
          ______F______
         /             \
      __D__           __I__
     /     \         /     \
    B       E       G       J
   / \               \
  A   C               H
"""
