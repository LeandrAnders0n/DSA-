#Question:617. Merge Two Binary Trees
# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.

#Approach:
# Merge trees by adding corresponding node values. If one of the nodes is `None`, return the other. This method recursively merges the left and right subtrees. The merged tree is returned as the result.
# Time and Space Complexity: O(n)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        root1.val+=root2.val
        root1.left=self.mergeTrees(root1.left,root2.left)
        root1.right=self.mergeTrees(root1.right,root2.right)

        return root1