#Question: Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

#Approach:
# Use a breadth-first traversal approach, starting with the root node. Use a deque (double-ended queue) for efficient node processing. 
# For each level, find the sum and count of nodes at that level, and calculate the average by dividing the sum by the count. The averages are stored in a list called `averages`. 
# Time and Space Complexity: O(n)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def average_of_levels(root):
    if root is None:
        return []
    averages = []
    queue = deque([root])
    while queue:
        level_sum = 0
        level_count = len(queue)
        for _ in range(level_count):
            current = queue.popleft()
            level_sum += current.val
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        averages.append(level_sum / level_count)
    return averages

root = [3,9,20,None,None,15,7]
print(average_of_levels(root))
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

root = [3,9,20,15,7]
print(average_of_levels(root))
# Output: [3.00000,14.50000,11.00000]