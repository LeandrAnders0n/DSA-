#Approach is to use a Queue
#Add each node and child node to the queue, in a sequential order.
#Pop the first item of the queue, print it and append if it has any child nodes. Continue this process till the end.
#Time: O(n)
#Space: O(n)

class Node():
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

def bfs(node):
    if node is None:
        return
    queue=[]
    queue.append(node)
    while queue:
        current=queue.pop(0)
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

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
c.left=f

bfs(a)










