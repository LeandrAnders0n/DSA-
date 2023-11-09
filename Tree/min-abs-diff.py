#Question: 530. Minimum Absolute Difference in BST
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

#Approach:In Order Traversal
# Use an inorder traversal (`inorder_traversal`) to visit nodes in ascending order, updating the minimum difference (`min_diff`) as it iterates through the tree. The `prev` variable keeps track of the previously visited node's value. The final result is the minimum absolute difference found during the traversal.

# Time Complexity: O(n)
# Space Complexity: O(h)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root):
        def inorder_traversal(node):
            nonlocal prev,min_diff
            if not node:
                return
            inorder_traversal(node.left)

            if prev is not None:
                min_diff=min(min_diff,node.val-prev)
            
            prev=node.val

            inorder_traversal(node.right)

        prev=None
        min_diff=float('inf')
        inorder_traversal(root)
        return min_diff