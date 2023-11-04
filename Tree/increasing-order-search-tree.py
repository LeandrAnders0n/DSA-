#Question:897. Increasing Order Search Tree
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

#Approach:
# Use in-order traversal to iterate through the tree, cutting off left subtrees, linking nodes in ascending order, and creating a new tree with the leftmost node as the root and each node having no left child and only one right child. The modified tree is returned.

#Time and Space Complexity:O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root):
        def inorder_traversal(node):
            if node is not None:
                inorder_traversal(node.left)
                node.left = None
                self.current.right = node
                self.current = node
                inorder_traversal(node.right)
        
        # Create a dummy node to serve as the new root
        dummy = TreeNode()
        self.current = dummy
        
        # Perform in-order traversal and reconstruct the tree
        inorder_traversal(root)
        
        return dummy.right

