#Questoin: 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

#Approach: In Order Traversal
# Use an in-order traversal (`inOrderTraversal`) with recursively checks for each node. The `lower` and `upper` parameters maintain the valid range for node values. If the current node's value violates the BST property, the function returns `False`. The `isValidBST` method initiates the traversal from the root and returns the result of the in-order traversal, indicating whether the entire tree is a valid BST.

# Time Complexity:O(n)
# Space Complexity:O(h)

class Solution:
    def isValidBST(self, root):
        def inOrderTraversal(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            # Check the left subtree
            if not inOrderTraversal(node.left, lower, node.val):
                return False

            # Check the current node's value
            if not lower < node.val < upper:
                return False

            # Update the lower bound for the right subtree
            lower = node.val

            # Check the right subtree
            return inOrderTraversal(node.right, lower, upper)

        return inOrderTraversal(root)
