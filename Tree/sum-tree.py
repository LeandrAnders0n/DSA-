# Approach is to solve it recursively with DFS
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def calculate_sum(root):
    if root is None:
        return 0
    #recursively add the child nodes
    return root.data + calculate_sum(root.left) + calculate_sum(root.right)

a = Node(10)
b = Node(10)
c = Node(10)
d = Node(10)
e = Node(10)
f = Node(10)

a.left = b
a.right = c
b.left = d
d.right = e
c.left = f

result = calculate_sum(a)
print("Sum:", result)
