#Question:103. Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

#Approach:
# Perform a zigzag level order traversal of a binary tree. Use a breadth-first search (BFS) approach with a queue to traverse the tree nodes. The `level` variable is used to determine the order of adding values to the result list, alternating between left-to-right and right-to-left for each level. The result is a list of lists containing the values of nodes in zigzag order.

# Time and Space Complexity: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [root]
        level = 0

        while queue:
            level_values = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)

                # Determine the order in which values should be added based on the level
                if level % 2 == 0:
                    level_values.append(node.val)
                else:
                    level_values = [node.val] + level_values

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)
            level += 1

        return result