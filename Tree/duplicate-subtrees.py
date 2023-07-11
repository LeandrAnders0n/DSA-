#Question:Find Duplicate Subtrees
# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.

#Approach:
# Using a bottom-up traversal to serialize each subtree in a binary tree and check for duplicate subtrees by counting the serialized representations.
# Identify duplicates based on the serialized representations stored in a dictionary.

# Time complexity: O(N^2)
# Space complexity: O(N) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count_map = {}
        result = []

        def traverse(node):
            if not node:
                return "#"

            left_serial = traverse(node.left)
            right_serial = traverse(node.right)

            # Serialize the current subtree
            subtree_serial = str(node.val) + "," + left_serial + "," + right_serial

            # Update the count of subtree serialization
            count_map[subtree_serial] = count_map.get(subtree_serial, 0) + 1

            # If count is 2, it means it is a duplicate subtree
            if count_map[subtree_serial] == 2:
                result.append(node)

            return subtree_serial

        traverse(root)  

        return result


