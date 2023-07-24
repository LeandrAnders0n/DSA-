#Question:Range Sum of BST
#Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

#Approach:The code implements an iterative depth-first search (DFS) approach using a stack to traverse the binary search tree (BST). It calculates the sum of all node values in the BST that fall within the given range [low, high]
# Time and Space Complexity: O(N)


# Definition for a binary tree node.
# class Node():
#     def __init__(self,val):
#         self.left=None
#         self.right=None
#         self.val=val

def rangeSumBST(low,high,root):
    if root is None:
        return
    stack=[]
    total_sum=0
    stack.append(root)
    while stack:
        current=stack.pop()
        if low<=current.val<=high:
            total_sum+=current.val
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return total_sum