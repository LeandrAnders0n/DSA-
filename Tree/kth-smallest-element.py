#Question:230. Kth Smallest Element in a BST
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

#Approach: Inorder Traversal
# Find the kth smallest element in a binary search tree (BST) using an inorder traversal. The `inorder_traversal` function recursively explores the left subtree, decrements the counter `k`, and returns the value of the kth smallest element when `k` becomes 0. If the element is not found in the left subtree, the function explores the right subtree. The method returns the result of the initial call to `inorder_traversal` on the BST's root.

# Time and Space Complexity: O(H)

class Solution:
    def kthSmallest(self, root, k):
        def inorder_traversal(node):
            nonlocal k
            if not node:
                return None

            result = inorder_traversal(node.left)
            if result is not None:
                return result

            k -= 1
            if k == 0:
                return node.val

            return inorder_traversal(node.right)

        return inorder_traversal(root)
