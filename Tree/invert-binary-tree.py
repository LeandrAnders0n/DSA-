# Question:Invert Binary Tree
# Given the root of a binary tree, invert the tree, and return its root.
#Approach:The invert_tree function takes the root node of the binary tree as input and recursively inverts the tree by swapping the left and right child nodes at each level.
#Time and Space Complexity:O(n)

class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    

a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')
g=Node('g')

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g

def dfs(a):
    if a is None:
        return
    stack=[]
    stack.append(a)

    while stack:
        current=stack.pop()
        yield current.value

        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)

def invert_tree(root):
    if root is None:
        return
    
    root.left,root.right=root.right,root.left

    invert_tree(root.left)
    invert_tree(root.right)
    return root


print("Binary Tree: ")
print(list(dfs(a)))
print("Inverted Tree: ")
new_root=invert_tree(a)
print(list(dfs(new_root)))














