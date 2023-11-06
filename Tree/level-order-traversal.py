#Question:102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Time Complexity:O(N)
# Space complexity:O(W), where W is the maximum width (number of nodes in the widest level) of the binary tree

#Approach:
# Perform a level-order traversal of a binary tree, returning a list of lists where each inner list contains the values of nodes at a specific level. Use a queue to traverse the tree level by level, appending the values to the `level` list.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return
        
        queue=[root]
        level=[]

        while queue:
            level_len=len(queue)
            current_level=[]
            for i in range(level_len):
                current=queue.pop(0)
                current_level.append(current.val)

                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)

            level.append(current_level)
        return level



















