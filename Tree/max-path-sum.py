#Question:Given a binary tree, find the maximum path sum.
#Approach:The code finds the maximum sum path in a binary tree by recursively calculating the maximum sum of the left and right subtrees and choosing the path with the higher sum. 
#Time Complexity is O(n), where n is the number of nodes in the tree
#Space Complexity is O(h), where h is the height of the tree.

# Find the maximum path value from the root to leaf using DFS
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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

def max_path(node):
    if node is None:
        return 0
    
    if node.right is None and node.left is None:
        return node.data
    
    left_max=max_path(node.left)
    right_max=max_path(node.right)

    return max(left_max,right_max)+node.data


max_path_value=max_path(a)
print("Maximum path value:", max_path_value)
