# Approach is to use BFS and check if element exists
class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

def breadth_first_travel(node, target):
    if node is None:
        return False

    queue = []
    queue.append(node)

    while queue:
        current = queue.pop(0)
        if current.data == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

# Create nodes and initialize
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

target = 'e'
if breadth_first_travel(a, target):
    print(f"Node '{target}' exists.")
else:
    print(f"Node '{target}' does not exist.")

print("Time: O(n)")
print("Space: O(n)")
