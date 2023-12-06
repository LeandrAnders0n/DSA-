#Question:110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.

#Approach:The code recursively determines if a binary tree is balanced by comparing the heights of its left and right subtrees. If the difference exceeds 1 at any node or if any subtree is unbalanced, it returns -1. 
# Time complexity is O(n), where n is the number of nodes
# Space complexity is O(h), where h is the height of the tree due to recursion.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            
            right_height = height(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1 

            return 1 + max(left_height, right_height)

        return height(root)!=-1