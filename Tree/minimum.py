# Approach is to use in-order traversal (DFS) to find the minimum value recursively
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

def find_min_value(node):
    if node is None:
        return float('inf')  # Return positive infinity as the base case

    left_min = find_min_value(node.left)
    right_min = find_min_value(node.right)

    return min(node.data, left_min, right_min)

# Create nodes and initialize
a = Node(34)
b = Node(24)
c = Node(0)
d = Node(1)
e = Node(56)
f = Node(-1)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

min_value = find_min_value(a)
print("Minimum value:", min_value)
