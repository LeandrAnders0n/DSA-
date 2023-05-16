#Approach is to use a Stack
#Traverse the tree from root to node, check if each node has a child, and add them. After every iteration, check if the node has a child node.
#Pop the elements of the stack and continue iterating until you reach the end.
#Time: O(n)
#Space: O(n)

class Node():
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

def dfs(node):
    if node is None:
        return
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        print(current.val)
        
        if current.left:
            stack.append(current.left)

        if current.right:
            stack.append(current.right)


a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

dfs(a)