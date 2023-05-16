# Find the maximum path value from the root to leaf using DFS
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def max_path(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return node.data

    left_max = max_path(node.left)
    right_max = max_path(node.right)

    return max(left_max, right_max) + node.data

# Create nodes and initialize
a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
d.right = e
c.left = f

max_path_value = max_path(a)
print("Maximum path value:", max_path_value)
