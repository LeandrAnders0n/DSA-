# Question: Same TreeGiven the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#Approach:The code checks if two binary trees, represented by p and q, are identical. It uses a stack-based approach to traverse the trees simultaneously. 
# It compares the values of corresponding nodes and their children, returning False if any mismatch is found, and True if the traversal completes without finding any differences.

# Time Complexity: O(n)
# Space Complexity: O(h)


class Node():
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

p=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')

q=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')

p.left=b
p.right=c
b.left=d
b.right=e
c.left=f       

q.left=b
q.right=c
b.left=d
b.right=e
c.left=f    

def isSameTree(p,q):
    if p is None and q is None:
        return True
    p_stack=[]
    q_stack=[]
    p_stack.append(p)
    q_stack.append(q)
    while p_stack and q_stack:
        p_current=p_stack.pop()
        q_current=q_stack.pop()
        if p_current is None and q_current is None:
            continue
        if p_current is None or q_current is None:
            return False
        if p_current.val != q_current.val:
            return False
        p_stack.append(p_current.left)
        q_stack.append(q_current.left)
        p_stack.append(p_current.right)
        q_stack.append(q_current.right)
    return True

print(isSameTree(p,q))        