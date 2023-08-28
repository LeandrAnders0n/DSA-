#Question: Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

#Approach: Use recursion along with DFS 
# Check if there's a path from the root of a binary tree to a leaf node, where the sum of node values along the path equals a given `targetSum`. Use depth-first search (DFS) recursively to traverse the tree, adding the values of nodes along the path. If a leaf node is reached, check if the sum matches the `targetSum`. 

# Time Complexity: O(N), where N is the number of nodes
# Space Complexity: O(H), where H is the height of the binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root,targetSum):
        def dfs(node,s):
            if not node:
                return
            s += (node.val)
            if node.left is None and node.right is None:
                if s == targetSum:
                    return True
            return dfs(node.left,s) or dfs(node.right,s)
        return dfs(root,0)
