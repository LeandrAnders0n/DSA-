#Question:129. Sum Root to Leaf Numbers
# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

#Approach: Depth-First Search (DFS)
# Calculate the sum of numbers formed by root-to-leaf paths in a binary tree using Depth-First Search (DFS). The recursive `dfs` function updates the path by multiplying it by 10 and adding the current node's value. If it reaches a leaf node, it returns the calculated path. The main method initiates the DFS with the root and zero as the starting path, providing the final sum.

# Time and Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:      
        def dfs(root, path):
            if not root:
                return 0
            path = path*10 + root.val
            if not root.left and not root.right:
                return path
            return dfs(root.left, path) + dfs(root.right, path)

        return dfs(root, 0)

