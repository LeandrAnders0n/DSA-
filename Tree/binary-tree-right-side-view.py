#Question:199. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#Approach:
# The rightmost node is obtained during the level-order traversal (BFS) of the binary tree. The code maintains a queue to process nodes level by level. Within each level, the for loop iterates through all nodes in that level, and the condition `if i == level_size - 1` checks if the current node is the last one in the level (i.e., the rightmost node). If it is, the value of that node (`current.val`) is appended to the `right_nodes` list. This ensures that only the rightmost node at each level is added to the final result, representing the right side view of the binary tree.

# Time and Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        queue = [root]
        right_nodes = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current = queue.pop(0)

                if i == level_size - 1:
                    right_nodes.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return right_nodes
